# Sky and Stone: Erreichbarkeits-Check (Heuristik, keine Spielsimulation).
# Prüft, ob jede Pflicht-Quest über ihre Abhängigkeiten erreichbar ist und ob jede
# Aufgaben-Item-ID aus Startwelt und Rezepten herstellbar ist.
# Ergebnis ist ein Prüfbericht: Befunde müssen von Hand geprüft werden. Es ist kein Beweis.
#
# Aufruf: python -I -X utf8 _src/erreichbar.py <dev_recipejson.json> <dev_tags.json>
#   dev_recipejson.json: Testserver, Dump aus zz_dev_recipejson.js
#   dev_tags.json: Testserver, kubejs/dev_tags.json
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import snbt  # noqa: E402

CHAPTERS = os.path.join(HERE, '..', 'config', 'ftbquests', 'quests', 'chapters')
LANG = os.path.join(HERE, '..', 'config', 'ftbquests', 'quests', 'lang', 'de_de.snbt')

# Annahme: Was auf der Startinsel und im Startinventar liegt (ohne Fluids).
# Lava- und Wassereimer sind seit 26.10.2026 nicht mehr im Startinventar. Der Bruchstein-Generator
# kommt nach dem Eisen (Quest „Bruchstein-Generator“, Eimer aus Eisen).
START_WORLD = [
    'minecraft:oak_log', 'minecraft:oak_leaves', 'minecraft:oak_sapling', 'minecraft:dirt',
    'minecraft:grass_block', 'minecraft:sand', 'minecraft:gravel', 'minecraft:cobblestone',
    'minecraft:torch', 'minecraft:bread',
    'minecraft:string', 'minecraft:stick', 'minecraft:oak_planks',
    'ftbquests:book', 'exdeorum:wooden_watering_can',
]

# Weltquellen: Items, die keine Rezepte haben, sondern aus Mob-Drops, Ernte, Bossen oder Truhen kommen.
# Annahme, im Spiel zu prüfen. Sie werden im Bericht getrennt ausgewiesen.
WELT_QUELLEN = {
    'minecraft:wheat': 'Ernte vom Feld',
    'minecraft:egg': 'Huhn-Drop',
    'minecraft:leather': 'Kuh-Drop',
    'minecraft:honeycomb': 'Bienenstock oder Wabe',
    'minecraft:rotten_flesh': 'Zombie-Drop',
    'minecraft:bone': 'Skelett-Drop',
    'minecraft:blaze_rod': 'Lohe-Drop (Nether)',
    'minecraft:nether_star': 'Wither-Boss',
    'minecraft:dragon_egg': 'Enderdrache',
    'minecraft:wither_skeleton_skull': 'Wither-Skelett',
    'minecraft:bee_spawn_egg': 'Sieb oder Kreativ',
    'minecraft:ender_pearl': 'Enderman-Drop',
}

ID_RE = re.compile(r'^[a-z0-9_.-]+:[a-z0-9_./-]+$')
RESULT_KEYS = ('result', 'results', 'output', 'outputs')
FLUID_RE = re.compile(r'fluid|chemical|gas|infus|slurry|pigment', re.IGNORECASE)
INPUT_KEYS = ('ingredient', 'ingredients', 'key', 'inputs', 'input', 'mesh', 'tool')


def load_quests():
    quests = {}
    lang = {}
    txt = open(LANG, encoding='utf-8').read()
    for m in re.finditer(r'^\s*quest\.([0-9A-F]+)\.title:\s*"((?:[^"\\]|\\.)*)"', txt, re.M):
        lang[m.group(1)] = m.group(2)
    for f in sorted(glob.glob(os.path.join(CHAPTERS, '*.snbt'))):
        d = snbt.load(f)
        for q in d.get('quests', []):
            tasks = []
            for t in q.get('tasks', []) or []:
                it = t.get('item')
                if isinstance(it, dict) and isinstance(it.get('id'), str):
                    tasks.append(it['id'].lstrip('#'))
                elif isinstance(it, str):
                    tasks.append(it.lstrip('#'))
            quests[q['id']] = {
                'deps': q.get('dependencies', []) or [],
                'tasks': tasks,
                'title': lang.get(q['id'], q['id']),
                'optional': bool(q.get('optional')),
                'chap': os.path.basename(f),
            }
    return quests


def result_ids(node, out):
    """Item-IDs unterhalb der Ergebnis-Schlüssel."""
    if isinstance(node, dict):
        for k, v in node.items():
            result_ids(v, out)
    elif isinstance(node, list):
        for v in node:
            result_ids(v, out)
    elif isinstance(node, str) and ID_RE.match(node):
        out.add(node)


def ingredient_groups(node, groups, depth=0):
    """Jede Zutat wird zu einer Menge alternativer Items oder Tags."""
    if depth > 6:
        return
    if isinstance(node, dict):
        if node.get('type') == 'mysticalagriculture:crop_component':
            # Mystical Agriculture: Essenz einer Pflanze ist ein Item, Material wird hier nicht modelliert
            if node.get('component') == 'essence' and isinstance(node.get('crop'), str):
                groups.append({node['crop'].split(':')[0] + ':' + node['crop'].split(':')[1] + '_essence'})
            return
        if 'item' in node or 'tag' in node:
            alts = set()
            if isinstance(node.get('item'), str):
                alts.add(node['item'])
            if isinstance(node.get('tag'), str):
                alts.add('#' + node['tag'])
            if alts:
                groups.append(alts)
            return
        for k, v in node.items():
            if k in INPUT_KEYS:
                ingredient_groups(v, groups, depth + 1)
            elif k not in RESULT_KEYS and isinstance(v, (dict, list)) and depth > 0:
                # Muster-Zuordnung (Symbol -> Zutat), z. B. shaped key
                ingredient_groups(v, groups, depth + 1)
    elif isinstance(node, list):
        for v in node:
            ingredient_groups(v, groups, depth + 1)


def jar_recipes(mods_dir, dump_ids):
    """Rezepte aus den Mod-Jars (data/<ns>/recipe/*.json), soweit der Dump sie nicht enthält.
    Der Dump lässt Rezepte mit bestimmten Serialisierern aus (siehe fail_types im Dump).
    Rezepte, die Pack-Skripte entfernen, fehlen im Dump und würden hier fälschlich ergänzt."""
    import zipfile
    recs = []
    for jar in sorted(glob.glob(os.path.join(mods_dir, '*.jar'))):
        try:
            z = zipfile.ZipFile(jar)
        except zipfile.BadZipFile:
            continue
        for name in z.namelist():
            m = re.match(r'data/([^/]+)/recipe/(.+)\.json$', name)
            if not m:
                continue
            rid = m.group(1) + ':' + m.group(2)
            if rid in dump_ids:
                continue
            try:
                j = json.loads(z.read(name).decode('utf-8'))
            except (ValueError, UnicodeDecodeError):
                continue
            if isinstance(j, dict):
                recs.append({'id': rid, 'json': j, 'jar': True})
    return recs


def load_recipes(path, mods_dir=None):
    data = json.load(open(path, encoding='utf-8'))
    recs = []
    entries = list(data['recipes'])
    if mods_dir:
        entries += jar_recipes(mods_dir, {r['id'] for r in data['recipes']})
    for r in entries:
        j = r['json']
        if not isinstance(j, dict):
            continue
        res = set()
        groups = []
        for k, v in j.items():
            if k in RESULT_KEYS:
                result_ids(v, res)
            else:
                ingredient_groups({k: v}, groups)
        # Fluid- und Chemikalien-Eingaben kann der Check nicht modellieren: solche Rezepte sind optimistisch
        opt = bool(FLUID_RE.search(json.dumps(j)))
        if res and (groups or opt):
            recs.append({'id': r['id'], 'out': res, 'groups': groups, 'opt': opt})
    return recs


def expand(alts, tags):
    items = set()
    for a in alts:
        if a.startswith('#'):
            items |= tags.get(a[1:], set())
        else:
            items.add(a)
    return items


def simulate(recs, tags, start, optimistic=False):
    have = set(start)
    changed = True
    while changed:
        changed = False
        for r in recs:
            if r['out'] <= have or (r['opt'] and not optimistic):
                continue
            if all(expand(g, tags) & have for g in r['groups']):
                have |= r['out']
                changed = True
    return have


def reachable_quests(quests):
    reach = set()
    changed = True
    while changed:
        changed = False
        for qid, q in quests.items():
            if qid not in reach and all(d in reach or d not in quests for d in q['deps']):
                reach.add(qid)
                changed = True
    return reach


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    raw_tags = json.load(open(sys.argv[2], encoding='utf-8'))
    tags = {k.lstrip('#'): set(v) for k, v in raw_tags.items()}
    mods_dir = sys.argv[3] if len(sys.argv) > 3 else None
    recs = load_recipes(sys.argv[1], mods_dir)
    have = simulate(recs, tags, START_WORLD)
    have_opt = simulate(recs, tags, START_WORLD, optimistic=True)
    quests = load_quests()
    reach = reachable_quests(quests)

    print(f'Rezepte mit Ergebnis: {len(recs)} · herstellbar aus Start: {len(have)} Item-IDs')
    print(f'Quests: {len(quests)} · über Abhängigkeiten erreichbar: {len(reach)}')

    unreach = sorted(q for q in quests if q not in reach and not quests[q]['optional'])
    print(f'\nPflicht-Quests ohne Weg über Abhängigkeiten: {len(unreach)}')
    for q in unreach[:40]:
        print('  -', quests[q]['chap'], '|', quests[q]['title'])

    missing = []
    for qid, q in quests.items():
        if q['optional'] or qid not in reach:
            continue
        for t in q['tasks']:
            if t.startswith('#') or t in tags:
                name = t.lstrip('#')
                members = tags.get(name, set())
                if not members:
                    missing.append((q['title'], t, 'Tag ohne Mitglieder'))
                elif not members & have:
                    missing.append((q['title'], t, 'kein Mitglied herstellbar'))
            elif ID_RE.match(t) and t not in have:
                if t in have_opt:
                    why = 'nur über Fluid/Chemie-Rezept (optimistisch, prüfen)'
                elif t in WELT_QUELLEN:
                    why = 'Weltquelle erwartet: ' + WELT_QUELLEN[t]
                else:
                    why = 'nicht herstellbar (Heuristik)'
                missing.append((q['title'], t, why))
    print(f'\nAufgaben ohne bekannten Weg (Heuristik, prüfen): {len(missing)}')
    for title, t, why in missing[:80]:
        print(f'  - {title}: {t} ({why})')
    return 0


if __name__ == '__main__':
    sys.exit(main())

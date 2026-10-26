# Sky and Stone: Rezept-Simulation (Meilenstein 1). Nur lesen, verändert nichts am Pack.
# Aufruf aus dem Pack-Ordner:
#   python -I -X utf8 _src/rezept-sim/analyse.py <dev_recipes.json> <dev_tags.json> <dev_items.json>
# Quelle der Dateien: Testserver-Dump (zz_dev_recipes.js, zz_dev_tags.js, zz_dev_items.js).
#
# Modell: Ein Gegenstand gilt als erreichbar, wenn er im Startinventar steht, wenn kein Rezept
# ihn herstellt (Rohstoff, optimistisch angenommen: Erz, Mob-Drop, Welt) oder wenn ein Rezept
# ihn herstellt und jede Eingabe mindestens eine erreichbare Option hat. Was danach fehlt, hat
# Rezepte, deren Eingaben nie erreichbar werden. Das sind echte Rezept-Lücken.
import json, os, re, sys, zipfile
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(os.path.dirname(HERE))
CHAPTERS = os.path.join(PACK, 'config', 'ftbquests', 'quests', 'chapters')
START = os.path.join(PACK, 'config', 'skyblockbuilder', 'starter_inventory.json5')
CRAFTING = 'minecraft:crafting'

dump_path, tags_path, items_path, server_dir = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
recipes = json.load(open(dump_path, encoding='utf-8'))['recipes']
tags = json.load(open(tags_path, encoding='utf-8'))
registry = set(json.load(open(items_path, encoding='utf-8'))['items'])
start_text = open(START, encoding='utf-8').read()
start_items = set(re.findall(r'"id":\s*"([^"]+)"', start_text))

# --- Weltquellen: Items, die Mobs oder Blöcke (Ernte, Erz) in den Loot-Tabellen liefern ---
# Mod-Jars und Vanilla-Daten des Testservers. Nur entities/ und blocks/; Truhen ausgeschlossen.
NAME_RE = re.compile(r'"name":\s*"([a-z0-9_.-]+:[a-z0-9_/.-]+)"')
natural = defaultdict(set)
jars = []
for folder in ['mods', os.path.join('libraries', 'net', 'minecraft', 'server')]:
    for root, _, files in os.walk(os.path.join(server_dir, folder)):
        jars += [os.path.join(root, f) for f in files if f.endswith('.jar')]
for jar in jars:
    try:
        with zipfile.ZipFile(jar) as z:
            for name in z.namelist():
                if '/loot_table/entities/' in name:
                    kind = 'Mob'
                elif '/loot_table/blocks/' in name:
                    kind = 'Block'
                else:
                    continue
                for item in NAME_RE.findall(z.read(name).decode('utf-8', 'replace')):
                    natural[item].add(kind)
    except zipfile.BadZipFile:
        continue

# --- Quest-Aufgaben aus den Kapiteln (nur type "item" in tasks, keine Belohnungen) ---
ITEM_BLOCK = re.compile(r'item: \{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}\s*type: "item"')
ID_IN_BLOCK = re.compile(r'id: "([a-z0-9_.-]+:[a-z0-9_/.-]+)"')
TAG_IN_BLOCK = re.compile(r'item_tag\(([^)]+)\)')

tasks = []  # (datei, kennung, mitglieder)
for name in sorted(os.listdir(CHAPTERS)):
    if not name.endswith('.snbt'):
        continue
    text = open(os.path.join(CHAPTERS, name), encoding='utf-8').read()
    for m in ITEM_BLOCK.finditer(text):
        t_task = text.rfind('tasks: [', 0, m.start())
        t_reward = text.rfind('rewards: [', 0, m.start())
        if t_task < 0 or t_task < t_reward:
            continue  # Belohnung
        body = m.group(1)
        item_id = ID_IN_BLOCK.search(body).group(1)
        if item_id == 'ftbfiltersystem:smart_filter':
            tag = TAG_IN_BLOCK.search(body).group(1)
            tasks.append((name, '#' + tag, tags.get(tag, [])))
        else:
            tasks.append((name, item_id, [item_id]))

# --- Rezeptgraph ---
producers = defaultdict(list)
slots_of = {}
errors = Counter()
unresolved = Counter()
for r in recipes:
    slots = [s for s in r['ins'] if s]
    slots_of[r['id']] = slots
    if r.get('insError'):
        errors['Eingaben: ' + r['insError'][:70]] += 1
    if r.get('outError'):
        errors['Ausgabe: ' + r['outError'][:70]] += 1
    for s in r['ins']:
        if not s and r['type'] != CRAFTING:
            unresolved[r['type']] += 1
    if r['out'] and r['out'] != 'minecraft:air':
        producers[r['out']].append(r)

# Quellen, die weder Rezept noch Loot-Tabelle zeigen (im Mod- oder Vanilla-Code, von Hand geprüft)
BEKANNTE_QUELLEN = {
    'minecraft:nether_star': 'Wither-Drop (im Code, nicht in Loot-Tabelle)',
    'ars_nouveau:starbuncle_shards': 'Zähmung wilder Starbuncle mit Goldklumpen (Code: Starbuncle.attemptTame); Spawn auf den Inseln ungeprüft',
}

produced = set(producers)
reachable = set(start_items) | (registry - produced) | {i for i in natural if i in registry} | set(BEKANNTE_QUELLEN)
changed = True
rounds = 0
while changed:
    changed = False
    rounds += 1
    for r in recipes:
        if not r['out'] or r['out'] == 'minecraft:air' or r['out'] in reachable:
            continue
        if all(any(i in reachable for i in s) for s in slots_of[r['id']]):
            reachable.add(r['out'])
            changed = True

def blocked_by(recipe):
    for s in slots_of[recipe['id']]:
        if not any(i in reachable for i in s):
            return s[:4]
    return []

# --- Auswertung ---
gaps = []
raw = []
missing_items = []
for name, key, members in tasks:
    if key.startswith('#'):
        if not members:
            missing_items.append((name, key, 'Tag unbekannt'))
            continue
        if any(i in reachable for i in members):
            continue
        reason = 'alle Mitglieder unerreichbar'
        gaps.append((name, key, reason))
        continue
    if key not in registry:
        missing_items.append((name, key, 'Item nicht registriert'))
        continue
    if key in reachable:
        if key not in produced and key not in start_items:
            raw.append((name, key))
        continue
    reasons = []
    for p in producers.get(key, []):
        reasons.append(p['id'] + ' braucht ' + str(blocked_by(p)))
    gaps.append((name, key, '; '.join(reasons[:3]) or 'kein Rezept'))

groups = sum(1 for _, k, _ in tasks if k.startswith('#'))
print('Rezepte gesamt:', len(recipes), '| Typen:', len(set(r['type'] for r in recipes)))
print('Weltquellen (Mob/Block-Loot):', len(natural), '| davon mit Rezept:', sum(1 for i in natural if i in produced))
print('Rezeptfehler im Dump:', sum(errors.values()), dict(errors.most_common(3)))
err_ids = [r['id'] for r in recipes if 'outError' in r]
print('  Ausgabe unlesbar, Beispiele:', Counter(i.split('/')[0] for i in err_ids).most_common(3))
print('Rezepte ohne Item-Ausgabe:', sum(1 for r in recipes if not r['out'] or r['out'] == 'minecraft:air'))
print('Leere Eingaben ausserhalb Crafting (je Typ):', unresolved.most_common(6))
print('Rezeptsuchrunden:', rounds, '| erreichbare Gegenstaende:', len(reachable))
print('Quest-Aufgaben (Item):', len(tasks), '| davon Gruppen (Filter):', groups)
print('Lücken (Aufgabe unerreichbar):', len(gaps))
print('Rohstoff-Annahme (kein Rezept, nicht im Start):', len(raw))
print('Aufgaben mit unbekanntem Item/Tag:', len(missing_items))
print('Manuell geprüfte Quellen:', len(BEKANNTE_QUELLEN), '| Weltquelle ohne Rezept, nicht im Start:', len([i for i in natural if i in registry and i not in produced and i not in start_items]))
for g in gaps[:40]:
    print('  LÜCKE', g)
for mi in missing_items[:20]:
    print('  UNBEKANNT', mi)

# Bekannte Warnungen aus dem Log
for rid in ['productivebees:centrifuge/modularbees/honeycomb_imperial',
            'ironfurnaces:upgrade_unobtainium', 'ironfurnaces:upgrade_vibranium']:
    present = any(r['id'] == rid for r in recipes)
    print('  Bekannt', rid, 'im Dump:', present)

out_dir = HERE
with open(os.path.join(out_dir, 'luecken.txt'), 'w', encoding='utf-8') as f:
    f.write('Lücken (Aufgabe unerreichbar)\n')
    for g in gaps:
        f.write('%s\t%s\t%s\n' % g)
    f.write('\nRohstoff-Annahme (Quelle im Spiel prüfen)\n')
    for r in raw:
        f.write('%s\t%s\n' % r)
    f.write('\nUnbekannt\n')
    for mi in missing_items:
        f.write('%s\t%s\t%s\n' % mi)
print('Details geschrieben:', os.path.join(out_dir, 'luecken.txt'))

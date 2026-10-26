"""Baut das Gesamtmodell aus den Testserver-Dumps: Register, Rezeptregeln, Loot, Weltregeln, Start.

Zwei Rezept-Dumps ergänzen sich:
- dev_recipejson.json (zz_dev_recipejson.js): vollständiges Rezept-JSON (Fluide, Chemikalien, Chancen, Netze),
  aber ohne Typ und ohne Rezepte, deren Codec scheitert.
- dev_recipes.json (rezept-sim/zz_dev_recipes.js): Typ und vom Spiel aufgelöste Item-Zutaten, nur Hauptergebnis.
Unklare Zutaten im JSON (Mod-eigene Zutat-Typen) werden durch die aufgelösten ersetzt; Rezepte nur im
aufgelösten Dump kommen mit ihrem Hauptergebnis hinein.
"""
import glob
import json
import os
from collections import Counter

from . import rezepte, welt
from .befund import Register
from .huelle import Regel


def _ist_itemgruppe(g):
    return all(':' in x and x.split(':', 1)[0] not in ('fluid', 'chem', 'kraft', 'ort', 'mob', 'biene', 'seele', 'hitze') for x in g)


def _aus_aufgeloest(a, kx):
    """Regel nur aus dem aufgelösten Dump (Typ, Item-Zutaten, Hauptergebnis)."""
    typ, out = a.get('type'), a.get('out')
    if not out or out == 'minecraft:air':
        return []
    ein = [frozenset(g) for g in a.get('ins', []) if g]
    if typ == 'null' and a['id'].startswith('create_mechanical_extruder:'):
        typ = 'create_mechanical_extruder:extruding'
    if typ == 'create_mechanical_extruder:extruding':
        # Extruder: Zutaten sind Nachbarblöcke/Fluide, im Dump leer. Wasser und Lava angenommen.
        haupt = kx.muster(rezepte.STATIONEN[typ][0].haupt)
        if not haupt:
            return []
        return [Regel(id=a['id'], typ=typ, eingaben=ein + [frozenset({'fluid:minecraft:water'}), frozenset({'fluid:minecraft:lava'}),
                                                            frozenset({rezepte.ROT})],
                      ausgaben=frozenset({out}), haupt=haupt, annahme=True, notiz='Extruder: Nachbarblöcke angenommen')]
    if typ == 'minecraft:crafting':
        # Form unbekannt: sicherheitshalber Werkbank
        return [Regel(id=a['id'], typ=typ, eingaben=ein, ausgaben=frozenset({out}), haupt=kx.muster('minecraft:crafting_table'))]
    specs = rezepte.STATIONEN.get(typ)
    if specs is None:
        kx.ohne_leser[typ or '?'] += 1
        return []
    regeln = []
    for n, v in enumerate(specs):
        haupt = kx.muster(v.haupt) if v.haupt else None
        if v.haupt and not haupt:
            continue
        regeln.append(Regel(id=a['id'] + (f'#{n}' if n else ''), typ=typ, ausgaben=frozenset({out}), haupt=haupt,
                            eingaben=ein + [kx.muster(k if isinstance(k, str) else tuple(k)) for k in v.kraft],
                            neben=[kx.muster(s) for s in v.neben]))
    return regeln


def regeln_aus_dumps(json_rezepte, aufgeloest, kx, jar_rezepte=None):
    """jar_rezepte: Rezept-JSON aus den Mod-Jars, nur für Rezepte, die das Spiel kennt (aufgelöster Dump),
    deren JSON der Dump aber nicht hat (Codec scheiterte)."""
    info = Counter()
    info['unklar_ohne_rueckfall'] = []
    regeln = []
    gesehen = set()
    jar_rezepte = jar_rezepte or {}
    eintraege = [(r['id'], r['json']) for r in json_rezepte]
    json_ids = {rid for rid, _ in eintraege}
    for rid in aufgeloest:
        if rid not in json_ids and rid in jar_rezepte:
            eintraege.append((rid, jar_rezepte[rid]))
            info['aus_jar'] += 1
    for rid, js in eintraege:
        if not isinstance(js, dict):
            continue
        gesehen.add(rid)
        a = aufgeloest.get(rid)
        typ = a.get('type') if a else None
        if (not typ or typ == 'null') and isinstance(js.get('type'), str):
            typ = js['type']
        kx.unklar = 0
        neu = rezepte.lies(rid, typ, js, kx)
        if not neu and a and typ not in rezepte.OHNE_ERGEBNIS and a.get('out') not in (None, '', 'minecraft:air'):
            # Leser kennt das Format nicht (z. B. eigene Serializer), das Spiel kennt aber ein Ergebnis
            neu = _aus_aufgeloest(a, kx)
            if neu:
                info['rueckfall_ergebnis'] += 1
            regeln += neu
            continue
        if kx.unklar:
            ins = [frozenset(g) for g in (a or {}).get('ins', []) if g]
            if ins:
                info['rueckfall'] += 1
                for x in neu:
                    x.eingaben = [g for g in x.eingaben if g and not _ist_itemgruppe(g)] + ins
            else:
                info['unklar_ohne_rueckfall'].append(rid)
        regeln += neu
    for rid, a in aufgeloest.items():
        if rid not in gesehen:
            neu = _aus_aufgeloest(a, kx)
            if neu:
                info['nur_aufgeloest'] += 1
            regeln += neu
    return regeln, info


def jar_rezept_ids(jars):
    """Alle Rezept-IDs, die Mod-Jars mitbringen (auch solche, die das Pack per KubeJS entfernt)."""
    import re
    import zipfile
    muster = re.compile(r'^data/([^/]+)/recipes?/(.+)\.json$')
    out = set()
    for jar in jars:
        try:
            with zipfile.ZipFile(jar) as z:
                out |= {f'{m.group(1)}:{m.group(2)}' for m in map(muster.match, z.namelist()) if m}
        except (zipfile.BadZipFile, OSError):
            continue
    return out


def lade_jar_rezepte(jars, ids):
    """Rezept-JSON (data/<ns>/recipe/<pfad>.json) aus Mod-Jars, nur für die gesuchten IDs."""
    import re
    import zipfile
    muster = re.compile(r'^data/([^/]+)/recipes?/(.+)\.json$')
    out = {}
    for jar in jars:
        try:
            with zipfile.ZipFile(jar) as z:
                for name in z.namelist():
                    m = muster.match(name)
                    if m and f'{m.group(1)}:{m.group(2)}' in ids:
                        try:
                            out[f'{m.group(1)}:{m.group(2)}'] = json.loads(z.read(name).decode('utf-8', 'replace'))
                        except ValueError:
                            pass
        except (zipfile.BadZipFile, OSError):
            continue
    return out


def _fluide_und_chemie(regeln):
    fl, ch = set(), set()
    for r in regeln:
        for g in list(r.eingaben) + [r.ausgaben]:
            for x in g:
                if x.startswith('fluid:'):
                    fl.add(x[6:])
                elif x.startswith('chem:'):
                    ch.add(x[5:])
    return fl, ch


def _json(pfad):
    with open(pfad, encoding='utf-8') as f:
        return json.load(f)


class Modell:
    """Alles, was die Stufenprüfung braucht."""

    def __init__(self):
        self.register = None
        self.kx = None
        self.regeln = []
        self.start = set()
        self.start_woher = {}
        self.loot = {}
        self.info = Counter()
        self.quellen = {}         # Dateiname -> Pfad (für den Bericht)
        self.konfig = None


def aufgeloester_dump(kandidaten):
    """Erster Dump im Format von zz_dev_recipes.js (mit Typ je Rezept). Ältere Dumps ohne Typ werden übersprungen."""
    for p in kandidaten:
        if not p or not os.path.exists(p):
            continue
        rez = _json(p).get('recipes') or []
        if rez and 'type' in rez[0]:
            return p, {r['id']: r for r in rez}
    return None, {}


def dump_pfade(pack, testserver):
    ts = os.path.join(testserver, 'kubejs')
    src = os.path.join(pack, '_src')
    def erster(*kand):
        return next((p for p in kand if p and os.path.exists(p)), None)
    return {
        'items': erster(os.path.join(ts, 'dev_items.json'), os.path.join(src, 'items.json')),
        'tags': erster(os.path.join(ts, 'dev_tags.json'), os.path.join(src, 'tags.json')),
        'rezept_json': erster(os.path.join(ts, 'dev_recipejson.json')),
        'rezept_aufgeloest': [os.path.join(ts, 'dev_recipes.json'), os.path.join(src, 'rezept-sim', 'dump', 'dev_recipes.json')],
        'register': erster(os.path.join(ts, 'dev_pruefdaten.json')),
    }


def lade_modell(pack, testserver):
    m = Modell()
    p = dump_pfade(pack, testserver)
    m.quellen = p
    items = _json(p['items'])['items']
    tags = _json(p['tags'])
    extra = _json(p['register']) if p['register'] else {}
    m.register = Register(items, tags, entities=extra.get('entities'), dimensionen=extra.get('dimensionen'),
                          stapel=extra.get('stapel'), fluide=extra.get('fluide'), bloecke=extra.get('bloecke'))
    json_rez = _json(p['rezept_json'])['recipes'] if p['rezept_json'] else []
    p['rezept_aufgeloest'], auf = aufgeloester_dump(p['rezept_aufgeloest'])
    jars = sorted(glob.glob(os.path.join(testserver, 'mods', '*.jar')))
    jars += sorted(glob.glob(os.path.join(testserver, 'libraries', 'net', 'minecraft', 'server', '**', '*.jar'), recursive=True))
    roh = welt.lade_loot(jars, [os.path.join(testserver, 'kubejs', 'data'), os.path.join(pack, 'kubejs', 'data')])
    m.loot = welt.loot_aufloesen(roh, m.register.tags)
    jar_rez = lade_jar_rezepte(jars, set(auf) - {r['id'] for r in json_rez})

    # Erster Durchgang nur, um die Fluide und Chemikalien kennenzulernen (für Fluid-Tags wie c:honey)
    kx0 = rezepte.Kontext(items, tags, loot=m.loot)
    r0, _ = regeln_aus_dumps(json_rez, auf, kx0, jar_rez)
    fl, ch = _fluide_und_chemie(r0)
    fl |= {i.split(':', 1)[0] + ':' + i.split(':', 1)[1][:-len('_bucket')] for i in items if i.endswith('_bucket')}
    if m.register.fluide:
        fl |= m.register.fluide
    kx = rezepte.Kontext(items, tags, fluide=fl, chemikalien=ch, loot=m.loot)
    for r in json_rez:
        if r['json'] and isinstance(r['json'], dict) and 'heat_value' in r['json']:
            blk = (r['json'].get('block_predicate') or {}).get('block')
            if blk in ('minecraft:fire', 'minecraft:soul_fire'):
                kx.hitzequellen.add('minecraft:flint_and_steel')
            elif blk == 'minecraft:lava':
                kx.hitzequellen.add('fluid:minecraft:lava')
            elif blk in kx.items:
                kx.hitzequellen.add(blk)
    rz, info = regeln_aus_dumps(json_rez, auf, kx, jar_rez)
    m.info.update({k: v for k, v in info.items() if k != 'unklar_ohne_rueckfall'})
    m.info['unklar_ohne_rueckfall'] = info['unklar_ohne_rueckfall']
    m.konfig = welt.lade_konfig([testserver, pack])
    wr = welt.weltregeln(kx, m.loot, m.konfig)
    # Varianten (Komponenten) aus allen Rezepten: Bienen-Eier setzen ihre Biene frei, Waben <-> Wabenblock
    varianten = set()
    for r in rz:
        for g in list(r.eingaben) + [r.ausgaben]:
            varianten |= {x for x in g if '{' in x}
    for e in sorted(v for v in varianten if v.startswith('productivebees:spawn_egg_configurable_bee{')):
        t = e[e.index('{') + 1:-1]
        wr.append(Regel(id='welt:ei/' + e, typ='welt', eingaben=[frozenset({e})], ausgaben=frozenset({'biene:' + t})))
    wr += welt.wabenregeln(varianten)
    m.regeln = rz + wr
    m.kx = kx
    m.start, m.start_woher = welt.start_ressourcen(pack, kx.items)
    m.info['rezepte_json'] = len(json_rez)
    m.info['rezepte_aufgeloest'] = len(auf)
    m.info['regeln'] = len(m.regeln)
    m.info['weltregeln'] = len(wr)
    m.info['loot_tabellen'] = len(m.loot)
    return m

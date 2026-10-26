"""Verweise in Datenpaket, Skripten und Konfig: Funktionen, Funktions-Tags, Advancements, Befehls-Belohnungen,
Startinventar (Skyblock Builder) und Item-IDs in KubeJS-Skripten."""
import glob
import json
import os
import re
from collections import Counter

from .befund import fehler, warnung, hinweis
from .welt import json5

B = 'Daten'
ID = r'[a-z0-9_.-]+:[a-z0-9_./-]+'
_ID = re.compile('^' + ID + '$')
SLOTS = {'offhand', 'mainhand', 'head', 'chest', 'legs', 'feet'}


def _funktionen(pack):
    out = set()
    for p in glob.glob(os.path.join(pack, 'kubejs', 'data', '*', 'function*', '**', '*.mcfunction'), recursive=True):
        rel = os.path.relpath(p, os.path.join(pack, 'kubejs', 'data')).replace(os.sep, '/')
        ns, _, rest = rel.partition('/')
        out.add(ns + ':' + rest.split('/', 1)[1][:-len('.mcfunction')])
    return out


def _pack_namespaces(pack):
    d = os.path.join(pack, 'kubejs', 'data')
    return {n for n in os.listdir(d) if n != 'minecraft'} if os.path.isdir(d) else set()


def _item_ok(reg, i):
    if i.startswith('#'):
        return i[1:] in reg.tags
    return i in reg.items


# ---------------- Funktionen ----------------
def pruefe_funktionen(pack, reg):
    befunde = []
    fun, eigene = _funktionen(pack), _pack_namespaces(pack)
    for p in sorted(glob.glob(os.path.join(pack, 'kubejs', 'data', '*', 'function*', '**', '*.mcfunction'), recursive=True)):
        rel = os.path.relpath(p, pack).replace(os.sep, '/')
        for nr, zeile in enumerate(open(p, encoding='utf-8'), 1):
            z = zeile.strip()
            if not z or z.startswith('#'):
                continue
            wo = f'{rel}:{nr}'
            for tag, f in re.findall(r'\bfunction\s+(#?)(' + ID + ')', z):
                if not tag and f not in fun:
                    befunde.append((fehler if f.split(':')[0] in eigene else hinweis)(B, f'{wo}: Funktion {f} gibt es nicht'))
            for befehl in ('give', 'clear'):
                for i in re.findall(r'(?<!effect )\b' + befehl + r'\s+\S+\s+(' + ID + ')', z):   # „effect give“ gibt Effekte, keine Items
                    if i not in reg.items:
                        befunde.append(fehler(B, f'{wo}: {befehl} mit unbekanntem Item {i}'))
            for i in re.findall(r'\bwith\s+(' + ID + ')', z):
                if i not in reg.items:
                    befunde.append(fehler(B, f'{wo}: item … with unbekanntem Item {i}'))
            if reg.entities is not None:
                for e in re.findall(r'\bsummon\s+(' + ID + ')', z):
                    if e not in reg.entities:
                        befunde.append(fehler(B, f'{wo}: summon mit unbekanntem Mob {e}'))
            m = re.search(r'\btellraw\s+\S+\s+(.+)$', z) or re.search(r'\btitle\s+\S+\s+(?:title|subtitle|actionbar)\s+(.+)$', z)
            if m:
                try:
                    json.loads(m.group(1))
                except ValueError:
                    befehl = 'tellraw' if 'tellraw' in z else 'title'
                    befunde.append(fehler(B, f'{wo}: JSON-Text in {befehl} ist kaputt: {m.group(1)[:60]}'))
    for p in sorted(glob.glob(os.path.join(pack, 'kubejs', 'data', '*', 'tags', 'function*', '*.json'))):
        rel = os.path.relpath(p, pack).replace(os.sep, '/')
        try:
            werte = json.load(open(p, encoding='utf-8')).get('values', [])
        except ValueError:
            continue                                    # meldet pack.pruefe_dateien
        for w in werte:
            f, noetig = (w, True) if isinstance(w, str) else (w.get('id'), w.get('required', True))
            if f and not f.startswith('#') and f not in fun and noetig:
                befunde.append(fehler(B, f'{rel}: Funktion {f} gibt es nicht (der Tag lädt dann nicht)'))
    return befunde


# ---------------- Advancements ----------------
def _krit_items(n, out):
    if isinstance(n, dict):
        for k, v in n.items():
            if k in ('items', 'item') and isinstance(v, (str, list)):
                for x in ([v] if isinstance(v, str) else v):
                    if isinstance(x, str):
                        out.add(x)
                    else:
                        _krit_items(x, out)
            else:
                _krit_items(v, out)
    elif isinstance(n, list):
        for v in n:
            _krit_items(v, out)


def pruefe_advancements(pack, reg):
    befunde = []
    fun, eigene = _funktionen(pack), _pack_namespaces(pack)
    adv = {}
    for p in glob.glob(os.path.join(pack, 'kubejs', 'data', '*', 'advancement*', '**', '*.json'), recursive=True):
        rel = os.path.relpath(p, os.path.join(pack, 'kubejs', 'data')).replace(os.sep, '/')
        ns, _, rest = rel.partition('/')
        try:
            adv[ns + ':' + rest.split('/', 1)[1][:-5]] = (os.path.relpath(p, pack).replace(os.sep, '/'), json.load(open(p, encoding='utf-8')))
        except ValueError:
            continue
    for aid, (rel, d) in sorted(adv.items()):
        par = d.get('parent')
        if par and par.split(':')[0] in eigene and par not in adv:
            befunde.append(fehler(B, f'{rel}: Eltern-Advancement {par} gibt es nicht'))
        icon = ((d.get('display') or {}).get('icon') or {})
        icon = icon.get('id') or icon.get('item')
        if icon and icon not in reg.items:
            befunde.append(fehler(B, f'{rel}: Icon {icon} ist kein bekanntes Item'))
        items = set()
        _krit_items(d.get('criteria', {}), items)
        for i in sorted(items):
            if _ID.match(i.lstrip('#')) and not _item_ok(reg, i):
                befunde.append(fehler(B, f'{rel}: Bedingung nennt unbekanntes Item {i}'))
        f = (d.get('rewards') or {}).get('function')
        if f and f not in fun:
            befunde.append(fehler(B, f'{rel}: Belohnungs-Funktion {f} gibt es nicht'))
    return befunde


# ---------------- Questbuch-Befehle ----------------
def pruefe_questbefehle(b, pack):
    befunde = []
    fun = _funktionen(pack)
    for q, r in b.alle_belohnungen():
        if r.typ == 'command' and r.befehl:
            for f in re.findall(r'\bfunction\s+(' + ID + ')', r.befehl):
                if f not in fun:
                    befunde.append(fehler(B, f'{b.name(q)}: Befehls-Belohnung ruft {f} auf, die Funktion gibt es nicht'))
    return befunde


# ---------------- Startinventar ----------------
def pruefe_startinventar(pack, reg):
    befunde = []
    p = os.path.join(pack, 'config', 'skyblockbuilder', 'starter_inventory.json5')
    if not os.path.exists(p):
        return [hinweis(B, 'config/skyblockbuilder/starter_inventory.json5 fehlt: Spieler starten ohne Ausrüstung')]
    try:
        d = json5(open(p, encoding='utf-8-sig').read())
    except ValueError as e:
        return [fehler(B, f'starter_inventory.json5 nicht lesbar ({e})')]
    for n, e in enumerate(d.get('items', []), 1):
        if 'Item' not in e:
            schl = ', '.join(sorted(e))
            befunde.append(fehler(B, f'starter_inventory.json5 Eintrag {n}: Schlüssel „Item“ fehlt (gefunden: {schl}; '
                                     'Projektregel 10: groß geschrieben)'))
            continue
        it = e['Item'] or {}
        i, anzahl = it.get('id'), int(it.get('count', 1))
        if i not in reg.items:
            befunde.append(fehler(B, f'starter_inventory.json5 Eintrag {n}: unbekanntes Item {i}'))
        st = reg.stapelgroesse(i)
        if st and anzahl > st:
            befunde.append(warnung(B, f'starter_inventory.json5 Eintrag {n}: {anzahl}× {i}, Stapelgröße ist {st}'))
        if 'Slot' in e:
            s = e['Slot']
            if not ((isinstance(s, str) and s.lower() in SLOTS) or (isinstance(s, int) and 0 <= s <= 40)):
                befunde.append(fehler(B, f'starter_inventory.json5 Eintrag {n}: unbekannter Slot {s!r}'))
    return befunde


# ---------------- KubeJS-Skripte ----------------
def ohne_kommentare(js):
    out, i, n, q = [], 0, len(js), None
    while i < n:
        c = js[i]
        if q:
            out.append(c)
            if c == '\\':
                out.append(js[i + 1:i + 2]); i += 2; continue
            if c == q:
                q = None
            i += 1
            continue
        if c in '\'"`':
            q = c; out.append(c); i += 1; continue
        if js.startswith('//', i):
            j = js.find('\n', i)
            i = n if j < 0 else j
            continue
        if js.startswith('/*', i):
            j = js.find('*/', i + 2)
            i = n if j < 0 else j + 2
            continue
        out.append(c)
        i += 1
    return ''.join(out)


STR = r'([\'"])([^\'"]+)\1(?!\s*\+)'          # zusammengesetzte Strings ('a_' + t) sind nicht prüfbar
AUSGABE = re.compile(r'event\.(?:shaped|shapeless|smelting|blasting|smoking|campfireCooking|stonecutting|smithing)\(\s*' + STR)
SCHLUESSEL = re.compile(r'\b(?:[A-Z]|item|output|input|result|ingredient)\s*:\s*' + STR)
OF = re.compile(r'\b(?:Item|Ingredient)\.of\(\s*' + STR)
FORMLOS = re.compile(r'event\.shapeless\(\s*' + STR + r'\s*,\s*\[([^\]]*)\]')
REZEPT_ID = re.compile(r'\.id\(\s*' + STR + r'\s*\)')
ENTFERNT = re.compile(r'event\.remove\(\s*\{\s*id\s*:\s*' + STR)


def pruefe_skripte(pack, reg, rezept_ids=None):
    befunde = []
    ids = Counter()
    wo_id = {}
    for ordner in ('server_scripts', 'startup_scripts', 'client_scripts'):
        for p in sorted(glob.glob(os.path.join(pack, 'kubejs', ordner, '**', '*.js'), recursive=True)):
            rel = os.path.relpath(p, pack).replace(os.sep, '/')
            js = ohne_kommentare(open(p, encoding='utf-8').read())
            gesehen = set()
            kand = [m.group(2) for m in AUSGABE.finditer(js)] + [m.group(2) for m in SCHLUESSEL.finditer(js)] + \
                   [m.group(2) for m in OF.finditer(js)]
            for m in FORMLOS.finditer(js):
                kand += [x[1] for x in re.findall(STR, m.group(3))]
            for k in kand:
                k = re.sub(r'^\d+x\s+', '', k.strip())
                if k in gesehen or not _ID.match(k.lstrip('#')):
                    continue
                gesehen.add(k)
                if not _item_ok(reg, k):
                    was = 'Item-Gruppe' if k.startswith('#') else 'Item'
                    befunde.append(fehler(B, f'{rel}: unbekannte {was} {k}'))
            for m in REZEPT_ID.finditer(js):
                ids[m.group(2)] += 1
                wo_id.setdefault(m.group(2), rel)
            if rezept_ids is not None:
                for m in ENTFERNT.finditer(js):
                    if m.group(2) not in rezept_ids:
                        befunde.append(hinweis(B, f'{rel}: entfernt Rezept {m.group(2)}, das es in keiner Mod gibt (veraltet?)'))
    for i, n in sorted(ids.items()):
        if n > 1:
            befunde.append(fehler(B, f'Rezept-ID {i} ist {n}× doppelt vergeben ({wo_id[i]} …): das spätere überschreibt das frühere'))
    return befunde


def pruefe_essen(pack, essen):
    """26.10.2026 (TODO 9.4): ItemEvents.foodEaten löst nur bei Items mit Nahrungs-Komponente aus.
    essen = Liste aus dev_pruefdaten.json (zz_dev_pruefdaten.js im Testserver); None = Dump fehlt."""
    if essen is None:
        return [hinweis(B, 'dev_pruefdaten.json ohne „essen“: Essbarkeit für foodEaten nicht geprüft (Testserver neu starten)')]
    befunde, essen = [], set(essen)
    for pfad in glob.glob(os.path.join(pack, 'kubejs', 'server_scripts', '*.js')):
        text = open(pfad, encoding='utf-8').read()
        if 'foodEaten' not in text:
            continue
        for item in sorted(set(re.findall(r"'([a-z0-9_.-]+:[a-z0-9_/.-]+)'", text))):
            if item not in essen:
                befunde.append(fehler(B, f'{os.path.basename(pfad)}: {item} ist kein Essen, foodEaten löst nie aus'))
    return befunde

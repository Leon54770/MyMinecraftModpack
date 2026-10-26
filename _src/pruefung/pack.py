"""Paket-Prüfungen: packwiz-Index (Hashes, fehlende/überzählige Dateien, Ignore-Liste), Mod-Metadaten,
Konfig-Dateien (BOM, TOML/JSON/JSON5 lesbar), Alter der Testserver-Dumps."""
import glob
import hashlib
import json
import os
import re
import tomllib

from .befund import fehler, warnung, hinweis
from .welt import json5

B = 'Paket'
IMMER_IGNORIERT = {'index.toml', 'pack.toml', '.packwizignore'}
IMMER_IGNORIERT_ORDNER = ('.git/',)


# ---------------- .packwizignore (gitignore-Regeln) ----------------
def _glob_regex(muster):
    out, i = [], 0
    while i < len(muster):
        c = muster[i]
        if muster.startswith('**', i):
            out.append('.*')
            i += 2
            continue
        out.append('[^/]*' if c == '*' else '[^/]' if c == '?' else re.escape(c))
        i += 1
    return ''.join(out)


def ignore_regeln(text):
    regeln = []
    for zeile in text.splitlines():
        z = zeile.strip()
        if not z or z.startswith('#'):
            continue
        neg = z.startswith('!')
        if neg:
            z = z[1:]
        ordner = z.endswith('/')
        z = z.strip('/') if ordner else z
        verankert = z.startswith('/') or '/' in z
        z = z.lstrip('/')
        kopf = '^' if verankert else '(^|.*/)'
        fuss = '/' if ordner else '(/.*)?$'
        regeln.append((neg, re.compile(kopf + _glob_regex(z) + fuss)))
    return regeln


def ignoriert(pfad, regeln):
    ergebnis = False
    for neg, rx in regeln:
        if rx.match(pfad):
            ergebnis = not neg
    return ergebnis


def _hash(pfad, art='sha256'):
    h = hashlib.new(art)
    with open(pfad, 'rb') as f:
        for block in iter(lambda: f.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def _toml(pfad):
    with open(pfad, 'rb') as f:
        return tomllib.load(f)


# ---------------- Index ----------------
def pruefe_index(pack):
    befunde = []
    pt = os.path.join(pack, 'pack.toml')
    if not os.path.exists(pt):
        return [fehler(B, 'pack.toml fehlt')]
    pack_toml = _toml(pt)
    idx_info = pack_toml.get('index', {})
    idx_pfad = os.path.join(pack, idx_info.get('file', 'index.toml'))
    if not os.path.exists(idx_pfad):
        return [fehler(B, 'index.toml fehlt')]
    if _hash(idx_pfad, idx_info.get('hash-format', 'sha256')) != idx_info.get('hash'):
        befunde.append(fehler(B, 'pack.toml: Hash von index.toml stimmt nicht (packwiz refresh fehlt)'))
    idx = _toml(idx_pfad)
    art = idx.get('hash-format', 'sha256')
    ig_pfad = os.path.join(pack, '.packwizignore')
    regeln = ignore_regeln(open(ig_pfad, encoding='utf-8').read()) if os.path.exists(ig_pfad) else []
    im_index = set()
    geaendert = []
    for e in idx.get('files', []):
        rel = e['file']
        im_index.add(rel)
        p = os.path.join(pack, *rel.split('/'))
        if not os.path.exists(p):
            befunde.append(fehler(B, f'{rel} steht im Index, fehlt aber auf der Platte (packwiz refresh)'))
            continue
        if _hash(p, e.get('hash-format', art)) != e.get('hash'):
            geaendert.append(rel)
        if ignoriert(rel, regeln):
            befunde.append(warnung(B, f'{rel} steht im Index, obwohl .packwizignore sie ausschließt: sie landet im Paket '
                                      '(packwiz refresh entfernt sie)'))
        elif '/' not in rel and rel.lower().endswith('.md'):
            befunde.append(hinweis(B, f'{rel}: Dokument im Paket (Projektregel 11: in .packwizignore eintragen?)'))
    if geaendert:
        befunde.append(fehler(B, f'{len(geaendert)} Dateien weichen vom Index ab (packwiz refresh fehlt): ' + ', '.join(geaendert[:8])))
    neu = []
    for wurzel, dirs, files in os.walk(pack):
        rel_dir = os.path.relpath(wurzel, pack).replace(os.sep, '/')
        rel_dir = '' if rel_dir == '.' else rel_dir + '/'
        dirs[:] = [d for d in dirs if not (rel_dir + d + '/').startswith(IMMER_IGNORIERT_ORDNER)
                   and not ignoriert(rel_dir + d + '/x', regeln)]
        for f in files:
            rel = rel_dir + f
            if rel in IMMER_IGNORIERT or rel in im_index or ignoriert(rel, regeln):
                continue
            neu.append(rel)
    if neu:
        befunde.append(warnung(B, f'{len(neu)} Dateien fehlen im Index (packwiz refresh): ' + ', '.join(sorted(neu)[:8])))
    return befunde


# ---------------- Mods ----------------
def pruefe_mods(pack, testserver):
    befunde = []
    dateinamen = {}
    seiten = {}
    for p in sorted(glob.glob(os.path.join(pack, 'mods', '*.pw.toml'))):
        name = os.path.basename(p)
        try:
            m = _toml(p)
        except tomllib.TOMLDecodeError as e:
            befunde.append(fehler(B, f'mods/{name}: nicht lesbar ({e})'))
            continue
        fn, seite, dl = m.get('filename'), m.get('side'), m.get('download') or {}
        if not fn or not m.get('name'):
            befunde.append(fehler(B, f'mods/{name}: name oder filename fehlt'))
            continue
        if seite not in ('both', 'client', 'server'):
            befunde.append(fehler(B, f'mods/{name}: side = {seite!r} (erlaubt: both, client, server)'))
        cf = (m.get('update') or {}).get('curseforge') or {}
        if not dl.get('url') and not (dl.get('mode') == 'metadata:curseforge' and cf.get('file-id') and cf.get('project-id')):
            befunde.append(fehler(B, f'mods/{name}: keine Download-Quelle (url oder CurseForge-IDs)'))
        if not dl.get('hash'):
            befunde.append(fehler(B, f'mods/{name}: kein Hash'))
        if fn in dateinamen:
            befunde.append(fehler(B, f'mods/{name} und mods/{dateinamen[fn]} haben denselben Dateinamen {fn}'))
        dateinamen[fn] = name
        seiten[fn] = seite
    ts_mods = os.path.join(testserver, 'mods') if testserver else None
    if ts_mods and os.path.isdir(ts_mods):
        jars = {f for f in os.listdir(ts_mods) if f.endswith('.jar')}
        for fn, s in sorted(seiten.items()):
            if s != 'client' and fn not in jars:
                befunde.append(warnung(B, f'{fn} ({dateinamen[fn]}) fehlt auf dem Testserver: Dumps und Prüfungen kennen diese Mod nicht'))
        for j in sorted(jars - set(seiten)):
            befunde.append(hinweis(B, f'Testserver hat {j}, das nicht (mehr) im Pack steht: Dumps enthalten dann fremde Rezepte'))
    return befunde


# ---------------- Konfig-Dateien ----------------
def pruefe_dateien(pack):
    befunde = []
    for ordner in ('config', 'kubejs'):
        for wurzel, dirs, files in os.walk(os.path.join(pack, ordner)):
            dirs[:] = [d for d in dirs if d != 'ftbquests']
            for f in files:
                endung = os.path.splitext(f)[1].lower()
                if endung not in ('.toml', '.json', '.json5'):
                    continue
                p = os.path.join(wurzel, f)
                rel = os.path.relpath(p, pack).replace(os.sep, '/')
                roh = open(p, 'rb').read()
                if roh.startswith(b'\xef\xbb\xbf'):
                    befunde.append(fehler(B, f'{rel}: beginnt mit BOM (Projektregel 10: NeoForge lehnt solche Dateien ab)'))
                    roh = roh[3:]
                try:
                    text = roh.decode('utf-8')
                    if endung == '.toml':
                        tomllib.loads(text)
                    elif endung == '.json':
                        json.loads(text)
                    else:
                        json5(text)
                except (UnicodeDecodeError, tomllib.TOMLDecodeError, ValueError) as e:
                    befunde.append(fehler(B, f'{rel}: nicht lesbar ({str(e)[:120]})'))
    return befunde


# ---------------- Dumps ----------------
def _neueste_quelle(pack):
    kandidaten = []
    for muster in ('kubejs/server_scripts/**/*.js', 'kubejs/startup_scripts/**/*.js', 'kubejs/data/**/*', 'mods/*.pw.toml'):
        kandidaten += glob.glob(os.path.join(pack, *muster.split('/')), recursive=True)
    for wurzel, dirs, files in os.walk(os.path.join(pack, 'config')):
        # Questbuch, Inseln und Startinventar liest die Suite direkt aus dem Pack, sie ändern keine Rezepte
        dirs[:] = [d for d in dirs if d not in ('ftbquests', 'skyblockbuilder')]
        kandidaten += [os.path.join(wurzel, f) for f in files]
    kandidaten = [k for k in kandidaten if os.path.isfile(k)]
    return max(kandidaten, key=os.path.getmtime) if kandidaten else None


def pruefe_dump_alter(pack, testserver, dumps):
    befunde = []
    neu = _neueste_quelle(pack)
    if neu:
        t = os.path.getmtime(neu)
        for d in dumps:
            if d and os.path.exists(d) and os.path.getmtime(d) + 1 < t:
                befunde.append(warnung(B, f'{os.path.basename(d)} ist älter als {os.path.relpath(neu, pack)}: Testserver neu starten, '
                                          'sonst prüft die Rezeptprüfung einen alten Stand'))
    src_items = os.path.join(pack, '_src', 'items.json')
    dev_items = os.path.join(testserver, 'kubejs', 'dev_items.json') if testserver else None
    if os.path.exists(src_items) and dev_items and os.path.exists(dev_items):
        alt = set(json.load(open(src_items, encoding='utf-8'))['items'])
        jetzt = set(json.load(open(dev_items, encoding='utf-8'))['items'])
        weg, dazu = sorted(alt - jetzt), sorted(jetzt - alt)
        if weg:
            befunde.append(warnung(B, f'_src/items.json kennt {len(weg)} Items, die es im Spiel nicht mehr gibt (Generator nimmt sie '
                                      f'trotzdem an), z. B. ' + ', '.join(weg[:5]) + '. Neu kopieren aus kubejs/dev_items.json'))
        if dazu:
            befunde.append(hinweis(B, f'_src/items.json fehlen {len(dazu)} Items aus dem Spiel, z. B. ' + ', '.join(dazu[:5])))
    src_tags = os.path.join(pack, '_src', 'tags.json')
    dev_tags = os.path.join(testserver, 'kubejs', 'dev_tags.json') if testserver else None
    if os.path.exists(src_tags) and dev_tags and os.path.exists(dev_tags):
        alt = json.load(open(src_tags, encoding='utf-8'))
        jetzt = json.load(open(dev_tags, encoding='utf-8'))
        anders = sorted(k for k in set(alt) | set(jetzt) if sorted(alt.get(k, [])) != sorted(jetzt.get(k, [])))
        if anders:
            befunde.append(hinweis(B, f'_src/tags.json weicht bei {len(anders)} Gruppen vom Spiel ab, z. B. ' + ', '.join(anders[:5])))
    return befunde

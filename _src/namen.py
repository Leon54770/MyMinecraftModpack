"""Item-Namen wie im Spiel: deutsch, wenn die Mod eine deutsche Übersetzung hat, sonst englisch.
Liest die Sprachdateien aus den Mod-Jars der Prism-Instanz und aus Vanilla. Ergebnis: _src/namen.json
Aufruf aus dem Pack-Ordner:  python -I _src/namen.py   (nur nötig, wenn Mods dazukommen)
"""
import json, os, re, zipfile, hashlib

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPDATA = os.environ['APPDATA']
PRISM = os.path.join(APPDATA, 'PrismLauncher')
MODS = os.path.join(PRISM, 'instances', 'Sky and Stone', 'minecraft', 'mods')
VANILLA_JAR = os.path.join(PRISM, 'libraries', 'com', 'mojang', 'minecraft', '1.21.1', 'minecraft-1.21.1-client.jar')

def lade_json(raw):
    try: return json.loads(raw.decode('utf-8-sig'))
    except Exception: return {}

en, de = {}, {}
def aus_jar(path):
    try: z = zipfile.ZipFile(path)
    except Exception: return
    for n in z.namelist():
        m = re.match(r'assets/[^/]+/lang/(en_us|de_de)\.json$', n)
        if m: (en if m.group(1) == 'en_us' else de).update(lade_json(z.read(n)))

aus_jar(VANILLA_JAR)
# Vanilla-Deutsch liegt nicht im Jar, sondern in den Assets
idx = json.load(open(os.path.join(PRISM, 'assets', 'indexes', '17.json'), encoding='utf-8'))
h = idx['objects']['minecraft/lang/de_de.json']['hash']
de.update(json.load(open(os.path.join(PRISM, 'assets', 'objects', h[:2], h), encoding='utf-8')))
for f in sorted(os.listdir(MODS)):
    if f.endswith('.jar'): aus_jar(os.path.join(MODS, f))
# 1.1.0: eigene Items des Packs (KubeJS) haben ihre Namen in kubejs/assets/<ns>/lang
_kj = os.path.join(PACK, 'kubejs', 'assets')
for ns in (os.listdir(_kj) if os.path.isdir(_kj) else []):
    for sprache, ziel in (('en_us', en), ('de_de', de)):
        f = os.path.join(_kj, ns, 'lang', sprache + '.json')
        if os.path.exists(f): ziel.update(lade_json(open(f, 'rb').read()))

items = json.load(open(os.path.join(PACK, '_src', 'items.json'), encoding='utf-8'))['items']
out = {}
for i in items:
    ns, p = i.split(':', 1)
    for art in ('item', 'block'):
        k = f'{art}.{ns}.{p.replace("/", ".")}'
        if k in en or k in de:
            name = de.get(k) or en.get(k)
            out[i] = ' '.join(name.replace('%s', ' ').split()) or en.get(k, i)   # Platzhalter wie „%s Jetpack“ entfernen
            break
json.dump(out, open(os.path.join(PACK, '_src', 'namen.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
print(f'{len(out)} von {len(items)} Items benannt')

# Sky and Stone: eigene 16×16-Pixel-Art für die Herz-der-Leere-Items und -Blöcke (Version 1.1.0).
# Reines Python (eigener PNG-Schreiber, kein PIL), feste Zufallssaat → bei jedem Lauf gleiche Bilder.
# Aufruf (aus dem Pack-Ordner): python -I -X utf8 _src/texturen.py
# Ausgabe: kubejs/assets/skyandstone/textures/{item,block}/*.png (+ .mcmeta für Animationen)
import os
import random
import struct
import zlib

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIEL = os.path.join(PACK, 'kubejs', 'assets', 'skyandstone', 'textures')
N = 16


def png(pfad, pixel, breite=N, hoehe=N):
    """pixel: Liste von Zeilen, jede Zeile Liste von (r,g,b,a)."""
    roh = b''.join(b'\x00' + b''.join(struct.pack('BBBB', *p) for p in zeile) for zeile in pixel)

    def chunk(typ, daten):
        c = struct.pack('>I', len(daten)) + typ + daten
        return c + struct.pack('>I', zlib.crc32(typ + daten) & 0xFFFFFFFF)
    data = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', breite, hoehe, 8, 6, 0, 0, 0))
    data += chunk(b'IDAT', zlib.compress(roh, 9)) + chunk(b'IEND', b'')
    os.makedirs(os.path.dirname(pfad), exist_ok=True)
    with open(pfad, 'wb') as f:
        f.write(data)


def leer():
    return [[(0, 0, 0, 0) for _ in range(N)] for _ in range(N)]


def hexf(h, a=255):
    h = h.lstrip('#')
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)


def mischen(c1, c2, t):
    return tuple(int(round(c1[i] + (c2[i] - c1[i]) * t)) for i in range(4))


def im_polygon(x, y, pts):
    inn = False
    j = len(pts) - 1
    for i in range(len(pts)):
        xi, yi = pts[i]
        xj, yj = pts[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi + 1e-9) + xi:
            inn = not inn
        j = i
    return inn


def maske_aus(pts):
    return [[im_polygon(x + 0.5, y + 0.5, pts) for x in range(N)] for y in range(N)]


def rand(m, x, y):
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N) or not m[ny][nx]:
            return True
    return False


# ---------------- Splitter (Kristallscherbe) ----------------
SCHERBE = [(1.5, 13.0), (3.0, 7.5), (8.5, 1.0), (14.5, 1.5), (13.0, 8.0), (8.0, 14.0), (4.0, 15.0)]


def splitter(farben, alpha=255, funkeln=True, seed=1):
    dunkel, mitte, hell, glanz = [hexf(c, alpha) for c in farben]
    rnd = random.Random(seed)
    m = maske_aus(SCHERBE)
    img = leer()
    for y in range(N):
        for x in range(N):
            if not m[y][x]:
                continue
            if rand(m, x, y):
                img[y][x] = mischen(dunkel, (0, 0, 0, alpha), 0.35)
                continue
            t = (x - y + 12) / 24.0            # links oben hell, rechts unten dunkel
            c = mischen(hell, dunkel, max(0.0, min(1.0, t)))
            if rnd.random() < 0.12:
                c = mischen(c, mitte, 0.6)
            img[y][x] = c
    for (x, y) in ((4, 11), (5, 10), (5, 9), (6, 8), (7, 7), (8, 6), (9, 5), (10, 4), (11, 3)):   # Glanzkante
        if m[y][x] and not rand(m, x, y):
            img[y][x] = glanz
    if funkeln:
        for (x, y) in ((13, 3), (12, 2), (6, 12)):
            if m[y][x]:
                img[y][x] = mischen(glanz, (255, 255, 255, 255), 0.5)
    return img


SPLITTER = {
    'splitter_erde':    ('3b2a1a', '6b8f3a', 'a8c96b', 'e8f5c0'),
    'splitter_glut':    ('5a1405', 'd2451e', 'ff9a3c', 'fff1a8'),
    'splitter_strom':   ('0d3550', '1f9ed1', '7fe7ff', 'fffbb0'),
    'splitter_ordnung': ('2a1450', '7b3fd1', 'c79bff', 'f2e6ff'),
    'splitter_leben':   ('1d4a1f', 'e05c8a', '9be38c', 'fff0f5'),
    'splitter_geist':   ('2c3f5c', '9fc8e8', 'e6f6ff', 'ffffff'),
    'splitter_leere':   ('0a0612', '3a1a5c', 'b23cff', 'ff9bff'),
}


# ---------------- weitere Items ----------------
def essenz():
    img = leer()
    rnd = random.Random(7)
    dunkel, mitte, hell = hexf('1a0b2e'), hexf('6a2bb0'), hexf('d68cff')
    for y in range(N):
        for x in range(N):
            d = ((x - 7.5) ** 2 + (y - 8.5) ** 2) ** 0.5
            if d < 5.2:
                t = d / 5.2
                c = mischen(hell, mitte, min(1, t * 1.3)) if t < 0.7 else mischen(mitte, dunkel, (t - 0.7) / 0.3)
                if rnd.random() < 0.1:
                    c = mischen(c, hell, 0.5)
                img[y][x] = c
    for (x, y) in ((6, 6), (2, 3), (13, 4), (12, 13), (3, 12)):
        img[y][x] = hexf('ffd6ff')
    return img


def karte():
    img = leer()
    rnd = random.Random(3)
    papier, rahmen = hexf('e3cfa0'), hexf('8a6a3a')
    for y in range(2, 14):
        for x in range(2, 14):
            img[y][x] = mischen(papier, hexf('cdb27a'), rnd.random() * 0.4)
    for i in range(2, 14):
        img[2][i] = img[13][i] = img[i][2] = img[i][13] = rahmen
    for (x, y) in ((4, 10), (5, 10), (4, 11), (5, 11), (6, 11)):         # Heimatinsel
        img[y][x] = hexf('5c8a3a')
    for (x, y) in ((6, 9), (7, 8), (8, 8), (9, 7)):                     # Pfad
        img[y][x] = hexf('7a5230')
    for (x, y) in ((10, 4), (12, 4), (11, 5), (10, 6), (12, 6)):          # rotes X
        img[y][x] = hexf('b3261e')
    return img


def kern():
    img = leer()
    m = maske_aus([(5, 2), (11, 2), (14, 5), (14, 11), (11, 14), (5, 14), (2, 11), (2, 5)])
    for y in range(N):
        for x in range(N):
            if not m[y][x]:
                continue
            d = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** 0.5
            if rand(m, x, y):
                img[y][x] = hexf('1c1c22')
            elif d < 2.6:
                img[y][x] = mischen(hexf('ffd0ff'), hexf('c040ff'), d / 2.6)
            elif d < 4.2:
                img[y][x] = hexf('5a1f80')
            else:
                img[y][x] = mischen(hexf('5e5e6b'), hexf('2e2e36'), (x + y) / 30)
    return img


def rohling():
    return splitter(('4a5560', '9aa8b4', 'd9e4ee', 'ffffff'), alpha=200, funkeln=False, seed=11)


# ---------------- Blöcke ----------------
def stein(seed, basis='6f6a75', fleck='57525c'):
    rnd = random.Random(seed)
    b, f = hexf(basis), hexf(fleck)
    return [[mischen(b, f, rnd.random() * 0.8) for _ in range(N)] for _ in range(N)]


def herz(helligkeit, seed=21):
    """Obsidian-artiger Grund mit Adern, die zur Mitte laufen. helligkeit 0 = schlafend, 1 = voll erwacht."""
    rnd = random.Random(seed)
    img = [[mischen(hexf('0d0a14'), hexf('1f1630'), rnd.random()) for _ in range(N)] for _ in range(N)]
    ader_dunkel, ader_hell = hexf('3a1f5c'), hexf('ff5cf2')
    ader = mischen(ader_dunkel, ader_hell, helligkeit)
    pfade = [[(0, 3), (2, 4), (4, 5), (6, 6), (7, 7)], [(15, 2), (13, 3), (11, 5), (9, 6), (8, 7)],
             [(1, 14), (3, 12), (5, 10), (6, 9), (7, 8)], [(14, 15), (12, 13), (10, 11), (9, 9), (8, 8)],
             [(7, 0), (7, 2), (8, 4), (7, 6)], [(8, 15), (8, 13), (7, 11), (8, 9)]]
    for p in pfade:
        for (x, y) in p:
            img[y][x] = ader
            for dx, dy in ((1, 0), (0, 1)):
                if 0 <= x + dx < N and 0 <= y + dy < N and helligkeit > 0:
                    img[y + dy][x + dx] = mischen(img[y + dy][x + dx], ader, 0.45)
    kern_farbe = mischen(hexf('5a2a80'), hexf('ffe6ff'), helligkeit)
    for (x, y) in ((7, 7), (8, 7), (7, 8), (8, 8)):
        img[y][x] = kern_farbe
    for y in range(5, 11):
        for x in range(5, 11):
            d = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** 0.5
            if 1.2 < d < 3.2:
                img[y][x] = mischen(img[y][x], mischen(ader, kern_farbe, 0.5), max(0.25, 0.9 - d * 0.2))
    return img


def sockel_oben(zerbrochen=False):
    img = stein(31)
    ring = hexf('6a3a9a') if not zerbrochen else hexf('3d3344')
    for y in range(N):
        for x in range(N):
            d = ((x - 7.5) ** 2 + (y - 7.5) ** 2) ** 0.5
            if 4.5 < d < 6.0:
                img[y][x] = ring
            if x in (0, 15) or y in (0, 15):
                img[y][x] = hexf('3e3a44')
    if zerbrochen:
        _risse(img, 5)
    return img


def sockel_seite(zerbrochen=False):
    img = stein(41)
    for x in range(N):
        img[0][x] = img[1][x] = hexf('4a4652')
        img[14][x] = img[15][x] = hexf('4a4652')
    rune = hexf('8a5ac0') if not zerbrochen else hexf('4a4058')
    for (x, y) in ((4, 5), (4, 6), (4, 7), (5, 8), (6, 7), (6, 6), (6, 5), (9, 5), (10, 6), (11, 7), (10, 8), (9, 9), (11, 9)):
        img[y][x] = rune
    if zerbrochen:
        _risse(img, 6)
        for (x, y) in ((1, 13), (2, 13), (2, 12), (13, 13), (14, 12)):
            img[y][x] = hexf('4f7a3a')     # Moos
    return img


def _risse(img, seed):
    rnd = random.Random(seed)
    x, y = rnd.randrange(3, 13), 2
    for _ in range(14):
        if 0 <= x < N and 0 <= y < N:
            img[y][x] = hexf('1a181e')
        y += 1
        x += rnd.choice((-1, 0, 1))


def animation(frames):
    """Frames untereinander (Minecraft-Animation, 16×(16·n))."""
    return [zeile for f in frames for zeile in f]


def main():
    it = os.path.join(ZIEL, 'item')
    bl = os.path.join(ZIEL, 'block')
    for i, (name, farben) in enumerate(SPLITTER.items()):
        png(os.path.join(it, name + '.png'), splitter(farben, seed=i + 1))
    png(os.path.join(it, 'splitter_rohling.png'), rohling())
    png(os.path.join(it, 'leerenessenz.png'), essenz())
    png(os.path.join(it, 'karte_werkstatt.png'), karte())
    png(os.path.join(it, 'waechterkern.png'), kern())
    png(os.path.join(bl, 'herz_der_leere.png'), herz(0.0))
    stufen = [0.55, 0.75, 1.0, 0.75]
    png(os.path.join(bl, 'herz_erwacht.png'), animation([herz(h) for h in stufen]), N, N * len(stufen))
    with open(os.path.join(bl, 'herz_erwacht.png.mcmeta'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('{"animation": {"frametime": 6, "interpolate": true}}\n')
    png(os.path.join(bl, 'herzsockel_oben.png'), sockel_oben())
    png(os.path.join(bl, 'herzsockel_seite.png'), sockel_seite())
    png(os.path.join(bl, 'herzsockel_unten.png'), stein(51))
    png(os.path.join(bl, 'herzsockel_zerbrochen_oben.png'), sockel_oben(True))
    png(os.path.join(bl, 'herzsockel_zerbrochen_seite.png'), sockel_seite(True))
    print('Texturen geschrieben nach', os.path.relpath(ZIEL, PACK))


if __name__ == '__main__':
    main()

"""Sky and Stone – erzeugt die wählbaren Startinseln für Skyblock Builder.

Aufruf:  python -I _src/inseln.py   (aus dem Pack-Ordner)
Ergebnis: config/skyblockbuilder/templates/islands/*.nbt + templates.json5
"""
import gzip, io, json, math, os, random, struct, sys
from collections import deque

DATA_VERSION = 3955  # Minecraft 1.21.1
PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(PACK, 'config', 'skyblockbuilder', 'templates', 'islands')

# ---------------- NBT ----------------
class Int(int): pass
class Byte(int): pass    # 0.10.0: für Block-Daten (Schild)
class TList(list):
    def __init__(self, tag, items): super().__init__(items); self.tag = tag

def _w_payload(buf, tag, v):
    if tag == 1: buf.write(struct.pack('>b', v))
    elif tag == 3: buf.write(struct.pack('>i', v))
    elif tag == 8:
        b = v.encode('utf-8'); buf.write(struct.pack('>H', len(b))); buf.write(b)
    elif tag == 9:
        buf.write(struct.pack('>bi', v.tag if len(v) else 0, len(v)))
        for x in v: _w_payload(buf, v.tag, x)
    elif tag == 10:
        for k, x in v.items():
            t = _tag(x); buf.write(struct.pack('>b', t)); _w_payload(buf, 8, k); _w_payload(buf, t, x)
        buf.write(b'\x00')
    else: raise ValueError(tag)

def _tag(v):
    if isinstance(v, TList): return 9
    if isinstance(v, Byte): return 1
    if isinstance(v, dict): return 10
    if isinstance(v, str): return 8
    if isinstance(v, int): return 3
    raise TypeError(type(v))

def write_nbt(path, root):
    buf = io.BytesIO(); buf.write(b'\x0a'); _w_payload(buf, 8, ''); _w_payload(buf, 10, root)
    with gzip.open(path, 'wb') as f: f.write(buf.getvalue())

# ---------------- Insel-Baukasten ----------------
LEAF_TYPES = ('leaves',)

class Island:
    def __init__(self, name):
        self.name = name; self.blocks = {}; self.nbt = {}   # nbt: Block-Daten je Position (Schild)
    def set(self, x, y, z, block, **props):
        self.blocks[(x, y, z)] = (block if ':' in block else 'minecraft:' + block, props)
    def get(self, x, y, z):
        b = self.blocks.get((x, y, z)); return b[0] if b else None
    def setif_air(self, x, y, z, block, **props):
        if (x, y, z) not in self.blocks: self.set(x, y, z, block, **props)

    # Rundes Inselstück: Oberfläche top, darunter filler, nach unten spitz zulaufend
    def disc(self, cx, cz, r, ytop, top, filler, depth, under='stone', seed=1):
        rnd = random.Random(seed)
        for x in range(cx - r - 1, cx + r + 2):
            for z in range(cz - r - 1, cz + r + 2):
                d = math.hypot(x - cx, z - cz)
                if d > r + 0.4: continue
                edge = d > r - 0.8
                if edge and rnd.random() < 0.35: continue
                col_depth = max(1, int(round(depth * (1 - (d / (r + 0.5)) ** 1.6))) + rnd.choice((0, 0, 1)))
                for i in range(col_depth):
                    y = ytop - i
                    blk = top if i == 0 else (filler if i <= 2 else under)
                    self.set(x, y, z, blk, **({'snowy': 'false'} if blk.endswith(('grass_block', 'mycelium', 'podzol')) else {}))

    def oak(self, x, y, z, log='oak_log', leaves='oak_leaves', h=5):
        for i in range(h): self.set(x, y + i, z, log, axis='y')
        top = y + h - 1
        for dy, r in ((-2, 2), (-1, 2), (0, 1), (1, 1)):
            for dx in range(-r, r + 1):
                for dz in range(-r, r + 1):
                    if r == 2 and abs(dx) == 2 and abs(dz) == 2: continue
                    if r == 1 and dy == 1 and abs(dx) + abs(dz) == 2: continue
                    self.setif_air(x + dx, top + dy, z + dz, leaves)

    def palm(self, x, y, z):
        for i in range(6): self.set(x + (1 if i >= 4 else 0), y + i, z, 'jungle_log', axis='y')
        tx, ty = x + 1, y + 6
        self.set(tx, ty, z, 'jungle_leaves')
        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            for k in (1, 2):
                self.setif_air(tx + dx * k, ty - (1 if k == 2 else 0), z + dz * k, 'jungle_leaves')
        for dx, dz in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
            self.setif_air(tx + dx, ty, z + dz, 'jungle_leaves')

    def cherry(self, x, y, z):
        for i in range(4): self.set(x, y + i, z, 'cherry_log', axis='y')
        for i, (dx, dz) in enumerate(((1, 0), (-1, 0))):
            self.set(x + dx, y + 4, z, 'cherry_log', axis='x'); self.set(x + 2 * dx, y + 5, z, 'cherry_log', axis='y')
        for cx in (x - 2, x + 2):
            for dy, r in ((5, 2), (6, 2), (7, 1)):
                for dx in range(-r, r + 1):
                    for dz in range(-r, r + 1):
                        if abs(dx) == r and abs(dz) == r: continue
                        self.setif_air(cx + dx, y + dy, z + dz, 'cherry_leaves')

    def mushroom(self, x, y, z):
        for i in range(5): self.set(x, y + i, z, 'mushroom_stem', up='false', down='false', north='true', south='true', east='true', west='true')
        for dx in range(-3, 4):
            for dz in range(-3, 4):
                if abs(dx) == 3 and abs(dz) == 3: continue
                self.set(x + dx, y + 5, z + dz, 'brown_mushroom_block', up='true', down='false',
                         north=str(dz == -3 or (abs(dx) == 3 and dz == -2)).lower(), south=str(dz == 3 or (abs(dx) == 3 and dz == 2)).lower(),
                         west=str(dx == -3 or (abs(dz) == 3 and dx == -2)).lower(), east=str(dx == 3 or (abs(dz) == 3 and dx == 2)).lower())

    def finish_leaves(self):
        """Blätter: distance per Breitensuche vom nächsten Stamm, damit sie korrekt zerfallen."""
        dist = {}; q = deque()
        for p, (b, _) in self.blocks.items():
            if b.endswith('_log') or b.endswith('_stem') and 'mushroom' not in b:
                dist[p] = 0; q.append(p)
        while q:
            p = q.popleft()
            for d in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
                n = (p[0]+d[0], p[1]+d[1], p[2]+d[2])
                b = self.blocks.get(n)
                if b and b[0].endswith('_leaves') and n not in dist and dist[p] < 7:
                    dist[n] = dist[p] + 1; q.append(n)
        for p, (b, props) in list(self.blocks.items()):
            if b.endswith('_leaves'):
                d = dist.get(p)
                self.blocks[p] = (b, {'distance': str(d if d else 7), 'persistent': 'false' if d else 'true', 'waterlogged': 'false'})

    def save(self, spawn_rel):
        self.finish_leaves()
        xs = [p[0] for p in self.blocks]; ys = [p[1] for p in self.blocks]; zs = [p[2] for p in self.blocks]
        mn = (min(xs), min(ys), min(zs)); size = (max(xs) - mn[0] + 1, max(ys) - mn[1] + 1, max(zs) - mn[2] + 1)
        palette, pidx, blocks = [], {}, []
        for p, (b, props) in sorted(self.blocks.items()):
            key = (b, tuple(sorted(props.items())))
            if key not in pidx:
                pidx[key] = len(palette)
                e = {'Name': b}
                if props: e['Properties'] = {k: str(v) for k, v in props.items()}
                palette.append(e)
            e = {'pos': TList(3, [Int(p[0]-mn[0]), Int(p[1]-mn[1]), Int(p[2]-mn[2])]), 'state': Int(pidx[key])}
            if p in self.nbt: e['nbt'] = self.nbt[p]
            blocks.append(e)
        root = {'DataVersion': Int(DATA_VERSION), 'size': TList(3, [Int(s) for s in size]),
                'palette': TList(10, palette), 'blocks': TList(10, blocks), 'entities': TList(10, [])}
        write_nbt(os.path.join(OUT, self.name + '.nbt'), root)
        sp = [spawn_rel[0] - mn[0], spawn_rel[1] - mn[1], spawn_rel[2] - mn[2]]
        return size, sp, len(blocks)

# ---------------- Spuren der Erbauer (0.10.0) ----------------
SCHILD = ['Hier wachte', 'der letzte', 'Wächter.', 'Folge dem Buch.']
def ruine(i, spawn):
    """Kleine verfallene Säule mit Schild am Inselrand: Stelle möglichst weit vom Spawn, ohne Baum darüber."""
    oben = {}
    for (x, y, z), (b, _) in i.blocks.items():
        if b.endswith(('grass_block', 'dirt', 'sand', 'mycelium', 'podzol', 'stone', 'moss_block', 'coarse_dirt')):
            if (x, z) not in oben or y > oben[(x, z)]: oben[(x, z)] = y
    def frei(x, y, z):
        return all((x + dx, y + dy, z + dz) not in i.blocks for dx in (-1, 0, 1) for dz in (-1, 0, 1) for dy in (1, 2, 3))
    kand = [(x, y, z) for (x, z), y in oben.items() if (x, y, z) in i.blocks and frei(x, y, z)
            and all((x + dx, z + dz) in oben for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
    if not kand:   # zerklüftete Insel: ohne Nachbar-Bedingung, dafür muss das Schildfeld frei sein
        kand = [(x, y, z) for (x, z), y in oben.items() if (x, y, z) in i.blocks and frei(x, y, z)]
    if not kand: return None
    x, y, z = max(kand, key=lambda p: ((p[0] - spawn[0]) ** 2 + (p[2] - spawn[2]) ** 2, p))
    i.set(x, y + 1, z, 'mossy_stone_bricks'); i.set(x, y + 2, z, 'cracked_stone_bricks')
    i.set(x, y + 3, z, 'mossy_stone_brick_slab', type='bottom', waterlogged='false')
    # Schild auf der dem Spawn zugewandten Seite, Blick zum Spawn
    dx, dz = spawn[0] - x, spawn[2] - z
    sx, sz = (x + (1 if dx > 0 else -1), z) if abs(dx) >= abs(dz) else (x, z + (1 if dz > 0 else -1))
    rot = {(0, 1): 0, (-1, 0): 4, (0, -1): 8, (1, 0): 12}[(sx - x, sz - z)]
    i.set(sx, y + 1, sz, 'oak_sign', rotation=str(rot), waterlogged='false')
    txt = lambda zeilen: {'messages': TList(8, [json.dumps({'text': t}, ensure_ascii=False) for t in zeilen]),
                          'color': 'black', 'has_glowing_text': Byte(0)}
    i.nbt[(sx, y + 1, sz)] = {'id': 'minecraft:sign', 'front_text': txt(SCHILD), 'back_text': txt(['', '', '', '']),
                              'is_waxed': Byte(1)}
    # Lootr-Truhe gegenüber dem Schild (0.20.1): jeder Spieler bekommt seine eigene Beute aus skyandstone:ruinen/fund
    cx, cz = x - (sx - x), z - (sz - z)
    if (cx, y + 1, cz) not in i.blocks:
        i.set(cx, y + 1, cz, 'lootr:lootr_chest', type='single', facing='north', waterlogged='false')
        i.nbt[(cx, y + 1, cz)] = {'id': 'lootr:lootr_chest', 'LootTable': 'skyandstone:ruinen/fund'}
    return (sx, y + 1, sz)

# ---------------- Die Inseln ----------------
def klassisch():
    i = Island('klassisch')  # das L aus SkyBlock 2.1 – drei Schichten, seit 0.20.1 größer (9×3 oben, 3×6 unten)
    for x in range(9):
        for z in range(3):
            for y in range(3): i.set(x, y, z, 'grass_block' if y == 2 else 'dirt', **({'snowy': 'false'} if y == 2 else {}))
    for x in range(3):
        for z in range(3, 9):
            for y in range(3): i.set(x, y, z, 'grass_block' if y == 2 else 'dirt', **({'snowy': 'false'} if y == 2 else {}))
    i.set(8, 2, 0, 'dirt'); i.oak(8, 3, 0)
    i.set(1, 0, 4, 'bedrock')
    return i, (2, 3, 1)

def lichtung():
    i = Island('lichtung')  # Waldlichtung mit Teich
    i.disc(0, 0, 6, 0, 'grass_block', 'dirt', 6, seed=3)
    i.oak(-3, 1, -2); i.oak(3, 1, 2, log='birch_log', leaves='birch_leaves', h=6)
    for x, z in ((1, -2), (2, -2), (1, -3)): i.set(x, 0, z, 'water', level='0')
    for x, z, f in ((-1, 3, 'poppy'), (0, 4, 'dandelion'), (-4, 1, 'cornflower'), (2, 4, 'short_grass'), (-2, -4, 'short_grass'), (4, -1, 'oxeye_daisy')):
        i.set(x, 1, z, f)
    i.set(-3, 0, 3, 'coarse_dirt'); i.set(0, 0, 0, 'grass_block', snowy='false')
    return i, (0, 1, 0)

def oase():
    i = Island('oase')  # Wüsten-Oase: Sand, Palme, Zuckerrohr, Kakteen
    i.disc(0, 0, 6, 0, 'sand', 'sandstone', 5, under='sandstone', seed=7)
    for x, z in ((0, 0), (1, 0), (0, 1), (1, 1)): i.set(x, 0, z, 'water', level='0'); i.set(x, -1, z, 'sand')
    for x, z in ((-1, 0), (-1, 1), (2, 0), (2, 1), (0, -1), (1, 2)): i.set(x, 0, z, 'grass_block', snowy='false')
    for x, z in ((-1, 0), (2, 1)): i.set(x, 1, z, 'sugar_cane', age='0')
    i.palm(-3, 1, -3); i.set(-3, 0, -3, 'dirt')
    for x, z in ((4, -2), (-4, 3)): i.set(x, 1, z, 'cactus', age='0')
    i.set(3, 1, 3, 'dead_bush')
    return i, (0, 1, -2)

def kirschhain():
    i = Island('kirschhain')  # Kirschblüten auf Moos
    i.disc(0, 0, 5, 0, 'grass_block', 'dirt', 5, seed=11)
    for x, z in ((-3, 1), (-2, 2), (3, -2), (2, 3)): i.set(x, 0, z, 'moss_block')
    i.cherry(0, 1, 0)
    for x, z, n in ((-3, -3, 3), (3, 2, 2), (-1, 3, 4), (2, -3, 1)):
        i.set(x, 1, z, 'pink_petals', facing='north', flower_amount=str(n))
    return i, (-2, 1, 3)

def pilzinsel():
    i = Island('pilzinsel')  # Myzel mit Riesenpilz, kleines Grasstück für Bäume
    i.disc(0, 0, 5, 0, 'mycelium', 'dirt', 5, seed=5)
    i.mushroom(0, 1, 0)
    for x, z in ((3, 3), (4, 2), (3, 2)): i.set(x, 0, z, 'grass_block', snowy='false')
    i.set(-3, 1, 2, 'red_mushroom'); i.set(2, 1, -3, 'brown_mushroom'); i.set(-2, 1, -3, 'red_mushroom')
    return i, (3, 1, 3)

def felsbrocken():
    i = Island('felsbrocken')  # Gruß an StoneBlock: Felsen mit etwas Erz, oben Gras und Baum
    rnd = random.Random(42)
    for x in range(-5, 6):
        for y in range(-6, 3):
            for z in range(-5, 6):
                r = 5.2 - max(0, -y - 2) * 0.55 - (max(0, y) * 0.9)
                if math.hypot(x, z) + rnd.random() * 0.8 > r: continue
                b = rnd.choices(['stone', 'cobblestone', 'andesite', 'diorite', 'granite', 'tuff'], [10, 4, 2, 1, 1, 1])[0]
                i.set(x, y, z, b)
    for x in range(-2, 3):
        for z in range(-2, 3):
            if abs(x) + abs(z) <= 3:
                top = max(y for (px, y, pz) in i.blocks if px == x and pz == z)
                i.set(x, top, z, 'grass_block', snowy='false'); i.set(x, top - 1, z, 'dirt')
    for x, y, z, ore in ((-3, -2, 1, 'coal_ore'), (2, -3, -2, 'coal_ore'), (3, -1, 2, 'copper_ore'), (-1, -4, -2, 'iron_ore')):
        if (x, y, z) in i.blocks: i.set(x, y, z, ore)
    gy = max(y for (px, y, pz) in i.blocks if px == 0 and pz == 0)
    i.oak(0, gy + 1, 0)
    return i, (2, gy + 1, 1)

ISLANDS = [
    (klassisch, 'Klassisch', 'Das L aus Erde wie in SkyBlock 2.1, mit mehr Platz für Felder und Maschinen.'),
    (lichtung, 'Waldlichtung', 'Runde Grasinsel mit Eiche, Birke und kleinem Teich.'),
]

def main():
    os.makedirs(OUT, exist_ok=True)
    templates, spawns = [], {}
    for fn, title, desc in ISLANDS:
        isl, sp = fn()
        r = ruine(isl, sp)
        size, sp_rel, n = isl.save(sp)
        spawns[isl.name] = {'south': [sp_rel], 'west': [], 'north': [], 'east': []}
        templates.append({'name': title, 'desc': desc, 'file': isl.name + '.nbt', 'spawns': isl.name,
                          'surroundingBlocks': 'default', 'spreads': 'default'})
        print(f'{isl.name:12} Größe {size}  Blöcke {n:4}  Spawn {sp_rel}  Ruine/Schild {r}')
    cfg = {
        'defaultOffset': 0, 'mainSpawnIsland': None, 'netherSpreads': [],
        'spawnPointReferences': spawns,
        'spreadReferences': {'default': []},
        'surroundingBlockReferences': {'default': {}},
        'templateList': templates,
    }
    path = os.path.join(PACK, 'config', 'skyblockbuilder', 'templates.json5')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('// Sky and Stone: wählbare Startinseln (erzeugt von _src/inseln.py)\n')
        json.dump(cfg, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()

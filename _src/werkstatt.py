"""Sky and Stone 1.1.0: die vergessene Werkstatt (Ruineninsel), gesetzt von der Karte der Werkstatt.

Aufruf (aus dem Pack-Ordner): python -I -X utf8 _src/werkstatt.py
Ergebnis: kubejs/data/skyandstone/structure/werkstatt.nbt (Vanilla-Strukturformat, Platzieren per /place template).
Größe passt in 15×13×15 (das Ritual-Skript prüft dieses Feld auf Luft, bevor es platziert).
Nutzt den NBT-Schreiber und die Insel-Bausteine aus _src/inseln.py.
"""
import json
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inseln as I  # noqa: E402

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIEL = os.path.join(PACK, 'kubejs', 'data', 'skyandstone', 'structure')
SCHILD = ['Hier schmiedeten', 'wir das Herz.', 'Es zersprang.', 'Sieben Splitter.']


def baue():
    i = I.Island('werkstatt')
    rnd = random.Random(1101)
    # Grund: Steininsel, Radius 6, unten spitz
    i.disc(0, 0, 6, 0, 'stone', 'stone', 5, under='stone', seed=11)
    # Boden aus Steinziegeln, teils rissig/bemoost
    for (x, y, z), (b, _) in list(i.blocks.items()):
        if y == 0 and math.hypot(x, z) <= 5.2:
            i.set(x, 0, z, rnd.choice(['stone_bricks', 'stone_bricks', 'cracked_stone_bricks', 'mossy_stone_bricks']))
    # Mauerreste auf dem Rand (Höhe 1–3, mit Lücken)
    for w in range(0, 360, 15):
        a = math.radians(w)
        x, z = int(round(5 * math.cos(a))), int(round(5 * math.sin(a)))
        if (x, 0, z) not in i.blocks or rnd.random() < 0.3:
            continue
        for h in range(1, rnd.choice((1, 2, 2, 3)) + 1):
            i.set(x, h, z, rnd.choice(['stone_bricks', 'mossy_stone_bricks', 'cracked_stone_bricks']))
    # Mitte: zerbrochener Herzsockel auf einem kleinen Podest, vier Säulen mit Seelenlaternen
    for x in (-1, 0, 1):
        for z in (-1, 0, 1):
            i.set(x, 1, z, 'smooth_stone_slab', type='bottom', waterlogged='false')
    i.set(0, 1, 0, 'skyandstone:herzsockel_zerbrochen')
    for (x, z) in ((-2, -2), (2, -2), (-2, 2), (2, 2)):
        hoehe = 3 if (x, z) != (2, 2) else 1          # eine Säule ist eingestürzt
        for h in range(1, hoehe + 1):
            i.set(x, h, z, 'chiseled_stone_bricks' if h == hoehe else 'stone_bricks')
        if hoehe == 3:
            i.set(x, 4, z, 'soul_lantern', hanging='false', waterlogged='false')
    i.set(2, 1, 3, 'cracked_stone_bricks')            # Trümmer der eingestürzten Säule
    # Leuchtturm-Säule am Rand, damit man die Insel von weitem sieht
    for h in range(1, 8):
        i.set(-4, h, 0, 'crying_obsidian' if h % 3 == 0 else 'polished_blackstone_bricks')
    i.set(-4, 8, 0, 'end_rod', facing='up')
    # Werkbank-Reste der Erbauer
    i.set(3, 1, -1, 'create:andesite_casing')
    i.set(3, 2, -1, 'create:andesite_casing')
    i.set(4, 1, 1, 'damaged_anvil', facing='north')
    i.set(-2, 1, -4, 'crafting_table')
    # Amethyst am Inselrand: Material für Splitter-Rohlinge
    for (x, z) in ((-3, 4), (4, -3), (-5, -2)):
        if (x, 0, z) in i.blocks:
            i.set(x, 1, z, 'amethyst_cluster', facing='up', waterlogged='false')
    # Lootr-Truhe: Fund der Werkstatt (pro Spieler eigene Beute)
    i.set(1, 1, -3, 'lootr:lootr_chest', type='single', facing='south', waterlogged='false')
    i.nbt[(1, 1, -3)] = {'id': 'lootr:lootr_chest', 'LootTable': 'skyandstone:werkstatt/fund'}
    # Schild vor dem Sockel
    i.set(0, 1, 2, 'oak_sign', rotation='0', waterlogged='false')
    txt = lambda z: {'messages': I.TList(8, [json.dumps({'text': t}, ensure_ascii=False) for t in z]),
                     'color': 'black', 'has_glowing_text': I.Byte(0)}
    i.nbt[(0, 1, 2)] = {'id': 'minecraft:sign', 'front_text': txt(SCHILD), 'back_text': txt(['', '', '', '']),
                        'is_waxed': I.Byte(1)}
    return i


def main():
    I.OUT = ZIEL
    os.makedirs(ZIEL, exist_ok=True)
    i = baue()
    xs = [p[0] for p in i.blocks]; ys = [p[1] for p in i.blocks]; zs = [p[2] for p in i.blocks]
    print('Ursprung (min):', (min(xs), min(ys), min(zs)), 'Größe:', (max(xs) - min(xs) + 1, max(ys) - min(ys) + 1, max(zs) - min(zs) + 1))
    size, _, n = i.save((0, 1, 0))
    print(f'werkstatt.nbt: Größe {size}, {n} Blöcke → {os.path.relpath(ZIEL, PACK)}')


if __name__ == '__main__':
    main()

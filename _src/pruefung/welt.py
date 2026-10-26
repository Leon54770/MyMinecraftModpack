"""Quellen ohne Rezept: Loot-Tabellen (Mobs, Blöcke, Angeln), natürliche Vorgänge (Bäume, Bruchsteingenerator,
Spawns, Portale, Bosse) und der Start (Startinventar, Inselblöcke).

Was vom Biom oder von Strukturen abhängt, ist als Annahme markiert (Regel.annahme). Der Bericht zeigt getrennt,
welche Quest-Items nur über Annahmen erreichbar sind.
"""
import gzip
import io
import json
import os
import re
import struct
import zipfile
from dataclasses import dataclass

from .huelle import Regel


@dataclass
class WeltKonfig:
    """Was die Skyblock-Welt erzeugt (config/skyblockbuilder). Standardwerte = Werte des Testservers."""
    festungen: bool = True          # structuresToGenerate enthält minecraft:fortress (Lohen, Witherskelette)
    end_hauptinsel: bool = True     # dimensions.End.keepMainIsland (Drache, Endstein)
    tiere_oberwelt: bool = True     # Oberwelt-Biome ohne Ozeane: Nutztiere können auf Gras spawnen (Annahme)
    quelle: str = 'Standard'

BODEN = ('minecraft:dirt', 'minecraft:grass_block', 'minecraft:podzol', 'minecraft:coarse_dirt', 'minecraft:rooted_dirt',
         'minecraft:moss_block', 'minecraft:mud', 'minecraft:mycelium')
WASSER, LAVA = 'fluid:minecraft:water', 'fluid:minecraft:lava'
# Oberwelt, Dunkelheit auf einer Plattform reicht (Skyblock): sicher
FEINDE_OBERWELT = ['zombie', 'skeleton', 'creeper', 'spider', 'enderman', 'witch', 'zombie_villager']
FEINDE_OBERWELT_ANNAHME = ['slime', 'drowned', 'phantom', 'husk', 'stray', 'pillager', 'bat']
# Nether ohne Festungen (Leere): Lohe und Witherskelett spawnen nicht
NETHER = ['zombified_piglin']
NETHER_ANNAHME = ['ghast', 'magma_cube', 'piglin', 'hoglin', 'strider', 'skeleton', 'enderman']
BLUMEN_ANNAHME = ['dandelion', 'poppy', 'azure_bluet', 'oxeye_daisy', 'cornflower', 'red_tulip', 'orange_tulip',
                  'white_tulip', 'pink_tulip']
# Mystical Agradditions: diese Pflanzen wachsen nur über ihrem Crux-Block
CRUX = {'nether_star', 'dragon_egg', 'gaia_spirit', 'awakened_draconium', 'neutronium', 'nitro_crystal'}
BRENNSTOFF = ('minecraft:coal', 'minecraft:charcoal', 'minecraft:coal_block', '#minecraft:logs', '#minecraft:planks',
              'minecraft:stick', 'minecraft:blaze_rod', 'minecraft:dried_kelp_block', 'minecraft:lava_bucket')
ROT, STROM = 'kraft:rotation', 'kraft:strom'


# ---------------- Loot ----------------
def entity_von_tabelle(tid):
    ns, _, pfad = tid.partition(':')
    if not pfad.startswith('entities/'):
        return None
    teile = pfad[len('entities/'):].split('/')
    return f'{ns}:{teile[0]}'


def _eintraege(n, out, tags, tabellen, offen, cache):
    if isinstance(n, list):
        for x in n:
            _eintraege(x, out, tags, tabellen, offen, cache)
        return
    if not isinstance(n, dict):
        return
    typ = n.get('type', '').replace('minecraft:', '')
    if typ == 'item' and isinstance(n.get('name'), str):
        out.add(n['name'])
    elif typ == 'tag' and isinstance(n.get('name'), str):
        out.update(tags.get(n['name'], ()))
    elif typ == 'loot_table':
        v = n.get('value', n.get('name'))
        if isinstance(v, str):
            out.update(_tabelle(v, tags, tabellen, offen, cache))
        elif isinstance(v, dict):
            _eintraege(v.get('pools', []), out, tags, tabellen, offen, cache)
    for k in ('children', 'entries'):
        if k in n:
            _eintraege(n[k], out, tags, tabellen, offen, cache)
    if 'pools' in n:
        _eintraege(n['pools'], out, tags, tabellen, offen, cache)


def _tabelle(tid, tags, tabellen, offen, cache):
    if tid in cache:
        return cache[tid]
    if tid in offen or tid not in tabellen:
        return frozenset()
    offen.add(tid)
    out = set()
    _eintraege(tabellen[tid], out, tags, tabellen, offen, cache)
    offen.discard(tid)
    cache[tid] = frozenset(out)
    return cache[tid]


def loot_aufloesen(tabellen, tags):
    """tabellen: id -> JSON. Ergebnis: id -> frozenset(Items). Bedingungen (Werkzeug, Zufall) zählen nicht."""
    cache = {}
    for tid in tabellen:
        _tabelle(tid, tags, tabellen, set(), cache)
    return cache


_LOOT_PFAD = re.compile(r'^data/([^/]+)/loot_tables?/(.+)\.json$')


def lade_loot(jars, ordner=()):
    """Loot-Tabellen aus Mod-Jars und Datenordnern (spätere überschreiben frühere, wie Datapacks)."""
    tab = {}
    for jar in jars:
        try:
            with zipfile.ZipFile(jar) as z:
                for name in z.namelist():
                    m = _LOOT_PFAD.match(name)
                    if m:
                        try:
                            tab[f'{m.group(1)}:{m.group(2)}'] = json.loads(z.read(name).decode('utf-8', 'replace'))
                        except ValueError:
                            pass
        except (zipfile.BadZipFile, OSError):
            continue
    for wurzel in ordner:
        for pfad, _, files in os.walk(wurzel):
            for f in files:
                rel = os.path.relpath(os.path.join(pfad, f), os.path.dirname(wurzel)).replace(os.sep, '/')
                m = _LOOT_PFAD.match(rel)
                if m:
                    try:
                        with open(os.path.join(pfad, f), encoding='utf-8') as fh:
                            tab[f'{m.group(1)}:{m.group(2)}'] = json.load(fh)
                    except ValueError:
                        pass
    return tab


# ---------------- Weltregeln ----------------
def _r(id, ein, aus, haupt=None, neben=(), annahme=False, notiz=''):
    return Regel(id='welt:' + id, typ='welt', eingaben=[frozenset(g) for g in ein], ausgaben=frozenset(aus),
                 haupt=frozenset(haupt) if haupt else None, neben=[frozenset(g) for g in neben], annahme=annahme, notiz=notiz)


def _baeume(kx):
    out = []
    boden = kx.muster(BODEN)
    for s in sorted(kx.items):
        ns, _, pfad = s.partition(':')
        if not pfad.endswith('_sapling'):
            continue
        art = pfad[:-len('_sapling')]
        aus = {f'{ns}:{art}_log', f'{ns}:{art}_leaves'} & kx.items
        if aus:
            out.append(_r('baum/' + s, [{s}, boden], aus))
    sonder = {'minecraft:mangrove_propagule': ['minecraft:mangrove_log', 'minecraft:mangrove_leaves', 'minecraft:mangrove_roots'],
              'minecraft:azalea': ['minecraft:oak_log', 'minecraft:azalea_leaves', 'minecraft:flowering_azalea_leaves'],
              'minecraft:flowering_azalea': ['minecraft:oak_log', 'minecraft:azalea_leaves', 'minecraft:flowering_azalea_leaves']}
    for s, aus in sonder.items():
        if s in kx.items:
            out.append(_r('baum/' + s, [{s}, boden], set(aus) & kx.items))
    knochenmehl = {'minecraft:bone_meal'}
    for farbe in ('red', 'brown'):
        out.append(_r(f'riesenpilz/{farbe}', [{f'minecraft:{farbe}_mushroom'}, boden, knochenmehl],
                      {f'minecraft:{farbe}_mushroom_block', 'minecraft:mushroom_stem'} & kx.items))
    for art, extra in (('crimson', ['minecraft:nether_wart_block', 'minecraft:weeping_vines']),
                       ('warped', ['minecraft:warped_wart_block', 'minecraft:twisting_vines'])):
        out.append(_r(f'riesenpilz/{art}', [{f'minecraft:{art}_fungus'}, {f'minecraft:{art}_nylium'}, knochenmehl],
                      ({f'minecraft:{art}_stem', 'minecraft:shroomlight'} | set(extra)) & kx.items))
        out.append(_r(f'nylium/{art}', [{'minecraft:netherrack'}, {f'minecraft:{art}_nylium'}, knochenmehl],
                      {f'minecraft:{art}_nylium'} & kx.items))
    out.append(_r('gras/knochenmehl', [{'minecraft:grass_block'}, knochenmehl], {'minecraft:short_grass', 'minecraft:tall_grass'} & kx.items))
    out.append(_r('gras/blumen', [{'minecraft:grass_block'}, knochenmehl], {f'minecraft:{b}' for b in BLUMEN_ANNAHME} & kx.items,
                  annahme=True, notiz='Blumen hängen vom Biom ab (angenommen: Ebene/Wald)'))
    out.append(_r('gras/ausbreiten', [{'minecraft:dirt'}, {'minecraft:grass_block'}], {'minecraft:grass_block'}))
    out.append(_r('moos/knochenmehl', [{'minecraft:moss_block'}, knochenmehl],
                  {'minecraft:moss_carpet', 'minecraft:azalea', 'minecraft:flowering_azalea', 'minecraft:short_grass'} & kx.items))
    return [r for r in out if r.ausgaben]


def _fluide(kx):
    out = [_r('generator/bruchstein', [{WASSER}, {LAVA}], {'minecraft:cobblestone'}),
           _r('generator/stein', [{WASSER}, {LAVA}], {'minecraft:stone'}),
           _r('generator/obsidian', [{WASSER}, {LAVA}], {'minecraft:obsidian'}),
           _r('generator/basalt', [{LAVA}, {'minecraft:blue_ice'}, {'minecraft:soul_soil'}], {'minecraft:basalt'})]
    eimer = 'minecraft:bucket'
    for i in sorted(kx.items):
        ns, _, pfad = i.partition(':')
        if not pfad.endswith('_bucket') or pfad in ('powder_snow_bucket', 'milk_bucket'):
            continue
        f = f'{ns}:{pfad[:-len("_bucket")]}'
        if f in kx.fluide:
            out.append(_r('eimer/leeren/' + f, [{i}], {'fluid:' + f, eimer}))
            out.append(_r('eimer/fuellen/' + f, [{eimer}, {'fluid:' + f}], {i}))
    if 'minecraft:milk_bucket' in kx.items:
        out.append(_r('melken', [{'mob:minecraft:cow', 'mob:minecraft:goat', 'mob:minecraft:mooshroom'}, {eimer}], {'minecraft:milk_bucket'}))
        if 'minecraft:milk' in kx.fluide:
            out.append(_r('eimer/leeren/milch', [{'minecraft:milk_bucket'}], {'fluid:minecraft:milk', eimer}))
    out.append(_r('eis/schmelzen', [{'minecraft:ice'}], {WASSER}))
    return out


FESTUNG_MOBS = ['blaze', 'wither_skeleton', 'skeleton', 'magma_cube']
FESTUNG_BLOECKE = ['minecraft:nether_bricks', 'minecraft:nether_brick_fence', 'minecraft:nether_brick_stairs',
                   'minecraft:nether_wart', 'minecraft:soul_sand']
NUTZTIERE = ['cow', 'sheep', 'pig', 'chicken', 'rabbit']


def _konfigregeln(kx, loot, k):
    out = []
    if k.festungen:
        for m in FESTUNG_MOBS:
            out.append(_r('festung/' + m, [{'ort:nether'}], {'mob:minecraft:' + m}, notiz='Festung im leeren Nether'))
        out.append(_r('festung/bloecke', [{'ort:nether'}], set(FESTUNG_BLOECKE) & kx.items))
        if loot.get('minecraft:chests/nether_bridge'):
            out.append(_r('festung/truhen', [{'ort:nether'}], loot['minecraft:chests/nether_bridge'], annahme=True,
                          notiz='Truhen sind endlich'))
    if k.end_hauptinsel:
        out.append(_r('end/hauptinsel', [{'ort:end'}], {'minecraft:end_stone', 'minecraft:obsidian'} & kx.items))
        out.append(_r('drache', [{'ort:end'}], {'mob:minecraft:ender_dragon'}, notiz='End-Hauptinsel bleibt (keepMainIsland)'))
    if k.tiere_oberwelt:
        for t in NUTZTIERE:
            out.append(_r('spawn/' + t, [{'minecraft:grass_block'}], {'mob:minecraft:' + t}, annahme=True,
                          notiz='Nutztiere spawnen selten auf Gras, Biom abhängig'))
    out.append(_r('huhn/ei', [{'mob:minecraft:chicken'}], {'minecraft:egg'}, notiz='Eier legen im Code'))
    # Ars-Vertraute: Spawn auf Grasblock bei Licht > 8 in allen Oberwelt-Biomen (ModEntities.genericGroundSpawn,
    # biome_modifier/*_spawn.json mit #minecraft:is_overworld). Splitter gibt es beim Zähmen (Mod-Code).
    for name, splitter in (('starbuncle', 'ars_nouveau:starbuncle_shards'), ('whirlisprig', 'ars_nouveau:whirlisprig_shards'),
                           ('drygmy', 'ars_nouveau:drygmy_shard')):
        if splitter in kx.items:
            out.append(_r('ars/spawn/' + name, [{'minecraft:grass_block'}], {'mob:ars_nouveau:' + name}, annahme=True,
                          notiz='Spawn auf Gras bei Licht > 8 (Kreaturen-Spawn, selten)'))
            out.append(_r('ars/zaehmen/' + name, [{'mob:ars_nouveau:' + name}], {splitter}, annahme=True, notiz='Zähmung im Mod-Code'))
    chimera = ['ars_nouveau:ritual_wilden_summon', 'ars_nouveau:wilden_horn', 'ars_nouveau:wilden_wing', 'ars_nouveau:wilden_spike']
    if all(c in kx.items for c in chimera) and 'ars_nouveau:ritual_brazier' in kx.items:
        out.append(_r('ars/chimera', [{c} for c in chimera], {'mob:ars_nouveau:wilden_boss'}, haupt={'ars_nouveau:ritual_brazier'},
                      annahme=True, notiz='Ritual der Wilden mit Horn, Flügel und Dorn beschwört die Chimera (nicht aus Daten belegt)'))
        out.append(_r('ars/chimera/tribut', [{'mob:ars_nouveau:wilden_boss'}], {'ars_nouveau:wilden_tribute'} & kx.items,
                      notiz='Drop der Chimera im Code'))
    blumen = {f'minecraft:{b}' for b in BLUMEN_ANNAHME} & kx.items
    setzlinge = {'minecraft:oak_sapling', 'minecraft:birch_sapling', 'minecraft:cherry_sapling', 'minecraft:mangrove_propagule'} & kx.items
    if blumen and setzlinge:
        out.append(_r('bienennest', [setzlinge, kx.muster(BODEN), blumen], {'minecraft:bee_nest', 'mob:minecraft:bee'} & (kx.items | {'mob:minecraft:bee'}),
                      annahme=True, notiz='5 % Chance, wenn ein Baum neben Blumen wächst'))
    return [r for r in out if r.ausgaben]


def wabenregeln(varianten):
    """Productive Bees: 4 Waben einer Biene <-> Wabenblock derselben Biene (Rezept mit Komponenten, im Dump allgemein)."""
    out = []
    for v in sorted(varianten):
        if v.startswith('productivebees:configurable_honeycomb{'):
            t = v[v.index('{'):]
            block = 'productivebees:configurable_comb' + t
            out.append(_r('wabe/block/' + t, [{v}], {block}))
            out.append(_r('wabe/zurueck/' + t, [{block}], {v}))
    return out


def lade_konfig(ordner):
    """Erster Ordner mit config/skyblockbuilder/*.json5 gewinnt (Testserver hat die vom Mod erzeugten Dateien)."""
    for o in ordner:
        d = os.path.join(o, 'config', 'skyblockbuilder')
        st, dim, wo = (os.path.join(d, f) for f in ('structures.json5', 'dimensions.json5', 'world.json5'))
        if not any(os.path.exists(p) for p in (st, dim, wo)):
            continue
        k = WeltKonfig(quelle=d)
        if os.path.exists(st):
            with open(st, encoding='utf-8-sig') as f:
                s = json5(f.read()).get('structuresToGenerate', {})
            drin = 'minecraft:fortress' in s.get('elements', [])
            k.festungen = drin if s.get('allow_list', True) else not drin
        if os.path.exists(dim):
            with open(dim, encoding='utf-8-sig') as f:
                e = json5(f.read()).get('End', {})
            k.end_hauptinsel = (not e.get('isCustom', True)) or bool(e.get('keepMainIsland', True))
        if os.path.exists(wo):
            with open(wo, encoding='utf-8-sig') as f:
                b = (json5(f.read()).get('biomes') or {}).get('minecraft:overworld', {})
            el = b.get('elements', [])
            k.tiere_oberwelt = (not b.get('allow_list', False) and all('ocean' in x for x in el)) or \
                               (b.get('allow_list', False) and any('ocean' not in x for x in el))
        return k
    return WeltKonfig()


def _mobs(kx, loot):
    out = []
    for m in FEINDE_OBERWELT:
        out.append(_r('spawn/' + m, [], {'mob:minecraft:' + m}))
    for m in FEINDE_OBERWELT_ANNAHME:
        out.append(_r('spawn/' + m, [], {'mob:minecraft:' + m}, annahme=True, notiz='Spawn hängt von Biom oder Höhe ab'))
    for m in NETHER:
        out.append(_r('spawn/nether/' + m, [{'ort:nether'}], {'mob:minecraft:' + m}))
    for m in NETHER_ANNAHME:
        out.append(_r('spawn/nether/' + m, [{'ort:nether'}], {'mob:minecraft:' + m}, annahme=True, notiz='Nether-Biom nötig'))
    out.append(_r('spawn/end/enderman', [{'ort:end'}], {'mob:minecraft:enderman'}))
    out.append(_r('portal/nether', [{'minecraft:obsidian'}, {'minecraft:flint_and_steel', 'minecraft:fire_charge'}], {'ort:nether'}))
    out.append(_r('portal/end', [{'minecraft:end_portal_frame'}, {'minecraft:ender_eye'}], {'ort:end'}))
    for i in sorted(kx.items):
        ns, _, pfad = i.partition(':')
        if pfad.endswith('_spawn_egg'):
            out.append(_r('ei/' + i, [{i}], {f'mob:{ns}:{pfad[:-len("_spawn_egg")]}'}))
        elif ns == 'productivebees' and pfad.startswith('spawn_egg_') and pfad != 'spawn_egg_configurable_bee':
            biene = f'productivebees:{pfad[len("spawn_egg_"):]}'
            out.append(_r('ei/' + i, [{i}], {'biene:' + biene, 'mob:' + biene}))
    out.append(_r('biene/vanilla', [{'mob:minecraft:bee'}], {'biene:minecraft:bee'}))
    out.append(_r('wither/beschwoeren', [{'minecraft:soul_sand', 'minecraft:soul_soil'}, {'minecraft:wither_skeleton_skull'}],
                  {'mob:minecraft:wither'}))
    out.append(_r('wither/stern', [{'mob:minecraft:wither'}], {'minecraft:nether_star'}, notiz='Drop im Code, nicht in der Loot-Tabelle'))
    out.append(_r('drache/ei', [{'mob:minecraft:ender_dragon'}], {'minecraft:dragon_egg'}, notiz='Ei beim ersten Sieg, im Code'))
    out.append(_r('drache/atem', [{'mob:minecraft:ender_dragon'}, {'minecraft:glass_bottle'}], {'minecraft:dragon_breath'}))
    for tid, items in loot.items():
        e = entity_von_tabelle(tid)
        if e and items:
            out.append(_r('mobloot/' + tid, [{'mob:' + e}], items))
    return out


def _abbau(kx, loot):
    """Block abbauen: Item des Blocks (gleiche ID) -> Drops der Block-Tabelle. Werkzeug und Behutsamkeit zählen nicht."""
    out = []
    for tid, items in loot.items():
        ns, _, pfad = tid.partition(':')
        if not pfad.startswith('blocks/'):
            continue
        blk = f'{ns}:{pfad[len("blocks/"):]}'
        rest = items - {blk}
        if rest:
            out.append(_r('abbau/' + blk, [{blk}], rest))
    return out


def _landwirtschaft(kx):
    out = []
    acker = [kx.muster('#minecraft:hoes') | kx.muster('mysticalagriculture:all_hoes'), kx.muster(BODEN), {WASSER}]
    out.append(_r('acker', acker, {'ort:acker'}))
    kompost = kx.muster(('#minecraft:leaves', '#minecraft:saplings', '#minecraft:flowers', 'minecraft:wheat_seeds',
                         'minecraft:short_grass', 'minecraft:kelp', 'minecraft:sugar_cane', 'minecraft:cactus', 'minecraft:wheat',
                         'minecraft:carrot', 'minecraft:potato', 'minecraft:beetroot', 'minecraft:apple', 'minecraft:melon_slice'))
    out.append(_r('komposter', [kompost], {'minecraft:bone_meal'}, haupt={'minecraft:composter'}))
    for s in sorted(kx.items):
        ns, _, pfad = s.partition(':')
        if ns not in ('mysticalagriculture', 'mysticalagradditions') or not pfad.endswith('_seeds'):
            continue
        art = pfad[:-len('_seeds')]
        essenz = f'{ns}:{art}_essence'
        if essenz not in kx.items:
            continue
        neben = []
        if art in CRUX:
            crux = f'{ns}:{art}_crux'
            if crux not in kx.items:
                continue
            neben = [{crux}]
        aus = {essenz} | ({'mysticalagriculture:fertilized_essence'} & kx.items)
        out.append(_r('ma/' + s, [{s}, {'ort:acker'}], aus, neben=neben))
    out.append(_r('bienen/wabe', [{'biene:minecraft:bee', 'mob:minecraft:bee'}, {'minecraft:beehive', 'minecraft:bee_nest'},
                                  {'minecraft:shears'}], {'minecraft:honeycomb'}))
    out.append(_r('bienen/honig', [{'biene:minecraft:bee', 'mob:minecraft:bee'}, {'minecraft:beehive', 'minecraft:bee_nest'},
                                   {'minecraft:glass_bottle'}], {'minecraft:honey_bottle'}))
    out.append(_r('seidenraupe', [{'exdeorum:silkworm'}, kx.muster('#minecraft:leaves')], {'exdeorum:infested_leaves'}))
    # Ex Deorum: Samen und Sporen per Rechtsklick auf Erde bzw. Netherrack (Item-Code, kein Rezept)
    for samen, boden, block in (('exdeorum:grass_seeds', 'minecraft:dirt', 'minecraft:grass_block'),
                                ('exdeorum:mycelium_spores', 'minecraft:dirt', 'minecraft:mycelium'),
                                ('exdeorum:crimson_nylium_spores', 'minecraft:netherrack', 'minecraft:crimson_nylium'),
                                ('exdeorum:warped_nylium_spores', 'minecraft:netherrack', 'minecraft:warped_nylium')):
        if samen in kx.items and block in kx.items:
            out.append(_r('sporen/' + samen, [{samen}, {boden}], {block}))
    # Axt entrindet Stämme und Holz (Rechtsklick in der Welt)
    axt = kx.muster('#minecraft:axes')
    for i in sorted(kx.items):
        ns, _, pfad = i.partition(':')
        if pfad.startswith('stripped_'):
            roh = f'{ns}:{pfad[len("stripped_"):]}'
            if roh in kx.items and axt:
                out.append(_r('entrinden/' + roh, [{roh}, axt], {i}))
    out.append(_r('certus/wachsen', [kx.muster(('ae2:flawless_budding_quartz', 'ae2:flawed_budding_quartz',
                                                'ae2:chipped_budding_quartz', 'ae2:damaged_budding_quartz'))],
                  kx.muster(('ae2:small_quartz_bud', 'ae2:medium_quartz_bud', 'ae2:large_quartz_bud', 'ae2:quartz_cluster'))))
    out.append(_r('amethyst/wachsen', [{'minecraft:budding_amethyst'}],
                  {'minecraft:small_amethyst_bud', 'minecraft:medium_amethyst_bud', 'minecraft:large_amethyst_bud',
                   'minecraft:amethyst_cluster'} & kx.items))
    return [r for r in out if r.ausgaben and all(r.eingaben)]


def _kraefte(kx):
    """Drehkraft, Strom, Quelle (Ars), Hitze (Create) und Großanlagen als eigene Regeln mit Hauptstation."""
    out = []
    brenn = kx.muster(BRENNSTOFF)

    def r(id, haupt, ein=(), aus=(), neben=()):
        h = kx.muster(haupt)
        if h and all(kx.muster(n) for n in neben):
            out.append(_r(id, [kx.muster(g) if not isinstance(g, frozenset) else g for g in ein], aus, haupt=h,
                          neben=[kx.muster(n) for n in neben]))
    r('rotation/kurbel', 'create:hand_crank', aus={ROT})
    r('rotation/wasserrad', ('create:water_wheel', 'create:large_water_wheel'), ein=[WASSER], aus={ROT})
    r('rotation/windmuehle', 'create:windmill_bearing', aus={ROT}, neben=[('create:white_sail', 'create:sail_frame')])
    r('rotation/motor', 'createaddition:electric_motor', ein=[STROM], aus={ROT})
    r('strom/alternator', 'createaddition:alternator', ein=[ROT], aus={STROM})
    r('strom/mek_hitze', 'mekanismgenerators:heat_generator', ein=[frozenset(brenn | {LAVA})], aus={STROM})
    r('strom/mek_sonne', ('mekanismgenerators:solar_generator', 'mekanismgenerators:advanced_solar_generator'), aus={STROM})
    r('strom/mek_wind', 'mekanismgenerators:wind_generator', aus={STROM})
    r('strom/mek_bio', 'mekanismgenerators:bio_generator', ein=['mekanism:bio_fuel'], aus={STROM})
    r('strom/mek_gas', 'mekanismgenerators:gas_burning_generator', ein=[('chem:mekanism:hydrogen', 'chem:mekanism:ethene')], aus={STROM})
    r('strom/powah_ofen', 're:^powah:furnator_', ein=[frozenset(brenn)], aus={STROM})
    r('strom/powah_sonne', 're:^powah:solar_panel_', aus={STROM})
    r('strom/powah_thermo', 're:^powah:thermo_generator_', ein=[(LAVA, 'minecraft:magma_block')], aus={STROM})
    r('strom/if_kohle', 'industrialforegoing:pitiful_generator', ein=[frozenset(brenn)], aus={STROM})
    r('strom/if_bio', 'industrialforegoing:biofuel_generator', ein=['fluid:industrialforegoing:biofuel'], aus={STROM})
    r('strom/honig', 'productivebees:honey_generator', ein=[('fluid:productivebees:honey', 'minecraft:honey_bottle')], aus={STROM})
    r('quelle', 'ars_nouveau:source_jar', aus={'kraft:quelle'},
      neben=[('ars_nouveau:volcanic_sourcelink', 'ars_nouveau:agronomic_sourcelink', 'ars_nouveau:mycelial_sourcelink',
              'ars_nouveau:vitalic_sourcelink', 'ars_nouveau:alchemical_sourcelink')])
    r('hitze', 'create:blaze_burner', ein=[frozenset(brenn)], aus={'kraft:hitze'})
    r('superhitze', 'create:blaze_burner', ein=['create:blaze_cake'], aus={'kraft:superhitze'})
    r('mek/spaltreaktor', 'mekanismgenerators:fission_reactor_casing',
      ein=['chem:mekanism:fissile_fuel', (WASSER, 'chem:mekanism:sodium')], aus={'chem:mekanism:nuclear_waste'},
      neben=['mekanismgenerators:fission_fuel_assembly', 'mekanismgenerators:control_rod_assembly', 'mekanismgenerators:fission_reactor_port'])
    r('mek/sps', 'mekanism:sps_casing', ein=['chem:mekanism:polonium', STROM], aus={'chem:mekanism:antimatter'},
      neben=['mekanism:sps_port', 'mekanism:supercharged_coil'])
    r('mek/schweres_wasser', 'mekanism:electric_pump', ein=[WASSER, STROM], aus={'fluid:mekanism:heavy_water'},
      neben=['mekanism:upgrade_filter'])
    # AE2: Materiekondensator vernichtet beliebige Items; mit Speicherkomponente entstehen Materiebälle/Singularitäten
    r('ae2/kondensator/ball', 'ae2:condenser', ein=[frozenset(kx.items - {'ae2:condenser'})], aus=kx.muster('ae2:matter_ball'),
      neben=[('ae2:cell_component_1k', 'ae2:cell_component_4k', 'ae2:cell_component_16k', 'ae2:cell_component_64k',
              'ae2:cell_component_256k')])
    r('ae2/kondensator/singularitaet', 'ae2:condenser', ein=[frozenset(kx.items - {'ae2:condenser'})], aus=kx.muster('ae2:singularity'),
      neben=[('ae2:cell_component_64k', 'ae2:cell_component_256k')])
    # Industrial Foregoing: Schlachtfabrik macht aus Mobs Pinkschleim und Fleisch (Maschinencode, kein Rezept)
    r('if/schlachtfabrik', 'industrialforegoing:mob_slaughter_factory', ein=[STROM],
      aus={'fluid:industrialforegoing:pink_slime', 'fluid:industrialforegoing:meat'})
    # Industrial Foregoing: Latex-Verarbeitung ist im Maschinencode, kein Rezept im Dump
    r('if/latex', 'industrialforegoing:latex_processing_unit', ein=['fluid:industrialforegoing:latex', WASSER, STROM],
      aus=kx.muster(('industrialforegoing:dryrubber', 'industrialforegoing:tinydryrubber')))
    return out


def _angeln(kx, loot):
    out = []
    for tabelle, annahme in (('minecraft:gameplay/fishing/fish', False), ('minecraft:gameplay/fishing/junk', False),
                             ('minecraft:gameplay/fishing/treasure', True)):
        if loot.get(tabelle):
            out.append(_r('angeln/' + tabelle.rsplit('/', 1)[1], [{'minecraft:fishing_rod'}, {WASSER}], loot[tabelle],
                          annahme=annahme, notiz='Schätze nur in offenem Wasser' if annahme else ''))
    if loot.get('minecraft:gameplay/piglin_bartering'):
        out.append(_r('tausch/piglin', [{'mob:minecraft:piglin'}, {'minecraft:gold_ingot'}], loot['minecraft:gameplay/piglin_bartering']))
    return out


def weltregeln(kx, loot, konfig=None):
    k = konfig or WeltKonfig()
    return (_baeume(kx) + _fluide(kx) + _mobs(kx, loot) + _abbau(kx, loot) + _landwirtschaft(kx) + _kraefte(kx)
            + _angeln(kx, loot) + _konfigregeln(kx, loot, k))


# ---------------- Start ----------------
def json5(txt):
    """Genug JSON5 für die Skyblock-Builder-Dateien: Kommentare und Kommas vor ] oder } entfernen."""
    out, i, n, in_str = [], 0, len(txt), False
    while i < n:
        c = txt[i]
        if in_str:
            out.append(c)
            if c == '\\':
                out.append(txt[i + 1:i + 2]); i += 2; continue
            if c == '"':
                in_str = False
            i += 1
            continue
        if c == '"':
            in_str = True; out.append(c); i += 1; continue
        if txt.startswith('//', i):
            j = txt.find('\n', i)
            i = n if j < 0 else j
            continue
        if txt.startswith('/*', i):
            j = txt.find('*/', i + 2)
            i = n if j < 0 else j + 2
            continue
        out.append(c)
        i += 1
    rein = re.sub(r',(\s*[\]}])', r'\1', ''.join(out))
    return json.loads(rein)


def _nbt_lesen(f, tag):
    def unp(fmt, n):
        return struct.unpack(fmt, f.read(n))[0]
    if tag == 1: return unp('>b', 1)
    if tag == 2: return unp('>h', 2)
    if tag == 3: return unp('>i', 4)
    if tag == 4: return unp('>q', 8)
    if tag == 5: return unp('>f', 4)
    if tag == 6: return unp('>d', 8)
    if tag == 7: return f.read(unp('>i', 4))
    if tag == 8: return f.read(unp('>H', 2)).decode('utf-8')
    if tag == 9:
        t, n = unp('>b', 1), unp('>i', 4)
        return [_nbt_lesen(f, t) for _ in range(n)]
    if tag == 10:
        d = {}
        while True:
            t = unp('>b', 1)
            if t == 0:
                return d
            k = _nbt_lesen(f, 8)
            d[k] = _nbt_lesen(f, t)
    if tag == 11: return [unp('>i', 4) for _ in range(unp('>i', 4))]
    if tag == 12: return [unp('>q', 8) for _ in range(unp('>i', 4))]
    raise ValueError(f'NBT-Tag {tag}')


def lade_nbt(pfad):
    with gzip.open(pfad, 'rb') as g:
        f = io.BytesIO(g.read())
    if struct.unpack('>b', f.read(1))[0] != 10:
        raise ValueError(f'{pfad}: kein NBT-Compound')
    _nbt_lesen(f, 8)
    return _nbt_lesen(f, 10)


def vorlage_bloecke(pfad):
    d = lade_nbt(pfad)
    pal = d.get('palette') or []
    return {pal[b['state']]['Name'] for b in d.get('blocks', []) if 0 <= b.get('state', -1) < len(pal)}


def start_ressourcen(pack, items):
    """Startinventar + Blöcke der Startinseln. Liefert (Menge, Notizen je Quelle)."""
    start, woher = set(), {}
    pfad = os.path.join(pack, 'config', 'skyblockbuilder', 'starter_inventory.json5')
    if os.path.exists(pfad):
        with open(pfad, encoding='utf-8-sig') as f:
            for e in json5(f.read()).get('items', []):
                it = (e.get('Item') or {}).get('id')
                if it:
                    start.add(it)
                    woher[it] = 'Startinventar'
    inseln = sorted(os.path.join(pack, 'config', 'skyblockbuilder', 'templates', 'islands', f)
                    for f in os.listdir(os.path.join(pack, 'config', 'skyblockbuilder', 'templates', 'islands'))
                    if f.endswith('.nbt')) if os.path.isdir(os.path.join(pack, 'config', 'skyblockbuilder', 'templates', 'islands')) else []
    # Nur Blöcke, die auf JEDER Insel liegen: der Spieler wählt eine
    gemeinsam = None
    for p in inseln:
        b = vorlage_bloecke(p)
        gemeinsam = b if gemeinsam is None else gemeinsam & b
    for b in sorted(gemeinsam or ()):
        res = 'fluid:' + b if b in ('minecraft:water', 'minecraft:lava') else b
        if res.startswith('fluid:') or b in items:
            start.add(res)
            woher.setdefault(res, 'Startinsel')
    return start, woher

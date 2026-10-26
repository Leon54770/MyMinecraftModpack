"""Rezepte aus dem Testserver-Dump als Regeln (huelle.Regel).

Jeder Rezepttyp hat einen Leser (Zutaten, Ergebnisse) und eine Stationsangabe (welche Maschine, welche
Nebenteile, welche Kraft: Drehkraft, Strom, Quelle, Hitze). Typen ohne Leser werden gezählt und im Bericht
genannt, sie fließen nicht stillschweigend ein.

Ergebnisse mit Chance > 0 zählen als erreichbar (Sieb, Zentrifuge). Mengen zählen nicht.
"""
import re
from collections import Counter, namedtuple

from .huelle import Regel

V = namedtuple('V', 'haupt neben kraft', defaults=(None, (), ()))
ROT, STROM, QUELLE = 'kraft:rotation', 'kraft:strom', 'kraft:quelle'
VARIANTEN_KOMPONENTEN = ('productivebees:bee_type',)
HAMMER = 're:^exdeorum:(wooden|stone|iron|golden|diamond|netherite)_hammer$'
FASS = 're:^exdeorum:[a-z_]+_barrel$'
# Feuerfeste Fässer (Ex Deorum BarrelMaterial.fireproof, BarrelBlockEntity.isHotFluid: Holzfässer brennen bei heißem Fluid)
FASS_HEISS = ['exdeorum:stone_barrel', 'exdeorum:crimson_barrel', 'exdeorum:warped_barrel', 'exdeorum:hellbark_barrel']
HEISSE_FLUIDE = {'minecraft:lava'}
KOCHHITZE = ('farmersdelight:stove', 'minecraft:campfire', 'minecraft:soul_campfire', 'minecraft:magma_block',
             'fluid:minecraft:lava', 'minecraft:flint_and_steel')


def _m(name, strom=True, neben=()):
    return [V('mekanism:' + name, tuple(neben), (STROM,) if strom else ())]


STATIONEN = {
    'hand': [V()],
    'minecraft:crafting': [V('minecraft:crafting_table')],
    'minecraft:smelting': [V('re:^minecraft:furnace$|^ironfurnaces:[a-z_]+_furnace$'),
                           V('mekanism:energized_smelter', (), (STROM,)),
                           V('create:encased_fan', (), (ROT, 'fluid:minecraft:lava'))],
    'minecraft:blasting': [V('minecraft:blast_furnace'), V('create:encased_fan', (), (ROT, 'fluid:minecraft:lava'))],
    'minecraft:smoking': [V('minecraft:smoker'),
                          V('create:encased_fan', (), (ROT, ('minecraft:campfire', 'minecraft:flint_and_steel')))],
    'minecraft:campfire_cooking': [V(('minecraft:campfire', 'minecraft:soul_campfire'))],
    'minecraft:stonecutting': [V('minecraft:stonecutter'), V('create:mechanical_saw', (), (ROT,))],
    'minecraft:smithing': [V('minecraft:smithing_table')],
    'create:milling': [V(('create:millstone', 'create:crushing_wheel'), (), (ROT,))],
    'create:crushing': [V('create:crushing_wheel', (), (ROT,))],
    'create:cutting': [V('create:mechanical_saw', (), (ROT,))],
    'create:deploying': [V('create:deployer', (), (ROT,))],
    'create:item_application': [V()],
    'create:mixing': [V('create:mechanical_mixer', ('create:basin',), (ROT,))],
    'create:compacting': [V('create:mechanical_press', ('create:basin',), (ROT,))],
    'create:pressing': [V('create:mechanical_press', (), (ROT,))],
    'create:splashing': [V('create:encased_fan', (), (ROT, 'fluid:minecraft:water'))],
    'create:haunting': [V('create:encased_fan', (), (ROT, ('minecraft:soul_campfire', 'minecraft:soul_sand', 'minecraft:soul_soil')))],
    'create:emptying': [V('create:item_drain')],
    'create:filling': [V('create:spout')],
    'create:sandpaper_polishing': [V(('create:sand_paper', 'create:red_sand_paper'))],
    'create:mechanical_crafting': [V('create:mechanical_crafter', (), (ROT,))],
    'createaddition:charging': [V('createaddition:tesla_coil', (), (STROM,))],
    'createaddition:rolling': [V('createaddition:rolling_mill', (), (ROT,))],
    'create_mechanical_extruder:extruding': [V('re:^create_mechanical_extruder:mechanical_[a-z_]*extruder$', (), (ROT,))],
    'exdeorum:sieve': [V('re:^exdeorum:(?!mechanical_)(?![a-z_]*compressed)[a-z_]+_sieve$'),
                       V('exdeorum:mechanical_sieve', (), (STROM,))],
    'exdeorum:compressed_sieve': [V('re:^exdeorum:[a-z_]+_compressed_sieve$')],
    'exdeorum:hammer': [V(HAMMER), V('exdeorum:mechanical_hammer', (), (STROM,))],
    'exdeorum:compressed_hammer': [V('re:^exdeorum:compressed_[a-z]+_hammer$')],
    'exdeorum:crook': [V(('exdeorum:crook', 'exdeorum:bone_crook'))],
    'exdeorum:lava_crucible': [V(('exdeorum:porcelain_crucible', 'exdeorum:crimson_crucible', 'exdeorum:warped_crucible',
                                  'exdeorum:hellbark_crucible'), (), ('hitze:exdeorum',))],
    'exdeorum:water_crucible': [V('re:^exdeorum:(?!porcelain|unfired|crimson|warped|hellbark)[a-z_]+_crucible$')],
    'fass': [V(FASS)],
    'fass_heiss': [V(tuple(FASS_HEISS))],
    'mekanism:crushing': _m('crusher'), 'mekanism:enriching': _m('enrichment_chamber'),
    'mekanism:combining': _m('combiner'), 'mekanism:compressing': _m('osmium_compressor'),
    'mekanism:injecting': _m('chemical_injection_chamber'), 'mekanism:purifying': _m('purification_chamber'),
    'mekanism:metallurgic_infusing': _m('metallurgic_infuser'), 'mekanism:sawing': _m('precision_sawmill'),
    'mekanism:painting': _m('painting_machine'), 'mekanism:pigment_extracting': _m('pigment_extractor'),
    'mekanism:pigment_mixing': _m('pigment_mixer'), 'mekanism:chemical_infusing': _m('chemical_infuser'),
    'mekanism:dissolution': _m('chemical_dissolution_chamber'), 'mekanism:oxidizing': _m('chemical_oxidizer'),
    'mekanism:crystallizing': _m('chemical_crystallizer'), 'mekanism:washing': _m('chemical_washer'),
    'mekanism:separating': _m('electrolytic_separator'), 'mekanism:reaction': _m('pressurized_reaction_chamber'),
    'mekanism:rotary': _m('rotary_condensentrator'), 'mekanism:centrifuging': _m('isotopic_centrifuge'),
    'mekanism:nucleosynthesizing': _m('antiprotonic_nucleosynthesizer'),
    'mekanism:activating': _m('solar_neutron_activator', strom=False),
    'mekanism:evaporating': _m('thermal_evaporation_controller', strom=False,
                               neben=('mekanism:thermal_evaporation_valve', 'mekanism:thermal_evaporation_block')),
    'mekanism:chemical_conversion': [V()],
    'ae2:inscriber': [V('ae2:inscriber', (), (STROM,))],
    'ae2:charger': [V('ae2:charger', (), ((STROM, 'ae2:crank'),))],
    'ae2:transform': [V()],
    'ae2:entropy': [V('ae2:entropy_manipulator', (), (STROM,))],
    'ae2:storage_cell_disassembly': [V()],
    'ars_nouveau:enchanting_apparatus': [V('ars_nouveau:enchanting_apparatus', ('ars_nouveau:arcane_pedestal',))],
    'ars_nouveau:imbuement': [V('ars_nouveau:imbuement_chamber')],
    'ars_nouveau:glyph': [V('ars_nouveau:scribes_table')],
    'ars_nouveau:crush': [V('ars_nouveau:glyph_crush', (('ars_nouveau:novice_spell_book', 'ars_nouveau:apprentice_spell_book',
                                                        'ars_nouveau:archmage_spell_book'),))],
    'ars_nouveau:budding_conversion': [V()],
    'ars_nouveau:dispel_entity': [V('ars_nouveau:glyph_dispel', (('ars_nouveau:novice_spell_book', 'ars_nouveau:apprentice_spell_book',
                                                                 'ars_nouveau:archmage_spell_book'),))],
    'topf': [V('re:^botanypots:[a-z_]*botany_pot$')],
    'farmersdelight:cooking': [V('farmersdelight:cooking_pot', (), (KOCHHITZE,))],
    'farmersdelight:cutting': [V('farmersdelight:cutting_board')],
    'framedblocks:frame': [V('framedblocks:framing_saw')],
    'functionalstorage:custom_compacting': [V('re:^functionalstorage:(simple_)?compacting_drawer$')],
    'industrialforegoing:dissolution_chamber': [V('industrialforegoing:dissolution_chamber', (), (STROM,))],
    'industrialforegoing:fluid_extractor': [V('industrialforegoing:fluid_extractor', (), (STROM,))],
    'industrialforegoing:laser_drill_ore': [V('industrialforegoing:ore_laser_base', ('industrialforegoing:laser_drill',), (STROM,))],
    'industrialforegoing:laser_drill_fluid': [V('industrialforegoing:fluid_laser_base', ('industrialforegoing:laser_drill',), (STROM,))],
    'industrialforegoing:stonework_generate': [V('industrialforegoing:material_stonework_factory', (), (STROM,))],
    'industrialforegoing:crusher': [V('industrialforegoing:material_stonework_factory', (), (STROM,))],
    'powah:energizing': [V('powah:energizing_orb', ('re:^powah:energizing_rod_',), (STROM,))],
    'mysticalagriculture:infusion': [V('mysticalagriculture:infusion_altar', ('mysticalagriculture:infusion_pedestal',))],
    'mysticalagriculture:awakening': [V('mysticalagriculture:awakening_altar', ('mysticalagriculture:awakening_pedestal',
                                                                                'mysticalagriculture:essence_vessel'))],
    'mysticalagriculture:reprocessor': [V('re:^mysticalagriculture:[a-z_]*reprocessor$')],
    'mysticalagriculture:soulium_spawner': [V('mysticalagriculture:soulium_spawner')],
    'mysticalagriculture:soul_extraction': [V('mysticalagriculture:soul_extractor', ('mysticalagriculture:soul_jar',))],
    'productivebees:advanced_beehive': [V('re:^productivebees:advanced_[a-z_]+beehive$')],
    'productivebees:centrifuge': [V('productivebees:centrifuge'), V('productivebees:powered_centrifuge', (), (STROM,)),
                                  V('productivebees:heated_centrifuge', (), (STROM,))],
    'productivebees:bottler': [V('productivebees:bottler')],
    'productivebees:bee_breeding': [V()], 'productivebees:bee_conversion': [V()], 'productivebees:bee_spawning': [V()],
}
STATIONEN['createsifter:sifting'] = [V(('createsifter:sifter', 'createsifter:brass_sifter'), (), (ROT,))]
STATIONEN['createsifter:sifting_advanced'] = [V('createsifter:brass_sifter', (), (ROT,))]

# Typen ohne Item-Ergebnis oder ohne Bedeutung für die Erreichbarkeit
OHNE_ERGEBNIS = {
    'almostunified:client_recipe_tracker', 'ae2:matter_cannon', 'ae2:crafting_unit_transform', 'ars_nouveau:caster_tome',
    'ars_nouveau:armor_upgrade', 'ars_nouveau:enchantment', 'ars_nouveau:prestidigitation', 'ars_nouveau:reactive_enchantment',
    'ars_nouveau:spell_write', 'ars_nouveau:scry_ritual', 'ars_nouveau:alakarkinos_conversion',
    'ars_nouveau:summon_ritual', 'botanypots:soil', 'botanypots:fertilizer', 'botanypots:pot_interaction',
    'createaddition:liquid_burning', 'exdeorum:crucible_heat_source', 'ironfurnaces:generator_blasting',
    'mekanism:energy_conversion', 'mysticalagriculture:enchanter', 'productivebees:block_conversion',
    'productivebees:bee_nbt_changer', 'productivebees:bee_fishing',
}
_ID = re.compile(r'^[a-z0-9_.-]+:[a-z0-9_./-]+$')


class Kontext:
    def __init__(self, items, tags, fluide=(), chemikalien=(), loot=None):
        self.items = set(items)
        self.tags = {k.lstrip('#'): list(v) for k, v in dict(tags).items()}
        self.fluide = set(fluide)
        self.chemikalien = set(chemikalien)
        self.loot = loot if loot is not None else {}     # Tabellen-ID -> frozenset(Items)
        self.hitzequellen = set()
        self.ohne_leser = Counter()
        self.unbekannte_zutat = Counter()
        self.fehlende_station = Counter()
        self.unklar = 0                 # Zutaten, die das JSON nicht auflöst (Rückfall: aufgelöster Dump)
        self._muster = {}

    def tag(self, t):
        return frozenset(self.tags.get(t.lstrip('#'), ()))

    def muster(self, spec):
        if isinstance(spec, (list, tuple, set, frozenset)):
            return frozenset().union(*(self.muster(s) for s in spec)) if spec else frozenset()
        if spec in self._muster:
            return self._muster[spec]
        if spec.startswith('re:'):
            rx = re.compile(spec[3:])
            r = frozenset(i for i in self.items if rx.search(i))
        elif spec.startswith('#'):
            r = self.tag(spec[1:])
        elif spec == 'hitze:exdeorum':
            r = frozenset(self.hitzequellen) or frozenset({'minecraft:torch', 'fluid:minecraft:lava'})
        elif spec.split(':', 1)[0] in ('kraft', 'ort', 'fluid', 'chem', 'mob', 'biene', 'seele'):
            r = frozenset({spec})
        else:
            r = frozenset({spec}) if spec in self.items else frozenset()
        self._muster[spec] = r
        return r

    def _nach_pfad(self, t, bekannt, praefix, art):
        """Fluid- und Chemie-Tags stehen nicht im Dump: Mitglieder sind die bekannten Fluide mit gleichem Pfad
        (c:honey -> create:honey, productivebees:honey). Ohne Treffer bleibt die Gruppe leer und wird gezählt."""
        pfad = t.split(':', 1)[-1]
        r = {f for f in bekannt if f.split(':', 1)[-1] == pfad}
        if not r:
            self.unbekannte_zutat[f'{art}-Tag ohne {art}: {t}'] += 1
        return frozenset(praefix + f for f in r)

    def fluid_tag(self, t):
        return self._nach_pfad(t, self.fluide, 'fluid:', 'Fluid')

    def chem_tag(self, t):
        return self._nach_pfad(t, self.chemikalien, 'chem:', 'Chemie')

    # ---- Zutaten ----
    def zutat(self, n, art='item'):
        if n is None:
            return frozenset()
        if isinstance(n, str):
            if n.startswith('#'):
                return {'item': self.tag, 'fluid': self.fluid_tag, 'chem': self.chem_tag}[art](n[1:])
            return frozenset({_praefix(art) + n})
        if isinstance(n, list):
            return frozenset().union(*(self.zutat(x, art) for x in n)) if n else frozenset()
        if not isinstance(n, dict):
            return frozenset()
        typ = n.get('type', '')
        if typ == 'neoforge:compound':
            return self.zutat(n.get('children', []), art)
        if typ == 'neoforge:difference':
            return self.zutat(n.get('base'), art) - self.zutat(n.get('subtracted'), art)
        if typ == 'neoforge:intersection':
            teile = [self.zutat(c, art) for c in n.get('children', [])]
            return frozenset.intersection(*teile) if teile else frozenset()
        if typ == 'mysticalagriculture:crop_component':
            crop = n.get('crop', '')
            teil = {'essence': '_essence', 'seed': '_seeds', 'seeds': '_seeds'}.get(n.get('component'))
            if teil and ':' in crop:
                return frozenset({crop + teil})
            self.unklar += 1            # 'material' steht nur im Mod-Code (z. B. Zombie -> verrottetes Fleisch)
            return frozenset()
        if typ == 'mysticalagriculture:all_hoes':
            return self.tag('minecraft:hoes')
        if 'chemical' in n:
            return frozenset({'chem:' + n['chemical']})
        if art == 'chem' and 'tag' in n:
            return self.chem_tag(n['tag'])
        if art == 'fluid' or ist_fluid(n):
            if isinstance(n.get('fluid'), dict):
                return frozenset({'fluid:' + n['fluid'].get('id', '')})
            if isinstance(n.get('fluid'), str):
                return frozenset({'fluid:' + n['fluid']})
            if 'fluids' in n:
                f = n['fluids']
                return frozenset('fluid:' + x for x in ([f] if isinstance(f, str) else f))
            if 'tag' in n:
                return self.fluid_tag(n['tag'])
            if 'id' in n:
                return frozenset({'fluid:' + n['id']})
        if 'items' in n:
            basis = self.zutat(n['items'] if isinstance(n['items'], list) else
                               ({'tag': n['items'][1:]} if n['items'].startswith('#') else {'item': n['items']}))
            return varianten(basis, n.get('components'))
        if isinstance(n.get('item'), str):
            return varianten(frozenset({n['item']}), n.get('components'))
        if isinstance(n.get('item'), dict):
            return self.zutat(n['item'], art)
        if isinstance(n.get('tag'), str):
            return self.tag(n['tag'])
        if isinstance(n.get('id'), str):
            return varianten(frozenset({n['id']}), n.get('components'))
        if isinstance(n.get('block'), str):
            return frozenset({n['block']})
        if isinstance(n.get('block_tag'), str):
            return self.tag(n['block_tag'])
        if 'ingredient' in n:
            return self.zutat(n['ingredient'], art)
        self.unbekannte_zutat[typ or ','.join(sorted(n)[:3])] += 1
        self.unklar += 1
        return frozenset()

    # ---- Ergebnisse ----
    def ergebnis(self, n, art='item'):
        if n is None:
            return frozenset()
        if isinstance(n, str):
            return frozenset({_praefix(art) + n}) if _ID.match(n) else frozenset()
        if isinstance(n, list):
            return frozenset().union(*(self.ergebnis(x, art) for x in n)) if n else frozenset()
        if not isinstance(n, dict):
            return frozenset()
        for k in ('chance', 'weight'):
            if isinstance(n.get(k), (int, float)) and n[k] <= 0:
                return frozenset()
        if 'stack' in n:
            return self.ergebnis(n['stack'], art)
        if isinstance(n.get('item'), dict):
            return self.ergebnis(n['item'], art)
        if 'items' in n:
            return varianten(self.zutat(n['items'] if isinstance(n['items'], list) else
                                        ({'tag': n['items'][1:]} if n['items'].startswith('#') else {'item': n['items']})),
                             n.get('components'))
        if isinstance(n.get('item'), str):
            return varianten(frozenset({n['item']}), n.get('components'))
        if isinstance(n.get('tag'), str):
            return self.tag(n['tag'])
        if isinstance(n.get('value'), str):
            return frozenset({n['value']})
        if isinstance(n.get('block'), dict):
            return self.ergebnis(n['block'], art)
        if 'drops' in n:
            return self.ergebnis(n['drops'], art)
        if isinstance(n.get('fluid'), (str, dict)):
            f = n['fluid'] if isinstance(n['fluid'], str) else n['fluid'].get('id', '')
            return frozenset({'fluid:' + f})
        if isinstance(n.get('id'), str):
            if art == 'item' and 'amount' in n and 'count' not in n:
                return frozenset({'fluid:' + n['id']})            # Create: Fluid-Ergebnis {id, amount}
            if art == 'item':
                return varianten(frozenset({n['id']}), n.get('components'))
            return frozenset({_praefix(art) + n['id']})
        return frozenset()


def _praefix(art):
    return {'item': '', 'fluid': 'fluid:', 'chem': 'chem:'}[art]


def ist_fluid(n):
    return isinstance(n, dict) and 'amount' in n and 'chemical' not in n and (
        'fluid' in n or 'fluids' in n or (n.get('type', '').startswith('neoforge:') and 'tag' in n))


def varianten(basis, comps):
    """Komponenten, die eine eigene Item-Art bilden (Productive-Bees-Waben, Bienen-Eier), werden Teil der ID."""
    if not comps:
        return basis
    for k in VARIANTEN_KOMPONENTEN:
        if isinstance(comps.get(k), str):
            return frozenset(f'{b}{{{comps[k]}}}' for b in basis)
    ed = comps.get('minecraft:entity_data')
    if isinstance(ed, dict) and isinstance(ed.get('type'), str):
        return frozenset(f'{b}{{{ed["type"]}}}' for b in basis)
    return basis


# ---------------- Leser ----------------
Teil = namedtuple('Teil', 'eingaben ausgaben station neben haupt annahme', defaults=('', (), None, False))


def _gruppen(kx, liste, art='item'):
    return [kx.zutat(z, art) for z in (liste or [])]


def _crafting(js, kx, rid):
    if 'ore_chunk' in js and isinstance(js.get('ore'), str):
        # Ex Deorum: 2×2 Erzbrocken -> Erzblock aus dem Tag (Ergebnis wählt der Mod aus dem Tag)
        return [Teil([kx.zutat(js['ore_chunk'])], kx.tag(js['ore']), 'hand')]
    if 'result' not in js:
        return []
    aus = kx.ergebnis(js['result'])
    if 'pattern' in js:
        zeilen = js['pattern']
        zeichen = sorted(set(''.join(zeilen)) - {' '})
        ein = [kx.zutat(js['key'][z]) for z in zeichen if z in js.get('key', {})]
        klein = len(zeilen) <= 2 and max((len(z) for z in zeilen), default=0) <= 2
    elif 'ingredients' in js:
        ein = _gruppen(kx, js['ingredients'])
        klein = len(js['ingredients']) <= 4
    else:
        return []
    return [Teil(ein, aus, 'hand' if klein else 'minecraft:crafting')]


def _einfach(ein_key='ingredient', aus_key='result'):
    def lese(js, kx, rid):
        if aus_key not in js:
            return []
        return [Teil([kx.zutat(js.get(ein_key))], kx.ergebnis(js[aus_key]), '')]
    return lese


def _smithing(js, kx, rid):
    if 'result' not in js:
        return []
    ein = [kx.zutat(js[k]) for k in ('template', 'base', 'addition') if k in js]
    return [Teil(ein, kx.ergebnis(js['result']), '')]


def _create(js, kx, rid):
    ein = []
    for z in js.get('ingredients', []):
        ein.append(kx.zutat(z))
    hitze = js.get('heat_requirement')
    if hitze == 'heated':
        ein.append(frozenset({'kraft:hitze', 'kraft:superhitze'}))
    elif hitze == 'superheated':
        ein.append(frozenset({'kraft:superhitze'}))
    aus = kx.ergebnis(js.get('results', []))
    return [Teil(ein, aus, '')] if aus else []


def _create_mech(js, kx, rid):
    t = _crafting(js, kx, rid)
    return [t[0]._replace(station='')] if t else []


SCHRITT_STATION = {'create:deploying': 'create:deployer', 'create:pressing': 'create:mechanical_press',
                   'create:cutting': 'create:mechanical_saw', 'create:filling': 'create:spout'}


def _sequenz(js, kx, rid):
    ein = [kx.zutat(js.get('ingredient'))]
    stationen = []
    for s in js.get('sequence', []):
        for z in s.get('ingredients', [])[1:]:
            ein.append(kx.zutat(z))
        st = SCHRITT_STATION.get(s.get('type'))
        if st and st not in stationen:
            stationen.append(st)
    aus = kx.ergebnis(js.get('results', [])) | kx.ergebnis(js.get('transitional_item'))
    ein.append(frozenset({ROT}))
    if not stationen:
        return [Teil(ein, aus, 'hand')]
    haupt = kx.muster(stationen[0])
    neben = [kx.muster(s) for s in stationen[1:]]
    return [Teil(ein, aus, 'hand', neben, haupt)]


def _sifter(js, kx, rid):
    mesh = (js.get('mesh') or {}).get('id') or (js.get('mesh') or {}).get('item')
    erw = bool(js.get('advancedSifter') or js.get('requiresAdvancedSifter') or (mesh or '').startswith('createsifter:advanced_'))
    aus = kx.ergebnis(js.get('results', []))
    if not aus:
        return []
    neben = [kx.muster(mesh)] if mesh else []
    return [Teil([kx.zutat(js.get('input'))], aus, 'createsifter:sifting_advanced' if erw else 'createsifter:sifting', neben)]


def _menge_positiv(js):
    m = js.get('result_amount', 1)
    if isinstance(m, dict):
        if m.get('type') == 'minecraft:binomial':
            return m.get('n', 0) > 0 and m.get('p', 0) > 0
        if m.get('type') == 'minecraft:uniform':
            return m.get('max', 0) > 0
        return m.get('value', 1) > 0
    return m > 0


def _exd_sieb(js, kx, rid):
    if not _menge_positiv(js):
        return []
    mesh = (js.get('mesh') or {}).get('item')
    return [Teil([kx.zutat(js.get('ingredient'))], kx.ergebnis(js.get('result')), '', [kx.muster(mesh)] if mesh else [])]


def _exd_hammer(js, kx, rid):
    if not _menge_positiv(js):
        return []
    return [Teil([kx.zutat(js.get('ingredient'))], kx.ergebnis(js.get('result')), '')]


def _exd_crook(js, kx, rid):
    p = js.get('block_predicate') or {}
    blk = frozenset({p['block']}) if 'block' in p else kx.tag(p.get('block_tag', ''))
    if js.get('chance', 1) <= 0:
        return []
    return [Teil([blk], kx.ergebnis(js.get('result')), '')]


def _exd_tiegel(js, kx, rid):
    f = js.get('fluid') or {}
    return [Teil([kx.zutat(js.get('ingredient'))], frozenset({'fluid:' + f.get('id', '')}), '')]


def _heiss(*fluide):
    return any(f.replace('fluid:', '') in HEISSE_FLUIDE for g in fluide for f in g)


def _exd_kompost(js, kx, rid):
    return [Teil([kx.zutat(js.get('ingredient'))], frozenset({'minecraft:dirt'}), 'fass')]


def _exd_fass_mix(js, kx, rid):
    fl = kx.zutat(js.get('fluid'), 'fluid')
    return [Teil([kx.zutat(js.get('ingredient')), fl], kx.ergebnis(js.get('result')), 'fass_heiss' if _heiss(fl) else 'fass')]


def _exd_fass_fluid(js, kx, rid):
    # Der Zusatz steht als Quellblock auf dem Fass; ob das Fass brennt, entscheidet nur das Grundfluid darin
    a, b = kx.zutat(js.get('base_fluid'), 'fluid'), kx.zutat(js.get('additive_fluid'), 'fluid')
    return [Teil([a, b], kx.ergebnis(js.get('result')), 'fass_heiss' if _heiss(a) else 'fass')]


def _exd_fass_wandel(js, kx, rid):
    a = kx.zutat(js.get('base_fluid'), 'fluid')
    kat = kx.zutat(js.get('catalyst'))
    aus = frozenset({'fluid:' + js.get('result_fluid', '')}) | kx.ergebnis(js.get('byproducts', []))
    return [Teil([a, kat], aus, 'fass_heiss' if _heiss(a) else 'fass')]


MEK_EIN = {'input': 'item', 'item_input': 'item', 'main_input': 'item', 'extra_input': 'item',
           'fluid_input': 'fluid', 'chemical_input': 'chem', 'left_input': 'chem', 'right_input': 'chem'}
MEK_AUS = {'item_output': 'item', 'main_output': 'item', 'secondary_output': 'item', 'chemical_output': 'chem',
           'fluid_output': 'fluid', 'left_chemical_output': 'chem', 'right_chemical_output': 'chem'}
MEK_INPUT_ART = {'mekanism:evaporating': 'fluid', 'mekanism:separating': 'fluid', 'mekanism:activating': 'chem',
                 'mekanism:centrifuging': 'chem', 'mekanism:crystallizing': 'chem'}
MEK_OUTPUT_ART = {'mekanism:activating': 'chem', 'mekanism:centrifuging': 'chem', 'mekanism:chemical_conversion': 'chem',
                  'mekanism:chemical_infusing': 'chem', 'mekanism:dissolution': 'chem', 'mekanism:oxidizing': 'chem',
                  'mekanism:pigment_extracting': 'chem', 'mekanism:pigment_mixing': 'chem', 'mekanism:washing': 'chem',
                  'mekanism:evaporating': 'fluid'}


def _mekanism(typ):
    def lese(js, kx, rid):
        if typ == 'mekanism:rotary':
            # Rotationskondensator: zwei getrennte Richtungen, nicht beide Eingaben zugleich
            teile = []
            if 'fluid_input' in js and 'chemical_output' in js:
                teile.append(Teil([kx.zutat(js['fluid_input'], 'fluid')], kx.ergebnis(js['chemical_output'], 'chem'), ''))
            if 'chemical_input' in js and 'fluid_output' in js:
                teile.append(Teil([kx.zutat(js['chemical_input'], 'chem')], kx.ergebnis(js['fluid_output'], 'fluid'), ''))
            return teile
        ein, aus = [], frozenset()
        for k, art in MEK_EIN.items():
            if k in js:
                if k == 'input':
                    art = MEK_INPUT_ART.get(typ, 'item')
                ein.append(kx.zutat(js[k], art))
        for k, art in MEK_AUS.items():
            if k in js and (k != 'secondary_output' or js.get('secondary_chance', 1) > 0):
                aus |= kx.ergebnis(js[k], art)
        if isinstance(js.get('output'), dict):
            aus |= kx.ergebnis(js['output'], MEK_OUTPUT_ART.get(typ, 'item'))
        return [Teil(ein, aus, '')] if aus else []
    return lese


def _inscriber(js, kx, rid):
    z = js.get('ingredients') or {}
    return [Teil([kx.zutat(z[k]) for k in ('top', 'middle', 'bottom') if k in z], kx.ergebnis(js.get('result')), '')]


def _transform(js, kx, rid):
    ein = _gruppen(kx, js.get('ingredients'))
    c = js.get('circumstance') or {}
    if c.get('type') == 'fluid':
        ein.append(kx.fluid_tag(c.get('tag', 'minecraft:water')))
    elif c.get('type') == 'explosion':
        ein.append(frozenset({'minecraft:tnt'}))
    return [Teil(ein, kx.ergebnis(js.get('result')), '')]


def _entropy(js, kx, rid):
    i, o = js.get('input') or {}, js.get('output') or {}
    ein = kx.zutat(i['fluid'], 'fluid') if 'fluid' in i else kx.zutat(i.get('block'))
    aus = kx.ergebnis(o)
    return [Teil([ein], aus, '')] if ein and aus else []


def _zellen(js, kx, rid):
    return [Teil([kx.zutat(js.get('cell'))], kx.ergebnis(js.get('cell_disassembly_items', [])), '')]


def _apparat(js, kx, rid):
    ein = [kx.zutat(js.get('reagent'))] + _gruppen(kx, js.get('pedestalItems'))
    if js.get('sourceCost', 0) > 0:
        ein.append(frozenset({QUELLE}))
    return [Teil(ein, kx.ergebnis(js.get('result')), '')] if 'result' in js else []


def _imbuement(js, kx, rid):
    # Keine Quelle nötig: ImbuementTile.tick erzeugt ohne Quellglas in Reichweite selbst 10 Quelle je Sekunde
    # (Bytecode Ars Nouveau 5.13.3, Zweig nach SourceUtil.takeSourceMultiple == null). Quellgläser machen es nur schneller.
    ein = [kx.zutat(js.get('input'))] + _gruppen(kx, js.get('pedestalItems'))
    neben = [kx.muster('ars_nouveau:arcane_pedestal')] if js.get('pedestalItems') else []
    return [Teil(ein, kx.ergebnis(js.get('output')), '', neben)]


def _glyph(js, kx, rid):
    return [Teil(_gruppen(kx, js.get('inputs')), kx.ergebnis(js.get('output')), '')]


def _crush(js, kx, rid):
    aus = kx.ergebnis(js.get('output', []))
    return [Teil([kx.zutat(js.get('input'))], aus, '')] if aus else []


def _bannen(js, kx, rid):
    """Bannzauber auf einen Mob (z. B. Hexe bei halber Gesundheit) gibt die Beute einer eigenen Loot-Tabelle."""
    aus = kx.loot.get(js.get('loot_table', ''), frozenset())
    return [Teil([frozenset({'mob:' + js['entity']})], aus, '')] if aus and js.get('entity') else []


def _budding(js, kx, rid):
    return [Teil([kx.zutat(js.get('input'))], kx.ergebnis(js.get('result')), '', annahme=True)]


def _drops(kx, d):
    if not isinstance(d, dict):
        return frozenset()
    if d.get('type') == 'botanypots:loot_table':
        return kx.loot.get(d.get('table_id', ''), frozenset())
    if d.get('type') == 'botanypots:block_state':
        blk = (d.get('block_state') or {}).get('block', '')
        ns, _, pfad = blk.partition(':')
        return kx.loot.get(f'{ns}:blocks/{pfad}', frozenset())
    return kx.ergebnis(d)


def _boden(js, kx):
    s = js.get('soil')
    if not s:
        return kx.muster(('minecraft:dirt', 'minecraft:grass_block', 'minecraft:farmland'))
    if isinstance(s, dict) and 'ingredients' in s:
        return frozenset().union(*(kx.zutat(x) for x in s['ingredients']))
    return kx.zutat(s)


def _topf(js, kx, rid):
    aus = _drops(kx, js.get('drops'))
    if not aus:
        return []
    saat, boden = kx.zutat(js.get('input')), _boden(js, kx)
    teile = [Teil([saat], aus, 'topf', [boden])]
    # Dieselbe Pflanze direkt in der Welt: Erde/Ackerland braucht Hacke und Wasser (ort:acker)
    acker = bool(boden & {'minecraft:dirt', 'minecraft:grass_block', 'minecraft:farmland'})
    ein = [saat, frozenset({'ort:acker'})] if acker else [saat, boden]
    teile.append(Teil(ein, aus, 'hand'))
    return teile


WERKZEUG_FAEHIGKEIT = {'knife_dig': 'c:tools/knife', 'axe_dig': 'minecraft:axes', 'pickaxe_dig': 'minecraft:pickaxes',
                       'shovel_dig': 'minecraft:shovels', 'shears_dig': 'c:tools/shear', 'hoe_dig': 'minecraft:hoes'}


def _schneiden(js, kx, rid):
    werkzeug = frozenset()
    for t in (js.get('tool') if isinstance(js.get('tool'), list) else [js.get('tool')]):
        if isinstance(t, dict) and t.get('type') == 'farmersdelight:item_ability':
            werkzeug |= kx.tag(WERKZEUG_FAEHIGKEIT.get(t.get('action'), ''))
            if t.get('action') == 'shears_dig':
                werkzeug |= kx.muster('minecraft:shears')
        elif t is not None:
            werkzeug |= kx.zutat(t)
    aus = kx.ergebnis(js.get('result', []))
    return [Teil(_gruppen(kx, js.get('ingredients')), aus, '', [werkzeug])] if aus else []


def _kochen(js, kx, rid):
    ein = _gruppen(kx, js.get('ingredients'))
    if js.get('container'):
        ein.append(kx.zutat(js['container']))
    return [Teil(ein, kx.ergebnis(js.get('result')), '')]


def _framed(js, kx, rid):
    ein = [kx.muster('framedblocks:framed_cube')] + [kx.zutat(a) for a in js.get('additives', [])]
    return [Teil(ein, kx.ergebnis(js.get('result')), '')]


def _verdichten(js, kx, rid):
    lo, hi = kx.zutat(js.get('lower_input')), kx.zutat(js.get('higher_input'))
    return [Teil([lo], hi, ''), Teil([hi], lo, '')]


def _if_aufloesung(js, kx, rid):
    ein = _gruppen(kx, js.get('input')) + ([kx.zutat(js['inputFluid'], 'fluid')] if js.get('inputFluid') else [])
    aus = kx.ergebnis(js.get('output'))
    if js.get('outputFluid'):
        aus |= kx.zutat(js['outputFluid'], 'fluid')
    return [Teil(ein, aus, '')] if aus else []


def _if_extraktor(js, kx, rid):
    o = js.get('output') or {}
    return [Teil([kx.zutat(js.get('input'))], frozenset({'fluid:' + o.get('id', '')}), '')]


def _if_laser(js, kx, rid):
    o = js.get('output') or {}
    aus = kx.zutat(o['fluid'], 'fluid') if 'fluid' in o else kx.ergebnis(o)
    ein = []
    orte = set()
    alle_offen = False
    for r in js.get('rarity', []):
        wl = (r.get('dimension_filter') or {}).get('whitelist') or []
        if not wl:
            alle_offen = True
        orte |= {'ort:' + d for d in wl}
    if orte and not alle_offen:
        ein.append(frozenset(o.replace('ort:minecraft:the_nether', 'ort:nether').replace('ort:minecraft:the_end', 'ort:end')
                             for o in orte))
    ent = ((js.get('entity_data') or {}).get('entity') or {}).get('type')
    if ent:
        ein.append(frozenset({'mob:' + ent}))
    return [Teil(ein, aus, '', [kx.zutat(js.get('catalyst'))])] if aus else []


def _if_stein(js, kx, rid):
    ein = []
    if js.get('waterNeed', 0) or js.get('waterConsume', 0):
        ein.append(frozenset({'fluid:minecraft:water'}))
    if js.get('lavaNeed', 0) or js.get('lavaConsume', 0):
        ein.append(frozenset({'fluid:minecraft:lava'}))
    return [Teil(ein, kx.ergebnis(js.get('output')), '')]


def _if_brecher(js, kx, rid):
    return [Teil([kx.zutat(js.get('input'))], kx.ergebnis(js.get('output')), '')]


def _powah(js, kx, rid):
    return [Teil(_gruppen(kx, js.get('ingredients')), kx.ergebnis(js.get('result')), '')]


def _infusion(js, kx, rid):
    return [Teil([kx.zutat(js.get('input'))] + _gruppen(kx, js.get('ingredients')), kx.ergebnis(js.get('result')), '')]


def _erwachen(js, kx, rid):
    ein = [kx.zutat(js.get('input'))] + _gruppen(kx, js.get('ingredients')) + [kx.zutat(e) for e in js.get('essences', [])]
    return [Teil(ein, kx.ergebnis(js.get('result')), '')]


def _seelen_spawner(js, kx, rid):
    mobs = frozenset('mob:' + e['entity'] for e in js.get('entities', []) if e.get('weight', 1) > 0)
    return [Teil([kx.zutat(js.get('input'))], mobs, '')]


def _seele(js, kx, rid):
    t = (js.get('result') or {}).get('type')
    return [Teil([kx.zutat(js.get('input'))], frozenset({'seele:' + t}), '')] if t else []


def _biene_wabe(js, kx, rid):
    aus = frozenset()
    for r in js.get('results', []):
        if r.get('chance', 1) > 0 and r.get('max', 1) > 0:
            aus |= kx.ergebnis(r.get('item'))
    return [Teil([frozenset({'biene:' + js.get('ingredient', '')})], aus, '')] if aus else []


def _zentrifuge(js, kx, rid):
    aus = frozenset()
    for r in js.get('outputs', []):
        if r.get('chance', 1) > 0 and r.get('max', 1) > 0:
            aus |= kx.ergebnis(r.get('item'))
    if js.get('fluid'):
        aus |= kx.zutat(js['fluid'], 'fluid')
    return [Teil([kx.zutat(js.get('ingredient'))], aus, '')] if aus else []


def _abfueller(js, kx, rid):
    return [Teil([kx.zutat(js.get('fluid'), 'fluid'), kx.zutat(js.get('ingredient'))], kx.ergebnis(js.get('result')), '')]


def _zucht(js, kx, rid):
    return [Teil([frozenset({'biene:' + js['parent1']}), frozenset({'biene:' + js['parent2']})],
                 frozenset({'biene:' + js['offspring']}), '')]


def _umwandlung(js, kx, rid):
    if js.get('chance', 1) <= 0:
        return []
    return [Teil([frozenset({'biene:' + js['source']}), kx.zutat(js.get('item'))], frozenset({'biene:' + js['result']}), '')]


def _nest(js, kx, rid):
    ein = [kx.zutat(js.get('ingredient'))]
    if js.get('spawn_item'):
        ein.append(kx.zutat(js['spawn_item']))
    return [Teil(ein, frozenset('biene:' + b for b in js.get('results', [])), '', annahme=True)]


def _extruder(js, kx, rid):
    return []          # nur im aufgelösten Dump lesbar (siehe lade_rezepte)


LESER = {
    'minecraft:crafting': _crafting, 'minecraft:smelting': _einfach(), 'minecraft:blasting': _einfach(),
    'minecraft:smoking': _einfach(), 'minecraft:campfire_cooking': _einfach(), 'minecraft:stonecutting': _einfach(),
    'minecraft:smithing': _smithing,
    'create:milling': _create, 'create:crushing': _create, 'create:cutting': _create, 'create:deploying': _create,
    'create:item_application': _create, 'create:mixing': _create, 'create:compacting': _create, 'create:pressing': _create,
    'create:splashing': _create, 'create:haunting': _create, 'create:emptying': _create, 'create:filling': _create,
    'create:sandpaper_polishing': _create, 'create:mechanical_crafting': _create_mech, 'create:sequenced_assembly': _sequenz,
    'createaddition:charging': _create, 'createaddition:rolling': _create, 'createsifter:sifting': _sifter,
    'create_mechanical_extruder:extruding': _extruder,
    'exdeorum:sieve': _exd_sieb, 'exdeorum:compressed_sieve': _exd_sieb, 'exdeorum:hammer': _exd_hammer,
    'exdeorum:compressed_hammer': _exd_hammer, 'exdeorum:crook': _exd_crook, 'exdeorum:lava_crucible': _exd_tiegel,
    'exdeorum:water_crucible': _exd_tiegel, 'exdeorum:barrel_compost': _exd_kompost, 'exdeorum:barrel_mixing': _exd_fass_mix,
    'exdeorum:barrel_fluid_mixing': _exd_fass_fluid, 'exdeorum:barrel_fluid_transformation': _exd_fass_wandel,
    'ae2:inscriber': _inscriber, 'ae2:charger': _einfach(), 'ae2:transform': _transform, 'ae2:entropy': _entropy,
    'ae2:storage_cell_disassembly': _zellen,
    'ars_nouveau:enchanting_apparatus': _apparat, 'ars_nouveau:imbuement': _imbuement, 'ars_nouveau:glyph': _glyph,
    'ars_nouveau:crush': _crush, 'ars_nouveau:budding_conversion': _budding, 'ars_nouveau:dispel_entity': _bannen,
    'botanypots:crop': _topf, 'farmersdelight:cooking': _kochen, 'farmersdelight:cutting': _schneiden,
    'framedblocks:frame': _framed, 'functionalstorage:custom_compacting': _verdichten,
    'industrialforegoing:dissolution_chamber': _if_aufloesung, 'industrialforegoing:fluid_extractor': _if_extraktor,
    'industrialforegoing:laser_drill_ore': _if_laser, 'industrialforegoing:laser_drill_fluid': _if_laser,
    'industrialforegoing:stonework_generate': _if_stein, 'industrialforegoing:crusher': _if_brecher,
    'powah:energizing': _powah,
    'mysticalagriculture:infusion': _infusion, 'mysticalagriculture:awakening': _erwachen,
    'mysticalagriculture:reprocessor': _einfach('input', 'result'), 'mysticalagriculture:soulium_spawner': _seelen_spawner,
    'mysticalagriculture:soul_extraction': _seele,
    'productivebees:advanced_beehive': _biene_wabe, 'productivebees:centrifuge': _zentrifuge,
    'productivebees:bottler': _abfueller, 'productivebees:bee_breeding': _zucht, 'productivebees:bee_conversion': _umwandlung,
    'productivebees:bee_spawning': _nest,
}
for _t in [t for t in STATIONEN if t.startswith('mekanism:')]:
    LESER[_t] = _mekanism(_t)

_CREATE_PFAD = re.compile(r':(mixing|milling|crushing|pressing|compacting|splashing|haunting|deploying|filling|emptying|cutting)/')


def typ_raten(rid, js):
    """Typ, wenn der Dump keinen nennt (KubeJS-Rezepte, Sifter)."""
    if 'mesh' in js and 'results' in js and 'input' in js:
        return 'createsifter:sifting'
    m = _CREATE_PFAD.search(rid)
    if m and 'results' in js:
        return 'create:' + m.group(1)
    return None


def lies(rid, typ, js, kx):
    if not typ or typ == 'null':
        typ = typ_raten(rid, js)
    if typ in OHNE_ERGEBNIS:
        return []
    leser = LESER.get(typ)
    if leser is None:
        kx.ohne_leser[typ or '?'] += 1
        return []
    regeln = []
    for n, t in enumerate(leser(js, kx, rid)):
        if not t.ausgaben:
            continue
        schluessel = t.station or typ
        for v_nr, v in enumerate(STATIONEN.get(schluessel, [V()])):
            if t.haupt is not None:
                haupt = t.haupt
            elif v.haupt:
                haupt = kx.muster(v.haupt)
                if not haupt:
                    kx.fehlende_station[f'{schluessel}: {v.haupt}'] += 1
                    continue
            else:
                haupt = None
            neben = [kx.muster(s) for s in v.neben] + list(t.neben)
            if any(not g for g in neben):
                kx.fehlende_station[f'{schluessel}: Nebenteil fehlt'] += 1
                continue
            kraft = [kx.muster(k if isinstance(k, str) else tuple(k)) for k in v.kraft]
            regeln.append(Regel(id=f'{rid}#{n}.{v_nr}' if (n or v_nr) else rid, typ=typ, eingaben=list(t.eingaben) + kraft,
                                ausgaben=frozenset(t.ausgaben), haupt=haupt, neben=neben, annahme=t.annahme))
    return regeln

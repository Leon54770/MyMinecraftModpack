import gzip
import io
import os
import unittest
import hilfen as H
from pruefung import welt
from pruefung.rezepte import Kontext
from pruefung.huelle import huelle


class Loot(unittest.TestCase):
    TABELLEN = {
        'minecraft:entities/zombie': {'pools': [{'entries': [{'type': 'minecraft:item', 'name': 'minecraft:rotten_flesh'}]},
                                                {'entries': [{'type': 'minecraft:alternatives', 'children': [
                                                    {'type': 'minecraft:item', 'name': 'minecraft:iron_ingot'},
                                                    {'type': 'minecraft:loot_table', 'value': 'minecraft:extra'}]}]}]},
        'minecraft:extra': {'pools': [{'entries': [{'type': 'minecraft:tag', 'name': 'c:gems'},
                                                   {'type': 'minecraft:loot_table', 'value': 'minecraft:entities/zombie'}]}]},
        'minecraft:entities/sheep/white': {'pools': [{'entries': [{'type': 'minecraft:item', 'name': 'minecraft:white_wool'}]}]},
    }

    def test_verschachtelt_mit_tag_und_verweis_ohne_endlosschleife(self):
        items = welt.loot_aufloesen(self.TABELLEN, {'c:gems': ['minecraft:diamond']})
        self.assertEqual(items['minecraft:entities/zombie'],
                         frozenset({'minecraft:rotten_flesh', 'minecraft:iron_ingot', 'minecraft:diamond'}))

    def test_schaf_untertabelle_gehoert_zum_schaf(self):
        self.assertEqual(welt.entity_von_tabelle('minecraft:entities/sheep/white'), 'minecraft:sheep')
        self.assertEqual(welt.entity_von_tabelle('minecraft:entities/zombie'), 'minecraft:zombie')
        self.assertIsNone(welt.entity_von_tabelle('minecraft:blocks/dirt'))


ITEMS = {'minecraft:oak_sapling', 'minecraft:oak_log', 'minecraft:oak_leaves', 'minecraft:dirt', 'minecraft:bucket',
         'minecraft:water_bucket', 'minecraft:lava_bucket', 'minecraft:cobblestone', 'minecraft:stone', 'minecraft:obsidian',
         'ars_nouveau:blue_archwood_sapling', 'ars_nouveau:blue_archwood_log', 'ars_nouveau:blue_archwood_leaves',
         'industrialforegoing:latex_processing_unit', 'industrialforegoing:dryrubber',
         'mysticalagriculture:iron_seeds', 'mysticalagriculture:iron_essence', 'mysticalagradditions:nether_star_seeds',
         'mysticalagradditions:nether_star_essence', 'mysticalagradditions:nether_star_crux', 'minecraft:iron_hoe',
         'mysticalagriculture:fertilized_essence', 'minecraft:zombie_spawn_egg', 'minecraft:flint_and_steel',
         'exdeorum:infested_leaves', 'exdeorum:silkworm'}
TAGS = {'minecraft:hoes': ['minecraft:iron_hoe'], 'minecraft:leaves': ['minecraft:oak_leaves', 'ars_nouveau:blue_archwood_leaves']}


def regeln():
    kx = Kontext(ITEMS, TAGS, fluide={'minecraft:water', 'minecraft:lava'})
    return welt.weltregeln(kx, loot={})


class Weltregeln(unittest.TestCase):
    def test_setzling_wird_baum(self):
        h = huelle(regeln(), {'minecraft:oak_sapling', 'minecraft:dirt'})
        self.assertTrue({'minecraft:oak_log', 'minecraft:oak_leaves'} <= h.da)

    def test_archwood_setzling(self):
        h = huelle(regeln(), {'ars_nouveau:blue_archwood_sapling', 'minecraft:dirt'})
        self.assertTrue({'ars_nouveau:blue_archwood_log', 'ars_nouveau:blue_archwood_leaves'} <= h.da)

    def test_axt_entrindet_staemme(self):
        kx = Kontext(ITEMS | {'minecraft:stripped_oak_log', 'minecraft:iron_axe'}, dict(TAGS, **{'minecraft:axes': ['minecraft:iron_axe']}),
                     fluide={'minecraft:water'})
        h = huelle(welt.weltregeln(kx, loot={}), {'minecraft:oak_log', 'minecraft:iron_axe'})
        self.assertIn('minecraft:stripped_oak_log', h.da)
        self.assertNotIn('minecraft:stripped_oak_log', huelle(welt.weltregeln(kx, loot={}), {'minecraft:oak_log'}).da)

    def test_exdeorum_sporen_auf_erde(self):
        kx = Kontext(ITEMS | {'exdeorum:mycelium_spores', 'minecraft:mycelium', 'exdeorum:grass_seeds', 'minecraft:grass_block',
                              'exdeorum:warped_nylium_spores', 'minecraft:warped_nylium', 'minecraft:netherrack'}, TAGS,
                     fluide={'minecraft:water'})
        h = huelle(welt.weltregeln(kx, loot={}), {'exdeorum:mycelium_spores', 'exdeorum:grass_seeds', 'minecraft:dirt'})
        self.assertTrue({'minecraft:mycelium', 'minecraft:grass_block'} <= h.da)
        self.assertNotIn('minecraft:warped_nylium', h.da)
        h = huelle(welt.weltregeln(kx, loot={}), {'exdeorum:warped_nylium_spores', 'minecraft:netherrack'})
        self.assertIn('minecraft:warped_nylium', h.da)

    def test_ars_vertraute_auf_gras_als_annahme(self):
        kx = Kontext(ITEMS | {'ars_nouveau:drygmy_shard', 'minecraft:grass_block'}, TAGS, fluide={'minecraft:water'})
        h = huelle(welt.weltregeln(kx, loot={}), {'minecraft:grass_block'})
        self.assertIn('ars_nouveau:drygmy_shard', h.da)
        self.assertNotIn('ars_nouveau:drygmy_shard', huelle(welt.weltregeln(kx, loot={}), {'minecraft:grass_block'}, annahmen=False).da)

    def test_kondensator_macht_singularitaet(self):
        kx = Kontext(ITEMS | {'ae2:condenser', 'ae2:cell_component_64k', 'ae2:singularity', 'ae2:matter_ball',
                              'ae2:cell_component_1k'}, TAGS, fluide={'minecraft:water'})
        start = {'ae2:condenser', 'ae2:cell_component_64k', 'minecraft:dirt', 'kraft:strom'}
        self.assertIn('ae2:singularity', huelle(welt.weltregeln(kx, loot={}), start).da)

    def test_chimera_per_ritual_ist_annahme(self):
        teile = {'ars_nouveau:ritual_brazier', 'ars_nouveau:ritual_wilden_summon', 'ars_nouveau:wilden_horn',
                 'ars_nouveau:wilden_wing', 'ars_nouveau:wilden_spike', 'ars_nouveau:wilden_tribute'}
        kx = Kontext(ITEMS | teile, TAGS, fluide={'minecraft:water'})
        start = teile - {'ars_nouveau:wilden_tribute'}
        self.assertIn('ars_nouveau:wilden_tribute', huelle(welt.weltregeln(kx, loot={}), start).da)
        self.assertNotIn('ars_nouveau:wilden_tribute', huelle(welt.weltregeln(kx, loot={}), start, annahmen=False).da)

    def test_schlachtfabrik_gibt_pinkschleim(self):
        kx = Kontext(ITEMS | {'industrialforegoing:mob_slaughter_factory'}, TAGS, fluide={'minecraft:water', 'minecraft:lava'})
        start = {'industrialforegoing:mob_slaughter_factory', 'kraft:strom'}
        self.assertIn('fluid:industrialforegoing:pink_slime', huelle(welt.weltregeln(kx, loot={}), start).da)

    def test_latex_wird_gummi(self):
        start = {'industrialforegoing:latex_processing_unit', 'fluid:industrialforegoing:latex', 'minecraft:water_bucket', 'kraft:strom'}
        self.assertIn('industrialforegoing:dryrubber', huelle(regeln(), start).da)

    def test_eimer_und_bruchsteingenerator(self):
        h = huelle(regeln(), {'minecraft:water_bucket', 'minecraft:lava_bucket'})
        self.assertTrue({'fluid:minecraft:water', 'fluid:minecraft:lava', 'minecraft:cobblestone', 'minecraft:bucket'} <= h.da)

    def test_ma_samen_brauchen_acker(self):
        h = huelle(regeln(), {'mysticalagriculture:iron_seeds', 'minecraft:dirt'})
        self.assertNotIn('mysticalagriculture:iron_essence', h.da)
        h = huelle(regeln(), {'mysticalagriculture:iron_seeds', 'minecraft:dirt', 'minecraft:iron_hoe', 'minecraft:water_bucket'})
        self.assertIn('mysticalagriculture:iron_essence', h.da)

    def test_netherstern_samen_brauchen_crux(self):
        start = {'mysticalagradditions:nether_star_seeds', 'minecraft:dirt', 'minecraft:iron_hoe', 'minecraft:water_bucket'}
        self.assertNotIn('mysticalagradditions:nether_star_essence', huelle(regeln(), start).da)
        self.assertIn('mysticalagradditions:nether_star_essence',
                      huelle(regeln(), start | {'mysticalagradditions:nether_star_crux'}).da)

    def test_feindliche_mobs_spawnen_lohen_nicht(self):
        h = huelle(regeln(), set())
        self.assertIn('mob:minecraft:zombie', h.da)
        self.assertNotIn('mob:minecraft:blaze', h.da)
        self.assertNotIn('mob:minecraft:wither_skeleton', h.da)

    def test_nethermobs_brauchen_portal(self):
        self.assertNotIn('mob:minecraft:zombified_piglin', huelle(regeln(), set()).da)
        h = huelle(regeln(), {'minecraft:obsidian', 'minecraft:flint_and_steel'})
        self.assertIn('ort:nether', h.da)
        self.assertIn('mob:minecraft:zombified_piglin', h.da)

    def test_spawn_ei_gibt_mob(self):
        self.assertIn('mob:minecraft:zombie', huelle(regeln(), {'minecraft:zombie_spawn_egg'}).da)

    def test_seidenraupe_befaellt_laub(self):
        self.assertIn('exdeorum:infested_leaves', huelle(regeln(), {'exdeorum:silkworm', 'minecraft:oak_leaves'}).da)


class Konfig(unittest.TestCase):
    PORTAL = {'minecraft:obsidian', 'minecraft:flint_and_steel'}

    def regeln(self, **konfig):
        kx = Kontext(ITEMS | {'minecraft:bee_nest', 'minecraft:birch_sapling', 'minecraft:egg', 'minecraft:end_stone',
                              'minecraft:dandelion', 'minecraft:poppy', 'minecraft:short_grass',
                              'productivebees:configurable_honeycomb', 'productivebees:configurable_comb'}, TAGS,
                     fluide={'minecraft:water', 'minecraft:lava'})
        return welt.weltregeln(kx, loot={}, konfig=welt.WeltKonfig(**konfig))

    def test_festung_bringt_lohen(self):
        self.assertIn('mob:minecraft:blaze', huelle(self.regeln(festungen=True), self.PORTAL).da)
        self.assertNotIn('mob:minecraft:blaze', huelle(self.regeln(festungen=False), self.PORTAL).da)

    def test_end_hauptinsel_mit_drache_ist_keine_annahme(self):
        start = {'minecraft:end_portal_frame', 'minecraft:ender_eye'}
        self.assertIn('mob:minecraft:ender_dragon', huelle(self.regeln(end_hauptinsel=True), start, annahmen=False).da)
        self.assertNotIn('mob:minecraft:ender_dragon', huelle(self.regeln(end_hauptinsel=False), start).da)
        self.assertIn('minecraft:end_stone', huelle(self.regeln(end_hauptinsel=True), start).da)

    def test_huhn_legt_eier(self):
        start = {'minecraft:chicken_spawn_egg'}
        r = self.regeln() + [welt._r('ei', [{'minecraft:chicken_spawn_egg'}], {'mob:minecraft:chicken'})]
        self.assertIn('minecraft:egg', huelle(r, start).da)

    def test_bienennest_am_setzling_neben_blumen(self):
        start = {'minecraft:birch_sapling', 'minecraft:dirt', 'minecraft:grass_block', 'minecraft:bone_meal'}
        h = huelle(self.regeln(), start)
        self.assertIn('minecraft:bee_nest', h.da)
        self.assertNotIn('minecraft:bee_nest', huelle(self.regeln(), start, annahmen=False).da)   # Blumen: Biom

    def test_waben_variante_wird_wabenblock(self):
        r = welt.wabenregeln({'productivebees:configurable_honeycomb{productivebees:iron}'})
        self.assertIn('productivebees:configurable_comb{productivebees:iron}',
                      huelle(r, {'productivebees:configurable_honeycomb{productivebees:iron}'}).da)

    def test_konfig_aus_dateien(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'config/skyblockbuilder/structures.json5',
                   '{ "structuresToGenerate": { "allow_list": true, "elements": ["minecraft:fortress"] } }')
        H.schreibe(o, 'config/skyblockbuilder/dimensions.json5', '{ "End": { "isCustom": true, "keepMainIsland": false } }')
        k = welt.lade_konfig([o])
        self.assertEqual((k.festungen, k.end_hauptinsel), (True, False))


class Json5(unittest.TestCase):
    def test_kommentare_und_kommas(self):
        txt = '// Kopf\n{\n  "items": [\n    { "Item": { "id": "a:b", "count": 1 } }, // Ende\n  ],\n  /* block */ "x": "http://y"\n}'
        self.assertEqual(welt.json5(txt), {'items': [{'Item': {'id': 'a:b', 'count': 1}}], 'x': 'http://y'})


class Nbt(unittest.TestCase):
    def test_inselbloecke_aus_vorlage(self):
        # Vorlage im Format von _src/inseln.py (echter Schreiber), aber in einen Temp-Ordner
        import inseln
        o = H.temp_ordner(self)
        pfad = os.path.join(o, 'test.nbt')
        I = inseln.Int
        root = {'DataVersion': I(3955), 'size': inseln.TList(3, [I(1), I(2), I(1)]),
                'palette': inseln.TList(10, [{'Name': 'minecraft:grass_block'},
                                             {'Name': 'minecraft:oak_log', 'Properties': {'axis': 'y'}}]),
                'blocks': inseln.TList(10, [{'pos': inseln.TList(3, [I(0), I(0), I(0)]), 'state': I(0)},
                                            {'pos': inseln.TList(3, [I(0), I(1), I(0)]), 'state': I(1)}]),
                'entities': inseln.TList(10, [])}
        inseln.write_nbt(pfad, root)
        self.assertEqual(welt.vorlage_bloecke(pfad), {'minecraft:grass_block', 'minecraft:oak_log'})


if __name__ == '__main__':
    unittest.main()

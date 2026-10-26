import unittest
import _pfad  # noqa: F401
from pruefung.rezepte import Kontext
from pruefung import laden

ITEMS = {'mysticalagriculture:zombie_seeds', 'mysticalagriculture:zombie_essence', 'minecraft:rotten_flesh',
         'mysticalagriculture:prosperity_seed_base', 'mysticalagriculture:infusion_altar', 'mysticalagriculture:infusion_pedestal',
         'minecraft:crafting_table', 'ironjetpacks:jetpack', 'minecraft:iron_ingot', 'create_mechanical_extruder:mechanical_extruder',
         'minecraft:cobblestone'}


def kx():
    return Kontext(ITEMS, {})


class Zutaten(unittest.TestCase):
    def test_crop_component_samen(self):
        k = kx()
        self.assertEqual(k.zutat({'crop': 'mysticalagriculture:zombie', 'component': 'seed',
                                  'type': 'mysticalagriculture:crop_component'}),
                         frozenset({'mysticalagriculture:zombie_seeds'}))

    def test_crop_component_material_ist_unklar(self):
        k = kx()
        k.unklar = 0
        self.assertEqual(k.zutat({'crop': 'mysticalagriculture:zombie', 'component': 'material',
                                  'type': 'mysticalagriculture:crop_component'}), frozenset())
        self.assertEqual(k.unklar, 1)


class Zusammenfuehren(unittest.TestCase):
    MA = {'input': {'item': 'mysticalagriculture:prosperity_seed_base'},
          'ingredients': [{'crop': 'mysticalagriculture:zombie', 'component': 'material', 'type': 'mysticalagriculture:crop_component'},
                          {'crop': 'mysticalagriculture:zombie', 'component': 'essence', 'type': 'mysticalagriculture:crop_component'}],
          'result': {'id': 'mysticalagriculture:zombie_seeds', 'count': 1}}

    def test_unklare_zutat_aus_aufgeloestem_dump(self):
        js = [{'id': 'ma:zombie', 'json': self.MA}]
        auf = {'ma:zombie': {'id': 'ma:zombie', 'type': 'mysticalagriculture:infusion',
                             'ins': [['mysticalagriculture:prosperity_seed_base'], ['minecraft:rotten_flesh'],
                                     ['mysticalagriculture:zombie_essence']], 'out': 'mysticalagriculture:zombie_seeds'}}
        regeln, info = laden.regeln_aus_dumps(js, auf, kx())
        r = regeln[0]
        self.assertIn(frozenset({'minecraft:rotten_flesh'}), r.eingaben)
        self.assertEqual(r.haupt, frozenset({'mysticalagriculture:infusion_altar'}))
        self.assertEqual(info['rueckfall'], 1)

    def test_unklar_ohne_aufgeloeste_zutaten_wird_gemeldet(self):
        auf = {'ma:zombie': {'id': 'ma:zombie', 'type': 'mysticalagriculture:infusion', 'ins': [], 'out': 'mysticalagriculture:zombie_seeds'}}
        regeln, info = laden.regeln_aus_dumps([{'id': 'ma:zombie', 'json': self.MA}], auf, kx())
        self.assertEqual(info['unklar_ohne_rueckfall'], ['ma:zombie'])

    def test_nur_im_aufgeloesten_dump_crafting(self):
        auf = {'ironjetpacks:x': {'id': 'ironjetpacks:x', 'type': 'minecraft:crafting', 'ins': [['minecraft:iron_ingot'], [], []],
                                  'out': 'ironjetpacks:jetpack'}}
        regeln, info = laden.regeln_aus_dumps([], auf, kx())
        self.assertEqual(regeln[0].haupt, frozenset({'minecraft:crafting_table'}))
        self.assertEqual(regeln[0].eingaben, [frozenset({'minecraft:iron_ingot'})])

    def test_extruder_aus_aufgeloestem_dump(self):
        auf = {'create_mechanical_extruder:extruding/cobblestone': {'id': 'create_mechanical_extruder:extruding/cobblestone',
                                                                    'type': 'null', 'ins': [], 'out': 'minecraft:cobblestone'}}
        r = laden.regeln_aus_dumps([], auf, kx())[0][0]
        self.assertEqual(r.haupt, frozenset({'create_mechanical_extruder:mechanical_extruder'}))
        self.assertTrue(r.annahme)


class Erzbrocken(unittest.TestCase):
    def test_exdeorum_brocken_zu_erz(self):
        k = Kontext(ITEMS | {'exdeorum:osmium_ore_chunk', 'mekanism:osmium_ore'}, {'c:ores/osmium': ['mekanism:osmium_ore']})
        js = [{'id': 'exdeorum:ores/osmium_from_chunks', 'json': {'ore_chunk': {'item': 'exdeorum:osmium_ore_chunk'}, 'ore': 'c:ores/osmium'}}]
        auf = {'exdeorum:ores/osmium_from_chunks': {'id': 'exdeorum:ores/osmium_from_chunks', 'type': 'minecraft:crafting',
                                                    'ins': [['exdeorum:osmium_ore_chunk']] * 4, 'out': 'mekanism:osmium_ore'}}
        r = laden.regeln_aus_dumps(js, auf, k)[0][0]
        self.assertEqual(r.ausgaben, frozenset({'mekanism:osmium_ore'}))
        self.assertIsNone(r.haupt)          # 2×2 geht ohne Werkbank

    def test_leser_ohne_ergebnis_nimmt_aufgeloestes(self):
        k = kx()
        js = [{'id': 'mod:sonder', 'json': {'eigenes_feld': 1}}]
        auf = {'mod:sonder': {'id': 'mod:sonder', 'type': 'minecraft:crafting', 'ins': [['minecraft:iron_ingot']],
                              'out': 'ironjetpacks:jetpack'}}
        regeln, info = laden.regeln_aus_dumps(js, auf, k)
        self.assertEqual(regeln[0].ausgaben, frozenset({'ironjetpacks:jetpack'}))
        self.assertEqual(info['rueckfall_ergebnis'], 1)


class JarRezepte(unittest.TestCase):
    def test_fehlendes_json_aus_dem_jar(self):
        # Nest-Rezepte scheitern im JSON-Dump; das Spiel kennt sie (aufgelöster Dump), das Jar hat das JSON
        k = Kontext(ITEMS | {'productivebees:stone_nest', 'minecraft:honey_bottle'}, {})
        auf = {'productivebees:bee_spawning/stone': {'id': 'productivebees:bee_spawning/stone', 'type': 'productivebees:bee_spawning',
                                                    'ins': [['productivebees:stone_nest']], 'out': ''}}
        jar = {'productivebees:bee_spawning/stone': {'type': 'productivebees:bee_spawning',
                                                     'ingredient': {'item': 'productivebees:stone_nest'},
                                                     'spawn_item': {'item': 'minecraft:honey_bottle'},
                                                     'results': ['productivebees:ashy_mining_bee']}}
        regeln, info = laden.regeln_aus_dumps([], auf, k, jar_rezepte=jar)
        self.assertEqual(regeln[0].ausgaben, frozenset({'biene:productivebees:ashy_mining_bee'}))
        self.assertEqual(info['aus_jar'], 1)

    def test_jar_rezept_ohne_spieleintrag_bleibt_draussen(self):
        # Steht nicht im aufgelösten Dump: vom Pack entfernt (KubeJS) oder durch Bedingung nicht geladen
        regeln, info = laden.regeln_aus_dumps([], {}, kx(), jar_rezepte={'a:b': {'type': 'minecraft:crafting',
                                                                                'ingredients': [{'item': 'minecraft:iron_ingot'}],
                                                                                'result': {'id': 'ironjetpacks:jetpack'}}})
        self.assertEqual(regeln, [])


class DumpWahl(unittest.TestCase):
    def test_nimmt_nur_aufgeloesten_dump_mit_typen(self):
        import json, os, hilfen as H
        o = H.temp_ordner(self)
        alt = H.schreibe(o, 'alt.json', json.dumps({'recipes': [{'id': 'a:b', 'ins': [], 'out': 'a:c'}]}))
        gut = H.schreibe(o, 'gut.json', json.dumps({'count': 1, 'recipes': [{'id': 'a:b', 'type': 'x:y', 'ins': [], 'out': 'a:c'}]}))
        pfad, rezepte = laden.aufgeloester_dump([alt, os.path.join(o, 'fehlt.json'), gut])
        self.assertEqual(pfad, gut)
        self.assertIn('a:b', rezepte)


if __name__ == '__main__':
    unittest.main()

import unittest
import _pfad  # noqa: F401
from pruefung.rezepte import Kontext, lies

ITEMS = {'minecraft:oak_planks', 'minecraft:stick', 'minecraft:crafting_table', 'minecraft:oak_log', 'minecraft:dirt',
         'create:andesite_alloy', 'minecraft:andesite', 'minecraft:iron_nugget', 'create:mechanical_mixer', 'create:basin',
         'create:blaze_burner', 'create:blaze_cake', 'create:millstone', 'create:crushing_wheel', 'minecraft:charcoal',
         'minecraft:black_dye', 'minecraft:gray_dye', 'minecraft:netherrack', 'create:cinder_flour', 'minecraft:cobblestone',
         'exdeorum:oak_sieve', 'exdeorum:mechanical_sieve', 'exdeorum:oak_compressed_sieve', 'exdeorum:flint_mesh',
         'exdeorum:crushed_deepslate', 'minecraft:amethyst_shard', 'mekanism:enrichment_chamber', 'minecraft:redstone',
         'minecraft:redstone_ore', 'mekanism:chemical_injection_chamber', 'mekanism:shard_copper', 'mekanism:raw_copper',
         'minecraft:raw_copper', 'mekanism:electrolytic_separator', 'createsifter:sifter', 'createsifter:brass_sifter',
         'createsifter:zinc_mesh', 'createsifter:advanced_sturdy_mesh', 'minecraft:flint', 'minecraft:gravel',
         'exdeorum:wooden_hammer', 'exdeorum:stone_hammer', 'exdeorum:compressed_wooden_hammer', 'exdeorum:mechanical_hammer',
         'minecraft:honey_block', 'create:mechanical_press', 'ae2:inscriber', 'ae2:logic_processor_press',
         'minecraft:iron_block', 'ae2:charger', 'ae2:crank', 'ae2:certus_quartz_crystal', 'ae2:charged_certus_quartz_crystal',
         'productivebees:configurable_honeycomb', 'productivebees:centrifuge', 'productivebees:powered_centrifuge',
         'productivebees:heated_centrifuge', 'productivebees:wax', 'mekanism:raw_lead', 'exdeorum:oak_barrel',
         'mysticalagriculture:infusion_altar', 'mysticalagriculture:infusion_pedestal', 'mysticalagriculture:prosperity_seed_base'}
TAGS = {'c:nuggets/iron': ['minecraft:iron_nugget'], 'c:ores/redstone': ['minecraft:redstone_ore'],
        'c:raw_materials/copper': ['minecraft:raw_copper'], 'minecraft:planks': ['minecraft:oak_planks'],
        'c:cobblestones': ['minecraft:cobblestone']}


def kx():
    return Kontext(ITEMS, TAGS, fluide={'minecraft:water', 'minecraft:lava', 'create:honey', 'productivebees:honey'})


def eine(regeln):
    assert len(regeln) == 1, regeln
    return regeln[0]


class Werkbank(unittest.TestCase):
    def test_kleines_rezept_ohne_werkbank(self):
        js = {'key': {'#': {'tag': 'minecraft:planks'}}, 'pattern': ['#', '#'], 'result': {'id': 'minecraft:stick', 'count': 4}}
        r = eine(lies('minecraft:stick', 'minecraft:crafting', js, kx()))
        self.assertIsNone(r.haupt)
        self.assertEqual(r.eingaben, [frozenset({'minecraft:oak_planks'})])
        self.assertEqual(r.ausgaben, frozenset({'minecraft:stick'}))

    def test_grosses_rezept_braucht_werkbank(self):
        js = {'key': {'#': {'item': 'minecraft:oak_planks'}, 'S': {'item': 'minecraft:stick'}},
              'pattern': ['###', ' S ', ' S '], 'result': {'id': 'minecraft:dirt'}}
        r = eine(lies('x', 'minecraft:crafting', js, kx()))
        self.assertEqual(r.haupt, frozenset({'minecraft:crafting_table'}))
        self.assertEqual(len(r.eingaben), 2)

    def test_formlos_mit_fuenf_zutaten_braucht_werkbank(self):
        js = {'ingredients': [{'item': 'minecraft:dirt'}] * 5, 'result': {'id': 'minecraft:stick'}}
        self.assertEqual(eine(lies('x', 'minecraft:crafting', js, kx())).haupt, frozenset({'minecraft:crafting_table'}))

    def test_sonderrezept_ohne_ergebnis_wird_uebersprungen(self):
        self.assertEqual(lies('minecraft:firework_rocket', 'minecraft:crafting', {'category': 'misc'}, kx()), [])


class Create(unittest.TestCase):
    def test_mixer_mit_becken_und_drehkraft(self):
        js = {'ingredients': [{'item': 'minecraft:andesite'}, {'tag': 'c:nuggets/iron'}], 'results': [{'id': 'create:andesite_alloy'}]}
        r = eine(lies('create:mixing/andesite_alloy', 'create:mixing', js, kx()))
        self.assertEqual(r.haupt, frozenset({'create:mechanical_mixer'}))
        self.assertIn(frozenset({'create:basin'}), r.neben)
        self.assertIn(frozenset({'kraft:rotation'}), r.eingaben)

    def test_erhitzt_braucht_hitze(self):
        js = {'ingredients': [{'item': 'minecraft:andesite'}], 'results': [{'id': 'create:andesite_alloy'}], 'heat_requirement': 'heated'}
        self.assertIn(frozenset({'kraft:hitze', 'kraft:superhitze'}), eine(lies('x', 'create:mixing', js, kx())).eingaben)

    def test_fluid_als_zutat(self):
        js = {'ingredients': [{'tag': 'c:cobblestones'}, {'item': 'create:cinder_flour'},
                              {'type': 'neoforge:tag', 'tag': 'minecraft:lava', 'amount': 25}], 'results': [{'id': 'minecraft:netherrack'}]}
        self.assertIn(frozenset({'fluid:minecraft:lava'}), eine(lies('x', 'create:mixing', js, kx())).eingaben)

    def test_mahlen_auch_mit_brechwalzen_und_zufallsausgabe(self):
        js = {'ingredients': [{'item': 'minecraft:charcoal'}], 'results': [{'id': 'minecraft:black_dye'},
                                                                           {'id': 'minecraft:gray_dye', 'count': 2, 'chance': 0.1}]}
        r = eine(lies('x', 'create:milling', js, kx()))
        self.assertEqual(r.haupt, frozenset({'create:millstone', 'create:crushing_wheel'}))
        self.assertEqual(r.ausgaben, frozenset({'minecraft:black_dye', 'minecraft:gray_dye'}))

    def test_fluid_tag_ohne_fluid_erfindet_nichts(self):
        k = kx()
        self.assertEqual(k.fluid_tag('c:unbekannt'), frozenset())
        self.assertEqual(k.unbekannte_zutat['Fluid-Tag ohne Fluid: c:unbekannt'], 1)

    def test_fluid_als_ergebnis(self):
        js = {'ingredients': [{'type': 'neoforge:tag', 'tag': 'c:honey', 'amount': 1000}], 'results': [{'id': 'minecraft:honey_block'}]}
        r = eine(lies('x', 'create:compacting', js, kx()))
        self.assertEqual(r.eingaben[0], frozenset({'fluid:create:honey', 'fluid:productivebees:honey'}))


class Sieb(unittest.TestCase):
    def test_exdeorum_sieb_mit_netz_als_nebenstation(self):
        js = {'result_amount': {'n': 1, 'p': 0.06, 'type': 'minecraft:binomial'}, 'mesh': {'item': 'exdeorum:flint_mesh'},
              'ingredient': {'item': 'exdeorum:crushed_deepslate'}, 'result': {'id': 'minecraft:amethyst_shard', 'count': 1}}
        rs = lies('x', 'exdeorum:sieve', js, kx())
        hand = [r for r in rs if r.haupt == frozenset({'exdeorum:oak_sieve'})]
        mech = [r for r in rs if r.haupt == frozenset({'exdeorum:mechanical_sieve'})]
        self.assertEqual(len(hand), 1)
        self.assertIn(frozenset({'exdeorum:flint_mesh'}), hand[0].neben)
        self.assertIn(frozenset({'kraft:strom'}), mech[0].eingaben)

    def test_chance_null_liefert_nichts(self):
        js = {'result_amount': {'n': 1, 'p': 0.0, 'type': 'minecraft:binomial'}, 'mesh': {'item': 'exdeorum:flint_mesh'},
              'ingredient': {'item': 'exdeorum:crushed_deepslate'}, 'result': {'id': 'minecraft:amethyst_shard', 'count': 1}}
        self.assertEqual(lies('x', 'exdeorum:sieve', js, kx()), [])

    def test_sifter_normal_und_fortgeschritten(self):
        js = {'input': {'item': 'minecraft:gravel'}, 'results': [{'id': 'minecraft:flint'}],
              'mesh': {'id': 'createsifter:zinc_mesh', 'count': 1}, 'processingTime': 200}
        r = eine(lies('skyandstone:sifting/1', None, js, kx()))
        self.assertEqual(r.haupt, frozenset({'createsifter:sifter', 'createsifter:brass_sifter'}))
        self.assertIn(frozenset({'createsifter:zinc_mesh'}), r.neben)
        js['mesh'] = {'id': 'createsifter:advanced_sturdy_mesh', 'count': 1}
        self.assertEqual(eine(lies('skyandstone:sifting/2', None, js, kx())).haupt, frozenset({'createsifter:brass_sifter'}))

    def test_hammer_mit_alternativen_zutaten(self):
        js = {'ingredient': [{'item': 'minecraft:cobblestone'}, {'item': 'minecraft:andesite'}],
              'result': {'id': 'minecraft:gravel', 'count': 1}, 'result_amount': 1}
        hand = [r for r in lies('x', 'exdeorum:hammer', js, kx()) if 'exdeorum:wooden_hammer' in (r.haupt or ())][0]
        self.assertEqual(hand.eingaben[0], frozenset({'minecraft:cobblestone', 'minecraft:andesite'}))
        self.assertNotIn('exdeorum:compressed_wooden_hammer', hand.haupt)

    def test_fass_heiss_nur_beim_grundfluid(self):
        # Lava als Zusatz liegt als Quellblock oben auf dem Fass; heiß ist nur, was im Fass steht
        k = Kontext(ITEMS | {'exdeorum:oak_barrel', 'exdeorum:stone_barrel', 'minecraft:netherrack', 'minecraft:obsidian'}, TAGS,
                    fluide={'minecraft:water', 'minecraft:lava', 'exdeorum:witch_water'})
        hexe = {'base_fluid': {'fluid': 'exdeorum:witch_water', 'amount': 1000}, 'additive_fluid': {'fluid': 'minecraft:lava'},
                'result': {'id': 'minecraft:netherrack', 'count': 1}}
        lava = {'base_fluid': {'fluid': 'minecraft:lava', 'amount': 1000}, 'additive_fluid': {'fluid': 'minecraft:water'},
                'result': {'id': 'minecraft:obsidian', 'count': 1}}
        self.assertIn('exdeorum:oak_barrel', eine(lies('x', 'exdeorum:barrel_fluid_mixing', hexe, k)).haupt)
        self.assertEqual(eine(lies('y', 'exdeorum:barrel_fluid_mixing', lava, k)).haupt, frozenset({'exdeorum:stone_barrel'}))

    def test_kompost_im_fass_gibt_erde(self):
        r = eine(lies('x', 'exdeorum:barrel_compost', {'ingredient': {'item': 'minecraft:oak_log'}, 'volume': 100}, kx()))
        self.assertEqual(r.ausgaben, frozenset({'minecraft:dirt'}))


class Mekanism(unittest.TestCase):
    def test_anreichern_braucht_strom(self):
        js = {'input': {'tag': 'c:ores/redstone', 'count': 1}, 'output': {'id': 'minecraft:redstone', 'count': 12}}
        r = eine(lies('x', 'mekanism:enriching', js, kx()))
        self.assertEqual(r.haupt, frozenset({'mekanism:enrichment_chamber'}))
        self.assertIn(frozenset({'kraft:strom'}), r.eingaben)
        self.assertEqual(r.ausgaben, frozenset({'minecraft:redstone'}))

    def test_injektion_mit_chemikalie(self):
        js = {'item_input': {'tag': 'c:raw_materials/copper', 'count': 3},
              'chemical_input': {'chemical': 'mekanism:hydrogen_chloride', 'amount': 1},
              'output': {'id': 'mekanism:shard_copper', 'count': 8}}
        r = eine(lies('x', 'mekanism:injecting', js, kx()))
        self.assertIn(frozenset({'chem:mekanism:hydrogen_chloride'}), r.eingaben)

    def test_rotationskondensator_in_beide_richtungen(self):
        js = {'fluid_input': {'tag': 'c:sulfuric_acid', 'amount': 1}, 'chemical_input': {'chemical': 'mekanism:sulfuric_acid', 'amount': 1},
              'chemical_output': {'id': 'mekanism:sulfuric_acid', 'amount': 1}, 'fluid_output': {'id': 'mekanism:sulfuric_acid', 'amount': 1}}
        k = Kontext(ITEMS | {'mekanism:rotary_condensentrator'}, TAGS, fluide={'mekanism:sulfuric_acid'})
        rs = lies('x', 'mekanism:rotary', js, k)
        richtungen = {(r.eingaben[0], r.ausgaben) for r in rs}
        self.assertEqual(richtungen, {(frozenset({'fluid:mekanism:sulfuric_acid'}), frozenset({'chem:mekanism:sulfuric_acid'})),
                                      (frozenset({'chem:mekanism:sulfuric_acid'}), frozenset({'fluid:mekanism:sulfuric_acid'}))})

    def test_elektrolyse_gibt_zwei_chemikalien(self):
        js = {'input': {'tag': 'minecraft:water', 'amount': 2}, 'left_chemical_output': {'id': 'mekanism:hydrogen', 'amount': 2},
              'right_chemical_output': {'id': 'mekanism:oxygen', 'amount': 1}}
        r = eine(lies('x', 'mekanism:separating', js, kx()))
        self.assertEqual(r.ausgaben, frozenset({'chem:mekanism:hydrogen', 'chem:mekanism:oxygen'}))
        self.assertIn(frozenset({'fluid:minecraft:water'}), r.eingaben)


class Sonstige(unittest.TestCase):
    def test_inscriber_alle_seiten(self):
        js = {'ingredients': {'top': {'item': 'ae2:logic_processor_press'}, 'middle': {'item': 'minecraft:iron_block'}},
              'result': {'id': 'ae2:logic_processor_press', 'count': 1}, 'mode': 'inscribe'}
        r = eine(lies('x', 'ae2:inscriber', js, kx()))
        self.assertEqual(len([g for g in r.eingaben if not any(x.startswith('kraft:') for x in g)]), 2)

    def test_bannzauber_auf_mob_gibt_loot(self):
        js = {'entity': 'minecraft:witch', 'loot_table': 'ars_nouveau:dispel_witch', 'loot_conditions': []}
        k = Kontext(ITEMS | {'ars_nouveau:glyph_dispel', 'ars_nouveau:novice_spell_book', 'ars_nouveau:wixie_shards'}, TAGS,
                    loot={'ars_nouveau:dispel_witch': frozenset({'ars_nouveau:wixie_shards'})})
        r = eine(lies('x', 'ars_nouveau:dispel_entity', js, k))
        self.assertEqual(r.eingaben, [frozenset({'mob:minecraft:witch'})])
        self.assertEqual(r.ausgaben, frozenset({'ars_nouveau:wixie_shards'}))
        self.assertEqual(r.haupt, frozenset({'ars_nouveau:glyph_dispel'}))

    def test_imbuement_braucht_keine_fremde_quelle(self):
        # ImbuementTile.tick: ohne Quellglas in Reichweite erzeugt die Kammer selbst 10 Quelle je Sekunde
        js = {'input': {'item': 'minecraft:dirt'}, 'output': {'id': 'minecraft:stick', 'count': 1}, 'source': 2000, 'pedestalItems': []}
        k = Kontext(ITEMS | {'ars_nouveau:imbuement_chamber'}, TAGS)
        r = eine(lies('x', 'ars_nouveau:imbuement', js, k))
        self.assertNotIn(frozenset({'kraft:quelle'}), r.eingaben)
        self.assertEqual(r.haupt, frozenset({'ars_nouveau:imbuement_chamber'}))

    def test_lader_mit_strom_oder_kurbel(self):
        js = {'ingredient': {'item': 'ae2:certus_quartz_crystal'}, 'result': {'id': 'ae2:charged_certus_quartz_crystal', 'count': 1}}
        self.assertIn(frozenset({'kraft:strom', 'ae2:crank'}), eine(lies('x', 'ae2:charger', js, kx())).eingaben)

    def test_zentrifuge_mit_komponenten_wabe(self):
        js = {'ingredient': {'items': 'productivebees:configurable_honeycomb', 'components': {'productivebees:bee_type': 'productivebees:lead'},
                             'type': 'productivebees:component'},
              'outputs': [{'item': {'item': 'mekanism:raw_lead'}, 'min': 1, 'max': 1, 'chance': 0.4},
                          {'item': {'item': 'productivebees:wax'}, 'min': 1, 'max': 1, 'chance': 1}],
              'fluid': {'fluid': 'productivebees:honey', 'amount': 100}}
        rs = lies('x', 'productivebees:centrifuge', js, kx())
        self.assertTrue(all(r.eingaben[0] == frozenset({'productivebees:configurable_honeycomb{productivebees:lead}'}) for r in rs))
        self.assertTrue(all('mekanism:raw_lead' in r.ausgaben and 'fluid:productivebees:honey' in r.ausgaben for r in rs))

    def test_unbekannter_typ_wird_gezaehlt(self):
        k = kx()
        self.assertEqual(lies('x', 'neu:maschine', {'input': {'item': 'minecraft:dirt'}}, k), [])
        self.assertEqual(k.ohne_leser['neu:maschine'], 1)


if __name__ == '__main__':
    unittest.main()

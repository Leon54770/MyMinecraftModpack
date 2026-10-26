import unittest
import hilfen as H
from hilfen import quest, aufgabe, buch
from pruefung import daten as D
from pruefung.befund import Register
from pruefung.modell import Belohnung

REG = Register(items={'minecraft:stone', 'minecraft:stick', 'minecraft:obsidian', 'minecraft:ender_eye', 'minecraft:end_stone',
                      'minecraft:end_portal_frame', 'create:blaze_burner', 'minecraft:paper'},
               tags={'c:ingots/iron': ['minecraft:iron_ingot']})


def texte(befunde, stufe=None):
    return [x.text for x in befunde if stufe is None or x.stufe == stufe]


class Funktionen(unittest.TestCase):
    def setUp(self):
        self.o = H.temp_ordner(self)
        H.schreibe(self.o, 'kubejs/data/skyandstone/function/a.mcfunction',
                   'function skyandstone:b\nfunction skyandstone:fehlt\ngive @s minecraft:stone 1\ngive @s mod:weg\n'
                   'tellraw @a {"text":"Hallo","color":"gold"}\ntitle @a title {"text":"kaputt"\n')
        H.schreibe(self.o, 'kubejs/data/skyandstone/function/b.mcfunction', 'say hi\n')
        H.schreibe(self.o, 'kubejs/data/minecraft/tags/function/load.json', '{"values": ["skyandstone:b", "skyandstone:nix"]}')

    def test_fehlende_funktion(self):
        t = texte(D.pruefe_funktionen(self.o, REG), 'FEHLER')
        self.assertTrue(any('skyandstone:fehlt' in x for x in t))
        self.assertTrue(any('skyandstone:nix' in x for x in t))

    def test_unbekanntes_item_in_give(self):
        self.assertTrue(any('mod:weg' in x for x in texte(D.pruefe_funktionen(self.o, REG), 'FEHLER')))

    def test_kaputter_json_text(self):
        self.assertTrue(any('title' in x for x in texte(D.pruefe_funktionen(self.o, REG), 'FEHLER')))

    def test_saubere_zeilen_kein_befund(self):
        t = texte(D.pruefe_funktionen(self.o, REG))
        self.assertFalse(any('minecraft:stone' in x or 'Hallo' in x for x in t))


class Advancements(unittest.TestCase):
    def test_eltern_icon_belohnung(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'kubejs/data/skyandstone/function/f.mcfunction', 'say x\n')
        H.schreibe(o, 'kubejs/data/skyandstone/advancement/root.json', '{"display": {"icon": {"id": "minecraft:stone"}}, "criteria": {}}')
        H.schreibe(o, 'kubejs/data/skyandstone/advancement/kind.json',
                   '{"parent": "skyandstone:weg", "display": {"icon": {"id": "mod:icon"}}, '
                   '"criteria": {"a": {"trigger": "minecraft:inventory_changed", "conditions": {"items": [{"items": "mod:krit"}]}}}, '
                   '"rewards": {"function": "skyandstone:nicht_da"}}')
        t = texte(D.pruefe_advancements(o, REG), 'FEHLER')
        self.assertEqual(len(t), 4, t)


class Questbefehle(unittest.TestCase):
    def test_befehls_belohnung_ohne_funktion(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'kubejs/data/skyandstone/function/feier/da.mcfunction', 'say x\n')
        q = quest('1000000000000001', 'Start', aufgaben=[aufgabe('minecraft:stone')],
                  belohnungen=[Belohnung(id='B000000000000001', typ='command', befehl='function skyandstone:feier/weg'),
                               Belohnung(id='B000000000000002', typ='command', befehl='function skyandstone:feier/da')])
        t = texte(D.pruefe_questbefehle(buch([q]), o), 'FEHLER')
        self.assertEqual(len(t), 1)
        self.assertIn('feier/weg', t[0])


class Startinventar(unittest.TestCase):
    def test_kleine_schluessel_und_unbekanntes_item(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'config/skyblockbuilder/starter_inventory.json5',
                   '{ "items": [ { "Item": { "id": "minecraft:stone", "count": 1 } }, { "item": { "id": "minecraft:stick", "count": 1 } },'
                   ' { "Item": { "id": "mod:weg", "count": 1 }, "Slot": "offhand" }, { "Item": { "id": "minecraft:paper" }, "Slot": "rucksack" } ] }')
        t = texte(D.pruefe_startinventar(o, REG), 'FEHLER')
        self.assertEqual(len(t), 3, t)


class Skripte(unittest.TestCase):
    SKRIPT = """
ServerEvents.recipes(event => {
  event.shaped('minecraft:end_portal_frame', ['OEO', 'SSS'], { O: 'minecraft:obsidian', E: 'mod:auge', S: 'minecraft:end_stone' })
    .id('skyandstone:end_portal_frame')
  event.shapeless('create:blaze_burner', ['minecraft:stick', '#c:ingots/iron', '#c:gibtsnicht']).id('skyandstone:brenner')
  event.custom({ type: 'create:mixing', ingredients: [{ item: 'minecraft:stone' }], results: [{ id: 'x:y' }] }).id('skyandstone:brenner')
  event.remove({ id: 'ftbquests:screen_1' })
  event.remove({ id: 'mod:gab_es_nie' })
  ['a', 'b'].forEach(t => { event.remove({ id: 'mod:zusammen_' + t }); Item.of('mod:teil_' + t) })
})
"""

    def test_items_tags_und_doppelte_ids(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'kubejs/server_scripts/x.js', self.SKRIPT)
        b = D.pruefe_skripte(o, REG, rezept_ids={'ftbquests:screen_1', 'skyandstone:end_portal_frame'})
        f = texte(b, 'FEHLER')
        self.assertTrue(any('mod:auge' in x for x in f))
        self.assertTrue(any('#c:gibtsnicht' in x for x in f))
        self.assertTrue(any('skyandstone:brenner' in x and 'doppelt' in x for x in f))
        self.assertFalse(any('minecraft:obsidian' in x or 'x:y' in x or 'create:mixing' in x for x in f))
        self.assertTrue(any('mod:gab_es_nie' in x for x in texte(b, 'HINWEIS')))
        self.assertFalse(any('zusammen_' in x or 'teil_' in x for x in texte(b)))   # zusammengesetzt: nicht prüfbar


if __name__ == '__main__':
    unittest.main()

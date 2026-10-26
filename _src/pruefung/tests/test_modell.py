import unittest
import hilfen as H
from pruefung import modell

KAPITEL = '''{
	filename: "akt1"
	group: "1A00000000000001"
	icon: { id: "minecraft:dirt" }
	id: "1C00000000000001"
	order_index: 0
	quest_links: [{ id: "1E00000000000001", linked_quest: "1B00000000000009", shape: "square", size: 1.0d, x: 0.0d, y: 0.0d }]
	quests: [
		{
			id: "1B00000000000001"
			tasks: [{ id: "1D00000000000001", item: { count: 1, id: "minecraft:dirt" }, type: "item" }]
			x: 0.0d
			y: 0.0d
		}
		{
			dependencies: ["1B00000000000001"]
			id: "1B00000000000002"
			optional: true
			can_repeat: true
			repeat_cooldown: 1200
			rewards: [
				{ id: "1F00000000000001", table_id: 2202241768434932880L, team_reward: true, type: "loot" }
				{ count: 4, id: "1F00000000000002", item: { count: 1, id: "minecraft:stick" }, type: "item" }
			]
			tasks: [{
				consume_items: true
				count: 16L
				id: "1D00000000000002"
				item: { components: { "ftbfiltersystem:filter": "item_tag(minecraft:logs)" }, count: 1, id: "ftbfiltersystem:smart_filter" }
				type: "item"
			}]
			x: 1.0d
			y: 0.0d
		}
	]
}'''
TABELLE = '''{
	id: "1E8FEF386D179C90"
	loot_crate: { color: 1, drops: { boss: 0, monster: 8, passive: 3 }, string_id: "holzkiste" }
	loot_size: 3
	order_index: 2
	rewards: [{ count: 4, id: "4F6A1E62E5266307", item: { count: 1, id: "minecraft:string" }, weight: 10.0f }]
}'''
LANG = '''{
	chapter.1C00000000000001.title: "Akt I"
	quest.1B00000000000001.title: "Erde"
	quest.1B00000000000002.quest_desc: ["Zeile 1", "Zeile 2"]
	quest.1B00000000000002.title: "Holz"
	reward_table.1E8FEF386D179C90.title: "Holzkiste"
	chapter_group.1A00000000000001.title: "Hauptstory"
}'''


class ModellLaden(unittest.TestCase):
    def setUp(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'quests/chapters/akt1.snbt', KAPITEL)
        H.schreibe(o, 'quests/reward_tables/holz.snbt', TABELLE)
        H.schreibe(o, 'quests/lang/de_de.snbt', LANG)
        H.schreibe(o, 'quests/chapter_groups.snbt', '{ chapter_groups: [{ id: "1A00000000000001" }] }')
        H.schreibe(o, 'quests/data.snbt', '{ version: 13 }')
        self.b = modell.lade(o)

    def test_titel_und_kapitel_aus_lang(self):
        q = self.b.quests['1B00000000000002']
        self.assertEqual((q.titel, q.kapitel.titel, q.text), ('Holz', 'Akt I', ['Zeile 1', 'Zeile 2']))
        self.assertEqual(self.b.gruppen['1A00000000000001'], 'Hauptstory')

    def test_filter_aufgabe_wird_zur_gruppe(self):
        t = self.b.quests['1B00000000000002'].aufgaben[0]
        self.assertEqual((t.item, t.tag, t.anzahl, t.verbraucht), (None, 'minecraft:logs', 16, True))

    def test_tabellen_id_als_long_wird_hex(self):
        r = self.b.quests['1B00000000000002'].belohnungen[0]
        self.assertEqual((r.typ, r.tabelle, r.team), ('loot', '1E8FEF386D179C90', True))
        self.assertEqual(self.b.tabellen['1E8FEF386D179C90'].eintraege, [('minecraft:string', 4, 10.0)])
        self.assertEqual(self.b.tabellen['1E8FEF386D179C90'].kiste['drops']['monster'], 8)

    def test_wiederholbar_und_optional(self):
        q = self.b.quests['1B00000000000002']
        self.assertEqual((q.optional, q.wiederholbar, q.abklingzeit), (True, True, 1200))

    def test_ahnen(self):
        self.assertEqual(self.b.ahnen('1B00000000000002'), {'1B00000000000001'})
        self.assertEqual(self.b.ahnen('1B00000000000001'), set())

    def test_verweise(self):
        self.assertEqual(self.b.kapitel[0].links[0]['linked_quest'], '1B00000000000009')


class LongNachHex(unittest.TestCase):
    def test_negative_long(self):
        self.assertEqual(modell.long_hex(-1), 'FFFFFFFFFFFFFFFF')

    def test_positive_long(self):
        self.assertEqual(modell.long_hex(0x1E8FEF386D179C90), '1E8FEF386D179C90')


if __name__ == '__main__':
    unittest.main()

import copy
import io
import os
import unittest
import zipfile
import hilfen as H
from hilfen import quest, aufgabe, gib, buch
from pruefung import idvergleich as V
from pruefung.modell import Tabelle


def basis():
    a = quest('1000000000000001', 'Start', aufgaben=[aufgabe('minecraft:dirt', id='2000000000000001')],
              belohnungen=[gib('minecraft:stick', id='3000000000000001')])
    c = quest('1000000000000002', 'Zweite', deps=['1000000000000001'],
              aufgaben=[aufgabe('minecraft:oak_log', n=4, id='2000000000000002')])
    b = buch([a, c], tabellen=[Tabelle(id='4000000000000001', datei='holz', kiste={'string_id': 'holzkiste'})])
    return b


def stufen(befunde):
    return sorted((x.stufe, x.text.split(':')[0]) for x in befunde)


class Vergleich(unittest.TestCase):
    def test_gleich_ohne_befund(self):
        self.assertEqual(V.vergleiche(basis(), basis()), [])

    def test_entfallene_quest_ist_fehler(self):
        neu = basis()
        del neu.quests['1000000000000002']
        neu.kapitel[0].quests.pop()
        self.assertEqual([x.stufe for x in V.vergleiche(basis(), neu)], ['FEHLER'])

    def test_entfallene_aufgabe_ist_warnung(self):
        neu = basis()
        neu.quests['1000000000000002'].aufgaben[0].id = '2000000000000009'
        st = sorted(x.stufe for x in V.vergleiche(basis(), neu))
        self.assertEqual(st, ['WARNUNG', 'WARNUNG'])   # alte weg, neue dazu

    def test_neue_belohnungs_id_ist_doppelt_abholbar(self):
        neu = basis()
        neu.quests['1000000000000001'].belohnungen[0].id = '3000000000000009'
        t = [x.text for x in V.vergleiche(basis(), neu) if x.stufe == 'WARNUNG']
        self.assertTrue(any('erneut' in s for s in t))

    def test_neuer_befehl_als_belohnung_nur_hinweis(self):
        # Ein erneut abholbarer Befehl (z. B. Feuerwerk) verdoppelt keine Items
        from pruefung.modell import Belohnung
        neu = basis()
        neu.quests['1000000000000001'].belohnungen.append(Belohnung(id='3000000000000005', typ='command', befehl='function x:y'))
        self.assertEqual([x.stufe for x in V.vergleiche(basis(), neu)], ['HINWEIS'])

    def test_geaenderte_aufgabe_gleiche_id(self):
        neu = basis()
        neu.quests['1000000000000002'].aufgaben[0].anzahl = 8
        self.assertEqual([x.stufe for x in V.vergleiche(basis(), neu)], ['HINWEIS'])

    def test_kisten_kennung_geaendert(self):
        neu = basis()
        neu.tabellen['4000000000000001'].kiste = {'string_id': 'holz_kiste'}
        self.assertEqual([x.stufe for x in V.vergleiche(basis(), neu)], ['WARNUNG'])

    def test_id_wechselt_objektart(self):
        neu = basis()
        neu.quests['1000000000000002'].aufgaben[0].id = '3000000000000001'   # war eine Belohnung
        self.assertIn('FEHLER', [x.stufe for x in V.vergleiche(basis(), neu)])


class Referenz(unittest.TestCase):
    KAP = '{ filename: "k1" group: "6000000000000001" id: "C000000000000001" order_index: 0 quest_links: [ ] ' \
          'quests: [{ id: "1000000000000001" tasks: [{ id: "2000000000000001" item: { count: 1, id: "minecraft:dirt" } type: "item" }] x: 0.0d y: 0.0d }] }'

    def test_mrpack_als_referenz(self):
        o = H.temp_ordner(self)
        pfad = os.path.join(o, 'Sky and Stone-0.9.0.mrpack')
        with zipfile.ZipFile(pfad, 'w') as z:
            z.writestr('overrides/config/ftbquests/quests/chapters/k1.snbt', self.KAP)
            z.writestr('overrides/config/ftbquests/quests/lang/de_de.snbt', '{ quest.1000000000000001.title: "Erde" }')
        b = V.lade_referenz(pfad)
        self.assertEqual(b.quests['1000000000000001'].titel, 'Erde')

    def test_ordner_mit_chapters_tief_drin(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'ftbquests/quests/chapters/k1.snbt', self.KAP)
        self.assertIn('1000000000000001', V.lade_referenz(o).quests)

    def test_neuestes_mrpack_nach_version(self):
        o = H.temp_ordner(self)
        for v in ('0.9.0', '0.10.0', '1.0.0', '0.20.0'):
            open(os.path.join(o, f'Sky and Stone-{v}.mrpack'), 'wb').close()
        self.assertTrue(V.neuestes_mrpack(o).endswith('Sky and Stone-1.0.0.mrpack'))


if __name__ == '__main__':
    unittest.main()

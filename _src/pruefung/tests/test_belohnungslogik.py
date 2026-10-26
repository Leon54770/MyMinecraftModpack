import unittest
import hilfen as H
from hilfen import quest, aufgabe, gib, kiste, buch
from pruefung import belohnungslogik as BL
from pruefung.modell import Tabelle


def texte(befunde, stufe=None):
    return [x.text for x in befunde if stufe is None or x.stufe == stufe]


START = lambda **kw: quest('1000000000000001', 'Start', aufgaben=[aufgabe('a:start')], **kw)


class ErfuelltAndereQuest(unittest.TestCase):
    def test_belohnung_erfuellt_spaetere_aufgabe(self):
        b = buch([START(belohnungen=[gib('a:mixer', 1)]),
                  quest('1000000000000002', 'Mixer bauen', deps=['1000000000000001'], aufgaben=[aufgabe('a:mixer')])])
        t = texte(BL.pruefe(b, tags={}))
        self.assertEqual(len(t), 1)
        self.assertIn('Mixer bauen', t[0])

    def test_zu_wenig_ist_kein_befund(self):
        b = buch([START(belohnungen=[gib('a:eisen', 2)]),
                  quest('1000000000000002', 'Eisen', deps=['1000000000000001'], aufgaben=[aufgabe('a:eisen', 10)])])
        self.assertEqual(BL.pruefe(b, tags={}), [])

    def test_vorher_erledigte_quest_ist_egal(self):
        b = buch([quest('1000000000000001', 'Start', aufgaben=[aufgabe('a:mixer')]),
                  quest('1000000000000002', 'Danach', deps=['1000000000000001'], aufgaben=[aufgabe('a:x')],
                        belohnungen=[gib('a:mixer')])])
        self.assertEqual(BL.pruefe(b, tags={}), [])

    def test_sammelquest_nur_teilweise_ist_kein_befund(self):
        # „Alle Essenzen“ mit vielen Aufgaben: eine belohnte Essenz erledigt die Quest nicht
        b = buch([START(belohnungen=[gib('a:inferium', 16)]),
                  quest('1000000000000002', 'Alle Essenzen', deps=['1000000000000001'],
                        aufgaben=[aufgabe('a:inferium'), aufgabe('a:prudentium')])])
        self.assertEqual(BL.pruefe(b, tags={}), [])

    def test_alle_aufgaben_durch_belohnungen_erfuellt(self):
        b = buch([START(belohnungen=[gib('a:rucksack'), gib('a:upgrade')]),
                  quest('1000000000000002', 'Rucksack', deps=['1000000000000001'],
                        aufgaben=[aufgabe('a:rucksack'), aufgabe('a:upgrade')])])
        self.assertEqual(len(BL.pruefe(b, tags={})), 1)

    def test_gruppenaufgabe_zaehlt(self):
        b = buch([START(belohnungen=[gib('a:eiche', 8)]),
                  quest('1000000000000002', 'Holz', deps=['1000000000000001'], aufgaben=[aufgabe(tag='c:logs', n=8)])])
        self.assertEqual(len(BL.pruefe(b, tags={'c:logs': ['a:eiche', 'a:birke']})), 1)


class Markt(unittest.TestCase):
    def tausch(self, id, nimmt, n, tabelle):
        return quest(id, f'Tausch {nimmt}', deps=['1000000000000001'], wiederholbar=True, abklingzeit=1200,
                     aufgaben=[aufgabe(nimmt, n, verbraucht=True)], belohnungen=[kiste(tabelle)])

    def test_tausch_gibt_mehr_zurueck_als_er_nimmt(self):
        t = Tabelle(id='3000000000000001', titel='Kiste', loot_size=3, eintraege=[('a:kies', 64, 1.0)])
        b = buch([START(), self.tausch('1000000000000002', 'a:kies', 64, '3000000000000001')], tabellen=[t])
        self.assertTrue(texte(BL.pruefe(b, tags={}), 'FEHLER'))

    def test_kreis_mit_gewinn(self):
        # 10 Kies -> Kiste mit Erwartung 20 Sand; 10 Sand -> Kiste mit Erwartung 20 Kies: Kreis mit Faktor 4
        t1 = Tabelle(id='3000000000000001', titel='K1', loot_size=1, eintraege=[('a:sand', 20, 1.0)])
        t2 = Tabelle(id='3000000000000002', titel='K2', loot_size=1, eintraege=[('a:kies', 20, 1.0)])
        b = buch([START(), self.tausch('1000000000000002', 'a:kies', 10, '3000000000000001'),
                  self.tausch('1000000000000003', 'a:sand', 10, '3000000000000002')], tabellen=[t1, t2])
        w = texte(BL.pruefe(b, tags={}), 'WARNUNG')
        self.assertTrue(any('Kreis' in x for x in w))

    def test_verlustkreis_ist_kein_befund(self):
        t1 = Tabelle(id='3000000000000001', titel='K1', loot_size=1, eintraege=[('a:sand', 5, 1.0), ('a:x', 1, 1.0)])
        t2 = Tabelle(id='3000000000000002', titel='K2', loot_size=1, eintraege=[('a:kies', 5, 1.0)])
        b = buch([START(), self.tausch('1000000000000002', 'a:kies', 10, '3000000000000001'),
                  self.tausch('1000000000000003', 'a:sand', 10, '3000000000000002')], tabellen=[t1, t2])
        self.assertEqual(BL.pruefe(b, tags={}), [])


class KistenKopie(unittest.TestCase):
    def test_gleiche_kistendaten_wie_andere_tabelle(self):
        gold = Tabelle(id='3000000000000001', titel='Goldkiste', kiste={'color': 1, 'glow': False, 'drops': {'monster': 0, 'passive': 0, 'boss': 5}})
        messing = Tabelle(id='3000000000000002', titel='Messing-Kiste', kiste={'color': 1, 'glow': False, 'drops': {'monster': 0, 'passive': 0, 'boss': 5}})
        holz = Tabelle(id='3000000000000003', titel='Holzkiste', kiste={'color': 2, 'glow': False, 'drops': {'monster': 8, 'passive': 3, 'boss': 0}})
        b = buch([START()], tabellen=[gold, messing, holz])
        t = texte(BL.pruefe(b, tags={}), 'HINWEIS')
        self.assertEqual(len(t), 1)
        self.assertTrue('Goldkiste' in t[0] and 'Messing-Kiste' in t[0])


class Kisten(unittest.TestCase):
    def test_kistenchance_je_kill(self):
        t1 = Tabelle(id='3000000000000001', titel='Holz', kiste={'drops': {'monster': 8, 'passive': 3, 'boss': 0}})
        t2 = Tabelle(id='3000000000000002', titel='Eisen', kiste={'drops': {'monster': 2, 'passive': 0, 'boss': 0}})
        b = buch([START()], tabellen=[t1, t2])
        b.daten = {'loot_crate_no_drop': {'monster': 990, 'passive': 4000, 'boss': 0}}
        k = BL.kistenchancen(b)
        self.assertAlmostEqual(k['monster']['gesamt'], 10 / 1000)
        self.assertAlmostEqual(k['monster']['Holz'], 8 / 1000)
        self.assertAlmostEqual(k['passive']['gesamt'], 3 / 4003)


if __name__ == '__main__':
    unittest.main()

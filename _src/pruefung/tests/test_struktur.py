import unittest
import hilfen as H
from hilfen import quest, aufgabe, gib, kiste, buch
from pruefung import struktur as S
from pruefung.befund import Register
from pruefung.modell import Tabelle

REG = Register(items={'minecraft:dirt', 'minecraft:stick', 'minecraft:oak_log', 'minecraft:iron_ingot',
                      'minecraft:shulker_box', 'minecraft:ender_pearl'},
               tags={'minecraft:logs': ['minecraft:oak_log'], 'c:leer': []},
               entities={'minecraft:wither'}, dimensionen={'minecraft:the_nether'},
               stapel={'minecraft:shulker_box': 1, 'minecraft:ender_pearl': 16, 'minecraft:dirt': 64})


def texte(befunde, stufe=None):
    return [b.text for b in befunde if stufe is None or b.stufe == stufe]


def start():
    return quest('1000000000000001', 'Start', aufgaben=[aufgabe('minecraft:dirt', id='2000000000000001')])


class Graph(unittest.TestCase):
    def test_fehlende_voraussetzung(self):
        b = buch([start(), quest('1000000000000002', deps=['1000000000000099'], aufgaben=[aufgabe('minecraft:dirt')])])
        self.assertTrue(any('1000000000000099' in t for t in texte(S.pruefe_graph(b), 'FEHLER')))

    def test_zyklus_wird_einmal_gemeldet(self):
        a = quest('1000000000000002', deps=['1000000000000003'], aufgaben=[aufgabe('minecraft:dirt')])
        c = quest('1000000000000003', deps=['1000000000000002'], aufgaben=[aufgabe('minecraft:dirt')])
        zyklen = [t for t in texte(S.pruefe_graph(buch([start(), a, c])), 'FEHLER') if 'Zyklus' in t]
        self.assertEqual(len(zyklen), 1)

    def test_zweite_quest_ohne_voraussetzung(self):
        frei = quest('1000000000000002', 'Frei', aufgaben=[aufgabe('minecraft:dirt')])
        self.assertTrue(any('Frei' in t for t in texte(S.pruefe_graph(buch([start(), frei])), 'WARNUNG')))

    def test_pflicht_an_optional(self):
        opt = quest('1000000000000002', 'Opt', deps=['1000000000000001'], optional=True, aufgaben=[aufgabe('minecraft:dirt')])
        pfl = quest('1000000000000003', 'Pflicht', deps=['1000000000000002'], aufgaben=[aufgabe('minecraft:dirt')])
        self.assertTrue(any('Pflicht' in t and 'Opt' in t for t in texte(S.pruefe_graph(buch([start(), opt, pfl])))))

    def test_eins_von_braucht_zwei(self):
        q = quest('1000000000000002', deps=['1000000000000001'], dep_any=True, aufgaben=[aufgabe('minecraft:dirt')])
        self.assertTrue(any('eins von' in t for t in texte(S.pruefe_graph(buch([start(), q])))))

    def test_sauberer_graph_ohne_befund(self):
        q = quest('1000000000000002', deps=['1000000000000001'], aufgaben=[aufgabe('minecraft:dirt')])
        self.assertEqual(S.pruefe_graph(buch([start(), q])), [])


class Aufgaben(unittest.TestCase):
    def pruefe(self, *aufgaben, **kw):
        q = quest('1000000000000002', 'Q', deps=['1000000000000001'], aufgaben=list(aufgaben), **kw)
        return S.pruefe_aufgaben(buch([start(), q]), REG)

    def test_unbekanntes_item(self):
        self.assertTrue(texte(self.pruefe(aufgabe('mod:gibtsnicht')), 'FEHLER'))

    def test_leere_gruppe(self):
        self.assertTrue(texte(self.pruefe(aufgabe(tag='c:leer')), 'FEHLER'))

    def test_unbekannte_gruppe(self):
        self.assertTrue(texte(self.pruefe(aufgabe(tag='c:unbekannt')), 'FEHLER'))

    def test_gruppe_beim_verbrauchen_verboten(self):
        self.assertTrue(texte(self.pruefe(aufgabe(tag='minecraft:logs', verbraucht=True)), 'FEHLER'))

    def test_haken_verboten(self):
        self.assertTrue(texte(self.pruefe(aufgabe(typ='checkmark')), 'FEHLER'))

    def test_quest_ohne_aufgabe(self):
        self.assertTrue(texte(self.pruefe(), 'FEHLER'))

    def test_anzahl_null(self):
        self.assertTrue(texte(self.pruefe(aufgabe('minecraft:dirt', n=0)), 'FEHLER'))

    def test_unbekannter_mob_und_dimension(self):
        self.assertEqual(len(texte(self.pruefe(aufgabe(typ='kill', entity='minecraft:zombie', n=1),
                                               aufgabe(typ='dimension', dimension='minecraft:the_end')), 'FEHLER')), 2)

    def test_bekannter_mob_ok(self):
        self.assertEqual(self.pruefe(aufgabe(typ='kill', entity='minecraft:wither')), [])

    def test_mehr_als_ins_inventar_passt(self):
        # 37 Plätze (36 + Nebenhand) mal Stapelgröße 16 = 592
        self.assertTrue(texte(self.pruefe(aufgabe('minecraft:ender_pearl', n=593)), 'WARNUNG'))
        self.assertEqual(self.pruefe(aufgabe('minecraft:ender_pearl', n=592)), [])

    def test_verbrauchen_darf_mehr_als_inventar(self):
        self.assertEqual(self.pruefe(aufgabe('minecraft:shulker_box', n=40, verbraucht=True)), [])

    def test_wiederholbar_ohne_verbrauch_ist_fehler(self):
        self.assertTrue(texte(self.pruefe(aufgabe('minecraft:dirt', n=64), wiederholbar=True, abklingzeit=1200), 'FEHLER'))

    def test_wiederholbar_mit_verbrauch_ok(self):
        self.assertEqual(self.pruefe(aufgabe('minecraft:dirt', n=64, verbraucht=True), wiederholbar=True, abklingzeit=1200), [])


class Belohnungen(unittest.TestCase):
    def pruefe(self, belohnungen, tabellen=()):
        q = quest('1000000000000002', 'Q', deps=['1000000000000001'], aufgaben=[aufgabe('minecraft:dirt')],
                  belohnungen=belohnungen)
        return S.pruefe_belohnungen(buch([start(), q], tabellen=tabellen), REG)

    def test_unbekanntes_belohnungs_item(self):
        self.assertTrue(texte(self.pruefe([gib('mod:weg')]), 'FEHLER'))

    def test_fehlende_tabelle(self):
        self.assertTrue(texte(self.pruefe([kiste('3000000000000009')]), 'FEHLER'))

    def test_auswahl_mit_einem_eintrag(self):
        t = Tabelle(id='3000000000000001', eintraege=[('minecraft:stick', 1, 1.0)])
        self.assertTrue(texte(self.pruefe([kiste('3000000000000001', art='choice')], [t]), 'WARNUNG'))

    def test_tabelle_mit_unbekanntem_item_und_gewicht_null(self):
        t = Tabelle(id='3000000000000001', eintraege=[('mod:weg', 1, 1.0), ('minecraft:stick', 1, 0.0)])
        self.assertEqual(len(texte(self.pruefe([kiste('3000000000000001')], [t]), 'FEHLER')), 2)


class Ids(unittest.TestCase):
    def test_doppelte_id_ueber_objektarten(self):
        q = quest('1000000000000002', deps=['1000000000000001'], aufgaben=[aufgabe('minecraft:dirt', id='1000000000000001')])
        self.assertTrue(texte(S.pruefe_ids(buch([start(), q])), 'FEHLER'))

    def test_ungueltige_id(self):
        q = quest('12XY', deps=['1000000000000001'], aufgaben=[aufgabe('minecraft:dirt', id='2000000000000005')])
        self.assertTrue(texte(S.pruefe_ids(buch([start(), q])), 'FEHLER'))


if __name__ == '__main__':
    unittest.main()

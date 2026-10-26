import unittest
import hilfen as H
from hilfen import quest, aufgabe, buch
from pruefung import struktur as S
from pruefung.modell import Kapitel


def texte(befunde, stufe=None):
    return [b.text for b in befunde if stufe is None or b.stufe == stufe]


def zwei_kapitel():
    a = quest('1000000000000001', 'Start', aufgaben=[aufgabe('minecraft:dirt')])
    c = quest('1000000000000002', 'Zweite', deps=['1000000000000001'], aufgaben=[aufgabe('minecraft:dirt')])
    b = buch([a])
    k2 = Kapitel(id='C000000000000002', datei='k2', titel='Kapitel 2', gruppe='6000000000000001', order_index=1)
    c.kapitel = k2
    k2.quests.append(c)
    b.kapitel.append(k2)
    b.quests[c.id] = c
    return b, k2


class Verweise(unittest.TestCase):
    def test_verweis_auf_fehlende_quest(self):
        b, k2 = zwei_kapitel()
        k2.links.append({'id': 'E000000000000001', 'linked_quest': '1000000000000099'})
        self.assertTrue(texte(S.pruefe_verweise(b), 'FEHLER'))

    def test_verweis_im_eigenen_kapitel(self):
        b, k2 = zwei_kapitel()
        k2.links.append({'id': 'E000000000000001', 'linked_quest': '1000000000000002'})
        self.assertTrue(texte(S.pruefe_verweise(b), 'HINWEIS'))

    def test_voraussetzung_aus_anderem_kapitel_ohne_verweis(self):
        # Ohne Verweis zeichnet FTB keine Linie. Ein Hinweis je Kapitel, nicht je Linie (sonst 80 Meldungen)
        b, k2 = zwei_kapitel()
        k2.quests.append(H.quest('1000000000000003', 'Dritte', deps=['1000000000000001'], aufgaben=[aufgabe('minecraft:dirt')]))
        k2.quests[-1].kapitel = k2
        b.quests['1000000000000003'] = k2.quests[-1]
        h = texte(S.pruefe_verweise(b), 'HINWEIS')
        self.assertEqual(len(h), 1)
        self.assertIn('Start', h[0])
        self.assertIn('2 Linien', h[0])

    def test_mit_verweis_kein_befund(self):
        b, k2 = zwei_kapitel()
        k2.links.append({'id': 'E000000000000001', 'linked_quest': '1000000000000001'})
        self.assertEqual(S.pruefe_verweise(b), [])


class Sprache(unittest.TestCase):
    def test_quest_ohne_titel(self):
        b = buch([quest('1000000000000001', '', aufgaben=[aufgabe('minecraft:dirt')])])
        b.quests['1000000000000001'].titel = ''
        self.assertTrue(texte(S.pruefe_sprache(b), 'FEHLER'))

    def test_verwaister_schluessel(self):
        b = buch([quest('1000000000000001', 'Start', aufgaben=[aufgabe('minecraft:dirt')])])
        b.lang = {'quest.1000000000000001.title': 'Start', 'quest.10000000000000FF.title': 'Weg',
                  'chapter.C000000000000001.title': 'Kapitel 1'}
        b.lang_en = dict(b.lang)
        self.assertTrue(any('10000000000000FF' in t for t in texte(S.pruefe_sprache(b), 'HINWEIS')))

    def test_englisch_fehlt_schluessel(self):
        b = buch([quest('1000000000000001', 'Start', aufgaben=[aufgabe('minecraft:dirt')])])
        b.lang = {'quest.1000000000000001.title': 'Start', 'chapter.C000000000000001.title': 'Kapitel 1'}
        b.lang_en = {'chapter.C000000000000001.title': 'Kapitel 1'}
        self.assertTrue(texte(S.pruefe_sprache(b), 'HINWEIS'))


class Kapitelpruefung(unittest.TestCase):
    def test_unbekannte_gruppe(self):
        b, k2 = zwei_kapitel()
        k2.gruppe = '6000000000000009'
        self.assertTrue(texte(S.pruefe_kapitel(b), 'FEHLER'))

    def test_doppelte_reihenfolge_in_gruppe(self):
        b, k2 = zwei_kapitel()
        k2.order_index = 0
        self.assertTrue(texte(S.pruefe_kapitel(b), 'WARNUNG'))

    def test_dateiname_passt_nicht(self):
        b, k2 = zwei_kapitel()
        k2.roh = {'filename': 'anders'}
        self.assertTrue(texte(S.pruefe_kapitel(b), 'FEHLER'))

    def test_leeres_kapitel(self):
        b, k2 = zwei_kapitel()
        b.kapitel.append(Kapitel(id='C000000000000003', datei='k3', titel='Leer', gruppe='6000000000000001', order_index=2))
        self.assertTrue(texte(S.pruefe_kapitel(b), 'WARNUNG'))


if __name__ == '__main__':
    unittest.main()

"""Tests für die Prüfungen vom 26.10.2026: Strom-Aufgabe ohne max_input, Texte (Zahlen, Farbcodes, Stil),
Kisten-Texte im Generator."""
import os
import sys
import unittest

import hilfen as H
from hilfen import quest, aufgabe, buch
from pruefung import struktur as S
from pruefung import texte as T
from pruefung.befund import Register

REG = Register(items={'minecraft:dirt', 'exdeorum:iron_ore_chunk'}, tags={})
NAMEN = {'exdeorum:iron_ore_chunk': 'Iron Ore Chunk', 'minecraft:dirt': 'Erde'}


def texte(befunde, stufe=None):
    return [b.text for b in befunde if stufe is None or b.stufe == stufe]


def start():
    return quest('1000000000000001', 'Start', aufgaben=[aufgabe('minecraft:dirt', id='2000000000000001')])


class StromTest(unittest.TestCase):
    def pruefe(self, **roh):
        q = quest('1000000000000002', 'Speicher', deps=['1000000000000001'],
                  aufgaben=[aufgabe(typ='forge_energy', id='2000000000000002', **roh)])
        return texte(S.pruefe_aufgaben(buch([start(), q]), REG), 'FEHLER')

    def test_ohne_max_input_ist_fehler(self):
        self.assertTrue(any('max_input' in t for t in self.pruefe(value=1000)))

    def test_mit_max_input_ok(self):
        self.assertFalse(any('max_input' in t for t in self.pruefe(value=1000, max_input=1000)))


class ZahlenTest(unittest.TestCase):
    def pruefe(self, text, n):
        q = quest('1000000000000002', 'Erz', deps=['1000000000000001'], text=text,
                  aufgaben=[aufgabe('exdeorum:iron_ore_chunk', n, id='2000000000000002')])
        return texte(T.pruefe_zahlen(buch([start(), q]), NAMEN), 'WARNUNG')

    def test_falsche_zahl(self):
        self.assertEqual(len(self.pruefe(['Sammle 4 &eIron Ore Chunk&r.'], 8)), 1)

    def test_passende_zahl_unter_mehreren(self):
        self.assertEqual(self.pruefe(['Sammle 8 &eIron Ore Chunk&r.', '4 Iron Ore Chunk ergeben 1 Erz.'], 8), [])

    def test_rezept_ergebnis_zaehlt_nicht(self):
        self.assertEqual(self.pruefe(['4 Kies + 1 Wasser = 2 Iron Ore Chunk.'], 8), [])

    def test_ohne_zahl_kein_befund(self):
        self.assertEqual(self.pruefe(['Sammle &eIron Ore Chunk&r.'], 8), [])


class FarbcodeTest(unittest.TestCase):
    def pruefe(self, text):
        return T.pruefe_farbcodes(buch([quest('1000000000000001', 'Start', text=text)]))

    def test_ungueltiger_code(self):
        self.assertTrue(texte(self.pruefe(['Ein &zFehler']), 'FEHLER'))

    def test_kursiv_ohne_notiz(self):
        self.assertTrue(texte(self.pruefe(['&oNur kursiv']), 'WARNUNG'))

    def test_kaufmanns_und_ok(self):
        self.assertEqual(texte(self.pruefe(['Create Crafts & Additions']), 'FEHLER'), [])

    def test_story_notiz_ok(self):
        self.assertEqual(texte(self.pruefe(['&o„Eine Notiz.“'])), [])


class StilTest(unittest.TestCase):
    def test_floskel(self):
        q = quest('1000000000000001', 'Start', text=['Perfekt! Weiter geht es.'])
        self.assertTrue(texte(T.pruefe_stil(buch([q])), 'WARNUNG'))

    def test_hauptstory_zu_lang(self):
        q = quest('1000000000000001', 'Start', text=['x'] * 7)
        b = buch([q]); b.kapitel[0].datei = 'akt1'
        self.assertTrue(any('6' in t for t in texte(T.pruefe_stil(b), 'WARNUNG')))


class StilNotizTest(unittest.TestCase):
    def test_notiz_zaehlt_nicht(self):
        q = quest('1000000000000001', 'Start', text=['&5&lNotiz: X', '&o„Zitat.“', ''] + ['x'] * 6)
        b = buch([q]); b.kapitel[0].datei = 'akt1'
        self.assertEqual(texte(T.pruefe_stil(b), 'WARNUNG'), [])


class KistenTextTest(unittest.TestCase):
    """quests.pruefe_kisten_texte: Herkunftszeile muss zu den Drops passen."""

    @classmethod
    def setUpClass(cls):
        src = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        sys.path.insert(0, src)
        import quests
        cls.f = staticmethod(quests.pruefe_kisten_texte)

    def tab(self, boss=0, monster=0, passive=0):
        return {'gold': ('ID', {'loot_crate': {'drops': {'boss': boss, 'monster': monster, 'passive': passive}}})}

    def test_passend(self):
        self.assertEqual(self.f(self.tab(boss=5), {'goldkiste': ('x', 'Von Bossen.')}), [])

    def test_boss_fehlt_im_text(self):
        self.assertEqual(len(self.f(self.tab(boss=5), {'goldkiste': ('x', 'Nur aus dem Questbuch.')})), 1)

    def test_text_fehlt(self):
        self.assertEqual(len(self.f(self.tab(), {})), 1)


if __name__ == '__main__':
    unittest.main()

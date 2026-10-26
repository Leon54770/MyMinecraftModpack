import unittest
import _pfad  # noqa: F401
from pruefung.befund import warnung, hinweis
from pruefung import ausnahmen


class Ausnahmen(unittest.TestCase):
    LISTE = [ausnahmen.Ausnahme('Spiellogik', r'Belohnung .*exdeorum:silkworm', 'Startbelohnung bewusst (0.6.3)')]

    def test_trennt_akzeptierte_befunde(self):
        befunde = [warnung('Spiellogik', '„Start“ (akt1): Belohnung Silkworm (exdeorum:silkworm) ist ein Quest-Item …'),
                   warnung('Spiellogik', '„Polonium“ (akt3): … fehlt Zerkleinerer')]
        offen, akzeptiert = ausnahmen.anwenden(befunde, self.LISTE)
        self.assertEqual([b.text[:10] for b in offen], ['„Polonium“'])
        self.assertEqual(len(akzeptiert), 1)
        self.assertEqual(akzeptiert[0][1].grund, 'Startbelohnung bewusst (0.6.3)')

    def test_bereich_muss_passen(self):
        offen, akzeptiert = ausnahmen.anwenden([hinweis('Questbuch', 'Belohnung exdeorum:silkworm')], self.LISTE)
        self.assertEqual((len(offen), len(akzeptiert)), (1, 0))

    def test_unbenutzte_ausnahme_wird_gemeldet(self):
        # Eine Ausnahme, die nichts mehr trifft, ist veraltet und soll auffallen
        offen, akzeptiert = ausnahmen.anwenden([], self.LISTE)
        self.assertEqual(ausnahmen.unbenutzt(self.LISTE, akzeptiert), self.LISTE)


if __name__ == '__main__':
    unittest.main()

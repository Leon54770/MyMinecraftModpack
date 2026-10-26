import unittest
import hilfen as H
from hilfen import quest, aufgabe, gib, kiste, buch
from pruefung import stufen
from pruefung.huelle import Regel
from pruefung.befund import Register
from pruefung.modell import Tabelle


def r(id, ein, aus, haupt=None, neben=(), annahme=False, notiz=''):
    return Regel(id=id, typ='t', eingaben=[frozenset(g) for g in ein], ausgaben=frozenset(aus),
                 haupt=frozenset(haupt) if haupt else None, neben=[frozenset(g) for g in neben], annahme=annahme, notiz=notiz)


class M:
    """Minimales Modell wie laden.Modell."""
    def __init__(self, regeln, start, tags=None):
        self.regeln, self.start = regeln, set(start)
        self.register = Register(items=set(), tags=tags or {})


REGELN = [
    r('mixer', [{'log'}, {'erz'}], {'mixer'}),
    r('messing', [{'kupfer'}, {'zink'}], {'messing'}, haupt={'mixer'}),
    r('presse', [{'log'}], {'presse'}),
    r('blech', [{'messing'}], {'blech'}, haupt={'presse'}),
    r('stern', [{'ganzweit'}], {'stern'}),
    r('honig', [{'log'}], {'honig'}, annahme=True, notiz='Bienen im Biom'),
    r('unnuetz', [{'log'}], {'z'}, annahme=True, notiz='hat mit Honig nichts zu tun'),
]
MODELL = M(REGELN, {'log', 'erz', 'kupfer', 'zink'})


def b(*qs, tabellen=()):
    return buch(list(qs), tabellen=tabellen)


def texte(e, stufe=None):
    return [x.text for x in e.befunde if stufe is None or x.stufe == stufe]


A = lambda **kw: quest('1000000000000001', 'Start', aufgaben=[aufgabe('log')], **kw)


class Vorgriff(unittest.TestCase):
    def test_station_aus_nicht_vorausgesetzter_quest(self):
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Mixer', deps=['1000000000000001'], aufgaben=[aufgabe('mixer')]),
                            quest('1000000000000003', 'Messing', deps=['1000000000000001'], aufgaben=[aufgabe('messing')])), MODELL)
        w = texte(e, 'WARNUNG')
        self.assertEqual(len(w), 1)
        self.assertIn('Messing', w[0])
        self.assertIn('mixer', w[0])
        self.assertIn('Mixer', w[0])            # nennt die Quest, die den Mixer einführt

    def test_mit_voraussetzung_kein_befund(self):
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Mixer', deps=['1000000000000001'], aufgaben=[aufgabe('mixer')]),
                            quest('1000000000000003', 'Messing', deps=['1000000000000002'], aufgaben=[aufgabe('messing')])), MODELL)
        self.assertEqual(texte(e), [])

    def test_station_in_derselben_quest(self):
        # „Baue den Mixer und mache Messing“ in einer Quest ist in Ordnung
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Beides', deps=['1000000000000001'],
                                       aufgaben=[aufgabe('mixer'), aufgabe('messing')])), MODELL)
        self.assertEqual(texte(e), [])

    def test_kette_aus_zwei_stationen(self):
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Mixer', deps=['1000000000000001'], aufgaben=[aufgabe('mixer')]),
                            quest('1000000000000003', 'Blech', deps=['1000000000000002'], aufgaben=[aufgabe('blech')])), MODELL)
        w = texte(e, 'WARNUNG')
        self.assertEqual(len(w), 1)
        self.assertIn('presse', w[0])
        self.assertNotIn('mixer', w[0].split('fehlt')[1] if 'fehlt' in w[0] else '')

    def test_von_keiner_quest_eingefuehrt(self):
        e = stufen.pruefe(b(A(), quest('1000000000000003', 'Messing', deps=['1000000000000001'], aufgaben=[aufgabe('messing')])), MODELL)
        self.assertTrue(any('keine Quest' in t for t in texte(e, 'WARNUNG')))

    def test_nennt_ersatzstation(self):
        regeln = [r('mek', [{'obsidian'}], {'mek_staub'}, haupt={'zerkleinerer'}),
                  r('create', [{'obsidian'}], {'create_staub'}, haupt={'brechwalzen'}),
                  r('raff', [{'mek_staub', 'create_staub'}], {'raff'}),
                  r('zerkleinerer', [{'log'}], {'zerkleinerer'}), r('brechwalzen', [{'log'}], {'brechwalzen'})]
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Raff', deps=['1000000000000001'], aufgaben=[aufgabe('raff')])),
                          M(regeln, {'log', 'obsidian'}))
        w = texte(e, 'WARNUNG')
        self.assertEqual(len(w), 1)
        self.assertIn('oder', w[0])
        self.assertTrue('zerkleinerer' in w[0] and 'brechwalzen' in w[0])

    def test_optionale_quest_nur_hinweis(self):
        e = stufen.pruefe(b(A(), quest('1000000000000003', 'Messing', deps=['1000000000000001'], optional=True,
                                       aufgaben=[aufgabe('messing')])), MODELL)
        self.assertEqual(len(texte(e, 'HINWEIS')), 1)
        self.assertEqual(texte(e, 'WARNUNG'), [])


class Erreichbarkeit(unittest.TestCase):
    def test_global_unerreichbar_mit_wurzel(self):
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Stern', deps=['1000000000000001'], aufgaben=[aufgabe('stern')])), MODELL)
        w = texte(e, 'WARNUNG')
        self.assertTrue(any('stern' in t and 'ganzweit' in t for t in w))

    def test_nur_ueber_annahme_nennt_die_noetige_annahme(self):
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Honig', deps=['1000000000000001'], aufgaben=[aufgabe('honig')])), MODELL)
        h = [t for t in texte(e, 'HINWEIS') if 'Annahme' in t]
        self.assertEqual(len(h), 1)
        self.assertIn('Bienen im Biom', h[0])
        self.assertNotIn('nichts zu tun', h[0])


MESSING_Q = quest('1000000000000009', 'Messing später', deps=['1000000000000001'], optional=True, aufgaben=[aufgabe('messing')])


class Belohnung(unittest.TestCase):
    def test_belohnung_zu_frueh(self):
        # Messing ist Aufgabe einer anderen Quest und hier noch nicht herstellbar
        e = stufen.pruefe(b(A(belohnungen=[gib('messing')]), MESSING_Q), MODELL)
        self.assertTrue(any('messing' in t and 'Belohnung' in t for t in texte(e, 'WARNUNG')))

    def test_belanglose_belohnung_wird_nicht_gemeldet(self):
        # Blech ist hier nicht herstellbar, aber weder Maschine noch Aufgabe einer Quest: kein Stufensprung
        e = stufen.pruefe(b(A(belohnungen=[gib('blech')])), MODELL)
        self.assertFalse(any('Belohnung' in t for t in texte(e)))

    def test_belohnung_mit_komponenten_ist_kein_stufensprung(self):
        # Tagebuchseite = Papier mit Namen: eigene Sammel-Belohnung, kein gewöhnliches Papier
        from pruefung.modell import Belohnung as Bel
        seite = Bel(id='B000000000000001', typ='item', item='messing', komponenten={'minecraft:custom_name': 'Seite 1'})
        e = stufen.pruefe(b(A(belohnungen=[seite]), MESSING_Q), MODELL)
        self.assertFalse(any('Belohnung' in t for t in texte(e)))

    def test_kisteninhalt_zu_frueh_ist_hinweis(self):
        t = Tabelle(id='3000000000000001', titel='Kiste', eintraege=[('messing', 1, 1.0), ('log', 1, 1.0)])
        e = stufen.pruefe(b(A(belohnungen=[kiste('3000000000000001')]), MESSING_Q, tabellen=[t]), MODELL)
        h = texte(e, 'HINWEIS')
        self.assertTrue(any('messing' in x and 'Kiste' in x for x in h))
        self.assertFalse(any('log' in x for x in h))

    def test_monsterkiste_ab_spielstart(self):
        t = Tabelle(id='3000000000000001', titel='Monsterkiste', eintraege=[('messing', 1, 1.0)],
                    kiste={'drops': {'monster': 5, 'passive': 0, 'boss': 0}, 'string_id': 'm'})
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Mixer', deps=['1000000000000001'], aufgaben=[aufgabe('mixer')]),
                            MESSING_Q, tabellen=[t]), MODELL)
        self.assertTrue(any('Monsterkiste' in x and 'Spielstart' in x for x in texte(e, 'HINWEIS')))


class Gewicht(unittest.TestCase):
    def test_nebenkapitel_meldet_nur_hinweis(self):
        a = A()
        neben = quest('1000000000000003', 'Messing', deps=['1000000000000001'], aufgaben=[aufgabe('messing')])
        bk = b(a, neben)
        from pruefung.modell import Kapitel
        k2 = Kapitel(id='C000000000000002', datei='mods', titel='Mods', gruppe='6000000000000002', order_index=0)
        neben.kapitel = k2
        k2.quests.append(neben)
        bk.kapitel[0].quests.remove(neben)
        bk.kapitel.append(k2)
        bk.gruppen = {'6000000000000001': 'Hauptstory', '6000000000000002': 'Mods'}
        bk.gruppen_reihe = ['6000000000000001', '6000000000000002']
        e = stufen.pruefe(bk, MODELL)
        self.assertEqual(texte(e, 'WARNUNG'), [])
        self.assertEqual(len(texte(e, 'HINWEIS')), 1)


class Kennzahlen(unittest.TestCase):
    def test_erste_quest_mit_item(self):
        e = stufen.pruefe(b(A(), quest('1000000000000002', 'Mixer', deps=['1000000000000001'], aufgaben=[aufgabe('mixer')]),
                            quest('1000000000000003', 'Messing', deps=['1000000000000002'], aufgaben=[aufgabe('messing')])), MODELL)
        self.assertEqual(e.neue_stationen['1000000000000003'], set())
        self.assertEqual(e.neue_stationen['1000000000000002'], {'mixer'})


if __name__ == '__main__':
    unittest.main()

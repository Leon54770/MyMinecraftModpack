import unittest
import _pfad  # noqa: F401
from pruefung.huelle import Regel, huelle, fehlende_stationen


def r(id, ein, aus, haupt=None, neben=(), annahme=False):
    return Regel(id=id, typ='test', eingaben=[frozenset(g) for g in ein], ausgaben=frozenset(aus),
                 haupt=frozenset(haupt) if haupt else None, neben=[frozenset(g) for g in neben], annahme=annahme)


REGELN = [
    r('bretter', [{'log'}], {'brett'}),
    r('werkbank', [{'brett'}], {'werkbank'}),
    r('mixer', [{'brett'}, {'eisen'}], {'mixer'}, haupt={'werkbank'}),
    r('messing', [{'kupfer'}, {'zink'}], {'messing'}, haupt={'mixer'}, neben=[{'becken'}]),
    r('becken', [{'eisen'}], {'becken'}, haupt={'werkbank'}),
    r('eisen', [{'erz'}], {'eisen'}),
]


class Huelle(unittest.TestCase):
    def test_kette_ohne_einschraenkung(self):
        h = huelle(REGELN, {'log', 'erz', 'kupfer', 'zink'})
        self.assertIn('messing', h.da)

    def test_fehlende_eingabe_blockiert(self):
        h = huelle(REGELN, {'log', 'erz', 'kupfer'})
        self.assertNotIn('messing', h.da)

    def test_station_muss_erlaubt_sein(self):
        # Mixer ist herstellbar, aber noch nicht eingeführt -> Messing nicht erreichbar
        h = huelle(REGELN, {'log', 'erz', 'kupfer', 'zink'}, erlaubt={'werkbank'})
        self.assertIn('mixer', h.da)
        self.assertNotIn('messing', h.da)

    def test_nebenstation_muss_nur_herstellbar_sein(self):
        h = huelle(REGELN, {'log', 'erz', 'kupfer', 'zink'}, erlaubt={'werkbank', 'mixer'})
        self.assertIn('messing', h.da)

    def test_erlaubte_station_muss_auch_da_sein(self):
        # Erlaubt heißt nicht vorhanden: ohne Eisen kein Mixer, also kein Messing
        h = huelle(REGELN, {'log', 'kupfer', 'zink'}, erlaubt={'werkbank', 'mixer'})
        self.assertNotIn('messing', h.da)

    def test_variante_bringt_grund_item(self):
        h = huelle([r('wabe', [{'biene'}], {'pb:wabe{pb:eisen}'})], {'biene'})
        self.assertIn('pb:wabe', h.da)

    def test_regel_ohne_eingabe_feuert(self):
        self.assertIn('x', huelle([r('frei', [], {'x'})], set()).da)

    def test_leere_gruppe_feuert_nie(self):
        self.assertNotIn('x', huelle([r('kaputt', [set()], {'x'})], {'a'}).da)

    def test_annahmen_abschaltbar(self):
        regeln = [r('unsicher', [{'a'}], {'b'}, annahme=True)]
        self.assertIn('b', huelle(regeln, {'a'}).da)
        self.assertNotIn('b', huelle(regeln, {'a'}, annahmen=False).da)

    def test_herkunft(self):
        h = huelle(REGELN, {'log', 'erz', 'kupfer', 'zink'})
        self.assertEqual(h.woher['messing'].id, 'messing')
        self.assertNotIn('log', h.woher)            # Startressourcen haben keine Regel


class WarumNicht(unittest.TestCase):
    def test_findet_die_wurzel(self):
        # Messing fehlt, weil Zink fehlt (keine Quelle) – nicht wegen Kupfer, das da ist
        from pruefung.huelle import warum_nicht
        h = huelle(REGELN, {'log', 'erz', 'kupfer'})
        wurzeln = warum_nicht(REGELN, h, 'messing')
        self.assertEqual(wurzeln, {'zink'})

    def test_kreis_ohne_einstieg_ist_wurzel(self):
        # Netherit-Vorlage: einziges Rezept braucht sich selbst -> die Vorlage ist die Wurzel
        from pruefung.huelle import warum_nicht
        regeln = [r('vorlage', [{'vorlage'}, {'diamant'}], {'vorlage'}), r('netz', [{'vorlage'}], {'netz'})]
        h = huelle(regeln, {'diamant'})
        self.assertEqual(warum_nicht(regeln, h, 'netz'), {'vorlage'})

    def test_station_als_wurzel(self):
        from pruefung.huelle import warum_nicht
        regeln = [r('x', [{'a'}], {'x'}, haupt={'maschine'}), r('maschine', [{'b'}], {'maschine'})]
        h = huelle(regeln, {'a'})
        self.assertEqual(warum_nicht(regeln, h, 'x'), {'b'})


class FehlendeStationen(unittest.TestCase):
    def test_nennt_den_fehlenden_mixer(self):
        start = {'log', 'erz', 'kupfer', 'zink'}
        self.assertEqual(fehlende_stationen(REGELN, start, {'werkbank'}, 'messing'), {'mixer'})

    def test_nennt_kette_von_stationen(self):
        # Ohne Werkbank fehlen Werkbank und Mixer; die Werkbank ist selbst ohne Station herstellbar
        start = {'log', 'erz', 'kupfer', 'zink'}
        self.assertEqual(fehlende_stationen(REGELN, start, set(), 'messing'), {'werkbank', 'mixer'})

    def test_global_unerreichbar_gibt_none(self):
        self.assertIsNone(fehlende_stationen(REGELN, {'log'}, set(), 'messing'))

    def test_minimale_menge_ohne_ueberfluessige_station(self):
        # y geht mit s2 oder s1; x braucht s1. Die Heuristik kann {s1, s2} liefern, minimal ist {s1}
        from pruefung.huelle import minimale_stationen
        regeln = [r('y2', [{'a'}], {'y'}, haupt={'s2'}), r('y1', [{'a'}], {'y'}, haupt={'s1'}),
                  r('x', [{'y'}], {'x'}, haupt={'s1'}), r('s1', [{'a'}], {'s1'}), r('s2', [{'a'}], {'s2'})]
        self.assertEqual(minimale_stationen(regeln, {'a'}, set(), {'x'}), {'s1'})

    def test_alternative_station_wird_genannt(self):
        # Obsidianstaub: Zerkleinerer (Mekanism) oder Brechwalzen (Create) – beide liefern ein Mitglied des Tags
        from pruefung.huelle import minimale_stationen, alternativen
        regeln = [r('mek', [{'obsidian'}], {'mek_staub'}, haupt={'zerkleinerer'}),
                  r('create', [{'obsidian'}], {'create_staub'}, haupt={'brechwalzen'}),
                  r('raff', [{'mek_staub', 'create_staub'}], {'raff'}),
                  r('zerkleinerer', [{'obsidian'}], {'zerkleinerer'}), r('brechwalzen', [{'obsidian'}], {'brechwalzen'})]
        m = minimale_stationen(regeln, {'obsidian'}, set(), {'raff'})
        self.assertEqual(len(m), 1)
        s = next(iter(m))
        self.assertEqual(alternativen(regeln, {'obsidian'}, set(), {'raff'}, m), {s: {'zerkleinerer', 'brechwalzen'} - {s}})

    def test_waehlt_billigere_alternative(self):
        regeln = REGELN + [r('messing2', [{'kupfer'}, {'zink'}], {'messing'}, haupt={'ofen'}),
                           r('ofen', [{'erz'}], {'ofen'})]
        start = {'log', 'erz', 'kupfer', 'zink'}
        self.assertEqual(fehlende_stationen(regeln, start, set(), 'messing'), {'ofen'})


if __name__ == '__main__':
    unittest.main()

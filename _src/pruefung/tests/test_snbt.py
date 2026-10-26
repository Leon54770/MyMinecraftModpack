import unittest
import _pfad  # noqa: F401
import snbt


class SnbtLesen(unittest.TestCase):
    def test_typisierte_arrays(self):
        d = snbt.loads('{ a: [I; 1, 2, 3], b: [L; 5L, 6L], c: [B; 1b, 0b] }')
        self.assertEqual(d, {'a': [1, 2, 3], 'b': [5, 6], 'c': [1, 0]})

    def test_escapes_im_string(self):
        d = snbt.loads(r'{ t: "Er sagte \"Hallo\"\nund ging \\ weg" }')
        self.assertEqual(d['t'], 'Er sagte "Hallo"\nund ging \\ weg')

    def test_steuerzeichen_im_string_bleiben_erhalten(self):
        # Ein echter Tabulator im String darf den Text nicht unverändert mit Rohzeichen zurückgeben
        d = snbt.loads('{ t: "a\tb \\u00e4" }')
        self.assertEqual(d['t'], 'a\tb ä')

    def test_einfache_anfuehrungszeichen(self):
        d = snbt.loads("{ 'mod:key': 'it''s' }".replace("''", "\\'"))
        self.assertEqual(d, {'mod:key': "it's"})

    def test_zahlen(self):
        d = snbt.loads('{ a: 1.5e3d, b: -2, c: 0.5f, d: 7s, e: true, f: 1b }')
        self.assertEqual(d, {'a': 1500.0, 'b': -2, 'c': 0.5, 'd': 7, 'e': True, 'f': 1})

    def test_fehler_mit_zeile(self):
        with self.assertRaises(snbt.SnbtFehler) as cm:
            snbt.loads('{\n  a: 1\n  b 2\n}')
        self.assertIn('Zeile 3', str(cm.exception))

    def test_rest_nach_dem_ende_ist_fehler(self):
        with self.assertRaises(snbt.SnbtFehler):
            snbt.loads('{ a: 1 } }')

    def test_offener_string_ist_fehler(self):
        with self.assertRaises(snbt.SnbtFehler):
            snbt.loads('{ a: "offen }')


if __name__ == '__main__':
    unittest.main()

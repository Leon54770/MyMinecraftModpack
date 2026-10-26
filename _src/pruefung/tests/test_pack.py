import hashlib
import os
import time
import unittest
import hilfen as H
from pruefung import pack as P


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def texte(befunde, stufe=None):
    return [x.text for x in befunde if stufe is None or x.stufe == stufe]


class Ignorieren(unittest.TestCase):
    REGELN = P.ignore_regeln('README.md\n*.mrpack\n_src/\n/CLAUDE.md\n# Kommentar\ndocs/*.md\n!docs/keep.md\n')

    def test_muster(self):
        fall = {'README.md': True, 'config/README.md': True, 'x.mrpack': True, '_src/quests.py': True,
                'CLAUDE.md': True, 'config/CLAUDE.md': False, 'docs/a.md': True, 'docs/keep.md': False,
                'config/a.toml': False, 'docs/sub/a.md': False}
        for pfad, erwartet in fall.items():
            self.assertEqual(P.ignoriert(pfad, self.REGELN), erwartet, pfad)


class Index(unittest.TestCase):
    def bau(self, dateien, index_eintraege, ignore='', pack_hash=None):
        o = H.temp_ordner(self)
        for rel, text in dateien.items():
            H.schreibe(o, rel, text)
        idx = 'hash-format = "sha256"\n' + ''.join(f'\n[[files]]\nfile = "{f}"\nhash = "{h}"\n' for f, h in index_eintraege)
        H.schreibe(o, 'index.toml', idx)
        H.schreibe(o, 'pack.toml', f'name = "X"\n[index]\nfile = "index.toml"\nhash-format = "sha256"\nhash = "{pack_hash or sha(idx)}"\n')
        H.schreibe(o, '.packwizignore', ignore)
        return o

    def test_alles_stimmt(self):
        o = self.bau({'config/a.toml': 'a = 1\n'}, [('config/a.toml', sha('a = 1\n'))])
        self.assertEqual(P.pruefe_index(o), [])

    def test_geaenderte_datei(self):
        o = self.bau({'config/a.toml': 'a = 2\n'}, [('config/a.toml', sha('a = 1\n'))])
        self.assertTrue(any('config/a.toml' in t for t in texte(P.pruefe_index(o), 'FEHLER')))

    def test_fehlende_datei(self):
        o = self.bau({}, [('config/weg.toml', sha('x'))])
        self.assertTrue(texte(P.pruefe_index(o), 'FEHLER'))

    def test_neue_datei_nicht_im_index(self):
        o = self.bau({'config/a.toml': 'a = 1\n', 'config/neu.toml': 'b = 1\n'}, [('config/a.toml', sha('a = 1\n'))])
        self.assertTrue(any('config/neu.toml' in t for t in texte(P.pruefe_index(o), 'WARNUNG')))

    def test_ignorierte_datei_steht_im_index(self):
        o = self.bau({'NOTIZ.md': 'x'}, [('NOTIZ.md', sha('x'))], ignore='NOTIZ.md\n')
        self.assertTrue(any('NOTIZ.md' in t for t in texte(P.pruefe_index(o), 'WARNUNG')))

    def test_pack_toml_hash_falsch(self):
        o = self.bau({}, [], pack_hash='0' * 64)
        self.assertTrue(any('pack.toml' in t for t in texte(P.pruefe_index(o), 'FEHLER')))


class Mods(unittest.TestCase):
    MOD = 'name = "{n}"\nfilename = "{f}"\nside = "{s}"\n\n[download]\nurl = "https://x/{f}"\nhash-format = "sha1"\nhash = "ab"\n'

    def test_doppelter_dateiname_und_falsche_seite(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'mods/a.pw.toml', self.MOD.format(n='A', f='a.jar', s='both'))
        H.schreibe(o, 'mods/b.pw.toml', self.MOD.format(n='B', f='a.jar', s='irgendwo'))
        f = texte(P.pruefe_mods(o, None), 'FEHLER')
        self.assertEqual(len(f), 2)

    def test_testserver_ohne_jar_und_mit_fremdem_jar(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'mods/a.pw.toml', self.MOD.format(n='A', f='a.jar', s='both'))
        H.schreibe(o, 'mods/c.pw.toml', self.MOD.format(n='C', f='c.jar', s='client'))
        ts = H.temp_ordner(self)
        H.schreibe(ts, 'mods/alt.jar', 'x')
        b = P.pruefe_mods(o, ts)
        self.assertTrue(any('a.jar' in t for t in texte(b, 'WARNUNG')))
        self.assertTrue(any('alt.jar' in t for t in texte(b, 'HINWEIS')))
        self.assertFalse(any('c.jar' in t for t in texte(b)))

    def test_curseforge_ohne_url_ist_ok(self):
        o = H.temp_ordner(self)
        H.schreibe(o, 'mods/a.pw.toml', 'name = "A"\nfilename = "a.jar"\nside = "both"\n[download]\nhash-format = "sha1"\n'
                                        'hash = "ab"\nmode = "metadata:curseforge"\n[update.curseforge]\nfile-id = 1\nproject-id = 2\n')
        self.assertEqual(P.pruefe_mods(o, None), [])


class Dateien(unittest.TestCase):
    def test_bom_und_kaputte_dateien(self):
        o = H.temp_ordner(self)
        with open(os.path.join(o, 'x.toml'), 'w', encoding='utf-8-sig') as f:
            f.write('a = 1\n')
        os.makedirs(os.path.join(o, 'config'))
        os.replace(os.path.join(o, 'x.toml'), os.path.join(o, 'config', 'bom.toml'))
        H.schreibe(o, 'config/kaputt.toml', 'a = = 1\n')
        H.schreibe(o, 'kubejs/data/x/kaputt.json', '{ "a": }')
        H.schreibe(o, 'config/ok.json5', '// k\n{ "a": 1, }')
        f = texte(P.pruefe_dateien(o), 'FEHLER')
        self.assertEqual(len(f), 3)
        self.assertTrue(any('BOM' in t for t in f))


class DumpAlter(unittest.TestCase):
    def test_dump_aelter_als_skript(self):
        o, ts = H.temp_ordner(self), H.temp_ordner(self)
        d = H.schreibe(ts, 'kubejs/dev_recipejson.json', '{}')
        s = H.schreibe(o, 'kubejs/server_scripts/neu.js', '//')
        alt = time.time() - 3600
        os.utime(d, (alt, alt))
        self.assertTrue(texte(P.pruefe_dump_alter(o, ts, [d]), 'WARNUNG'))

    def test_inselvorlage_macht_dump_nicht_alt(self):
        # Inseln und Startinventar liest die Suite direkt aus dem Pack; sie ändern keine Rezepte
        o, ts = H.temp_ordner(self), H.temp_ordner(self)
        d = H.schreibe(ts, 'kubejs/dev_recipejson.json', '{}')
        H.schreibe(o, 'config/skyblockbuilder/templates.json5', '{}')
        alt = time.time() - 3600
        os.utime(d, (alt, alt))
        self.assertEqual(P.pruefe_dump_alter(o, ts, [d]), [])

    def test_items_kopie_veraltet(self):
        o = H.temp_ordner(self)
        H.schreibe(o, '_src/items.json', '{"items": ["a:x", "a:weg"]}')
        ts = H.temp_ordner(self)
        H.schreibe(ts, 'kubejs/dev_items.json', '{"items": ["a:x", "a:neu"]}')
        t = texte(P.pruefe_dump_alter(o, ts, []))
        self.assertTrue(any('a:weg' in x for x in t))


if __name__ == '__main__':
    unittest.main()

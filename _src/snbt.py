"""SNBT lesen (FTB-Quests-Dateien). Kein Schreiben, das macht ftbformat.py.

Kann: Compounds, Listen, typisierte Arrays ([I; …], [L; …], [B; …]), Strings in "…" und '…' mit Escapes,
Zahlen mit Suffix (b, s, L, f, d) und Exponent, true/false, unquotierte Wörter.
Fehler melden Zeile und Spalte (vorher: AssertionError oder IndexError ohne Ort).
"""
import re

_ZAHL_FLOAT = re.compile(r'[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?[dDfF]?')
_ZAHL_INT = re.compile(r'[-+]?\d+[bBsSlL]?')
_WORT = re.compile(r'[^\s,:\[\]{}"\']+')
_ESC = {'"': '"', "'": "'", '\\': '\\', '/': '/', 'n': '\n', 't': '\t', 'r': '\r', 'b': '\b', 'f': '\f'}


class SnbtFehler(ValueError):
    pass


class P:
    def __init__(self, s):
        self.s = s
        self.i = 0

    def fehler(self, was):
        zeile = self.s.count('\n', 0, self.i) + 1
        spalte = self.i - (self.s.rfind('\n', 0, self.i) + 1) + 1
        auszug = self.s[max(0, self.i - 25):self.i + 25].replace('\n', '⏎')
        return SnbtFehler(f'{was} (Zeile {zeile}, Spalte {spalte}: …{auszug}…)')

    def ws(self):
        s = self.s
        while self.i < len(s) and s[self.i] in ' \t\r\n,':
            self.i += 1

    def zeichen(self):
        if self.i >= len(self.s):
            raise self.fehler('unerwartetes Dateiende')
        return self.s[self.i]

    def val(self):
        self.ws()
        c = self.zeichen()
        if c == '{':
            return self.comp()
        if c == '[':
            return self.lst()
        if c in '"\'':
            return self.string()
        return self.atom()

    def string(self):
        s, q = self.s, self.s[self.i]
        j = self.i + 1
        out = []
        while True:
            if j >= len(s):
                self.i = j
                raise self.fehler('String ohne Ende')
            c = s[j]
            if c == '\\':
                n = s[j + 1:j + 2]
                if n == 'u' and re.fullmatch(r'[0-9a-fA-F]{4}', s[j + 2:j + 6]):
                    out.append(chr(int(s[j + 2:j + 6], 16)))
                    j += 6
                    continue
                if n in _ESC:
                    out.append(_ESC[n])
                    j += 2
                    continue
                self.i = j
                raise self.fehler(f'unbekannte Escape-Folge \\{n}')
            if c == q:
                break
            out.append(c)
            j += 1
        self.i = j + 1
        return ''.join(out)

    def key(self):
        self.ws()
        if self.zeichen() in '"\'':
            return self.string()
        m = re.compile(r'[A-Za-z0-9_.+\-]+').match(self.s, self.i)
        if not m:
            raise self.fehler('Schlüssel erwartet')
        self.i = m.end()
        return m.group(0)

    def comp(self):
        self.i += 1
        d = {}
        while True:
            self.ws()
            if self.zeichen() == '}':
                self.i += 1
                return d
            k = self.key()
            self.ws()
            if self.zeichen() != ':':
                raise self.fehler(f'„:“ nach Schlüssel {k} erwartet')
            self.i += 1
            if k in d:
                raise self.fehler(f'Schlüssel {k} doppelt')
            d[k] = self.val()

    def lst(self):
        self.i += 1
        m = re.compile(r'\s*([BIL])\s*;').match(self.s, self.i)
        if m:
            self.i = m.end()
        a = []
        while True:
            self.ws()
            if self.zeichen() == ']':
                self.i += 1
                return a
            a.append(self.val())

    def atom(self):
        m = _WORT.match(self.s, self.i)
        if not m:
            raise self.fehler('Wert erwartet')
        tok = m.group(0)
        self.i = m.end()
        if _ZAHL_INT.fullmatch(tok):
            return int(tok.rstrip('bBsSlL'))
        if _ZAHL_FLOAT.fullmatch(tok):
            return float(tok.rstrip('dDfF'))
        if tok == 'true':
            return True
        if tok == 'false':
            return False
        return tok


def loads(txt):
    p = P(txt)
    p.ws()
    if p.zeichen() != '{':
        raise p.fehler('Datei muss mit { beginnen')
    d = p.comp()
    p.ws()
    if p.i < len(txt):
        raise p.fehler('Text nach dem Ende des Compounds')
    return d


def load(path):
    with open(path, encoding='utf-8') as f:
        txt = f.read()
    try:
        return loads(txt)
    except SnbtFehler as e:
        raise SnbtFehler(f'{path}: {e}') from None

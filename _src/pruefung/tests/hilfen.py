"""Testhilfen: kleine Questbücher als Dateien oder direkt als Objekte bauen."""
import os
import tempfile
import _pfad  # noqa: F401
from pruefung.modell import Questbuch, Kapitel, Quest, Aufgabe, Belohnung, Tabelle


def schreibe(ordner, rel, text):
    pfad = os.path.join(ordner, *rel.split('/'))
    os.makedirs(os.path.dirname(pfad), exist_ok=True)
    with open(pfad, 'w', encoding='utf-8', newline='') as f:     # Zeilenenden unverändert (Hashes)
        f.write(text)
    return pfad


def temp_ordner(testfall):
    t = tempfile.TemporaryDirectory()
    testfall.addCleanup(t.cleanup)
    return t.name


def aufgabe(item=None, n=1, tag=None, typ='item', verbraucht=False, id=None, **extra):
    return Aufgabe(id=id or f'A{abs(hash((item, tag, n, typ))) % 10**12:015X}', typ=typ, item=item, tag=tag,
                   anzahl=n, verbraucht=verbraucht, komponenten=extra.pop('komponenten', None), roh=extra)


def gib(item, n=1, id=None):
    return Belohnung(id=id or f'B{abs(hash((item, n))) % 10**12:015X}', typ='item', item=item, anzahl=n)


def kiste(tabelle_id, art='loot', id=None):
    return Belohnung(id=id or f'D{abs(hash((tabelle_id, art))) % 10**12:015X}', typ=art, tabelle=tabelle_id)


def buch(quests, kapitel_gruppe='haupt', tabellen=(), gruppen=None):
    """quests: Liste von Quest-Objekten (kapitel wird gesetzt). Ein Kapitel 'k1'."""
    k = Kapitel(id='C000000000000001', datei='k1', titel='Kapitel 1', gruppe='6000000000000001', order_index=0)
    for q in quests:
        q.kapitel = k
        k.quests.append(q)
    b = Questbuch()
    b.gruppen = gruppen or {'6000000000000001': kapitel_gruppe}
    b.kapitel = [k]
    b.quests = {q.id: q for q in quests}
    b.tabellen = {t.id: t for t in tabellen}
    return b


def quest(id, titel=None, deps=(), aufgaben=(), belohnungen=(), **kw):
    return Quest(id=id, titel=titel or id, deps=list(deps), aufgaben=list(aufgaben), belohnungen=list(belohnungen), **kw)

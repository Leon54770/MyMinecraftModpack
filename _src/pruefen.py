# Sky and Stone: Prüfsuite – alle Prüfungen auf einmal (aus dem Pack-Ordner).
# Aufruf: python -I -X utf8 _src/pruefen.py [--schnell] [--referenz <Sicherung|.mrpack>] [--selbsttest]
#   --schnell     ohne Spiellogik (Rezeptmodell, ca. 1 min)
#   --referenz    Stand für den ID-Vergleich (Standard: neuestes „Sky and Stone-*.mrpack“)
#   --selbsttest  nur die Tests der Prüfsuite (_src/pruefung/tests)
# Bericht: _src/pruefung/bericht/PRUEFBERICHT.md. Exit 1 bei offenen FEHLERN.
import json
import os
import sys
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
PACK = os.path.dirname(HERE)
TESTSERVER = os.path.join(os.path.dirname(PACK), '_testserver-sky-and-stone')

from pruefung import (ausnahmen, belohnungslogik, daten, idvergleich, laden, modell, pack,  # noqa: E402
                      struktur, stufen, texte)
from pruefung.befund import Register  # noqa: E402


def selbsttest():
    tests = os.path.join(HERE, 'pruefung', 'tests')
    sys.path.insert(0, tests)
    r = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.discover(tests, top_level_dir=tests))
    return 0 if r.wasSuccessful() else 1


def main():
    args = sys.argv[1:]
    if '--selbsttest' in args:
        return selbsttest()
    ref = args[args.index('--referenz') + 1] if '--referenz' in args else idvergleich.neuestes_mrpack(PACK)
    t0 = time.time()
    buch = modell.lade(os.path.join(PACK, 'config', 'ftbquests'))
    p = laden.dump_pfade(PACK, TESTSERVER)
    extra = json.load(open(p['register'], encoding='utf-8')) if p['register'] else {}
    reg = Register(json.load(open(p['items'], encoding='utf-8'))['items'], json.load(open(p['tags'], encoding='utf-8')),
                   entities=extra.get('entities'), dimensionen=extra.get('dimensionen'), stapel=extra.get('stapel'),
                   fluide=extra.get('fluide'), bloecke=extra.get('bloecke'))
    befunde, kennzahlen = [], []

    def lauf(name, f):
        t = time.time()
        neu = f()
        befunde.extend(neu)
        print(f'{name}: {len(neu)} Befunde ({time.time() - t:.1f} s)')

    lauf('Questbuch', lambda: struktur.pruefe_ids(buch) + struktur.pruefe_graph(buch) + struktur.pruefe_aufgaben(buch, reg)
         + struktur.pruefe_belohnungen(buch, reg) + struktur.pruefe_verweise(buch) + struktur.pruefe_sprache(buch)
         + struktur.pruefe_kapitel(buch))
    if ref:
        lauf(f'Quest-IDs gegen {os.path.basename(ref)}', lambda: idvergleich.vergleiche(idvergleich.lade_referenz(ref), buch))
    lauf('Belohnungen', lambda: belohnungslogik.pruefe(buch, reg.tags))
    lauf('Texte, Sperrliste, Testserver', lambda: texte.pruefe_alles(buch, reg, PACK, TESTSERVER))
    kc = belohnungslogik.kistenchancen(buch)
    kennzahlen.append('Kistenchance je Kill: ' + ', '.join(f'{a} {w["gesamt"] * 100:.2f} %' for a, w in kc.items()))
    lauf('Paket', lambda: pack.pruefe_index(PACK) + pack.pruefe_mods(PACK, TESTSERVER) + pack.pruefe_dateien(PACK)
         + pack.pruefe_dump_alter(PACK, TESTSERVER, [p['rezept_json'], p['items'], p['tags']]))
    m = None
    if '--schnell' not in args:
        m = laden.lade_modell(PACK, TESTSERVER)
        m.namen = json.load(open(os.path.join(HERE, 'namen.json'), encoding='utf-8'))
        kennzahlen.append(f'Rezeptmodell: {m.info["regeln"]} Regeln ({m.info["weltregeln"]} Weltregeln), '
                          f'{m.info["loot_tabellen"]} Loot-Tabellen, Welt: Festungen={m.konfig.festungen}, '
                          f'End-Hauptinsel={m.konfig.end_hauptinsel}')
        lauf('Spiellogik', lambda: stufen.pruefe(buch, m).befunde)
    import glob
    jars = glob.glob(os.path.join(TESTSERVER, 'mods', '*.jar'))
    rez_ids = laden.jar_rezept_ids(jars) | ({r['id'] for r in json.load(open(p['rezept_json'], encoding='utf-8'))['recipes']}
                                           if p['rezept_json'] else set())
    lauf('Daten', lambda: daten.pruefe_funktionen(PACK, reg) + daten.pruefe_advancements(PACK, reg)
         + daten.pruefe_questbefehle(buch, PACK) + daten.pruefe_startinventar(PACK, reg) + daten.pruefe_skripte(PACK, reg, rez_ids)
         + daten.pruefe_essen(PACK, extra.get('essen')))

    offen, akzeptiert = ausnahmen.anwenden(befunde)
    veraltet = ausnahmen.unbenutzt(ausnahmen.LISTE, akzeptiert)
    zahl = {s: sum(b.stufe == s for b in offen) for s in ('FEHLER', 'WARNUNG', 'HINWEIS')}
    zeilen = [f'# Prüfbericht Sky and Stone', '',
              f'Stand: {time.strftime("%d.%m.%Y %H:%M")} · Dauer {time.time() - t0:.0f} s · '
              f'{zahl["FEHLER"]} Fehler, {zahl["WARNUNG"]} Warnungen, {zahl["HINWEIS"]} Hinweise, {len(akzeptiert)} akzeptiert', '',
              'Erzeugt von `_src/pruefen.py`. WARNUNG aus der Spiellogik beruht auf dem Rezeptmodell (Dumps vom Testserver): '
              'im Spiel gegenprüfen, bevor etwas geändert wird.', '']
    if kennzahlen:
        zeilen += ['## Kennzahlen', ''] + [f'- {k}' for k in kennzahlen] + ['']
    for s in ('FEHLER', 'WARNUNG', 'HINWEIS'):
        bs = [b for b in offen if b.stufe == s]
        if bs:
            zeilen += [f'## {s} ({len(bs)})', '']
            for bereich in sorted({b.bereich for b in bs}):
                zeilen += [f'### {bereich}', ''] + [f'- {b.text}' for b in bs if b.bereich == bereich] + ['']
    if akzeptiert:
        zeilen += ['## Akzeptiert (pruefung/ausnahmen.py)', ''] + [f'- {b.text} — {a.grund}' for b, a in akzeptiert] + ['']
    if veraltet:
        zeilen += ['## Veraltete Ausnahmen (treffen nichts mehr, löschen)', ''] + [f'- {a.muster}' for a in veraltet] + ['']
    ziel = os.path.join(HERE, 'pruefung', 'bericht', 'PRUEFBERICHT.md')
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    with open(ziel, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(zeilen))
    print(f'\n{zahl["FEHLER"]} Fehler, {zahl["WARNUNG"]} Warnungen, {zahl["HINWEIS"]} Hinweise, {len(akzeptiert)} akzeptiert')
    print(f'Bericht: {ziel}')
    return 1 if zahl['FEHLER'] else 0


if __name__ == '__main__':
    sys.exit(main())

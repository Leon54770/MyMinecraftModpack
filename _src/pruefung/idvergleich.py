"""Vergleicht die Objekt-IDs des Questbuchs mit einem Referenzstand (Sicherung oder exportiertes .mrpack).

Was eine ID-Änderung in einer bestehenden Welt bewirkt:
- Quest-ID weg: Fortschritt der Quest ist verloren, Folgequests können wieder gesperrt sein (FEHLER).
- Aufgaben-ID weg oder neu: Teilfortschritt weg bzw. eine fertige Quest bekommt eine offene Aufgabe (WARNUNG).
- Belohnungs-ID neu: FTB merkt sich abgeholte Belohnungen je ID, eine neue ID ist erneut abholbar (WARNUNG).
- Kisten-Kennung (string_id) geändert: Beutekisten in alten Inventaren zeigen ins Leere (WARNUNG).
"""
import glob
import os
import re
import shutil
import tempfile
import zipfile

from . import modell
from .befund import fehler, warnung, hinweis

B = 'Quest-IDs'


def _objekte(b):
    o = {}
    for k in b.kapitel:
        o[k.id] = ('Kapitel', k)
        for q in k.quests:
            o[q.id] = ('Quest', q)
            for t in q.aufgaben:
                o[t.id] = ('Aufgabe', q)
            for r in q.belohnungen:
                o[r.id] = ('Belohnung', q)
    for t in b.tabellen.values():
        o[t.id] = ('Tabelle', t)
    return o


def _aufgabe_sig(t):
    return (t.typ, t.item, t.tag, t.anzahl, t.verbraucht, t.roh.get('entity'), t.roh.get('dimension'))


def vergleiche(alt, neu):
    befunde = []
    oa, on = _objekte(alt), _objekte(neu)
    for i in sorted(set(oa) & set(on)):
        if oa[i][0] != on[i][0]:
            befunde.append(fehler(B, f'ID {i} war {oa[i][0]}, ist jetzt {on[i][0]}: alter Fortschritt landet beim falschen Objekt'))
    for qid, q in sorted(alt.quests.items()):
        if qid not in neu.quests:
            befunde.append(fehler(B, f'Quest {alt.name(q)} ({qid}) entfallen: Fortschritt in bestehenden Welten verloren'))
            continue
        nq = neu.quests[qid]
        ta, tn = {t.id: t for t in q.aufgaben}, {t.id: t for t in nq.aufgaben}
        for t in sorted(set(ta) - set(tn)):
            if on.get(t, ('', None))[0] != 'Aufgabe':
                befunde.append(warnung(B, f'{neu.name(nq)}: Aufgabe {t} ({ta[t].item or ta[t].tag or ta[t].typ}) entfallen, '
                                          'ihr Teilfortschritt ist weg'))
        for t in sorted(set(tn) - set(ta)):
            if oa.get(t, ('', None))[0] not in ('', 'Aufgabe'):
                continue                                    # Artwechsel ist oben schon FEHLER
            befunde.append(warnung(B, f'{neu.name(nq)}: neue Aufgabe {t} ({tn[t].item or tn[t].tag or tn[t].typ}) in bestehender '
                                      'Quest. In alten Welten bekommt eine fertige Quest eine offene Aufgabe (im Spiel prüfen)'))
        for t in sorted(set(ta) & set(tn)):
            if _aufgabe_sig(ta[t]) != _aufgabe_sig(tn[t]):
                befunde.append(hinweis(B, f'{neu.name(nq)}: Aufgabe {t} geändert {_aufgabe_sig(ta[t])[1:4]} → '
                                          f'{_aufgabe_sig(tn[t])[1:4]}, gespeicherter Fortschritt passt evtl. nicht mehr'))
        ra = {r.id for r in q.belohnungen}
        for r in sorted((r for r in nq.belohnungen if r.id not in ra), key=lambda r: r.id):
            if oa.get(r.id, ('', None))[0] not in ('', 'Belohnung'):
                continue
            if r.typ in ('command', 'xp', 'xp_levels', 'toast'):
                befunde.append(hinweis(B, f'{neu.name(nq)}: neue Belohnung {r.id} ({r.typ}) ist in alten Welten erneut abholbar'))
            else:
                befunde.append(warnung(B, f'{neu.name(nq)}: Belohnung {r.id} ({r.item or r.typ}) hat eine neue ID. '
                                          'Wer die Quest schon hatte, kann sie erneut abholen'))
    for kid, (art, k) in sorted(oa.items()):
        if art == 'Kapitel' and kid not in on:
            befunde.append(warnung(B, f'Kapitel {k.datei} ({kid}) entfallen'))
    for tid, t in sorted(alt.tabellen.items()):
        alt_sid = (t.kiste or {}).get('string_id')
        if tid not in neu.tabellen:
            befunde.append(warnung(B, f'Tabelle {t.datei or tid} entfallen' +
                                      (f': Kisten „{alt_sid}“ in alten Inventaren zeigen ins Leere' if alt_sid else '')))
            continue
        neu_sid = (neu.tabellen[tid].kiste or {}).get('string_id')
        if alt_sid and alt_sid != neu_sid:
            befunde.append(warnung(B, f'Tabelle {t.datei or tid}: Kisten-Kennung „{alt_sid}“ → „{neu_sid}“, '
                                      'alte Kisten lassen sich nicht mehr öffnen'))
    return befunde


# ---------------- Referenz laden ----------------
def _quests_ordner(wurzel, tiefe=6):
    """Sucht einen Ordner mit chapters/*.snbt. Bevorzugt …/quests/chapters (vollständiger Stand)."""
    funde = []
    for pfad, dirs, files in os.walk(wurzel):
        if pfad[len(wurzel):].count(os.sep) > tiefe:
            dirs[:] = []
            continue
        if os.path.basename(pfad) == 'chapters' and any(f.endswith('.snbt') for f in files):
            funde.append(os.path.dirname(pfad))
    if not funde:
        return None
    funde.sort(key=lambda p: (os.path.basename(p) != 'quests', len(p)))
    return funde[0]


def lade_referenz(pfad):
    if os.path.isfile(pfad):
        tmp = tempfile.mkdtemp(prefix='idcheck-')
        try:
            with zipfile.ZipFile(pfad) as z:
                for n in z.namelist():
                    m = re.search(r'(?:^|/)config/ftbquests/(quests/.+\.snbt)$', n)
                    if m:
                        ziel = os.path.join(tmp, *m.group(1).split('/'))
                        os.makedirs(os.path.dirname(ziel), exist_ok=True)
                        with open(ziel, 'wb') as f:
                            f.write(z.read(n))
            q = _quests_ordner(tmp)
            if q is None:
                raise FileNotFoundError(f'{pfad}: keine Questdateien (config/ftbquests/quests/chapters) im Archiv')
            return modell.lade_quests(q)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    q = _quests_ordner(pfad)
    if q is None:
        raise FileNotFoundError(f'{pfad}: kein Ordner chapters/ mit .snbt-Dateien gefunden')
    return modell.lade_quests(q)


def _version(name):
    m = re.search(r'-(\d+(?:\.\d+)*)\.mrpack$', name)
    return tuple(int(x) for x in m.group(1).split('.')) if m else ()


def neuestes_mrpack(ordner):
    kandidaten = glob.glob(os.path.join(ordner, 'Sky and Stone-*.mrpack'))
    return max(kandidaten, key=lambda p: _version(os.path.basename(p))) if kandidaten else None

"""Textprüfung (Farbcodes, Zahlen im Text gegen die Aufgabe, Regeln aus _src/TEXTSTIL.md), Sperrliste
(_src/sperren.py gegen Questindex und Register) und Testserver-Log (letzter Lauf von _src/testlauf.py).
Stand 26.10.2026. Aus den offenen Punkten der Prüfsuite (Vault: Modpack-Werkstatt)."""
import json
import os
import re
import sys

from .befund import fehler, hinweis, warnung

B_TEXT, B_SPERR, B_LOG = 'Texte', 'Sperrliste', 'Testserver'
HAUPTSTORY = {'akt1', 'akt2', 'akt3', 'akt4'}
FARBCODE = re.compile(r'&(.)')
GUELTIG = set('0123456789abcdefklmnor')
# TEXTSTIL.md, Abschnitt Ton: Floskeln, die nicht vorkommen sollen (Kleinschreibung, Teilstring)
FLOSKELN = ['perfekt!', 'geschafft!', 'ab jetzt ', 'das herz jeder', 'sondern auch', 'willkommen in der welt',
            '!!', 'magisch', 'landet direkt bei dir']
EMOJI = re.compile('[\U0001F300-\U0001FAFF☀-➿]')


def _beispiele(liste, n=5):
    return ', '.join(liste[:n]) + (f' (+{len(liste) - n})' if len(liste) > n else '')


def pruefe_farbcodes(b):
    befunde, offen = [], []
    for q in b.quests.values():
        for z in [q.titel, q.untertitel] + list(q.text):
            for m in FARBCODE.finditer(z or ''):
                if not m.group(1).isspace() and m.group(1).lower() not in GUELTIG:   # „Crafts & Additions“ ist kein Code
                    befunde.append(fehler(B_TEXT, f'„{q.titel}“ ({q.kapitel.datei}): ungültiger Farbcode „&{m.group(1)}“ in „{z[:60]}“'))
            # &e mitten in der Zeile ohne späteres &r färbt den Rest der Zeile
            for m in re.finditer(r'&e', z or ''):
                if m.start() > 0 and '&r' not in z[m.end():] and len(z) - m.end() > 30:
                    offen.append(f'„{q.titel}“')
        for z in q.text:
            if z.startswith('&o') and '„' not in z:
                befunde.append(warnung(B_TEXT, f'„{q.titel}“ ({q.kapitel.datei}): Zeile beginnt mit &o, ist aber keine Story-Notiz '
                                               f'(TEXTSTIL: &o nur für Notizen): „{z[:60]}“'))
    if offen:
        befunde.append(hinweis(B_TEXT, f'{len(offen)} Zeilen mit &e ohne schließendes &r (Rest der Zeile wird gelb): {_beispiele(sorted(set(offen)))}'))
    return befunde


def pruefe_zahlen(b, namen):
    """Nennt der Text eine Menge direkt vor dem Item-Namen der Aufgabe, muss eine davon zur Aufgabe passen
    (Fehlerart aus Spieltest/Prüfung 26.10.: Text 8 Stämme, Aufgabe 5; Text 4 Brocken, Rezept braucht 8)."""
    befunde = []
    for q in b.quests.values():
        text = ' '.join(q.text)
        for a in q.aufgaben:
            name = namen.get(a.item) if a.item else None
            if not name or len(name) < 4:
                continue
            # Mengen nach „=“ oder „→“ sind Rezept-Ergebnisse („4 Prudentium + 1 Messing = 2 Tertium“), keine Aufgabe
            zahlen = [int(m.group(1)) for m in re.finditer(r'(?<![=→]\s)(?<![=→])\b(\d+)\s*(?:×\s*)?(?:&[0-9a-fk-or])*' + re.escape(name), text) if not re.search(r'(ergeben|ergibt|macht|=|→)\s*$', text[:m.start()])]
            if zahlen and a.anzahl not in zahlen:
                befunde.append(warnung(B_TEXT, f'„{q.titel}“ ({q.kapitel.datei}): Text nennt {"/".join(map(str, zahlen))} × {name}, '
                                               f'die Aufgabe verlangt {a.anzahl}'))
    return befunde


def pruefe_stil(b):
    befunde, lang, titel_lang, titel_doppel = [], [], [], []
    for q in b.quests.values():
        kap = q.kapitel.datei if q.kapitel else '?'
        # Story-Notiz (Kopfzeile „&5&lNotiz“ + Zitat „&o„…“) zählt nicht zum Textstil-Limit
        zeilen = [z for z in q.text if not (z.startswith('&5&lNotiz') or (z.startswith('&o') and '„' in z))]
        while zeilen and not zeilen[0].strip(): zeilen.pop(0)
        if kap in HAUPTSTORY and len(zeilen) > 6:
            befunde.append(warnung(B_TEXT, f'„{q.titel}“ ({kap}): {len(zeilen)} Zeilen, TEXTSTIL erlaubt in der Hauptstory 6'))
        elif len(zeilen) > 9:
            lang.append(f'„{q.titel}“ ({len(zeilen)})')
        alles = ' '.join([q.titel] + zeilen)
        klein = alles.lower()
        for f in FLOSKELN:
            if f in klein:
                befunde.append(warnung(B_TEXT, f'„{q.titel}“ ({kap}): Floskel „{f.strip()}“ (TEXTSTIL, Ton)'))
        if EMOJI.search(alles):
            befunde.append(warnung(B_TEXT, f'„{q.titel}“ ({kap}): Emoji im Text (TEXTSTIL, Ton)'))
        if not q.wiederholbar:
            if len(q.titel.split()) > 4:
                titel_lang.append(f'„{q.titel}“')
            if ':' in q.titel:
                titel_doppel.append(f'„{q.titel}“')
    if lang:
        befunde.append(hinweis(B_TEXT, f'{len(lang)} Quests außerhalb der Hauptstory mit mehr als 9 Zeilen: {_beispiele(lang)}'))
    if titel_lang:
        befunde.append(hinweis(B_TEXT, f'{len(titel_lang)} Titel mit mehr als 4 Wörtern (TEXTSTIL, Titel): {_beispiele(titel_lang)}'))
    if titel_doppel:
        befunde.append(hinweis(B_TEXT, f'{len(titel_doppel)} Titel im Doppelpunkt-Stil (TEXTSTIL, Titel): {_beispiele(titel_doppel)}'))
    return befunde


def lade_questindex(src):
    p = os.path.join(src, 'questindex.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None


def pruefe_questindex(b, idx):
    if idx is None:
        return [warnung(B_SPERR, 'questindex.json fehlt: Generator laufen lassen (python -I -X utf8 _src/quests.py)')]
    befunde = []
    ids = {v['id'] for v in idx.values()}
    alt = sorted(k for k, v in idx.items() if v['id'] not in b.quests)
    if alt:
        befunde.append(fehler(B_SPERR, f'questindex.json passt nicht zu den Questdateien ({len(alt)} Schlüssel ohne Quest, z. B. '
                                       f'{_beispiele(alt)}): Generator neu laufen lassen'))
    fehlt = [q.titel for q in b.quests.values() if q.id not in ids]
    if fehlt:
        befunde.append(fehler(B_SPERR, f'{len(fehlt)} Quests fehlen im questindex.json, z. B. {_beispiele(fehlt)}'))
    return befunde


def pruefe_sperren(src, idx, reg):
    """sperren.py: Meilensteine (Werte) müssen Quests sein, Items (Schlüssel) müssen es im Spiel geben,
    jedes VERBOTEN-Muster muss mindestens ein Item treffen (sonst veraltet)."""
    if idx is None:
        return []
    sys.path.insert(0, src)
    import sperren
    befunde = []
    for item, ms in sorted(sperren.AB.items()):
        if ms not in idx:
            befunde.append(fehler(B_SPERR, f'AB[{item}] verweist auf Quest „{ms}“, die es nicht gibt: Sperre greift nie'))
        if reg is not None and item not in reg.items:
            befunde.append(warnung(B_SPERR, f'AB: Item {item} gibt es im Spiel nicht (Dump)'))
    for stufe, ms in sorted(sperren.KISTE_AB.items()):
        if ms not in idx:
            befunde.append(fehler(B_SPERR, f'KISTE_AB[{stufe}] verweist auf Quest „{ms}“, die es nicht gibt'))
    if reg is not None:
        for muster in sperren.VERBOTEN:
            if not any(re.search(muster, i) for i in reg.items):
                befunde.append(hinweis(B_SPERR, f'VERBOTEN-Muster {muster} trifft kein Item mehr (veraltet?)'))
    return befunde


def pruefe_testlog(pack, testserver):
    """Letzter Testserver-Lauf: neuer als alle Pack-Dateien und alle Pflichtpunkte grün (Auswertung aus _src/testlauf.py)."""
    log = os.path.join(testserver, 'logs', 'latest.log')
    if not os.path.exists(log):
        return [warnung(B_LOG, 'Kein Testserver-Log: python -I -X utf8 _src/testlauf.py')]
    neuest, datei = 0, ''
    for teil in ('config', 'kubejs', 'mods'):
        for wurzel, _, dateien in os.walk(os.path.join(pack, teil)):
            for d in dateien:
                t = os.path.getmtime(os.path.join(wurzel, d))
                if t > neuest:
                    neuest, datei = t, os.path.relpath(os.path.join(wurzel, d), pack)
    befunde = []
    if os.path.getmtime(log) < neuest:
        befunde.append(warnung(B_LOG, f'Testserver-Log ist älter als {datei}: python -I -X utf8 _src/testlauf.py'))
    sys.path.insert(0, os.path.join(pack, '_src'))
    import testlauf
    try:
        punkte, neu, _ = testlauf.werte_aus(testlauf.lese_quests_soll())
    except OSError as e:
        return befunde + [warnung(B_LOG, f'Log nicht lesbar: {e}')]
    for name, ok, det in punkte:
        if not ok:
            befunde.append(fehler(B_LOG, f'{name}: {det}'))
    for z, _ in neu[:5]:
        befunde.append(fehler(B_LOG, f'ERROR im Log: {z[:200]}'))
    return befunde


def pruefe_alles(b, reg, pack, testserver):
    src = os.path.join(pack, '_src')
    namen = json.load(open(os.path.join(src, 'namen.json'), encoding='utf-8'))
    idx = lade_questindex(src)
    return (pruefe_farbcodes(b) + pruefe_zahlen(b, namen) + pruefe_stil(b) + pruefe_questindex(b, idx)
            + pruefe_sperren(src, idx, reg) + pruefe_testlog(pack, testserver))

"""Belohnungen im Zusammenspiel: erledigt eine Belohnung eine andere Quest, lohnt sich ein Tausch endlos,
wie oft fallen Kisten von Mobs (Kennzahl für den Bericht)."""
from collections import defaultdict

from .befund import fehler, warnung, hinweis

B = 'Belohnungen'
TABELLEN = ('loot', 'choice', 'random', 'all_table')


def _gewicht(b, q):
    from .stufen import gewicht
    return gewicht(b, q)


def erwartung(t, art):
    """Erwartete Menge je Item für eine Belohnung aus Tabelle t. loot/random: loot_size Ziehungen nach Gewicht,
    choice: der Spieler nimmt das Beste (je Item die größte Menge), all_table: alles."""
    out = defaultdict(float)
    eintraege = [(i, n, w) for i, n, w in t.eintraege if w > 0]
    if not eintraege:
        return out
    if art == 'choice':
        for i, n, _ in eintraege:
            out[i] = max(out[i], n)
    elif art == 'all_table':
        for i, n, _ in eintraege:
            out[i] += n
    else:
        summe = sum(w for _, _, w in eintraege)
        for i, n, w in eintraege:
            out[i] += max(1, t.loot_size) * n * w / summe
    return out


def pruefe(b, tags):
    befunde = []
    # 1. Die festen Belohnungen einer Quest erfüllen alle Aufgaben einer anderen, nicht vorausgesetzten Quest
    for q in b.quests.values():
        gaben = [r for r in q.belohnungen if r.typ == 'item' and r.item and not r.komponenten]
        if not gaben:
            continue
        ahnen = b.ahnen(q.id)
        for p in b.quests.values():
            if p.id == q.id or p.id in ahnen or p.wiederholbar or not p.aufgaben:
                continue
            if any(t.typ != 'item' or t.komponenten for t in p.aufgaben):
                continue
            treffer = [(t, next((r for r in gaben if r.item in t.items(tags) and r.anzahl >= t.anzahl), None)) for t in p.aufgaben]
            if all(r for _, r in treffer):
                was = ', '.join(f'{r.anzahl}× {r.item}' for _, r in treffer)
                befunde.append(_gewicht(b, p)(B, f'Belohnung aus {b.name(q)} ({was}) erfüllt sofort alle Aufgaben von {b.name(p)}'))
    # 1b. Kisten mit denselben Kistendaten (Farbe, Leuchten, Drops) wie eine andere: meist beim Kopieren übernommen
    gleich = defaultdict(list)
    for t in b.tabellen.values():
        if t.kiste:
            d = t.kiste.get('drops') or {}
            gleich[(t.kiste.get('color'), bool(t.kiste.get('glow')), int(d.get('monster', 0)), int(d.get('passive', 0)),
                    int(d.get('boss', 0)))].append(t.titel or t.datei)
    for (farbe, _, mo, pa, bo), namen in gleich.items():
        if len(namen) > 1 and (mo or pa or bo):
            befunde.append(hinweis(B, f'{", ".join(sorted(namen))} haben dieselben Kistendaten (Farbe {farbe}, Drops Monster {mo}/'
                                      f'Tier {pa}/Boss {bo}): kopiert? Alle fallen dann gleich oft von Mobs'))
    # 2. Markt: Tausche (wiederholbar, verbrauchen ein Item, geben Kisten)
    kanten = defaultdict(dict)        # X -> {Y: Faktor}
    woher = {}
    for q in b.quests.values():
        if not q.wiederholbar:
            continue
        ein = [t for t in q.aufgaben if t.typ == 'item' and t.verbraucht and t.item]
        if len(ein) != 1:
            continue
        x, n = ein[0].item, ein[0].anzahl
        aus = defaultdict(float)
        for r in q.belohnungen:
            if r.typ in TABELLEN and r.tabelle in b.tabellen:
                for i, m in erwartung(b.tabellen[r.tabelle], r.typ).items():
                    aus[i] += m
            elif r.typ == 'item' and r.item:
                aus[r.item] += r.anzahl
        if aus.get(x, 0) >= n:
            befunde.append(fehler(B, f'{b.name(q)} gibt im Schnitt {aus[x]:.1f}× {x} zurück und verbraucht nur {n}: '
                                     'endlose Vermehrung (nur durch die Abklingzeit gebremst)'))
        for y, m in aus.items():
            if y != x and m > 0:
                kanten[x][y] = max(kanten[x].get(y, 0), m / n)
                woher[(x, y)] = q
    befunde += _kreise(b, kanten, woher)
    return befunde


def _kreise(b, kanten, woher, laenge=4):
    gefunden, out = set(), []

    def dfs(start, knoten, pfad, faktor):
        for y, f in kanten.get(knoten, {}).items():
            if y == start and faktor * f > 1 and len(pfad) > 1:
                schluessel = frozenset(pfad)
                if schluessel not in gefunden:
                    gefunden.add(schluessel)
                    tausche = [b.name(woher[(pfad[i], pfad[(i + 1) % len(pfad)])]) for i in range(len(pfad))]
                    out.append(warnung(B, f'Tausch-Kreis mit Gewinn (Faktor {faktor * f:.2f} je Runde): '
                                          + ' → '.join(pfad + [start]) + ' über ' + ', '.join(tausche)))
            elif y not in pfad and len(pfad) < laenge:
                dfs(start, y, pfad + [y], faktor * f)

    for x in sorted(kanten):
        dfs(x, x, [x], 1.0)
    return out


def kistenchancen(b):
    """Chance je Kill, dass eine Kiste fällt (FTB: Gewicht der Kiste / (Summe aller Kisten + Gewicht „keine Kiste“))."""
    keine = (b.daten or {}).get('loot_crate_no_drop') or {}
    out = {}
    for art in ('monster', 'passive', 'boss'):
        gew = {(t.titel or t.datei): int(((t.kiste or {}).get('drops') or {}).get(art, 0)) for t in b.tabellen.values() if t.kiste}
        summe = sum(gew.values()) + int(keine.get(art, 0))
        werte = {k: (v / summe if summe else 0.0) for k, v in gew.items() if v > 0}
        werte['gesamt'] = sum(werte.values())
        out[art] = werte
    return out

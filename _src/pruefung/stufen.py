"""Spiellogik je Quest: Ist das, was eine Quest verlangt, zu diesem Zeitpunkt herstellbar?

„Zu diesem Zeitpunkt“ heißt: Der Spieler hat den Start (Inventar, Insel), alles, was die Voraussetzungen
verlangt oder fest belohnt haben, und er kennt nur die Maschinen, die das Buch bis dahin eingeführt hat
(Aufgaben und Belohnungen der Voraussetzungen, dazu Vanilla-Grundstationen wie Werkbank und Ofen).
Fehlt eine Maschine, nennt der Befund sie und die Quest, die sie einführt – meist fehlt dort eine Abhängigkeit.

Dazu: Belohnungen, die etwas geben, das an dieser Stelle noch nicht herstellbar wäre (Stufe übersprungen),
Monsterkisten mit Inhalt, der erst später herstellbar ist, und Quest-Items ohne jeden Weg im Modell.
"""
from collections import defaultdict
from dataclasses import dataclass, field

from dataclasses import replace

from .befund import warnung, hinweis
from .huelle import huelle, minimale_stationen, alternativen, warum_nicht, annahmen_auf_dem_weg
from .rezepte import varianten
from .struktur import freischaltbar, startquest

B = 'Spiellogik'
# Vanilla-Stationen und Handwerkzeuge kennt jeder Spieler (JEI zeigt sie); alles andere muss das Buch einführen
GRUNDSTATIONEN = {'minecraft:crafting_table', 'minecraft:furnace', 'minecraft:campfire', 'minecraft:soul_campfire',
                  'minecraft:smoker', 'minecraft:blast_furnace', 'minecraft:stonecutter', 'minecraft:smithing_table',
                  'minecraft:composter', 'create:sand_paper', 'create:red_sand_paper'}
TABELLEN = ('loot', 'choice', 'random', 'all_table')


@dataclass
class Ergebnis:
    befunde: list = field(default_factory=list)
    neue_stationen: dict = field(default_factory=dict)     # Quest-ID -> Hauptstationen, die diese Quest neu einführt
    erreichbar: dict = field(default_factory=dict)         # Quest-ID -> Menge erreichbarer Ressourcen nach der Quest
    erstmals: dict = field(default_factory=dict)           # Ressource -> erste Quest (wenigste Voraussetzungen), ab der sie da ist


def _reihenfolge(b):
    frei = freischaltbar(b)
    fertig, out = set(), []
    offen = [q for q in b.quests if q in frei]
    while offen:
        rest = []
        for q in offen:
            if all(d in fertig or d not in frei for d in b.quests[q].deps):
                out.append(q)
                fertig.add(q)
            else:
                rest.append(q)
        if len(rest) == len(offen):
            break
        offen = rest
    return out


def _aufgaben_items(t, tags):
    its = t.items(tags)
    return set(varianten(frozenset(its), t.komponenten)) if t.komponenten else its


def _namen(modell):
    return getattr(modell, 'namen', None) or {}


def _n(namen, i):
    return f'{namen[i]} ({i})' if i in namen else i


def hauptgruppe(b):
    """Kapitelgruppe der Hauptstory: erste Gruppe im Buch, sonst die Gruppe der Startquest."""
    if b.gruppen_reihe:
        return b.gruppen_reihe[0]
    s = startquest(b)
    return b.quests[s].kapitel.gruppe if s and b.quests[s].kapitel else None


def gewicht(b, q):
    """WARNUNG nur auf dem Pfad (Hauptstory, nicht optional, nicht wiederholbar), sonst HINWEIS."""
    pfad = q.kapitel is not None and q.kapitel.gruppe == hauptgruppe(b) and not q.optional and not q.wiederholbar
    return warnung if pfad else hinweis


def einzelne_annahmen(regeln, start, G):
    """Je Annahme-Regel die Hülle, wenn nur sie zugelassen ist. Nur Regeln, die überhaupt feuern können."""
    sicher = [r for r in regeln if not r.annahme]
    out = []
    for r in regeln:
        if r.annahme and all(g & G.da for g in r.gruppen()):
            out.append((r, huelle(sicher + [replace(r, annahme=False)], start).da))
    return out


def noetige_annahmen(einzeln, ziele):
    """Annahme-Regeln, von denen jede allein (ohne die übrigen Annahmen) ein Ziel erreichbar macht."""
    return [r for r, da in einzeln if set(ziele) & da]


def pruefe(b, modell, grund=GRUNDSTATIONEN):
    e = Ergebnis()
    tags = modell.register.tags
    regeln, start = modell.regeln, set(modell.start)
    namen = _namen(modell)
    stationen_alle = set().union(*(r.haupt for r in regeln if r.haupt)) if regeln else set()
    G = huelle(regeln, start)
    Ga = huelle(regeln, start, annahmen=False)

    # Wer führt welche Station ein (Aufgaben, auch über Gruppen); welche Items verlangt welche Quest
    fuehrt_ein, verlangt = defaultdict(set), defaultdict(set)
    for q, t in b.alle_aufgaben():
        if t.typ == 'item':
            for i in _aufgaben_items(t, tags) | t.items(tags):
                verlangt[i].add(q.id)
                if i in stationen_alle:
                    fuehrt_ein[i].add(q.id)

    def relevant(i, q):
        """Belohnung zählt als Stufensprung nur bei Maschinen oder Items, die eine andere (spätere) Quest verlangt."""
        return i in stationen_alle or bool(verlangt.get(i, set()) - b.ahnen(q.id) - {q.id})

    erlaubt_von, global_fehlt, nur_annahme = {}, defaultdict(list), defaultdict(list)
    for qid in _reihenfolge(b):
        q = b.quests[qid]
        ahnen = b.ahnen(qid)
        basis, erl = set(start), {s for s in grund}
        for a in ahnen:
            for t in b.quests[a].aufgaben:
                if t.typ != 'item':
                    continue
                if t.item:
                    basis |= _aufgaben_items(t, tags)
                erl |= t.items(tags)
            for r in b.quests[a].belohnungen:
                if r.typ == 'item' and r.item:
                    basis.add(r.item)
                    erl.add(r.item)
        eltern_erl = set(erl)
        eigene = set()
        for t in q.aufgaben:
            if t.typ == 'item':
                eigene |= _aufgaben_items(t, tags) | t.items(tags)
        C = huelle(regeln, basis, erl)
        while True:
            neu = {x for x in eigene if x in C.da} - erl
            if not neu:
                break
            erl |= neu
            C = huelle(regeln, basis, erl)
        erlaubt_von[qid] = erl
        e.erreichbar[qid] = C.da
        e.neue_stationen[qid] = (erl - eltern_erl) & stationen_alle
        for t in q.aufgaben:
            if t.typ != 'item':
                continue
            its = _aufgaben_items(t, tags)
            if not its:
                continue
            if not its & G.da:
                global_fehlt[tuple(sorted(its))].append(qid)
                continue
            if not its & Ga.da:
                nur_annahme[tuple(sorted(its))].append(qid)
            if its & C.da:
                continue
            fehlt = minimale_stationen(regeln, basis, erl, its)
            alt = alternativen(regeln, basis, erl, its, fehlt) if fehlt else {}
            e.befunde.append(_vorgriff(b, q, its, fehlt, fuehrt_ein, namen, alt))
        for r in q.belohnungen:
            if r.komponenten:
                continue        # eigenes Sammel-Item (Tagebuchseite, Buch), kein gewöhnliches Material
            if r.typ == 'item' and r.item and r.item not in C.da and r.item in G.da and relevant(r.item, q):
                was = 'eine Maschine' if r.item in stationen_alle else 'ein Quest-Item'
                e.befunde.append(gewicht(b, q)(
                    B, f'{b.name(q)}: Belohnung {_n(namen, r.item)} ist {was}, das hier noch nicht herstellbar wäre (überspringt eine Stufe)'))
            elif r.typ in TABELLEN and r.tabelle in b.tabellen:
                t = b.tabellen[r.tabelle]
                frueh = sorted({i for i, _, w in t.eintraege if w > 0 and i not in C.da and i in G.da and relevant(i, q)})
                if frueh:
                    e.befunde.append(hinweis(B, f'{b.name(q)}: „{t.titel or t.datei}“ kann {", ".join(_n(namen, i) for i in frueh)} '
                                                'geben, das hier noch nicht herstellbar wäre'))

    # Erstes Auftreten je Ressource (Quest mit den wenigsten Voraussetzungen)
    for qid in sorted(e.erreichbar, key=lambda x: len(b.ahnen(x))):
        for res in e.erreichbar[qid]:
            e.erstmals.setdefault(res, qid)

    s = startquest(b)
    if s in e.erreichbar:
        for t in b.tabellen.values():
            drops = (t.kiste or {}).get('drops') or {}
            if not (int(drops.get('monster', 0)) > 0 or int(drops.get('passive', 0)) > 0):
                continue
            frueh = sorted({i for i, _, w in t.eintraege if w > 0 and i not in e.erreichbar[s] and i in G.da
                            and (i in stationen_alle or i in verlangt)})
            if frueh:
                ab = [f'{_n(namen, i)} (sonst ab {b.name(e.erstmals[i])})' if i in e.erstmals else _n(namen, i) for i in frueh]
                e.befunde.append(hinweis(B, f'„{t.titel or t.datei}“ fällt ab Spielstart von Monstern/Tieren und kann geben: '
                                            + ', '.join(ab)))

    for its, qs in sorted(global_fehlt.items()):
        wurzeln = set()
        for i in its[:3]:
            wurzeln |= warum_nicht(regeln, G, i)
        stufe = warnung if any(gewicht(b, b.quests[q]) is warnung for q in qs) else hinweis
        if not any(b.quests[q].optional for q in qs):
            stufe = warnung          # nicht lösbare Pflicht-Quest wiegt auch im Nebenkapitel schwer
        e.befunde.append(stufe(B, f'{", ".join(_n(namen, i) for i in its[:3])} ist im Modell nirgends herstellbar '
                                  f'(gebraucht in {", ".join(b.name(q) for q in qs)}). Fehlende Quelle: '
                                  + ', '.join(_n(namen, w) for w in sorted(wurzeln)[:6])))
    einzeln = einzelne_annahmen(regeln, start, G) if nur_annahme else []
    for its, qs in sorted(nur_annahme.items()):
        regs = noetige_annahmen(einzeln, set(its))
        if not regs:
            for i in its[:3]:
                if i in G.da:
                    regs += [r for r in annahmen_auf_dem_weg(G, i) if r not in regs]
            art = 'mehrere Annahmen zusammen, z. B.'
        else:
            art = 'eine davon reicht'
        warum = '; '.join(sorted({r.notiz or r.id for r in regs})[:4]) or 'Annahme-Regel'
        e.befunde.append(hinweis(B, f'{", ".join(_n(namen, i) for i in its[:3])} nur über Annahmen erreichbar '
                                    f'({", ".join(b.name(q) for q in qs)}), {art}: {warum}'))
    return e


def _vorgriff(b, q, its, fehlt, fuehrt_ein, namen, alt=None):
    item = _n(namen, sorted(its)[0]) + (f' (oder eins von {len(its)})' if len(its) > 1 else '')
    stufe = gewicht(b, q)
    if not fehlt:
        return stufe(B, f'{b.name(q)}: {item} ist hier noch nicht herstellbar (Grund im Modell nicht bestimmbar)')
    alt = alt or {}
    teile = []
    for s in sorted(fehlt):
        ersatz = ' oder ' + ' oder '.join(_n(namen, x) for x in sorted(alt[s])) if s in alt else ''
        quellen = sorted(set().union(*(fuehrt_ein.get(x, set()) for x in {s} | alt.get(s, set()))) - {q.id})
        if not quellen:
            teile.append(f'{_n(namen, s)}{ersatz} (keine Quest führt sie ein)')
            continue
        nach = [x for x in quellen if q.id in b.ahnen(x)]
        wo = ', '.join(b.name(x) for x in quellen[:3])
        art = 'kommt erst danach' if nach and len(nach) == len(quellen) else 'keine Voraussetzung dieser Quest'
        teile.append(f'{_n(namen, s)}{ersatz} (eingeführt in {wo}, {art})')
    return stufe(B, f'{b.name(q)}: {item} ist hier noch nicht herstellbar, es fehlt: ' + '; '.join(teile))

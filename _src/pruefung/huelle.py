"""Erreichbarkeit als UND-ODER-Graph: Eine Regel feuert, wenn jede ihrer Gruppen mindestens ein vorhandenes
Element hat. Gruppen sind Zutaten (verbraucht), Nebenstationen (nur vorhanden) und die Hauptstation.

Die Hauptstation ist die Maschine, die ein Spieler kennen muss (Mixer, Sieb, Anreicherungskammer). Mit
`erlaubt` lässt sich festlegen, welche Hauptstationen bis zu einer Quest eingeführt sind; Nebenteile
(Becken zum Mixer, Sockel zum Altar) müssen dagegen nur herstellbar sein.

Ressourcen sind Strings: Items 'mod:id', Varianten 'mod:id{typ}' (bringen immer auch 'mod:id'),
Fluide 'fluid:…', Chemikalien 'chem:…', Mobs 'mob:…', Bienen 'biene:…', Kräfte 'kraft:…', Orte 'ort:…'.
"""
from collections import deque, defaultdict
from dataclasses import dataclass, field


@dataclass
class Regel:
    id: str
    typ: str
    eingaben: list                      # [frozenset] – jede Gruppe: Alternativen
    ausgaben: frozenset
    haupt: frozenset = None             # Alternativen der Hauptstation (None = keine)
    neben: list = field(default_factory=list)
    annahme: bool = False               # unsichere Weltregel (Biom, Spawn) – abschaltbar
    notiz: str = ''

    def gruppen(self, erlaubt=None):
        g = list(self.eingaben) + list(self.neben)
        if self.haupt is not None:
            h = self.haupt if erlaubt is None else self.haupt & erlaubt
            if not h:
                return None
            g.append(h)
        return g


def grund(res):
    i = res.find('{')
    return res[:i] if i > 0 else None


@dataclass
class Huelle:
    da: set
    woher: dict                         # Ressource -> erste Regel, die sie geliefert hat
    tiefe: dict                         # Ressource -> Anzahl Regeln bis dahin (ungefähr kürzester Weg)


def huelle(regeln, start, erlaubt=None, annahmen=True):
    da = set()
    woher, tiefe = {}, {}
    rest, erfuellt, gtiefe = [], [], []
    index = defaultdict(list)
    q = deque()

    def neu(res, t, regel=None):
        if res in da:
            return
        da.add(res)
        tiefe[res] = t
        if regel is not None:
            woher[res] = regel
        q.append(res)
        g = grund(res)
        if g:
            neu(g, t, regel)

    sofort = []
    for ri, r in enumerate(regeln):
        gs = None if (r.annahme and not annahmen) else r.gruppen(erlaubt)
        if gs is None:
            rest.append(-1); erfuellt.append(None); gtiefe.append(None)
            continue
        rest.append(len(gs)); erfuellt.append([False] * len(gs)); gtiefe.append([0] * len(gs))
        for gi, g in enumerate(gs):
            for res in g:
                index[res].append((ri, gi))
        if not gs:
            sofort.append(ri)
    for s in start:
        neu(s, 0)
    for ri in sofort:
        for o in regeln[ri].ausgaben:
            neu(o, 1, regeln[ri])
    while q:
        res = q.popleft()
        t = tiefe[res]
        for ri, gi in index.get(res, ()):
            e = erfuellt[ri]
            if e is None or e[gi]:
                continue
            e[gi] = True
            gtiefe[ri][gi] = t
            rest[ri] -= 1
            if rest[ri] == 0:
                tr = max(gtiefe[ri]) + 1
                for o in regeln[ri].ausgaben:
                    neu(o, tr, regeln[ri])
    return Huelle(da, woher, tiefe)


def warum_nicht(regeln, h, ziel, tiefe=12):
    """Wurzeln einer Unerreichbarkeit: Ressourcen ohne erreichbare Quelle, die auf jedem Weg zu `ziel` fehlen.
    Folgt je Regel der ersten fehlenden Gruppe und darin dem ersten Element; Ergebnis: Menge der Wurzeln."""
    erzeuger = defaultdict(list)
    for r in regeln:
        for o in r.ausgaben:
            erzeuger[o].append(r)
    wurzeln, gesehen = set(), set()

    def suche(res, t):
        """True, wenn unterhalb von res eine Wurzel gefunden (oder res selbst eine ist)."""
        if res in h.da:
            return False
        if res in gesehen:
            return res in wurzeln
        gesehen.add(res)
        rs = erzeuger.get(res, [])
        if not rs or t >= tiefe:
            wurzeln.add(res)
            return True
        gefunden = False
        for r in rs:
            for g in r.gruppen():
                if not (g & h.da):
                    gefunden |= suche(sorted(g)[0], t + 1)
                    break
        if not gefunden:
            wurzeln.add(res)           # alle Wege führen im Kreis zurück (z. B. Vorlage braucht sich selbst)
        return True

    suche(ziel, 0)
    return wurzeln


def minimale_stationen(regeln, start, erlaubt, ziele, annahmen=True):
    """Kleinste Menge zusätzlicher Hauptstationen (nicht weiter verkleinerbar), mit der eines der Ziele erreichbar wird.
    Startet bei der Heuristik aus stationslabels und streicht jede Station, ohne die es auch geht (echte Hülle je Test).
    None, wenn kein Ziel erreichbar ist."""
    label = stationslabels(regeln, start, erlaubt, annahmen)
    kand = [label[z] for z in ziele if z in label]
    if not kand:
        return None
    menge = set(min(kand, key=len))
    basis = set(erlaubt)
    for s in sorted(menge):
        rest = menge - {s}
        if set(ziele) & huelle(regeln, start, basis | rest, annahmen).da:
            menge = rest
    return menge


def fehlende_stationen(regeln, start, erlaubt, ziel, annahmen=True, runden=60):
    """Kleinste gefundene Menge nicht erlaubter Hauptstationen, mit der `ziel` erreichbar wird.
    Heuristik (Bellman-Ford über Mengen, kürzeste Menge gewinnt): zeigt, welche Maschine fehlt.
    None, wenn `ziel` auch mit allen Stationen nicht erreichbar ist."""
    if ziel not in huelle(regeln, start, annahmen=annahmen).da:
        return None
    label = stationslabels(regeln, start, erlaubt, annahmen, runden)
    return set(label[ziel]) if ziel in label else None


def stationslabels(regeln, start, erlaubt, annahmen=True, runden=60):
    """Für jede erreichbare Ressource: kleinste gefundene Menge nicht erlaubter Hauptstationen auf dem Weg dorthin."""
    erlaubt = set(erlaubt)
    label = {s: frozenset() for s in start}
    for s in list(start):
        g = grund(s)
        if g:
            label.setdefault(g, frozenset())
    aktiv = [r for r in regeln if annahmen or not r.annahme]
    for _ in range(runden):
        besser = False
        for r in aktiv:
            teile = []
            ok = True
            for g in list(r.eingaben) + list(r.neben):
                kand = [label[m] for m in g if m in label]
                if not kand:
                    ok = False
                    break
                teile.append(min(kand, key=len))
            if not ok:
                continue
            if r.haupt is not None:
                opt = []
                for s in r.haupt:
                    if s in label:
                        opt.append(label[s] if s in erlaubt else label[s] | {s})
                if not opt:
                    continue
                teile.append(min(opt, key=len))
            lab = frozenset().union(*teile) if teile else frozenset()
            for o in r.ausgaben:
                for x in (o, grund(o)):
                    if x and (x not in label or len(lab) < len(label[x])):
                        label[x] = lab
                        besser = True
        if not besser:
            break
    return label


def alternativen(regeln, start, erlaubt, ziele, menge, annahmen=True):
    """Für jede Station der minimalen Menge: andere Stationen, die sie ersetzen können (die Station wird verboten
    und neu gesucht). Ergebnis: {station: {ersatz, …}}, nur Stationen mit Ersatz."""
    from dataclasses import replace
    out = {}
    for s in sorted(menge):
        ohne = []
        for r in regeln:
            if r.haupt and s in r.haupt:
                if len(r.haupt) == 1:
                    continue
                r = replace(r, haupt=r.haupt - {s})
            ohne.append(r)
        m2 = minimale_stationen(ohne, start, erlaubt, ziele, annahmen)
        if m2:
            ersatz = m2 - (set(menge) - {s})
            if ersatz and len(ersatz) <= 2:
                out[s] = ersatz
    return out


def annahmen_auf_dem_weg(h, ziel, grenze=4):
    """Annahme-Regeln auf dem ersten gefundenen Weg zu `ziel` (aus Huelle.woher), für die Begründung im Bericht."""
    out, gesehen, stapel = [], set(), [ziel]
    while stapel and len(out) < grenze:
        res = stapel.pop()
        if res in gesehen or res not in h.woher:
            continue
        gesehen.add(res)
        r = h.woher[res]
        if r.annahme and r not in out:
            out.append(r)
        for g in r.gruppen():
            vorhanden = sorted(x for x in g if x in h.da)
            if vorhanden:
                stapel.append(min(vorhanden, key=lambda x: h.tiefe.get(x, 0)))
    return out

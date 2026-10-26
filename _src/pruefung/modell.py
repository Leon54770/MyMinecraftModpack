"""Das geschriebene Questbuch (config/ftbquests) als Objekte – genau das, was das Spiel lädt.

Unabhängig vom Generator: Die Prüfungen sehen so auch Fehler, die quests.py selbst nicht bemerkt
(z. B. Dateien, die FTB Quests beim Beenden neu geschrieben hat).
"""
import glob
import json
import os
import re
from dataclasses import dataclass, field

import snbt

FILTER_ITEM = 'ftbfiltersystem:smart_filter'


def long_hex(v):
    """FTB speichert Tabellen-Verweise als Long, die Tabelle selbst als Hex-String."""
    return format(v & 0xFFFFFFFFFFFFFFFF, '016X')


@dataclass
class Aufgabe:
    id: str
    typ: str
    item: str = None            # feste Item-ID
    tag: str = None             # Item-Gruppe (FTB Filter System item_tag)
    anzahl: int = 1
    verbraucht: bool = False
    komponenten: dict = None
    roh: dict = field(default_factory=dict)
    filter: str = None          # Filter-Ausdruck, falls er nicht nur item_tag(...) ist
    quest: 'Quest' = None

    def items(self, tags):
        """Alle Item-IDs, die diese Aufgabe erfüllen (Gruppe aufgelöst)."""
        if self.item:
            return {self.item}
        if self.tag:
            return set(tags.get(self.tag, ()))
        return set()


@dataclass
class Belohnung:
    id: str
    typ: str                    # item, xp, command, loot, choice, random, all_table, …
    item: str = None
    anzahl: int = 1
    tabelle: str = None         # Hex-ID der Tabelle
    team: bool = False
    komponenten: dict = None
    befehl: str = None
    roh: dict = field(default_factory=dict)


@dataclass
class Quest:
    id: str
    titel: str = ''
    deps: list = field(default_factory=list)
    aufgaben: list = field(default_factory=list)
    belohnungen: list = field(default_factory=list)
    kapitel: 'Kapitel' = None
    untertitel: str = ''
    text: list = field(default_factory=list)
    dep_any: bool = False
    optional: bool = False
    wiederholbar: bool = False
    abklingzeit: int = 0
    x: float = 0.0
    y: float = 0.0
    groesse: float = 1.0
    form: str = ''
    roh: dict = field(default_factory=dict)

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return f'Quest({self.id} {self.titel!r})'


@dataclass
class Kapitel:
    id: str
    datei: str
    titel: str = ''
    gruppe: str = ''
    order_index: int = 0
    quests: list = field(default_factory=list)
    links: list = field(default_factory=list)
    untertitel: list = field(default_factory=list)
    roh: dict = field(default_factory=dict)

    def __repr__(self):
        return f'Kapitel({self.datei})'


@dataclass
class Tabelle:
    id: str
    datei: str = ''
    titel: str = ''
    eintraege: list = field(default_factory=list)   # (item, anzahl, gewicht)
    loot_size: int = 1
    kiste: dict = None          # loot_crate: {'drops': {'monster':…, 'passive':…, 'boss':…}, 'string_id':…}
    roh: dict = field(default_factory=dict)


class Questbuch:
    def __init__(self):
        self.kapitel = []
        self.quests = {}
        self.tabellen = {}
        self.gruppen = {}          # Gruppen-ID -> Titel
        self.gruppen_reihe = []    # Reihenfolge aus chapter_groups.snbt
        self.lang = {}
        self.lang_en = {}
        self.daten = {}
        self.schluessel = {}       # Quest-ID -> Generator-Schlüssel (aus _src/questindex.json, falls vorhanden)
        self.ordner = None
        self._ahnen = {}

    # ---- Graph ----
    def ahnen(self, qid):
        """Alle direkten und indirekten Voraussetzungen (ohne die Quest selbst)."""
        if qid in self._ahnen:
            return self._ahnen[qid]
        out, stapel = set(), list(self.quests[qid].deps) if qid in self.quests else []
        while stapel:
            d = stapel.pop()
            if d in out or d not in self.quests:
                continue
            out.add(d)
            stapel.extend(self.quests[d].deps)
        self._ahnen[qid] = out
        return out

    def kinder(self):
        k = {q: [] for q in self.quests}
        for q in self.quests.values():
            for d in q.deps:
                if d in k:
                    k[d].append(q.id)
        return k

    def nachfahren(self, qid):
        k = self.kinder()
        out, stapel = set(), list(k.get(qid, []))
        while stapel:
            c = stapel.pop()
            if c not in out:
                out.add(c)
                stapel.extend(k.get(c, []))
        return out

    def gruppe_von(self, q):
        return self.gruppen.get(q.kapitel.gruppe, '') if q.kapitel else ''

    def name(self, q):
        if isinstance(q, str):
            q = self.quests.get(q)
            if q is None:
                return '?'
        k = self.schluessel.get(q.id)
        kap = q.kapitel.datei if q.kapitel else '?'
        return f'„{q.titel}“ ({kap}' + (f', {k})' if k else ')')

    def alle_aufgaben(self):
        for q in self.quests.values():
            for t in q.aufgaben:
                yield q, t

    def alle_belohnungen(self):
        for q in self.quests.values():
            for r in q.belohnungen:
                yield q, r


# ---------------- Laden ----------------
_FILTER_TAG = re.compile(r'^item_tag\(\s*([a-z0-9_.-]+:[a-z0-9_./-]+)\s*\)$')
_FILTER_ITEM = re.compile(r'^item\(\s*([a-z0-9_.-]+:[a-z0-9_./-]+)\s*\)$')


def _aufgabe(t):
    a = Aufgabe(id=t.get('id', ''), typ=t.get('type', '?'), anzahl=int(t.get('count', 1)),
                verbraucht=bool(t.get('consume_items', False)), roh=t)
    it = t.get('item')
    if isinstance(it, str):                     # ältere FTB-Schreibweise: item: "minecraft:dirt"
        it = {'id': it}
    if isinstance(it, dict):
        iid = it.get('id')
        comps = it.get('components') or None
        if iid == FILTER_ITEM:
            ausdruck = (comps or {}).get('ftbfiltersystem:filter', '')
            m, m2 = _FILTER_TAG.match(ausdruck.strip()), _FILTER_ITEM.match(ausdruck.strip())
            if m:
                a.tag = m.group(1)
            elif m2:
                a.item = m2.group(1)
            else:
                a.filter = ausdruck
        else:
            a.item, a.komponenten = iid, comps
    return a


def _belohnung(r):
    b = Belohnung(id=r.get('id', ''), typ=r.get('type', '?'), roh=r, team=bool(r.get('team_reward', False)))
    if b.typ == 'item':
        it = r.get('item') or {}
        if isinstance(it, str):
            it = {'id': it}
        b.item, b.komponenten = it.get('id'), it.get('components') or None
        b.anzahl = int(r.get('count', it.get('count', 1)))
    elif 'table_id' in r:
        v = r['table_id']
        b.tabelle = long_hex(v) if isinstance(v, int) else str(v).upper()
    elif b.typ == 'command':
        b.befehl = r.get('command', '')
    return b


def _liste(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def lade(ftbquests_ordner, schluessel_datei=None):
    """ftbquests_ordner: config/ftbquests (mit Unterordner quests/)."""
    sd = schluessel_datei or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(ftbquests_ordner))),
                                          '_src', 'questindex.json')
    return lade_quests(os.path.join(ftbquests_ordner, 'quests'), sd)


def lade_quests(qdir, schluessel_datei=None):
    """qdir: Ordner mit chapters/ (lang/, reward_tables/ usw. sind optional, z. B. bei alten Sicherungen)."""
    b = Questbuch()
    b.ordner = qdir
    lang_pfad = os.path.join(qdir, 'lang', 'de_de.snbt')
    b.lang = snbt.load(lang_pfad) if os.path.exists(lang_pfad) else {}
    en = os.path.join(qdir, 'lang', 'en_us.snbt')
    b.lang_en = snbt.load(en) if os.path.exists(en) else {}
    dpfad = os.path.join(qdir, 'data.snbt')
    b.daten = snbt.load(dpfad) if os.path.exists(dpfad) else {}
    gpfad = os.path.join(qdir, 'chapter_groups.snbt')
    if os.path.exists(gpfad):
        for g in snbt.load(gpfad).get('chapter_groups', []):
            b.gruppen_reihe.append(g['id'])
            b.gruppen[g['id']] = b.lang.get(f'chapter_group.{g["id"]}.title', g['id'])
    for f in sorted(glob.glob(os.path.join(qdir, 'reward_tables', '*.snbt'))):
        d = snbt.load(f)
        t = Tabelle(id=d['id'], datei=os.path.basename(f)[:-5], roh=d, loot_size=int(d.get('loot_size', 1)),
                    kiste=d.get('loot_crate'), titel=b.lang.get(f'reward_table.{d["id"]}.title', ''))
        for r in d.get('rewards', []):
            it = r.get('item') or {}
            if isinstance(it, str):
                it = {'id': it}
            t.eintraege.append((it.get('id'), int(r.get('count', it.get('count', 1))), float(r.get('weight', 1.0))))
        b.tabellen[t.id] = t
    for f in sorted(glob.glob(os.path.join(qdir, 'chapters', '*.snbt'))):
        d = snbt.load(f)
        k = Kapitel(id=d['id'], datei=os.path.basename(f)[:-5], gruppe=d.get('group', ''),
                    order_index=int(d.get('order_index', 0)), links=list(d.get('quest_links', [])), roh=d,
                    titel=b.lang.get(f'chapter.{d["id"]}.title', ''),
                    untertitel=_liste(b.lang.get(f'chapter.{d["id"]}.chapter_subtitle')))
        for qd in d.get('quests', []):
            qid = qd['id']
            q = Quest(id=qid, kapitel=k, roh=qd, deps=list(qd.get('dependencies', [])),
                      dep_any=qd.get('dependency_requirement') == 'one_completed',
                      optional=bool(qd.get('optional', False)), wiederholbar=bool(qd.get('can_repeat', False)),
                      abklingzeit=int(qd.get('repeat_cooldown', 0)), x=float(qd.get('x', 0)), y=float(qd.get('y', 0)),
                      groesse=float(qd.get('size', 1.0)), form=qd.get('shape', ''),
                      titel=b.lang.get(f'quest.{qid}.title', ''),
                      untertitel=b.lang.get(f'quest.{qid}.quest_subtitle', ''),
                      text=_liste(b.lang.get(f'quest.{qid}.quest_desc')))
            for t in qd.get('tasks', []):
                a = _aufgabe(t)
                a.quest = q
                q.aufgaben.append(a)
            q.belohnungen = [_belohnung(r) for r in qd.get('rewards', [])]
            k.quests.append(q)
            b.quests[qid] = q
        b.kapitel.append(k)
    sd = schluessel_datei
    if sd and os.path.exists(sd):
        with open(sd, encoding='utf-8') as fh:
            idx = json.load(fh)
        b.schluessel = {v['id']: k for k, v in idx.get('quests', {}).items()}
    return b

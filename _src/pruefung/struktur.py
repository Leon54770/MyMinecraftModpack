"""Strukturprüfungen am geschriebenen Questbuch: IDs, Abhängigkeiten, Aufgaben, Belohnungen, Tabellen,
Verweise, Sprachdatei, Kapitel. Alles ohne Rezeptmodell, deshalb sind die Befunde meist sicher (FEHLER)."""
import re
from collections import defaultdict

from .befund import fehler, warnung, hinweis

B = 'Questbuch'
HEX16 = re.compile(r'^[0-9A-F]{16}$')
INVENTAR_PLAETZE = 37          # 36 Plätze + Nebenhand; FTB zählt nur das Spielerinventar
MIN_ABKLINGZEIT = 600          # Sekunden; darunter wird ein Tausch zur Dauerschleife
AUFGABEN_TYPEN = {'item', 'kill', 'dimension', 'forge_energy', 'checkmark', 'advancement', 'stat', 'location', 'xp',
                  'biome', 'structure', 'observation', 'fluid', 'gamestage', 'stage', 'custom'}
BELOHNUNGS_TYPEN = {'item', 'xp', 'xp_levels', 'command', 'loot', 'choice', 'random', 'all_table', 'advancement',
                    'toast', 'custom', 'stage', 'gamestage'}
TABELLEN_TYPEN = {'loot', 'choice', 'random', 'all_table'}


# ---------------- IDs ----------------
def pruefe_ids(b):
    befunde = []
    vorkommen = defaultdict(list)          # id -> [(art, ort)]
    for gid in b.gruppen:
        vorkommen[gid].append(('Kapitelgruppe', b.gruppen[gid]))
    for t in b.tabellen.values():
        vorkommen[t.id].append(('Tabelle', t.datei or t.id))
        for r in t.roh.get('rewards', []):
            if 'id' in r:
                vorkommen[r['id']].append(('Tabelleneintrag', t.datei or t.id))
    for k in b.kapitel:
        vorkommen[k.id].append(('Kapitel', k.datei))
        for l in k.links:
            if 'id' in l:
                vorkommen[l['id']].append(('Verweis', k.datei))
        for q in k.quests:
            vorkommen[q.id].append(('Quest', b.name(q)))
            for t in q.aufgaben:
                vorkommen[t.id].append(('Aufgabe', b.name(q)))
            for r in q.belohnungen:
                vorkommen[r.id].append(('Belohnung', b.name(q)))
    for i, wo in sorted(vorkommen.items()):
        if not HEX16.match(str(i)) or set(str(i)) == {'0'}:
            befunde.append(fehler(B, f'ungültige ID {i!r} ({wo[0][0]} in {wo[0][1]}): erwartet 16 Hex-Zeichen, nicht 0'))
        if len(wo) > 1:
            arten = ', '.join(f'{a} in {o}' for a, o in wo)
            nur_tabelle = all(a == 'Tabelleneintrag' for a, _ in wo)
            befunde.append((warnung if nur_tabelle else fehler)(B, f'ID {i} mehrfach vergeben: {arten}'))
    return befunde


# ---------------- Abhängigkeiten ----------------
def _zyklen(b):
    """Starke Zusammenhangskomponenten (Tarjan, iterativ) mit mehr als einem Knoten oder Selbstbezug."""
    index, low, auf_stapel, stapel, out = {}, {}, set(), [], []
    zaehler = [0]
    for start in b.quests:
        if start in index:
            continue
        arbeit = [(start, iter(b.quests[start].deps))]
        index[start] = low[start] = zaehler[0]; zaehler[0] += 1
        stapel.append(start); auf_stapel.add(start)
        while arbeit:
            v, it = arbeit[-1]
            weiter = False
            for w in it:
                if w not in b.quests:
                    continue
                if w not in index:
                    index[w] = low[w] = zaehler[0]; zaehler[0] += 1
                    stapel.append(w); auf_stapel.add(w)
                    arbeit.append((w, iter(b.quests[w].deps)))
                    weiter = True
                    break
                if w in auf_stapel:
                    low[v] = min(low[v], index[w])
            if weiter:
                continue
            arbeit.pop()
            if arbeit:
                low[arbeit[-1][0]] = min(low[arbeit[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stapel.pop(); auf_stapel.discard(w); comp.append(w)
                    if w == v:
                        break
                if len(comp) > 1 or v in b.quests[v].deps:
                    out.append(comp)
    return out


def startquest(b):
    """Die Quest ohne Voraussetzung im ersten Kapitel der ersten Gruppe (dort beginnt das Buch)."""
    reihe = {g: i for i, g in enumerate(b.gruppen_reihe)}
    kapitel = sorted(b.kapitel, key=lambda k: (reihe.get(k.gruppe, 99), k.order_index))
    for k in kapitel:
        for q in k.quests:
            if not q.deps:
                return q.id
    return None


def freischaltbar(b):
    """Quests, die sich überhaupt freischalten lassen (fehlende Voraussetzungen und Zyklen blockieren)."""
    frei, neu = set(), True
    while neu:
        neu = False
        for q in b.quests.values():
            if q.id in frei:
                continue
            da = [d in frei for d in q.deps]
            if not q.deps or (q.dep_any and any(da)) or (not q.dep_any and all(da)):
                frei.add(q.id)
                neu = True
    return frei


def pruefe_graph(b):
    befunde = []
    for q in b.quests.values():
        for d in q.deps:
            if d == q.id:
                befunde.append(fehler(B, f'{b.name(q)} hängt an sich selbst'))
            elif d not in b.quests:
                befunde.append(fehler(B, f'{b.name(q)}: Voraussetzung {d} gibt es nicht'))
        if q.dep_any and len(q.deps) < 2:
            befunde.append(warnung(B, f'{b.name(q)}: „eins von“ mit weniger als zwei Voraussetzungen'))
        if not q.optional and q.deps:
            opt = [d for d in q.deps if d in b.quests and b.quests[d].optional]
            if opt and (not q.dep_any or len(opt) == len([d for d in q.deps if d in b.quests])):
                befunde.append(warnung(B, f'Pflicht-Quest {b.name(q)} hängt an optionaler Quest '
                                          + ', '.join(b.name(d) for d in opt)))
    for comp in _zyklen(b):
        befunde.append(fehler(B, 'Zyklus in den Abhängigkeiten: ' + ' → '.join(b.name(q) for q in sorted(comp))))
    start = startquest(b)
    for q in b.quests.values():
        if not q.deps and q.id != start:
            befunde.append(warnung(B, f'{b.name(q)} hat keine Voraussetzung und steht frei im Buch (Start ist {b.name(start)})'))
    frei = freischaltbar(b)
    direkt = {q.id for q in b.quests.values() if any(d not in b.quests or d == q.id for d in q.deps)}
    direkt |= {q for comp in _zyklen(b) for q in comp}
    rest = sorted(q for q in b.quests if q not in frei and q not in direkt and not b.quests[q].optional)
    if rest:
        befunde.append(fehler(B, f'{len(rest)} Pflicht-Quests lassen sich nie freischalten (Folge der Fehler oben): '
                                 + ', '.join(b.name(q) for q in rest)))
    return befunde


# ---------------- Aufgaben ----------------
def pruefe_aufgaben(b, reg):
    befunde = []
    for q in b.quests.values():
        if not q.aufgaben:
            befunde.append(fehler(B, f'{b.name(q)} hat keine Aufgabe: FTB Quests hakt sie sofort ab'))
        if q.wiederholbar:
            for t in q.aufgaben:
                if t.typ == 'item' and not t.verbraucht:
                    befunde.append(fehler(B, f'{b.name(q)} ist wiederholbar, verbraucht aber {t.item or t.tag} nicht: '
                                             'die Belohnung lässt sich beliebig oft abholen'))
            if q.abklingzeit < MIN_ABKLINGZEIT:
                befunde.append(hinweis(B, f'{b.name(q)} ist wiederholbar mit nur {q.abklingzeit} s Abklingzeit'))
        for t in q.aufgaben:
            befunde += _aufgabe(b, reg, q, t)
    return befunde


def _aufgabe(b, reg, q, t):
    out = []
    wo = b.name(q)
    if t.typ == 'checkmark':
        return [fehler(B, f'{wo}: Haken-Aufgabe (Projektregel: Quests prüfen sich selbst)')]
    if t.typ not in AUFGABEN_TYPEN:
        return [warnung(B, f'{wo}: unbekannter Aufgabentyp {t.typ}')]
    if t.typ == 'item':
        if t.filter is not None:
            out.append(warnung(B, f'{wo}: Filter-Ausdruck „{t.filter}“ wird nicht geprüft (nur item_tag/item)'))
        elif t.tag:
            if t.tag not in reg.tags:
                out.append(fehler(B, f'{wo}: unbekannte Item-Gruppe {t.tag}'))
            elif not reg.tags[t.tag]:
                out.append(fehler(B, f'{wo}: Item-Gruppe {t.tag} ist leer, die Aufgabe ist unerfüllbar'))
            if t.verbraucht:
                out.append(fehler(B, f'{wo}: Gruppe {t.tag} in einer verbrauchenden Aufgabe (Projektregel 4)'))
        elif not t.item:
            out.append(fehler(B, f'{wo}: Item-Aufgabe ohne Item'))
        elif t.item not in reg.items:
            out.append(fehler(B, f'{wo}: unbekanntes Item {t.item}'))
        if t.anzahl < 1:
            out.append(fehler(B, f'{wo}: Anzahl {t.anzahl} bei {t.item or t.tag}'))
        elif not t.verbraucht:
            out += _kapazitaet(reg, wo, t)
    elif t.typ == 'kill':
        e = t.roh.get('entity')
        if reg.entities is not None and e not in reg.entities:
            out.append(fehler(B, f'{wo}: unbekannter Mob {e}'))
        if int(t.roh.get('value', 1)) < 1:
            out.append(fehler(B, f'{wo}: Anzahl {t.roh.get("value")} beim Töten'))
    elif t.typ == 'dimension':
        d = t.roh.get('dimension')
        if reg.dimensionen is not None and d not in reg.dimensionen:
            out.append(fehler(B, f'{wo}: unbekannte Dimension {d}'))
    elif t.typ == 'forge_energy':
        if int(t.roh.get('value', 0)) <= 0:
            out.append(fehler(B, f'{wo}: Strom-Aufgabe ohne Menge'))
        # FTB Quests 2101.1.37: fehlendes max_input = 0, der Aufgabenbildschirm nimmt dann keinen Strom an (Jar geprüft 26.10.2026)
        if int(t.roh.get('max_input', 0)) <= 0:
            out.append(fehler(B, f'{wo}: Strom-Aufgabe ohne max_input, FTB Quests nimmt dann keinen Strom an (Quest unlösbar)'))
    return out


def _kapazitaet(reg, wo, t):
    if t.item:
        stapel = reg.stapelgroesse(t.item)
    else:
        groessen = [reg.stapelgroesse(i) for i in reg.tags.get(t.tag, [])]
        stapel = max(groessen) if groessen and None not in groessen else None
    grenze = INVENTAR_PLAETZE * (stapel or 64)
    if t.anzahl > grenze:
        wie = f'Stapelgröße {stapel}' if stapel else 'Stapelgröße unbekannt, gerechnet mit 64'
        return [warnung(B, f'{wo}: {t.anzahl}× {t.item or t.tag} ohne Verbrauch, ins Inventar passen höchstens '
                           f'{grenze} ({wie}). FTB zählt das Inventar auf einmal')]
    return []


# ---------------- Belohnungen und Tabellen ----------------
def pruefe_belohnungen(b, reg):
    befunde = []
    benutzt = set()
    for q, r in b.alle_belohnungen():
        wo = b.name(q)
        if r.typ not in BELOHNUNGS_TYPEN:
            befunde.append(warnung(B, f'{wo}: unbekannter Belohnungstyp {r.typ}'))
        if r.typ == 'item':
            if r.item not in reg.items:
                befunde.append(fehler(B, f'{wo}: Belohnung mit unbekanntem Item {r.item}'))
            if r.anzahl < 1:
                befunde.append(fehler(B, f'{wo}: Belohnung {r.item} mit Anzahl {r.anzahl}'))
        elif r.typ in TABELLEN_TYPEN:
            t = b.tabellen.get(r.tabelle)
            benutzt.add(r.tabelle)
            if t is None:
                befunde.append(fehler(B, f'{wo}: Belohnungstabelle {r.tabelle} gibt es nicht'))
            elif r.typ == 'choice' and len(t.eintraege) < 2:
                befunde.append(warnung(B, f'{wo}: Auswahl aus „{t.titel or t.datei}“ hat nur {len(t.eintraege)} Eintrag'))
    kisten = defaultdict(list)
    for t in b.tabellen.values():
        name = t.titel or t.datei or t.id
        if t.loot_size < 1:
            befunde.append(fehler(B, f'Tabelle {name}: loot_size {t.loot_size}'))
        for item, n, w in t.eintraege:
            if item not in reg.items:
                befunde.append(fehler(B, f'Tabelle {name}: unbekanntes Item {item}'))
            if w <= 0:
                befunde.append(fehler(B, f'Tabelle {name}: {item} mit Gewicht {w} kommt nie'))
            if n < 1:
                befunde.append(fehler(B, f'Tabelle {name}: {item} mit Anzahl {n}'))
        if t.kiste:
            kisten[t.kiste.get('string_id')].append(name)
            faellt = any(int(v) > 0 for v in (t.kiste.get('drops') or {}).values())
        else:
            faellt = False
        if t.id not in benutzt and not faellt:
            befunde.append(hinweis(B, f'Tabelle {name} wird von keiner Quest vergeben und fällt von keinem Mob'))
    for sid, namen in kisten.items():
        if len(namen) > 1:
            befunde.append(fehler(B, f'Kisten-Kennung {sid} mehrfach: {", ".join(namen)}'))
    return befunde


# ---------------- Verweise ----------------
def pruefe_verweise(b):
    """FTB zeichnet eine Linie zu einer Voraussetzung aus einem anderen Kapitel nur, wenn dort ein Verweis steht."""
    befunde = []
    for k in b.kapitel:
        gesehen = set()
        for l in k.links:
            ziel = l.get('linked_quest')
            if ziel not in b.quests:
                befunde.append(fehler(B, f'Kapitel {k.datei}: Verweis auf unbekannte Quest {ziel}'))
                continue
            if b.quests[ziel].kapitel is k:
                befunde.append(hinweis(B, f'Kapitel {k.datei}: Verweis auf {b.name(ziel)} aus dem eigenen Kapitel'))
            if ziel in gesehen:
                befunde.append(hinweis(B, f'Kapitel {k.datei}: {b.name(ziel)} doppelt verwiesen'))
            gesehen.add(ziel)
        ohne = [(q, d) for q in k.quests for d in q.deps
                if d in b.quests and b.quests[d].kapitel is not k and d not in gesehen]
        if ohne:
            ziele = sorted({b.name(d) for _, d in ohne})
            befunde.append(hinweis(B, f'Kapitel {k.datei}: {len(ohne)} Linien zu Voraussetzungen aus anderen Kapiteln '
                                      f'fehlen (kein Verweis im Kapitel): ' + ', '.join(ziele)))
    return befunde


# ---------------- Sprachdatei ----------------
_LANG_KEY = re.compile(r'^([a-z_]+)\.([0-9A-Fa-f]{16})\.')


def pruefe_sprache(b):
    befunde = []
    for q in b.quests.values():
        if not q.titel.strip():
            befunde.append(fehler(B, f'Quest {q.id} in {q.kapitel.datei if q.kapitel else "?"} hat keinen Titel'))
    for k in b.kapitel:
        if not k.titel.strip():
            befunde.append(fehler(B, f'Kapitel {k.datei} hat keinen Titel'))
    bekannt = set(b.quests) | {k.id for k in b.kapitel} | set(b.tabellen) | set(b.gruppen) | {'0000000000000001'}
    for q in b.quests.values():
        bekannt |= {t.id for t in q.aufgaben} | {r.id for r in q.belohnungen}
    waisen = sorted(k for k in b.lang if (m := _LANG_KEY.match(k)) and m.group(2).upper() not in bekannt)
    if waisen:
        befunde.append(hinweis(B, f'{len(waisen)} Texte in de_de.snbt gehören zu keinem Objekt mehr, z. B. '
                                  + ', '.join(waisen[:5])))
    if b.lang_en and set(b.lang) != set(b.lang_en):
        nur_de, nur_en = set(b.lang) - set(b.lang_en), set(b.lang_en) - set(b.lang)
        befunde.append(hinweis(B, f'de_de und en_us unterscheiden sich: {len(nur_de)} nur deutsch, {len(nur_en)} nur englisch'))
    elif not b.lang_en and b.lang:
        befunde.append(hinweis(B, 'en_us.snbt fehlt: englische Clients sehen IDs statt Texten'))
    return befunde


# ---------------- Kapitel ----------------
def pruefe_kapitel(b):
    befunde = []
    reihe = defaultdict(list)
    for k in b.kapitel:
        if k.gruppe not in b.gruppen:
            befunde.append(fehler(B, f'Kapitel {k.datei}: Gruppe {k.gruppe} gibt es nicht'))
        reihe[(k.gruppe, k.order_index)].append(k.datei)
        fn = k.roh.get('filename') if k.roh else None
        if fn is not None and fn != k.datei:
            befunde.append(fehler(B, f'Kapitel {k.datei}.snbt trägt filename „{fn}“'))
        if not k.quests and not k.links:
            befunde.append(warnung(B, f'Kapitel {k.datei} ist leer'))
    for (g, i), dateien in reihe.items():
        if len(dateien) > 1:
            befunde.append(warnung(B, f'Kapitel {", ".join(dateien)} haben in Gruppe {b.gruppen.get(g, g)} '
                                      f'dieselbe Position {i}: Reihenfolge im Buch zufällig'))
    return befunde

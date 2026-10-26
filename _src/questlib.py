"""Baukasten für FTB-Quests-Dateien (SNBT) – Sky and Stone.

Ein Kapitel ist eine Liste von Q(...)-Einträgen. IDs werden stabil aus Namen gehasht,
damit Fortschritt beim Neu-Erzeugen erhalten bleibt.
"""
import hashlib, json, os

# ---------------- IDs ----------------
def hid(*parts):
    h = hashlib.sha1('/'.join(parts).encode()).hexdigest().upper()[:16]
    return ('1' + h[1:]) if h[0] in '89ABCDEF0' else h   # positiv als long, nie 0

# ---------------- SNBT ----------------
class D(float): pass          # double
class L(int): pass            # long
class F(float): pass          # float

import re as _re
def _key(k):   # Schlüssel mit Sonderzeichen (z. B. 'ftbfiltersystem:filter') müssen in Anführungszeichen
    return k if _re.fullmatch(r'[A-Za-z0-9_.+-]+', k) else json.dumps(k, ensure_ascii=False)

def snbt(v, ind=0):
    p = '\t' * ind
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, D): return f'{float(v)}d'
    if isinstance(v, F): return f'{float(v)}f'
    if isinstance(v, L): return f'{int(v)}L'
    if isinstance(v, int): return str(v)
    if isinstance(v, float): return f'{v}d'
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        if not v: return '[ ]'
        if all(isinstance(x, str) for x in v) and len(v) <= 4 and sum(len(x) for x in v) < 70:
            return '[' + ', '.join(snbt(x) for x in v) + ']'
        return '[\n' + '\n'.join(p + '\t' + snbt(x, ind + 1) for x in v) + '\n' + p + ']'
    if isinstance(v, dict):
        if not v: return '{ }'
        return '{\n' + '\n'.join(f'{p}\t{_key(k)}: {snbt(x, ind + 1)}' for k, x in v.items()) + '\n' + p + '}'
    raise TypeError(type(v))

# ---------------- Aufgaben / Belohnungen ----------------
def item(i, n=1, consume=False, komponenten=None):
    """komponenten (0.8.0): Datenkomponenten, die das Item haben muss (FTB-Abgleich „fuzzy“),
    z. B. {'productivebees:bee_type': 'productivebees:iron'} für eine Eisenbienen-Wabe."""
    return ('item', i, n, consume, komponenten)
def tag(t, n=1, icon=None, title=None, consume=False):  return ('tag', t, n, icon, title, consume)   # irgendein Item aus der Gruppe (FTB Filter System)

# Eigene Gruppen aus kubejs/server_scripts/gruppen.js. Rückfall, solange eine neue Gruppe noch nicht im Tag-Dump steht;
# steht sie dort, prüft der Generator zusätzlich, dass sie nicht leer ist.
EIGENE_TAGS = {'skyandstone:sieves', 'skyandstone:water_crucibles', 'skyandstone:hopper_botany_pots',
               'skyandstone:archwood_saplings', 'skyandstone:roofs', 'skyandstone:rope_bridges', 'skyandstone:weg_zum_herz',
               'skyandstone:erz_ohne_sieb'}
def check():                      return ('checkmark',)
def dim(d):                       return ('dimension', d)
def kill(e, n=1):                 return ('kill', e, n)
def energie(fe):                  return ('forge_energy', fe)   # 0.8.0: Strom in einen Aufgabenbildschirm einspeisen

def xp(n):                        return ('xp', n)
# 1.1.0: Block ansehen (FTB ObservationTask: observe_type 0 = Block) und Fortschritt (AdvancementTask, criterion '' = ganz)
def beobachte(block, ticks=40):    return ('observation', block, ticks)
def fortschritt(adv):              return ('advancement', adv)
def give(i, n=1, komponenten=None): return ('give', i, n, komponenten)   # komponenten: z. B. Name/Lore einer Tagebuchseite
def crate(name, team=False, art='loot'):
    """Belohnung aus einer Tabelle. art: 'loot' = die Kiste selbst ins Inventar (zum Öffnen, 0.8.0),
    'choice' = Spieler wählt ein Item aus der Tabelle, 'random' = ein zufälliges Item direkt (bis 0.7.0 überall).
    team=True: eine pro Team statt pro Spieler."""
    return ('table', name, team, art)

class Q:
    def __init__(self, key, title, x, y, tasks, desc=(), sub='', deps=(), rewards=(), shape=None, size=None,
                 icon=None, optional=False, dep_any=False, repeat=None):
        self.key, self.title, self.x, self.y = key, title, x, y
        self.tasks = tasks if isinstance(tasks, list) else [tasks]
        self.desc, self.sub, self.deps, self.rewards = list(desc), sub, list(deps), list(rewards)
        self.shape, self.size, self.icon, self.optional, self.dep_any = shape, size, icon, optional, dep_any
        self.repeat = repeat   # Abklingzeit in Sekunden -> wiederholbar

class Chapter:
    def __init__(self, key, title, group, icon, quests, sub='', links=(), mode='baum'):
        self.key, self.title, self.group, self.icon, self.quests, self.sub = key, title, group, icon, quests, sub
        self.links = list(links)   # Quest-Schlüssel aus anderen Kapiteln, die hier als Verweis erscheinen
        self.mode = mode           # 'baum' = Spalten nach Abhängigkeit, 'pfad' = Schlangenlinie in Listenreihenfolge

def pfad_layout(items, per_row=5, dx=2.0, dy=3.0):
    """Schlangenlinie: Reihen zu per_row, Richtung wechselt je Reihe, leichter Zickzack. items = [(schlüssel, größe)]."""
    pos, x, row, col = {}, 0.0, 0, 0
    prev = None
    for i, (k, s) in enumerate(items):
        if col == per_row:
            row, col, prev = row + 1, 0, None
        richtung = 1 if row % 2 == 0 else -1
        if prev is not None:
            x += richtung * max(dx, (prev + s) * 0.5 + 0.6)
        zick = 0.45 if col % 2 else -0.45
        extra = max(0.0, (s - 1.0) * 0.6)   # große Meilensteine etwas tiefer, damit sie nicht in die Reihe darüber ragen
        pos[k] = (round(x, 2), round(row * dy + zick + extra, 2))
        prev, col = s, col + 1
    return pos

# ---------------- Automatisches Layout (0.6.4) ----------------
# Spalten nach Abhängigkeitstiefe, Verweise direkt eine Spalte vor ihrer ersten Quest. Lange Kapitel laufen
# als Schlange: nach `breite` Spalten geht es eine Reihe tiefer in die andere Richtung weiter.
# Danach verschiebt eine Suche Quests innerhalb ihrer Spalte, bis möglichst keine Linie mehr durch eine
# fremde Quest läuft und sich wenige Linien kreuzen (Maßstab: layoutcheck.py, wie FTB Quests zeichnet).
import random

def ebenen_layout(chapter, dx=2.4, dy=1.8, max_zeilen=6, runden=8000):
    import layoutcheck as LC
    qs = {q.key: q for q in chapter.quests}
    alle_links = [l for l in chapter.links if l not in qs]
    hat_kind = {l for l in alle_links if any(l in q.deps for q in qs.values())}
    links = [l for l in alle_links if l in hat_kind]          # Verweise mit Linie: Teil des Baums
    nur_info = [l for l in alle_links if l not in hat_kind]   # reine Verweise: eigene Reihe oben, ohne Linien
    nodes = list(qs) + links
    size = {k: (qs[k].size or 1.0) if k in qs else 1.0 for k in nodes}
    deps = {k: [d for d in qs[k].deps if d in qs or d in links] for k in qs}
    deps.update({l: [] for l in links})
    kinder = {k: [c for c in qs if k in deps[c]] for k in nodes}
    layer = {}
    def lq(k, seen=()):
        if k in layer: return layer[k]
        if k in seen: return 0
        ps = [p for p in deps[k] if p in qs]
        layer[k] = 0 if not ps else 1 + max(lq(p, seen + (k,)) for p in ps)
        return layer[k]
    for k in qs: lq(k)
    if links:   # Platz für Verweise direkt vor ihrer ersten Quest
        for k in qs: layer[k] += 1
        for l in links:
            ks = [layer[c] for c in kinder[l]]
            layer[l] = max(0, min(ks) - 1) if ks else 0
    # Zu volle Spalten aufteilen: Überzählige eine Spalte weiter, alles dahinter rückt nach
    L = 0
    while L <= max(layer.values()):
        ks = [k for k in nodes if layer[k] == L]
        if len(ks) > max_zeilen:
            ks.sort(key=lambda k: (len(kinder[k]) == 0, nodes.index(k)))   # Quests mit Nachfolgern bleiben vorn
            rest = set(ks[max_zeilen:])
            for k in nodes:
                if layer[k] > L or k in rest: layer[k] += 1
        L += 1
    # Verweise, die nur Nachfolger weiter rechts haben, so nah wie möglich davor
    for l in links:
        ks = [layer[c] for c in kinder[l]]
        if ks:
            ziel = min(ks) - 1
            if sum(1 for k in nodes if layer[k] == ziel and k != l) < max_zeilen: layer[l] = max(0, ziel)
    def spalten(layer):
        cols = {}
        for k in nodes: cols.setdefault(layer[k], []).append(k)
        return cols
    cols = spalten(layer)
    order = {k: i for i, k in enumerate(nodes)}
    for _ in range(6):   # Mittelwert der Nachbarn -> wenige Kreuzungen
        for L in sorted(cols):
            def bary(k):
                nb = [order[p] for p in deps[k] + kinder[k]]
                return sum(nb) / len(nb) if nb else order[k]
            cols[L].sort(key=bary)
            for i, k in enumerate(cols[L]): order[k] = L * 100 + i
    slot = {}
    for L, ks in cols.items():
        y = 0.0
        for i, k in enumerate(ks):
            if i: y += max(1.0, (size[ks[i - 1]] + size[k]) * 0.5 / dy + 0.35)
            slot[k] = y
        mid = y / 2
        for k in ks: slot[k] -= mid   # Spalten mittig ausrichten
    def pos_of(layer, slot): return {k: (round(layer[k] * dx, 2), round(slot[k] * dy, 2)) for k in nodes}
    def frei(layer, slot, k):
        return all(abs(slot[k] - slot[o]) >= (size[k] + size[o]) * 0.5 / dy + 0.25 for o in nodes if o != k and layer[o] == layer[k])
    def kosten(layer, slot):
        pos = pos_of(layer, slot)
        ch = {'quests': [{'id': k, 'x': pos[k][0], 'y': pos[k][1], 'size': size[k], 'dependencies': deps[k]} for k in qs],
              'quest_links': [{'linked_quest': l, 'x': pos[l][0], 'y': pos[l][1], 'size': 1.0} for l in links]}
        r = LC.pruefe(ch)
        ausdehnung = (max(slot.values()) - min(slot.values())) * 0.5 + sum(abs(v) for v in slot.values()) * 0.02
        return 100 * len(r['durch']) + 100 * len(r['ueberlappt']) + 10 * len(r['kreuzt']) + ausdehnung
    start_layer, start_slot = dict(layer), dict(slot)
    gesamt = None
    for versuch in range(16):          # 0.7.0: weitere Anläufe nur, solange noch eine Linie durch eine Quest läuft
      layer, slot = dict(start_layer), dict(start_slot)
      rnd = random.Random(chapter.key if versuch == 0 else f'{chapter.key}/{versuch}')   # fest -> gleiche Ausgabe
      best = kosten(layer, slot)
      if len(nodes) > 1:
        for _ in range(runden):
              if best < 2: break
              k = rnd.choice(nodes)
              nl, ns = dict(layer), dict(slot)
              art = rnd.random()
              if art < 0.4:                                   # mit einer Quest derselben Spalte tauschen
                  os_ = [x for x in nodes if x != k and layer[x] == layer[k]]
                  if not os_: continue
                  o = rnd.choice(os_); ns[k], ns[o] = slot[o], slot[k]
              elif art < 0.8:                                 # in der Spalte verschieben
                  ns[k] = slot[k] + rnd.choice([-2.0, -1.5, -1.0, -0.5, 0.5, 1.0, 1.5, 2.0])
                  if not frei(nl, ns, k): continue
              else:                                           # eine Spalte nach links/rechts, wenn die Abhängigkeiten es erlauben
                  lo = max([layer[d] + 1 for d in deps[k]], default=0)
                  hi = min([layer[c] - 1 for c in kinder[k]], default=layer[k] + 1)
                  ziel = layer[k] + rnd.choice([-1, 1])
                  if not (lo <= ziel <= hi): continue
                  nl[k] = ziel
                  if sum(1 for o in nodes if nl[o] == ziel) > max_zeilen or not frei(nl, ns, k): continue
              c = kosten(nl, ns)
              if c < best: best, layer, slot = c, nl, ns
      if gesamt is None or best < gesamt[0]: gesamt = (best, layer, slot)
      if gesamt[0] < 100: break
    best, layer, slot = gesamt
    m = min(layer.values())
    pos = pos_of({k: v - m for k, v in layer.items()}, slot)
    for k, q in qs.items(): q.x, q.y = pos[k]
    out = {l: pos[l] for l in links}
    if nur_info:
        top = min(p[1] - size[k] / 2 for k, p in pos.items()) - 2.0
        for i, l in enumerate(nur_info):
            r, c = divmod(i, 10)
            out[l] = (round(c * 1.6, 2), round(top - r * 1.5, 2))
    return out

def auto_layout(chapter, dx=2.2, dy=1.7, link_gap=2.6):
    if chapter.quests: return ebenen_layout(chapter)
    return pfad_layout([(k, 1.0) for k in chapter.links])   # reine Verweis-Kapitel (Story)

def auto_layout_alt(chapter, dx=2.2, dy=1.7, link_gap=2.6):
    """Spalten nach Abhängigkeitstiefe (nur Abhängigkeiten im selben Kapitel), Zeilen nach Eltern-Mittelwert.
    Verweise (links) stehen in einer eigenen Spalte ganz links. Gibt {schlüssel: (x, y)} für Verweise zurück."""
    if chapter.mode == 'pfad':
        if chapter.quests:   # Hauptstory: Quests als Pfad, Verweise (falls vorhanden) darüber
            pos = pfad_layout([(q.key, q.size or 1.0) for q in chapter.quests])
            for q in chapter.quests: q.x, q.y = pos[q.key]
            return {k: (i * 1.6, -2.6) for i, k in enumerate(chapter.links)}
        return pfad_layout([(k, 1.0) for k in chapter.links])
    keys = {q.key: q for q in chapter.quests}
    depth = {}
    def d(k, seen=()):
        if k in depth: return depth[k]
        if k in seen: return 0
        ps = [p for p in keys[k].deps if p in keys]
        depth[k] = 0 if not ps else 1 + max(d(p, seen + (k,)) for p in ps)
        return depth[k]
    for k in keys: d(k)
    cols = {}
    for q in chapter.quests: cols.setdefault(depth[q.key], []).append(q)
    max_rows = 6
    link_cols = (len(chapter.links) + max_rows - 1) // max_rows
    x = (link_gap + (link_cols - 1) * 1.6) if chapter.links else 0.0
    ypos, prev_size = {}, None
    order = {q.key: i for i, q in enumerate(chapter.quests)}
    for col in sorted(cols):
        qs = cols[col]
        def pref(q):
            ps = [ypos[p] for p in q.deps if p in ypos]
            return sum(ps) / len(ps) if ps else order[q.key] * 0.001
        qs.sort(key=pref)
        # zu hohe Spalten in mehrere Teilspalten aufteilen
        parts = [qs[i:i + max_rows] for i in range(0, len(qs), max_rows)]
        for part in parts:
            big = max((q.size or 1.0) for q in part)
            if prev_size is not None:
                x += max(dx, (prev_size + big) * 0.5 + 0.6)
            prev_size = big
            sizes = [(q.size or 1.0) for q in part]
            ys, y = [], 0.0
            for i, s in enumerate(sizes):
                if i: y += max(dy, (sizes[i - 1] + s) * 0.5 + 0.45)
                ys.append(y)
            target = (sum(pref(q) for q in part) / len(part)) if col and len(parts) == 1 else 0.0
            shift = target - (ys[0] + ys[-1]) / 2
            for q, yy in zip(part, ys):
                q.x, q.y = round(x, 2), round(yy + shift, 2)
                ypos[q.key] = q.y
    links = {}
    for i, k in enumerate(chapter.links):   # Verweise in Spalten zu höchstens 6
        col, row = divmod(i, max_rows)
        in_col = min(max_rows, len(chapter.links) - col * max_rows)
        links[k] = (round(col * 1.6, 2), round((row - (in_col - 1) / 2) * 1.5, 2))
    return links

# ---------------- Ausgabe ----------------
# Gegen Tippfehler in Kill-/Dimensions-Aufgaben (items.json kennt nur Items). Neue Ziele hier eintragen.
BEKANNTE_DIMENSIONEN = {'minecraft:overworld', 'minecraft:the_nether', 'minecraft:the_end'}
BEKANNTE_MOBS = {'minecraft:ender_dragon', 'minecraft:wither', 'ars_nouveau:wilden_boss',
                 'minecraft:wither_skeleton', 'minecraft:enderman'}   # 26.10.2026: Prüfungen Festung/Schattenjagd

class Builder:
    def __init__(self, out_dir, known_items, known_tags=()):
        self.out, self.known = out_dir, set(known_items)
        self.known_tags = set(known_tags)
        # 0.7.0: Inhalt der Gruppen (tags.json vom Testserver, kubejs/dev_tags.json), damit leere Gruppen auffallen
        self.tag_inhalt = dict(known_tags) if isinstance(known_tags, dict) else {}
        self.lang = {}                 # Schlüssel -> Text/Liste
        self.qids = {}                 # 'kapitel/quest' und 'quest' -> ID
        self.tables = {}               # name -> (id, rewards)
        self.errors = []
        self.hinweise = []            # Layout-Probleme: werden gemeldet, blockieren aber nicht

    def check_item(self, i, where):
        if self.known and i not in self.known: self.errors.append(f'{where}: unbekanntes Item {i}')

    def table(self, name, title, entries, loot_size=1, crate=None):
        tid = hid('table', name)
        rewards = []
        for i, n, w in entries:
            self.check_item(i, f'Tabelle {name}')
            rewards.append({'count': n, 'id': hid('table', name, i), 'item': {'count': 1, 'id': i}, 'type': 'item', 'weight': F(w)})
        data = {'id': tid, 'loot_size': loot_size, 'rewards': rewards, 'use_title': True}
        if crate:   # (Farbe, leuchtet, passiv, Monster, Boss) -> Kisten-Item, das Mobs fallen lassen
            color, glow, pa, mo, bo = crate
            data['loot_crate'] = {'color': color, 'drops': {'boss': bo, 'monster': mo, 'passive': pa}, 'glow': glow, 'item_name': '', 'string_id': name + 'kiste'}
        self.tables[name] = (tid, data)
        self.lang[f'reward_table.{tid}.title'] = title

    def register(self, chapters):
        for c in chapters:
            for q in c.quests:
                qid = hid('quest', c.key, q.key)
                if q.key in self.qids: self.errors.append(f'doppelter Quest-Schlüssel {q.key}')
                self.qids[q.key] = qid

    def _task(self, c, q, n, t):
        tid = hid('task', c.key, q.key, str(n))
        if t[0] == 'item':
            self.check_item(t[1], f'{c.key}/{q.key}')
            d = {'id': tid, 'item': {'count': 1, 'id': t[1]}, 'type': 'item'}
            if t[2] != 1: d['count'] = L(t[2])
            if t[3]: d['consume_items'] = True
            if len(t) > 4 and t[4]:
                d['item']['components'] = dict(t[4]); d['match_components'] = 'fuzzy'
            return d
        if t[0] == 'tag':
            tg, n_, icon, title = t[1:5]
            if self.known_tags and tg not in self.known_tags and tg not in EIGENE_TAGS:
                self.errors.append(f'{c.key}/{q.key}: unbekannte Item-Gruppe {tg}')
            elif tg in self.tag_inhalt and not self.tag_inhalt[tg]:
                self.errors.append(f'{c.key}/{q.key}: Item-Gruppe {tg} ist leer (Aufgabe unerfüllbar)')
            d = {'id': tid, 'item': {'components': {'ftbfiltersystem:filter': f'item_tag({tg})'}, 'count': 1,
                                     'id': 'ftbfiltersystem:smart_filter'}, 'type': 'item'}
            if n_ != 1: d['count'] = L(n_)
            if len(t) > 5 and t[5]: d['consume_items'] = True
            if icon:
                self.check_item(icon, f'{c.key}/{q.key} Aufgaben-Icon'); d['icon'] = {'count': 1, 'id': icon}
            if title: self.lang[f'task.{tid}.title'] = title
            return d
        if t[0] == 'checkmark': return {'id': tid, 'type': 'checkmark'}
        if t[0] == 'dimension':
            if t[1] not in BEKANNTE_DIMENSIONEN: self.errors.append(f'{c.key}/{q.key}: unbekannte Dimension {t[1]}')
            return {'dimension': t[1], 'id': tid, 'type': 'dimension'}
        if t[0] == 'kill':
            if t[1] not in BEKANNTE_MOBS: self.errors.append(f'{c.key}/{q.key}: unbekannter Mob {t[1]} (in BEKANNTE_MOBS eintragen)')
            return {'entity': t[1], 'id': tid, 'type': 'kill', 'value': L(t[2])}
        # 26.10.2026: max_input MUSS gesetzt sein. FTB Quests 2101.1.37 liest fehlendes max_input als 0 (EnergyTask.readData,
        # getLong), dann nimmt der Aufgabenbildschirm keinen Strom an (TaskEnergyHandler.receiveEnergy: min(maxInput, …)).
        # Wert = Ziel, also keine künstliche Drossel: Wie schnell es geht, bestimmt das Stromnetz des Spielers.
        if t[0] == 'forge_energy': return {'id': tid, 'max_input': L(t[1]), 'type': 'forge_energy', 'value': L(t[1])}
        if t[0] == 'observation':
            self.check_item(t[1], f'{c.key}/{q.key} Beobachten')      # Block mit Item, steht deshalb in items.json
            return {'id': tid, 'observation_type': 'block', 'observe_type': 0, 'timer': L(t[2]), 'to_observe': t[1],
                    'type': 'observation'}
        if t[0] == 'advancement':
            ns, pfad = t[1].split(':', 1)
            datei = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'kubejs', 'data', ns, 'advancement', pfad + '.json')
            if ns == 'skyandstone' and not os.path.exists(datei):
                self.errors.append(f'{c.key}/{q.key}: Advancement {t[1]} fehlt ({datei})')
            return {'advancement': t[1], 'criterion': '', 'id': tid, 'type': 'advancement'}
        raise ValueError(t)

    def _reward(self, c, q, n, r):
        rid = hid('reward', c.key, q.key, str(n))
        if r[0] == 'xp': return {'id': rid, 'type': 'xp', 'xp': r[1]}
        if r[0] == 'command':  # Befehl als Spieler mit Berechtigung 2: @s ist der Spieler, /function läuft
            return {'id': rid, 'type': 'command', 'command': r[1], 'permission_level': 2, 'silent': True}
        if r[0] == 'give':
            self.check_item(r[1], f'{c.key}/{q.key} Belohnung')
            d = {'id': rid, 'item': {'count': 1, 'id': r[1]}, 'type': 'item'}
            if len(r) > 3 and r[3]: d['item']['components'] = dict(r[3])
            if r[2] != 1: d['count'] = r[2]
            return d
        if r[0] == 'table':
            if r[1] not in self.tables: self.errors.append(f'{q.key}: Tabelle {r[1]} fehlt'); return None
            art = r[3] if len(r) > 3 else 'random'
            if art not in ('loot', 'choice', 'random', 'all_table'): raise ValueError(art)
            d = {'id': rid, 'table_id': L(int(self.tables[r[1]][0], 16)), 'type': art}
            if len(r) > 2 and r[2]: d['team_reward'] = True
            return d
        raise ValueError(r)

    def chapter(self, c, group_id, order):
        cid = hid('chapter', c.key)
        self.lang[f'chapter.{cid}.title'] = c.title
        if c.sub: self.lang[f'chapter.{cid}.chapter_subtitle'] = c.sub if isinstance(c.sub, list) else [c.sub]
        link_pos = auto_layout(c)
        self.check_item(c.icon, f'Kapitel {c.key} Icon')
        quests = []
        for q in c.quests:
            qid = self.qids[q.key]
            self.lang[f'quest.{qid}.title'] = q.title
            if q.sub: self.lang[f'quest.{qid}.quest_subtitle'] = q.sub
            if q.desc: self.lang[f'quest.{qid}.quest_desc'] = q.desc
            d = {}
            deps = []
            for k in q.deps:
                if k not in self.qids: self.errors.append(f'{q.key}: Abhängigkeit {k} fehlt'); continue
                deps.append(self.qids[k])
            if deps: d['dependencies'] = deps
            if q.dep_any and len(deps) > 1: d['dependency_requirement'] = 'one_completed'
            if q.icon:
                self.check_item(q.icon, f'{q.key} Icon'); d['icon'] = {'count': 1, 'id': q.icon}
            d['id'] = qid
            if q.optional: d['optional'] = True
            if q.repeat: d['can_repeat'] = True; d['repeat_cooldown'] = int(q.repeat)
            rewards = [r for r in (self._reward(c, q, n, r) for n, r in enumerate(q.rewards)) if r]
            if rewards: d['rewards'] = rewards
            if q.shape: d['shape'] = q.shape
            if q.size: d['size'] = D(q.size)
            d['tasks'] = [self._task(c, q, n, t) for n, t in enumerate(q.tasks)]
            d['x'] = D(q.x); d['y'] = D(q.y)
            quests.append(d)
        links = []
        for k, (x, y) in link_pos.items():
            if k not in self.qids: self.errors.append(f'Kapitel {c.key}: Verweis auf unbekannte Quest {k}'); continue
            links.append({'id': hid('link', c.key, k), 'linked_quest': self.qids[k], 'shape': 'square', 'size': D(1.0), 'x': D(x), 'y': D(y)})
        data = {'default_hide_dependency_lines': False, 'default_quest_shape': '', 'filename': c.key,
                'group': group_id, 'icon': {'count': 1, 'id': c.icon}, 'id': cid, 'order_index': order,
                'quest_links': links, 'quests': quests}
        return data

    def write(self, groups, chapters, file_title, vorfehler=()):
        """Erst alles erzeugen und prüfen, dann schreiben. Bei Fehlern bleibt der alte Stand auf der Platte
        (Nachtschicht 0.6.3: vorher stand ein unbekanntes Item trotz FEHLER in der SNBT)."""
        self.register(chapters)
        qdir = os.path.join(self.out, 'quests')
        out = {}                       # Pfad -> Daten
        gids = {}
        glist = []
        for g_key, g_title in groups:
            gid = hid('group', g_key); gids[g_key] = gid
            glist.append({'id': gid}); self.lang[f'chapter_group.{gid}.title'] = g_title
        import ftbformat as FF
        out[os.path.join(qdir, 'chapter_groups.snbt')] = FF.gruppen([g['id'] for g in glist])
        import layoutcheck as LC
        namen = {v: k for k, v in self.qids.items()}
        self.layout = {}
        je_gruppe = {}
        for n, c in enumerate(chapters):
            data = self.chapter(c, gids[c.group], n)
            idx = je_gruppe.get(c.group, 0); je_gruppe[c.group] = idx + 1
            out[os.path.join(qdir, 'chapters', c.key + '.snbt')] = FF.kapitel(data, idx)
            r = LC.pruefe(data, namen)
            self.layout[c.key] = r
            for a, b, x in r['durch']: self.hinweise.append(f'Layout {c.key}: Linie {a} -> {b} läuft durch {x}')
            for a, b in r['ueberlappt']: self.hinweise.append(f'Layout {c.key}: {a} und {b} überlappen sich')
        for i, name in enumerate(sorted(self.tables)):
            out[os.path.join(qdir, 'reward_tables', name + '.snbt')] = FF.tabelle(self.tables[name][1], i)
        self.lang['file.0000000000000001.title'] = file_title   # die Questdatei hat in FTB Quests immer die ID 1
        out[os.path.join(qdir, 'data.snbt')] = FF.daten({
            'default_autoclaim_rewards': 'disabled', 'default_consume_items': False, 'default_quest_disable_jei': False,
            'default_quest_shape': 'circle', 'default_reward_team': False, 'detection_delay': 20,
            'disable_gui': False, 'drop_book_on_death': False, 'drop_loot_crates': True, 'loot_crate_no_drop': {'boss': 0, 'monster': 1000, 'passive': 4000}, 'emergency_items_cooldown': 300,
            'fallback_locale': 'de_de', 'grid_scale': D(0.5), 'hide_excluded_quests': False, 'id': hid('file'),
            'lock_message': '', 'pause_game': False, 'progression_mode': 'flexible', 'show_lock_icons': True, 'version': 13}, D)
        # Deutsch als Hauptsprache, Englisch als Rückfall mit gleichem Text
        for loc in ('de_de', 'en_us'):
            out[os.path.join(qdir, 'lang', loc + '.snbt')] = dict(sorted(self.lang.items()))
        errors = list(vorfehler) + self.errors
        if errors: return errors       # nichts schreiben
        for sub in ('chapters', 'reward_tables', 'lang'):
            d = os.path.join(qdir, sub); os.makedirs(d, exist_ok=True)
            for f in os.listdir(d):
                if f.endswith('.snbt'): os.remove(os.path.join(d, f))
        for path, data in out.items():
            if os.sep + 'lang' + os.sep in path: self._w(path, data)      # Sprachdateien schreibt FTB nicht neu
            else:
                with open(path, 'w', encoding='utf-8', newline='') as f: f.write(FF.text(data))
        return errors

    @staticmethod
    def _w(path, data):
        with open(path, 'w', encoding='utf-8', newline='\n') as f: f.write(snbt(data) + '\n')

"""Prüft das Questbuch-Layout so, wie FTB Quests es zeichnet (0.6.4).
Linien: gerade Strecken von jeder Voraussetzung zur Quest. Liegt die Voraussetzung in einem anderen Kapitel,
startet die Linie am Verweis (quest_link) – fehlt der Verweis, gibt es keine Linie.
Gemeldet wird: Linie läuft durch eine fremde Quest, Quests überlappen sich, Linien kreuzen sich.
"""
import math

RAND = 0.15   # Abstand, den eine Linie zum Rand einer fremden Quest mindestens halten soll

def _knoten(ch):
    k = {}   # quest-id -> (x, y, radius)
    for q in ch['quests']:
        k[q['id']] = (float(q['x']), float(q['y']), float(q.get('size', 1.0)) / 2)
    for l in ch['quest_links']:
        k.setdefault(l['linked_quest'], (float(l['x']), float(l['y']), float(l.get('size', 1.0)) / 2))
    return k

def kanten(ch):
    k = _knoten(ch)
    out = []
    for q in ch['quests']:
        for d in q.get('dependencies', []):
            if d in k: out.append((d, q['id']))
    return k, out

def _abstand(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    l2 = dx * dx + dy * dy
    t = 0 if l2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / l2))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))

def _kreuzen(p1, p2, p3, p4):
    def o(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    d1, d2, d3, d4 = o(p3, p4, p1), o(p3, p4, p2), o(p1, p2, p3), o(p1, p2, p4)
    return (d1 * d2 < -1e-9) and (d3 * d4 < -1e-9)

def pruefe(ch, namen=None):
    """-> dict mit Listen 'durch', 'ueberlappt', 'kreuzt'. namen: id -> lesbarer Schlüssel."""
    n = namen or {}
    k, ks = kanten(ch)
    res = {'durch': [], 'ueberlappt': [], 'kreuzt': []}
    ids = list(k)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            ax, ay, ar = k[a]; bx, by, br = k[b]
            if math.hypot(ax - bx, ay - by) < ar + br - 0.05: res['ueberlappt'].append((n.get(a, a), n.get(b, b)))
    for a, b in ks:
        ax, ay, _ = k[a]; bx, by, _ = k[b]
        for c, (cx, cy, cr) in k.items():
            if c in (a, b): continue
            if _abstand(cx, cy, ax, ay, bx, by) < cr + RAND: res['durch'].append((n.get(a, a), n.get(b, b), n.get(c, c)))
    for i, (a, b) in enumerate(ks):
        for c, d in ks[i + 1:]:
            if len({a, b, c, d}) < 4: continue
            if _kreuzen(k[a][:2], k[b][:2], k[c][:2], k[d][:2]): res['kreuzt'].append(((n.get(a, a), n.get(b, b)), (n.get(c, c), n.get(d, d))))
    return res

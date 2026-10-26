"""Schreibt Questdateien genau so, wie FTB Quests 2101.1.37 sie selbst speichert (0.7.0).

Grund: FTB Quests speichert beim ersten Welt-Save alle Kapitel, Tabellen, Gruppen und data.snbt neu.
Weichen die Bytes vom Pack ab, stimmen die Hashes nicht mehr, und packwiz-installer stellt die Datei
später nicht wieder her (er prüft nur seinen Cache gegen den Index). Mit identischem Format ist das egal.
Regeln ermittelt aus Instanzdateien und Bytecode (Audit E, 25.10.2026), 25/25 Dateien byte-gleich.
lang/*.snbt schreibt FTB nicht neu – dafür bleibt der alte Schreiber in questlib.py.
"""
import json, re

class Byte(int): pass         # 1b
class Single(dict): pass      # Compound, den FTB in einer Zeile schreibt: { a: 1, b: "x" }

def _key(k):
    return k if re.fullmatch(r'[A-Za-z0-9_.+-]+', k) else json.dumps(k, ensure_ascii=False)

def _num(v):
    n = type(v).__name__
    if isinstance(v, bool): return 'true' if v else 'false'
    if n == 'Byte': return f'{int(v)}b'
    if n == 'D': return f'{float(v)}d'
    if n == 'F': return f'{float(v)}f'
    if n == 'L': return f'{int(v)}L'
    if isinstance(v, int): return str(v)
    if isinstance(v, float): return f'{v}d'
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    raise TypeError(type(v))

def w(v, ind=0):
    """Schlüssel alphabetisch, Tabs, Listen mit 1 Element inline, ab 2 Elementen mehrzeilig."""
    p = '\t' * ind
    if isinstance(v, Single):
        return '{ ' + ', '.join(f'{_key(k)}: {w(v[k], ind)}' for k in sorted(v)) + ' }'
    if isinstance(v, dict):
        if not v: return '{ }'
        return '{\n' + ''.join(f'{p}\t{_key(k)}: {w(v[k], ind + 1)}\n' for k in sorted(v)) + p + '}'
    if isinstance(v, list):
        if not v: return '[ ]'
        if len(v) == 1: return '[' + w(v[0], ind) + ']'
        return '[\n' + ''.join(f'{p}\t{w(x, ind + 1)}\n' for x in v) + p + ']'
    return _num(v)

def text(d):
    """Dateiinhalt mit CRLF und Zeilenumbruch am Ende (wie FTB)."""
    return (w(d) + '\n').replace('\n', '\r\n')

def _icon(d):
    d = dict(d)
    if d.get('count') == 1: d.pop('count')
    return d

def _single(d):
    return Single({k: (_single(x) if isinstance(x, dict) else x) for k, x in d.items()})

def _task(t):
    t = dict(t)
    if 'item' in t: t['item'] = _single(t['item'])
    if 'icon' in t: t['icon'] = _icon(t['icon'])
    return t

def _reward(r, in_table=False):
    r = dict(r)
    if r.get('count') == 1: r.pop('count')
    if in_table and r.get('type') == 'item': r.pop('type')
    return r

def kapitel(c, order_index):
    c = dict(c)
    c['icon'] = _icon(c['icon'])
    c.setdefault('images', [])
    c['order_index'] = order_index          # Index innerhalb der eigenen Gruppe
    links = []
    for l in c.get('quest_links', []):
        l = dict(l)
        if float(l.get('size', 1.0)) == 1.0: l.pop('size', None)
        links.append(l)
    c['quest_links'] = links
    qs = []
    for q in c['quests']:
        q = dict(q)
        if 'icon' in q: q['icon'] = _icon(q['icon'])
        if 'tasks' in q: q['tasks'] = [_task(t) for t in q['tasks']]
        if 'rewards' in q: q['rewards'] = [_reward(r) for r in q['rewards']]
        qs.append(q)
    c['quests'] = qs
    return c

def tabelle(t, order_index):
    t = dict(t)
    t['order_index'] = order_index          # alphabetische Reihenfolge der Dateinamen
    t['rewards'] = [_reward(r, True) for r in t['rewards']]
    lc = t.get('loot_crate')
    if lc:
        lc = dict(lc)
        if lc.get('glow') is False: lc.pop('glow')
        elif lc.get('glow') is True: lc['glow'] = Byte(1)
        if lc.get('item_name') == '': lc.pop('item_name')
        t['loot_crate'] = lc
    return t

def daten(d, D):
    d = dict(d)
    d.pop('id', None)                       # FTB liest kein id aus data.snbt, die Datei hat immer ID 1
    d['presets'] = {'goal': {'shape': 'hexagon', 'size': D(2.0)}, 'info': {'shape': 'gear', 'size': D(1.0)},
                    'normal': {'shape': 'square', 'size': D(1.0)}}
    d['verify_on_load'] = False
    return d

def gruppen(ids):
    return {'chapter_groups': [Single({'id': g}) for g in ids]}

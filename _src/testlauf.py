# Sky and Stone: Testserver-Lauf mit Log-Prüfung (Pflichtprüfung aus CLAUDE.md, Teil „Testserver“).
# Aufruf (aus dem Pack-Ordner): python -I -X utf8 _src/testlauf.py [--ohne-sync] [--warten 20] [--befehl "..."]...
#   1. packwiz-installer synchronisiert den Testserver mit diesem Ordner (außer --ohne-sync)
#   2. Server startet mit Java 21, Eingabe über eine Pipe (so lässt er sich immer mit „stop“ beenden)
#   3. nach „Done (“ wartet das Skript --warten Sekunden (Dumps), schickt die --befehl-Zeilen und dann „stop“
#   4. Auswertung von logs/latest.log und logs/kubejs/*.log, Bericht _src/pruefung/bericht/TESTLAUF.md
# Exit 0 = alle Pflichtpunkte grün. Der Server läuft danach NICHT weiter.
import datetime
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(HERE)
SERVER = os.path.join(os.path.dirname(PACK), '_testserver-sky-and-stone')
JAVA = r'C:\Program Files\Microsoft\jdk-21.0.12.101-hotspot\bin\java.exe'
PACK_URL = 'file:///' + os.path.join(PACK, 'pack.toml').replace('\\', '/')
BERICHT = os.path.join(HERE, 'pruefung', 'bericht', 'TESTLAUF.md')

# Bekannte, begründete Log-Meldungen (TEST_REPORT.md / PROJECT_AUDIT.md). Alles andere mit ERROR ist ein Befund.
BEKANNT = [
    (r'\[Curios API/\]: (example|feet) is not a registered slot type', 'Curios-Slots aus Industrial Foregoing, harmlos'),
]


def lese_quests_soll():
    """Soll-Werte aus den Questdateien, die der Generator geschrieben hat."""
    q = os.path.join(PACK, 'config', 'ftbquests', 'quests')
    kap = [f for f in os.listdir(os.path.join(q, 'chapters')) if f.endswith('.snbt')]
    tab = [f for f in os.listdir(os.path.join(q, 'reward_tables')) if f.endswith('.snbt')]
    sys.path.insert(0, HERE)
    import snbt
    n = sum(len(snbt.load(os.path.join(q, 'chapters', f)).get('quests', [])) for f in kap)
    return len(kap), n, len(tab)


def sync():
    cmd = [JAVA, '-jar', 'packwiz-installer-bootstrap.jar', '-g', '-s', 'server', PACK_URL]
    r = subprocess.run(cmd, cwd=SERVER, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=600)
    return r.returncode, (r.stdout + r.stderr)[-2000:]


def starte_server(warten, befehle, timeout=420):
    log = os.path.join(SERVER, 'logs', 'latest.log')
    start = time.time()
    args = [JAVA, '@user_jvm_args.txt', '@libraries/net/neoforged/neoforge/21.1.264/win_args.txt', 'nogui']
    out = open(os.path.join(SERVER, 'logs', 'testlauf-konsole.txt'), 'w', encoding='utf-8', errors='replace')
    p = subprocess.Popen(args, cwd=SERVER, stdin=subprocess.PIPE, stdout=out, stderr=subprocess.STDOUT, text=True)
    status = 'timeout'
    while time.time() - start < timeout:
        time.sleep(2)
        if p.poll() is not None:
            status = f'beendet mit Code {p.returncode} vor „Done“'
            break
        if os.path.exists(log) and os.path.getmtime(log) >= start - 1:
            text = open(log, encoding='utf-8', errors='replace').read()
            if 'Done (' in text:
                status = 'done'
                break
    if status == 'done':
        time.sleep(warten)
        for b in befehle:
            p.stdin.write(b + '\n'); p.stdin.flush(); time.sleep(3)
    if p.poll() is None:
        p.stdin.write('stop\n'); p.stdin.flush()
        try:
            p.wait(timeout=120)
        except subprocess.TimeoutExpired:
            p.kill()            # eigener Kindprozess, nur wenn „stop“ nach 2 min nicht greift
            status += ' (stop hing, Prozess beendet)'
    out.close()
    return status, time.time() - start


def werte_aus(soll):
    log = open(os.path.join(SERVER, 'logs', 'latest.log'), encoding='utf-8', errors='replace').read()
    kj = {}
    for n in ('startup', 'server'):
        f = os.path.join(SERVER, 'logs', 'kubejs', n + '.log')
        kj[n] = open(f, encoding='utf-8', errors='replace').read() if os.path.exists(f) else ''
    punkte = []   # (Name, ok, Detail)

    m = re.search(r'Done \(([\d.,]+)s\)', log)
    punkte.append(('Serverstart „Done“', bool(m), m.group(0) if m else 'kein Done im Log'))
    for art in ('startup', 'server'):
        m = re.findall(rf'Loaded (\d+)/(\d+) KubeJS {art} scripts in [\d.,]+ s with (\d+) errors and (\d+) warnings', log)
        if not m:
            punkte.append((f'KubeJS {art}', False, 'keine Ladezeile')); continue
        a, b, e, w = map(int, m[-1])
        punkte.append((f'KubeJS {art}', a == b and e == 0, f'{a}/{b} Skripte, {e} Fehler, {w} Warnungen'))
    m = re.findall(r'with (\d+) failed recipes', log)
    punkte.append(('Rezepte', bool(m) and m[-1] == '0', f'{m[-1]} fehlgeschlagene Rezepte' if m else 'keine Rezeptzeile'))
    m = re.search(r'Loaded (\d+) chapter groups, (\d+) chapters, (\d+) quests, (\d+) reward tables', log)
    if m:
        ist = (int(m.group(2)), int(m.group(3)), int(m.group(4)))
        punkte.append(('Questbuch', ist == soll, f'{ist[0]} Kapitel, {ist[1]} Quests, {ist[2]} Tabellen (Soll {soll[0]}/{soll[1]}/{soll[2]})'))
    else:
        punkte.append(('Questbuch', False, 'FTB Quests hat nichts geladen'))

    fehler, bekannt = [], []
    for z in log.splitlines():
        if '/ERROR]' not in z and '/FATAL]' not in z: continue
        grund = next((g for muster, g in BEKANNT if re.search(muster, z)), None)
        (bekannt if grund else fehler).append((z.strip(), grund))
    for n, t in kj.items():
        for z in t.splitlines():
            if '[ERROR]' in z: fehler.append((f'kubejs/{n}.log: {z.strip()}', None))
    punkte.append(('ERROR-Zeilen', not fehler, f'{len(fehler)} neu, {len(bekannt)} bekannt'))
    return punkte, fehler, bekannt


def main():
    args = sys.argv[1:]
    warten = int(args[args.index('--warten') + 1]) if '--warten' in args else 20
    befehle = [args[i + 1] for i, a in enumerate(args) if a == '--befehl']
    soll = lese_quests_soll()
    zeilen = [f'# Testlauf Sky and Stone', '', f'Stand: {datetime.datetime.now():%d.%m.%Y %H:%M} · Java 21 · Server `{SERVER}`', '']
    if '--ohne-sync' not in args:
        code, text = sync()
        print('Sync:', 'ok' if code == 0 else f'Fehler {code}')
        zeilen += [f'- Sync (packwiz-installer): {"ok" if code == 0 else "FEHLER " + str(code)}']
        if code != 0:
            print(text); zeilen += ['```', text, '```']
            open(BERICHT, 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n'); return 1
    status, dauer = starte_server(warten, befehle)
    print(f'Server: {status} ({dauer:.0f} s)')
    zeilen += [f'- Lauf: {status}, {dauer:.0f} s, Befehle: {len(befehle)}', '']
    punkte, fehler, bekannt = werte_aus(soll)
    zeilen += ['| Prüfpunkt | Ergebnis | Detail |', '|---|---|---|']
    for name, ok, det in punkte:
        print(f'  {"OK  " if ok else "FEHL"} {name}: {det}')
        zeilen.append(f'| {name} | {"OK" if ok else "FEHLER"} | {det} |')
    if fehler:
        zeilen += ['', '## Neue ERROR-Zeilen', ''] + [f'- `{z[:300]}`' for z, _ in fehler[:40]]
        for z, _ in fehler[:10]: print('  ERROR:', z[:200])
    if bekannt:
        zeilen += ['', '## Bekannte Meldungen', ''] + sorted({f'- {g}' for _, g in bekannt})
    zeilen += ['', 'Im Spiel NICHT GETESTET: Der Lauf prüft nur Laden und Log, keine Spielmechanik.']
    open(BERICHT, 'w', encoding='utf-8', newline='\n').write('\n'.join(zeilen) + '\n')
    print('Bericht:', os.path.relpath(BERICHT, PACK))
    return 0 if status.startswith('done') and all(ok for _, ok, _ in punkte) else 1


if __name__ == '__main__':
    sys.exit(main())

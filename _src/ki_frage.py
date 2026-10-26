# Zweitmeinung über das lokale KI-Gateway FreeLLMAPI (http://127.0.0.1:31415, OpenAI-kompatibel).
# Aufruf: python -I -X utf8 _src/ki_frage.py "Frage" [-f datei]... [-m auto|fusion|auto:coding] [-s "System"] [-o antwort.md]
# Key: Umgebungsvariable FREELLMAPI_API_KEY, sonst ANTHROPIC_AUTH_TOKEN aus ~/.claude/settings.json (wird nie ausgegeben).
# Antworten sind Vorschläge: vor der Übernahme gegen Log oder Mod-Code prüfen (CLAUDE.md, Grenzen).
import json
import os
import sys
import time
import urllib.error
import urllib.request

URL = 'http://127.0.0.1:31415/v1/chat/completions'


def key():
    k = os.environ.get('FREELLMAPI_API_KEY')
    if k: return k
    s = json.load(open(os.path.expanduser('~/.claude/settings.json'), encoding='utf-8'))
    return s.get('env', {}).get('ANTHROPIC_AUTH_TOKEN', '')


def frage(text, dateien=(), modell='auto', system=None, timeout=300, versuche=3):
    teile = [text]
    for d in dateien:
        teile.append(f'\n\n===== Datei: {os.path.basename(d)} =====\n' + open(d, encoding='utf-8', errors='replace').read())
    msgs = ([{'role': 'system', 'content': system}] if system else []) + [{'role': 'user', 'content': ''.join(teile)}]
    body = json.dumps({'model': modell, 'messages': msgs, 'temperature': 0.3}).encode('utf-8')
    letzter = None
    for i in range(versuche):
        req = urllib.request.Request(URL, data=body, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key()})
        try:
            t = time.time()
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.load(r)
            return d['choices'][0]['message']['content'], d.get('model', modell), time.time() - t
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            letzter = e
            time.sleep(5 * (i + 1))   # Gateway wechselt beim nächsten Versuch den Anbieter (Fallback-Kette)
    raise SystemExit(f'Gateway-Fehler nach {versuche} Versuchen: {letzter}')


def main():
    a = sys.argv[1:]
    if not a: print(__doc__ or 'Aufruf siehe Kopf der Datei'); return 2
    dateien, modell, system, ausgabe, text = [], 'auto', None, None, []
    i = 0
    while i < len(a):
        if a[i] == '-f': dateien.append(a[i + 1]); i += 2
        elif a[i] == '-m': modell = a[i + 1]; i += 2
        elif a[i] == '-s': system = a[i + 1]; i += 2
        elif a[i] == '-o': ausgabe = a[i + 1]; i += 2
        else: text.append(a[i]); i += 1
    antwort, wer, dauer = frage(' '.join(text), dateien, modell, system)
    kopf = f'<!-- FreeLLMAPI, Modell {wer}, {dauer:.0f} s -->\n'
    if ausgabe:
        open(ausgabe, 'w', encoding='utf-8', newline='\n').write(kopf + antwort + '\n')
        print(f'Antwort ({wer}, {dauer:.0f} s) in {ausgabe}')
    else:
        print(kopf + antwort)
    return 0


if __name__ == '__main__':
    sys.exit(main())

# Sky and Stone: prüft, ob die IDs im Questbuch gegenüber einem Referenzstand gleich geblieben sind.
# Quest-, Aufgaben- und Belohnungs-IDs hängen am Fortschritt bestehender Welten (Einzelheiten: pruefung/idvergleich.py).
# Aufruf: python -I -X utf8 _src/idcheck.py [Referenz]
#   Referenz: Sicherungsordner (irgendwo darin chapters/*.snbt) oder .mrpack/.zip.
#   Ohne Angabe: das neueste „Sky and Stone-<Version>.mrpack“ im Pack-Ordner (Stand, den Spieler haben).
# Exit 1, wenn eine Quest-ID entfallen ist oder eine ID die Objektart wechselt.
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pruefung import idvergleich, modell  # noqa: E402

PACK = os.path.dirname(HERE)


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else idvergleich.neuestes_mrpack(PACK)
    if not ref:
        print('Keine Referenz: kein .mrpack im Pack-Ordner und kein Pfad angegeben.')
        return 2
    alt = idvergleich.lade_referenz(ref)
    neu = modell.lade(os.path.join(PACK, 'config', 'ftbquests'))
    befunde = idvergleich.vergleiche(alt, neu)
    print(f'Referenz: {ref}')
    print(f'Referenz: {len(alt.quests)} Quests, aktuell: {len(neu.quests)} Quests')
    neue = sorted(set(neu.quests) - set(alt.quests))
    print(f'Neu: {len(neue)} Quests' + (': ' + ', '.join(neu.name(q) for q in neue) if neue else ''))
    for stufe in ('FEHLER', 'WARNUNG', 'HINWEIS'):
        for b in befunde:
            if b.stufe == stufe:
                print(f'{stufe}: {b.text}')
    n = sum(b.stufe == 'FEHLER' for b in befunde)
    print(f'{n} Fehler, {sum(b.stufe == "WARNUNG" for b in befunde)} Warnungen')
    return 1 if n else 0


if __name__ == '__main__':
    sys.exit(main())

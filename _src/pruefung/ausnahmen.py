"""Bewusst akzeptierte Befunde. Jede Ausnahme braucht einen Grund mit Beleg (Entscheidung, Changelog, Spieltest).

Ein Befund, auf den eine Ausnahme passt, erscheint im Bericht unter „Akzeptiert“ statt bei den offenen Befunden.
Trifft eine Ausnahme nichts mehr, meldet der Bericht sie als veraltet: dann hier löschen.
"""
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Ausnahme:
    bereich: str
    muster: str          # regulärer Ausdruck auf den Befundtext
    grund: str


LISTE = [
    Ausnahme('Spiellogik', r'Willkommen in der Leere.*Belohnung .*\(exdeorum:silkworm\)',
             'Seidenraupe als Startbelohnung bewusst, weil Faden aus dem Laub zu langsam ist (Vault Modpack-Werkstatt, 0.6.3)'),
    Ausnahme('Texte', r'„Willkommen in der Leere“ \(akt1\): \d+ Zeilen',
             'Start-Quest bündelt das Tutorial (Questbuch, Handbuch, Belohnungen, Markt, Jobs+, Team, Welttyp); Entscheidung 26.10.2026'),
    Ausnahme('Texte', r'„Erz ohne Sieb“ \(akt3\): \d+ Zeilen',
             'Wahl-Quest listet drei Wege samt Belohnungs-Quests; kürzer wird die Wahl unverständlich (26.10.2026)'),
]


def anwenden(befunde, liste=None):
    liste = LISTE if liste is None else liste
    offen, akzeptiert = [], []
    for b in befunde:
        a = next((a for a in liste if a.bereich == b.bereich and re.search(a.muster, b.text)), None)
        if a:
            akzeptiert.append((b, a))
        else:
            offen.append(b)
    return offen, akzeptiert


def unbenutzt(liste, akzeptiert):
    benutzt = {a for _, a in akzeptiert}
    return [a for a in liste if a not in benutzt]

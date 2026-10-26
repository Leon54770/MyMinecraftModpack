"""Ein Befund einer Prüfung. FEHLER = sicher falsch, WARNUNG = sehr wahrscheinlich ein Problem
(oft aus einem Modell, das Lücken haben kann), HINWEIS = zur Kenntnis, kein Handlungsbedarf erzwungen."""
from dataclasses import dataclass

STUFEN = ('FEHLER', 'WARNUNG', 'HINWEIS')


@dataclass(frozen=True)
class Befund:
    stufe: str
    bereich: str
    text: str

    def __post_init__(self):
        if self.stufe not in STUFEN:
            raise ValueError(self.stufe)


def fehler(bereich, text):
    return Befund('FEHLER', bereich, text)


def warnung(bereich, text):
    return Befund('WARNUNG', bereich, text)


def hinweis(bereich, text):
    return Befund('HINWEIS', bereich, text)


class Register:
    """Was es im Spiel gibt (aus den Testserver-Dumps). None = unbekannt, dann wird die Prüfung übersprungen."""

    def __init__(self, items, tags, entities=None, dimensionen=None, stapel=None, fluide=None, bloecke=None):
        self.items = set(items)
        self.tags = {k.lstrip('#'): list(v) for k, v in dict(tags).items()}
        self.entities = set(entities) if entities is not None else None
        self.dimensionen = set(dimensionen) if dimensionen is not None else None
        self.stapel = dict(stapel) if stapel is not None else None
        self.fluide = set(fluide) if fluide is not None else None
        self.bloecke = set(bloecke) if bloecke is not None else None

    def stapelgroesse(self, item):
        if self.stapel is None:
            return None
        return self.stapel.get(item)

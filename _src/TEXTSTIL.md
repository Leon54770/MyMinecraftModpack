# Textstil für das Questbuch (ab 0.6.4)

Stand: 25.10.2026 · Gilt für Quest-Titel, Beschreibungen, Kapitel und Story-Notizen. Texte stehen in `_src/texte_*.py`.

## Ton
- Wie das Quest-Log eines guten Abenteuerspiels: knapp, klar, mit einem Hauch Dungeon-Atmosphäre (Leere, Splitter, Ruinen der Erbauer, Wächter). Nie kitschig.
- Du-Form, Deutsch, kurze Sätze. Erst kurz Stimmung, dann klare Anweisung.
- Keine KI-Floskeln: kein „Perfekt!“, „Geschafft!“, „Ab jetzt …“, „Das Herz jeder …“, „nicht nur … sondern auch“, „Willkommen in der Welt von …“, keine Ausrufezeichen-Ketten, keine Emojis, kein „magisch“ als Füllwort, keine Gedankenstrich-Kaskaden.
- Keine erfundenen Zahlen oder Mechaniken. Alles Mechanische aus dem alten Text bleibt erhalten (Chancen, Rezepte, Warnungen, Tipps), nur besser formuliert.

## Titel
- 1–4 Wörter, sagen, worum es geht, und klingen nach Spiel: „Das erste Sieb“, „Feuer ohne Nether“, „Funken aus Kupfer“.
- Kein Doppelpunkt-Stil („Sammlerbuch: Alle Essenzen“ → „Alle Essenzen“), kein reiner Itemname, wenn ein besserer Titel geht.
- Meilensteine (Zahnrad) dürfen etwas epischer sein: „Der Funke“, „Die erste Maschine“.

## Beschreibung (Liste von Zeilen)
1. Eine Zeile Stimmung (höchstens ~12 Wörter).
2. Leerzeile `''`.
3. 1–3 Zeilen: was zu tun ist und wie.
4. Optional eine Zeile `Tipp: …`
- Höchstens 6 Zeilen. Mod-Kapitel dürfen etwas mehr erklären als die Hauptstory.
- Wichtige Items einmal mit `&e…&r` hervorheben. `&l` sparsam, `&c` nur für Warnungen.
- **Keine Zeile darf mit `&o` beginnen** (reserviert für Story-Notizen).

## Item-Namen
- Genau so schreiben, wie sie im Spiel heißen: Deutsch, wenn die Mod eine deutsche Übersetzung hat, sonst Englisch. Nachschlagen in `_src/namen.json` (Item-ID → Anzeigename).
- Beispiele: `Oak Sieve`, `Crook`, `Silkworm`, `String Mesh`, `Energizing Orb`, `Loot Fabricator` (englisch, weil ohne Übersetzung) · `Lohenbrenner`, `Eisenbarren`, `Tertiumessenz`, `ME-Controller` (deutsch).
- Nie selbst übersetzen. Allgemeine Begriffe (Kies, Erde, Sieb, Strom) dürfen deutsch bleiben, wenn kein bestimmtes Item gemeint ist.

## Belohnungen
- Werden im Questbuch selbst abgeholt (nicht mehr automatisch). Nicht schreiben „landet direkt bei dir“.

## Beispiel
```python
'e_sieb': ('Das erste Sieb', [
    'Was die Leere verschluckt hat, gibt das Sieb zurück.',
    '',
    'Stell ein Sieb auf, setz ein &eString Mesh&r ein und leg Erde, Kies oder Sand darauf. Dann Rechtsklick halten.',
    'Tipp: Bis zu 5×5 Siebe nebeneinander siebst du mit einem Klick gleichzeitig.']),
```
Story-Notiz (Tagebuchseite des letzten Wächters, ein bis zwei Sätze, in „…“):
```python
'e_eisen': ('Der Funke', '„Das erste Metall. Wir nannten es den Funken, weil danach alles schneller brannte.“'),
```

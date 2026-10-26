# Prüfbericht Sky and Stone

Stand: 26.10.2026 15:02 · Dauer 2 s · 0 Fehler, 0 Warnungen, 18 Hinweise, 2 akzeptiert

Erzeugt von `_src/pruefen.py`. WARNUNG aus der Spiellogik beruht auf dem Rezeptmodell (Dumps vom Testserver): im Spiel gegenprüfen, bevor etwas geändert wird.

## Kennzahlen

- Kistenchance je Kill: monster 1.09 %, passive 0.07 %, boss 100.00 %

## HINWEIS (18)

### Belohnungen

- Belohnung aus „Der Gärtnergeist“ (ars) (8× minecraft:wheat_seeds) erfüllt sofort alle Aufgaben von „Was in der Erde steckt“ (landwirtschaft)

### Questbuch

- Kapitel ae2: 1 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Elektrolyse“ (mekanism)
- Kapitel akt2: 12 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Der Funke“ (akt1), „Der Infusionsaltar“ (akt1), „Feuer aus Stein“ (akt1), „Messing“ (akt1), „Splitter der Erde“ (akt1), „Stufe 2: Prudentium“ (akt1), „Waschen mit Wind“ (akt1)
- Kapitel akt3: 9 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Das Herz schlägt“ (akt4), „Das ME-Netz“ (akt2), „Die zerbrochene Unterwelt“ (akt2), „Infundierte Legierung“ (akt2), „Lohenruten“ (akt2), „Obsidian“ (akt2), „Prozessoren“ (akt2), „Stufe 3: Tertium“ (akt2), „Vierfach-Erz“ (akt2)
- Kapitel akt4: 7 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Der Wither“ (akt3), „Der Wächter am Ende“ (akt3), „Enderperlen“ (akt3), „Stufe 4: Imperium“ (akt3), „Vier von Sieben“ (akt2)
- Kapitel ars: 2 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Der Wither“ (akt3), „Die Chimera“ (pruefungen)
- Kapitel bau: 2 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Der Funke“ (akt1), „Funken aus Drehung“ (akt2)
- Kapitel bienen: 2 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Der Funke“ (akt1), „Die zerbrochene Unterwelt“ (akt2)
- Kapitel energie: 3 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Elite-Schaltkreis“ (akt3), „Prozessoren“ (akt2)
- Kapitel exdeorum: 1 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Funken aus Drehung“ (akt2)
- Kapitel markt: 36 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Brücke ins Nichts“ (bau), „Der Funke“ (akt1), „Der Wither“ (akt3), „Ein Dach über dem Kopf“ (bau), „Ein besserer Stock“ (bienen), „Enderperlen“ (akt3), „Lohenruten“ (akt2), „Messing“ (akt1), „Mühlstein statt Hammer“ (akt1), „Polonium“ (akt3), „Präzisionsarbeit“ (akt2), „Samen der Essenz“ (akt1), „Stein, der Quelle trägt“ (ars), „Stufe 5: Supremium“ (akt3)
- Kapitel maschinengeist: 2 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Geladener Stahl“ (energie)
- Kapitel mysticalag: 1 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Der Wither“ (akt3)
- Kapitel pruefungen: 10 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Das End“ (akt3), „Das Ritualbecken“ (ars), „Der Herzschlag“ (akt3), „Der Wächter am Ende“ (akt3), „Die Festung“ (akt2), „Die erste Maschine“ (akt1), „Messing“ (akt1), „Strom verteilen“ (mekanism)
- Kapitel sammler: 8 Linien zu Voraussetzungen aus anderen Kapiteln fehlen (kein Verweis im Kapitel): „Archwood“ (ars), „Das Erbe der Erbauer“ (akt3), „Der Funke“ (akt1), „Der Wither“ (akt3), „Der Wächter am Ende“ (akt3)

### Sperrliste

- VERBOTEN-Muster ^mekanism:.*_reactor trifft kein Item mehr (veraltet?)

### Texte

- 3 Titel mit mehr als 4 Wörtern (TEXTSTIL, Titel): „Ein Dach über dem Kopf“, „Mit dem Haken ins Laub“, „Was in der Erde steckt“
- 8 Titel im Doppelpunkt-Stil (TEXTSTIL, Titel): „Stufe 2: Prudentium“, „×2: Anreicherung“, „×3: Reinigung“, „Stufe 3: Tertium“, „Stufe 4: Imperium“ (+3)

## Akzeptiert (pruefung/ausnahmen.py)

- „Willkommen in der Leere“ (akt1): 10 Zeilen, TEXTSTIL erlaubt in der Hauptstory 6 — Start-Quest bündelt das Tutorial (Questbuch, Handbuch, Belohnungen, Markt, Jobs+, Team, Welttyp); Entscheidung 26.10.2026
- „Erz ohne Sieb“ (akt3): 8 Zeilen, TEXTSTIL erlaubt in der Hauptstory 6 — Wahl-Quest listet drei Wege samt Belohnungs-Quests; kürzer wird die Wahl unverständlich (26.10.2026)

## Veraltete Ausnahmen (treffen nichts mehr, löschen)

- Willkommen in der Leere.*Belohnung .*\(exdeorum:silkworm\)

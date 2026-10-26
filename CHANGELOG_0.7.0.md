# Sky and Stone 0.7.0 – The Heart of the Void

Stand: 25.10.2026 · Basis: 0.6.4 · Minecraft 1.21.1, NeoForge 21.1.264 · Keine neuen Mods, keine Versionswechsel.

## Kurz
Weniger Rätselraten im Frühspiel, zwei echte Entscheidungen vor dem Finale, eine Geschichte ohne Widersprüche – und drei Fehler weniger, die man im Spiel nur schwer bemerkt hätte.

## Frühspiel
- **Mystical Agriculture früher:** Inferium-Samen entstehen an der Werkbank (8 Inferiumessenz um einen Weizensamen). Der Infusionsaltar (18 Goldbarren) kommt erst danach, wenn er für Stufe-3-Samen wirklich gebraucht wird. Inferiumessenz gibt es direkt aus dem Sieb, ohne vorher ein Feld anzulegen.
- **Seidenraupe richtig erklärt:** Befallenes Laub gibt nur mit dem Crook Faden (etwa jedes zweite voll befallene Blatt), von Hand gar nichts. Vorher stand im Buch eine falsche Mechanik.
- **Prudentium:** Die Quest nennt jetzt den Infusionskristall (1 Diamant, 4 Prosperiumsplitter, 4 Inferiumessenz). Ohne ihn kam man hier nicht weiter.
- **Erst der Sifter, dann die Presse:** Die Presse kostet einen Eisenblock, der Sifter kein Eisen. Die Hauptstory führt jetzt in dieser Reihenfolge, damit das Eisen für die Presse schon von allein kommt.
- **Meilensteine sagen, was sie öffnen:** „Der Funke“, „Messing“, „Die erste Maschine“ und „Vierfach-Erz“ nennen die freigeschalteten Möglichkeiten. Akt II ist schon ab Messing offen, nicht erst nach der Siebfabrik.
- **Pilzinsel:** Hinweis, wie man ohne Startbaum an Holz kommt.
- **Das erste Feld** verlangt wieder echten Weizen (vorher zählten auch gesiebte Karotten oder Kakteen).

## Create
- **Zinc Mesh herstellbar:** Stöcke um einen Zinkbarren. Vorher gab es kein Rezept, und 22 Sifter-Rezepte der Eisennetz-Stufe waren unbenutzbar.
- **Mühlstein repariert:** Stein, Steinziegel (alle Varianten), Prismarin (alle drei) und Tropfsteinblock ergaben im Mühlstein nichts. Jetzt geben sie dieselben Kiesel wie der Hammer.

## Entscheidungen statt Pflichtreihenfolge
- **Neu: „Erz ohne Sieb“** (Akt III): Wähl einen Weg – Osmium-Samen (Mystical Agriculture), Erz-Laserbasis (Industrial Foregoing) oder Erz-Bienen (Productive Bees). Einer reicht fürs Finale. Laserbohrer und Bienen haben damit erstmals einen Platz im großen Ziel.
- **„Maschine oder Magie“** bleibt, ist jetzt aber ab Akt III im Untertitel angekündigt („früh anfangen lohnt sich“).
- **Bienenzucht ehrlich:** Die Quest erklärt den echten Weg zu Erz-Bienen (Quartz Nest im Nether + Gravel Nest in einem Fluss- oder Strandbiom) und verlangt beide Nester statt nur 8 Honey Treats.
- **Loot Fabricator:** Die Quest erklärt den Netherit-Weg (Schwarzstein hämmern, Schutt sieben gibt Antiken Schrott).

## Geschichte „Das Herz der Leere“
- Kein Widerspruch mehr: Die Notiz zur Weiche sagt jetzt „Einer der Wege hätte gereicht“, das Finale spricht von „deinem gewählten Weg“.
- Die Kern-Notiz „Kraft aus der Leere … der Boden riss“ steht jetzt beim Spaltreaktor in der Hauptstory statt bei einer Nebenquest. Akt II bekommt eine eigene Notiz („Die Leitungen“).
- Das Story-Kapitel heißt „Tagebuch des Wächters“ (vorher gleicher Name wie Akt III). 17 Notizen.
- Die Start-Quest erklärt die drei Bereiche des Buchs: Der Weg der Erbauer, Handbuch der Mods, Abseits des Weges.

## Balance
- **Keine Essenz-Verdopplung mehr:** Tertium → 4 Prudentium und Insanium → 4 Supremium (Rückbau-Rezepte) machten aus den neuen Stufenrezepten eine Endlosschleife. Beide Rückbauten sind entfernt; alle anderen bleiben.
- **Goldkisten nicht vor Messing:** Auch „Magisches Autocrafting“ (Wixie) gibt jetzt eine Eisenkiste.
- **Sternkiste:** Netheritbarren statt 32 Prudentium (war im Endgame wertlos).

## Technik und Leistung
- **Kein Hash-Drift mehr:** Das Questbuch wird genau in dem Format geschrieben, das FTB Quests selbst speichert. Vorher speicherte FTB beim ersten Welt-Save alle Dateien neu, und das Auto-Update konnte sie danach nicht mehr reparieren.
- **Bienen fliegen nicht mehr ziellos herum** (`disableWanderGoal`), sie bestäuben aber weiter. Weniger Rechenlast bei großen Bienenfarmen.
- Questbuch-Titel „Sky and Stone“ unter dem richtigen Schlüssel.

## Für bestehende Welten
Quest-IDs bleiben gleich, Fortschritt bleibt erhalten. Neu ist nur die Quest „Erz ohne Sieb“; die Quest „Antimaterie-Handel“ gibt es seit 0.6.3 nicht mehr.

# Spieldesign Sky and Stone (Phase C)

Grundlage: Questgraph aus `_src/bausteine.py` (Kapitel, Abhängigkeiten), `texte_hauptstory.py` (Akte), Belohnungen aus `_src/belohnungen.py`. Die Stufen sind aus dem Graphen abgeleitet, nicht im Spiel gespielt.

## Leitregeln
1. Jede Stufe braucht einen Zweck: ein Problem, das sie löst.
2. Technik und Magie sind gleichwertig, aber verschieden: Technik ist planbar und strombasiert, Magie ist ressourcenfressend und verlangt Sammeln.
3. Entscheidungen haben Folgen. Eine Route darf nicht dauerhaft unterlegen sein.
4. Keine Pflicht ohne Mehrwert. Optionales bleibt optional.
5. Belohnungen dürfen keine Schranke überspringen.

## Progressionsstufen

| Stufe | Funktion | Voraussetzung | Erwartete Leistung | Engpass | Übergang |
|---|---|---|---|---|---|
| 0 Start | Orientierung, Baum, Haken | keine | Holz, Setzlinge, Ducken | Wachstum langsam | Erde/Kies-Kapitel |
| 1 Erde | Sieb, Erzbrocken | Holz, Faden, Hammer | Sieb in 5×5, Feuerstein | Erster Eisenbarren ~25–40 min (Ziel, ungemessen) | Eisenbarren öffnet Create, Feld, Werkzeug |
| 2 Create | Mühle, Sieb-Automatik, Messing | Kupfer, Zink, Wasserrad | Sifter, Presse, Mixer | Messing, Wartezeiten | Strom-Kapitel |
| 3 Strom und Mekanism | Osmium, Infuser, Reinigung | Kupferdraht, Netz | Anreicherung, Injektion | Schaltkreise | Wahl Magie oder Mekanism |
| 4 Magie oder Technik | Essenzen, Ars | Mystical Agriculture oder Ars | Essenz-Stufen | Stufenkette | Akt III |
| 5 Netzwerk | AE2, Lager, Autocrafting | Prozessoren, Certus | Netz, Lader | Verkabelung | Erz ohne Sieb |
| 6 Akt III | Wahlen, Bosse, Antimaterie | Weg der Magie oder Maschine | Wither, Drache | Teile sammeln | Finale |
| 7 Finale | Ewige Fabrik, Versiegeln | alle Wege | Insanium, Antimaterie | Zeit | Weiterbauen |

## Entscheidungen
- **Maschine oder Magie** (Akt III): Belohnung je Weg. Heute ohne spürbare Folgen. Vorschlag: Folgen über Quest-Sperren oder KubeJS, sobald der Spike (Stufen-Abfrage im Spiel) geklärt ist. Ohne diese Prüfung nicht umsetzen.
- **Erz ohne Sieb**: Felder, Laserbohrer oder Bienen. Ebenfalls Belohnungen, keine Folgen.

## Belohnungen und Abkürzungen
- Bei Messing und Siebfabrik gibt es seit 25.10. die Messing-Kiste statt der Goldkiste. Ob die übrige Goldkiste zu früh kommt, zeigt der Spieltest.
- Sternkiste: Netheritbarren seit 26.10. entfernt, nur Netherit-Schrott bleibt (Pipez-Sperre greift nicht). Entscheidung von Leon offen.
- Inselmarkt: 19 Tausch-Quests mit Abklingzeit. Balance nach Spieltest.

## Systeme und Mods
- Lootr (neu): eigene Beute pro Spieler, Truhen nicht craftbar.
- Jobs+ (neu): freiwillige Berufe, Bedienung noch nicht verifiziert.
- Nicht übernommen: Wirtschaft, Werkzeugstufen, neue Dimensionen.

## Endgame und Wiederspielwert
- Finale "Die ewige Fabrik", Versiegeln, Erbe der Ewigkeit. Das Archiv und der Codex bieten Sammelziele.
- Offen: Was nach dem Finale passiert, ist nur angedeutet. Das bleibt eine Designaufgabe.

### Entwurf „Nach dem Finale“ (Sprint 7.4, 25.10.2026, Vorschlag)
- Ziel: Wiederspielwert ohne Pflicht. Das Finale „Die ewige Fabrik“ bleibt der Abschluss der Story.
- Anti-Ziele: keine Grind-Schleifen, keine neuen Dimensionen, keine Pflicht-Quests nach dem Finale (siehe CLAUDE.md).
- Vorschlag A (klein): Abschluss-Titel für den Codex, das Sammlerbuch und den Inselmarkt. Reine Anerkennung, kaum Balance-Risiko.
- Vorschlag B (mittel): optionale „Prüfungen der Leere“ als Herausforderungen mit Titeln, auf der bestehenden Kapitelstruktur aufgebaut. Ersetzt die gestrichenen Haken-Quests.
- Vorschlag C (Wahl-Folgen): Die Route „Maschine“ oder „Magie“ aus Akt III gibt im Endgame unterschiedliche Bauteile frei. Hängt an den Spike-Ergebnissen (Phase 5).
- Entscheidung bei Leon: Umfang (A, A+B oder A+B+C). Ohne Spieltest nur A und B.

## Arbeitsannahmen (25.10.2026, ohne Spieltest)
- **Koop:** optional, keine Team-Pflicht. Team-Belohnungen gibt es vorerst nur im Inselmarkt. Die Koop-Entscheidung wird nach dem ersten Mehrspieler-Test neu bewertet.
- **Zielzeit bis zum Finale:** Arbeitsannahme 20 Stunden reine Spielzeit. Nach dem Spieltest korrigieren.
- **Klassische Insel:** etwas größer (9×3 oben, 3×6 unten). Spawn unverändert.

## Priorität (nach Spielerwirkung, Risiko, Aufwand)
1. Spieltest der Frühphase (Eisenbarren-Zeit), Grundlage für alle Balance.
2. Goldkiste und Sternkiste prüfen, gegebenenfalls anpassen.
3. Spike Stufen-Abfrage im Spiel prüfen, dann erst wegabhängige Folgen planen.
4. Lootr im Spiel prüfen.
5. Mehrspieler-Test (Team-Belohnungen).

## Entscheidungen zum Backlog (25.10.2026, volle Verantwortung)
- **8.3 Sieb-Fundgrube: gestrichen.** Ex-Deorum-Siebrezepte liefern genau ein Ergebnis pro Rezept. Eine seltene Zusatzbeute bräuchte ein zweites Rezept mit derselben Zutat und demselben Mesh. Das gibt Konflikte und eine Balance-Änderung ohne Spieltest. Die Seltenheit gibt es stattdessen über die Ruinen-Beute (Seite 18, 5 %). Hinweis 26.10.2026: Die Begründung oben stimmt nicht ganz. sieben.js hängt bereits Zusatzrezepte mit derselben Zutat und demselben Netz an. Die Entscheidung ist neu zu bewerten (Leon).
- **8.6 Schatzkarte: gestrichen.** Eine Karte braucht Strukturen, die die Skyblock-Welt nicht hat. Der Entdeckungsreiz kommt über Ruinen-Schilder und die Tagebuchseite.
- **8.7 Ersatz-Begleiter: keiner.** Die Logistik übernehmen Create-Depot, Schubladen-Wand (`l_controller`) und Functional Storage. Ein neues Lebewesen würde die Quest-Logik neu bauen, dafür fehlt der Spieltest.
- **8.9 Leere-Nebel: abgelehnt.** Der Effekt braucht Client-Shader oder ein Ressourcenpaket, das ich nicht im Spiel prüfen kann. Die Stabilität hat Vorrang.

## Planänderung (25.10.2026, ohne Spieltest)
- **Früh-Wahl bei Messing und Siebfabrik:** Die Goldkiste (Diamanten, Osmium) war zu früh. Neu: Messing-Kiste mit Eisen, Kupfer, Messing, Gold, Prudentium, Quarz u. a. Begründung: Diamant und Osmium sind Zwischenstufen der Mekanism- und Mystical-Ketten. Kosten bei Irrtum: Eine frühe Wahl bietet weniger Seltenes. Die Goldkiste bleibt sonst unverändert.

# Night Report – Sky and Stone 0.6.2 → 0.6.3

Stand: 25.10.2026 (Nachtschicht) · Kein Release exportiert, nichts hochgeladen.

**Kurz:** Die Basis war technisch sauber. Behoben wurden vier Frühspiel-Hänger im Questbuch (Lohenbrenner/Netherrack, Zink, Seidenraupe, unsichtbare Voraussetzungen), ein Glücks-Blocker auf dem Magie-Weg (Totem), zu frühe Goldkisten im Markt und eine Lücke im Questgenerator. Der Testserver startet mit 0 Fehlern. **Im Spiel (Client) wurde nichts getestet.**

Legende: **BESTÄTIGT** = durch Test nachgewiesen · **STATISCH GEPRÜFT** = Dateien geprüft, nicht im Spiel · **UNGETESTET** · **BLOCKIERT**

## 1. Ausgangszustand
- `pack.toml` 0.6.2, MC 1.21.1, NeoForge 21.1.264, 119 Mod-Einträge, 3 Ressourcenpakete. Kein Git-Repo, Sicherungen laufen über `_backups/`.
- Sicherung vor der Nacht: `C:\Projekte\modpacks\_backups\sky-and-stone-0.6.2-vor-nachtschicht-20261025` (`_src`, `config`, `kubejs`, `mods`, `index.toml`, `pack.toml`, `options.txt`, README).
- Ausgangsprüfung: Generator byte-gleich mit den Questdateien (19 Kapitel, 174 Quests, 68 Hauptstory). Testserver: 7/7 KubeJS-Skripte, 0 fehlgeschlagene Rezepte. **BESTÄTIGT**

## 2. Ergebnisse der drei Audits (Auswahl, selbst nachgeprüft)
| Audit | Befund | Bewertung |
|---|---|---|
| Quest-Fluss | Leerer Lohenbrenner braucht Netherrack, der Nether ist leer, der Weg (Hexenwasser) stand nirgends | bestätigt im Create-Rezept + Ex-Deorum-Daten → behoben |
| Quest-Fluss | „Kupfer und Zink“ wollte 4 Zinkbarren; Zink 3,5–4 % pro Kies → ~400 Kies von Hand | bestätigt (Siebtabellen) → behoben |
| Quest-Fluss | Seidenraupe Pflicht fürs erste Sieb, Haken findet sie nur mit ~1 % pro Laub | bestätigt → behoben |
| Quest-Fluss | 10 Akt-Quests hängen an Mod-Kapitel-Quests, im Akt unsichtbar | bestätigt → behoben (Verweise) |
| Design | Erzmagier-Buch braucht Totem – in der Leere nur per Glück (Sternkiste) | bestätigt im Ars-Jar, Totem hat kein Rezept → behoben |
| Design | Gold-Tausche (Enderperlen, Quellsteine) vor Messing → Messing/Osmium aus dem Markt umgeht Tertium-Schwelle | bestätigt per Abhängigkeits-Skript → behoben |
| Design | Antimaterie-/32-Supremium-Tausch lohnen sich nicht | → angepasst |
| Design | Starbuncle (Magie-Logistik) hing an Technik-Lager-Controller | → entkoppelt |
| Design | Productive Bees / Hostile Networks könnten Essenz-Stufen umgehen | **Hypothese**, nicht geändert, im Spiel per JEI prüfen |
| QA | Generator schrieb SNBT auch bei Fehlern; Mob-/Dimensions-Tippfehler wurden nicht erkannt | bestätigt (Fehler in Kopie eingebaut) → behoben |
| QA | Testserver Sichtweite 10/Simulation 10 statt 8/6 | → angepasst |
| QA | Bekannte Log-Fehler (modularbees-Rezept, Curios-Slots) | harmlos, unverändert |
| QA | index.toml, Hashes, BOM, TOML, JS-Syntax, Versionen (alle NeoForge/1.21.1, kein Connector) | alles ok |

## 3. Änderungen
| Datei | Änderung | Warum fürs Spielen wichtig |
|---|---|---|
| `_src/questlib.py` | `write()` erzeugt erst alles, schreibt nur ohne Fehler; Prüfliste für Mobs und Dimensionen | Ein kaputtes Questbuch kann nicht mehr versehentlich per `packwiz refresh` ins Spiel gelangen |
| `_src/quests.py` | `main()` übergibt die Strukturfehler an `write()` | dito |
| `_src/quests.py` | `c_brenner`: Aufgaben leerer Brenner + Brenner, Anleitung Netherrack über Myzel → Hexenwasser + Lava | Der wahrscheinlich größte Hänger vor Messing |
| `_src/quests.py` | `e_kupfer`: 4 Kupfer + 1 Zink (vorher 8 + 4), Text ehrlich | Spart ~300 Kies Handarbeit; Zink kommt später vom Create-Sifter |
| `_src/quests.py` | `w_start` gibt zusätzlich 1 Seidenraupe; `e_raupe` belohnt 4 Faden statt 2 Raupen; `e_brocken`-Text korrigiert (Fadennetz reicht schon) | Erstes Netz planbar statt Zufall |
| `_src/quests.py` | `kap()` für die Akte: Voraussetzungen aus Mod-Kapiteln als Verweise (Akt I: Haken, Inferium; Akt II: Eisennetz, Stahl, Fortschritt; Akt III: Controller, Diamant-Samen, Netherstern-Samen, Erzmagier, Beute-Fabrikator) | Gesperrte Akt-Quests zeigen, was fehlt |
| `kubejs/server_scripts/balance.js` | Erzmagier-Buch-Upgrade: Totem → Diamantblock (Rezept `skyandstone:archmage_book_upgrade`, Typ `ars_nouveau:book_upgrade`) | Magie-Weg zum Finale ohne Glücksspiel |
| `_src/quests.py` | `a_erzmagier`: hängt an `j_wither`, nennt alle Zutaten, **Warnung: Chimera-Ritual zerstört Blöcke** | Schützt die Insel |
| `_src/quests.py` | `a_starbuncle` ohne `l_controller`, Eisen- statt Goldkiste; `b_zucht` Eisen- statt Goldkiste | Magie eigenständig; keine Goldkiste im Frühspiel |
| `_src/quests.py` | Wiederholbare Gold-/Sterntausche brauchen `c_messing`; `x_antimaterie` gestrichen; `x_supremium` 8 statt 32 | Markt umgeht die Messing-Schwelle nicht mehr, Endgame-Tausche sinnvoll |
| `config/ftbquests/**` | neu erzeugt (Akte, ars, bienen, markt, lang) – 173 Quests | Folge der Änderungen oben |
| `pack.toml`, `index.toml` | Version 0.6.3, `packwiz refresh` | Prism holt den Stand beim nächsten Start |
| `.packwizignore` | `NIGHT_REPORT.md`, `MORGEN-PLAYTEST.md` | Berichte landen nicht im Spielordner |
| `README.md` | Version, Quest-Zahlen, Markt, Verlauf 0.6.3 | Doku stimmte nicht mehr (stand noch auf 0.4.1) |
| `_testserver-sky-and-stone/server.properties` | view-distance 8, simulation-distance 6 (Original: `server.properties.vor-nachtschicht`) | Gleiche Last wie am Laptop |

Bewusst **nicht** geändert: Mods, Versionen, `options.txt`, Ressourcenpakete, Startinseln, Startinventar-Datei, Siebchancen, „Erster Eisenbarren“ (bleibt 4 Barren), Productive Bees/HNN.

## 4. Tests
| Prüfung | Ergebnis | Status |
|---|---|---|
| Generator im Projekt | 19 Kapitel, 173 Quests, 68 Hauptstory, Exit 0, alle Item-IDs bekannt | BESTÄTIGT |
| Generator mit absichtlichem Fehler (Scratch-Kopie) | Exit 1, „Nichts geschrieben“, Datei unverändert | BESTÄTIGT |
| Scratch-Ausgabe = Projekt-Ausgabe | identisch | BESTÄTIGT |
| `node --check` balance.js | ok | BESTÄTIGT |
| packwiz refresh + installer auf Testserver | 170/170 Dateien, Index-Hash = pack.toml | BESTÄTIGT |
| Testserver-Start 0.6.3 | Done, 7/7 KubeJS, 0 Fehler, **0 failed recipes**, 245 hinzugefügt/47 entfernt (je +1 = Erzmagier), FTB Quests: 19 Kapitel, 173 Quests, 4 Tabellen | BESTÄTIGT (Server) |
| Diff gegen Sicherung | nur die Dateien oben; mods/ und options.txt unverändert | BESTÄTIGT |
| Erzmagier-Rezept in JEI sichtbar und craftbar | – | STATISCH GEPRÜFT (lädt fehlerfrei, im Spiel nicht angesehen) |
| Quest-Layout der neuen Verweise im Buch | – | UNGETESTET (Client) |
| Hexenwasser → Netherrack-Anleitung im Spiel | Rezeptdaten aus dem Ex-Deorum-Jar gelesen | STATISCH GEPRÜFT |
| Zeit bis erster Eisenbarren | Schätzung 25–40 min | UNGETESTET |
| Leistung (TPS/RAM/FPS) | nicht gemessen, kein Spieler auf dem Server | UNGETESTET |
| Client-Start in Prism | nicht ausgeführt | UNGETESTET |

## 5. Risiken und offene Punkte
- Der genaue Lava-Schritt beim Hexenwasser-Fass steht nur als „siehe JEI“ im Text – beim Spieltest genauer beschreiben.
- Productive Bees und Hostile Networks könnten Essenz-Stufen umgehen (Hypothese).
- `l_auto` (AE2-Autocrafting) hängt weiter an einem Functional-Storage-Controller – jetzt sichtbar, aber vielleicht unnötige Pflicht.
- Quest-IDs hängen am Kapitelnamen: Quests in andere Kapitel zu verschieben löscht Fortschritt in bestehenden Welten (heute nicht passiert).
- `file:///`-Update-Adresse funktioniert nur auf diesem PC.
- Kein Blocker bekannt.

## 6. packwiz / Prism
- `pack.toml` 0.6.3, Index-Hash `101b7d61…4fb3`, 170 Dateien. Testserver hat genau diesen Stand.
- Prism-Instanz „Sky and Stone“ hat noch 0.6.2; der Pre-Launch-Befehl (`packwiz-installer-bootstrap.jar file:///C:/Projekte/modpacks/sky-and-stone/pack.toml`) holt 0.6.3 beim nächsten Start. `options.txt` bleibt durch `preserve`.
- Kein `.mrpack` für 0.6.3 exportiert (nicht beauftragt). Befehl bei Bedarf: `../tools/packwiz/packwiz.exe modrinth export`.

## 7. Wiederherstellung
Kein Git. Zurück auf 0.6.2: Ordner aus `_backups/sky-and-stone-0.6.2-vor-nachtschicht-20261025` zurückkopieren (`_src`, `config`, `kubejs`, `index.toml`, `pack.toml`, `README.md`, `.packwizignore`), dann `packwiz refresh`. Testserver-Einstellung: `server.properties.vor-nachtschicht` zurückkopieren.

## 8. Nächste fünf Aufgaben (nach dem Spieltest)
1. Hexenwasser-/Netherrack-Text nach dem Spieltest präzisieren; ggf. „Erster Eisenbarren“ 4 → 2 Barren, falls über 40 min.
2. Im Spiel per JEI prüfen, ob Ressourcen-Bienen (Diamant, Osmium …) vor Imperium/Supremium gehen; falls ja, Zuchtrezept an Stufen-Essenz koppeln.
3. Entscheiden, ob `l_auto` den Functional-Storage-Controller wirklich braucht.
4. TODO-0.7 (Item-Gruppen für Barren, Certus, Bruchstein …) umsetzen.
5. Leistung messen (spark) und erst dann Export 0.7.0 bzw. privates GitHub-Repo für Updates auf anderen PCs.

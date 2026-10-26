# Night Report – Sky and Stone 0.6.4 → 0.7.0 „The Heart of the Void“

Stand: 25.10.2026 · Kein Upload, keine Veröffentlichung. Spielerseitige Änderungen: `CHANGELOG_0.7.0.md`. Spieltest: `MORGEN-PLAYTEST.md`.

Legende: **BESTÄTIGT** = durch Test/Datei nachgewiesen · **STATISCH GEPRÜFT** = plausibel aus Dateien/Jars, nicht im Spiel · **UNGETESTET** · **BLOCKIERT**

## 1. Ausgangs- und Zielversion
- Auftrag nannte 0.6.2 als Basis; tatsächlicher Stand war **0.6.4** (0.6.3 + 0.6.4 aus früheren Sitzungen). Darauf aufgebaut.
- Ausgang: 119 Mod-Einträge, 3 Ressourcenpakete, 6 Inseln, 19 Kapitel, 173 Quests (68 Hauptstory). Ziel: 0.7.0, 174 Quests (69 Hauptstory), 17 Story-Notizen.
- Erster echter Client-Nachweis: Prism-Session 25.10. 02:00–03:15 mit 0.6.4, Welt geladen, nur 4 bekannte harmlose ERROR (GeckoLib-Animation, modularbees-Rezept, 2× Curios-Slot). **BESTÄTIGT** (Log). Spielzeit im Log nur ~11 min, keine Spark-Werte.

## 2. Audits (5 Agenten, nur lesend) – wichtigste Ergebnisse
| Agent | Befund | Status | Umgesetzt |
|---|---|---|---|
| A Spielerweg | Infusionsaltar (18 Gold) sperrt MA-Einstieg, obwohl Inferium-Samen ein Werkbank-Rezept sind | BESTÄTIGT (MA-Jar) | ja |
| A | Seidenraupen-Text falsch (Spinnweben) – Faden nur per Crook von voll befallenem Laub (40 %+10 %) | BESTÄTIGT (Ex-Deorum-Jar) | ja |
| A | Prudentium-Text ohne Infusionskristall | BESTÄTIGT | ja |
| A | Presse (Eisenblock) vor dem Sifter (kein Eisen) | BESTÄTIGT (Create-Rezepte) | ja |
| A | Meilensteine nennen keine Freischaltung; Akt II wirkt erst nach der Siebfabrik offen | BESTÄTIGT | ja |
| A | Pilzinsel ohne Baum | Text BESTÄTIGT, Wachstum UNGETESTET | Hinweis |
| B Balance | Essenz-Verdopplung über MA-Rückbau (Tertium→4 Prudentium, Insanium→4 Supremium) | BESTÄTIGT | ja |
| B | Bienen/HNN umgehen keine Essenz-Stufe (Hypothese aus 0.6.3 erledigt) | BESTÄTIGT | – |
| B | Bienenzucht-Quest = Schein-Quest, falscher Weg | BESTÄTIGT | ja |
| B | Laserbohrer/Bienen ohne Platz im großen Ziel → zweite Wahl | Vorschlag | ja (`z_erz`) |
| B/D | Wixie gibt Goldkiste vor Messing; Sternkiste mit wertlosem Prudentium | BESTÄTIGT | ja |
| C Story | Widerspruch „erst zusammen“ vs. „ein Weg reicht“; zwei Kapitel „Das Herz der Leere“; Kern-Notiz auf Nebenquest; Akt II ohne Story | BESTÄTIGT | ja |
| D QA | Zinc Mesh ohne Rezept → 22 Sifter-Rezepte unbenutzbar | BESTÄTIGT (Jar) | ja |
| D | Mühlstein: 8 Rezepte ohne Ergebnis (min/max statt min_inclusive) | BESTÄTIGT (Jar + Simulation) | ja |
| D | `c:crops` löst „Das erste Feld“ ohne Feld; Tag-Liste veraltet | BESTÄTIGT | ja |
| E Release | FTB Quests schreibt alle 25 Questdateien beim ersten Save neu → Hash-Drift, Auto-Update repariert nicht | BESTÄTIGT | ja (`ftbformat.py`) |
| E | Questbuch-Titel unter falschem Schlüssel | BESTÄTIGT (Bytecode) | ja |
| E | Bienen-Wandern als größtes Entity-Risiko | Config BESTÄTIGT, Wirkung UNGETESTET | ja (`disableWanderGoal`) |
| E | .mrpack enthält CurseForge-Jars als Overrides → nur privat | BESTÄTIGT | dokumentiert |

## 3. Änderungen
| Datei | Änderung |
|---|---|
| `_src/ftbformat.py` (neu) | Schreibt Kapitel, Tabellen, Gruppen, data.snbt exakt im FTB-2101.1.37-Format (sortierte Schlüssel, CRLF, Inline-Regeln, order_index je Gruppe, presets/verify_on_load) |
| `_src/questlib.py` | Ausgabe über ftbformat; Datei-Titel `file.0000000000000001.title`; leere Item-Gruppen sind Fehler (Inhalt aus tags.json); Layout-Suche mit bis zu 16 Anläufen nur bei Problemen |
| `_src/quests.py` | MA-Reihenfolge (Inferium → Prudentium → Altar), Altar vor Stufe-2/3-Samen und Prägeplatten; Presse nach Sifter; `g_feld` fest auf Weizen; Wixie/Bienen Eisenkiste; Bienenzucht = Quartz Nest + Gravel Nest, nach dem Nether; neue Quest `z_erz` (eins von `m_niemehr`/`h_laser`/`b_zucht`) als Finale-Voraussetzung statt `m_niemehr`; `m_insanium` ohne `m_niemehr`; Sternkiste Netheritbarren statt 32 Prudentium; Story: `k_spalt` statt `s_reaktor`, neu `c_alternator`, `z_weg`; Platzhalter-Prüfung für Notizen |
| `_src/texte_hauptstory.py` | 0.7.0-Block: Akt-III-Untertitel mit Wahl-Hinweis, Start-Quest mit den drei Buchbereichen, korrigierte Mechaniken (Raupe, Inferium, Prudentium, Altar), Freischaltungen, Zinc Mesh, Presse-Tipp, Erz-Wahl-Text |
| `_src/texte_technik.py`, `texte_abenteuer.py` | Stimmungszeile Powah-Reaktor; Story-Kapitel „Tagebuch des Wächters“, neue/umgehängte Notizen; Bienen- und Netherit-Weg |
| `_src/tags.json` | Neu aus `kubejs/dev_tags.json` des Testservers (inkl. aller `skyandstone:`-Gruppen) |
| `kubejs/server_scripts/sieben.js` | uniform min/max; leere Hammer-Ergebnisse übersprungen; Rezept `skyandstone:zinc_mesh` |
| `kubejs/server_scripts/balance.js` | Entfernt `mysticalagriculture:tertium_essence_uncraft`, `mysticalagradditions:insanium_essence_uncraft` |
| `kubejs/server_scripts/gruppen.js` | Gruppe `skyandstone:erz_ohne_sieb` |
| `config/productivebees-server.toml` (neu) | Mod-Standard, nur `disableWanderGoal = true` |
| `config/ftbquests/**` | neu erzeugt (174 Quests) |
| `pack.toml`, `index.toml` | 0.7.0, 171 Dateien |
| `README.md`, `.packwizignore`, `MORGEN-PLAYTEST.md`, `CHANGELOG_0.7.0.md` | Doku; Berichte nicht im Spielpaket |

Bewusst nicht geändert: Mods/Versionen, `options.txt`, Ressourcenpakete, Startinseln/-inventar, Siebchancen, Essenz-Stufenrezepte, „Erster Eisenbarren“ (4 Barren).

## 4. Reviews
- Unabhängiger Reviewer auf den Gesamt-Diff: keine Code-Fehler. Gefunden und **behoben**: Erz-Wahl war wirkungslos (`m_insanium` hing an `m_niemehr`), Altar-Text (ab Stufe 2), Nest-Rezepte fehlten im Text, Netherit-Barren-Schritt, Platzhalter-Risiko.
- Nicht übernommen: „Antiker Schutt“ – laut Sprachdatei heißt das Item „Antiker Schrott“. Advancement-Aufgabe für Bienen – Productive Bees liefert seine Advancements im alten Ordner `advancements/`, der unter 1.21.1 nicht geladen wird (STATISCH GEPRÜFT).
- Nachweis nach den Fixes: ohne die beiden Wahlen ist keine der Wahl-Quests (`m_niemehr`, `h_laser`, `b_zucht`, `a_erzmagier`, `h_fab`) mehr Pflicht fürs Finale. **BESTÄTIGT** (Abhängigkeitsgraph).

## 5. Tests
| Prüfung | Ergebnis | Status |
|---|---|---|
| Generator 0.6.4-Quellen mit neuem Format vs. FTB-gespeicherte Instanzdateien | 25/25 byte-gleich | BESTÄTIGT |
| Generator 0.7.0 | 19 Kapitel, 174 Quests, 0 Fehler, Layout 0 Probleme / 19 Kreuzungen | BESTÄTIGT |
| `node --check` alle 4 KubeJS-Dateien, TOML-Parse aller `config/*.toml` | ok | BESTÄTIGT |
| packwiz refresh + Installer auf Testserver | 171 Dateien, Index-Hash = pack.toml | BESTÄTIGT |
| Testserver 0.7.0 (3 Starts) | 7/7 Skripte, 0 Fehler, **0 failed recipes**, 246 hinzugefügt / 49 entfernt (+1 Zinc Mesh, +2 Rückbau), 174 Quests, nur 3 bekannte ERROR | BESTÄTIGT (Server) |
| FTB-Neuspeichern beim Stopp | Questdateien byte-gleich mit Pack | BESTÄTIGT |
| Bienen-Config nach Serverstart | unverändert, `disableWanderGoal = true` | BESTÄTIGT |
| Tag `erz_ohne_sieb` im Server-Dump | 3 Mitglieder | BESTÄTIGT |
| .mrpack-Export | `Sky and Stone-0.7.0.mrpack`, 8,5 MB, ohne `_src`/Berichte, 27 Questdateien | BESTÄTIGT |
| Mühlstein gibt jetzt Kiesel aus Stein | Rezepte laden; Inhalt per Simulation (Audit D) | STATISCH GEPRÜFT |
| Zinc Mesh in JEI/Werkbank | Rezept lädt ohne Fehler | STATISCH GEPRÜFT |
| Client-Start mit 0.7.0, Questbuch-Layout, Texte im Spiel | – | UNGETESTET |
| Zeit bis erster Eisenbarren, Befallsdauer Laub | – | UNGETESTET |
| TPS/RAM/FPS | – | UNGETESTET |
| Erz-Bienen im Fluss-/Strandbiom auffindbar | Biom-Config erlaubt alles außer Ozeanen | STATISCH GEPRÜFT |

## 6. Risiken und bekannte Probleme
- Bienenzucht-Quest prüft gebaute Nester, nicht die gezüchtete Eisenbiene (keine ladbaren Advancements, Waben nur mit Komponenten). `z_erz` gilt damit beim Bienen-Weg früh als erledigt.
- Mystical Agriculture bleibt über `z_fabrik`/`z_netherstern` (Insanium, Netherstern-Samen) Teil des Endspiels – Absicht, steht im Changelog.
- Generator braucht jetzt ~1 min (Layout-Suche). Nur Rechenzeit.
- `config/tiab-server.toml` wird von der Mod lokal umgeschrieben (harmlos, nur Kommentare/Format).
- Gravel Nest braucht ein Fluss-/Strandbiom: in der Leere muss man es erst finden (F3).
- `file:///`-Update funktioniert nur auf diesem PC; .mrpack nur privat (CurseForge-Jars als Overrides).

## 7. packwiz, Export, Update-Weg
- `pack.toml` 0.7.0, Index-Hash `164ddaca…7daf` (nach dem Export neu geschrieben, alle 171 Datei-Hashes identisch mit dem getesteten Stand); Testserver auf genau diesem Stand.
- Prism-Instanz steht auf 0.6.4. Alle Questdateien haben neue Hashes → der Pre-Launch lädt sie beim nächsten Start vollständig neu. Ab dann bleibt FTB-Neuspeichern ohne Wirkung auf die Hashes.
- `Sky and Stone-0.7.0.mrpack` liegt im Projektordner (nur privat).

## 8. Git und Wiederherstellung
- Kein Git-Repo (Projektkonvention: Ordner-Sicherungen). Sicherung vor 0.7.0: `C:\Projekte\modpacks\_backups\sky-and-stone-0.6.4-vor-0.7.0-20261025` (`_src`, `config`, `kubejs`, `mods`, `resourcepacks`, `index.toml`, `pack.toml`, `options.txt`, Doku).
- Zurück auf 0.6.4: diese Ordner/Dateien zurückkopieren, `config/productivebees-server.toml` und `_src/ftbformat.py` löschen, `packwiz refresh`. Ältere Stände: weitere Ordner in `_backups`.

## 9. Nächste fünf Aufgaben (nach dem ersten Spieltest)
1. Messwerte aus `MORGEN-PLAYTEST.md` auswerten: Eisenbarren-Zeit, Befallsdauer, Netherrack-Schritt (Lava-Weg präzisieren), danach ggf. „Der Funke“ 4 → 2 Barren.
2. Leistung messen (spark) mit Bienen- und Create-Anlagen; erst danach über `forceBeeSimulation` oder IF-Grenzen entscheiden.
3. Bienenzucht prüfbar machen (z. B. eigenes KubeJS-Advancement für die Eisenbiene oder Abgabe eines Erz-Waben-Produkts).
4. TODO-0.7 (Item-Gruppen für Barren, Certus, Bruchstein …) als 0.8 umsetzen.
5. Privates GitHub-Repo als packwiz-Quelle für andere PCs statt .mrpack.

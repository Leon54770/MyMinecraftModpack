# Umsetzungsprotokoll Sky and Stone (Phase D/F)

Sicherung vor Änderungen: `_backups/` mit Ständen vor 0.11.1, 0.11.2 und 0.20.0. Kein Git-Repo, Rückweg ist der Sicherungsordner plus `packwiz refresh`.

## 0.11.1 (25.10.)
- Neu: `kubejs/server_scripts/bereinigung.js` entfernt das Rezept `productivebees:centrifuge/modularbees/honeycomb_imperial`.
- Begründung: Verweist auf ein Item von Modularbees, das nicht im Pack ist. Fehler im Startlog.
- Rückweg: Datei löschen, `packwiz refresh`.

## 0.11.2 (25.10.)
- Geändert: Starttext in `_src/texte_hauptstory.py`. Ziel und erster Schritt eingefügt.
- Lehre: Die Texte der Willkommens-Quest stehen in `texte_hauptstory.py`, nicht in `quests.py`. Eine Einfügung per Listenposition hat zuerst den falschen Satz überschrieben. Behoben, Diff geprüft.
- Rückweg: `config/ftbquests` aus `_backups/sky-and-stone-0.11.1-vor-start/` zurück und Generator neu starten.

## 0.20.0 (25.10.)
- Neu: Lootr (`lootr` 1.11.38.127) mit Hinweis im Starttext.
- Neu: Jobs+ (`jobsplus` 9.0.2) mit Abhängigkeiten Arc Lib 9.0.0, UI Lib 9.0.0, Item Restrictions 9.0.0, YAML Config 9.0.0.
- Nicht übernommen: When Dungeons Arise, Expanded Equipment, Wirtschaftsmods.
- Änderung in `_src/texte_hauptstory.py`: zwei Hinweiszeilen per `append`.
- Rückweg: `packwiz remove lootr jobsplus arc itemrestrictions uilib yaml-config`, Version zurück auf 0.11.2.

## Entscheidungen
- Keine Quests für Lootr und Jobs+ angelegt: Lootr-Truhen sind nicht craftbar, Jobs+-Items nicht verifiziert. Der Generator lehnt Haken-Aufgaben in diesen Kapiteln ab.
- Keine Balance-Änderung an Belohnungen ohne Spieltest.

## Offen (nicht umgesetzt, mit Begründung)
- Stufen-Folgen für Wahlen: Spike nur teilweise geprüft, daher nicht gebaut.
- Goldkiste, Sternkiste: Verdacht, erst nach Spieltest.
- TODO-0.7 (Item-Gruppen): wirkungslos, Almost Unified reduziert Tags auf ein Item.
- Warnungen (Curios, Mixins): ungeklärt.

## Release-Stand
- Pack `version = "0.20.0"`, Mrpack `Sky and Stone-0.20.0.mrpack`, Changelog `CHANGELOG_0.20.0.md`.
- Bekannte Probleme: siehe TEST_REPORT.md, Abschnitt „Nicht ausgeführt“.


## Prüflauf 25.10.2026 (Abnahme-Kriterien, Stand 0.20.0)

**Änderungen an Pack-Dateien in diesem Lauf: keine.** Begründung: Die offenen TODOs (PLAN-0.20.0 P1, P3, P4, P5, P6) brauchen Spieltest oder einen Testserver mit Spieler. Laut Kriterium 4 darf keine Balance-Änderung allein aufgrund einer Vermutung erfolgen. Verifizierbare Änderungen ohne Spieltest gab es nicht.

| Datei | Zweck | Status |
|---|---|---|
| IMPLEMENTATION_LOG.md | Dieser Abschnitt | Aktualisiert |
| TEST_REPORT.md | Prüfergebnisse je Kriterium | Aktualisiert (Abschnitt „Abnahmeprüfung 25.10.2026“) |
| PROJECT_AUDIT.md | Konflikte, Warnungen, Befunde | Aktualisiert (Abschnitt „Abnahmeprüfung 25.10.2026“) |

## TODO-Status (PLAN-0.20.0)

| TODO | Status | Begründung |
|---|---|---|
| P1 Playtest auswerten | BLOCKIERT | Braucht Spieltest durch Leon (MORGEN-PLAYTEST.md). FEEDBACK-LOG.md wurde nicht angelegt, da keine Befunde vorliegen. |
| P2 Belohnungs-Audit | Teilweise (Dokument vorhanden) | AUDIT-BELOHNUNGEN-0.11.md existiert. Generator-Check nicht gebaut, Balance-Änderungen warten auf Spieltest. |
| P3 Stuck-Quest-Test | NICHT GETESTET | Braucht Spieler, der Items in Gruppen-Aufgaben abgibt. Testserver hat keinen Client. |
| P4 Wahlen Akt III | BLOCKIERT | Spike nur teilweise (Ladeteil bestätigt, Wirkung nicht). Wegabhängige Rezepte nicht gebaut. |
| P5 Team-Fortschritt | BLOCKIERT | Entscheidung offen (PLAN Abschnitt 6, Frage 2). Test mit zwei Spielern nötig. |
| P6 Frühspiel Eisenbarren | BLOCKIERT | Braucht Messwert aus Spieltest. |
| P7 Item-Gruppen (TODO-0.7) | Offen, Empfehlung „schließen“ | Laut PLAN wirkungslos (Almost Unified). Schließen ist eine Entscheidung; im Pack unverändert. |
| P8 Log-Reste | Geprüft, NICHT BEHOBEN | Curios-Fehler `example`/`feet` und Rezept-Fallbacks: Herkunft nicht gefunden (siehe PROJECT_AUDIT.md). |
| P9 Versionssicherheit | BLOCKIERT | pack.toml nutzt noch file:/// -Adresse. Eine Online-Adresse braucht ein Repo bzw. einen Host, den es nicht gibt. |

## Offene Entscheidungen für Leon
1. Spieltest mit MORGEN-PLAYTEST.md (Prism, Welttyp Skyblock). Voraussetzung für P1, P3, P5, P6.
2. Koop-Pflicht für Team-Belohnungen (PLAN Frage 2).
3. Zielzeit bis zum Finale (PLAN Frage 3).
4. Update-Adresse für P9.

## Abstimmung nach Spieltest 1 (25.10.2026, Stand 0.20.0+)
Quelle: Notizen des Spielers. Frühspiel bis Funke funktioniert, Jobs+ unklar, Mob-Markt und Inselkisten noch ohne Urteil.
- Geändert: `_src/texte_hauptstory.py`, Quest `e_cobble`: Hinweis, dass Lava- und Wassereimer aus dem Startinventar sofort reichen.
- Geändert: `_src/texte_hauptstory.py`, Willkommens-Quest: Jobs+-Zeile nennt jetzt `/help job` statt „Die Bedienung zeigt das Spiel selbst“.
  Offen: Der Befehl `job` ist nur aus der Klassendatei des Mods abgeleitet, nicht im Spiel bestätigt.
- Generator `_src/quests.py` gelaufen: 186 Quests, 0 Layoutprobleme. Nur die Sprachdateien `de_de.snbt` und `en_us.snbt` haben sich geändert.
- Testserver (Java 21): Start `Done (1.851s)`, 186 Quests geladen, KubeJS ohne Fehler. Curios- und Mixin-Warnungen unverändert.
- packwiz refresh ausgeführt, Index aktualisiert.
- Backup: `_backups/sky-and-stone-0.20.0-vor-abstimmung/`.
- Nicht geändert: Abhängigkeit `e_cobble` hängt an `e_fass` (Kompostfass). Das wartet auf Erde. Balance-Entscheidung, erst nach weiterem Test.
- Nicht geändert: Mob-Kisten, Inselmarkt (keine Daten).
- Rückweg: Backup-Ordner zurück nach `config/ftbquests` kopieren und `packwiz refresh`.

## Gesamtrunde 25.10.2026 (nach Spieltest-Feedback)
Backup: `_backups/sky-and-stone-0.20.0-vor-gesamt/` (_src, kubejs, config/ftbquests).
- Geändert `_src/quests.py` (AKT1): `e_cobble` hängt jetzt an `e_holz` statt `e_fass`. Grund: Start-Lava- und Wassereimer machen Bruchstein sofort möglich.
- Geändert `_src/texte_hauptstory.py` (Willkommen): Jobs+-Erklärung mit Taste „Open Jobs+ GUI“, „Start performing this job“, kostenlose ersten 2 Berufe (amount_of_free_jobs=2 laut Config), EXP-Hinweis. Quelle: Mod-Sprachdatei und Config.
- Geändert `_src/texte_abenteuer.py` (Inselmarkt): Anleitung zum Abgeben, eine Kiste pro Team bei Tausch.
- Nicht geändert, weil keine Messwerte vorliegen: Eisenbarren-Menge (4), Mob-Kisten-Rate (1 %), Tausch-Mengen und Abklingzeiten, Wahlen Akt III.
- Generator: 186 Quests, 0 Layoutprobleme. Testserver Java 21: Done 1.897s, 186 Quests, KubeJS 9/9 ohne Fehler. Unverändert: Curios- und Rezept-Warnungen.
- packwiz refresh ausgeführt.
- Ausstehend: Spieltest mit Prüfung der Jobs+-Tasten und des Markt-Ablaufs im Spiel.

## Eisenbarren-Menge 25.10.2026
- Geändert: `_src/bausteine.py` (Quest e_eisen "Erster Eisenbarren") 4 → 2 Eisenbarren. Plan P6, siehe PLAN-0.20.0.md.
- Geändert: `_src/texte_hauptstory.py` (Text Der Funke) "zu 4" → "zu 2".
- Generator: 186 Quests, 0 Layoutprobleme. Testserver Java 21: Done 1.211s, 186 Quests, KubeJS 9/9 ohne Fehler. Curios-Warnungen unverändert.
- packwiz refresh ausgeführt.
- Rückweg: Backup _backups/sky-and-stone-0.20.0-vor-gesamt/_src/ zurückkopieren, Generator, refresh.
- Nicht verifiziert: Spielzeit bis zum Eisenbarren (Messung steht aus).

## Vollprüfung 25.10.2026 (Quest-Graph, Skripte, Configs, Mod-Set)
Backup: _backups/sky-and-stone-0.20.0-vor-gesamt/ (vor diesen Änderungen).
Methode: Zwei Prüfagenten (lesend) plus eigene Stichproben. Quest-Graph: 186 Quests, keine fehlenden Abhängigkeiten, keine Zyklen, keine unerreichbaren Quests, alle 240 Item-Aufgaben in dev_items.json. Keine Softlocks gefunden. Vollständige Rezept-Simulation NICHT erreicht (Dump-Lauf ohne vollständiges Ergebnis).

### Geändert
- _src/bausteine.py und _src/texte_hauptstory.py: Verweis auf das Kapitel „Erde, Kies und Hoffnung“ ersetzt durch „Akt I: Ein Splitter im Nichts“. Das Kapitel existiert im Questbuch nicht als eigene Datei, die Quests liegen in Akt I.
- _src/quests.py (t_drache, „Der zweite Drache“): kill 2 → kill 1. Text sagt „ein zweites Mal“, der erste Drache ist bereits Drachentöter (j_drache).
- kubejs/server_scripts/sieben.js: Enderperlen und Enderaugen aus den Ex-Deorum-Sieben werden nicht mehr in Create-Sifter-Rezepte übernommen. Grund: Die Akt-III-Quest verlangt sie, der Endstein-Sieb-Weg wäre eine frühe Abkürzung. Hinweis: Die Anzahl der Sifter-Rezepte blieb bei 132, weil die Gruppen weiter bestehen. Die Wirkung ist nicht im Dump belegt, nur die Filterlogik.

### Geprüft, verworfen
- Gold-Tausch im Inselmarkt: Existiert über x_perlen (Kiste gold). Text stimmt.
- Bienen-Zentrifuge (Vermutung des Agenten, belegt durch Jar): Nicht geändert, siehe Entscheidungen.

### Entscheidungen für Leon (nicht geändert)
1. Tertium-Ausbeute 2 statt 1 (balance.js 27-34), Insanium ebenfalls 2. Bewusste Balance oder Fehler?
2. Productive Bees Zentrifuge liefert Mystical-Essenzen (Tertium 50 %, Imperium/Supremium 30 %, Insanium 10 %). balance.js entfernt nur Crafting. hinweise.js:14 sagt „nur im Create-Mixer“, das stimmt dann nicht. Entweder Zentrifugen-Rezepte für Stufen 3–6 entfernen oder den Hinweis ändern.
3. Startinventar: starter_inventory.json5 sagt „bekommt jedes neue Team“, inventory.json5 setzt initialInventoryType spawn (pro Spieler). Bei Koop bekommt jeder Eimer und Eis.
4. Obsidian früh: Startinventar mit Eimern und Netherportal aus Feuerstein-Sieb wäre früh möglich (Vermutung, nicht getestet).
5. Endstein früh: Die Endstein-Sieb-Kette ist nicht geprüft; hängt davon ab, ob Endstein früh verfügbar ist.
6. Mod-Set: advancedae.pw.toml ohne extendedae. Log zeigt Fehler extendedae:crystal_assembler und Mixin-Warnungen. Vermutung: AdvancedAE braucht ExtendedAE. Entweder ExtendedAE ergänzen oder AdvancedAE entfernen.
7. luecken.js:14 Kommentar falsch (FTB hat ein Rezept ftbquests:screen_1). Pack-Rezept dupliziert es. Kommentar korrigieren oder Duplikat entfernen.
8. Erzmagier-Text verlangt Wilden-Tribut aus Chimera, Chimera ist aber keine Abhängigkeit (Design).
9. Sammlerbuch-Untertitel „Optional“, aber keine Quest ist optional (Text oder optional-Flag).
10. Archiv des Wächters braucht alle 17 Tagebuchseiten, Seiten sind einmalig (Verlustrisiko).

### Log-Warnungen (harmlos, nicht behoben)
- Curios example/feet: Quelle Industrial Foregoing (data/industrialforegoing/curios/entities/entities.json).
- ironfurnaces Upgrade-Rezepte: Bedingungsrezepte (allthemodium nicht installiert).
- Mixin-Warnungen: Klassen nicht installierter Mods.

### Testserver
- 18:58: Done (1.151s), KubeJS 10/10 ohne Fehler, 186 Quests, 20 Kapitel, 132 Sifter-Rezepte.
- Generator: 186 Quests, 0 Layoutprobleme.
- packwiz refresh ausgeführt.

## Entscheidungen 25.10.2026 (eigenständig getroffen)
1. Tertium 2 statt 1 (balance.js): BELASSEN. Begründung: Bewusste Balance aus 0.3.0, Insanium 2 ist laut CHANGELOG 0.5.0 ebenso gewollt.
2. Bienen-Zentrifuge: GEÄNDERT. balance.js entfernt productivebees:centrifuge/mysticalagriculture/honeycomb_{tertium,imperium,supremium,insanium}. Prudentium und Inferium bleiben (Frühspiel). hinweise.js-Text stimmt jetzt.
3. Startinventar: BELASSEN auf spawn (pro Spieler). Kommentar in starter_inventory.json5 korrigiert.
4. AdvancedAE: ENTFERNT aus dem Pack (packwiz remove advancedae). Kein Quest-Bezug. Testserver: Jar NOCH VORHANDEN (Löschen blockiert), daher Test mit altem Mod-Set.
5. Obsidian und Endstein früh: BELASSEN. Lava-Eimer ist Teil des Frühspiel-Feedbacks.
6. Kleinkram:
   - luecken.js: FTB-Rezept ftbquests:screen_1 wird ersetzt (remove + pack-Rezept). Kommentar korrigiert.
   - Erzmagier hängt jetzt zusätzlich an t_chimera (Reihenfolge wie im Text).
   - Sammlerbuch: Untertitel auf Freiwillig geändert.
   - Archiv: BELASSEN. Texte sagen bereits, dass die Seiten nicht verbraucht werden. Verlust durch Tod oder Verlieren bleibt Restrisiko.
Generator: 186 Quests, 0 Layoutprobleme. Testserver 19:04: Done 1.172s, KubeJS 10/10 ohne Fehler, 132 Sifter-Rezepte. Neu aufgetreten: Meldung RuntimeDistCleaner DISTXFORM (Klasse PoseStack auf dedizierem Server), Ursache offen, vermutlich ein Mod-Client-Klassen-Zugriff.

## Spieler-Rückmeldung 25.10.2026 und Umsetzung
- Standardinsel gewählt. Startinseln auf zwei reduziert: Klassisch (143 Blöcke, 8x9x8) und Waldlichtung (516 Blöcke, 13x14x13). Pilzinsel, Kirschhain, Oase, Felsbrocken entfernt (Backup in _backups/sky-and-stone-0.20.0-vor-gesamt/islands-unused/). Klassisch wurde NICHT vergrößert. Das braucht eine Neugestaltung.
- Starttext (w_start) neu gefasst, am Ende von _src/texte_hauptstory.py als Überschreibung. Jobs+-Taste benannt (Steuerung, Kategorie Jobs+, Open Jobs+ GUI). Taste selbst nicht im Spiel abgelesen.
- Neues Handbuch: kubejs/data/skyandstone/function/handbuch.mcfunction. Befehl /function skyandstone:handbuch gibt ein Buch mit 8 Seiten und das Questbuch (ftbquests:book). Test: Funktion lädt ohne Parse-Fehler (Pages als JSON-Text). Im Spiel NICHT ausgeführt. Braucht Cheats oder OP.
- Testserver: Done 1.6s, 186 Quests, 2 Inseln geladen, KubeJS 9/9 ohne Fehler.
- TPS-Messung des Spielers (Standardinsel, Nach ca. 10 min): 20, 20, 16, 19, 19.
- Spielerdaten: Minuten bis Eisenbarren nicht gemessen (geschätzt 10-25 min).

## Sprint 2, Punkt 2.1 Meilenstein-Feier (25.10.2026)
- Neu: kubejs/data/skyandstone/function/feier/*.mcfunction (11 Dateien), je Story-Erfolg Titel, Untertitel und Glockenton für den Spieler.
- Geändert: kubejs/data/skyandstone/advancement/*.json (11 Dateien) mit rewards.function auf skyandstone:feier/<name>.
- Prüfung: Testserver Done 1.778s, 6397 Fortschritte geladen, keine Funktions- oder Fortschritts-Fehler. Im Spiel NICHT GETESTET.
- Rückweg: rewards-Eintrag aus den Fortschritts-JSONs entfernen und den Ordner function/feier löschen.

## Meilenstein 1: Rezept-Simulation (25.10.2026)
- Datei: `_src/rezept-sim/` (`REZEPT-SIM.md` Bericht, `analyse.py` Auswertung, `zz_dev_recipes.js` Testserver-Dump, `dump/` Rohdaten).
- Zweck: Erreichbarkeit aller Quest-Items über Rezepte, Startinventar und Weltquellen prüfen. Nur Analyse, keine Pack-Änderung.
- Ergebnis: 15.618 Rezepte, 241 Item-Aufgaben (20 Gruppen), 0 Lücken nach manueller Prüfung zweier Quellen.
- Befund offen: Starbuncle-Shards nur über Zähmung wilder Starbuncles (Code), Spawn auf Inseln ungeprüft (`ars.snbt`, Charm-Quest). Polonium-Pellet per Chemie-Reaktion, Herstellung nicht im Dump sichtbar.
- Prüfstatus: Analyse BESTANDEN. Spiel NICHT GETESTET.
- Einschränkung (Stand 20:12): Der echte Testserver war zuerst durch Prozess 9532 gesperrt (`world/session.lock`). Bei der Nachprüfung lief 9532 nicht mehr, beendet habe ich ihn nicht. Der Dump lief in einer Kopie mit gleichen Mods. Neuer Start des echten Testservers (PID 7520, 20:11:47, Argumente wie `run.bat nogui`): Done (1.362s), KubeJS 10/10 Skripte ohne Ladefehler, 0 fehlgeschlagene Rezepte. Einziger Fehler: `zz_dev_recipejson.js` (altes Skript, nicht von dieser Sitzung, Rhino `getClass`), auf Wunsch von Leon im Testserver behalten.
- Rückweg: `_src/rezept-sim/` löschen. Keine Pack-Dateien geändert, kein `packwiz refresh` nötig.

## Sprint 2, Punkte 2.2 und 2.7: Zeit-Basis, Sturm, Herzschlag (25.10.2026)
- Neu: kubejs/data/minecraft/tags/function/tick.json und load.json (Vanilla-Tags, Werte: skyandstone:tick und skyandstone:load).
- Neu: kubejs/data/skyandstone/function/load.mcfunction, tick.mcfunction, zeit/slow, zeit/herzschlag, zeit/sturm_check, zeit/sturm.
- Ablauf: Tick zählt, alle 200 Ticks wird geprüft. Herzschlag einmal am Tag zur Dämmerung (12000 bis 12600). Sturm am Morgen, alle 3 Tage, 10 Minuten Regen ohne Blitze.
- Prüfung: Testserver Done 1.124s, keine Funktions- oder Tag-Fehler. Im Spiel NICHT GETESTET (Scoreboard-Ablauf, Titel, Wetter).
- Rückweg: Ordner kubejs/data/minecraft/tags/function und skyandstone/function/zeit/ sowie load.mcfunction und tick.mcfunction löschen.

## Sprint 3.1 und 3.2 Erreichbarkeits-Check (25.10.2026)
- Neu: _src/erreichbar.py (Heuristik: Quest-Abhängigkeiten, Startwelt, Rezept-Graph). Aufruf: python -I -X utf8 _src/erreichbar.py <dev_recipejson.json> <dev_tags.json>.
- Neu: _src/snbt.py (SNBT-Parser für den Check).
- Testserver-only: zz_dev_recipejson.js (nicht im Paket). Dump: 15319 Rezepte, 0 Fehler.
- Ergebnis: 186 von 186 Quests erreichbar, 0 Zyklen über Abhängigkeiten. 79 Aufgaben-Items ohne Weg laut Heuristik. Die Heuristik kennt keine Fluids und keine Energie, deshalb sind die meisten Treffer Fehlalarme. Liste im Lauf erzeugen und von Hand prüfen.
- Rückweg: Dateien _src/erreichbar.py und _src/snbt.py löschen. Kein Einfluss auf das Pack.

## Sprint 3.4 Begrüßungsbuch (25.10.2026)
- Neu: kubejs/data/skyandstone/function/handbuch_buch.mcfunction (nur das Buch, ohne Questbuch-Duplikat).
- Geändert: kubejs/server_scripts/willkommen.js ruft die Funktion beim ersten Login einmal auf (Flag bleibt wie bisher).
- Prüfung: Testserver Done 1.252s, KubeJS 10/10 ohne Fehler. Im Spiel NICHT GETESTET.
- Rückweg: Zeile p.runCommandSilent in willkommen.js entfernen, Datei handbuch_buch.mcfunction löschen.

## Lauf 2: Erreichbarkeits-Check mit Weltquellen (25.10.2026)
- Geändert: _src/erreichbar.py (WELT_QUELLEN, 12 Einträge; Ausgabe trennt Weltquellen von Heuristik-Lücken).
- Ergebnis: 186/186 erreichbar, 111 Aufgaben-Items ohne Weg laut Heuristik, davon 11 Weltquellen.
- Rückweg: Zeile WELT_QUELLEN und die elif-Zeile zurücksetzen (oder Datei löschen, ohne Einfluss auf das Pack).

## Lauf 3: Fehlalarm-Ursache (25.10.2026)
- Befund 1: Der Rezept-Dump erfasst keine Rezepte, die Pack-Skripte per event.custom ergänzen (0 Sifter-Rezepte, 0 Inferium-Sieb-Rezepte im Dump, obwohl sieben.js sie erzeugt). Der Erreichbarkeits-Check meldet daher Fehlalarme.
- Befund 2: Rezepte mit reiner Fluid- oder Chemikalien-Eingabe fehlen im Graph.
- Keine Pack-Dateien geändert. Behebung als Sprint 3.6 im Backlog.

## Sprint 3.6: Dump nach allen Rezept-Skripten (25.10.2026)
- Geändert (Testserver-only): zz_dev_recipejson.js nutzt ServerEvents.afterRecipes und den Mojang-Codec. 15467 Rezepte, 151 Fehler.
- Ergebnis Check: 92 Aufgaben ohne Weg (vorher 111). Pack-eigene Rezepte werden jetzt erfasst.
- Pack-Dateien: keine Änderung in diesem Schritt.

## Feier für Quest-Meilensteine (25.10.2026)
- Neu: `kubejs/data/skyandstone/function/feier/` mit 5 Funktionen: `g_autark`, `c_siebfabrik`, `k_inject`, `k_jetpack`, `z_herr` (Titel, Untertitel, Glockenton).
- Neu: Befehls-Belohnung in `_src/questlib.py` (Befehl, Berechtigung 2, still). Zuordnung `FEIER` in `_src/quests.py`, nach der Neuzuweisung aus `belohnungen.py`, sonst geht sie verloren.
- Ausgelassen: `e_eisen`, `j_drache`, `a_erzmagier`, `s_reaktor`, `l_auto`, `m_niemehr` (Story-Feiern vorhanden), `w_start` (Begrüßung). `h_boss`, `u_meister`, `x_markt`, `p_start` stehen nicht im Buch.
- Prüfung: Generator 186 Quests, 0 Layoutprobleme. ID-Check gegen Sicherung: 828 Referenz-IDs, 0 entfallen, 5 neu (Reward-IDs). `packwiz refresh` ok.
- Testserver-Kopie: `Done (1.205s)`, KubeJS 9/9 ohne Fehler, 0 fehlgeschlagene Rezepte, FTB Quests 186 Quests und 7 Belohnungstabellen, keine Meldungen zu Feier-Funktionen oder Belohnungen. Im Spiel NICHT GETESTET (Ausführung als Spieler, Titel, Glockenton).
- Der echte Testserver lief während der Prüfung (PID 7520) mit dem alten Stand. Vor dem nächsten Start per packwiz-installer synchronisieren.
- Nachtrag 25.10.2026, 20:26: Prozess 7520 war nicht mehr vorhanden (letzter Lauf: Done 20:17:27, ohne Stopp-Vermerk im Log, Ursache unbekannt, nicht von mir beendet). Echter Testserver per packwiz-installer synchronisiert und mit Java 21 in eigenem Fenster gestartet (PID 11388). Log: `Done (1.747s)`, KubeJS 10/10 ohne Ladefehler, 0 fehlgeschlagene Rezepte, FTB Quests 186 Quests und 7 Belohnungstabellen. Nur bekannte Curios-Meldungen. Im Spiel NICHT GETESTET.
- Rückweg: Sicherung `_backups/sky-and-stone-0.20.0-vor-feier-meilensteine-20261025/` zurückkopieren (`_src`, `config/ftbquests`, `kubejs`), Generator laufen lassen, `packwiz refresh`, die fünf Feier-Dateien löschen.

## TODO-Abgleich (25.10.2026)
- TODO-0.7 geschlossen (Empfehlung aus `AUDIT-BELOHNUNGEN-0.11.md`), Vermerk in `_src/TODO-0.7.md`.
- Wegweiser (SCRUM 1.4) als erledigt verbucht: Text im Quest „Der Funke“, keine Pack-Änderung nötig.
- Sprint 2.2 (Sturm) und 2.7 (Herzschlag) waren schon umgesetzt, nur die TODO war nicht nachgezogen. Ladetest OK, im Spiel NICHT GETESTET.
- Offen mit Blockade: 2.3 (Lootr-Test), 2.4 (Starbuncle-Spawn), 2.5 (Biome und Klangkulisse), 2.6 (zurückgestellt).
- Keine Pack-Dateien geändert.

## Quest „Der magische Logistiker“ entfernt (25.10.2026)
- Entscheidung von Leon: Quest `a_starbuncle` entfernen. Umsetzung nach Projektregel über die Ersatz-Tabelle (`ERSATZ` in `_src/quests.py`, Ersatz `l_controller`). Die Definition bleibt im Quellcode für Abhängigkeiten erhalten.
- Mitgezogen: Belohnungseintrag in `_src/belohnungen.py` und Text in `_src/texte_abenteuer.py` entfernt, weil beide sonst auf eine fehlende Quest zeigen würden.
- `p_ohnerohr` („Fabrik ohne Rohre“) hängt jetzt an `l_controller` (Schubladen-Wand), Beschreibung und Icon angepasst. Die Quest steht selbst nicht im Buch, sie war schon vorher ersetzt. Die Änderung wirkt also nur, wenn sie wieder eingebaut wird.
- Generator: 185 Quests (vorher 186), 0 Layoutprobleme.
- ID-Check gegen Sicherung vor dieser Änderung: Referenz 833, aktuell 830, entfallen 3, neu 0. Die drei IDs sind die Quest und ihre Belohnungen. Der Eintrag geht verloren, wer die Quest in einer Taiga-Welt schon abgeschlossen hat.
- Testkopie: `Done (1.201s)`, 0 fehlgeschlagene Rezepte, FTB Quests 185 Quests, 7 Belohnungstabellen, keine neuen Fehler.
- Der echte Testserver läuft noch mit dem alten Stand (186 Quests). Vor dem nächsten Start per packwiz-installer synchronisieren.
- Rückweg: Sicherung `_backups/sky-and-stone-0.20.0-vor-starbuncle-entfernen-20261025/` zurückkopieren (`_src`, `config/ftbquests`, `kubejs`), Generator laufen lassen, `packwiz refresh`.

## Klangkulisse (Sprint 2.5), Biome-Prüfung (25.10.2026)
- Die Insel-Vorlagen (`templates/islands/*.nbt`) speichern keine Biome. Die Welt-Einstellung `centeredBiomes` in `dimensions.json5` ist leer, also wählt der Overworld-Generator die Biome nach Position. Der Insel-Abstand in der Welt ist 8192 Blöcke (`islandDistance` in `world.json5`).
- Stichprobe Testwelt (Region-Dateien, Oberflächenbereich Y 48 bis 127): Ebene (plains) überwiegt, dazu Wald (forest), Hain (grove), Kirschhain (cherry_grove) und vereinzelt Schneehänge.
- AmbientSounds 6.3.11 (Client, `side = "client"`) bringt biomabhängige Regionen mit (u. a. plains, forest, grass, beach, cave). Die Konfiguration liegt in der Prism-Instanz. Eine Änderung am Pack ist nicht nötig.
- Offen: Klangkulisse pro Insel wäre nur über `centeredBiomes` (Weltgenerierung, nur neue Welten, Wirkung auf Ring-Biome ungeprüft) möglich. Entschieden 25.10.2026 von Leon: Mod-Standard, keine Änderung am Pack.
- Keine Pack-Dateien geändert. Ladetest entfällt, weil nichts geändert wurde.
- Entscheidung 25.10.2026 von Leon: Klangkulisse bleibt beim Mod-Standard.

## Befunde aus den Mod-Daten (25.10.2026)
- Starbuncle-Spawn: Wilde Starbuncles spawnen laut Ars-Nouveau-Daten (`BiomeTags` / `berry_spawn`) nur in `#minecraft:is_taiga` und `ars_nouveau:archwood_forest`. Die Testwelt hat keine dieser Biome. Folge: Quest `a_starbuncle` („Der magische Logistiker“, Charm) ist praktisch nicht lösbar, `p_ohnerohr` (optional) hängt daran. Entscheidung bei Leon nötig.
- Polonium-Pellet: Kein Fehler. Kette über Polonium-Gas (Aktivierung aus Atommüll). Atommüll hat kein Rezept, er entsteht im Fission-Reaktor (Mekanism Generators). Spätspiel.
- Keine Pack-Dateien geändert.

## Testserver-Neustart und Klassisch-Insel (25.10.2026, 20:47)
- Testserver-Prozess 11388 (mein Start) geordnet beendet, da Fenster-Schluss nicht reichte, erzwungen. Kein Spielstand betroffen, niemand war auf dem Server.
- Neustart mit dem Pack-Stand, Java 21: `Done (1.192s)`, KubeJS 10/10 ohne Fehler, 0 fehlgeschlagene Rezepte, FTB Quests 185 Quests.
- Klassisch vergrößert in `_src/inseln.py` (`klassisch()`): oben 9×3, unten 3×6. Ergebnis 11×9×11, 197 Blöcke (vorher 143). Spawn `[2, 3, 3]` unverändert. Waldlichtung unverändert (516 Blöcke).
- `inseln.py` erzeugt NBT und `templates.json5` neu. Die Vorlagen gelten nur für neu erstellte Welten, die bestehende Testwelt ändert sich nicht.
- Koop und Zielzeit als Arbeitsannahmen in `GAME_DESIGN.md`. Die Update-Adresse (P9) bleibt offen, weil sie ein Repo außerhalb des Rechners braucht.
- Rückweg: Sicherung `_backups/sky-and-stone-0.20.0-vor-klassisch-vergroessern-20261025/` (`inseln.py`, `skyblockbuilder/`), dann `python -I -X utf8 _src/inseln.py` und `packwiz refresh`.
- Keine Pack-Dateien außer den genannten geändert.
- Nachtrag 20:50: `packwiz refresh` nachgeholt (der Index war nach der Insel-Änderung veraltet). Testserver ein zweites Mal synchronisiert und neu gestartet: `Done (1.229s)`, 185 Quests, keine Fehler.

## Ruinen-Truhen als Lootr-Truhen (Sprint 2.3, 25.10.2026, 20:50)
- `_src/inseln.py` (`ruine()`): Neben dem Schild jeder Ruine steht jetzt eine Lootr-Truhe (`lootr:lootr_chest`), gegenüber dem Schild. Die Truhe bekommt die Beute `skyandstone:ruinen/fund`. Lootr-Truhen erben von der Truhenklasse und lesen den Schlüssel `LootTable` aus der Block-Entity.
- Neu: `kubejs/data/skyandstone/loot_table/ruinen/fund.json`. Drei Würfe mit Gewicht: Brot 2–4 (4), Fackeln 4–8 (3), Eisennuggets 2–6 (2), Setzlinge 1–2 (2), Goldnuggets 1–3 (1). Das ist ein Standard, bei Bedarf änderbar.
- Ergebnis: Klassisch 198 Blöcke, Waldlichtung 517 Blöcke, Spawn unverändert. Beide NBT-Dateien enthalten Truhe und Beute-Verweis.
- Testserver: `Done (1.226s)`, 185 Quests, keine Fehler. Die Beute-Tabelle lädt ohne Meldung.
- Im Spiel NICHT GETESTET: Lootr-Verhalten pro Spieler und Platzierung in einer neuen Welt. Die bestehende Testwelt ändert sich nicht.
- Rückweg: `config/skyblockbuilder/templates` aus `_backups/sky-and-stone-0.20.0-vor-klassisch-vergroessern-20261025/skyblockbuilder/` zurückkopieren, `kubejs/data/skyandstone/loot_table/ruinen/fund.json` löschen, `inseln.py` aus demselben Backup zurückkopieren, dann `packwiz refresh`.

## Sprint 6: Spaß und Gimmicks (25.10.2026)
- Neu über den Paket-Manager (`packwiz modrinth add`, Abhängigkeiten automatisch):
  - Emotecraft 2.4.12 (beide Seiten), mit player-animation-lib
  - Enchantment Descriptions 21.1.11 (beide Seiten)
  - Loot Journal 6.2.2 (nur Client), mit Fragmentum 5.4.0 (beide Seiten)
  - Better Combat 2.4.0 (beide Seiten), mit playerAnimator 2.0.4
- Nicht aufgenommen: Alex's Mobs (keine gültige Version für 1.21.1 NeoForge bei Modrinth).
- Gimmick ohne Mod: Feuerwerk-Partikel in allen 16 Meilenstein-Feiern (`kubejs/data/skyandstone/function/feier/*.mcfunction`).
- Testserver: `Done (1.265s)`, 185 Quests, keine Fehler. Nur bekannte Warnungen (Mixin-Klassen fehlender Mods, JarJar-Hinweis bei Fragmentum, harmlos). Ladeprüfung der Partikel-Befehle: Syntax wird erst bei der Ausführung geprüft.
- Client-Teile (Emote-Taste, Pickup-Anzeige, Kampfgefühl) NICHT GETESTET.
- CLAUDE.md: Mod-Freigabe für diese vier Mods vermerkt.
- Rückweg: `packwiz remove emotecraft enchantment-descriptions loot-journal better-combat fragmentum playeranimator` (plus Abhängigkeits-Reste prüfen), `packwiz refresh`, die Partikel-Zeile aus den Feier-Funktionen entfernen.
- Wächter-Spruch (6.7): `kubejs/server_scripts/waechter.js`, fünf Zufallszeilen nach dem Wiederbeleben (`PlayerEvents.respawned`). Ein erster Versuch mit `PlayerEvents.died` scheiterte beim Laden (unbekanntes Ereignis). Korrigiert. Testserver: 11/11 KubeJS-Skripte ohne Fehler, `Done (1.223s)`, 185 Quests. Die Nachricht im Spiel NICHT GETESTET. Rückweg: Datei löschen.

## Sprint 7: Fehlendes bis zum Release (25.10.2026)
- Analyse gegen das Ziel „fertiges, final spielbares Modpack“ und Recherche zu Release-Checklisten. Ergebnis: fünf Lücken (7.1 bis 7.5) in `SCRUM/BACKLOG.md` und `TODO.md` (Phase 8).
- Neu: `FEEDBACK-LOG.md` mit Smoke-Test, Koop-Testplan und Befundtabellen. In `.packwizignore` eingetragen, gehört nicht ins Paket.
- Keine Pack-Inhalte geändert. Rückweg: Datei löschen, `.packwizignore`-Zeile entfernen.
- Keine Prüfung im Spiel. Status der Punkte: 7.1 und 7.2 vorbereitet, Test offen; 7.3 bis 7.5 offen.

## Rest von Sprint 7 und Ideen-Backlog (25.10.2026)
- 7.4: Endgame-Entwurf in `GAME_DESIGN.md` (Vorschläge A, B, C, Umfang offen bei Leon).
- 7.3: Teilstand. Fission-Reaktor als Atommüll-Quelle bestätigt. Akt-II- und Akt-III-Ketten von Mekanism noch offen.
- Sprint 8 in `SCRUM/BACKLOG.md`: elf Ideen nach Aufwand und Wirkung, nicht gebaut.
- Keine Pack-Inhalte geändert. Verteilen und Koop bleiben auf später, wie von Leon festgelegt.

## Sprint 8: Umsetzung (25.10.2026)
- Neu: `kubejs/server_scripts/lagerfeuer.js` (8.1), drei Advancements `leere_sturz`, `schlaf_der_erbauer`, `fellfreund` (8.10), Feier `x_perlen` (8.5, in `FEIER` in `_src/quests.py`).
- Geändert: `function/zeit/herzschlag.mcfunction` mit Partikel-Zeile (8.4). `loot_table/ruinen/fund.json` mit eigener Pool für Tagebuchseite 18, 5 % (8.2).
- Ladeprüfung: 12/12 KubeJS-Skripte, 6400 Advancements, 185 Quests, `Done (1.261s)`, keine Fehler.
- Im Spiel NICHT GETESTET: alle Teile. Die Story-Passung der Seite 18 braucht Leons Prüfung.
- Offen: 8.3 (Ereignis-Haken Sieb), 8.6 (Schatzkarte braucht Strukturen), 8.11 (Entscheidung Umfang).
- Rückweg: die genannten Dateien löschen bzw. die Zeilen entfernen, `packwiz refresh`.

## Erreichbarkeits-Check: Fluid- und Chemie-Rezepte (25.10.2026, Lauf 4)
- Geändert: _src/erreichbar.py. Rezepte ohne Item-Zutaten, aber mit Fluid- oder Chemie-Eingabe, werden optimistisch geführt. Im Bericht als Fluid/Chemie-Weg, Prüfung nötig, getrennt ausgewiesen.
- Ergebnis: 96 Aufgaben ohne bekannten Weg, davon 30 nur über Fluid- oder Chemie-Rezepte (zu prüfen), 43 sonst nicht herstellbar.
- Hinweis: Quest-Anzahl im Check ist jetzt 185 (vorher 186). Die Kapitel wurden zwischen 21:09 und 21:11 von einer anderen Sitzung geändert (Sprint 6). Ursache nicht von mir.
- Rückweg: Zeilen FLUID_RE, opt und have_opt in _src/erreichbar.py entfernen.

## Paket-Audit und Korrekturen (25.10.2026, 21:30)
Prüf-Subagent (Lesezugriff, ohne Änderungen) hat das ganze Paket gegengelesen. Befunde mit Belegen nachgeprüft:
- **Berechtigung der Befehle (korrigiert):** `EntityKJS.runCommandSilent` läuft mit der Berechtigung des Spielers, `/function` und `/title` brauchen Stufe 2. Handbuch (`willkommen.js`) und Lagerfeuer-Titel (`lagerfeuer.js`) laufen jetzt über `Utils.server.runCommandSilent` (Konsolenrechte) mit `execute as <Spieler>`.
- **Herzschlag-Ton (korrigiert):** `playsound` ohne ausführende Entität war an den Welt-Spawn gebunden. Jetzt `execute as @a at @s`.
- **Tagebuchseite 18 (korrigiert):** Label „Bonusseite, ohne Zählung“ statt „Seite 18 von 18“, passend zum 17-Seiten-Archiv.
- **Dokumente (korrigiert):** Quest-Anzahl 185 in CLAUDE.md und README, Startinseln und Klassisch-Blöcke in CLAUDE.md, Skriptliste in CLAUDE.md (lagerfeuer.js, waechter.js), Feier-Zahl in TODO und Backlog.
- Neue Ladeprüfung: 12/12 KubeJS-Skripte, 185 Quests, `Done (1.972s)`, keine Fehler.

Offen, Entscheidung bei Leon (nicht geändert):
- Sternkiste enthält Netheritbarren, das Pipez-Ultimate-Upgrade (`balance.js`) wird damit umgangen. Balance-Entscheidung.
- Tagebuchseite 18 braucht eine Prüfung der Story-Passung.
- Ressourcenpakete `bare-bones` und `vanilla-exp` laden bei jedem Update, werden aber nicht genutzt. Entfernen?
- Mod-Überschneidungen: mouse-tweaks und inventory-essentials, ftb-ultimine und mining-gadgets (Mining Gadgets ohne Quest), mekanism-tools trotz Entscheidung „keine Werkzeugstufen“. Lithium und ModernFix melden Mixin-Konflikte im Log.
- Acht Mods sind nur bei CurseForge (`mode = "metadata:curseforge"`). Relevant, sobald verteilt wird (Punkt auf später gesetzt).
- Client-Lauf: Ein Prism-Protokoll vom 25.10. (19:17–19:44, Spieler LAB6) soll existieren. Nicht verifiziert, TEST_REPORT sagt noch „nicht möglich“.
- Historische Tabellen in TEST_REPORT.md (186 Quests, 6 Startinseln) bleiben als Protokoll stehen. Korrektur nur mit Hinweis.
- Keine Pack-Dateien außer den genannten geändert.

## Lauf 5: 43 offene Items geprüft (25.10.2026, nur Analyse, keine Kapitel geändert)
- Dump: zz_dev_recipejson.js schreibt jetzt Rezept-IDs und fail_types. 15467 Rezepte, 151 nicht serialisierbar: ShapedRecipe 40, MA Enchanter 42, ProductiveBees Spawning 33, Extruder 20, Ironjetpacks 12, ProductiveBees Fishing 3, CreateAddition Charging 1.
- _src/erreichbar.py: Rezepte aus den Mod-Jars (data/<ns>/recipe) ergänzt, Mystical-Agriculture-Essenz als Zutat modelliert. Ergebnis: 95 Aufgaben ohne Weg (vorher 96).
- Befund (belegt): MA-Config seedCraftingRecipes = false. Die Seed-Rezepte für Certus, Osmium, Zink, Kupfer, Kohle sind damit ausgeschaltet. Verbleibend: Infusion (seed/infusion), das braucht Certus-Essenz.
- Befund (belegt im Datensatz): Certus-Essenz hat im Datensatz genau ein Rezept, den Seed-Reprocessor, der selbst Seeds braucht. Das ist ein Zirkel ohne Startquelle. Ob im Spiel eine andere Quelle existiert (Mob-Drop, Essenz-Quelle), ist nicht belegt. Kein Essenz-Brunnen in der MA-Jar.
- Auswirkung: Quest-Gruppe "Felder aus Erz" (Akt III, Wahl "Erz ohne Sieb") hängt an diesem Zirkel. Die Wahl hat Alternativen (Laser, Bienen). Prüfen im Spiel, bevor Akt III als abgenommen gilt.
- Pack-Dateien: nicht geändert.

## Sternkiste, Mod-Überschneidungen, Restliste (25.10.2026, 21:40)
- Sternkiste: Netheritbarren entfernt (`_src/quests.py`, Tabelle `stern`). Netherit-Schrott bleibt drin, er erfüllt die Pipez-Sperre `#c:ingots/netherite` nicht.
- Mods entfernt (packwiz remove): `mekanism-tools` (Werkzeugstufen sind verworfen, keine Quest nutzt sie), `mining-gadgets` (überschneidet FTB Ultimine, keine Quest nutzt sie).
- Mods behalten, Überschneidung geprüft: Inventory Essentials nur Sortierung, Mouse Tweaks Ziehen und Scrollen. Keine Doppelfunktion. Lithium und ModernFix: nur Info- und Konfigurationsmeldungen im Log, kein Fehler, keine Änderung.
- Ressourcenpakete bleiben drin (Freigabe von Leon).
- Prism-Protokoll: Singleplayer-Lauf 25.10. 19:18–19:44 belegt, im Testbericht vermerkt.
- Dokumente korrigiert: README (Version, zwei Inseln, Startinventar ohne Haken, 19 Tausch-Quests), TEST_REPORT (Korrekturhinweis), CLAUDE (Mod-Liste).
- Ladeprüfung: `Done (1.834s)`, 12/12 KubeJS, 185 Quests, keine Fehler. Im Spiel NICHT GETESTET.
- Rückweg: `packwiz add mekanism-tools` und `packwiz add mining-gadgets`, Netherit in `quests.py` wieder eintragen, Generator, `packwiz refresh`.

## Sprint 7 Rest: Mekanism-Audit und Archiv-Feier (25.10.2026, 21:42)
- Mekanism-Ketten Akt II und III geprüft (Prüf-Subagent, Rezepte aus Dump und Mod-Jar). Keine Sackgasse. Drei Quests hängen an der Reaktor-Kette (Spätspiel): `p_pellet`-Polonium (akt3), Herzschlag/Antimaterie (akt3, SPS-Gas aus Polonium), MekaSuit (Pellet-Zutaten). Die Ketten sind im Jar belegt, aber im Spiel nicht getestet.
- Neu: Feier `p_archiv` („Das Archiv ist vollständig“), Abschluss des Sammelbuchs (Vorschlag A aus dem Endgame-Entwurf). In `FEIER` in `_src/quests.py`.
- Ladeprüfung: 12/12 KubeJS-Skripte, 185 Quests, `Done (1.380s)`, keine Fehler. Im Spiel NICHT GETESTET.
- Rückweg: Zeile in `FEIER` entfernen, `feier/p_archiv.mcfunction` löschen, Generator, `packwiz refresh`.

## Fallback Essenz im Mischer für Felder aus Erz (25.10.2026, nach Zustimmung von Leon)
- Geändert: kubejs/server_scripts/luecken.js. Create-Mischer-Rezepte: 4 Certus-Quarz, 4 Osmium-Barren, 4 Zinkbarren, je plus 1 Inferiumessenz ergeben 1 Essenz (Certus, Osmium, Zink). Beleg: Lauf 5 (Essenz nur über Seed-Zirkel im Datensatz, seedCraftingRecipes = false).
- Geändert: _src/texte_hauptstory.py, Hinweis an „Erz ohne Sieb“. Generator läuft: 185 Quests, 0 Layoutprobleme.
- Prüfung: Testserver-Kopie (ohne gesperrte Welt, Port 25599) lädt luecken.js, 15354 Rezepte. Erreichbarkeits-Check: Certus-Essenz und Certus-Seeds jetzt erreichbar, Zink vollständig, Osmium-Seeds nur über Fluid-/Chemie-Rezept (optimistisch). Aufgaben ohne Weg: 95 -> 79.
- Im Spiel NICHT GETESTET.
- Rückweg: die drei Rezepte in luecken.js entfernen (Block „Fallbacks“), Hinweis-Zeile in texte_hauptstory.py entfernen, Generator, packwiz refresh.

## Befund: Quest-IDs verschwunden (ID-Check gegen Backup 0.20.0)
- 3 IDs fehlen: Quest „Der magische Logistiker“ (key a_starbuncle, Kapitel ars) samt Aufgabe und Belohnung. Ursache: quests.py Z. 36 ersetzt a_starbuncle durch l_controller (Abhängigkeitsabbildung). Die Quest existiert in bausteine.py Z. 346 weiterhin, im Ausgabe-Set aber nicht mehr.
- Regel 6 in CLAUDE.md: IDs dürfen nicht entfallen. Fortschritt bereits abgehakter Spieler geht verloren. Nicht von mir geändert. Entscheidung offen (wiederherstellen oder bewusst entfernen mit Hinweis).
- Ursache der Änderung: nicht von mir. Vermutlich andere Sitzung (21:09 bis 21:11).

## Release 1.0.0 (25.10.2026, 21:52)
- `pack.toml`: Version 1.0.0. Index aktualisiert.
- Export: `Sky and Stone-1.0.0.mrpack` (7,4 MB), lokal erzeugt. Nicht veröffentlicht.
- Neu: `CHANGELOG_1.0.0.md` mit allen Änderungen seit 0.20.0, Entscheidungen und bekannten Einschränkungen.
- Status: Release-Kandidat. Ladeprüfung bestanden, im Spiel nicht getestet.
- Rückweg für die Version: `version` in `pack.toml` auf 0.20.0 setzen, `packwiz refresh`.

## Pehkui-Gimmick und Mrpack-Neubau (25.10.2026, 21:57)
- Neu: Mod `pehkui` (3.8.3, beide Seiten, keine Abhängigkeiten nötig).
- Neu: `kubejs/server_scripts/pehkui_pilze.js`. Rot = klein (0,5), braun = groß (2,0), Chorusfrucht = normal (1,0). Befehl `scale set base <wert> @s` als Spieler über den Server.
- Ladeprüfung: Pehkui lädt ohne Fehler, 13/13 KubeJS-Skripte, `Done (1.220s)`. Die Befehlswirkung im Spiel NICHT GETESTET.
- `Sky and Stone-1.0.0.mrpack` neu exportiert. Changelog ergänzt.
- Rückweg: `packwiz remove pehkui`, Datei `pehkui_pilze.js` löschen, Export neu.

## Entscheidung: Quest "Der magische Logistiker" bleibt entfernt (25.10.2026, Leon)
- Entscheidung: Die Quest wurde durch die andere Sitzung entfernt, sie bleibt entfernt. Ersatz-Abbildung in quests.py Z. 36 (a_starbuncle -> l_controller) bleibt.
- Folge: Spieler, die die Quest schon abgehakt haben, verlieren diesen Fortschritt. Das gehört in den Changelog von 1.0.
- Offen: bausteine.py Z. 346 enthält die Definition noch. Sie wird im Ausgabe-Set nicht mehr erzeugt. Aufräumen nur mit der anderen Sitzung abstimmen.

## Änderungsrunde (25.10.2026, 22:00)
- Neu: Advancements `riesenpilz`, `pilzgroesse`, `zurueck_zur_mitte`, `feuerstelle`.
- Geändert: `pehkui_pilze.js` (Titel-Rückmeldung), `lagerfeuer.js` (Rauch-Partikel), `waechter.js` (drei Zeilen dazu).
- Ladeprüfung: 13/13 KubeJS, 6371 Advancements, 185 Quests, `Done (1.826s)`. Nur die bekannten Ironfurnaces-Warnungen.
- Export `Sky and Stone-1.0.0.mrpack` neu gebaut. Changelog aktualisiert.
- Nicht umgesetzt, mit Grund: 8.3 Sieb-Fundgrube (kein Ereignis-Haken), 8.6 Schatzkarte (keine Strukturen), 8.7 Ersatz-Begleiter (Designentscheidung), 8.9 Leere-Nebel (Client-Ressourcenpaket, nicht im Spiel prüfbar).

## Entscheidungen Backlog 8.3, 8.6, 8.7, 8.9 (25.10.2026, 22:05)
- 8.3 gestrichen: Ex-Deorum-Sieb liefert ein Ergebnis pro Rezept, eine Zusatzbeute würde Konflikte erzeugen (Begründung in GAME_DESIGN).
- 8.6 gestrichen: Schatzkarten brauchen Strukturen, die die Welt nicht hat.
- 8.7 entschieden: kein Ersatz-Begleiter, Logistik über Create-Depot und Schubladen-Wand.
- 8.9 abgelehnt: Client-Nebel nicht prüfbar, Stabilität hat Vorrang.
- Keine Pack-Dateien geändert, keine Ladeprüfung nötig. Rückweg: die Entscheidungen in GAME_DESIGN und SCRUM zurücknehmen.

## Planänderung Messing-Kiste (25.10.2026, 22:08)
- Geprüft: Jobs+-Befehl `job` ist im Mod-Jar belegt, der Starttext stimmt.
- Neu: Tabelle `messing` in `_src/quests.py`, Wahl bei `c_messing` und `c_siebfabrik` in `_src/belohnungen.py` auf `messing` gesetzt (vorher `gold`).
- Ladeprüfung: 13/13 KubeJS, 185 Quests, 8 Belohnungstabellen, `Done (1.318s)`. Export neu gebaut.
- Rückweg: in `belohnungen.py` die beiden Einträge zurück auf `'gold'` setzen, Generator, `packwiz refresh`.

## 25.10.2026, 22:30 – Gesamtprüfung Code und Logik (ohne Serverstart)
- Testserver (PID 5008, seit 22:05) beendet. Letzter Start sauber (13/13 Skripte, 0 Fehler).
- Generator neu laufen lassen: Questdateien byte-gleich. Inseln mit gleichem Inhalt, Originale wegen Zeitstempel zurückgespielt (Index unverändert).
- Prüfskripte (Scratchpad): Questgraph, Datenpaket, `node --check`, Rezept-Simulation. Ergebnisse und 20 Befunde in `PRUEFBERICHT_1.0.0.md`, Aufgaben in `TODO.md` Phase 9.
- `.packwizignore`: `CHANGELOG_1.0.0.md` und `PRUEFBERICHT_1.0.0.md` ergänzt. Kein `refresh`, das `.mrpack` enthält den Changelog noch. Rückweg: die zwei Zeilen löschen.
- Sonst keine Änderung am Spielinhalt.


## 25.10.2026, 23:50 – Prüfsuite `_src/pruefen.py` (neue und überarbeitete Prüfskripte)
- Neu: `_src/pruefung/` (nicht im Paket, `_src/` ist ignoriert). Einstieg `python -I -X utf8 _src/pruefen.py` (ca. 2 min, `--schnell` ohne Rezeptmodell, `--selbsttest` = 197 Tests). Bericht: `_src/pruefung/bericht/PRUEFBERICHT.md`.
- Prüft: Questbuch-Dateien (IDs, Graph, Aufgaben, Belohnungen, Verweise, Sprache, Kapitel), ID-Stabilität gegen das letzte `.mrpack` (Quest-, Aufgaben-, Belohnungs-IDs, Kisten-Kennungen), Belohnungslogik (Belohnung erledigt fremde Quest, Tausch-Kreise, gleiche Kistendaten, Kistenchance), Paket (packwiz-Index/Hashes, Ignore-Liste, Mods, BOM/TOML/JSON, Dump-Alter, veraltete `_src/items.json`), Daten (Funktionen, Advancements, Befehls-Belohnungen, Startinventar, Item-IDs in KubeJS), Spiellogik (Rezept- und Weltmodell: Ist jede Aufgabe mit den bis dahin eingeführten Maschinen herstellbar? Welche Maschine fehlt, wer führt sie ein? Belohnungen, die Stufen überspringen; Items ohne Quelle; Items nur über Annahmen).
- Überarbeitet: `snbt.py` (typisierte Arrays, Escapes, Fehler mit Zeile/Spalte; liest alle 32 Questdateien gleich wie vorher), `idcheck.py` (Objektarten statt Textsuche, Standard-Referenz = neuestes `.mrpack`).
- Belegt aus Mod-Code (javap/Jar): Imbuement-Kammer erzeugt ohne Quellglas selbst Quelle; Ars-Vertraute spawnen auf Gras bei Licht > 8 in allen Oberwelt-Biomen (widerspricht REZEPT-SIM Befund 1 zum Starbuncle, im Spiel prüfen); Ex-Deorum-Fässer brennen bei heißem Grundfluid; fortgeschrittene Sifter-Netze nur im Messing-Sifter. Welt laut Testserver-Konfig: leerer Nether mit Festungen, End-Hauptinsel bleibt.
- Lauf 23:45: 3 Fehler, 12 Warnungen, 45 Hinweise. Am Spielinhalt nichts geändert. Prüfstatus: Tests grün, Befunde nicht im Spiel geprüft.
- Rückweg: `_src/pruefung/` und `_src/pruefen.py` löschen; `snbt.py`/`idcheck.py` aus `_backups/sky-and-stone-1.0.0-vor-pruefskripte-20261025/_src` zurückkopieren.

## 25.10.2026, 23:58 – packwiz refresh
- Grund: Prism meldete „Hash invalid“ für CHANGELOG_1.0.0.md (stand trotz .packwizignore im Index und war danach geändert). Befund der Prüfsuite (Paket).
- `packwiz refresh`: Datei aus dem Index entfernt, Index-Prüfung 0 Befunde. Spielinhalt unverändert. Rückweg: nicht nötig.

## 26.10.2026 – Phase 9 A/B und Phase 10 (Teil): Startausrüstung, Holzkiste, Hinweise
- Geändert: `_src/bausteine.py` (e_holz 8 → 5 Stämme), `_src/texte_hauptstory.py` (e_holz, j_obsidian mit Warnung und Diamantspitzhacke, Handbuch-Text 5 Stämme), `_src/quests.py` (string_mesh aus Tabelle `holz`), `_src/erreichbar.py` (Eis entfernt), `config/skyblockbuilder/starter_inventory.json5` (Eis entfernt), `kubejs/data/skyandstone/function/handbuch*.mcfunction` (5 Stämme), `kubejs/server_scripts/lagerfeuer.js` (`execute … at <Spieler>` für Partikel), `kubejs/server_scripts/pehkui_pilze.js` (Untertitel → actionbar).
- Nicht geändert: 9.4 Pilz-Essbarkeit (Entscheidung nötig, [B]), Lava- und Wassereimer (Entscheidung nötig), Netherit-Schrott in Sternkiste (Entscheidung nötig), Phase 10.6–10.9 (Vorschlag in TODO.md, Freigabe nötig).
- Generator: 20 Kapitel, 185 Quests, 8 Belohnungstabellen, 0 Layoutprobleme, 25 Linienkreuzungen (vorher 26).
- `packwiz refresh`: ok.
- Testserver: mit packwiz-installer synchronisiert (Java 21, Microsoft JDK), Start geprüft (siehe Eintrag unten).
- Rückweg: Sicherung `C:/Projekte/modpacks/_backups/sky-and-stone-0.20.0-vor-phase9-20261026` (`_src`, `config`, `kubejs`) zurückkopieren, dann Generator und `packwiz refresh`.
- Prüfstatus: Generator und Index geprüft. Im Spiel NICHT GETESTET.
- Testserver-Lauf 26.10.2026 08:53: Start mit Java 21 (Microsoft JDK) nach packwiz-installer-Sync, `Done (3.657s)`. KubeJS Server 13/13 Skripte, 0 Fehler, 0 Warnungen. Zwei ERROR-Zeilen: Curios „example“ und „feet“ (bekannt, siehe Prüfbericht). Serverprozess läuft noch, Beenden durch Leon nötig (Stopp-Befehl wurde vom Berechtigungssystem abgelehnt).

## 26.10.2026 – Phase 9 C bis E (Texte, Dokumente)
- Korrektur Vorlauf: Der Obsidian-Hinweis (9.3) gehört zu Q5 `e_cobble` („Stein aus dem Nichts“), nicht zu `j_obsidian`. Umgesetzt in `e_cobble`, `j_obsidian` enthält nur noch die Diamantspitzhacke. Der Eis-Tipp in `e_cobble` ist entfernt, weil Eis nicht mehr im Startinventar liegt.
- Geändert: `_src/texte_hauptstory.py` (w_start auf 4 Zeilen, e_raupe/e_sieb/e_feuernetz Faden-Zahlen, e_brocken 8 Brocken, e_eisen Ofenhinweis, e_lavatiegel Porzellan-Rezept, c_muehle Casing-Tipp, c_brenner ohne Pilzinsel), `_src/bausteine.py` (e_brocken 4 → 8 Chunks, e_tiegel und e_lavatiegel optional, c_rad mit 2 Andesite Casings), Handbuch (Silkworm, Crook, Flint Mesh).
- Docs: README, CLAUDE.md, TODO.md Version 1.0.0; GAME_DESIGN Tausch-Quests 19, Sternkiste und Messing-Kiste aktualisiert, 8.3-Begründung als fraglich markiert.
- Nicht geändert: 9.15 und 9.16 (Balance-Verdacht, erst messen).
- Generator: 20 Kapitel, 185 Quests, 0 Layoutprobleme. `packwiz refresh`: ok.
- Prüfsuite `--schnell`: 2 Fehler, beide Gruppen (Dachdecker, Brückenbauer) in verbrauchenden Aufgaben im Markt. Nicht Teil dieser Änderung, offen.
- Prüfstatus: Generator, Index und Prüfsuite geprüft. Testserver läuft noch mit dem Stand vor dieser Runde. Neustart mit Synchronisation nötig. Im Spiel NICHT GETESTET.
- Rückweg: Sicherung `C:/Projekte/modpacks/_backups/sky-and-stone-0.20.0-vor-phase9-20261026`.

## 26.10.2026 – Markt-Fehler Dachdecker und Brückenbauer behoben
- Ursache: `x_dach` und `x_bruecke` nutzten Item-Gruppen (`skyandstone:roofs`, `skyandstone:rope_bridges`) in verbrauchenden Aufgaben. Das verletzt Projektregel 4.
- Geändert: `_src/quests.py` (DEKO nutzt feste Eichen-Items, keine Gruppen-Überschreibung mehr), `_src/texte_abenteuer.py` (Texte „Eichen-Dachblöcke“, „Eichen-Hängebrücken“). Die Gruppen bleiben bei `u_dach` und `u_bruecke2` (nicht verbrauchend).
- Folge: Für den Markt zählt nur noch Eichen-Dach und Eichen-Brücke. Das ist ein Rückschritt gegenüber dem Spieltest-Wunsch aus 0.6.2 („nicht nur Eichenholz“).
- Nebenwirkung: Die Aufgaben-IDs der beiden Markt-Quests haben sich geändert. Gespeicherter Fortschritt dieser zwei Quests kann in bestehenden Welten zurückgesetzt sein (Prüfbericht Zeilen 40–41).
- Generator: 185 Quests, 0 Layoutprobleme. `packwiz refresh`: ok. Prüfsuite `--schnell`: 0 Fehler, 5 Warnungen, 22 Hinweise.
- Im Spiel NICHT GETESTET. Testserver läuft noch mit dem alten Stand.

## 26.10.2026 – Startinventar: Knochenmehl entfernt (Eimer offen)
- Auf Wunsch von Leon: 16 Knochenmehl aus dem Startinventar entfernt. Eimer (Lava, Wasser) bleiben vorerst drin, siehe unten.
- Geändert: `config/skyblockbuilder/starter_inventory.json5`, `_src/erreichbar.py` (Startliste), `_src/texte_hauptstory.py` (Hinweis bei `e_holz`: Knochenmehl kommt jetzt aus dem Kompostfass).
- Prüfung: Rezept-Simulation vorher und nachher 0 Lücken, 240 Item-Aufgaben. Generator: 185 Quests, 20 Kapitel, 0 Layoutprobleme.
- Offen: Eimer. Die Quest „Stein aus dem Nichts“ (`e_cobble`) braucht Lava- und Wassereimer. Ohne sie geht sie erst mit Eisen (Eisenschwelle). Das ist eine Progressionsentscheidung von Leon.
- Offen: Testserver-Start (Pflichtprüfung) ist noch nicht gelaufen. Im Spiel NICHT GETESTET.
- Rückweg: Sicherung `C:/Projekte/modpacks/_backups/sky-and-stone-1.0.0-vor-startinventar-20261026` (nur `_src` und `config/skyblockbuilder`).

## 26.10.2026 – Eimer aus dem Startinventar, Bruchstein-Generator nach Eisen
- Auf Wunsch von Leon: Lava- und Wassereimer aus dem Startinventar entfernt. Der Bruchstein-Generator (`e_cobble`) braucht jetzt einen Eimer aus Eisen und hängt an `e_eisen`.
- Die Kette Hammer → Sieb → Erz → Eisen bleibt intakt: `e_hammer` hängt jetzt an `e_fass` statt an `e_cobble`. Der Hammer braucht nur Bruchstein, den die Startinsel liefert (Insel-Filler „stone“ in `inseln.py`).
- Geändert: `config/skyblockbuilder/starter_inventory.json5`, `_src/erreichbar.py`, `_src/bausteine.py` (Position und Abhängigkeiten von `e_cobble`/`e_hammer`, Text), `_src/texte_hauptstory.py` (Text `e_cobble`, Hinweis Eis entfernt), `_src/quests.py` (Vorgängerliste). Quest-IDs unverändert.
- Prüfung: Rezept-Simulation 0 Lücken, 240 Item-Aufgaben. Generator: 185 Quests, 20 Kapitel, 0 Layoutprobleme, 26 Linienkreuzungen (vorher 25). `packwiz refresh`: ok.
- Offen: Testserver-Start (Pflichtprüfung) ist nicht gelaufen. Im Spiel NICHT GETESTET.
- Offen: Der Hammer braucht Bruchstein vor dem Eisen. Ob die Startinsel genug Stein für Hammer und Sieb hergibt, ist im Spiel zu prüfen.
- Offen: `j_obsidian` verlangt Wasser auf eine Lava-Quelle. Das geht jetzt erst mit Eimer aus Eisen. Der Text bleibt, prüfen.
- Rückweg: Sicherung `C:/Projekte/modpacks/_backups/sky-and-stone-1.0.0-vor-startinventar-20261026` (vor der Knochenmehl-Änderung, die Eimer-Änderung kommt davon hinzu; `_src` und `config/skyblockbuilder` zurückkopieren und `packwiz refresh`).

## 26.10.2026, Mittag – Version 1.0.1: offene Tests, Entscheidungen, Prüfsuite, Prüfungen der Leere
- Entscheidungen Leon (im Chat, 26.10.): alten Testserver beenden (lief seit 08:52 ohne Eingabe, alter Stand); Pilze essbar machen; Netherit-Schrott nur beim Wither ersetzen; Lootkisten: Texte + Story-Beute, kein Preis.
- Korrektur zur Netherit-Frage: Ich hatte „Sternkiste selten 1 Schrott“ geschrieben, richtig sind 4 Schrott je Treffer (Gewicht 5/23, 2 Ziehungen). Neu zu entscheiden (TODO, Phase 4).
- Geändert (Paket): `kubejs/startup_scripts/pilze_essbar.js` (neu), `kubejs/data/skyandstone/loot_table/ruinen/fund.json` (dritter Pool: 4 Erinnerungsstücke, übrige Pools unverändert), `kubejs/client_scripts/hinweise.js` (erzeugt: Kisten-Tooltips), `config/ftbquests/` (erzeugt: 3 neue Prüfungen, `max_input` an Strom-Aufgaben, Messing-Kiste, Belohnungen u_dach/j_wither, b_zentri hängt an e_eisen).
- Geändert (`_src`, nicht im Paket): `questlib.py` (max_input, BEKANNTE_MOBS), `quests.py` (Kisten-Prüfung, questindex.json, Messing-Kiste, Prüfungen, b_zentri), `belohnungen.py`, `hinweise_daten.py` (KISTEN), `texte_abenteuer.py`, `items.json`/`tags.json` (aus den Dumps 26.10. 12:29), neu `testlauf.py`, `ki_frage.py`, `pruefung/texte.py`, `pruefung/tests/test_texte.py`; `pruefung/struktur.py` (max_input), `pruefung/daten.py` (pruefe_essen), `pruefen.py`.
- Testserver-only: `kubejs/server_scripts/zz_dev_pruefdaten.js` (Register-Dump für die Prüfsuite). Erste Fassung erzeugte 17 RuntimeDistCleaner-ERROR (Rhino reflektiert Item-Unterklassen), umgebaut auf `Item.of(id)`, danach 0 neue ERROR.
- Fund im FTB-Quests-Jar (2101.1.37, javap): `EnergyTask.readData` setzt `maxInput = getLong("max_input")`, also 0 ohne Schlüssel; `TaskEnergyHandler.receiveEnergy` nimmt `min(maxInput, …)`. „Der Speicher der Erbauer“ (10 Mio. FE) war damit unlösbar. Generator setzt jetzt `max_input = value`.
- FreeLLMAPI-Zweitmeinung (Modell fusion, 207 s): Briefing `_src/KI-PRUEFUNG/BRIEFING-2026-10-26.md`, Antwort `ANTWORT-2026-10-26-fusion.md`. Übernommen: Festungs-Jagd, Endgame-Strom, Technik-Kistenzeile. Abgelehnt mit Grund: „Quelle“ ist der Ars-Rohstoff, „Herzschlag“ ist Story-Bezug, Antimaterie/End betreten sind schon Hauptstory, „alle 4 Erinnerungsstücke“ geht nicht (eine Ruinen-Truhe je Spieler). Wahl-Folgen als Idee in TODO Phase 5.
- Prüfung: Generator 20 Kapitel, 188 Quests, 8 Tabellen, 0 Layoutprobleme, 26 Kreuzungen. `idcheck.py` gegen die Sicherung: 0 entfallen, 3 neu. Selbsttest Prüfsuite: 210 Tests OK. Testlauf 12:5x (`_src/testlauf.py`): Done (2.428s), KubeJS Startup 2/2 und Server 14/14 ohne Fehler, 0 fehlgeschlagene Rezepte, FTB Quests 20/188/8, 0 neue ERROR (2 bekannte Curios-Zeilen). Server danach sauber per `stop` beendet. Register: beide Pilze haben die Nahrungs-Komponente.
- Im Spiel NICHT GETESTET: Pilze essen, Kisten-Tooltips (Client-Skript), Erinnerungsstücke, neue Prüfungen, Strom am Aufgabenbildschirm.
- Rückweg: Sicherung `C:/Projekte/modpacks/_backups/sky-and-stone-1.0.0-vor-sitzung-26-10-mittag-20261026` (`_src`, `config`, `kubejs`, `pack.toml`, `index.toml`) zurückkopieren, `kubejs/startup_scripts/pilze_essbar.js` löschen, `packwiz refresh`.

## 26.10.2026, 13:10 – Akt I: Reihenfolge und Tiegel für die klassische Insel (Befund der vollen Prüfsuite)
- Befund: Volle Prüfsuite 12:56 (Spiellogik) meldete 44 Warnungen; fast alle mit „Oak Crucible … keine Voraussetzung dieser Quest“. Ursache geprüft: Die klassische Insel (`_src/inseln.py`, `klassisch()`) hat nur Gras, Erde, einen Baum und Grundgestein, kein Wasser, keinen Stein. Seit Lava- und Wassereimer aus dem Startinventar sind (Eintrag 26.10. vormittags), gibt es dort Wasser nur aus dem Holztiegel und Bruchstein nur aus Stone Pebbles vom Sieb (Rezept `exdeorum:cobblestone`, 2×2 Pebbles). Die Annahme „Der Hammer braucht nur Bruchstein von der Startinsel“ galt nur für die Waldlichtung.
- Geändert: `_src/bausteine.py` (e_hammer an e_sieb, e_sieb ohne e_hammer, e_tiegel und e_lavatiegel nicht mehr optional), `_src/quests.py` (AKT1-Pfad Sieb → Hammer → Brocken; zusätzliche Abhängigkeiten c_rad→e_tiegel, c_brenner/e_cobble/j_obsidian→e_lavatiegel, e_lavatiegel→e_hammer), `_src/texte_hauptstory.py` (Hammer: Stone Pebble; Tiegel: einzige Wasserquelle ohne Teich; Bruchstein-Generator und Wasserrad: Wasserquellen), `_src/belohnungen.py` (s_mechhammer Sand statt Bruchstein).
- Prüfsuite verfeinert: `&` mit Leerzeichen kein Farbcode, Mengen nach „ergeben/=/→“ zählen nicht, Story-Notiz zählt nicht zum Zeilenlimit; Ausnahmen für Start-Quest und „Erz ohne Sieb“ mit Begründung. Selbsttest 213 OK.
- Generator: 188 Quests, 0 Layoutprobleme, 31 Linienkreuzungen (vorher 26). Quest-IDs unverändert (nur Abhängigkeiten).
- Im Spiel NICHT GETESTET: Frühspiel auf der klassischen Insel (Pebbles → Bruchstein → Hammer, Wasser aus dem Holztiegel ohne Eimer).
- Rückweg: Sicherung wie im Eintrag „Mittag“.
- Abschluss 13:10: Version 1.0.1 (`pack.toml`), `packwiz refresh`, Testlauf grün (Done 2.499s, 2/2 + 14/14 KubeJS, 0 Rezeptfehler, 20/188/8, 0 neue ERROR), volle Prüfsuite 0 Fehler / 9 Warnungen (alle bekannt) / 53 Hinweise / 3 akzeptiert. Export `Sky and Stone-1.0.1.mrpack`. Im Spiel NICHT GETESTET.

## 26.10.2026 – Startinventar ohne Eimer (Stand auf der Festplatte)
- `config/skyblockbuilder/starter_inventory.json5`: Lava- und Wassereimer sind raus, Eis war schon raus. Das Startinventar enthält jetzt Fackeln, Gießkanne, Brot, Knochenmehl und Setzlinge.
- Korrektur (26.10.2026, 15:00, Sitzung „Modpack-Projekt Entwicklung fortsetzen“): Laut Datei (Stand 11:57) enthält das Startinventar Questbuch, Fackeln, Holz-Gießkanne, Brot und Eichensetzlinge. Knochenmehl ist seit dem Vormittag nicht mehr drin.
- Passend dazu: `e_cobble` (Stein aus dem Nichts) verlangt einen Eisen-Eimer (3 Barren). Der Text ist angepasst. `erreichbar.py` enthält keine Eimer und kein Eis mehr (Stand auf der Festplatte).
- Offen: Im Spiel prüfen, ob der Einstieg ohne Eimer flüssig ist (siehe TODO, Phase 1, „Klassische Insel ohne Eimer“).
- Nicht im Spiel getestet.

## 26.10.2026, 15:05 – Version 1.1.0 „Die sieben Splitter“ (Auftrag Leon: große Weiterentwicklung, ohne Rückfragen)
- Neu (Paket): `kubejs/startup_scripts/herz_items.js`, `kubejs/server_scripts/herz_rezepte.js` (12 Rezepte), `kubejs/server_scripts/herz_ritual.js`, `kubejs/assets/skyandstone/` (Texturen, Lang), `kubejs/data/skyandstone/structure/werkstatt.nbt`, `loot_table/werkstatt/fund.json`, `kubejs/data/minecraft/loot_table/entities/enderman.json` (Vanilla + Leerenessenz), Advancements `splitter_*`, `herz_gebaut`, `waechter_besiegt`, `herz_erwacht`, `erster_herzschlag`, Funktionen `waechter/*`, `feier/splitter_*`, `feier/herz_erwacht`; load/tick ergänzt.
- Neu (`_src`): `texturen.py`, `werkstatt.py`, `herz_daten.py`, `texte_herz.py`, `DESIGN-HERZ-DER-LEERE.md`; Generator: Aufgaben `beobachte`/`fortschritt`, Kapitel `akt4`, 15 Quests, Belohnungen, Sperrliste; `namen.py` liest Pack-Lang; Prüfsuite: `effect give` kein Fehlalarm. Testserver-only: `zz_dev_recipejson.js` schreibt den Rezept-Typ mit.
- Funde: KubeJS `runCommandSilent` ist void (Prüfungen per Blockabfrage/Scoreboard); `execute positioned` mit ganzen Zahlen zentriert schon (Marker-Versatz behoben).
- Prüfung: Generator 21 Kapitel/203 Quests/0 Layoutprobleme; `idcheck` 0 entfallen; Testlauf grün; Konsole: Boss 400 Leben, Skalierung 2,5, Abbruch nach Nicht-Spieler-Tod, Sieg setzt `herz_erwacht`, Werkstatt platziert, Beute fällt; Prüfsuite schnell 0/0. Export `Sky and Stone-1.1.0.mrpack`. Volle Prüfsuite (Spiellogik) nicht erneut gelaufen.
- Im Spiel NICHT GETESTET: Splitter herstellen, Karte, Bosskampf mit Spieler, Herzschlag, Client-Grafik.
- Rückweg: Sicherung `_backups/sky-and-stone-1.0.0-vor-sitzung-26-10-mittag-20261026` bzw. Export 1.0.1.

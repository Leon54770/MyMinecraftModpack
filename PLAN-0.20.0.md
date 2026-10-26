Stand: 25.10.2026 · Entwurf · Basis 0.11.1

# Plan Sky and Stone 0.20.0

Dieser Plan beruht auf dem Projektstand (Dateien, Logs, Notizen) und auf einer kleinen Recherche. Die Recherche ist dünn: Die Websuche findet fast nur Listen, kaum Reddit-Threads zu den Vergleichspacks. Alles, was aus Quellen kommt, ist entsprechend markiert.

## 1. Was Vergleich und Feedback tatsächlich zeigen

**Quellen (Recherche 25.10.2026)**
- ATM-10 Quest-Balance: Ein Feedback-Thread auf GitHub kritisiert, dass das Questbuch Belohnungen gibt, die Fortschrittsschranken überspringen (z. B. Erz sofort in der Dimension). Quelle: https://github.com/AllTheMods/ATM-10/discussions/3539 (betrifft den Hauptpack, nicht To the Sky).
- StoneBlock 4: Ein Review lobt flüssige Progression, verzweigte Pfade und die Story „World Engine“. Kritik: Events, die der Tester abschaltete. Quelle: https://mmcreviews.com/all/modpacks/ftb-stoneblock-4/
- ATM10 To the Sky: Sehr wenige Bewertungen (2,8/5 bei 3 Stimmen). Ein Kommentar: „poliert, aber wenig spannend“, Ressourcen-Erzeugung wiederholend. Quelle: https://moddex.gg/modpack/all-the-mods-10-sky
- SkyFactory 5: Community gespalten zwischen Originalität des Farbsystems und dem bewährten SkyFactory-4-Modell. Die letzte Version ist von März 2025. Quelle: https://topmoddedservers.com/en/guides/modpack-skyfactory
- Allgemeine Frust-Muster (Hypixel SkyBlock, Server-Spiel, nicht Modpack): Inhalte, die „dünn gestreckt“ sind, und Grind, der als Progression verkauft wird. Quelle: https://hypixel.net/threads/skyblock-has-gotten-way-too-comfortable-with-wasting-the-player%E2%80%99s-time.6152287/

**Was das für Sky and Stone heißt (abgeleitet, nicht bewiesen)**
- Belohnungsschranken sind das häufigste Konstruktionsrisiko. Unser Pack hat Quest-Belohnungen mit Kisten, eine Inselmarkt-Schleife (17 Tausch-Quests) und Mob-Beutekisten. Das muss geprüft werden.
- Story und verzweigte Pfade kommen bei StoneBlock gut an. Unsere Wahlen sind das richtige Thema, aber ohne Folgen wirken sie beliebig.
- Das Spielgefühl „poliert, aber langweilig“ ist die größere Gefahr als Fehler. Dagegen helfen die Playtests.
- Ein Hinweis aus dem Projekt selbst: Das Feedback vom 0.6.1-Test („nur Eichenholz erlaubt“) war ein echter Fehler, der sich nur im Spiel zeigt. Das ist unsere wertvollste Quelle.

**Was wir nicht wissen**
- Keine belastbaren Reddit-Daten zu Sky and Stone oder den Vergleichspacks. Die Suche hat nur Listen gefunden.
- Keine Daten zur tatsächlichen Spielzeit bis zum Finale. Der Spieltest (MORGEN-PLAYTEST.md) liefert das erst.

## 2. Was fehlt, was doppelt ist

**Fehlt (begründet):**
1. **Belohnungs-Audit:** Keine automatische Prüfung, ob eine Quest eine Belohnung gibt, die spätere Stufen überspringt. Wird als Generator-Check gebaut (`_src/`, nicht in der Quest-Datei).
2. **Stufen-Sperren ohne Game-Stages-Mod:** Das Pack hat keinen Stages-Mod. Konsequenzen einer Wahl brauchen daher einen Weg über FTB Quests oder KubeJS. Ob FTB Quests das zuverlässig kann, ist ungeprüft.
3. **Stuck-Quest-Test:** Die Quellen (ZC Skyfactory) zeigen Quests, die nach Abgabe weiter als unerledigt gelten. Bei uns ungeprüft, besonders bei Item-Gruppen (TODO-0.7).
4. **Team-Fortschritt:** Team-Belohnungen gibt es nur beim Inselmarkt. Solo und Koop sind nicht getestet.
5. **Ein Ort für Spielerfeedback:** Das Playtest-Dokument ist Fragebogen, aber kein Feedback-Log mit Versionsbezug.

**Doppelt oder überflüssig:**
- Die Änderungen zu Pipez, Essenz-Stufen und Sieb sind bereits in `balance.js` und `sieben.js`. Nicht erneut anfassen, nur testen.
- Die Story-Notizen (14 Meilensteine, 17 Tagebuchseiten) sind eigenständig. Keine Zweitfassung.

## 3. Ziel von 0.20.0

Ein Pack, das sich nach einem Spiel anfühlt: klare Progression, spürbare Wahl, keine Belohnungs-Abkürzungen, bessere Fehlerfestigkeit. Keine neuen großen Mods, keine neue Dimension (passt zur Leitidee: kein Grind, Technik und Magie gleichwertig).

## 4. Arbeitspakete

Reihenfolge: zuerst Messung und Tests, dann Inhalte. Jedes Paket hat Prüfung und Rückweg.

| # | Paket | Inhalt | Prüfung | Rückweg |
|---|---|---|---|---|
| P1 | Playtest auswerten | MORGEN-PLAYTEST ausfüllen lassen, Befunde in `FEEDBACK-LOG.md` mit Version | Manuell | – |
| P2 | Belohnungs-Audit | Generator prüft je Quest-Belohnung, ob sie eine spätere Stufe überspringt | Lauf von `quests.py` mit neuem Check, 0 Treffer oder begründet | Check abschaltbar |
| P3 | Stuck-Quest-Test | Testserver: Items in Gruppen-Aufgaben abgeben, prüfen ob die Quest abgeschlossen wird | Testserver-Log und Quest-Stand | Gruppenaufgaben zurück auf festes Item |
| P4 | Wahlen Akt III | Wahl-Folgen über FTB Quests klären (Sperren, Freischaltung) oder KubeJS. Vorher prüfen, was FTB Quests kann | Testserver mit beiden Pfaden | Alte Quest-Datei aus `_backups` |
| P5 | Team-Fortschritt | Entscheiden, welche Belohnungen team- statt spielerbezogen sein sollen | Testserver mit zwei Spielern (manuell) | Schalter in `belohnungen.py` |
| P6 | Frühspiel | Nach Playtest: Eisenbarren-Schritt anpassen (ggf. 4 → 2 Barren) | Manuell + Quest-Layout | Einzelwert |
| P7 | Item-Gruppen | TODO-0.7 umsetzen, Mitglieder vorher in `tags.json` prüfen | Generator-Check, Testserver | Gruppe zurück auf Item |
| P8 | Log-Reste | Curios-Slots und Mixin-Warnungen prüfen, unnötige Referenzen entfernen | Serverlog | Config-Backup |
| P9 | Versionssicherheit | Update-Adresse statt `file:///`, Changelog, `.mrpack` | Export und Import in Prism | – |

## 5. Was 0.20.0 nicht enthält
- Keine neuen Mods außer klar begründeten.
- Keine Umstrukturierung der 186 Quests. Die Quest-IDs hängen am Kapitelnamen, Verschieben löscht Fortschritt.
- Keine neuen Dimensionen.

## 5a. Wegabhängige Rezepte: Befund (25.10.2026)

Entschieden vom Nutzer: Wahl-Folgen über **wegabhängige Rezepte**. Prüfung am Jar-Inhalt der installierten Mods (`ftb-quests-neoforge-2101.1.37`, `ftb-teams-neoforge-2101.1.11`, `kubejs-neoforge-2101.7.2-build.377`):

**Bestätigt (Klassen im Jar vorhanden)**
- FTB Quests hat `StageReward` (vergibt eine Team-Stufe) und `StageTask` (prüft sie). Beide nutzen FTB Teams über `TeamStagesHelper` (`addTeamStage`, `removeTeamStage`, `hasTeamStage`).
- FTB Quests hat einen `StageBarrierBlock` (Sperrblock, der an Stufen hängt).
- KubeJS hat eigene Stufen-Events (`StageChangedEvent`, `player.stages`-Umfeld) und Befehle (`StageCommands`).
- Nur FTB Quests und FTB Teams lesen Team-Stufen. Kein installierter Mod filtert Rezepte nach Stufe.

**Nicht bestätigt**
- Ob KubeJS Rezepte pro Team oder Spieler über Stufen filtern kann. Im `RecipeFilter` der KubeJS-Klasse fand sich kein Stufen-Bezug. Der Fund ist kein Beweis.
- Ob der `StageBarrierBlock` Rezept-Ausgabe oder nur Interaktion sperrt.
- Ob `ServerEvents.recipes` pro Team wirken kann. Rezepte sind global, sie sind nicht pro Spieler sichtbar.

**Folgerung für Wahl-Folgen**
1. Wahl-Quest vergibt eine Team-Stufe (`StageReward`), nicht nur Kisten.
2. Die Folge wird **nicht** durch Entfernen globaler Rezepte gelöst, sonst würde jede Wahl alle Teams betreffen.
3. Stattdessen Spike im Testserver: a) Prüfen, ob ein Stufen-Reward im Testserver zu einer Sperre führt (StageBarrierBlock an einer Maschine). b) Prüfen, ob KubeJS ein Event für Craften oder Ausgabe bei Stufe abfangen kann (Ergebnis zurückgeben, nicht global entfernen).
4. Erst wenn a oder b funktioniert, werden wegabhängige Rezepte umgesetzt. Sonst fällt die Wahl auf Belohnungen plus Quest-Gates zurück.

**Empfehlung:** Den Spike vor dem Ausbau machen, weil er die Grundlage für alle Wahl-Folgen ist.

### Spike-Ergebnis (25.10.2026, Testserver)
- Skript `_testserver-sky-and-stone/spike/zz_spike_stages.js` mit `ItemEvents.crafted` und `event.player.stages.has('spike_test')`. Serverstart: `Loaded 10/10 KubeJS server scripts … with 0 errors`, `Done (2.498s)`. **Das Skript lädt**, die Namen der Events und die Stufen-Abfrage sind im Startlog nicht als falsch aufgefallen.
- **Nicht getestet:** Ob der Handler beim Craften läuft und ob `player.stages.has` einen echten Wert liefert. Dafür braucht es einen Spieler. Der Testserver hat keinen Client und RCON ist aus.
- **Nicht getestet:** Ob ein `StageBarrierBlock` eine Maschine für Spieler ohne Stufe sperrt.
- **Ergebnis:** Der Spike ist teilweise. Der Ladeteil ist bestätigt, die Wirkung nicht. Die Machbarkeit wegabhängiger Rezepte ist damit **nicht** bewiesen.

**Nötig für den vollständigen Test (manuell in Prism, zwei Welten oder Spieler):**
1. Spieler A craftet etwas mit der Stufe `spike_test` gesetzt (Befehl oder Quest-Belohnung) und Spieler B ohne Stufe. Im Log steht bei beiden `SPIKE crafted … stage spike_test=true/false`.
2. Eine Maschine mit Stufen-Sperrblock: Spieler ohne Stufe kann sie nicht öffnen.

## 6. Offene Fragen an dich
1. Beantwortet: Wegabhängige Rezepte, mit Spike zur Machbarkeit (Abschnitt 5a).
2. Soll Koop Pflicht für Team-Belohnungen werden oder optional bleiben?
3. Wie viel Zeit bis zum Finale ist das Ziel (Stunden)?

## Quellen
- https://github.com/AllTheMods/ATM-10/discussions/3539
- https://mmcreviews.com/all/modpacks/ftb-stoneblock-4/
- https://moddex.gg/modpack/all-the-mods-10-sky
- https://topmoddedservers.com/en/guides/modpack-skyfactory
- https://hypixel.net/threads/skyblock-has-gotten-way-too-comfortable-with-wasting-the-player%E2%80%99s-time.6152287/

## Status (25.10.2026, nach 0.11.2)
- **P2 Belohnungs-Audit:** Auswertung als Dokument erledigt, siehe `AUDIT-BELOHNUNGEN-0.11.md`. Kein Generator-Check gebaut. Gleichgewichtsänderungen erst nach Spieltest.
- **P7 Item-Gruppen (TODO-0.7):** Fast wirkungslos, weil Almost Unified jeden Barren-Tag auf ein Item reduziert. Nicht umgesetzt. Empfehlung: schließen.
- **Starttext:** Ziel und erster Schritt in 0.11.2 ergänzt.

## Feature-Erweiterungen (Kandidaten, 25.10.2026, noch nicht installiert)

Stand der Suche: Modrinth-API, Filter NeoForge + MC 1.21.1. Nur Name, Downloads und Kurzbeschreibung geprüft. **Nicht geprüft:** Abhängigkeiten, Konflikte mit den 118 Mods, Server/Client-Seite, Lizenz, Verhalten in Skyblock-Welt.

**Abenteuer außerhalb der Insel**
- Lootr (Slug `lootr`, ~24 Mio Downloads): Loot-Truhen pro Spieler instanziert. Passt zum Koop-Ziel, weil jeder seine Beute bekommt. Kandidat Nr. 1.
- Dungeons and Taverns (Datenpaket, nur Strukturen) oder When Dungeons Arise: Risiko Skyblock-Welt. Strukturen brauchen Boden, die Insel-Welt hat keinen. **Vor Einbau testen**, sonst keine Wirkung.

**Wirtschaft außerhalb des Inselmarkts**
- Jobs+ (`jobsplus`, 10 Berufe, erweiterbar): Berufe als Spielschleife. Kandidat, falls Berufe gewünscht.
- Shop- und Währungs-Mods (AVECOINS, SDM Shop, MMO Econ u. a.): Konflikt mit der Quest-Belohnungslogik. **Nicht empfohlen**, weil dann zwei Wirtschaften konkurrieren.

**Werkzeugstufen**
- Expanded Equipment Tools and Armor (`expanded-equipment-tools-and-armor`): neue Werkzeugstufe, Konflikt mit Mekanism-Werkzeugen möglich. Prüfen.
- Melded (modulare Werkzeuge, ~478 Downloads): kleiner, aber unbekannte Reife.
- Tinkers' Construct: in der Suche nur ein inoffizieller Port gefunden, kein offizieller 1.21.1-Eintrag. **Nicht verifiziert**, nicht empfohlen, bevor der offizielle Stand geprüft ist.

**Empfehlung:** Erst Lootr testen (ein Mod, geringes Risiko, klarer Nutzen). Werkzeugstufen und Jobs danach. Wirtschaft nicht einführen.

## Stand 0.20.0 (25.10.2026)
- Umgesetzt: Lootr und Jobs+ (mit Abhängigkeiten) im Pack, Hinweise im Starttext, Changelog `CHANGELOG_0.20.0.md`, Mrpack exportiert.
- Testserver mit dem Pack-Stand: Start `Done (1.053s)`, 186 Quests, KubeJS 9/9 ohne Fehler, 0 fehlgeschlagene Rezepte.
- Nicht übernommen: When Dungeons Arise (Fortschritts-Fehler, Strukturen ungeprüft), Expanded Equipment (unreif), Wirtschaftsmods (Konkurrenz zu Belohnungen).
- Offen: Spieltest für Lootr und Jobs+, Entscheidung zu When Dungeons Arise nach Test in einer Skyblock-Welt.
- Quest-Hinweise statt eigener Quests: Lootr-Truhen sind nicht craftbar, und Jobs+-Items habe ich nicht verifiziert.

## Dokumentation (25.10.2026)
Die Ergebnisse der Phasen A bis F liegen in: `PROJECT_AUDIT.md`, `MODPACK_COMPARISON.md`, `GAME_DESIGN.md`, `TEST_REPORT.md`, `IMPLEMENTATION_LOG.md`. Alle sind in `.packwizignore` und gehen nicht ins Paket.

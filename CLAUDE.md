# CLAUDE.md – Sky and Stone

Stand: 26.10.2026 · Pack-Version 1.0.1 (`pack.toml`) · Projekt-Hirn für Claude Code.

Zuerst lesen: `TODO.md` (was offen ist), `GAME_DESIGN.md` (Progression), `TEST_REPORT.md` (was tatsächlich geprüft ist). Danach nur gezielt, nicht den ganzen Ordner.

## Projekt-Vision & System

**Pack:** Sky and Stone, deutsches Skyblock-Modpack von Leon. Start auf einer Insel mit dem Ex-Deorum-Sieb, danach Technik (Create, Mekanism, AE2) und Magie (Mystical Agriculture, Ars Nouveau) bis zum Finale.

**Plattform:** Minecraft 1.21.1, NeoForge 21.1.264 (`pack.toml`). Kein Fabric, kein Forge. Der Testserver lief zuletzt auf Java 21 (Start bestanden). Das Java der Prism-Instanz ist nicht dokumentiert.

**Kern-Thema:** Die Welt ist in Inseln zerbrochen („Das Herz der Leere“). Der Weg der Erbauer hat drei Akte (Ein Splitter im Nichts · Die Maschinen erwachen · Das Herz der Leere). Die Notizen des letzten Wächters liegen als Tagebuchseiten im Spiel und führen zum Finale.

**Zielgerät:** Laptop mit Intel Iris Xe, 5–6 GB RAM für Minecraft. Gaming-PC mit 8 GB. Performance ist auf dem Laptop noch nicht gemessen.

**Werkzeuge und Ablauf:**
- **packwiz** verwaltet den Pack. Dieser Ordner ist die Quelle. Nach jeder Änderung `..\tools\packwiz\packwiz.exe refresh` im Pack-Ordner. Export: `..\tools\packwiz\packwiz.exe modrinth export` → `Sky and Stone-<version>.mrpack`.
- **Questbuch-Generator:** `python -I -X utf8 _src/quests.py` (aus dem Pack-Ordner). Er schreibt nur, wenn alle Prüfungen bestehen.
- **Testserver:** `C:\Projekte\modpacks\_testserver-sky-and-stone`. Er zieht den Stand per packwiz-installer aus diesem Ordner. Log: `logs\latest.log`.
- **Testlauf:** `python -I -X utf8 _src/testlauf.py` synchronisiert, startet den Server mit Eingabe-Pipe, prüft das Log (Done, KubeJS, Rezepte, Quest-Anzahl, neue ERROR-Zeilen) und stoppt ihn sauber. Bericht `_src/pruefung/bericht/TESTLAUF.md`. Den Server nie ohne Eingabe starten, sonst lässt er sich nicht mit `stop` beenden.
- **Prüfsuite:** `python -I -X utf8 _src/pruefen.py` (voll, ca. 2–3 min), `--schnell`, `--selbsttest`. Bericht `_src/pruefung/bericht/PRUEFBERICHT.md`.
- **Zweitmeinung:** `python -I -X utf8 _src/ki_frage.py "Frage" -f datei -m fusion -o antwort.md` über FreeLLMAPI (127.0.0.1:31415). Antworten sind Vorschläge, siehe Grenzen.
- **Prism-Instanz „Sky and Stone“** holt vor jedem Start den Stand aus `file:///C:/Projekte/modpacks/sky-and-stone/pack.toml`. Das funktioniert nur auf diesem PC (siehe `TODO.md`, P9).
- **Sicherungen:** `C:\Projekte\modpacks\_backups\`. Ordnername `sky-and-stone-<version>-vor-<grund>-<JJJJMMTT>`. Vor jeder größeren Änderung sichern. Kein Git-Repo, der Rückweg ist die Sicherung plus `packwiz refresh`.

**Aufbau des Pack-Ordners:**
- Im Paket: `pack.toml`, `index.toml`, `mods/*.pw.toml` (gut 120 Mods), `config/`, `kubejs/`, `resourcepacks/`, `options.txt`.
- Nicht im Paket (`.packwizignore`): `_src/` (Generator, Texte, Inseln, Balance-Daten), `SCRUM/`, alle Dokumente und Changelogs.

**Grenzen:**
- Das Pack „Louis“ (`louis-pruefung`) ist unabhängig. Nicht als Basis nehmen.
- Im Spiel nicht geprüft heißt NICHT GETESTET. Nie als getestet melden.
- Antworten aus Gemini oder ChatGPT sind Vorschläge. Vor der Übernahme gegen Log oder Mod-Code prüfen. Gemini hat schon einmal falsche Fakten gemeldet (Vault-Notiz „Gemini-Helfer“).
- Mods hinzufügen oder entfernen nur nach Freigabe durch Leon. Freigegeben (25.10.2026, Sprint 6, Spaß-Features): Emotecraft, Enchantment Descriptions, Loot Journal, Better Combat. Entfernt (25.10.2026, Überschneidung ohne Quest-Nutzen): Mekanism Tools (Werkzeugstufen sind verworfen), Mining Gadgets (überschneidet FTB Ultimine). Weitere Mods wieder nur nach Freigabe.

## Progression & Tech-Tree

Quelle: `GAME_DESIGN.md`. Die Stufen sind aus dem Questgraphen abgeleitet, nicht im Spiel gespielt.

| Stufe | Thema | Engpass | Übergang |
|---|---|---|---|
| 0 Start | Baum, Kompost, Bruchstein, Hammer, Faden | Wachstum langsam | Erde |
| 1 Erde | Ex-Deorum-Sieb, Erzbrocken, erster Eisenbarren (2 Barren seit 0.20.0) | Siebchancen | Create |
| 2 Create | Mühle, Sifter, Presse, Messing | Messing, Wartezeiten | Strom |
| 3 Strom & Mekanism | Osmium, Infuser, Schaltkreise | Schaltkreise | Wahl Magie oder Technik |
| 4 Magie oder Technik | Mystical-Agriculture-Essenzen, Ars Nouveau | Stufenkette | Akt III |
| 5 Netzwerk | AE2, Lager, Autocrafting | Verkabelung, Prozessoren | Erz ohne Sieb |
| 6 Akt III | Wahlen, Wither, Drache, Antimaterie | Teile sammeln | Finale |
| 7 Finale | Ewige Fabrik, Insanium, Versiegeln | Zeit | Weiterbauen |

**Questbuch:** 20 Kapitel, 188 Quests (Stand 26.10.2026). Hauptstory in Akt I–III, dazu Mod-Kapitel („Handbuch der Mods“) und Extras („Abseits des Weges“: Tagebuch, Inselmarkt, Sammlerbuch, Baumeister). Keine Haken-Quests.

**Regeln für die Progression:**
- Jede Stufe braucht einen Zweck, ein Problem, das sie löst.
- Frühspiel-Ziel: erster Eisenbarren in 25–40 min. Das ist ein Ziel, nicht gemessen. Ein Spieler schätzte 10–25 min.
- Akt-III-Wahlen („Maschine oder Magie“, „Erz ohne Sieb“) geben heute nur Belohnungen, keine Folgen. Wegabhängige Rezepte sind nicht bewiesen (der Spike hat nur den Ladeteil bestätigt). Erst bauen, wenn der Spike mit zwei Spielern klar ist.
- Startinseln: zwei (Klassisch mit 198 Blöcken, seit Sprint 1.5 vergrößert; Waldlichtung mit 517). Die anderen vier sind seit 0.20.0 entfernt.
- Das Endgame nach dem Finale ist nur angedeutet. Das ist eine offene Designaufgabe.

## KubeJS / CraftTweaker Richtlinien

**Stand:** CraftTweaker ist nicht installiert. Alle Skripte sind KubeJS.

**Skripte im Pack:**
- `kubejs/server_scripts/`: `lagerfeuer.js` (Rast am Lagerfeuer), `waechter.js` (Spruch nach dem Tod), `balance.js` (Essenz-Stufen, Pipez, Time in a Bottle), `bereinigung.js` (entfernt Fehlerrezepte), `gruppen.js` (Item-Gruppen für Aufgaben), `luecken.js` (schließt Lücken, z. B. Endportalrahmen), `sieben.js` (Sieb → Create-Sifter, 132 Rezepte), `willkommen.js`.
- `kubejs/client_scripts/`: `hinweise.js` (Tooltips, JEI-Seiten), `quest_tooltips.js` (vom Generator geschrieben, nicht von Hand ändern).
- Im Testserver zusätzlich `zz_dev_*.js`, `main.js` und `spike/`. Das sind Testhilfen. Nie in den Quellordner übernehmen.

**Regeln:**
1. **Rezepte umleiten:** Änderungen ins passende Modul (Balance in `balance.js`, Fehler in `bereinigung.js`, Lücken in `luecken.js`). Jede Änderung hat einen Kommentar mit Zweck und Beleg (Log-Zeile oder Quelle).
2. **Entfernen nur mit Grund:** (a) Rezept verweist auf ein fehlendes Item oder Mod (Log-Beleg, wie bei ProductiveBees), (b) Duplikat. Eine Balance-Abkürzung entfernt man erst nach dem Spieltest, nie aus Vermutung.
3. **Ore Unification:** Erledigt durch Almost Unified (installiert). Die Barren-Tags haben je ein Mitglied (`_src/tags.json`). Keine eigene Vereinheitlichung ohne Log-Beleg. TODO-0.7 (Item-Gruppen für Barren, Bruchstein, Leder) ist laut Analyse wirkungslos.
4. **Item-Gruppen in Quests:** Nur dort, wo der Zweck zählt (Holzart, Farbe, Material: Barren, Certus, Honig, Leder, Eier). Festes Item, wo Stufe oder Art zählt (Netze, Schaltkreise, Samen und Essenzen, Maschinen, Obsidian, Gerichte, Trophäen). Keine Gruppe bei verbrauchenden Aufgaben (`consume`). Mitglieder vorher in `_src/tags.json` prüfen.
5. **Quests nie von Hand:** `config/ftbquests` schreibt der Generator. Struktur in `_src/quests.py`, Bausteine in `_src/bausteine.py`, Texte in `_src/texte_*.py` (Stil: `_src/TEXTSTIL.md`). Textstellen nicht per Listenposition überschreiben, das hat in 0.11.2 den falschen Satz ersetzt. Diff prüfen.
6. **Quest-IDs sind der Fortschritt:** Die IDs hängen am Kapitelnamen. Umbenennen oder Verschieben löscht den Fortschritt bestehender Welten. Vor jeder Änderung an Kapiteln: `python -I -X utf8 _src/idcheck.py <Backup-Ordner mit chapters/>`. Ergebnis: 0 IDs dürfen entfallen.
7. **Keine Aufgabe ohne Aufgabe:** Eine Quest ohne Aufgabe hakt FTB Quests sofort ab. Der Generator verbietet das.
8. **Belohnungen:** Kisten in `_src/belohnungen.py`, Sperrliste in `_src/sperren.py`. Eine Belohnung darf keine spätere Schranke überspringen. Keine Stufen als Belohnung vergeben, bis der Spike geklärt ist.
9. **Loot:** Mob-Beutekisten (ca. 1 % pro Monster, Bosse immer) laufen über FTB-Quests-Tabellen, Gewichte in `_src/quests.py` und `data.snbt`. Nicht ohne Messwert ändern. Lootr-Truhen sind pro Spieler (seit 0.20.0, im Spiel ungeprüft).
10. **Config-Dateien** (TOML, JSON5) ohne BOM schreiben, sonst lehnt NeoForge sie ab. Im Skyblock-Builder-Inventar heißen die Schlüssel `Item` und `Slot` (großgeschrieben).
11. **Neue Projektdateien** (CLAUDE.md, TODO.md, `.claude/`, Dokumente) gehören in `.packwizignore`. Sonst landen sie beim nächsten `packwiz refresh` im Paket.

**Pflichtprüfung nach jeder Änderung** (Definition of Done aus `SCRUM/BACKLOG.md`):
- Generator läuft fehlerfrei, wenn Quests betroffen sind (`0 Layoutprobleme`).
- Testserver startet mit `Done (` im Log, KubeJS ohne Fehler, Quest-Anzahl stimmt, `0 fehlgeschlagene Rezepte` (alles in einem Schritt: `_src/testlauf.py`).
- Strom-Aufgaben brauchen `max_input` (fehlt es, nimmt FTB Quests keinen Strom an). Der Generator setzt es, die Prüfsuite prüft es.
- `packwiz refresh` im Pack-Ordner.
- Eintrag in `IMPLEMENTATION_LOG.md`: Datei, Zweck, Prüfstatus, Rückweg.

## Design-Philosophie

Das Spiel soll sich nach einem Spiel anfühlen: klare Progression, spürbare Wahl, keine Belohnungs-Abkürzungen, keine Wirtschaft. Keine neuen großen Mods und keine neue Dimension (`PLAN-0.20.0.md`).

- **Grind:** Kein Grind als Progression. Zufallskisten sind Bonus. Der Inselmarkt hat bewusst Abklingzeiten von 1–3 Minecraft-Tagen. Die tägliche Begrüßung (Sprint 2.6) ist wegen Grind-Risiko zurückgestellt.
- **Tutorial-Führung:** Das Questbuch führt. Jeder Meilenstein sagt, was als Nächstes kommt. Kapitel-Untertitel beginnen mit „Problem: …“. Erklärungen müssen im Spiel funktionieren: Ein Spieler hat die Jobs+-Erklärung nicht verstanden, deshalb ist sie neu geschrieben worden.
- **Quest-Zwang vs. Open World:** Die Hauptstory (Akt I–III, Finale) ist der Pfad. Alles andere bleibt freiwillig: „Abseits des Weges“, Handbuch der Mods, Sammlerbuch, Baumeister, Inselmarkt. Optionales wird nicht zur Pflicht.
- **Wahlen mit Folgen:** Ziel ist, dass eine Entscheidung spürbar ist. Keine Route darf dauerhaft unterlegen sein. Heute haben die Wahlen noch keine Folgen (siehe Progression).
- **Technik und Magie gleichwertig, aber verschieden:** Technik ist planbar und strombasiert, Magie ist ressourcenhungrig und verlangt Sammeln.
- **Koop:** Das Pack ist bisher auf Einzelspieler ausgelegt. Team-Belohnungen gibt es nur im Inselmarkt. Die Koop-Entscheidung steht aus (`TODO.md`).
- **Balance nur nach Messung:** Gleichgewichtsänderungen erst nach Spieltest oder Messwert. Vermutungen werden als „Verdacht“ markiert, nicht umgesetzt.
- **Spielerfeedback zählt am meisten:** Die Rückmeldung „nur Eichenholz erlaubt“ (0.6.1) war ein Fehler, den nur das Spiel zeigte. Solche Hinweise haben Vorrang vor Theorie.
- **Text-Stil:** Deutsch, im Spielstil. Item-Namen wie im Spiel (`_src/namen.py`). Regeln in `_src/TEXTSTIL.md`.

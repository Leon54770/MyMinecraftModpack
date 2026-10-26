# Sky and Stone

Stand: 26.10.2026 · Skyblock-Modpack für Minecraft 1.21.1 (NeoForge 21.1.264), unabhängig von „Louis“. Version 1.0.1 (laut `pack.toml`, siehe Protokoll).

## Idee
Klassischer Skyblock (Skyblock Builder) mit Ex Deorum als Start, danach Create, Mystical Agriculture,
Mekanism, AE2, Ars Nouveau und viel zum Bauen. Ein Questbuch (FTB Quests) führt durch alles.

## Startinseln (config/skyblockbuilder, erzeugt von `_src/inseln.py`)
Beim Erstellen der Welt (Welttyp „Skyblock“ → Anpassen) wählbar:
Zwei Inseln: Klassisch (das L aus SkyBlock 2.1, seit Sprint 1.5 größer, 9×3 oben und 3×6 unten) und Waldlichtung (Teich, Eiche, Birke). Oase, Kirschhain, Pilzinsel und Felsbrocken wurden entfernt.
Startinventar: Questbuch, Fackeln, Gießkanne, Brot, Lava- und Wassereimer, Eis, Knochenmehl, Setzlinge.

## Questbuch (config/ftbquests, erzeugt von `_src/quests.py`)
20 Kapitel, 185 Quests (74 Hauptstory), Texte auf Deutsch, Item-Namen wie im Spiel. Der Generator schreibt nur, wenn alle Prüfungen bestehen, und zwar im exakt gleichen Format, das FTB Quests selbst speichert (`_src/ftbformat.py`).
- **Der Weg der Erbauer (Hauptstory):** Akt I: Ein Splitter im Nichts · Akt II: Die Maschinen erwachen · Akt III: Das Herz der Leere
- **Handbuch der Mods:** Ex Deorum · Felder und Küche · Create · Strom und Rohre · Mekanism · Lager und Rucksack · AE2 · Mystical Agriculture · Ars Nouveau · Productive Bees · Nether und End · Hostile Networks und IF
- **Abseits des Weges (ohne Pflicht):** Tagebuch des Wächters · Inselmarkt · Sammlerbuch · Baumeister
- **Zwei echte Entscheidungen vor dem Finale:** „Maschine oder Magie“ (Erzmagier-Zauberbuch oder Loot Fabricator) und „Erz ohne Sieb“ (Osmium-Samen, Erz-Laserbasis oder Erz-Bienen). Je einer reicht.

**Story „Das Herz der Leere“ (0.5.0):** Die Erbauer verbanden Maschinen und Magie und zapften eine Energiequelle unter der Welt an, bis die Welt in Inseln zerbrach. Notizen des letzten Wächters stehen kursiv in 14 Meilensteinen (`LORE` in `_src/quests.py`) und führen zum Finale.

Regeln: Kapitel verzweigen sich und laufen wieder zusammen, jedes endet mit einem Meilenstein (Zahnrad-Symbol).
Belohnungen über vier Kisten (Holz, Eisen, Gold, Stern) plus XP. Die Sternkiste enthält keine gesperrten Essenzen, dafür seit 0.7.0 einen Netheritbarren statt 32 Prudentium. Markt-Tausche geben eine Kiste pro Team.
Questdateien nie von Hand ändern: Struktur in `_src/quests.py`, Texte in `_src/texte_*.py` (Stil: `_src/TEXTSTIL.md`), dann `python -I -X utf8 _src/quests.py`.
Der Generator prüft Item-IDs (`_src/items.json`), Item-Gruppen samt Inhalt (`_src/tags.json` = `kubejs/dev_tags.json` vom Testserver), Zyklen, Quests ohne Aufgabe/Voraussetzung und das Layout (`_src/layoutcheck.py`: keine Linie durch eine Quest). Item-Namen: `python -I _src/namen.py`.

## Sicherheit und Komfort (0.4.0)
- **Forgiving Void:** Wer in die Leere fällt, fällt oben wieder herunter. Kostet 3 Herzen, tötet nie (`config/forgivingvoid-common.toml`).
- **Simple Backups:** Welt-Backup alle 60 Minuten (nur geänderte Dateien, einmal täglich voll), die letzten 8 bleiben, höchstens 10 GB (`config/simplebackups-common.toml`, Ordner `simplebackups/`).
- **Beutekisten von Mobs:** ca. 1 % pro Monster (Holz, selten Eisen), Bosse immer Gold oder Stern. FTB Quests unterscheidet nicht zwischen Spieler- und Farm-Kills, deshalb bewusst niedrig. Gewichte in `_src/quests.py` (Tabellen) und `data.snbt`.
- **Inselmarkt:** 19 wiederholbare Tausch-Quests (Überschuss → Kiste), Abklingzeit 1–3 Minecraft-Tage. Gold- und Sterntausche erst ab Messing.

## Prism mit Auto-Update
Instanz „Sky and Stone“ in Prism: Vor jedem Start holt `packwiz-installer-bootstrap.jar` den Stand aus diesem Ordner
(`file:///C:/Projekte/modpacks/sky-and-stone/pack.toml`). Kein neuer Import nötig, nur `packwiz refresh` nach Änderungen.
`options.txt` ist mit `preserve = true` geschützt: eigene Einstellungen bleiben.
Für andere PCs bräuchte es eine Online-Adresse (z. B. privates GitHub-Repo).

## Leistung messen
Im Spiel nach ca. 10 Minuten: `/spark tps`, `/spark health --memory`, F3 für FPS. Die Ausgaben landen im Log der Instanz
(`%APPDATA%\PrismLauncher\instances\Sky and Stone\minecraft\logs\latest.log`) und lassen sich dort auswerten.

## Weniger Sieb-Plackerei (kubejs/server_scripts/sieben.js)
- Mit der Hand bis zu 5×5 Siebe gleichzeitig (Ex-Deorum-Config).
- **Create-Sifter** benutzt dieselben Siebtabellen wie Ex Deorum (132 Rezepte), automatisierbar mit Wasserrad oder Windmühle.
  Netze: Faden → Faden, Feuerstein → Andesit, Eisen → Zink, Gold → Messing, Diamant → Messing (fortgeschritten), Netherit → stabil (fortgeschritten).
- **Mühlstein und Brechwalzen** übernehmen die Hammer-Rezepte (Bruchstein → Kies → Sand → Staub …).
- Das **mechanische Sieb** braucht Andesit-Gehäuse statt Eisenblöcken und nur halb so viel Strom.
- Extra im Sieb: Inferium-Essenz und Prosperity-Splitter, Fluorit, Uraninit, Bienen- und Nutztier-Spawneier, Shulker-Schalen, Wilden-Teile.
- Danach ersetzen die Mystical-Agriculture-Samen das Sieben ganz.

## Leere-Lücken (kubejs/server_scripts/luecken.js)
- Endportalrahmen herstellbar (Obsidian, Enderauge, Endstein), weil es keine Strongholds gibt.
- Lohenbrenner aus leerem Brenner + 4 Lohenpulver, damit Messing (Create) nicht hinter dem Nether hängt.

## Balance 0.3.0 (kubejs/server_scripts/balance.js, config/tiab-server.toml)
- Mystical Agriculture: Tertium nur im Create-Mixer (mit Messing), Imperium braucht Mekanism-Infused-Alloy, Supremium braucht einen AE2-Engineering-Prozessor. So ersetzen die Samen das Sieben erst Schritt für Schritt.
- Pipez: Advanced-Upgrade braucht Mekanism-Schaltkreise, Ultimate zusätzlich Elite-Schaltkreise und AE2-Prozessoren.
- Time in a Bottle: höchstens 8-fach, höchstens 24 h gespeichert.
- Neu: MEGA Cells (großer AE2-Speicher).
- **0.5.0:** Insanium = 4 Supremium + 1 Mekanism-Ultimate-Schaltkreis → 2 (vorher nur Infusionskristall). Ars-Nouveau-Glyphe „Crush“ kann jetzt auch Sand → Staub, damit ersetzt ein Zauberturm den Hammer komplett.
Hintergrund steht in GEMINI-REVIEW.md (nicht im Export).

## Komfort
RightClickHarvest (Ernten per Rechtsklick), Jade + Jade Addons,
FTB Ultimine, Inventory Essentials (Sortieren), Waystones, Xaero-Karten, Sophisticated Backpacks.

## Leistung
Sodium, Lithium, ModernFix, FerriteCore, ImmediatelyFast, Entity Culling, More Culling, Dynamic FPS, Clumps,
FastWorkbench/FastFurnace, spark. Continuity bewusst weggelassen (braucht auf NeoForge den Sinytra Connector).
Voreinstellung (options.txt): Sichtweite 8, Simulation 6, Grafik „Schnell“, weniger Partikel, Deutsch. Shader (Iris) installiert, aber aus.
- **RAM im Launcher:** Laptop 5–6 GB, Gaming-PC 8 GB.

## Befehle
```bash
python -I _src/inseln.py
python -I _src/quests.py
../tools/packwiz/packwiz.exe refresh
../tools/packwiz/packwiz.exe modrinth export
```
Testserver: `../_testserver-sky-and-stone` (Java 21: `C:\Program Files\Microsoft\jdk-21.0.12.101-hotspot`), Welttyp `skyblockbuilder\:skyblock`.
Inseln testen über die Konsole: `skyblock manage islandShape <Insel>`, dann `skyblock manage teams create <Name>`.

## Verlauf
- **0.11.0** (25.10.2026, `CHANGELOG_0.11.0.md`): „Die Wahl zählt“ – Weg-Quests mit eigenen Belohnungen, Archiv des Wächters mit Codex, Problem-Zeile je Kapitel, Hinweise aus `_src/hinweise_daten.py`.
- **0.10.0** (25.10.2026, `CHANGELOG_0.10.0.md`): Tagebuchseiten, Ruinen mit Schild auf allen Inseln (`_src/inseln.py`), eigene Item-Namen (`kubejs/assets/ftbquests/lang`), automatische Quest-Tooltips, Themen-Kisten (Magie/Technik/Natur), 12 Story-Erfolge (`kubejs/data/skyandstone/advancement`), Koop-Hinweis. Lasttest: 20 TPS bei 140 Mobs.
- **0.9.0** (25.10.2026, `CHANGELOG_0.9.0.md`): Tooltips und JEI-Infoseiten zu Leere-Mechaniken (`kubejs/client_scripts/hinweise.js`), Begrüßung beim ersten Login (`willkommen.js`), XP-Zweck (Wegsteine) erklärt.
- **0.8.0** (25.10.2026, `CHANGELOG_0.8.0.md`): Belohnungen neu (echte Kisten mit 3 Items, Auswahl bei großen Meilensteinen, passende Items je Quest aus `_src/belohnungen.py`, keine XP, Sperrliste `_src/sperren.py`); Prüfungen der Leere (Chimera, 10 Mio. FE, 1024 Eisen, zweiter Drache); Aufgabenbildschirm-Rezept; Deko-Tausch im Markt; Bienenzucht prüft Eisenbienen-Wabe; Squat Grow entfernt.
- **0.7.0** (25.10.2026, „The Heart of the Void“, siehe `CHANGELOG_0.7.0.md` und `NIGHT_REPORT_0.7.0.md`): Fünf Audits umgesetzt. Questdateien im FTB-Eigenformat (kein Hash-Drift mehr), Zinc-Mesh-Rezept, Mühlstein-Fehler (8 leere Rezepte) behoben, Essenz-Verdopplung über Rückbau-Rezepte entfernt; MA-Einstieg ohne Gold-Altar, Presse nach dem Sifter, Seidenraupen- und Prudentium-Mechanik richtig erklärt, Meilensteine nennen ihre Freischaltung; neue Wahl „Erz ohne Sieb“; Bienenzucht mit echter Aufgabe; Story ohne Widerspruch, Tagebuch des Wächters, Notiz für Akt II; Bienen ohne Herumfliegen (Leistung).
- **0.6.4** (25.10.2026): Belohnungen werden im Questbuch selbst abgeholt; alle Questtexte neu im Spielstil (`_src/texte_*.py`, Regeln `_src/TEXTSTIL.md`), Item-Namen wie im Spiel (`_src/namen.py` → `namen.json`, Englisch ohne deutsche Übersetzung); neues Ebenen-Layout ohne Linien durch fremde Quests (`_src/layoutcheck.py`, 0 Probleme, 20 Kreuzungen). Offen: FTB Quests speichert Reward-Tabellen/Gruppen beim Beenden im eigenen Format neu, packwiz stellt sie dann nicht wieder her.
- **0.6.3** (25.10.2026, Nachtschicht, siehe `NIGHT_REPORT.md`): Lohenbrenner-Quest erklärt Netherrack über Hexenwasser; Zink von Hand 1 statt 4 Barren; Seidenraupe als Start-Belohnung; Akt-Kapitel zeigen Voraussetzungen aus Mod-Kapiteln als Verweise; Erzmagier-Buch ohne Totem (Diamantblock) + Chimera-Warnung; Gold-/Stern-Tausche erst ab Messing, Antimaterie-Tausch gestrichen, Supremium-Tausch 8 statt 32; Starbuncle ohne Lager-Controller; Ressourcen-Bienen Eisen- statt Goldkiste. Generator schreibt bei Fehlern nichts, prüft Mobs/Dimensionen. Testserver Sichtweite 8/Simulation 6.
- **0.6.2** (25.10.2026): Spieltest-Feedback: Hauptstory auf 68 Quests erweitert (Gemini-Vorschlag, gegengeprüft), Pfad-Layout (Schlangenlinie, kompakter), Mod-Kapitel zeigen Hauptstory-Quests als Verweise. Story-Notizen stehen jetzt im Meilenstein selbst, das Story-Kapitel ist ein Verweis-Pfad (Quests ohne Aufgabe hakt FTB Quests sofort ab). Item-Gruppen statt fester Holzart/Farbe über FTB Filter System (16 Aufgaben, eigene Gruppen in `kubejs/server_scripts/gruppen.js`). „Maschine oder Magie“ mit echter Aufgabe. Generator: SNBT-Schlüssel mit Sonderzeichen in Anführungszeichen, Regel „keine Quest ohne Aufgabe“.
- **0.6.1** (25.10.2026): Umsetzung `_src/ANWEISUNG-0.6.1.md` + Logik-Prüfung. Story-Kette nur über Hauptstory-Meilensteine (Mod-Notizen als Seitenäste); Spaltreaktor + Polonium vor Antimaterie; Finale braucht Erzmagier ODER Beute-Fabrikator (`z_weg`); Großkraftwerk optional; Insanium-Quest 8, Siebfabrik 32/16/32. Fehler behoben: 4 Quests ohne Voraussetzung (Ursache im Zusammenlegen, jetzt erben sie die Voraussetzungen), Mystical-Agriculture-Samen nach echter Stufe (Eisen/Kupfer Stufe 3 → nach Tertium, Gold 4 → nach Imperium, Diamant 5 → nach Supremium; vorher Kreis Tertium↔Eisen), Prägeplatten-Weg erklärt (Certus-Essenz) und an Tertium gehängt, Wixie-Quest ohne unbaubaren Wixie-Kessel, Totem aus den Trophäen (nur Glück), Polonium-Tausch an Polonium-Quest, Trophäen an den Wither. Generator prüft jetzt selbst: Quests ohne Voraussetzung, Pflicht an optional, Story an Nicht-Hauptstory. Welttyp-Hinweis in der Start-Quest.
- **0.6.0** (25.10.2026): Questbuch-Umbau (andere Sitzung): Hauptstory Akt I–III, Mod-Kapitel, Story als Extra, keine Haken-Quests, Belohnungen automatisch.
- **0.5.1** (25.10.2026): Abschlussprüfung vor dem ersten Spieltest: Generator synchron, 0 Überlappungen, 0 Zyklen, Testserver fehlerfrei; Insanium-Quest erklärt jetzt den Ultimate-Schaltkreis und hängt an „Elite-Schaltkreis“.
- **0.5.0** (25.10.2026): ChatGPT-Auftrag geprüft und umgesetzt (`_src/KONZEPT-0.5.md`): Story „Das Herz der Leere“, Finale „Erbe der Ewigkeit“ mit „Die ewige Fabrik“, Kapitel „Prüfungen der Leere“ (Ingenieursprüfungen, Herausforderungen, Sammlerbuch), 3 Ars-Nouveau-Alternativen (Crush-Turm, Wixie, Whirlisprig), Insanium an Mekanism gekoppelt, Sternkiste ohne Imperium, Markt-Kisten pro Team.
- **0.4.1** (25.10.2026): Gemini-Loop Etappe 1: Backups stündlich inkrementell, Kistenrate 1 %, Gold nur von Bossen, 3 Endgame-Tausche, Sternkiste mit 4 Netherit-Schrott.
- **0.4.0** (25.10.2026): Forgiving Void, Simple Backups, Mob-Beutekisten, Inselmarkt, Prism-Auto-Update.
- **0.3.0** (25.10.2026): Startinseln, Questbuch, Komfort-Mods, Lohenbrenner-Rezept, Balance (andere Sitzung), MEGA Cells.
- **0.2.1** (25.10.2026): Ressourcenpaket Whimscape (Standard), Bare Bones und Vanilla Experience+ zum Einschalten.
- **0.2.0** (24.10.2026): Rezept-Dump geprüft (8.796 Items), Lücken geschlossen, Applied Mekanistics, Extruder, Inventory Essentials.
- **0.1.0** (24.10.2026): Grundpaket.

## Erster Spieltest (Messpunkte statt Balance-Raten)
**Wichtig:** Beim Erstellen der Welt den Welttyp auf **Skyblock** stellen (lässt sich ohne Zusatz-Mod nicht als Standard setzen).
1. **Frühspiel:** Minuten bis „Erster Eisenbarren“. Ziel unter ~30 min, sonst Siebchancen prüfen.
2. **Create-Einstieg:** Hänger zwischen Sieb und Messing (Lohenpulver → Lohenbrenner)? Wo genau?
3. **Leistung:** nach 10 min `/spark tps` und `/spark health --memory`, FPS (F3) am Laptop bei Sichtweite 8. Ziel 20 TPS, RAM unter 80 %.
4. **Mystical Agriculture:** Wann ersetzt die erste Ressourcen-Saat (Eisen, Stufe 3) das Sieben? Fühlt sich Tertium fair an?
5. **Belohnungen:** Mob-Kisten nach 1 h Farm, wird der Inselmarkt genutzt?

## Offen
- Erster echter Spieltest mit `MORGEN-PLAYTEST.md` (Zeit bis zum Eisenbarren, Netherrack-Weg, Erz-Wahl, FPS/TPS).
- 0.8: Item-Gruppen nur, wo es Sinn ergibt (Barren, Certus, Bruchstein, Waben, Leder/Eier …), Plan in `_src/TODO-0.7.md`
- Das Kapitel „Prüfungen der Leere“ aus 0.5 gibt es nicht mehr (Haken-Quests gestrichen); Ersatz mit echten Aufgaben offen.

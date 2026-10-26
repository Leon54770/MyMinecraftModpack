# Prüfauftrag: Minecraft-Modpack „Sky and Stone“ (Stand 0.10.0)

Du bist ein erfahrener Modpack-Entwickler und Game Designer (Referenzen: SkyFactory 4/5, StoneBlock 3/4, ATM10 Sky) und zugleich ein sorgfältiger Code-Reviewer. Prüfe das Projekt vollständig und sag ehrlich, wie du damit weitermachen würdest. Antworte auf Deutsch.

## Das Projekt
- Eigenes Skyblock-Modpack, Minecraft 1.21.1, NeoForge 21.1.264, Java 21, ca. 120 Mods, verwaltet mit packwiz, gestartet über Prism Launcher (Auto-Update vor jedem Start). Zielrechner: Laptop mit Intel Iris Xe, 16 GB RAM (5–6 GB für Minecraft), Sichtweite 8 / Simulation 6.
- Wichtige Mods: Ex Deorum (Sieben), Create + Create Sifter, Mekanism (+ Generators/Tools), Powah, Pipez, Applied Energistics 2 (+ Applied Mekanistics, MEGA Cells, Wireless), Mystical Agriculture + Agradditions, Ars Nouveau, Productive Bees, Hostile Neural Networks, Industrial Foregoing, Botany Pots, Farmer's Delight, Sophisticated Backpacks/Storage, Functional Storage, Iron Jetpacks, Building/Mining Gadgets, FTB Quests/Teams/Ultimine, Waystones, Macaw's, Handcrafted, FramedBlocks, Forgiving Void, Simple Backups, Gravestone, Almost Unified, KubeJS 7, Leistungsmods (Sodium, Lithium, ModernFix, FerriteCore …). Skyblock Builder mit 6 eigenen Startinseln.
- Ziel des Erstellers: Das Pack soll sich wie EIN durchdachtes eigenes Spiel anfühlen, nicht wie 120 nebeneinander installierte Mods. Technik und Magie gleichwertig, freies Bauen soll sich lohnen, Quests geben Orientierung statt Pflicht-Checklisten, kein künstlicher Grind, allein und mit Freunden spielbar.
- Geschichte „Das Herz der Leere“: Die Erbauer verbanden Maschinen und Magie, zapften eine Energiequelle unter der Welt an, die Welt zerbrach in Inseln. 17 Notizen des letzten Wächters begleiten die Hauptstory bis zum Finale.
- Progression: Sieben von Hand → Create-Sifter → Strom/Mekanism → Mystical Agriculture (Essenzstufen gekoppelt: Tertium nur im Create-Mixer mit Messing, Imperium braucht Mekanism Infused Alloy, Supremium einen AE2-Engineering-Prozessor, Insanium einen Ultimate-Schaltkreis) → AE2-Autocrafting → Endgame (Antimaterie, „Die ewige Fabrik“, Drache). Vor dem Finale zwei echte Wahlen: „Maschine oder Magie“ und „Erz ohne Sieb“ (Felder, Laserbohrer oder Bienen).

## Wie das Projekt aufgebaut ist (die Dateien unten)
- Das Questbuch wird von einem Python-Generator erzeugt: `bausteine.py` (Grunddefinitionen der Quests) → `quests.py` (Änderungen je Version, Hauptstory Akt I–III, Kapitel, Belohnungstabellen, Story) → `texte_*.py` (alle Titel/Beschreibungen) → `belohnungen.py` (Belohnung je Quest) → `questlib.py` (Prüfungen + Ausgabe) mit `ftbformat.py` (schreibt exakt das Format, das FTB Quests selbst speichert), `layoutcheck.py` (keine Linie durch eine Quest), `sperren.py` (keine Belohnung überspringt eine Stufe). `inseln.py` erzeugt die Startinseln, `namen.py` die Item-Namen.
- KubeJS: `sieben.js` (Ex-Deorum-Siebtabellen → Create Sifter, Hammer → Mühlstein), `balance.js` (Stufenrezepte, Pipez, Erzmagier), `luecken.js` (Endportalrahmen, Lohenbrenner, Aufgabenbildschirm), `gruppen.js` (Item-Gruppen), `willkommen.js` (Begrüßung), `hinweise.js` (Tooltips + JEI-Infoseiten).
- Bereits geprüft: Testserver startet ohne Fehler, 0 fehlgeschlagene Rezepte, 180 Quests geladen, Lasttest 20 TPS mit 140 Mobs. Noch kein richtiger Spieltest im Client.

## Was du liefern sollst
1. **Gesamturteil** in 3–5 Sätzen: Wie gut ist das Pack auf dem Weg zum Ziel „ein durchdachtes eigenes Spiel“?
2. **Fehler und Risiken** (höchstens 10, nach Schwere): konkrete Datei und Stelle, was falsch ist oder schiefgehen kann, wie man es behebt. Unterscheide „sicher ein Fehler“ von „Vermutung“. Erfinde keine Mod-Verhalten; wenn du dir bei einer Mod nicht sicher bist, schreib das dazu.
3. **Spielerlebnis** (höchstens 8 Punkte): Wo wirkt das Pack noch wie „viele Mods“ statt wie ein Spiel? Frühspiel, Übergänge, Story, Belohnungen, Technik/Magie, Bauen, Koop.
4. **Wie würdest du weitermachen?** Ein Plan für die nächsten 3 Versionen (je 3–6 Punkte, sortiert nach Nutzen), umsetzbar mit den vorhandenen Mods und Werkzeugen (FTB Quests, KubeJS 7, Configs, Python-Generator). Keine neuen großen Mods, keine neuen Dimensionen.
5. **Drei kreative Ideen**, die dieses Pack einzigartig machen würden.
Halte dich insgesamt an etwa 1.500–2.500 Wörter.

---

# Projektdateien

## Datei: README.md
```md
# Sky and Stone

Stand: 25.10.2026 · Skyblock-Modpack für Minecraft 1.21.1 (NeoForge 21.1.264), unabhängig von „Louis“. Version 0.10.0.

## Idee
Klassischer Skyblock (Skyblock Builder) mit Ex Deorum als Start, danach Create, Mystical Agriculture,
Mekanism, AE2, Ars Nouveau und viel zum Bauen. Ein Questbuch (FTB Quests) führt durch alles.

## Startinseln (config/skyblockbuilder, erzeugt von `_src/inseln.py`)
Beim Erstellen der Welt (Welttyp „Skyblock“ → Anpassen) wählbar:
Klassisch (das L aus SkyBlock 2.1), Waldlichtung (Teich, Eiche, Birke), Oase (Sand, Palme, Zuckerrohr, Kakteen),
Kirschhain, Pilzinsel (Myzel, Riesenpilz) und Felsbrocken (StoneBlock-Gruß mit etwas Erz).
Startinventar: Questbuch, Fackeln, Gießkanne, Haken, Brot, Lava- und Wassereimer, Eis, Knochenmehl, Setzlinge.

## Questbuch (config/ftbquests, erzeugt von `_src/quests.py`)
20 Kapitel, 180 Quests (69 Hauptstory), Texte auf Deutsch, Item-Namen wie im Spiel. Der Generator schreibt nur, wenn alle Prüfungen bestehen, und zwar im exakt gleichen Format, das FTB Quests selbst speichert (`_src/ftbformat.py`).
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
- **Inselmarkt:** 17 wiederholbare Tausch-Quests (Überschuss → Kiste), Abklingzeit 1–3 Minecraft-Tage. Gold- und Sterntausche erst ab Messing.

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
```

## Datei: CHANGELOG_0.10.0.md
```md
# Sky and Stone 0.10.0

Stand: 25.10.2026 · Basis 0.9.0 · Ziel: Das Pack soll sich wie ein eigenes Spiel anfühlen.

## Neu
- **Tagebuchseiten:** Jeder der 17 Story-Meilensteine gibt eine leuchtende Tagebuchseite (Papier mit Titel und Notiz als Beschreibung, „Seite 4 von 17“). Zum Sammeln und Ausstellen.
- **Ruinen der Erbauer:** Jede der 6 Startinseln hat am Rand eine verfallene Säule mit gewachstem Schild („Hier wachte der letzte Wächter. Folge dem Buch.“).
- **Eigene Namen:** Questbuch heißt „Tagebuch der Erbauer“, Beutekisten „Kiste der Leere“.
- **Quest-Tooltips:** An 195 Items steht, wofür sie im Questbuch gebraucht werden („Questbuch: Messing (Akt I)“). Erzeugt der Generator selbst, bleibt also immer aktuell (`kubejs/client_scripts/quest_tooltips.js`).
- **Themen-Kisten:** Kiste der Magie (Ars), der Technik (Create, Strom, Mekanism, AE2, Lager) und der Natur (Landwirtschaft, Bienen) in den Mod-Kapiteln statt allgemeiner Holz-/Eisenkisten.
- **12 Erfolge mit Einblendung** entlang der Geschichte: „Was die Leere zurückgibt“, „Der Funke“, „Messing“, „Die Maschinen erwachen“, „Der Wächter am Ende“, „Der Herzschlag“ …
- **Koop:** Start-Quest erklärt, dass ein Team den Fortschritt teilt und jeder seine Belohnungen selbst abholt.

## Gemessen
- Lasttest auf dem Laptop (Testserver, 140 Tiere/Bienen auf einer Plattform): 20 TPS, Tick-Median 1,5 ms, 95 % unter 3,4 ms, CPU 1–2 %. Ohne Grafik – FPS im Client sind noch offen.
```

## Datei: _src/quests.py
```py
"""Sky and Stone – Questbuch-Aufbau (0.6). Aufruf aus dem Pack-Ordner:  python -I _src/quests.py

Aufbau wie SkyFactory 4 / StoneBlock:
  * Hauptstory (3 Akte) mit den wichtigsten Schritten für Früh-, Mittel- und Endspiel
  * Ein Kapitel pro Mod bzw. Modbereich mit den Details (oben links Verweise auf die Hauptstory)
  * Extras: Story „Das Herz der Leere“ (läuft von allein mit), Inselmarkt, Sammlerbuch, Baumeister
Alle Aufgaben werden automatisch erkannt (keine Haken-Quests). Belohnungen holt man selbst im Questbuch ab (0.6.4).
Texte und Aufgaben der einzelnen Quests stehen in _src/bausteine.py, hier nur Struktur und Änderungen.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from questlib import *
import bausteine as B

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G, M = 'gear', 'hexagon'

ALLE = {q.key: q for c in [B.willkommen, B.erde, B.gruen, B.create, B.strom, B.mek, B.lager, B.ma, B.ars, B.bienen,
                           B.jenseits, B.geist, B.bau, B.markt, B.pruefungen, B.ende] for q in c.quests}

# ---------------------------------------------------------------------
# 1. Streichen oder zusammenlegen (alter Schlüssel -> Ersatz für Abhängigkeiten)
# ---------------------------------------------------------------------
ERSATZ = {
    # Willkommen: 7 Haken-Quests -> eine automatische Start-Quest mit allen Tipps
    'w_wachsen': 'w_start', 'w_ernte': 'w_start', 'w_jei': 'w_start', 'w_ultimine': 'w_start',
    'w_karte': 'w_start', 'w_team': 'w_start', 'w_los': 'w_start',
    # Zwischenschritte in ihr Ziel gelegt
    'e_porzellan': 'e_lavatiegel', 's_draht': 'c_alternator', 's_paste': 's_orb', 'l_fluix': 'l_lader',
    'a_kammer': 'a_quelle', 'k_kabel': 'k_cube', 'g_brett': 'g_topf',
    # Reine Beschäftigung / nicht automatisch prüfbar
    'l_muell': 'l_fass', 'j_brenner': 'j_lohe', 'h_boss': 'h_fab', 'x_markt': 'e_eisen', 'z_versiegeln': 'z_fabrik',
    'p_start': 'e_eisen', 'p_kompakt': 'c_siebfabrik', 'p_ohnebrenn': 's_reaktor', 'p_ohnerohr': 'a_starbuncle',
    'p_vierfach': 'k_inject', 'p_nether': 'j_nether', 'p_ohnesieb': 'm_eisen', 'p_wither': 'j_wither',
    # Gemini-Umbau (GEMINI-UMBAU.md): doppelte/kleine Schritte zusammengelegt
    'e_faden': 'e_raupe', 'c_netze': 'c_sifter', 'c_tertium': 'c_messing', 'l_pickup': 'l_rucksack',
    # Baumeister-Haken -> neue Quests mit echten Aufgaben (unten)
    'u_haus': 'u_dach', 'u_moebel': 'u_moebel2', 'u_bruecke': 'u_bruecke2', 'u_garten': 'u_bruecke2', 'u_meister': 'u_kopie',
}
ORIG = dict(ALLE)   # Originale, auch der gestrichenen Quests (für ihre Abhängigkeiten)
for k in ERSATZ: ALLE.pop(k, None)

def _aufloesen(d, eigener, seen=()):
    """Abhängigkeit d auflösen. Wurde d in die eigene Quest gelegt (z. B. e_porzellan -> e_lavatiegel),
    erbt die Quest die Voraussetzungen von d – sonst stünde sie ohne Voraussetzung im Buch (Fehler in 0.6.0)."""
    if d not in ERSATZ: return [d]
    ziel = d
    while ziel in ERSATZ: ziel = ERSATZ[ziel]
    if ziel != eigener: return [ziel]
    if d in seen or d not in ORIG: return []
    out = []
    for dd in ORIG[d].deps: out += _aufloesen(dd, eigener, seen + (d,))
    return out

def ersetze_deps(q):
    neu = []
    for d0 in q.deps:
        for d in _aufloesen(d0, q.key):
            if d != q.key and d not in neu: neu.append(d)
    q.deps = neu

# ---------------------------------------------------------------------
# 2. Geänderte Quests
# ---------------------------------------------------------------------
A = ALLE
A['w_start'].tasks = [item('ftbquests:book')]
A['w_start'].desc = [
    'Unter dir: nichts. Um dich: nichts. Nur deine Insel.',
    '',
    'Dieses Buch führt dich durch alles. Die &lHauptstory&r zeigt dir die wichtigsten Schritte, die &lMod-Kapitel&r erklären jede Mod im Detail.',
    'Quests erledigen sich von selbst, sobald du die Items hast, und Belohnungen landen direkt bei dir.',
    '',
    '&lNützlich von Anfang an:&r',
    '- Ducken neben Setzlingen und Feldern lässt sie etwas schneller wachsen. Die Gießkanne kann das besser.',
    '- Reife Pflanzen per Rechtsklick ernten, sie werden neu gesetzt.',
    '- R zeigt das Rezept eines Items, U wofür es gebraucht wird (auch alle Siebfunde mit Chancen).',
    '- Taste ` (Gravis) halten und abbauen: ganze Bäume, Adern und Kiesflächen auf einmal.',
    '- M öffnet die Karte. Freunde holst du mit /skyblock invite <Name>.',
    '- Wer in die Leere fällt, landet oben wieder auf der Insel (kostet 3 Herzen).',
    '',
    '&cKeine Insel, sondern eine normale Welt?&r Dann wurde beim Erstellen der Welttyp nicht umgestellt. Neue Welt anlegen und unter „Welt“ → „Welttyp“ &lSkyblock&r wählen.']
A['w_start'].rewards = [crate('holz'), xp(10)]

A['c_alternator'].tasks = [item('createaddition:alternator'), item('createaddition:copper_spool')]
A['c_alternator'].desc = ['Der Alternator (Create Crafts & Additions) macht aus Drehkraft Strom (FE).',
                          'Mit Kupferdraht-Rollen verbindest du ihn mit Akkus und Maschinen. Ab hier gibt es Strom.']
A['s_orb'].tasks = [item('powah:energizing_orb'), item('powah:energizing_rod_starter', 2), item('powah:dielectric_paste', 8)]
A['s_orb'].desc = ['Dielektrische Paste (Ton, Kohle, Lava) ist die Grundzutat von Powah.',
                   'Der Orb lädt Items mit Strom auf, die Stäbe drumherum liefern die Energie.']
A['l_lader'].title = 'Lader und Fluix'
A['l_lader'].tasks = [item('ae2:charger'), item('ae2:fluix_crystal', 8)]
A['l_lader'].desc = ['Der Lader lädt Certus mit Strom auf.', 'Geladener Certus + Redstone + Quarz ins Wasser geworfen ergibt Fluix.']
A['l_inscriber'].deps = ['l_lader', 'k_stahl']
A['a_quelle'].tasks = [item('ars_nouveau:imbuement_chamber'), item('ars_nouveau:source_gem', 8)]
A['a_quelle'].desc = ['Amethyst (aus dem Sieb) in der Imbuement Chamber wird zu Quellstein.', 'Quellstein ist der Grundstoff aller Magie in Ars Nouveau.']
A['k_cube'].title = 'Strom verteilen'
A['k_cube'].tasks = [item('mekanism:basic_universal_cable', 8), item('mekanism:basic_energy_cube')]
A['k_cube'].desc = ['Universalkabel tragen Strom, der Energiewürfel speichert ihn.']
A['g_topf'].title = 'Die Küche'
A['g_topf'].tasks = [item('farmersdelight:cutting_board'), item('farmersdelight:cooking_pot')]
A['g_topf'].desc = ['Farmer\'s Delight: Das Schneidebrett holt mehr aus deinen Zutaten, der Kochtopf macht Gerichte, die lange satt machen.']
A['g_autark'].tasks = [item('botanypots:terracotta_hopper_botany_pot', 4)]
A['g_autark'].desc = ['Vier Trichter-Töpfe: Holz und Essen wachsen von selbst und landen in Truhen.',
                      'Ab jetzt versorgt sich deine Insel selbst.']
A['z_herr'].tasks = [item('minecraft:dragon_egg')]
A['z_herr'].desc = [d for d in A['z_herr'].desc if not d.startswith('&o')] + ['',
                    'Aufgabe: Bring das Drachenei nach Hause. Tipp: Das Ei teleportiert sich beim Schlagen – ein Kolben schiebt es herunter.']
A['e_raupe'].tasks = [item('exdeorum:silkworm'), item('minecraft:string', 8)]
A['e_raupe'].title = 'Seidenraupe und Faden'
A['e_raupe'].desc = ['Setz eine Seidenraupe auf Laub: Es wird langsam zu Spinnweben, die beim Abbauen zu Faden zerfallen.',
                     'Faden brauchst du für das erste Siebnetz.']
A['c_sifter'].tasks = [item('createsifter:sifter'), item('createsifter:string_mesh'), item('createsifter:andesite_mesh')]
A['l_rucksack'].tasks = [item('sophisticatedbackpacks:backpack'), item('sophisticatedbackpacks:pickup_upgrade')]
A['l_rucksack'].desc = ['Mehr Platz zum Mitnehmen. Das Aufsammel-Upgrade füllt den Rucksack automatisch mit Siebfunden.']
A['m_tertium'].desc = ['4 Prudentium + 1 Messingbarren im Create-Mixer ergeben 2 Tertium-Essenz.', 'Nur so kommst du an Stufe-3-Samen.']
A['h_fab'].shape, A['h_fab'].size = G, 2.0
A['h_fab'].desc = A['h_fab'].desc + ['Meilenstein: Ab jetzt kommen Mob-Drops aus der Maschine.']
for k in ('p_essenzen', 'p_netze', 'p_archwood', 'p_trophaeen'):
    A[k].optional = False   # das ganze Sammlerbuch-Kapitel ist optional
# Ex-Deorum-Startitems kommen jetzt aus dem Startinventar, der Haken also auch
A['e_haken'].desc = ['Den Haken hast du im Startinventar. Er lässt Laub öfter Setzlinge fallen und findet Seidenraupen.']

# Baumeister: echte Aufgaben statt Haken (jede Quest stellt eine Bau-Mod vor)
NEU = [
    Q('u_dach', 'Ein Dach über dem Kopf', 0, 0, item('mcwroofs:oak_roof', 16), deps=['u_meissel'], rewards=[crate('holz'), xp(20)],
      desc=['Macaw\'s Roofs, Doors und Windows: Dächer, Türen und Fenster in allen Holzarten.']),
    Q('u_moebel2', 'Einrichten', 0, 0, [item('handcrafted:oak_chair', 2), item('handcrafted:oak_table')], deps=['u_dach'], rewards=[xp(20)],
      desc=['Handcrafted und Macaw\'s Furniture: Stühle, Tische, Regale, Betten.']),
    Q('u_bruecke2', 'Brücke ins Nichts', 0, 0, item('mcwbridges:rope_oak_bridge', 8), deps=['u_meissel'], rewards=[xp(20)],
      desc=['Macaw\'s Bridges: Hängebrücken zu deinen Nebeninseln. Wege und Laternen gibt es in Macaw\'s Paths und Lights.']),
    Q('u_kopie', 'Inselarchitekt', 0, 0, item('buildinggadgets2:gadget_copy_paste'), deps=['u_gadget', 'u_framed', 'u_moebel2'], shape=G, size=1.8,
      rewards=[crate('gold'), xp(60)], desc=['Das Kopier-Gadget speichert ganze Gebäude und baut sie woanders wieder auf.']),
    Q('z_ultkreis', 'Ultimate-Schaltkreis', 0, 0, item('mekanism:ultimate_control_circuit', 2), deps=['z_elite'], rewards=[crate('gold'), xp(60)],
      desc=['Elite-Schaltkreise + Atomlegierung. Brauchst du für Insanium-Essenz und die ewige Fabrik.']),
]
NEU += [
    # 0.6.1 (ANWEISUNG-0.6.1.md A2): Antimaterie braucht Polonium, Polonium braucht einen Spaltreaktor
    Q('k_spalt', 'Spaltreaktor', 0, 0, [item('mekanismgenerators:fission_reactor_casing', 4), item('mekanismgenerators:fission_fuel_assembly')],
      deps=['z_elite'], rewards=[crate('gold'), xp(80)],
      desc=['Mekanism Generators: Ein Spaltreaktor macht aus Uran viel Strom – und Atommüll, den du gleich brauchst.',
            'Uran: Uranbrocken aus zerkleinertem Tiefenschiefer im Sieb oder Uran-Samen. Weg: Uran → Yellowcake → Uranoxid → Uranhexafluorid → Spaltbrennstoff.',
            'Vorsicht: Kühlung (Wasser) nicht vergessen und den Reaktor nie überhitzen lassen.']),
    Q('k_polonium', 'Polonium', 0, 0, item('mekanism:pellet_polonium'), deps=['k_spalt'], rewards=[crate('gold'), xp(80)],
      desc=['Atommüll aus dem Spaltreaktor wird im Solar Neutron Activator (braucht Tageslicht) zu Polonium.',
            'Polonium-Pellets sind die Zutat für Antimaterie im SPS.']),
    # A4: Finale „Maschine oder Magie“ – eins von beiden reicht
    # 0.6.2: echte Aufgabe statt keiner (Quests ohne Aufgabe gelten in FTB Quests sofort als erledigt)
    Q('z_weg', 'Maschine oder Magie', 0, 0,
      [tag('skyandstone:weg_zum_herz', icon='ars_nouveau:archmage_spell_book', title='Erzmagier-Zauberbuch oder Loot Fabricator')],
      deps=['a_erzmagier', 'h_fab'], dep_any=True, icon='ars_nouveau:archmage_spell_book',
      rewards=[xp(100)],
      desc=['Die Erbauer brauchten beides. Dir reicht einer der Wege:',
            '- &lMagie:&r das Erzmagier-Zauberbuch (Ars Nouveau)',
            '- &lMaschinen:&r der Beute-Fabrikator (Hostile Networks)',
            'Diese Quest erledigt sich von selbst, sobald du einen davon hast.']),
]
for q in NEU: A[q.key] = q
for q in A.values(): ersetze_deps(q)
A['m_insanium'].deps = [d for d in A['m_insanium'].deps if d != 'z_elite'] + ['z_ultkreis']
# 0.7.0 (Review): Insanium braucht keine Osmium-Samen. Sonst wäre m_niemehr über z_fabrik doch Pflicht und die Erz-Wahl wirkungslos.
A['m_insanium'].deps = [d for d in A['m_insanium'].deps if d != 'm_niemehr'] + (['m_supremium'] if 'm_supremium' not in A['m_insanium'].deps else [])

# ---------------------------------------------------------------------
# 0.6.1 Logik-Prüfung: Mystical-Agriculture-Samen nach ihrer echten Stufe (aus dem Mod-Code gelesen)
#   Stufe 2: Kohle, Silizium · Stufe 3: Eisen, Kupfer, Redstone, Certus · Stufe 4: Gold, Fluix, Osmium · Stufe 5: Diamant
#   Vorher hing m_tertium an m_eisen, obwohl Eisen-Samen selbst Tertium brauchen (Kreis).
# ---------------------------------------------------------------------
A['m_tertium'].deps = ['m_prudentium', 'c_messing']
A['m_eisen'].deps = ['m_tertium']
A['m_eisen'].desc = ['Eisen-Samen sind Stufe 3: Sie brauchen Tertium-Essenz (Create-Mixer).',
                     'Der Moment, in dem das Sieben endet: Eisen wächst.']
A['m_kupfer'].deps = ['m_tertium']
A['m_kupfer'].desc = ['Kohle ist Stufe 2, Kupfer Stufe 3 (Tertium).']
A['m_gold'].deps = ['m_imperium']
A['m_gold'].title = 'Gold und Redstone'
A['m_gold'].desc = ['Redstone ist Stufe 3, Gold Stufe 4: Dafür brauchst du Imperium-Essenz (Mekanism).']
A['m_diamant'].deps = ['m_supremium']
A['m_diamant'].desc = ['Diamant-Samen sind Stufe 5 und brauchen Supremium-Essenz (AE2).']
# AE2-Prägeplatten: in der Leere keine Meteoriten -> Mystical Agriculture (Certus-Essenz, Stufe 3)
A['l_inscriber'].deps = ['l_lader', 'k_stahl', 'm_tertium']
A['l_inscriber'].desc = ['In der Leere gibt es keine Meteoriten. Die vier Prägeplatten stellst du aus Certus-Quarz-Essenz her:',
                         'Zum Beispiel 8 Essenz um einen Goldbarren = Logik-Platte, 8 Essenz um Silizium = Silizium-Platte. Die anderen beiden zeigt JEI (U auf die Essenz).',
                         'Certus-Samen sind Stufe 3 (Tertium). Freischaltung danach: Supremium-Essenz und Pipez-Ultimate.']
# Wixie-Kessel entsteht erst in der Welt (Wixie auf einen Kessel setzen) und hat kein Rezept
A['a_wixie'].tasks = [item('ars_nouveau:wixie_charm'), item('minecraft:cauldron')]
A['a_wixie'].desc = ['Setz die Wixie mit ihrem Amulett auf einen Kessel: Daraus wird ein Wixie-Kessel.',
                     'Lege Zutaten in Truhen daneben und zeige ihr das Rezept: Sie stellt es immer wieder her.',
                     'Für einfache Dinge (Fackeln, Bleche, Legierungen) ein früher Ersatz für AE2-Autocrafting. Für große Mengen bleibt AE2 stärker.']
# Totem gibt es nur selten aus Sternkisten (keine Plünderer in der Leere) -> kein Glücksspiel im Sammlerbuch
A['p_trophaeen'].tasks = [t for t in A['p_trophaeen'].tasks if t[1] != 'minecraft:totem_of_undying']
A['p_trophaeen'].desc = ['Netherstern, Drachenei und Wither-Schädel. Stell sie irgendwo schön aus.']

# Voraussetzung muss garantieren, dass das verlangte Item erreichbar ist
A['x_polonium'].deps = ['k_polonium']                      # Polonium erst nach der Polonium-Quest
if 'j_wither' not in A['p_trophaeen'].deps: A['p_trophaeen'].deps.append('j_wither')   # Netherstern braucht den Wither

# ---------------------------------------------------------------------
# Nachtschicht 0.6.3 (NIGHT_REPORT.md): Befunde der Design-Prüfung
# ---------------------------------------------------------------------
# Erzmagier: Rezept ohne Totem (balance.js). Netherstern braucht den Wither, Tribut die Chimera.
A['a_erzmagier'].deps = A['a_erzmagier'].deps + ['j_wither']
A['a_erzmagier'].desc = ['Das stärkste Zauberbuch. Magie ist ab jetzt kein Spielzeug mehr.', '',
    '&lZutaten (Buch-Upgrade am Schreibtisch):&r Lehrlings-Zauberbuch, 3 Enderperlen, 2 Smaragde, 1 Diamantblock, 1 Netherstern (Wither) und 1 Wilden-Tribut.',
    'Den Tribut lässt die &lWilden-Chimera&r fallen: Ritual „Wilden beschwören“ im Ritualbecken, verstärkt mit Wilden-Horn, -Stachel und -Flügel.',
    '&cAchtung:&r Das Chimera-Ritual zerstört Blöcke rund um das Becken. Bau es auf einer eigenen Plattform weit weg von deiner Basis.']
# Starbuncle: Magie-Logistik ohne Technik-Lager als Voraussetzung (eigener Seitenweg ab dem Schreibtisch)
A['a_starbuncle'].deps = [d for d in A['a_starbuncle'].deps if d != 'l_controller']
A['a_starbuncle'].rewards = [crate('eisen'), xp(60)]
A['a_starbuncle'].desc = ['Ein Starbuncle trägt Items von A nach B – sichtbar statt in Rohren.',
    'Zum Beispiel: Siebfunde aus der Truhe unter dem Sieb in deine Lagertruhe bringen. Goldnuggets machen ihn glücklich.']
# Ressourcen-Bienen sind ein Frühspiel-Seitenweg: Goldkiste (Messing, Osmium) wäre zu früh
A['b_zucht'].rewards = [crate('eisen'), xp(60)]
# Wiederholbare Gold-/Sterntausche erst ab Messing, sonst gibt es Messing (-> Tertium) und Osmium aus dem Markt
for k, q in A.items():
    if k.startswith('x_') and q.repeat and any(r[0] == 'table' and r[1] in ('gold', 'stern') for r in q.rewards):
        if 'c_messing' not in q.deps: q.deps.append('c_messing')
# Befunde Quest-Fluss (Frühspiel)
# Der leere Lohenbrenner braucht Netherrack, der Nether ist leer -> Weg über Hexenwasser erklären
A['c_brenner'].tasks = [item('create:empty_blaze_burner'), item('create:blaze_burner')]
A['c_brenner'].desc = ['1. &lLeerer Lohenbrenner:&r 4 Eisenbleche (Presse) um 1 Netherrack.',
    '2. Leerer Brenner + 4 Lohenpulver (Staub sieben) = Lohenbrenner. Mit Kohle oder Holz gefüttert heizt er dein Becken für Messing.',
    '',
    '&lNetherrack ohne Nether:&r Myzelsporen (Erde sieben) auf Erde ergeben Myzel. Ein Wasserfass auf Myzel wird nach gut einer Minute zu Hexenwasser.',
    'Hexenwasser im Fass + Lava ergibt Netherrack (genauer Aufbau in JEI: U auf Netherrack). Auf der Pilzinsel hast du Myzel schon.']
# Zink von Hand: 3,5-4 % pro Kies. 4 Barren wären ~400 Kies, gebraucht wird Zink erst für Messing (dann siebt Create)
A['e_kupfer'].tasks = [item('minecraft:copper_ingot', 4), item('create:zinc_ingot', 1)]
A['e_kupfer'].desc = ['Kupfer- und Zinkbrocken kommen auch aus dem Kies (Zink ist selten, etwa 4 %).',
    'Ein Zinkbarren reicht für den Anfang. Den Rest siebt später der Create-Sifter mit dem Eisennetz.']
# Seidenraupe: Der Haken findet sie nur mit ~1 % pro Laubblock -> eine gibt es zum Start, damit das erste Netz planbar ist
A['w_start'].rewards = [crate('holz'), give('exdeorum:silkworm'), xp(10)]
A['e_raupe'].rewards = [give('minecraft:string', 4), xp(15)]
A['e_raupe'].desc = ['Setz die Seidenraupe (Belohnung der Start-Quest) auf Laub: Es wird langsam zu Spinnweben, die beim Abbauen zu Faden zerfallen.',
    'Mit dem Haken findest du im Laub weitere Seidenraupen. Faden brauchst du für das erste Siebnetz.']
A['e_brocken'].desc = ['Schon das Fadennetz gibt aus Kies Eisen- (10 %) und Kupferbrocken (8 %).',
    'Das Feuersteinnetz bringt etwas mehr und dazu Andesit-Kiesel für Create.', '4 Brocken = 1 Erz zum Schmelzen.']
# Endgame-Tausche lohnen sich sonst nicht (Sternkiste ist weniger wert als 32 Supremium oder Antimaterie)
A['x_supremium'].tasks = [item('mysticalagriculture:supremium_essence', 8, consume=True)]
A.pop('x_antimaterie')

# ---------------------------------------------------------------------
# 0.7.0 (NIGHT_REPORT_0.7.0.md): Befunde der fünf Audits
# ---------------------------------------------------------------------
# Mystical Agriculture ohne Gold-Grind starten: Inferium-Samen sind ein Werkbank-Rezept (8 Essenz + Weizensamen),
# der Infusionsaltar (18 Goldbarren) wird erst für Stufe-3-Samen gebraucht. Inferium fällt beim Sieben von Erde.
A['g_inferium'].deps = ['e_sieb']
A['m_inferium'].deps = ['g_inferium']
A['m_altar'].deps = ['m_prudentium']
for k in ('m_eisen', 'm_kupfer', 'l_inscriber'):
    if 'm_altar' not in A[k].deps: A[k].deps.append('m_altar')
# Erst den Sifter, dann die Presse: Die Presse kostet einen Eisenblock, der Sifter kein Eisen
A['c_presse'].deps = ['c_sifter']
# Weizen kommt nur vom Feld; c:crops enthielt auch gesiebte Karotten/Kartoffeln, Kaktus, Netherwarze
GRUPPEN_FEST = {'g_feld'}
# Wixie: Goldkiste (8 Messing) vor Messing würde Tertium früher öffnen (wie b_zucht/a_starbuncle in 0.6.3)
A['a_wixie'].rewards = [crate('eisen'), xp(50)]
# Ressourcen-Bienen: echte Aufgabe statt 8 Honey Treat. Erz-Bienen = Kristallbiene (Netherquarz-Nest im Nether)
# x Ashy Mining Bee (Kiesnest in Fluss-/Strandbiom). Der Nether muss also offen sein.
A['b_zucht'].deps = A['b_zucht'].deps + ['j_nether']
# 0.8.0: Prüft jetzt die gezüchtete Eisenbiene über ihre Wabe (Komponente bee_type), nicht nur gebaute Nester
A['b_zucht'].tasks = [item('productivebees:configurable_honeycomb', 1, komponenten={'productivebees:bee_type': 'productivebees:iron'})]
A['b_zucht'].icon = 'productivebees:configurable_honeycomb'
# Zweite echte Wahl: Erz ohne Sieb – Felder (MA), Laserbohrer (IF) oder Bienen. Vorher waren IF und Bienen totes Holz.
NEU2 = [
    Q('z_erz', 'Erz ohne Sieb', 0, 0, [tag('skyandstone:erz_ohne_sieb', icon='industrialforegoing:ore_laser_base',
                                          title='Osmium-Samen, Erz-Laserbasis oder Netherquarz-Nest')],
      deps=['m_niemehr', 'h_laser', 'b_zucht'], dep_any=True, icon='industrialforegoing:ore_laser_base', shape=M, size=1.5,
      rewards=[crate('gold'), xp(100)]),
]
for q in NEU2: A[q.key] = q

# ---------------------------------------------------------------------
# 0.8.0: Prüfungen der Leere (Ersatz für die alten Haken-Quests) und Deko-Tausch im Markt
# ---------------------------------------------------------------------
PRUEF = [
    Q('t_chimera', 'Die Chimera', 0, 0, kill('ars_nouveau:wilden_boss'), deps=['a_ritual', 'c_messing'], shape=M, size=1.4,
      icon='ars_nouveau:wilden_tribute', rewards=[crate('gold', art='choice')]),
    Q('t_speicher', 'Der Speicher der Erbauer', 0, 0, energie(10_000_000), deps=['k_cube'], icon='mekanism:basic_energy_cube',
      rewards=[crate('gold')]),
    Q('t_fabrik', 'Tausend Barren', 0, 0, item('minecraft:iron_ingot', 1024), deps=['c_siebfabrik'], icon='minecraft:iron_block',
      rewards=[crate('eisen'), crate('eisen')]),
    Q('t_drache', 'Der zweite Drache', 0, 0, kill('minecraft:ender_dragon', 2), deps=['j_drache'], shape=M, size=1.4,
      icon='minecraft:dragon_head', rewards=[crate('stern', art='choice')]),
]
for q in PRUEF: A[q.key] = q
# Bauen bekommt einen Wert: Deko-Überschuss gegen Kisten (Gruppen-Aufgabe, jede Holzart zählt, wird verbraucht)
DEKO = [
    B.tausch('x_dach', 'Dachdecker', 0, 0, 'mcwroofs:oak_roof', 64, 'eisen', B.TAG, ['u_dach', 'c_messing'], 'Dachziegel im Überfluss.'),
    B.tausch('x_bruecke', 'Brückenbauer', 0, 0, 'mcwbridges:rope_oak_bridge', 32, 'holz', B.TAG, ['u_bruecke2'], 'Hängebrücken für die Nachbarinseln.'),
]
for q, (gruppe, titel) in zip(DEKO, [('skyandstone:roofs', 'Beliebige Dachblöcke'), ('skyandstone:rope_bridges', 'Beliebige Hängebrücken')]):
    q.tasks = [tag(gruppe, q.tasks[0][2], icon=q.tasks[0][1], title=titel, consume=True)]
    A[q.key] = q

# A2/A5: Antimaterie hängt an Polonium statt am (jetzt optionalen) Großkraftwerk
A['z_sps'].deps = ['k_polonium', 'l_auto', 'z_elite']
A['z_sps'].desc = ['Polonium-Pellets im SPS (Supercritical Phase Shifter) werden zu Antimaterie. Ein einziges Pellet reicht.',
                   'Der SPS braucht sehr viel Strom: Spaltreaktor, Powah-Reaktor oder viele Generatoren.']
A['z_strom'].optional = True
A['z_strom'].desc = ['Optional: Ein großer Powah-Reaktor ist der bequeme Weg zu viel Strom.',
                     'Jede andere große Stromquelle (z. B. der Spaltreaktor) reicht für die Antimaterie auch.']
# A3: Mengen (jede Aufgabe wird einzeln erkannt, mehr bringt nichts)
A['z_insanium'].tasks = [item('mysticalagradditions:insanium_essence', 8)]
A['c_siebfabrik'].tasks = [item('minecraft:iron_ingot', 32), item('create:zinc_ingot', 16), item('minecraft:copper_ingot', 32)]
# A4: Finale braucht Magie ODER Maschinen
A['z_herr'].deps = ['z_fabrik', 'j_drache', 'm_niemehr', 'z_weg']
# 0.7.0: Erz-Wahl statt Pflicht-Felder (Felder bleiben über z_fabrik/z_netherstern trotzdem Teil des Endspiels)
A['z_herr'].deps = [d for d in A['z_herr'].deps if d != 'm_niemehr'] + ['z_erz']

# ---------------------------------------------------------------------
# 3. Hauptstory: (Schlüssel, Hauptstory-Vorgänger oder None)
#    Der Vorgänger wird als zusätzliche Abhängigkeit eingetragen, damit die Linie sichtbar ist.
#    None = nur die echten Voraussetzungen (Nebenzweig, z. B. Nether).
# ---------------------------------------------------------------------
# 0.6.2: erweitert auf 68 Quests (Spieltest: "zu wenig Quests in der Hauptstory"),
#        Vorschlag Gemini + Gegencheck der Parallel-Sitzung, siehe _src/GEMINI-HAUPTSTORY.md
AKT1 = [
    ('w_start', None), ('e_holz', 'w_start'), ('e_raupe', 'e_holz'), ('e_fass', 'e_holz'), ('e_cobble', 'e_fass'),
    ('e_hammer', 'e_cobble'), ('e_sieb', 'e_hammer'), ('e_tiegel', 'e_sieb'), ('e_lavatiegel', 'e_tiegel'),
    ('e_brocken', 'e_sieb'), ('e_feuernetz', 'e_brocken'), ('e_eisen', 'e_feuernetz'),
    ('m_inferium', 'e_eisen'), ('m_prudentium', 'm_inferium'), ('m_altar', 'm_prudentium'),
    ('e_kupfer', 'e_eisen'), ('c_andesit', 'e_kupfer'), ('c_rad', 'c_andesit'), ('c_muehle', 'c_rad'), ('c_sifter', 'c_muehle'),
    ('c_extruder', 'c_muehle'), ('c_presse', 'c_sifter'), ('c_fan', 'c_presse'), ('c_mixer', 'c_presse'), ('c_brenner', 'c_mixer'),
    ('c_messing', 'c_brenner'), ('c_siebfabrik', 'c_messing'),
]
AKT2 = [
    ('c_mechanismus', 'c_messing'), ('c_alternator', 'c_mechanismus'), ('k_osmium', 'c_alternator'), ('k_infuser', 'k_osmium'),
    ('k_alloy', 'k_infuser'), ('k_schalt', 'k_infuser'), ('k_enrich', 'k_infuser'), ('k_purif', 'k_enrich'),
    ('m_tertium', 'c_messing'), ('m_eisen', 'm_tertium'),
    ('j_obsidian', 'e_eisen'), ('j_nether', 'j_obsidian'), ('j_festung', 'j_nether'), ('j_lohe', 'j_festung'),
    ('k_jetpack', 'k_alloy'),
    ('l_certus', 'e_eisen'), ('l_lader', 'l_certus'), ('l_inscriber', 'm_tertium'), ('l_prozessoren', 'l_inscriber'), ('l_netz', 'l_prozessoren'),
    ('k_inject', 'k_purif'),
]
AKT3 = [
    ('l_auto', 'l_netz'), ('m_imperium', 'k_alloy'), ('m_supremium', 'm_imperium'), ('m_niemehr', 'm_supremium'),
    ('j_hexe', 'j_nether'), ('j_wither', 'j_hexe'), ('j_perlen', 'j_obsidian'), ('j_augen', 'j_perlen'), ('j_rahmen', 'j_augen'),
    ('j_end', 'j_rahmen'), ('j_drache', 'j_end'),
    ('z_elite', 'k_inject'), ('z_ultkreis', 'z_elite'), ('m_insanium', 'z_ultkreis'),
    ('k_spalt', 'z_elite'), ('k_polonium', 'k_spalt'), ('z_sps', 'k_polonium'),
    ('z_fabrik', 'z_sps'), ('z_weg', None), ('z_erz', None), ('z_herr', 'z_fabrik'),
]
HAUPT_KEYS = {k for akt in (AKT1, AKT2, AKT3) for k, _ in akt}
for akt in (AKT1, AKT2, AKT3):
    for k, v in akt:
        if v and v not in A[k].deps: A[k].deps.append(v)
for k, _ in AKT1[-1:] + AKT2[-1:] + AKT3[-1:]: A[k].shape = G

# ---------------------------------------------------------------------
# 0.6.2: Item-Gruppen statt einer festen Holzart/Farbe (Spieltest: "nur Eichenholz erlaubt").
#        Aufgaben mit diesen Items akzeptieren jedes Item der Gruppe (FTB Filter System, item_tag).
# ---------------------------------------------------------------------
GRUPPEN = {
    'minecraft:oak_log': ('minecraft:logs', 'Beliebige Holzstämme'),
    'minecraft:oak_sapling': ('minecraft:saplings', 'Beliebige Setzlinge'),
    'minecraft:wheat_seeds': ('c:seeds', 'Beliebige Samen'),
    'minecraft:wheat': ('c:crops', 'Beliebige Feldfrüchte'),
    'exdeorum:oak_barrel': ('exdeorum:wooden_barrels', 'Beliebiges Holzfass'),
    'exdeorum:oak_sieve': ('skyandstone:sieves', 'Beliebiges Sieb'),
    'exdeorum:oak_crucible': ('skyandstone:water_crucibles', 'Beliebiger Holztiegel'),
    'botanypots:terracotta_botany_pot': ('botanypots:botany_pots', 'Beliebiger Botany Pot'),
    'botanypots:terracotta_hopper_botany_pot': ('skyandstone:hopper_botany_pots', 'Beliebiger Trichter-Botany-Pot'),
    'functionalstorage:oak_1': ('functionalstorage:drawer', 'Beliebige Schubladen'),
    'handcrafted:oak_chair': ('handcrafted:chairs', 'Beliebige Stühle'),
    'handcrafted:oak_table': ('handcrafted:tables', 'Beliebiger Tisch'),
    'mcwroofs:oak_roof': ('skyandstone:roofs', 'Beliebige Dachblöcke'),
    'mcwbridges:rope_oak_bridge': ('skyandstone:rope_bridges', 'Beliebige Hängebrücke'),
    'ars_nouveau:blue_archwood_sapling': ('skyandstone:archwood_saplings', 'Beliebiger Archwood-Setzling'),
    'productivebees:advanced_oak_beehive': ('productivebees:advanced_beehives', 'Beliebiger fortgeschrittener Bienenstock'),
    # 0.8.0: Almost Unified vereinheitlicht Metalle schon (jeder Barren-Tag hat nur ein Mitglied); bei Certus zählt so auch geladener
    'ae2:certus_quartz_crystal': ('c:gems/certus_quartz', 'Certus-Quarz (auch geladen)'),
}
GRUPPEN_AUSNAHMEN = {'p_archwood'} | GRUPPEN_FEST   # Sammlerbuch: jede Farbe einzeln; g_feld: echter Weizen
for q in A.values():
    if q.key in GRUPPEN_AUSNAHMEN: continue
    q.tasks = [tag(GRUPPEN[t[1]][0], t[2], icon=t[1], title=GRUPPEN[t[1]][1]) if t[0] == 'item' and t[1] in GRUPPEN and not t[3] else t
               for t in q.tasks]

def kap(key, title, group, icon, keys, sub='', links=(), mode='baum'):
    keys = [k for k in keys if k not in ERSATZ]
    links = [l for l in links if l not in ERSATZ]
    if group == 'haupt':
        # Nachtschicht 0.6.3: Voraussetzungen aus Mod-Kapiteln als Verweis oben im Akt zeigen,
        # sonst ist eine Akt-Quest gesperrt, ohne dass man sieht, was fehlt (z. B. m_altar <- g_inferium).
        for k in keys:
            for d in A[k].deps:
                if d not in HAUPT_KEYS and d not in links: links.append(d)
    if group == 'mods':
        # Quests, die in der Hauptstory stehen, erscheinen im Mod-Kapitel als Verweis (nicht doppelt)
        for k in keys:
            if k in HAUPT_KEYS and k not in links: links.append(k)
        keys = [k for k in keys if k not in HAUPT_KEYS]
    return Chapter(key, title, group, icon, [A[k] for k in keys], sub=sub, links=links, mode=mode)

haupt = [
    kap('akt1', 'Akt I: Die Insel', 'haupt', 'exdeorum:oak_sieve', [k for k, _ in AKT1],
        sub=['Vom ersten Baum bis zur Siebfabrik.', 'Details zu jedem Schritt stehen in den Mod-Kapiteln.'], mode='pfad'),
    kap('akt2', 'Akt II: Maschinen', 'haupt', 'mekanism:metallurgic_infuser', [k for k, _ in AKT2],
        sub=['Strom, Mekanism, Nether, AE2 – die Insel wird zur Fabrik.'], mode='pfad'),
    kap('akt3', 'Akt III: Das Herz der Leere', 'haupt', 'mekanism:pellet_antimatter', [k for k, _ in AKT3],
        sub=['Autocrafting, Erz vom Feld, Bosse und das Finale.'], mode='pfad'),
]


# ---------------------------------------------------------------------
# 4. Mod-Kapitel
# ---------------------------------------------------------------------
mods = [
    kap('exdeorum', 'Ex Deorum: Sieben', 'mods', 'exdeorum:oak_sieve',
        ['e_haken', 'e_raupe', 'e_faden', 'e_fass', 'e_cobble', 'e_hammer', 'e_tiegel', 'e_lavatiegel', 'e_brocken', 'e_feuernetz',
         'e_eisennetz', 'e_kanne', 's_mechsieb', 's_mechhammer'],
        sub='Siebe, Netze, Tiegel und Gießkannen.', links=['e_holz', 'e_sieb', 'e_eisen']),
    kap('landwirtschaft', 'Landwirtschaft und Küche', 'mods', 'minecraft:wheat',
        ['e_samen', 'g_feld', 'g_topf', 'g_tiere', 'g_topf_pflanze', 'g_baumtopf', 'g_festessen', 'g_inferium', 'g_autark'],
        sub='Farmer\'s Delight, Botany Pots, Nutztiere.', links=['e_sieb']),
    kap('create', 'Create', 'mods', 'create:cogwheel',
        ['c_rad', 'c_muehle', 'c_netze', 'c_extruder', 'c_presse', 'c_fan', 'c_mixer', 'c_brenner', 'c_tertium', 'c_mechanismus',
         'c_deployer', 'c_crafter'],
        sub='Zahnräder, Mühlstein, Sifter, Messing.', links=['c_andesit', 'c_sifter', 'c_messing', 'c_siebfabrik']),
    kap('energie', 'Energie und Rohre', 'mods', 'powah:energy_cell_starter',
        ['s_akku', 's_orb', 's_stahl', 's_furnator', 's_solar', 's_kristall', 's_pipe', 's_upgrade', 's_reaktor', 'z_ultimate', 'z_strom'],
        sub='Create Crafts & Additions, Powah, Pipez.', links=['c_alternator']),
    kap('mekanism', 'Mekanism', 'mods', 'mekanism:metallurgic_infuser',
        ['k_stahl', 'k_schalt', 'k_alloy', 'k_cube', 'k_separator', 'k_purif', 'k_x5', 'k_fortschritt', 'k_meka', 'k_tiab', 'k_spalt', 'z_meka'],
        sub='Erzverarbeitung, Schaltkreise, Atomtechnik, Werkzeuge.',
        links=['k_osmium', 'k_infuser', 'k_enrich', 'k_inject', 'k_jetpack', 'z_elite', 'k_polonium', 'z_sps']),
    kap('lagerung', 'Lagerung', 'mods', 'functionalstorage:oak_1',
        ['l_rucksack', 'l_pickup', 'l_fass', 'l_schubladen', 'l_controller'],
        sub='Sophisticated Backpacks/Storage, Functional Storage.', links=['e_eisen']),
    kap('ae2', 'Applied Energistics 2', 'mods', 'ae2:controller',
        ['l_certus', 'l_lader', 'l_prozessoren', 'l_wireless', 'l_appmek', 'l_mega'],
        sub='ME-Netz, Autocrafting, kabellos.', links=['l_inscriber', 'l_netz', 'l_auto']),
    kap('mysticalag', 'Mystical Agriculture', 'mods', 'mysticalagriculture:inferium_seeds',
        ['m_altar', 'm_prudentium', 'm_eisen', 'm_kupfer', 'm_gold', 'm_diamant', 'm_beschleuniger', 'm_acker', 'z_insanium', 'z_netherstern'],
        sub=['Erz, das auf Feldern wächst.', 'Stufen: Inferium → Prudentium → Tertium (Create) → Imperium (Mekanism) → Supremium (AE2) → Insanium.'],
        links=['m_inferium', 'm_tertium', 'm_imperium', 'm_supremium', 'm_niemehr', 'm_insanium']),
    kap('ars', 'Ars Nouveau', 'mods', 'ars_nouveau:novice_spell_book',
        ['a_quelle', 'a_buch', 'a_tisch', 'a_glas', 'a_archwood', 'a_whirli', 'a_crush', 'a_starbuncle', 'a_drygmy', 'a_wilden',
         'a_apparat', 'a_ritual', 'a_wixie', 'a_erzmagier'],
        sub='Magie, die Arbeit spart: Transport, Mob-Drops, Autocrafting.', links=['e_eisen']),
    kap('bienen', 'Productive Bees', 'mods', 'productivebees:advanced_oak_beehive',
        ['b_biene', 'b_stock', 'b_zentri', 'b_nest', 'b_zucht', 'b_upgrade'],
        sub='Rohstoffe, die summen.', links=['e_sieb']),
    kap('dimensionen', 'Nether und End', 'mods', 'minecraft:obsidian',
        ['j_obsidian', 'j_festung', 'j_hexe', 'j_perlen', 'j_augen', 'j_rahmen', 'j_end', 'j_shulker'],
        sub='Festungen in der Leere, Wither und Drache.', links=['j_nether', 'j_lohe', 'j_wither', 'j_drache']),
    kap('maschinengeist', 'Hostile Networks und IF', 'mods', 'hostilenetworks:deep_learner',
        ['h_learner', 'h_modell', 'h_sim', 'h_fab', 'h_rahmen', 'h_plastik', 'h_laser'],
        sub='Mobs simulieren statt jagen, Erz per Laser.', links=['c_alternator']),
]

# ---------------------------------------------------------------------
# 5. Extras
# ---------------------------------------------------------------------
# Story: jede Notiz schaltet sich frei, wenn der passende Meilenstein erreicht ist (Quest ohne Aufgabe = erledigt sich selbst)
STORY = [
    ('w_start', 'Die erste Notiz', 'Notiz des letzten Wächters: „Wer das liest, steht auf einem Splitter unserer Welt. Darunter schläft das Herz der Leere.“'),
    ('e_sieb', 'Sternenstaub', '„Wir siebten einst Sternenstaub. Jetzt siebst du Kies – es ist derselbe Anfang.“'),
    ('e_eisen', 'Der Funke', '„Das erste Metall. Die Erbauer nannten es den Funken.“'),
    ('g_autark', 'Zurück zum Leben', '„Eine Insel, die sich selbst nährt, ist der erste Schritt zurück.“'),
    ('c_alternator', 'Die Leitungen', '…'),
    ('c_siebfabrik', 'Die erste Maschine', '„Unsere Maschinen arbeiteten Tag und Nacht. Du hast gerade die erste wieder geweckt.“'),
    ('j_nether', 'Die zerbrochene Unterwelt', '„Auch die Unterwelt zerbrach. Unsere Festungen hängen dort noch in der Luft.“'),
    ('k_inject', 'Gier', '„Aus jedem Brocken das Vierfache. So reich waren wir – und so gierig.“'),
    ('l_auto', 'Netze, die denken', '„Unsere Netze dachten mit. Am Ende dachten sie schneller als wir.“'),
    ('m_niemehr', 'Felder aus Erz', '„Die Felder wuchsen Erz, als die Minen versiegt waren. Wenigstens das haben wir richtig gemacht.“'),
    ('k_spalt', 'Kraft aus der Leere', '„Wir nahmen die Kraft aus der Leere, nicht aus Kohle. Zu viel davon zerriss den Boden.“'),
    ('a_erzmagier', 'Maschine und Magie', '„Maschine und Magie waren für uns nie Gegensätze. Erst zusammen erreichten sie das Herz.“'),
    ('z_weg', 'Ein Weg genügt', '…'),
    ('h_fab', 'Feinde auswendig', '„Wir lernten unsere Feinde auswendig, bis wir sie nicht mehr bekämpfen mussten.“'),
    ('j_drache', 'Der Wächter am Ende', '„Der Drache bewachte das Ende, nicht für uns, sondern vor uns.“'),
    ('z_sps', 'Der Herzschlag', '„Antimaterie: der Herzschlag der Leere in einer Kapsel. Behandle sie mit Respekt.“'),
    ('z_herr', 'Das Erbe', '„Wer das Herz der Leere wieder schlagen lässt, trägt unser Erbe. Nimm nur, was du brauchst.“'),
]
# 0.6.2: Quests ohne Aufgabe gelten in FTB Quests sofort als erledigt (Spieltest). Darum steht jede Notiz jetzt
# oben im Meilenstein selbst, und das Story-Kapitel zeigt die Meilensteine als Verweis-Pfad. Fortschritt = echter Fortschritt.
# 0.6.4: Texte im Spielstil stehen in eigenen Dateien (_src/texte_*.py), Struktur und Aufgaben bleiben hier.
#        QUESTS = {schlüssel: (titel, [zeilen])}, KAPITEL = {kapitel: (titel, untertitel)}, STORY = {meilenstein: (titel, text)}
TEXT_FEHLER = []
TEXT_MODULE = []
for _name in ('texte_hauptstory', 'texte_technik', 'texte_abenteuer'):
    try: TEXT_MODULE.append(__import__(_name))
    except ModuleNotFoundError: pass
_story = {ms: (t, x) for ms, t, x in STORY}
for _m in TEXT_MODULE:
    for k, (titel, zeilen) in getattr(_m, 'QUESTS', {}).items():
        if k not in A: TEXT_FEHLER.append(f'{_m.__name__}: unbekannte Quest {k}'); continue
        if any(z.startswith('&o') for z in zeilen): TEXT_FEHLER.append(f'{k}: Zeile beginnt mit &o (für Story-Notizen reserviert)')
        A[k].title, A[k].desc = titel, list(zeilen)
    for ms, (t, x) in getattr(_m, 'STORY', {}).items():
        if ms not in _story: TEXT_FEHLER.append(f'{_m.__name__}: unbekannte Story-Notiz {ms}'); continue
        _story[ms] = (t, x)
STORY = [(ms, t, x) for ms, (t, x) in _story.items()]
# 0.8.0: Belohnungen je Quest aus _src/belohnungen.py: ('item', id, n) · ('kiste', stufe) = Kiste zum Öffnen ·
#        ('wahl', stufe) = ein Item aus der Kiste aussuchen. Keine XP mehr. Markt-Tausche (x_*) behalten ihre Teamkiste.
try:
    import belohnungen as _bel
    for k, liste in _bel.BELOHNUNGEN.items():
        if k not in A: TEXT_FEHLER.append(f'belohnungen: unbekannte Quest {k}'); continue
        neu = []
        for r in liste:
            if r[0] == 'item': neu.append(give(r[1], r[2]))
            elif r[0] == 'kiste': neu.append(crate(r[1]))
            elif r[0] == 'wahl': neu.append(crate(r[1], art='choice'))
            else: TEXT_FEHLER.append(f'belohnungen: {k} unbekannte Art {r[0]}')
        A[k].rewards = neu
    for k, q in A.items():
        if k.startswith('x_'): continue
        q.rewards = [r for r in q.rewards if r[0] != 'xp']
except ModuleNotFoundError:
    pass
TEXT_FEHLER += [f'Story-Notiz {ms} hat noch keinen Text (Platzhalter …)' for ms, t, x in STORY if x.strip() in ('…', '...')]
story_q = []
import re as _re, textwrap as _tw
SEITEN = []
def tagebuchseite(nr, titel, text):
    j = lambda t, farbe, kursiv=False: json.dumps({'text': t, 'color': farbe, 'italic': kursiv}, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    zeilen = [j(f'Seite {nr} von {len(STORY)}', 'dark_purple')] + [j(z, 'gray', True) for z in _tw.wrap(text, 34)]
    return {'minecraft:custom_name': j(f'Tagebuch: {titel}', 'light_purple'), 'minecraft:lore': zeilen,
            'minecraft:enchantment_glint_override': __import__('ftbformat').Byte(1)}   # FTB schreibt 1b
def _woerter(t): return {w.lower() for w in _re.findall(r'[A-Za-zÄÖÜäöüß]{4,}', t)}
for ms, titel, text in STORY:
    rest = [d for d in A[ms].desc if not d.startswith('&o')]
    # 0.6.4: Wiederholt die erste Stimmungszeile nur die Notiz, fällt sie weg (sonst steht das Zitat doppelt da)
    if rest:
        a, b = _woerter(rest[0]), _woerter(text)
        if a and len(a & b) / len(a) >= 0.4:
            rest = rest[1:]
            if rest and rest[0] == '': rest = rest[1:]
    A[ms].desc = [f'&5&lNotiz: {titel}', '&o' + text, ''] + rest
    # 0.10.0: Jede Notiz gibt es zusätzlich als Tagebuchseite (Papier mit Titel und Text) zum Sammeln
    A[ms].rewards = A[ms].rewards + [give('minecraft:paper', 1, komponenten=tagebuchseite(len(SEITEN) + 1, titel, text))]
    SEITEN.append(ms)

extras = [
    Chapter('story', 'Story: Das Herz der Leere', 'extras', 'minecraft:writable_book', [],
            sub=['Die Notizen des letzten Wächters, in der Reihenfolge der Geschichte.',
                 'Jede Notiz steht im zugehörigen Meilenstein und wird lesbar, sobald du ihn erreichst.'],
            links=[ms for ms, _, _ in STORY], mode='pfad'),
    kap('markt', 'Inselmarkt', 'extras', 'minecraft:emerald', [k for k in A if k.startswith('x_')],
        sub=['Überschuss gegen Beutekisten tauschen. Die Items werden beim Abgeben verbraucht.',
             'Jeder Tausch hat eine Abklingzeit. Kisten fallen auch selten von Monstern, Bosse lassen immer eine fallen.']),
    kap('sammler', 'Sammlerbuch', 'extras', 'minecraft:book', ['p_essenzen', 'p_netze', 'p_archwood', 'p_trophaeen'],
        sub='Optional: Sammle alles einmal.'),
    kap('bau', 'Baumeister', 'extras', 'rechiseled:chisel', ['u_meissel', 'u_dach', 'u_moebel2', 'u_bruecke2', 'u_framed', 'u_gadget', 'u_kopie'],
        sub='Optional: schön statt nur praktisch.'),
    kap('pruefungen', 'Prüfungen der Leere', 'extras', 'minecraft:spyglass', [q.key for q in PRUEF],
        sub='Optional: Herausforderungen für Ingenieure und Mutige.'),
]

# 0.10.0: Themen-Kisten – in den Mod-Kapiteln passt der Inhalt zum Thema (Holz-/Eisenkisten werden ersetzt, wenn die Stufe passt)
THEMA = {'ars': 'magie', 'landwirtschaft': 'natur', 'bienen': 'natur', 'create': 'technik', 'energie': 'technik',
         'mekanism': 'technik', 'ae2': 'technik', 'lagerung': 'technik'}
import sperren as _sp
def _ahnen(k, s=None):
    s = set() if s is None else s
    for d in A[k].deps:
        if d not in s: s.add(d); _ahnen(d, s)
    return s
for c in mods:
    th = THEMA.get(c.key)
    if not th: continue
    gate = _sp.KISTE_AB.get(th)
    for q in c.quests:
        if gate and gate != q.key and gate not in _ahnen(q.key): continue
        q.rewards = [crate(th, r[2], r[3]) if r[0] == 'table' and r[1] in ('holz', 'eisen') else r for r in q.rewards]

GROUPS = [('haupt', 'Hauptstory'), ('mods', 'Mods'), ('extras', 'Extras')]
CHAPTERS = haupt + mods + extras
_kap = {c.key: c for c in CHAPTERS}
for _m in TEXT_MODULE:
    for k, (titel, sub) in getattr(_m, 'KAPITEL', {}).items():
        if k not in _kap: TEXT_FEHLER.append(f'{_m.__name__}: unbekanntes Kapitel {k}'); continue
        _kap[k].title, _kap[k].sub = titel, sub
for _m in TEXT_MODULE:
    GROUPS = [(g, getattr(_m, 'GRUPPEN', {}).get(g, t)) for g, t in GROUPS]

def pruefe_struktur():
    fehler = []
    benutzt = {}
    for c in CHAPTERS:
        for q in c.quests:
            if q.key in benutzt: fehler.append(f'{q.key} in {benutzt[q.key]} und {c.key}')
            benutzt[q.key] = c.key
            if any(t[0] == 'checkmark' for t in q.tasks): fehler.append(f'{q.key}: Haken-Aufgabe')
            if not q.tasks: fehler.append(f'{q.key}: keine Aufgabe (FTB Quests hakt sie sofort ab)')
    for k in A:
        if k not in benutzt: fehler.append(f'{k} in keinem Kapitel')
    # B7 (0.6.1): Logik-Regeln, damit kein Stand mehr mit verwaisten oder blockierten Quests entsteht
    alle = {q.key: q for c in CHAPTERS for q in c.quests}
    for k, q in alle.items():
        if k != 'w_start' and not q.deps: fehler.append(f'{k}: keine Voraussetzung (steht frei im Buch)')
        if not q.optional:
            for d in q.deps:
                if d in alle and alle[d].optional and not q.dep_any: fehler.append(f'{k}: Pflicht-Quest hängt an optionaler Quest {d}')
        if k.startswith('st_'):
            for d in q.deps:
                ms = k[3:]
                if not (d == ms or d in HAUPT_KEYS or (d.startswith('st_') and d[3:] in HAUPT_KEYS)):
                    fehler.append(f'{k}: Story hängt an Nicht-Hauptstory-Quest {d}')
        if q.dep_any and len(q.deps) < 2: fehler.append(f'{k}: „eins von“ mit weniger als 2 Voraussetzungen')
    # 0.8.0: Belohnungen dürfen keine Stufe überspringen (_src/sperren.py)
    import sperren
    def ahnen(k, s=None):
        s = set() if s is None else s
        for d in alle.get(k).deps if k in alle else []:
            if d not in s: s.add(d); ahnen(d, s)
        return s
    fehler += sperren.pruefe(alle, ahnen)
    # Zyklen
    g = {q.key: q.deps for c in CHAPTERS for q in c.quests}
    seen, stack = set(), set()
    def dfs(k):
        if k in stack: fehler.append(f'Zyklus bei {k}'); return
        if k in seen: return
        seen.add(k); stack.add(k)
        for d in g.get(k, []): dfs(d)
        stack.discard(k)
    for k in g: dfs(k)
    return fehler

def schreibe_quest_tooltips():
    """0.10.0: Tooltip „Gebraucht für: <Quest>“ an jedem Aufgaben-Item (aus den Questdaten, deshalb immer aktuell)."""
    titel_kap = {q.key: c.title for c in CHAPTERS for q in c.quests}
    nutzung = {}
    for c in CHAPTERS:
        for q in c.quests:
            if q.repeat: continue                       # Markt-Tausche nicht, sonst stünde an jedem Rohstoff ein Händler
            for t in q.tasks:
                ids = [t[1]] if t[0] == 'item' else ([t[3]] if t[0] == 'tag' and t[3] else [])
                for i in ids:
                    nutzung.setdefault(i, [])
                    if q.title not in [x[0] for x in nutzung[i]]: nutzung[i].append((q.title, titel_kap[q.key]))
    zeilen = ['// ERZEUGT von _src/quests.py – nicht von Hand ändern. Zeigt an Aufgaben-Items, wofür sie im Questbuch gebraucht werden.',
              'const QUEST_NUTZUNG = {']
    for i in sorted(nutzung):
        n = nutzung[i]
        text = '; '.join(f'{t} ({k.split(":")[0]})' for t, k in n[:2]) + (f' und {len(n) - 2} weitere' if len(n) > 2 else '')
        zeilen.append(f'  {json.dumps(i)}: {json.dumps(text, ensure_ascii=False)},')
    zeilen += ['}', '', 'ItemEvents.modifyTooltips(event => {',
               '  Object.keys(QUEST_NUTZUNG).forEach(id => event.add(id, Text.darkAqua("Questbuch: " + QUEST_NUTZUNG[id])))',
               '})', '']
    pfad = os.path.join(PACK, 'kubejs', 'client_scripts', 'quest_tooltips.js')
    with open(pfad, 'w', encoding='utf-8', newline=chr(10)) as f: f.write(chr(10).join(zeilen))

def main():
    items = json.load(open(os.path.join(PACK, '_src', 'items.json'), encoding='utf-8'))['items']
    tags = json.load(open(os.path.join(PACK, '_src', 'tags.json'), encoding='utf-8'))
    b = Builder(os.path.join(PACK, 'config', 'ftbquests'), items, tags)
    # 0.8.0: jede Kiste gibt mehrere Items (loot_size), Inhalt passt zur Spielphase und hilft beim nächsten Schritt
    b.table('holz', 'Holzkiste', [('minecraft:string', 4, 10), ('minecraft:bone_meal', 12, 10), ('minecraft:flint', 4, 8),
        ('minecraft:oak_sapling', 2, 6), ('minecraft:birch_sapling', 2, 6), ('minecraft:baked_potato', 6, 8), ('minecraft:clay_ball', 8, 6),
        ('minecraft:iron_nugget', 6, 6), ('minecraft:torch', 12, 6), ('minecraft:dirt', 16, 6), ('exdeorum:string_mesh', 1, 3)],
        loot_size=3, crate=(0x8B5A2B, False, 3, 8, 0))
    b.table('eisen', 'Eisenkiste', [('minecraft:iron_ingot', 6, 10), ('minecraft:copper_ingot', 8, 10), ('create:zinc_ingot', 3, 8),
        ('create:andesite_alloy', 12, 8), ('minecraft:redstone', 12, 8), ('minecraft:coal', 12, 8), ('create:cogwheel', 6, 6),
        ('create:shaft', 8, 6), ('minecraft:lapis_lazuli', 8, 4), ('exdeorum:flint_mesh', 1, 4)],
        loot_size=3, crate=(0xC8C8C8, False, 0, 3, 0))
    b.table('gold', 'Goldkiste', [('minecraft:diamond', 2, 6), ('create:brass_ingot', 6, 8), ('mekanism:ingot_osmium', 6, 8),
        ('mysticalagriculture:prudentium_essence', 12, 6), ('minecraft:ender_pearl', 3, 6), ('minecraft:gold_ingot', 6, 8),
        ('minecraft:quartz', 16, 6), ('minecraft:glowstone_dust', 12, 6), ('mysticalagriculture:prosperity_shard', 8, 6)],
        loot_size=3, crate=(0xFFD700, False, 0, 0, 5))
    b.table('magie', 'Kiste der Magie', [('ars_nouveau:source_gem', 8, 10), ('ars_nouveau:magebloom_fiber', 4, 8), ('minecraft:amethyst_shard', 8, 8),
        ('minecraft:lapis_lazuli', 8, 8), ('minecraft:glowstone_dust', 8, 6), ('minecraft:experience_bottle', 4, 6),
        ('minecraft:gold_ingot', 3, 6), ('ars_nouveau:blue_archwood_sapling', 1, 4)], loot_size=3, crate=(0x7B3FB0, True, 0, 0, 0))
    b.table('technik', 'Kiste der Technik', [('create:andesite_alloy', 8, 10), ('create:cogwheel', 4, 8), ('create:shaft', 8, 8),
        ('create:iron_sheet', 4, 8), ('create:copper_sheet', 4, 6), ('create:belt_connector', 4, 6), ('minecraft:redstone', 12, 8),
        ('create:andesite_casing', 2, 6), ('create:fluid_pipe', 8, 4)], loot_size=3, crate=(0xB87333, False, 0, 0, 0))
    b.table('natur', 'Kiste der Natur', [('minecraft:bone_meal', 16, 10), ('minecraft:wheat_seeds', 8, 8), ('farmersdelight:cabbage_seeds', 4, 6),
        ('farmersdelight:tomato_seeds', 4, 6), ('minecraft:carrot', 6, 6), ('minecraft:potato', 6, 6), ('minecraft:sugar_cane', 4, 6),
        ('minecraft:oak_sapling', 2, 6), ('botanypots:terracotta_botany_pot', 2, 4), ('minecraft:cooked_beef', 4, 6), ('minecraft:honeycomb', 2, 4)],
        loot_size=3, crate=(0x4CAF50, False, 0, 0, 0))
    b.table('stern', 'Sternkiste', [('mysticalagradditions:nether_star_shard', 2, 4), ('minecraft:netherite_ingot', 1, 8),
        ('minecraft:enchanted_golden_apple', 1, 3),
        ('minecraft:netherite_scrap', 4, 5), ('minecraft:diamond', 8, 8), ('minecraft:totem_of_undying', 1, 3)],
        loot_size=2, crate=(0xA020F0, True, 0, 0, 5))
    fehler = pruefe_struktur() + TEXT_FEHLER
    errors = b.write(GROUPS, CHAPTERS, 'Sky and Stone', vorfehler=fehler)   # schreibt nur, wenn alles stimmt
    if not errors: schreibe_quest_tooltips()
    nq = sum(len(c.quests) for c in CHAPTERS)
    print(f'{len(CHAPTERS)} Kapitel, {nq} Quests ({len(HAUPT_KEYS)} Hauptstory, {len(story_q)} Story), {len(b.tables)} Belohnungstabellen')
    kreuz = sum(len(r['kreuzt']) for r in b.layout.values())
    print(f'Layout: {len(b.hinweise)} Probleme (Linie durch Quest / Überlappung), {kreuz} Linienkreuzungen')
    for h in b.hinweise: print('HINWEIS:', h)
    for e in errors: print('FEHLER:', e)
    if errors: print('Nichts geschrieben – die Questdateien sind unverändert.')
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
```

## Datei: _src/questlib.py
```py
"""Baukasten für FTB-Quests-Dateien (SNBT) – Sky and Stone.

Ein Kapitel ist eine Liste von Q(...)-Einträgen. IDs werden stabil aus Namen gehasht,
damit Fortschritt beim Neu-Erzeugen erhalten bleibt.
"""
import hashlib, json, os

# ---------------- IDs ----------------
def hid(*parts):
    h = hashlib.sha1('/'.join(parts).encode()).hexdigest().upper()[:16]
    return ('1' + h[1:]) if h[0] in '89ABCDEF0' else h   # positiv als long, nie 0

# ---------------- SNBT ----------------
class D(float): pass          # double
class L(int): pass            # long
class F(float): pass          # float

import re as _re
def _key(k):   # Schlüssel mit Sonderzeichen (z. B. 'ftbfiltersystem:filter') müssen in Anführungszeichen
    return k if _re.fullmatch(r'[A-Za-z0-9_.+-]+', k) else json.dumps(k, ensure_ascii=False)

def snbt(v, ind=0):
    p = '\t' * ind
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, D): return f'{float(v)}d'
    if isinstance(v, F): return f'{float(v)}f'
    if isinstance(v, L): return f'{int(v)}L'
    if isinstance(v, int): return str(v)
    if isinstance(v, float): return f'{v}d'
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        if not v: return '[ ]'
        if all(isinstance(x, str) for x in v) and len(v) <= 4 and sum(len(x) for x in v) < 70:
            return '[' + ', '.join(snbt(x) for x in v) + ']'
        return '[\n' + '\n'.join(p + '\t' + snbt(x, ind + 1) for x in v) + '\n' + p + ']'
    if isinstance(v, dict):
        if not v: return '{ }'
        return '{\n' + '\n'.join(f'{p}\t{_key(k)}: {snbt(x, ind + 1)}' for k, x in v.items()) + '\n' + p + '}'
    raise TypeError(type(v))

# ---------------- Aufgaben / Belohnungen ----------------
def item(i, n=1, consume=False, komponenten=None):
    """komponenten (0.8.0): Datenkomponenten, die das Item haben muss (FTB-Abgleich „fuzzy“),
    z. B. {'productivebees:bee_type': 'productivebees:iron'} für eine Eisenbienen-Wabe."""
    return ('item', i, n, consume, komponenten)
def tag(t, n=1, icon=None, title=None, consume=False):  return ('tag', t, n, icon, title, consume)   # irgendein Item aus der Gruppe (FTB Filter System)

# Eigene Gruppen aus kubejs/server_scripts/gruppen.js. Rückfall, solange eine neue Gruppe noch nicht im Tag-Dump steht;
# steht sie dort, prüft der Generator zusätzlich, dass sie nicht leer ist.
EIGENE_TAGS = {'skyandstone:sieves', 'skyandstone:water_crucibles', 'skyandstone:hopper_botany_pots',
               'skyandstone:archwood_saplings', 'skyandstone:roofs', 'skyandstone:rope_bridges', 'skyandstone:weg_zum_herz',
               'skyandstone:erz_ohne_sieb'}
def check():                      return ('checkmark',)
def dim(d):                       return ('dimension', d)
def kill(e, n=1):                 return ('kill', e, n)
def energie(fe):                  return ('forge_energy', fe)   # 0.8.0: Strom in einen Aufgabenbildschirm einspeisen

def xp(n):                        return ('xp', n)
def give(i, n=1, komponenten=None): return ('give', i, n, komponenten)   # komponenten: z. B. Name/Lore einer Tagebuchseite
def crate(name, team=False, art='loot'):
    """Belohnung aus einer Tabelle. art: 'loot' = die Kiste selbst ins Inventar (zum Öffnen, 0.8.0),
    'choice' = Spieler wählt ein Item aus der Tabelle, 'random' = ein zufälliges Item direkt (bis 0.7.0 überall).
    team=True: eine pro Team statt pro Spieler."""
    return ('table', name, team, art)

class Q:
    def __init__(self, key, title, x, y, tasks, desc=(), sub='', deps=(), rewards=(), shape=None, size=None,
                 icon=None, optional=False, dep_any=False, repeat=None):
        self.key, self.title, self.x, self.y = key, title, x, y
        self.tasks = tasks if isinstance(tasks, list) else [tasks]
        self.desc, self.sub, self.deps, self.rewards = list(desc), sub, list(deps), list(rewards)
        self.shape, self.size, self.icon, self.optional, self.dep_any = shape, size, icon, optional, dep_any
        self.repeat = repeat   # Abklingzeit in Sekunden -> wiederholbar

class Chapter:
    def __init__(self, key, title, group, icon, quests, sub='', links=(), mode='baum'):
        self.key, self.title, self.group, self.icon, self.quests, self.sub = key, title, group, icon, quests, sub
        self.links = list(links)   # Quest-Schlüssel aus anderen Kapiteln, die hier als Verweis erscheinen
        self.mode = mode           # 'baum' = Spalten nach Abhängigkeit, 'pfad' = Schlangenlinie in Listenreihenfolge

def pfad_layout(items, per_row=5, dx=2.0, dy=3.0):
    """Schlangenlinie: Reihen zu per_row, Richtung wechselt je Reihe, leichter Zickzack. items = [(schlüssel, größe)]."""
    pos, x, row, col = {}, 0.0, 0, 0
    prev = None
    for i, (k, s) in enumerate(items):
        if col == per_row:
            row, col, prev = row + 1, 0, None
        richtung = 1 if row % 2 == 0 else -1
        if prev is not None:
            x += richtung * max(dx, (prev + s) * 0.5 + 0.6)
        zick = 0.45 if col % 2 else -0.45
        extra = max(0.0, (s - 1.0) * 0.6)   # große Meilensteine etwas tiefer, damit sie nicht in die Reihe darüber ragen
        pos[k] = (round(x, 2), round(row * dy + zick + extra, 2))
        prev, col = s, col + 1
    return pos

# ---------------- Automatisches Layout (0.6.4) ----------------
# Spalten nach Abhängigkeitstiefe, Verweise direkt eine Spalte vor ihrer ersten Quest. Lange Kapitel laufen
# als Schlange: nach `breite` Spalten geht es eine Reihe tiefer in die andere Richtung weiter.
# Danach verschiebt eine Suche Quests innerhalb ihrer Spalte, bis möglichst keine Linie mehr durch eine
# fremde Quest läuft und sich wenige Linien kreuzen (Maßstab: layoutcheck.py, wie FTB Quests zeichnet).
import random

def ebenen_layout(chapter, dx=2.4, dy=1.8, max_zeilen=6, runden=8000):
    import layoutcheck as LC
    qs = {q.key: q for q in chapter.quests}
    alle_links = [l for l in chapter.links if l not in qs]
    hat_kind = {l for l in alle_links if any(l in q.deps for q in qs.values())}
    links = [l for l in alle_links if l in hat_kind]          # Verweise mit Linie: Teil des Baums
    nur_info = [l for l in alle_links if l not in hat_kind]   # reine Verweise: eigene Reihe oben, ohne Linien
    nodes = list(qs) + links
    size = {k: (qs[k].size or 1.0) if k in qs else 1.0 for k in nodes}
    deps = {k: [d for d in qs[k].deps if d in qs or d in links] for k in qs}
    deps.update({l: [] for l in links})
    kinder = {k: [c for c in qs if k in deps[c]] for k in nodes}
    layer = {}
    def lq(k, seen=()):
        if k in layer: return layer[k]
        if k in seen: return 0
        ps = [p for p in deps[k] if p in qs]
        layer[k] = 0 if not ps else 1 + max(lq(p, seen + (k,)) for p in ps)
        return layer[k]
    for k in qs: lq(k)
    if links:   # Platz für Verweise direkt vor ihrer ersten Quest
        for k in qs: layer[k] += 1
        for l in links:
            ks = [layer[c] for c in kinder[l]]
            layer[l] = max(0, min(ks) - 1) if ks else 0
    # Zu volle Spalten aufteilen: Überzählige eine Spalte weiter, alles dahinter rückt nach
    L = 0
    while L <= max(layer.values()):
        ks = [k for k in nodes if layer[k] == L]
        if len(ks) > max_zeilen:
            ks.sort(key=lambda k: (len(kinder[k]) == 0, nodes.index(k)))   # Quests mit Nachfolgern bleiben vorn
            rest = set(ks[max_zeilen:])
            for k in nodes:
                if layer[k] > L or k in rest: layer[k] += 1
        L += 1
    # Verweise, die nur Nachfolger weiter rechts haben, so nah wie möglich davor
    for l in links:
        ks = [layer[c] for c in kinder[l]]
        if ks:
            ziel = min(ks) - 1
            if sum(1 for k in nodes if layer[k] == ziel and k != l) < max_zeilen: layer[l] = max(0, ziel)
    def spalten(layer):
        cols = {}
        for k in nodes: cols.setdefault(layer[k], []).append(k)
        return cols
    cols = spalten(layer)
    order = {k: i for i, k in enumerate(nodes)}
    for _ in range(6):   # Mittelwert der Nachbarn -> wenige Kreuzungen
        for L in sorted(cols):
            def bary(k):
                nb = [order[p] for p in deps[k] + kinder[k]]
                return sum(nb) / len(nb) if nb else order[k]
            cols[L].sort(key=bary)
            for i, k in enumerate(cols[L]): order[k] = L * 100 + i
    slot = {}
    for L, ks in cols.items():
        y = 0.0
        for i, k in enumerate(ks):
            if i: y += max(1.0, (size[ks[i - 1]] + size[k]) * 0.5 / dy + 0.35)
            slot[k] = y
        mid = y / 2
        for k in ks: slot[k] -= mid   # Spalten mittig ausrichten
    def pos_of(layer, slot): return {k: (round(layer[k] * dx, 2), round(slot[k] * dy, 2)) for k in nodes}
    def frei(layer, slot, k):
        return all(abs(slot[k] - slot[o]) >= (size[k] + size[o]) * 0.5 / dy + 0.25 for o in nodes if o != k and layer[o] == layer[k])
    def kosten(layer, slot):
        pos = pos_of(layer, slot)
        ch = {'quests': [{'id': k, 'x': pos[k][0], 'y': pos[k][1], 'size': size[k], 'dependencies': deps[k]} for k in qs],
              'quest_links': [{'linked_quest': l, 'x': pos[l][0], 'y': pos[l][1], 'size': 1.0} for l in links]}
        r = LC.pruefe(ch)
        ausdehnung = (max(slot.values()) - min(slot.values())) * 0.5 + sum(abs(v) for v in slot.values()) * 0.02
        return 100 * len(r['durch']) + 100 * len(r['ueberlappt']) + 10 * len(r['kreuzt']) + ausdehnung
    start_layer, start_slot = dict(layer), dict(slot)
    gesamt = None
    for versuch in range(16):          # 0.7.0: weitere Anläufe nur, solange noch eine Linie durch eine Quest läuft
      layer, slot = dict(start_layer), dict(start_slot)
      rnd = random.Random(chapter.key if versuch == 0 else f'{chapter.key}/{versuch}')   # fest -> gleiche Ausgabe
      best = kosten(layer, slot)
      if len(nodes) > 1:
        for _ in range(runden):
              if best < 2: break
              k = rnd.choice(nodes)
              nl, ns = dict(layer), dict(slot)
              art = rnd.random()
              if art < 0.4:                                   # mit einer Quest derselben Spalte tauschen
                  os_ = [x for x in nodes if x != k and layer[x] == layer[k]]
                  if not os_: continue
                  o = rnd.choice(os_); ns[k], ns[o] = slot[o], slot[k]
              elif art < 0.8:                                 # in der Spalte verschieben
                  ns[k] = slot[k] + rnd.choice([-2.0, -1.5, -1.0, -0.5, 0.5, 1.0, 1.5, 2.0])
                  if not frei(nl, ns, k): continue
              else:                                           # eine Spalte nach links/rechts, wenn die Abhängigkeiten es erlauben
                  lo = max([layer[d] + 1 for d in deps[k]], default=0)
                  hi = min([layer[c] - 1 for c in kinder[k]], default=layer[k] + 1)
                  ziel = layer[k] + rnd.choice([-1, 1])
                  if not (lo <= ziel <= hi): continue
                  nl[k] = ziel
                  if sum(1 for o in nodes if nl[o] == ziel) > max_zeilen or not frei(nl, ns, k): continue
              c = kosten(nl, ns)
              if c < best: best, layer, slot = c, nl, ns
      if gesamt is None or best < gesamt[0]: gesamt = (best, layer, slot)
      if gesamt[0] < 100: break
    best, layer, slot = gesamt
    m = min(layer.values())
    pos = pos_of({k: v - m for k, v in layer.items()}, slot)
    for k, q in qs.items(): q.x, q.y = pos[k]
    out = {l: pos[l] for l in links}
    if nur_info:
        top = min(p[1] - size[k] / 2 for k, p in pos.items()) - 2.0
        for i, l in enumerate(nur_info):
            r, c = divmod(i, 10)
            out[l] = (round(c * 1.6, 2), round(top - r * 1.5, 2))
    return out

def auto_layout(chapter, dx=2.2, dy=1.7, link_gap=2.6):
    if chapter.quests: return ebenen_layout(chapter)
    return pfad_layout([(k, 1.0) for k in chapter.links])   # reine Verweis-Kapitel (Story)

def auto_layout_alt(chapter, dx=2.2, dy=1.7, link_gap=2.6):
    """Spalten nach Abhängigkeitstiefe (nur Abhängigkeiten im selben Kapitel), Zeilen nach Eltern-Mittelwert.
    Verweise (links) stehen in einer eigenen Spalte ganz links. Gibt {schlüssel: (x, y)} für Verweise zurück."""
    if chapter.mode == 'pfad':
        if chapter.quests:   # Hauptstory: Quests als Pfad, Verweise (falls vorhanden) darüber
            pos = pfad_layout([(q.key, q.size or 1.0) for q in chapter.quests])
            for q in chapter.quests: q.x, q.y = pos[q.key]
            return {k: (i * 1.6, -2.6) for i, k in enumerate(chapter.links)}
        return pfad_layout([(k, 1.0) for k in chapter.links])
    keys = {q.key: q for q in chapter.quests}
    depth = {}
    def d(k, seen=()):
        if k in depth: return depth[k]
        if k in seen: return 0
        ps = [p for p in keys[k].deps if p in keys]
        depth[k] = 0 if not ps else 1 + max(d(p, seen + (k,)) for p in ps)
        return depth[k]
    for k in keys: d(k)
    cols = {}
    for q in chapter.quests: cols.setdefault(depth[q.key], []).append(q)
    max_rows = 6
    link_cols = (len(chapter.links) + max_rows - 1) // max_rows
    x = (link_gap + (link_cols - 1) * 1.6) if chapter.links else 0.0
    ypos, prev_size = {}, None
    order = {q.key: i for i, q in enumerate(chapter.quests)}
    for col in sorted(cols):
        qs = cols[col]
        def pref(q):
            ps = [ypos[p] for p in q.deps if p in ypos]
            return sum(ps) / len(ps) if ps else order[q.key] * 0.001
        qs.sort(key=pref)
        # zu hohe Spalten in mehrere Teilspalten aufteilen
        parts = [qs[i:i + max_rows] for i in range(0, len(qs), max_rows)]
        for part in parts:
            big = max((q.size or 1.0) for q in part)
            if prev_size is not None:
                x += max(dx, (prev_size + big) * 0.5 + 0.6)
            prev_size = big
            sizes = [(q.size or 1.0) for q in part]
            ys, y = [], 0.0
            for i, s in enumerate(sizes):
                if i: y += max(dy, (sizes[i - 1] + s) * 0.5 + 0.45)
                ys.append(y)
            target = (sum(pref(q) for q in part) / len(part)) if col and len(parts) == 1 else 0.0
            shift = target - (ys[0] + ys[-1]) / 2
            for q, yy in zip(part, ys):
                q.x, q.y = round(x, 2), round(yy + shift, 2)
                ypos[q.key] = q.y
    links = {}
    for i, k in enumerate(chapter.links):   # Verweise in Spalten zu höchstens 6
        col, row = divmod(i, max_rows)
        in_col = min(max_rows, len(chapter.links) - col * max_rows)
        links[k] = (round(col * 1.6, 2), round((row - (in_col - 1) / 2) * 1.5, 2))
    return links

# ---------------- Ausgabe ----------------
# Gegen Tippfehler in Kill-/Dimensions-Aufgaben (items.json kennt nur Items). Neue Ziele hier eintragen.
BEKANNTE_DIMENSIONEN = {'minecraft:overworld', 'minecraft:the_nether', 'minecraft:the_end'}
BEKANNTE_MOBS = {'minecraft:ender_dragon', 'minecraft:wither', 'ars_nouveau:wilden_boss'}

class Builder:
    def __init__(self, out_dir, known_items, known_tags=()):
        self.out, self.known = out_dir, set(known_items)
        self.known_tags = set(known_tags)
        # 0.7.0: Inhalt der Gruppen (tags.json vom Testserver, kubejs/dev_tags.json), damit leere Gruppen auffallen
        self.tag_inhalt = dict(known_tags) if isinstance(known_tags, dict) else {}
        self.lang = {}                 # Schlüssel -> Text/Liste
        self.qids = {}                 # 'kapitel/quest' und 'quest' -> ID
        self.tables = {}               # name -> (id, rewards)
        self.errors = []
        self.hinweise = []            # Layout-Probleme: werden gemeldet, blockieren aber nicht

    def check_item(self, i, where):
        if self.known and i not in self.known: self.errors.append(f'{where}: unbekanntes Item {i}')

    def table(self, name, title, entries, loot_size=1, crate=None):
        tid = hid('table', name)
        rewards = []
        for i, n, w in entries:
            self.check_item(i, f'Tabelle {name}')
            rewards.append({'count': n, 'id': hid('table', name, i), 'item': {'count': 1, 'id': i}, 'type': 'item', 'weight': F(w)})
        data = {'id': tid, 'loot_size': loot_size, 'rewards': rewards, 'use_title': True}
        if crate:   # (Farbe, leuchtet, passiv, Monster, Boss) -> Kisten-Item, das Mobs fallen lassen
            color, glow, pa, mo, bo = crate
            data['loot_crate'] = {'color': color, 'drops': {'boss': bo, 'monster': mo, 'passive': pa}, 'glow': glow, 'item_name': '', 'string_id': name + 'kiste'}
        self.tables[name] = (tid, data)
        self.lang[f'reward_table.{tid}.title'] = title

    def register(self, chapters):
        for c in chapters:
            for q in c.quests:
                qid = hid('quest', c.key, q.key)
                if q.key in self.qids: self.errors.append(f'doppelter Quest-Schlüssel {q.key}')
                self.qids[q.key] = qid

    def _task(self, c, q, n, t):
        tid = hid('task', c.key, q.key, str(n))
        if t[0] == 'item':
            self.check_item(t[1], f'{c.key}/{q.key}')
            d = {'id': tid, 'item': {'count': 1, 'id': t[1]}, 'type': 'item'}
            if t[2] != 1: d['count'] = L(t[2])
            if t[3]: d['consume_items'] = True
            if len(t) > 4 and t[4]:
                d['item']['components'] = dict(t[4]); d['match_components'] = 'fuzzy'
            return d
        if t[0] == 'tag':
            tg, n_, icon, title = t[1:5]
            if self.known_tags and tg not in self.known_tags and tg not in EIGENE_TAGS:
                self.errors.append(f'{c.key}/{q.key}: unbekannte Item-Gruppe {tg}')
            elif tg in self.tag_inhalt and not self.tag_inhalt[tg]:
                self.errors.append(f'{c.key}/{q.key}: Item-Gruppe {tg} ist leer (Aufgabe unerfüllbar)')
            d = {'id': tid, 'item': {'components': {'ftbfiltersystem:filter': f'item_tag({tg})'}, 'count': 1,
                                     'id': 'ftbfiltersystem:smart_filter'}, 'type': 'item'}
            if n_ != 1: d['count'] = L(n_)
            if len(t) > 5 and t[5]: d['consume_items'] = True
            if icon:
                self.check_item(icon, f'{c.key}/{q.key} Aufgaben-Icon'); d['icon'] = {'count': 1, 'id': icon}
            if title: self.lang[f'task.{tid}.title'] = title
            return d
        if t[0] == 'checkmark': return {'id': tid, 'type': 'checkmark'}
        if t[0] == 'dimension':
            if t[1] not in BEKANNTE_DIMENSIONEN: self.errors.append(f'{c.key}/{q.key}: unbekannte Dimension {t[1]}')
            return {'dimension': t[1], 'id': tid, 'type': 'dimension'}
        if t[0] == 'kill':
            if t[1] not in BEKANNTE_MOBS: self.errors.append(f'{c.key}/{q.key}: unbekannter Mob {t[1]} (in BEKANNTE_MOBS eintragen)')
            return {'entity': t[1], 'id': tid, 'type': 'kill', 'value': L(t[2])}
        if t[0] == 'forge_energy': return {'id': tid, 'type': 'forge_energy', 'value': L(t[1])}
        raise ValueError(t)

    def _reward(self, c, q, n, r):
        rid = hid('reward', c.key, q.key, str(n))
        if r[0] == 'xp': return {'id': rid, 'type': 'xp', 'xp': r[1]}
        if r[0] == 'give':
            self.check_item(r[1], f'{c.key}/{q.key} Belohnung')
            d = {'id': rid, 'item': {'count': 1, 'id': r[1]}, 'type': 'item'}
            if len(r) > 3 and r[3]: d['item']['components'] = dict(r[3])
            if r[2] != 1: d['count'] = r[2]
            return d
        if r[0] == 'table':
            if r[1] not in self.tables: self.errors.append(f'{q.key}: Tabelle {r[1]} fehlt'); return None
            art = r[3] if len(r) > 3 else 'random'
            if art not in ('loot', 'choice', 'random', 'all_table'): raise ValueError(art)
            d = {'id': rid, 'table_id': L(int(self.tables[r[1]][0], 16)), 'type': art}
            if len(r) > 2 and r[2]: d['team_reward'] = True
            return d
        raise ValueError(r)

    def chapter(self, c, group_id, order):
        cid = hid('chapter', c.key)
        self.lang[f'chapter.{cid}.title'] = c.title
        if c.sub: self.lang[f'chapter.{cid}.chapter_subtitle'] = c.sub if isinstance(c.sub, list) else [c.sub]
        link_pos = auto_layout(c)
        self.check_item(c.icon, f'Kapitel {c.key} Icon')
        quests = []
        for q in c.quests:
            qid = self.qids[q.key]
            self.lang[f'quest.{qid}.title'] = q.title
            if q.sub: self.lang[f'quest.{qid}.quest_subtitle'] = q.sub
            if q.desc: self.lang[f'quest.{qid}.quest_desc'] = q.desc
            d = {}
            deps = []
            for k in q.deps:
                if k not in self.qids: self.errors.append(f'{q.key}: Abhängigkeit {k} fehlt'); continue
                deps.append(self.qids[k])
            if deps: d['dependencies'] = deps
            if q.dep_any and len(deps) > 1: d['dependency_requirement'] = 'one_completed'
            if q.icon:
                self.check_item(q.icon, f'{q.key} Icon'); d['icon'] = {'count': 1, 'id': q.icon}
            d['id'] = qid
            if q.optional: d['optional'] = True
            if q.repeat: d['can_repeat'] = True; d['repeat_cooldown'] = int(q.repeat)
            rewards = [r for r in (self._reward(c, q, n, r) for n, r in enumerate(q.rewards)) if r]
            if rewards: d['rewards'] = rewards
            if q.shape: d['shape'] = q.shape
            if q.size: d['size'] = D(q.size)
            d['tasks'] = [self._task(c, q, n, t) for n, t in enumerate(q.tasks)]
            d['x'] = D(q.x); d['y'] = D(q.y)
            quests.append(d)
        links = []
        for k, (x, y) in link_pos.items():
            if k not in self.qids: self.errors.append(f'Kapitel {c.key}: Verweis auf unbekannte Quest {k}'); continue
            links.append({'id': hid('link', c.key, k), 'linked_quest': self.qids[k], 'shape': 'square', 'size': D(1.0), 'x': D(x), 'y': D(y)})
        data = {'default_hide_dependency_lines': False, 'default_quest_shape': '', 'filename': c.key,
                'group': group_id, 'icon': {'count': 1, 'id': c.icon}, 'id': cid, 'order_index': order,
                'quest_links': links, 'quests': quests}
        return data

    def write(self, groups, chapters, file_title, vorfehler=()):
        """Erst alles erzeugen und prüfen, dann schreiben. Bei Fehlern bleibt der alte Stand auf der Platte
        (Nachtschicht 0.6.3: vorher stand ein unbekanntes Item trotz FEHLER in der SNBT)."""
        self.register(chapters)
        qdir = os.path.join(self.out, 'quests')
        out = {}                       # Pfad -> Daten
        gids = {}
        glist = []
        for g_key, g_title in groups:
            gid = hid('group', g_key); gids[g_key] = gid
            glist.append({'id': gid}); self.lang[f'chapter_group.{gid}.title'] = g_title
        import ftbformat as FF
        out[os.path.join(qdir, 'chapter_groups.snbt')] = FF.gruppen([g['id'] for g in glist])
        import layoutcheck as LC
        namen = {v: k for k, v in self.qids.items()}
        self.layout = {}
        je_gruppe = {}
        for n, c in enumerate(chapters):
            data = self.chapter(c, gids[c.group], n)
            idx = je_gruppe.get(c.group, 0); je_gruppe[c.group] = idx + 1
            out[os.path.join(qdir, 'chapters', c.key + '.snbt')] = FF.kapitel(data, idx)
            r = LC.pruefe(data, namen)
            self.layout[c.key] = r
            for a, b, x in r['durch']: self.hinweise.append(f'Layout {c.key}: Linie {a} -> {b} läuft durch {x}')
            for a, b in r['ueberlappt']: self.hinweise.append(f'Layout {c.key}: {a} und {b} überlappen sich')
        for i, name in enumerate(sorted(self.tables)):
            out[os.path.join(qdir, 'reward_tables', name + '.snbt')] = FF.tabelle(self.tables[name][1], i)
        self.lang['file.0000000000000001.title'] = file_title   # die Questdatei hat in FTB Quests immer die ID 1
        out[os.path.join(qdir, 'data.snbt')] = FF.daten({
            'default_autoclaim_rewards': 'disabled', 'default_consume_items': False, 'default_quest_disable_jei': False,
            'default_quest_shape': 'circle', 'default_reward_team': False, 'detection_delay': 20,
            'disable_gui': False, 'drop_book_on_death': False, 'drop_loot_crates': True, 'loot_crate_no_drop': {'boss': 0, 'monster': 1000, 'passive': 4000}, 'emergency_items_cooldown': 300,
            'fallback_locale': 'de_de', 'grid_scale': D(0.5), 'hide_excluded_quests': False, 'id': hid('file'),
            'lock_message': '', 'pause_game': False, 'progression_mode': 'flexible', 'show_lock_icons': True, 'version': 13}, D)
        # Deutsch als Hauptsprache, Englisch als Rückfall mit gleichem Text
        for loc in ('de_de', 'en_us'):
            out[os.path.join(qdir, 'lang', loc + '.snbt')] = dict(sorted(self.lang.items()))
        errors = list(vorfehler) + self.errors
        if errors: return errors       # nichts schreiben
        for sub in ('chapters', 'reward_tables', 'lang'):
            d = os.path.join(qdir, sub); os.makedirs(d, exist_ok=True)
            for f in os.listdir(d):
                if f.endswith('.snbt'): os.remove(os.path.join(d, f))
        for path, data in out.items():
            if os.sep + 'lang' + os.sep in path: self._w(path, data)      # Sprachdateien schreibt FTB nicht neu
            else:
                with open(path, 'w', encoding='utf-8', newline='') as f: f.write(FF.text(data))
        return errors

    @staticmethod
    def _w(path, data):
        with open(path, 'w', encoding='utf-8', newline='\n') as f: f.write(snbt(data) + '\n')
```

## Datei: _src/ftbformat.py
```py
"""Schreibt Questdateien genau so, wie FTB Quests 2101.1.37 sie selbst speichert (0.7.0).

Grund: FTB Quests speichert beim ersten Welt-Save alle Kapitel, Tabellen, Gruppen und data.snbt neu.
Weichen die Bytes vom Pack ab, stimmen die Hashes nicht mehr, und packwiz-installer stellt die Datei
später nicht wieder her (er prüft nur seinen Cache gegen den Index). Mit identischem Format ist das egal.
Regeln ermittelt aus Instanzdateien und Bytecode (Audit E, 25.10.2026), 25/25 Dateien byte-gleich.
lang/*.snbt schreibt FTB nicht neu – dafür bleibt der alte Schreiber in questlib.py.
"""
import json, re

class Byte(int): pass         # 1b
class Single(dict): pass      # Compound, den FTB in einer Zeile schreibt: { a: 1, b: "x" }

def _key(k):
    return k if re.fullmatch(r'[A-Za-z0-9_.+-]+', k) else json.dumps(k, ensure_ascii=False)

def _num(v):
    n = type(v).__name__
    if isinstance(v, bool): return 'true' if v else 'false'
    if n == 'Byte': return f'{int(v)}b'
    if n == 'D': return f'{float(v)}d'
    if n == 'F': return f'{float(v)}f'
    if n == 'L': return f'{int(v)}L'
    if isinstance(v, int): return str(v)
    if isinstance(v, float): return f'{v}d'
    if isinstance(v, str): return json.dumps(v, ensure_ascii=False)
    raise TypeError(type(v))

def w(v, ind=0):
    """Schlüssel alphabetisch, Tabs, Listen mit 1 Element inline, ab 2 Elementen mehrzeilig."""
    p = '\t' * ind
    if isinstance(v, Single):
        return '{ ' + ', '.join(f'{_key(k)}: {w(v[k], ind)}' for k in sorted(v)) + ' }'
    if isinstance(v, dict):
        if not v: return '{ }'
        return '{\n' + ''.join(f'{p}\t{_key(k)}: {w(v[k], ind + 1)}\n' for k in sorted(v)) + p + '}'
    if isinstance(v, list):
        if not v: return '[ ]'
        if len(v) == 1: return '[' + w(v[0], ind) + ']'
        return '[\n' + ''.join(f'{p}\t{w(x, ind + 1)}\n' for x in v) + p + ']'
    return _num(v)

def text(d):
    """Dateiinhalt mit CRLF und Zeilenumbruch am Ende (wie FTB)."""
    return (w(d) + '\n').replace('\n', '\r\n')

def _icon(d):
    d = dict(d)
    if d.get('count') == 1: d.pop('count')
    return d

def _single(d):
    return Single({k: (_single(x) if isinstance(x, dict) else x) for k, x in d.items()})

def _task(t):
    t = dict(t)
    if 'item' in t: t['item'] = _single(t['item'])
    if 'icon' in t: t['icon'] = _icon(t['icon'])
    return t

def _reward(r, in_table=False):
    r = dict(r)
    if r.get('count') == 1: r.pop('count')
    if in_table and r.get('type') == 'item': r.pop('type')
    return r

def kapitel(c, order_index):
    c = dict(c)
    c['icon'] = _icon(c['icon'])
    c.setdefault('images', [])
    c['order_index'] = order_index          # Index innerhalb der eigenen Gruppe
    links = []
    for l in c.get('quest_links', []):
        l = dict(l)
        if float(l.get('size', 1.0)) == 1.0: l.pop('size', None)
        links.append(l)
    c['quest_links'] = links
    qs = []
    for q in c['quests']:
        q = dict(q)
        if 'icon' in q: q['icon'] = _icon(q['icon'])
        if 'tasks' in q: q['tasks'] = [_task(t) for t in q['tasks']]
        if 'rewards' in q: q['rewards'] = [_reward(r) for r in q['rewards']]
        qs.append(q)
    c['quests'] = qs
    return c

def tabelle(t, order_index):
    t = dict(t)
    t['order_index'] = order_index          # alphabetische Reihenfolge der Dateinamen
    t['rewards'] = [_reward(r, True) for r in t['rewards']]
    lc = t.get('loot_crate')
    if lc:
        lc = dict(lc)
        if lc.get('glow') is False: lc.pop('glow')
        elif lc.get('glow') is True: lc['glow'] = Byte(1)
        if lc.get('item_name') == '': lc.pop('item_name')
        t['loot_crate'] = lc
    return t

def daten(d, D):
    d = dict(d)
    d.pop('id', None)                       # FTB liest kein id aus data.snbt, die Datei hat immer ID 1
    d['presets'] = {'goal': {'shape': 'hexagon', 'size': D(2.0)}, 'info': {'shape': 'gear', 'size': D(1.0)},
                    'normal': {'shape': 'square', 'size': D(1.0)}}
    d['verify_on_load'] = False
    return d

def gruppen(ids):
    return {'chapter_groups': [Single({'id': g}) for g in ids]}
```

## Datei: _src/layoutcheck.py
```py
"""Prüft das Questbuch-Layout so, wie FTB Quests es zeichnet (0.6.4).
Linien: gerade Strecken von jeder Voraussetzung zur Quest. Liegt die Voraussetzung in einem anderen Kapitel,
startet die Linie am Verweis (quest_link) – fehlt der Verweis, gibt es keine Linie.
Gemeldet wird: Linie läuft durch eine fremde Quest, Quests überlappen sich, Linien kreuzen sich.
"""
import math

RAND = 0.15   # Abstand, den eine Linie zum Rand einer fremden Quest mindestens halten soll

def _knoten(ch):
    k = {}   # quest-id -> (x, y, radius)
    for q in ch['quests']:
        k[q['id']] = (float(q['x']), float(q['y']), float(q.get('size', 1.0)) / 2)
    for l in ch['quest_links']:
        k.setdefault(l['linked_quest'], (float(l['x']), float(l['y']), float(l.get('size', 1.0)) / 2))
    return k

def kanten(ch):
    k = _knoten(ch)
    out = []
    for q in ch['quests']:
        for d in q.get('dependencies', []):
            if d in k: out.append((d, q['id']))
    return k, out

def _abstand(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    l2 = dx * dx + dy * dy
    t = 0 if l2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / l2))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))

def _kreuzen(p1, p2, p3, p4):
    def o(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    d1, d2, d3, d4 = o(p3, p4, p1), o(p3, p4, p2), o(p1, p2, p3), o(p1, p2, p4)
    return (d1 * d2 < -1e-9) and (d3 * d4 < -1e-9)

def pruefe(ch, namen=None):
    """-> dict mit Listen 'durch', 'ueberlappt', 'kreuzt'. namen: id -> lesbarer Schlüssel."""
    n = namen or {}
    k, ks = kanten(ch)
    res = {'durch': [], 'ueberlappt': [], 'kreuzt': []}
    ids = list(k)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            ax, ay, ar = k[a]; bx, by, br = k[b]
            if math.hypot(ax - bx, ay - by) < ar + br - 0.05: res['ueberlappt'].append((n.get(a, a), n.get(b, b)))
    for a, b in ks:
        ax, ay, _ = k[a]; bx, by, _ = k[b]
        for c, (cx, cy, cr) in k.items():
            if c in (a, b): continue
            if _abstand(cx, cy, ax, ay, bx, by) < cr + RAND: res['durch'].append((n.get(a, a), n.get(b, b), n.get(c, c)))
    for i, (a, b) in enumerate(ks):
        for c, d in ks[i + 1:]:
            if len({a, b, c, d}) < 4: continue
            if _kreuzen(k[a][:2], k[b][:2], k[c][:2], k[d][:2]): res['kreuzt'].append(((n.get(a, a), n.get(b, b)), (n.get(c, c), n.get(d, d))))
    return res
```

## Datei: _src/sperren.py
```py
"""Items, die als Quest-Belohnung erst ab einem bestimmten Meilenstein erlaubt sind (0.8.0).

Der Generator prüft: Gibt eine Quest so ein Item, muss der Meilenstein die Quest selbst oder eine ihrer
(indirekten) Voraussetzungen sein. Sonst würde die Belohnung eine Stufe überspringen.
VERBOTEN: Items, die nie als Belohnung kommen sollen (Maschinen-Kerne, Stufen-Samen, Prägeplatten …).
"""
import re

AB = {
    # Create / Messing-Schwelle
    'create:brass_ingot': 'c_messing', 'create:brass_sheet': 'c_messing', 'create:brass_nugget': 'c_messing',
    'create:brass_casing': 'c_messing', 'create:precision_mechanism': 'c_mechanismus', 'createsifter:brass_mesh': 'c_messing',
    'create:blaze_burner': 'c_brenner', 'createsifter:zinc_mesh': 'c_sifter',
    # Mystical Agriculture: Essenz-Stufen
    'mysticalagriculture:prudentium_essence': 'm_inferium', 'mysticalagriculture:tertium_essence': 'm_tertium',
    'mysticalagriculture:imperium_essence': 'm_imperium', 'mysticalagriculture:supremium_essence': 'm_supremium',
    'mysticalagradditions:insanium_essence': 'm_insanium', 'mysticalagriculture:infusion_crystal': 'm_inferium',
    # Mekanism
    'mekanism:ingot_osmium': 'k_osmium', 'mekanism:alloy_infused': 'k_alloy', 'mekanism:alloy_reinforced': 'z_elite',
    'mekanism:alloy_atomic': 'z_elite', 'mekanism:basic_control_circuit': 'k_schalt', 'mekanism:advanced_control_circuit': 'k_alloy',
    'mekanism:elite_control_circuit': 'z_elite', 'mekanism:ultimate_control_circuit': 'z_ultkreis', 'mekanism:ingot_steel': 'k_stahl',
    # AE2
    'ae2:logic_processor': 'l_prozessoren', 'ae2:calculation_processor': 'l_prozessoren', 'ae2:engineering_processor': 'l_prozessoren',
    'ae2:fluix_crystal': 'l_lader', 'ae2:certus_quartz_crystal': 'l_certus',
    # Nether / End / Bosse
    'minecraft:blaze_rod': 'j_lohe', 'minecraft:nether_star': 'j_wither', 'mysticalagradditions:nether_star_shard': 'j_wither',
    'minecraft:netherite_ingot': 'j_nether', 'minecraft:netherite_scrap': 'j_nether', 'minecraft:ancient_debris': 'j_nether',
    'minecraft:ender_eye': 'j_augen', 'minecraft:end_portal_frame': 'j_rahmen', 'minecraft:shulker_shell': 'j_end',
    'minecraft:dragon_breath': 'j_drache', 'minecraft:elytra': 'j_drache',
}
VERBOTEN = [
    r'^mysticalagriculture:(?!inferium_seeds$).*_seeds$',   # Ressourcen-Samen sind der Fortschritt selbst
    r'^ae2:.*_press$', r'^ae2:controller$', r'^mekanism:pellet_', r'^mekanism:.*_reactor', r'^mekanismgenerators:',
    r'^hostilenetworks:', r'^industrialforegoing:(?!plastic$|dryrubber$|tinydryrubber$)', r'^ars_nouveau:.*_spell_book$',
    r'^ironjetpacks:jetpack$', r'^tiab:', r'^minecraft:(dragon_egg|totem_of_undying|enchanted_golden_apple)$',
]

# Kisten-Stufen: Goldkiste enthält Messing/Osmium, Sternkiste Endgame-Items. Bosse dürfen früher (großer Aufwand).
KISTE_AB = {'gold': 'c_messing', 'stern': 'c_messing',
            'technik': 'c_andesit', 'magie': 'a_quelle', 'natur': 'e_sieb'}   # Themen-Kisten (0.10.0)
KISTE_AUSNAHMEN = {'j_wither', 'j_drache', 't_drache',
                   'a_erzmagier', 'p_essenzen', 'p_trophaeen'}   # Aufgabe selbst verlangt Netherstern, Insanium bzw. Drachenei

def pruefe(alle, ahnen):
    """alle: {schlüssel: Q}, ahnen(k) -> Menge aller Voraussetzungen. Gibt Fehlerliste zurück."""
    fehler = []
    for k, q in alle.items():
        for r in q.rewards:
            if r[0] == 'table':
                gate = KISTE_AB.get(r[1])
                if gate and k not in KISTE_AUSNAHMEN and gate != k and gate not in ahnen(k):
                    fehler.append(f'{k}: {r[1]}-Kiste erst ab {gate}')
                continue
            if r[0] != 'give': continue
            i = r[1]
            if any(re.match(p, i) for p in VERBOTEN): fehler.append(f'{k}: Belohnung {i} ist gesperrt (sperren.VERBOTEN)')
            gate = AB.get(i)
            if gate and gate != k and gate not in ahnen(k):
                fehler.append(f'{k}: Belohnung {i} erst ab {gate} erlaubt (überspringt eine Stufe)')
    return fehler
```

## Datei: _src/belohnungen.py
```py
"""Quest-Belohnungen (0.8.0, Entwurf Gemini, geprüft vom Generator: Sperrliste _src/sperren.py, Item-IDs).
('item', id, anzahl) · ('kiste', stufe) = Kiste zum Öffnen · ('wahl', stufe) = ein Item aus der Kiste aussuchen. Keine XP."""
BELOHNUNGEN = {
    'w_start': [('kiste', 'holz'), ('item', 'exdeorum:silkworm', 1)],
    'e_holz': [('item', 'minecraft:oak_sapling', 2)],
    'e_raupe': [('item', 'minecraft:dirt', 4)],
    'e_fass': [('item', 'minecraft:dirt', 4)],
    'e_cobble': [('item', 'minecraft:stick', 4)],
    'e_hammer': [('item', 'minecraft:gravel', 8)],
    'e_sieb': [('kiste', 'holz'), ('item', 'minecraft:clay_ball', 4)],
    'e_tiegel': [('item', 'minecraft:oak_sapling', 4)],
    'e_lavatiegel': [('item', 'minecraft:cobblestone', 16)],
    'e_brocken': [('item', 'minecraft:flint', 2)],
    'e_feuernetz': [('item', 'minecraft:iron_nugget', 4)],
    'e_eisen': [('wahl', 'eisen')],
    'm_inferium': [('item', 'minecraft:bone_meal', 8)],
    'm_prudentium': [('item', 'mysticalagriculture:prosperity_shard', 8), ('item', 'mysticalagriculture:inferium_essence', 16)],
    'm_altar': [('item', 'mysticalagriculture:prosperity_shard', 16)],
    'e_kupfer': [('item', 'minecraft:iron_nugget', 8)],
    'c_andesit': [('item', 'create:shaft', 4)],
    'c_rad': [('item', 'create:cogwheel', 2)],
    'c_muehle': [('item', 'create:large_cogwheel', 2)],
    'c_sifter': [('kiste', 'eisen'), ('item', 'create:andesite_casing', 2)],
    'c_extruder': [('item', 'create:cogwheel', 4)],
    'c_presse': [('item', 'create:iron_sheet', 4)],
    'c_fan': [('item', 'minecraft:redstone', 8)],
    'c_mixer': [('item', 'minecraft:copper_ingot', 8)],
    'c_brenner': [('item', 'minecraft:coal', 8)],
    'c_messing': [('wahl', 'gold')],
    'c_siebfabrik': [('wahl', 'gold')],
    'c_mechanismus': [('item', 'create:brass_ingot', 4)],
    'c_alternator': [('item', 'minecraft:redstone', 16)],
    'k_osmium': [('item', 'minecraft:redstone', 16)],
    'k_infuser': [('item', 'minecraft:iron_ingot', 8)],
    'k_alloy': [('item', 'mekanism:ingot_osmium', 4)],
    'k_schalt': [('item', 'minecraft:redstone', 16)],
    'k_enrich': [('item', 'minecraft:iron_ingot', 8)],
    'k_purif': [('item', 'mekanism:fluorite_gem', 4)],
    'm_tertium': [('item', 'mysticalagriculture:prudentium_essence', 16)],
    'm_eisen': [('kiste', 'gold'), ('item', 'mysticalagriculture:prosperity_shard', 16)],
    'j_obsidian': [('item', 'minecraft:flint', 2)],
    'j_nether': [('item', 'minecraft:gold_ingot', 4)],
    'j_festung': [('item', 'minecraft:blaze_powder', 2)],
    'j_lohe': [('item', 'minecraft:nether_wart', 4), ('item', 'minecraft:soul_sand', 4)],
    'k_jetpack': [('kiste', 'gold'), ('item', 'sophisticatedbackpacks:backpack', 1)],
    'l_certus': [('item', 'ae2:certus_quartz_crystal', 4), ('item', 'ae2:silicon', 8)],
    'l_lader': [('item', 'ae2:certus_quartz_crystal', 8), ('item', 'minecraft:redstone', 16)],
    'l_inscriber': [('kiste', 'gold')],
    'l_prozessoren': [('item', 'ae2:fluix_crystal', 8), ('item', 'minecraft:redstone', 16)],
    'l_netz': [('item', 'ae2:fluix_crystal', 16), ('item', 'ae2:silicon', 16)],
    'k_inject': [('wahl', 'gold')],
    'l_auto': [('wahl', 'gold')],
    'm_imperium': [('item', 'mysticalagriculture:imperium_essence', 2), ('item', 'mysticalagriculture:prosperity_shard', 8)],
    'm_supremium': [('item', 'mysticalagriculture:supremium_essence', 1), ('item', 'mysticalagriculture:prosperity_shard', 16)],
    'm_niemehr': [('kiste', 'gold'), ('item', 'mysticalagriculture:supremium_essence', 1)],
    'j_hexe': [('item', 'minecraft:soul_sand', 8), ('item', 'minecraft:blaze_powder', 4)],
    'j_wither': [('kiste', 'stern'), ('item', 'minecraft:netherite_scrap', 2)],
    'j_perlen': [('item', 'minecraft:blaze_powder', 4), ('item', 'minecraft:gold_ingot', 4)],
    'j_augen': [('item', 'minecraft:obsidian', 8), ('item', 'minecraft:end_stone', 4)],
    'j_rahmen': [('item', 'minecraft:ender_pearl', 4), ('item', 'minecraft:end_stone', 8)],
    'j_end': [('item', 'minecraft:end_stone', 16), ('item', 'minecraft:experience_bottle', 4)],
    'j_drache': [('kiste', 'stern'), ('item', 'minecraft:golden_apple', 2)],
    'z_elite': [('item', 'minecraft:redstone', 16), ('item', 'minecraft:diamond', 2)],
    'z_ultkreis': [('item', 'mekanism:basic_control_circuit', 4), ('item', 'minecraft:diamond', 4)],
    'm_insanium': [('item', 'mysticalagriculture:supremium_essence', 4), ('item', 'mysticalagriculture:prosperity_shard', 32)],
    'k_spalt': [('item', 'minecraft:redstone', 32), ('item', 'mekanism:fluorite_gem', 16)],
    'k_polonium': [('item', 'mekanism:basic_control_circuit', 8), ('item', 'minecraft:diamond', 8)],
    'z_sps': [('wahl', 'stern')],
    'z_fabrik': [('kiste', 'stern'), ('item', 'minecraft:netherite_scrap', 4)],
    'z_weg': [('item', 'minecraft:experience_bottle', 8), ('item', 'minecraft:golden_apple', 1)],
    'z_erz': [('kiste', 'stern')],
    'z_herr': [('wahl', 'stern')],
    'e_haken': [('item', 'minecraft:oak_sapling', 2)],
    'e_eisennetz': [('item', 'minecraft:iron_ingot', 4), ('item', 'minecraft:gravel', 16)],
    'e_kanne': [('item', 'minecraft:bone_meal', 8), ('item', 'minecraft:dirt', 8)],
    's_mechsieb': [('kiste', 'eisen')],
    's_mechhammer': [('item', 'minecraft:cobblestone', 32), ('item', 'minecraft:gravel', 16)],
    'e_samen': [('item', 'minecraft:bone_meal', 4), ('item', 'minecraft:dirt', 4)],
    'g_feld': [('item', 'minecraft:wheat_seeds', 8), ('item', 'minecraft:bone_meal', 8)],
    'g_topf': [('item', 'minecraft:baked_potato', 8), ('item', 'minecraft:cooked_beef', 8)],
    'g_tiere': [('item', 'minecraft:wheat_seeds', 16), ('item', 'minecraft:bone_meal', 8)],
    'g_topf_pflanze': [('item', 'botanypots:terracotta_botany_pot', 1)],
    'g_baumtopf': [('item', 'minecraft:oak_sapling', 4), ('item', 'minecraft:bone_meal', 8)],
    'g_festessen': [('kiste', 'eisen'), ('item', 'minecraft:golden_apple', 1)],
    'g_inferium': [('item', 'mysticalagriculture:inferium_essence', 8), ('item', 'mysticalagriculture:prosperity_shard', 4)],
    'g_autark': [('kiste', 'eisen')],
    'c_deployer': [('item', 'create:andesite_alloy', 8), ('item', 'create:shaft', 8)],
    'c_crafter': [('item', 'create:brass_ingot', 4), ('item', 'create:cogwheel', 4)],
    's_akku': [('item', 'minecraft:redstone', 16), ('item', 'minecraft:iron_ingot', 8)],
    's_orb': [('item', 'minecraft:gold_ingot', 4), ('item', 'minecraft:redstone', 16)],
    's_stahl': [('item', 'minecraft:iron_ingot', 8), ('item', 'minecraft:redstone', 16)],
    's_furnator': [('item', 'minecraft:coal', 16)],
    's_solar': [('item', 'minecraft:lapis_lazuli', 8), ('item', 'minecraft:quartz', 8)],
    's_kristall': [('item', 'minecraft:blaze_powder', 4), ('item', 'minecraft:redstone', 16)],
    's_pipe': [('item', 'minecraft:iron_ingot', 4), ('item', 'minecraft:redstone', 8)],
    's_upgrade': [('item', 'minecraft:gold_ingot', 4), ('item', 'minecraft:redstone', 16)],
    's_reaktor': [('kiste', 'gold')],
    'z_ultimate': [('item', 'minecraft:diamond', 4), ('item', 'minecraft:emerald', 4)],
    'z_strom': [('kiste', 'gold')],
    'k_stahl': [('item', 'mekanism:ingot_osmium', 4)],
    'k_cube': [('item', 'minecraft:redstone', 16)],
    'k_separator': [('item', 'mekanism:fluorite_gem', 4)],
    'k_x5': [('kiste', 'gold')],
    'k_fortschritt': [('item', 'mekanism:alloy_infused', 4)],
    'k_meka': [('kiste', 'gold')],
    'k_tiab': [('item', 'minecraft:diamond', 2)],
    'z_meka': [('wahl', 'stern')],
    'l_rucksack': [('item', 'minecraft:chest', 2)],
    'l_fass': [('item', 'minecraft:oak_log', 16)],
    'l_schubladen': [('item', 'minecraft:iron_ingot', 4)],
    'l_controller': [('wahl', 'eisen')],
    'l_wireless': [('item', 'ae2:fluix_crystal', 4)],
    'l_appmek': [('item', 'ae2:certus_quartz_crystal', 8)],
    'l_mega': [('kiste', 'gold')],
    'm_kupfer': [('item', 'mysticalagriculture:inferium_essence', 8)],
    'm_gold': [('item', 'mysticalagriculture:prudentium_essence', 4)],
    'm_diamant': [('wahl', 'gold')],
    'm_beschleuniger': [('item', 'mysticalagriculture:prudentium_essence', 4)],
    'm_acker': [('item', 'mysticalagriculture:tertium_essence', 2)],
    'z_insanium': [('kiste', 'gold')],
    'z_netherstern': [('kiste', 'stern')],
    'a_quelle': [('item', 'ars_nouveau:source_gem', 4)],
    'a_buch': [('item', 'minecraft:lapis_lazuli', 8)],
    'a_tisch': [('item', 'ars_nouveau:source_gem', 4)],
    'a_glas': [('item', 'minecraft:glass', 16)],
    'a_archwood': [('item', 'minecraft:bone_meal', 8)],
    'a_whirli': [('item', 'minecraft:wheat_seeds', 8)],
    'a_crush': [('kiste', 'eisen')],
    'a_starbuncle': [('kiste', 'eisen')],
    'a_drygmy': [('item', 'minecraft:gold_ingot', 4)],
    'a_wilden': [('item', 'ars_nouveau:source_gem', 8)],
    'a_apparat': [('item', 'minecraft:gold_ingot', 4)],
    'a_ritual': [('item', 'minecraft:glowstone_dust', 8)],
    'a_wixie': [('item', 'minecraft:redstone', 8)],
    'a_erzmagier': [('wahl', 'gold')],
    'b_biene': [('item', 'minecraft:honeycomb', 4)],
    'b_stock': [('item', 'minecraft:oak_log', 16)],
    'b_zentri': [('item', 'minecraft:iron_ingot', 4)],
    'b_nest': [('item', 'minecraft:stone_bricks', 16)],
    'b_zucht': [('wahl', 'eisen')],
    'b_upgrade': [('item', 'minecraft:honeycomb', 8)],
    'j_shulker': [('item', 'minecraft:end_stone', 16)],
    'h_learner': [('item', 'minecraft:redstone', 8)],
    'h_modell': [('item', 'minecraft:lapis_lazuli', 8)],
    'h_sim': [('item', 'minecraft:iron_ingot', 8)],
    'h_fab': [('wahl', 'eisen')],
    'h_rahmen': [('item', 'minecraft:iron_ingot', 8)],
    'h_plastik': [('item', 'minecraft:redstone', 16)],
    'h_laser': [('wahl', 'gold')],
    'p_essenzen': [('kiste', 'gold')],
    'p_netze': [('kiste', 'eisen')],
    'p_archwood': [('kiste', 'eisen')],
    'p_trophaeen': [('kiste', 'stern')],
    'u_meissel': [('item', 'minecraft:stone_bricks', 16)],
    'u_dach': [('item', 'framedblocks:framed_cube', 8)],
    'u_moebel2': [('item', 'minecraft:lantern', 4)],
    'u_bruecke2': [('item', 'minecraft:string', 16)],
    'u_framed': [('item', 'framedblocks:framed_cube', 16)],
    'u_gadget': [('item', 'minecraft:diamond', 2)],
    'u_kopie': [('wahl', 'eisen')],
    't_chimera': [('wahl', 'gold')],
    't_speicher': [('item', 'minecraft:redstone', 32)],
    't_fabrik': [('item', 'minecraft:iron_ingot', 32)],
    't_drache': [('wahl', 'stern')],
}
```

## Datei: _src/texte_hauptstory.py
```py
"""Questtexte Hauptstory (Akt I–III), Stil siehe TEXTSTIL.md."""
KAPITEL = {
    'akt1': ('Akt I: Ein Splitter im Nichts', [
        'Vom ersten Baum bis zur Siebfabrik mit Create.',
        'Details zu jedem Schritt stehen in den Mod-Kapiteln.']),
    'akt2': ('Akt II: Die Maschinen erwachen', [
        'Strom, Mekanism, der zerbrochene Nether und das erste ME-Netz.']),
    'akt3': ('Akt III: Das Herz der Leere', [
        'Autocrafting, Erz vom Feld, Bosse, Antimaterie und das Finale.']),
}

QUESTS = {
    # ---------------- Akt I ----------------
    'w_start': ('Willkommen in der Leere', [
        'Unter dir nichts. Um dich nichts. Nur ein Splitter der alten Welt.',
        '',
        'Die &lHauptstory&r führt dich durch die großen Schritte, die &lMod-Kapitel&r erklären jede Mod genauer.',
        'Quests erledigen sich, sobald du die Items hast. Belohnungen holst du im Questbuch selbst ab: Quest anklicken und abholen.',
        '',
        '- Die &eWooden Watering Can&r lässt Setzlinge und Felder schneller wachsen: Wasser einfüllen, Rechtsklick halten.',
        '- Reife Pflanzen per Rechtsklick ernten, sie werden neu gesetzt.',
        '- In JEI zeigt R das Rezept, U wofür ein Item gebraucht wird (auch alle Siebfunde mit Chancen).',
        '- Taste ` (Gravis) halten und abbauen: ganze Bäume, Adern und Kiesflächen auf einmal.',
        '- M öffnet die Karte. Freunde holst du mit /skyblock invite <Name>.',
        '- Wer in die Leere fällt, landet wieder oben auf der Insel, verliert aber 3 Herzen.',
        '&cKeine Insel, sondern eine normale Welt?&r Neue Welt anlegen und unter „Welt“ → „Welttyp“ &lSkyblock&r wählen.']),
    'e_holz': ('Der erste Baum', [
        'Ein Baum ist alles, was die Erbauer dir gelassen haben.',
        '',
        'Fäll den Baum und sammle 8 Holzstämme.',
        'Tipp: Pflanz die Setzlinge sofort wieder, sonst ist dein einziger Baum weg.']),
    'e_raupe': ('Seidenraupe und Faden', [
        'Aus Laub wird Seide, aus Seide wird dein erstes Netz.',
        '',
        'Setz die &eSilkworm&r aus der Start-Quest auf Laub. Es wird langsam zu Spinnweben, die beim Abbauen zu Faden zerfallen.',
        'Mit dem Haken findest du im Laub weitere Seidenraupen. Den Faden brauchst du für das erste Siebnetz.']),
    'e_fass': ('Kompostfass', [
        'Aus Abfall wird Boden. So wächst deine Insel.',
        '',
        'Bau ein Holzfass (z. B. &eOak Barrel&r) und wirf Laub, Setzlinge oder Essen hinein. Nach einer Weile wird daraus Erde.',
        'Tipp: Fässer sammeln bei Regen auch Wasser.']),
    'e_cobble': ('Stein aus dem Nichts', [
        'Wo Lava auf Wasser trifft, entsteht Stein. Unendlich viel.',
        '',
        'Platzier Lava und Wasser so, dass sie neben einem freien Block zusammenfließen. Bau 32 &eBruchstein&r ab.',
        'Tipp: Mit dem Eis aus dem Startinventar baust du eine unendliche Wasserquelle (2×2-Becken).']),
    'e_hammer': ('Hammerzeit', [
        'Stein ist nur Kies, der noch nicht zerschlagen wurde.',
        '',
        'Bau einen &eStone Hammer&r. Hämmer zerschlagen Blöcke: Bruchstein → Kies → Sand → Staub.',
        'Später übernimmt das der Create-Mahlstein.']),
    'e_sieb': ('Das erste Sieb', [
        'Was die Leere verschluckt hat, gibt das Sieb zurück.',
        '',
        'Stell ein Sieb auf (z. B. &eOak Sieve&r), setz ein &eString Mesh&r ein und leg Erde, Kies oder Sand darauf. Dann Rechtsklick halten.',
        'Tipp: Bis zu 5×5 Siebe nebeneinander siebst du mit einem Klick gleichzeitig.']),
    'e_tiegel': ('Wasser aus Blättern', [
        'Auch Laub trägt noch Wasser in sich.',
        '',
        'Bau einen Holztiegel (z. B. &eOak Crucible&r) und füll ihn mit Laub oder Setzlingen. Er schmilzt sie zu Wasser.',
        'Fürs Erste ist das deine zweite Wasserquelle.']),
    'e_lavatiegel': ('Feuer aus Stein', [
        'Stein erinnert sich an das Feuer, aus dem er kam.',
        '',
        'Der &ePorcelain Crucible&r schmilzt Bruchstein zu Lava, wenn darunter eine Hitzequelle steht (Fackel, Lava, Feuer).',
        'Damit musst du nie wieder um deinen Lavaeimer fürchten.']),
    'e_brocken': ('Erz im Kies', [
        'Im Kies liegen Splitter der alten Minen.',
        '',
        'Schon das String Mesh gibt aus Kies Eisen- (10 %) und Kupferbrocken (8 %). Sammle 4 &eIron Ore Chunk&r.',
        '4 Brocken ergeben 1 Erz zum Schmelzen.',
        'Tipp: Das Flint Mesh bringt etwas mehr und dazu Andesit-Kiesel für Create.']),
    'e_feuernetz': ('Ein besseres Netz', [
        'Feinere Maschen, reichere Funde.',
        '',
        'Bau ein &eFlint Mesh&r und setz es statt des Fadennetzes ins Sieb.',
        'Tipp: Netze lassen sich mit Effizienz und Glück verzaubern.']),
    'e_eisen': ('Der Funke', [
        'Metall aus dem Nichts. Die Erbauer nannten es den Funken.',
        '',
        'Schmilz Erz aus deinen Brocken zu 4 &eEisenbarren&r.',
        'Damit öffnen sich Create, Mystical Agriculture und bessere Werkzeuge.']),
    'm_altar': ('Der Infusionsaltar', [
        'Hier verbanden die Erbauer Erde und Essenz.',
        '',
        'Stell den &eInfusionsaltar&r in die Mitte und 8 &eInfusionssockel&r drumherum. Hier entstehen Samen.']),
    'm_inferium': ('Samen der Essenz', [
        'Was du bisher gesiebt hast, wächst jetzt auf dem Feld.',
        '',
        'Stell am Infusionsaltar die ersten Inferium-Samen her. Sie lassen Inferiumessenz wachsen.',
        'Von nun an wird Essenz geerntet statt gesiebt.']),
    'm_prudentium': ('Stufe 2: Prudentium', [
        'Jede Stufe Essenz ist dichter als die letzte.',
        '',
        '4 Inferiumessenz ergeben 1 Prudentium. Sammle 16 &ePrudentiumessenz&r.']),
    'e_kupfer': ('Kupfer und Zink', [
        'Zwei Metalle, ohne die keine Maschine läuft.',
        '',
        'Kupfer- und Zinkbrocken kommen auch aus dem Kies, Zink ist selten (etwa 4 %). Schmilz 4 &eKupferbarren&r und 1 &eZinkbarren&r.',
        'Ein Zinkbarren reicht für den Anfang. Den Rest siebt später der Create-Sifter mit dem Eisennetz.']),
    'c_andesit': ('Andesitlegierung', [
        'Der Grundstoff, aus dem fast alles in Create gebaut ist.',
        '',
        'Andesit + Zink- oder Eisennuggets ergeben &eAndesitlegierung&r. Stell 16 her.',
        'Tipp: Andesit-Kiesel kommen aus dem Sieb. U auf Andesit in JEI zeigt alle Wege.']),
    'c_rad': ('Die erste Kraft', [
        'Die Insel hat jetzt einen Puls: Drehkraft.',
        '',
        'Bau ein &eWasserrad&r und stell es in fließendes Wasser. Das ist deine erste Kraftquelle.',
        'Alternativ: eine Windmühle mit Segeln.']),
    'c_muehle': ('Mühlstein statt Hammer', [
        'Was du mit dem Hammer zerschlagen hast, mahlt jetzt die Mühle.',
        '',
        'Der &eMahlstein&r macht alles, was der Hammer konnte: Bruchstein → Kies → Sand → Staub.',
        'Setz einen Trichter oben drauf, dann läuft das Mahlen von allein.']),
    'c_sifter': ('Sieben ohne Hände', [
        'Das Sieb arbeitet weiter, auch wenn du schläfst.',
        '',
        'Der &eSifter&r siebt mit denselben Tabellen wie das Handsieb, nur ohne dich. Bau dazu ein String Mesh und ein Andesite Mesh.',
        'Netze: String → Faden, Andesite → Feuerstein, Zinc → Eisen, Brass → Gold.']),
    'c_extruder': ('Der Extruder', [
        'Stein, der aus dem Nichts nachwächst.',
        '',
        'Der &eMechanical Extruder&r erzeugt Bruchstein (oder Basalt, Stein …) aus Lava und Wasser daneben.',
        'Zusammen mit Mahlstein und Sifter wird daraus eine Siebfabrik ohne Handarbeit.']),
    'c_presse': ('Die Presse', [
        'Aus Barren werden Bleche, aus Blechen Maschinen.',
        '',
        'Bau eine &eMechanische Presse&r. Sie presst Bleche, die du für viele Bauteile brauchst.']),
    'c_fan': ('Waschen mit Wind', [
        'Wind und Wasser holen mehr aus jedem Erz.',
        '',
        'Ein &eUmmantelter Lüfter&r, der durch Wasser bläst, wäscht zerkleinerte Erze. Das gibt mehr Nuggets.']),
    'c_mixer': ('Mixer und Becken', [
        'Hier verschmelzen Metalle zu neuen Legierungen.',
        '',
        'Stell einen Mixer (&eMechanischer Mixer&r) über ein &eBecken&r. Zusammen mischen sie Legierungen und Flüssigkeiten.']),
    'c_brenner': ('Feuer ohne Nether', [
        'Der Nether ist fern. Sein Feuer holst du dir trotzdem.',
        '',
        '1. &eLeerer Lohenbrenner&r: 4 Eisenbleche (Presse) um 1 Netherrack.',
        '2. Leerer Brenner + 4 Lohenstaub (aus Staub gesiebt) = &eLohenbrenner&r. Mit Kohle oder Holz gefüttert heizt er dein Becken.',
        '&lNetherrack ohne Nether:&r Mycelium Spores (Erde sieben) auf Erde ergeben Myzel. Ein Wasserfass auf Myzel wird nach gut einer Minute zu Hexenwasser.',
        'Hexenwasser im Fass + Lava ergibt Netherrack (U auf Netherrack in JEI). Auf der Pilzinsel hast du Myzel schon.']),
    'c_messing': ('Messing', [
        'Gold für Arme, aber Create liebt es.',
        '',
        'Gib Kupfer und Zink in den Mixer. Das Becken muss beheizt sein: Darunter gehört ein Lohenbrenner.',
        'Stell 16 &eMessingbarren&r her.']),
    'c_siebfabrik': ('Die erste Maschine', [
        'Die Maschinen der Erbauer arbeiteten Tag und Nacht. Deine jetzt auch.',
        '',
        'Verbinde Extruder → Mahlstein → Sifter → Waschen → Ofen mit Förderbändern.',
        'Wenn 32 &eEisenbarren&r, 16 Zinkbarren und 32 Kupferbarren von allein kommen, ist Akt I abgeschlossen.']),

    # ---------------- Akt II ----------------
    'c_mechanismus': ('Präzisionsarbeit', [
        'Die Erbauer bauten nichts von Hand, was ein Fließband bauen konnte.',
        '',
        'Das &ePräzisionsgetriebe&r entsteht am Fließband mit Einsatzgerät und Presse.',
        'Das ist dein erster Weg über „Sequenced Assembly“. JEI zeigt die einzelnen Schritte.']),
    'c_alternator': ('Funken aus Drehung', [
        'Drehkraft wird zu Strom. Die alten Leitungen erwachen.',
        '',
        'Der &eAlternator&r (Create Crafts & Additions) macht aus Drehkraft Strom (FE).',
        'Mit der &eKupfersuple&r verbindest du ihn mit Akkus und Maschinen.']),
    'k_osmium': ('Osmium', [
        'Ein schweres, blaues Metall. Mekanism ist darauf gebaut.',
        '',
        'Osmiumbrocken findest du im Kies mit dem Iron Mesh. Schmilz 8 &eOsmiumbarren&r.']),
    'k_infuser': ('Die Infusionsanlage', [
        'Die wichtigste Maschine von Mekanism.',
        '',
        'Bau eine &eMetallurgische Infusionsanlage&r. Sie macht Legierungen, Stahl und Schaltkreise.']),
    'k_alloy': ('Infundierte Legierung', [
        'Eisen, durchtränkt mit Redstone.',
        '',
        'Infundier Eisen mit Redstone zu 8 &eInfundierte Legierung&r.',
        'Tipp: Du brauchst sie auch für Imperiumessenz (Mystical Agriculture).']),
    'k_schalt': ('Grundschaltkreis', [
        'Ohne Schaltkreis bleibt jede Maschine stumm.',
        '',
        'Osmium + Redstone in der Infusionsanlage: Stell 4 &eEinfacher Steuerschaltkreis&r her.',
        'Er steckt in fast jeder Maschine.']),
    'k_enrich': ('×2: Anreicherung', [
        'Ein Erz, zwei Barren. Der erste Schritt zu mehr.',
        '',
        'Bau eine &eAnreicherungskammer&r. Sie macht aus einem Erz zwei Staub.']),
    'k_purif': ('×3: Reinigung', [
        'Sauerstoff wäscht noch mehr Metall aus dem Gestein.',
        '',
        'Bau eine &eKlärkammer&r. Mit Sauerstoff aus dem Elektrolyseur bekommst du drei Barren pro Erz.']),
    'm_tertium': ('Stufe 3: Tertium', [
        'Hier treffen Maschine und Essenz zum ersten Mal aufeinander.',
        '',
        '4 Prudentium + 1 Messingbarren im Create-Mixer ergeben 2 &eTertiumessenz&r. Sammle 16.',
        'Nur so kommst du an Stufe-3-Samen.']),
    'm_eisen': ('Eisen vom Feld', [
        'Hier endet das Sieben. Eisen wächst.',
        '',
        'Stell Eisen-Samen her. Sie sind Stufe 3 und brauchen Tertiumessenz aus dem Create-Mixer.']),
    'j_obsidian': ('Obsidian', [
        'Das Tor in die Unterwelt beginnt mit schwarzem Stein.',
        '',
        'Gieß Wasser auf eine Lava-Quelle und bau 10 &eObsidian&r ab.',
        '&cVorsicht beim Abbauen über der Leere.&r']),
    'j_nether': ('Die zerbrochene Unterwelt', [
        'Auch die Unterwelt zerbrach. Nur die Festungen hängen noch in der Luft.',
        '',
        'Bau ein Netherportal aus Obsidian und betritt den Nether.',
        'Er ist leer bis auf die Netherfestungen, die frei in der Luft liegen.']),
    'j_festung': ('Die Festung', [
        'Alte Mauern über dem Nichts. Hier lebt noch etwas.',
        '',
        'Finde eine Netherfestung und bau 16 &eNetherziegel&r ab.',
        'Dort spawnen Lohen und Wither-Skelette.']),
    'j_lohe': ('Lohenruten', [
        'Gefangenes Feuer, das man in der Hand tragen kann.',
        '',
        'Besieg Lohen in der Festung und sammle 8 &eLohenrute&r.',
        'Du brauchst sie für Brauen, Lohenbrenner (Create) und Enderaugen.']),
    'k_jetpack': ('Über der Leere', [
        'Zum ersten Mal trägt dich nichts als deine eigene Maschine.',
        '',
        'Bau ein &eJetpack&r (Iron Jetpacks) aus Triebwerken, Kondensator und den übrigen Teilen (Rezept in JEI) und lade es mit Strom.',
        'Tipp: Prüf vorher lieber noch einmal deinen Fallschutz.']),
    'l_certus': ('Certus-Quarz', [
        'Kristalle, die Wissen speichern können.',
        '',
        'Siebe Sand mit dem Iron Mesh. Sammle 16 &eCertusquarzkristall&r.']),
    'l_lader': ('Lader und Fluix', [
        'Strom im Kristall, Kristall im Wasser.',
        '',
        'Das &eLadegerät&r lädt Certus mit Strom auf.',
        'Wirf geladenen Certus + Redstone + Quarz ins Wasser. Daraus wird &eFluixkristall&r. Sammle 8.']),
    'l_inscriber': ('Prägeplatten ohne Meteor', [
        'In der Leere fallen keine Meteoriten. Die Platten machst du selbst.',
        '',
        'Bau eine &eGravurmaschine&r. Die vier Prägeplatten stellst du aus Certus-Quarz-Essenz her.',
        'Beispiel: 8 Essenz um einen Goldbarren = Logik-Platte, 8 Essenz um Silizium = Silizium-Platte. Die anderen zwei zeigt JEI (U auf die Essenz).',
        'Certus-Samen sind Stufe 3 (Tertium). Danach frei: Supremiumessenz und Pipez-Ultimate.']),
    'l_prozessoren': ('Prozessoren', [
        'Die Gedanken des Netzes entstehen hier.',
        '',
        'Präg je 4 &eLogikprozessor&r, &eKalkulationsprozessor&r und &eKonstruktionsprozessor&r in der Gravurmaschine.',
        'Tipp: Füttere die Gravurmaschine mit Pipez, sonst wird es mühsam.']),
    'l_netz': ('Das ME-Netz', [
        'Alles, was du besitzt, an einem Ort.',
        '',
        'Bau &eME-Controller&r, ME-Laufwerk, eine 4k-ME-Speicherzelle und eine ME-Konsole und verbinde sie.']),
    'k_inject': ('Vierfach-Erz', [
        'Aus jedem Brocken das Vierfache. So reich waren die Erbauer, und so gierig.',
        '',
        'Die &eChemische Injektionskammer&r macht vier Barren pro Erz.',
        'Sie braucht Chlorwasserstoff aus Salz (Verdampfung) und Wasserstoff. Damit ist Erz nie wieder knapp.']),

    # ---------------- Akt III ----------------
    'l_auto': ('Das Netz denkt mit', [
        'Die Netze der Erbauer dachten mit. Am Ende schneller als sie.',
        '',
        'Autocrafting: Bau einen &eME Schablonen-Provider&r, einen Molekularassembler und eine Fertigungseinheit für die Crafting-CPU.',
        'Danach bestellst du Dinge, statt sie zu bauen.']),
    'm_imperium': ('Stufe 4: Imperium', [
        'Essenz, gebunden an Metall aus der Maschine.',
        '',
        'Leg 4 Tertium im Kreuz um eine Infundierte Legierung (Mekanism). Sammle 16 &eImperiumessenz&r.']),
    'm_supremium': ('Stufe 5: Supremium', [
        'Fast so rein wie das, was unter der Welt schläft.',
        '',
        'Leg 4 Imperium im Kreuz um einen Konstruktionsprozessor (AE2). Sammle 8 &eSupremiumessenz&r.']),
    'm_niemehr': ('Felder aus Erz', [
        'Die Felder wuchsen Erz, als die Minen versiegt waren.',
        '',
        'Stell Osmium-, Certus- und Zink-Samen her. Dann wächst alles, was du bisher gesiebt hast.',
        'Dein Sieb darf in Rente gehen.']),
    'j_hexe': ('Hexenwasser-Trick', [
        'Was im Hexenwasser läuft, kommt dunkler wieder heraus.',
        '',
        'Skelette, die durch Hexenwasser (Ex Deorum) laufen, werden zu Wither-Skeletten.',
        'Sammle 3 &eWither-Skelettschädel&r für den Wither.']),
    'j_wither': ('Der Wither', [
        'Manche Dinge baut man besser weit weg von zu Hause.',
        '',
        'Beschwör den Wither und besieg ihn für einen &eNetherstern&r.',
        '&cBau ihn weit weg von deiner Insel. Sehr weit.&r']),
    'j_perlen': ('Enderperlen', [
        'Die Endermen kommen auch in die Leere.',
        '',
        'Endermen spawnen nachts auf dunklen Plattformen. Alternativ siebst du Staub.',
        'Sammle 12 &eEnderperle&r.']),
    'j_augen': ('Enderaugen', [
        'Augen, die den Weg ans Ende kennen.',
        '',
        'Stell 12 &eEnderauge&r aus Enderperlen und Lohenstaub her.']),
    'j_rahmen': ('Portalrahmen', [
        'Ohne Festungen in der Leere baust du das Tor selbst.',
        '',
        'Stell 12 &eEndportalrahmen&r aus Obsidian, Enderauge und Endstein her.']),
    'j_end': ('Das End', [
        'Das letzte Tor steht offen.',
        '',
        'Bau die Endportalrahmen zum Portal zusammen, setz die Enderaugen ein und betritt das End.']),
    'j_drache': ('Der Wächter am Ende', [
        'Der Drache bewachte das Ende. Nicht für die Erbauer, sondern vor ihnen.',
        '',
        'Die End-Hauptinsel ist da, mit Türmen und Kristallen. Besieg den Enderdrachen.',
        'Viel Glück.']),
    'z_elite': ('Elite-Schaltkreis', [
        'Feinere Schaltkreise für größere Maschinen.',
        '',
        'Stell 4 &eElitärer Steuerschaltkreis&r her. Das Rezept zeigt JEI (R).']),
    'z_ultkreis': ('Ultimate-Schaltkreis', [
        'Der feinste Schaltkreis, den Mekanism kennt.',
        '',
        'Aus Elite-Schaltkreisen + &eAtomlegierung&r stellst du 2 Ultimativer Steuerschaltkreis her.',
        'Du brauchst ihn für Insanium Essence und die ewige Fabrik.']),
    'm_insanium': ('Stufe 6: Insanium', [
        'Die höchste Stufe. Mehr gibt der Boden nicht her.',
        '',
        '4 Supremium + 1 Ultimativer Steuerschaltkreis (Mekanism) = 2 &eInsanium Essence&r. Sammle 4.',
        'Den Schaltkreis baust du aus Elite-Schaltkreisen und Atomlegierung. Weiter geht es im Kapitel „Das Herz der Leere“.']),
    'k_spalt': ('Spaltreaktor', [
        'Die Erbauer spalteten Atome. Respekt ist angebracht.',
        '',
        'Mekanism Generators: Ein Spaltreaktor aus &eKernreaktorgehäuse&r und &eKernbrennstoffbaugruppe&r macht aus Uran viel Strom und Atommüll, den du gleich brauchst.',
        'Uran: Uranbrocken aus zerkleinertem Tiefenschiefer im Sieb oder Uran-Samen. Weg: Uran → Yellowcake → Uranoxid → Uranhexafluorid → Spaltbrennstoff.',
        '&cKühlung (Wasser) nicht vergessen und den Reaktor nie überhitzen lassen.&r']),
    'k_polonium': ('Polonium', [
        'Aus Müll wird der Stoff, der das Herz der Leere nährt.',
        '',
        'Atommüll aus dem Spaltreaktor wird im &eSolarneutronenaktivator&r (braucht Tageslicht) zu Polonium.',
        'Das &ePolonium Pellet&r ist die Zutat für Antimaterie im SPS.']),
    'z_sps': ('Der Herzschlag', [
        'Antimaterie: der Herzschlag der Leere in einer Kapsel.',
        '',
        'Polonium-Pellets im SPS (Supercritical Phase Shifter) werden zu Antimaterie. Ein einziges &eAntimaterie Pellet&r reicht.',
        'Der SPS braucht sehr viel Strom: Spaltreaktor, Powah-Reaktor oder viele Generatoren.']),
    'z_fabrik': ('Die ewige Fabrik', [
        'Maschinen, Felder und Netz laufen endlich als ein Ganzes.',
        '',
        'Zeig 4 &eUltimativer Steuerschaltkreis&r aus Mekanism, 32 Supremiumessenz vom Feld und 2 Nethersterne aus der Netherstern-Saat vor.',
        'Die Items werden nur vorgezeigt, nicht verbraucht. Wenn dein ME-Netz sie von allein nachbaut, hast du es geschafft.']),
    'z_weg': ('Maschine oder Magie', [
        'Die Erbauer brauchten beides. Dir reicht einer der Wege.',
        '',
        '&lMagie:&r das &eErzmagier-Zauberbuch&r (Ars Nouveau).',
        '&lMaschinen:&r der &eLoot Fabricator&r (Hostile Networks).',
        'Die Quest erledigt sich, sobald du eins davon hast.']),
    'z_herr': ('Das Erbe der Erbauer', [
        'Das Herz der Leere schlägt wieder ruhig. Du trägst jetzt ihr Erbe.',
        '',
        'Maschinen, Magie und Felder arbeiten zusammen. Aus einer Insel mit einem Baum ist eine Welt geworden.',
        'Letzte Aufgabe: Bring das &eDrachenei&r nach Hause.',
        'Tipp: Das Ei teleportiert sich, wenn du es schlägst. Ein Kolben schiebt es herunter.',
        'Danke fürs Spielen von Sky and Stone.']),
}

# ---------------------------------------------------------------------
# 0.7.0: Korrekturen aus den Audits (falsche Mechanik, fehlende Freischaltungen, Wahl Maschine/Magie, Erz-Wahl)
# ---------------------------------------------------------------------
KAPITEL['akt3'] = ('Akt III: Das Herz der Leere', [
    'Autocrafting, Erz vom Feld, Bosse, Antimaterie und das Finale.',
    'Fürs Finale brauchst du einen Weg: Magie (Ars Nouveau) oder Maschinen (Hostile Networks). Früh anfangen lohnt sich.'])
_q = QUESTS
_q['w_start'][1][2] = ('&lDer Weg der Erbauer&r führt dich durch die großen Schritte, das &lHandbuch der Mods&r erklärt jede Mod genauer. '
                       '&lAbseits des Weges&r liegt alles ohne Pflicht: Markt, Bauen, Sammeln.')
_q['e_holz'][1].append('Kein Baum auf deiner Insel? Pflanz die Setzlinge aus dem Startinventar auf Erde und hilf mit Knochenmehl nach.')
_q['e_raupe'] = ('Seidenraupe und Faden', [
    'Aus Laub wird Seide, aus Seide wird dein erstes Netz.',
    '',
    'Setz die &eSilkworm&r aus der Start-Quest auf Laub. Es wird nach und nach befallen und steckt Nachbarlaub an.',
    'Voll befallenes Laub mit dem &eCrook&r abbauen: etwa jedes zweite gibt Faden. Mit der Hand gibt es nichts.',
    'Tipp: Pflanz vorher einen zweiten Baum, damit dir das Laub nicht ausgeht.'])
_q['e_eisen'][1][3] = 'Freigeschaltet: Kupfer und Zink für Create, das &eIron Mesh&r und der Einstieg in Mystical Agriculture.'
_q['e_eisen'][1].append('Tipp: Abseits des Weges warten jetzt der Inselmarkt und der Baumeister.')
_q['e_kupfer'][1][3] = 'Ein Zinkbarren reicht für den Anfang. Den Rest siebt später der Create-Sifter mit dem &eZinc Mesh&r.'
_q['m_inferium'] = ('Samen der Essenz', [
    'Was du bisher gesiebt hast, wächst jetzt auf dem Feld.',
    '',
    'An der Werkbank: 8 &eInferiumessenz&r um einen Weizensamen ergeben Inferium-Samen. Pflanz sie auf Ackerboden.',
    'Von nun an wird Essenz geerntet statt gesiebt. Den Infusionsaltar brauchst du erst später.'])
_q['m_prudentium'] = ('Stufe 2: Prudentium', [
    'Jede Stufe Essenz ist dichter als die letzte.',
    '',
    '4 Inferiumessenz um einen &eInfusionskristall&r ergeben 1 Prudentium. Der Kristall bleibt erhalten.',
    'Kristall: 1 Diamant, 4 Prosperiumsplitter (Kies mit Flint Mesh) und 4 Inferiumessenz. Sammle 16 &ePrudentiumessenz&r.'])
_q['m_altar'] = ('Der Infusionsaltar', [
    'Hier verbanden die Erbauer Erde und Essenz.',
    '',
    'Stell den &eInfusionsaltar&r in die Mitte und 8 &eInfusionssockel&r drumherum. Zusammen kosten sie 18 Goldbarren.',
    'Gebraucht wird er für alle Samen außer Inferium, also ab Stufe 2 (z. B. Kohle). Gold sammelt sich nebenbei beim Sieben.'])
_q['c_sifter'][1][3] = 'Netze: String → Faden, Andesite → Feuerstein, Zinc → Eisen (Stöcke um einen Zinkbarren), Brass → Gold.'
_q['c_presse'][1].append('Tipp: Die Presse braucht einen ganzen Eisenblock. Lass vorher den Sifter laufen, dann kommt das Eisen von allein.')
_q['c_messing'][1].append('Freigeschaltet: Akt II, die Tertiumessenz und die Gold-Tausche im Inselmarkt.')
_q['c_siebfabrik'][1][3] = 'Wenn 32 &eEisenbarren&r, 16 Zinkbarren und 32 Kupferbarren von allein kommen, steht deine Fabrik.'
_q['c_siebfabrik'][1].append('Akt II ist schon seit dem Messing offen. Die Fabrik liefert das Metall dafür.')
_q['k_inject'][1].append('Weiter in Akt III: Elite-Schaltkreise, Autocrafting und die Wahl deines Weges.')
_q['m_insanium'][1][3] = ('Den Schaltkreis baust du aus Elite-Schaltkreisen und Atomlegierung. '
                          'Weiter geht es im Kapitel Mystical Agriculture: Insanium-Ernte und Sterne vom Feld.')
_q['z_weg'][1][0] = 'Zwei Wege führen zum Herz. Du musst nur einen gehen.'
_q['z_herr'][1][2] = 'Maschinen, Felder und dein gewählter Weg arbeiten zusammen. Aus einer Insel mit einem Baum ist eine Welt geworden.'
_q['z_erz'] = ('Erz ohne Sieb', [
    'Das Sieb hat dich weit getragen. Jetzt soll das Erz von selbst kommen.',
    '',
    'Wähl einen Weg, einer reicht:',
    '- &lFelder:&r Osmium-Samen (Mystical Agriculture)',
    '- &lLaser:&r die &eErz-Laserbasis&r (Industrial Foregoing)',
    '- &lBienen:&r ein &eQuartz Nest&r für Erz-Bienen (Productive Bees)'])

# 0.9.0: XP hat einen Zweck (Wegsteine kosten Erfahrung), Hinweise am Item
_q['w_start'][1].append('- Erfahrung (XP) brauchst du für Reisen mit Wegsteinen und für Verzauberungen. Wichtige Items erklären sich im Tooltip und in JEI (U).')

# 0.10.0: Koop und Tagebuchseiten
_q['w_start'][1].append('- Mit Freunden: Im Team teilt ihr den Questfortschritt, jeder holt seine Belohnungen selbst ab.')
_q['w_start'][1].append('- Jeder Meilenstein mit einer Notiz gibt eine &dTagebuchseite&r. Sammle alle 17.')
```

## Datei: _src/texte_technik.py
```py
"""Questtexte Mod-Kapitel Technik/Natur, Stil siehe TEXTSTIL.md."""
KAPITEL = {
    'exdeorum': ('Ex Deorum: Staub und Siebe', ['Siebe, Netze, Tiegel und Gießkannen. Was die Leere nahm, holst du dir Korn für Korn zurück.']),
    'landwirtschaft': ('Felder und Küche', ['Farmer\'s Delight, Botany Pots, Nutztiere. Eine Insel, die sich selbst nährt.']),
    'create': ('Create: Zahnrad und Messing', ['Zahnräder, Mühlstein, Sifter, Messing. Die Maschinen der Erbauer drehen sich wieder.']),
    'energie': ('Strom und Rohre', ['Create Crafts & Additions, Powah, Pipez. Kraft erzeugen, speichern und verteilen.']),
    'mekanism': ('Mekanism: Die Werkhalle', ['Erzverarbeitung, Schaltkreise, Atomtechnik, Werkzeuge.']),
    'lagerung': ('Lager und Rucksack', ['Sophisticated Backpacks, Sophisticated Storage, Functional Storage. Ordnung gegen das Kistenchaos.']),
    'ae2': ('Applied Energistics 2: Das Netz', ['ME-Netz, Autocrafting, kabellos.']),
    'mysticalag': ('Mystical Agriculture: Erzfelder', [
        'Erz, das auf Feldern wächst.',
        'Stufen: Inferium → Prudentium → Tertium (Create) → Imperium (Mekanism) → Supremium (AE2) → Insanium.']),
}

QUESTS = {
    # --- Ex Deorum ---
    'e_haken': ('Mit dem Haken ins Laub', [
        'Im Laub verstecken sich mehr Setzlinge, als man denkt.',
        '',
        'Den &eCrook&r hast du schon im Startinventar. Brich damit Laub ab: Es lässt öfter Setzlinge fallen und gibt Seidenraupen.']),
    'e_eisennetz': ('Das Eisennetz', [
        'Feinere Maschen, seltenere Funde.',
        '',
        'Setz ein &eIron Mesh&r ins Sieb. Damit tauchen Osmium-, Zinn-, Blei- und Silberbrocken auf.',
        'Tipp: In der Erde steckt auch Inferiumessenz für Mystical Agriculture.']),
    'e_kanne': ('Die bessere Gießkanne', [
        'Mehr Wasser, schnellere Bäume.',
        '',
        'Bau eine &eIron Watering Can&r. Sie hält mehr Wasser und lässt Bäume schneller wachsen.']),
    's_mechsieb': ('Das Sieb mit Strom', [
        'Die Hand ermüdet. Die Maschine nicht.',
        '',
        'Das &eMechanical Sieve&r ist das Ex-Deorum-Sieb mit Strom: Netz einsetzen, Kies per Trichter hinein, den Rest erledigt es.',
        'Tipp: Es braucht nur 20 FE pro Tick.']),
    's_mechhammer': ('Hammer ohne Arm', [
        'Stein zu Kies, Kies zu Sand, ohne einen Schlag.',
        '',
        'Der &eMechanical Hammer&r zerkleinert Blöcke mit Strom.']),

    # --- Landwirtschaft ---
    'e_samen': ('Was in der Erde steckt', [
        'Die Erde der Insel ist voller vergessener Saat.',
        '',
        'Siebe Erde mit dem &eString Mesh&r. Dabei fallen Samen, Setzlinge und mehr heraus.',
        'Von hier aus geht es weiter zu Feldern, Küche und Tieren.']),
    'g_feld': ('Das erste Feld', [
        'Ein Streifen Grün über der Leere.',
        '',
        'Weizen, Karotten, Kartoffeln: Alles kommt aus dem Sieb. Leg ein Feld an und ernte &e16 Feldfrüchte&r.',
        'Tipp: Mit der Gießkanne wächst das Feld schneller.']),
    'g_topf': ('Die Küche', [
        'Wer gut isst, siebt länger.',
        '',
        'Bau ein &eSchneidebrett&r und einen &eKochtopf&r aus Farmer\'s Delight.',
        'Das Schneidebrett holt mehr aus deinen Zutaten, der Kochtopf macht Gerichte, die lange satt machen.']),
    'g_tiere': ('Nutztiere', [
        'Leben kehrt auf die Insel zurück.',
        '',
        'Spawneier für Kuh, Schaf, Huhn und Schwein findest du beim Sieben von Erde. Sammle Leder und Eier.',
        '&cZäune nicht vergessen: Um dich herum ist nur Leere.']),
    'g_topf_pflanze': ('Pflanzen im Topf', [
        'Ein Garten, der sich selbst pflegt.',
        '',
        'In einem &eBotany Pot&r wachsen Pflanzen und Bäume von allein.',
        'Tipp: Ein Trichter-Topf erntet selbst und reicht weiter. Deine erste Automatik.']),
    'g_baumtopf': ('Holz im Topf', [
        'Nie wieder Bäume fällen.',
        '',
        'Setzling und Erde in einen &eHopper Botany Pot&r: unendlich Holz ohne Axt.']),
    'g_festessen': ('Sterneküche in der Leere', [
        'Ein Festmahl, gewachsen auf einem Felsen im Nichts.',
        '',
        'Koch einen &eHirtenkuchen&r und ein &eBackhähnchen&r, beide komplett aus Inselzutaten.',
        'Damit ist Hunger kein Thema mehr.']),
    'g_inferium': ('Inferiumessenz', [
        'Ein grüner Schimmer im Siebgut. Er ist mehr als Staub.',
        '',
        'Siebe Erde mit dem String Mesh oder einem besseren Netz. Dabei fällt &eInferiumessenz&r.',
        'Damit beginnt Mystical Agriculture.']),
    'g_autark': ('Die autarke Insel', [
        '„Eine Insel, die sich selbst nährt, ist der erste Schritt zurück.“',
        '',
        'Stell vier &eHopper Botany Pots&r auf: Holz und Essen wachsen von selbst und landen in Truhen.',
        'Deine Insel versorgt sich jetzt selbst.']),

    # --- Create ---
    'c_deployer': ('Die mechanische Hand', [
        'Eine Hand aus Messing, die nie müde wird.',
        '',
        'Das &eEinsatzgerät&r klickt für dich: Blöcke setzen, Items benutzen, Gegner schlagen.']),
    'c_crafter': ('Werkbank im Großformat', [
        'Neun Einheiten, ein Rezept.',
        '',
        'Bau neun &eMechanische Handwerkseinheiten&r. Zusammen stellen sie große Rezepte automatisch her.']),

    # --- Energie ---
    's_akku': ('Strom auf Vorrat', [
        'Auch der Wind ruht manchmal.',
        '',
        'Der &eAkkumulator&r speichert Strom für windstille Zeiten.']),
    's_orb': ('Der Energizing Orb', [
        'Eine Kugel, die Metall mit Kraft tränkt.',
        '',
        '&eDielectric Paste&r aus Ton, Kohle und Lava ist die Grundzutat von Powah.',
        'Der &eEnergizing Orb&r lädt Items mit Strom auf. Die Energizing Rods drumherum liefern die Energie.']),
    's_stahl': ('Geladener Stahl', [
        'Eisen und Gold, verschmolzen durch Strom.',
        '',
        'Leg Eisen und Gold in den Orb. Heraus kommt &eEnergized Steel&r, die Basis für alle Powah-Maschinen.']),
    's_furnator': ('Feuer zu Strom', [
        'Alte Technik, ehrliche Kraft.',
        '',
        'Der &eFurnator&r verbrennt Kohle und Holz zu Strom. Solide Grundversorgung.']),
    's_solar': ('Licht über der Leere', [
        'Hier oben scheint die Sonne ungehindert.',
        '',
        'Vier &eSolar Panels&r liefern Strom ohne Brennstoff. Allerdings nur tagsüber.']),
    's_kristall': ('Glut im Kristall', [
        'Feuer, eingefangen in Stein.',
        '',
        'Lohenstaub im Orb ergibt &eBlazing Crystal&r. Lohenstaub findest du beim Sieben von Dust.']),
    's_pipe': ('Rohre verlegen', [
        'Was von selbst fließt, musst du nicht tragen.',
        '',
        'Pipez bringt Items, Flüssigkeiten und Strom von A nach B. Leg &eItem Rohre&r und &eStrom Rohre&r.',
        'Tipp: Der Schraubenschlüssel öffnet die Einstellungen am Rohrende.']),
    's_upgrade': ('Schnellere Rohre', [
        'Mehr Durchfluss, mehr Kontrolle.',
        '',
        'Die &eNormale&r und die &eVerbesserte Rohr Modifikation&r machen Rohre schneller und erlauben Filter.',
        'Die Fortgeschrittene braucht Mekanism-Schaltkreise, die Ultimative zusätzlich AE2-Prozessoren.']),
    's_reaktor': ('Netzstrom', [
        '„Wir nahmen die Kraft aus der Leere, nicht aus Kohle. Zu viel davon zerriss den Boden.“',
        '',
        'Bau einen Powah-Reaktor: 3×4×3 aus &eReactor (Basic)&r, befeuert mit Uraninite aus dem Gold-Sieb.',
        'Danach ist Strom kein Engpass mehr.']),
    'z_ultimate': ('Rohre ohne Grenzen', [
        'Das Beste aus Mekanism und AE2 in einem Rohr.',
        '',
        'Bau die &eUltimative Rohr Modifikation&r. Dafür brauchst du Elite-Schaltkreise aus Mekanism und Prozessoren aus AE2.']),
    'z_strom': ('Großkraftwerk', [
        'Genug Kraft, um Materie zu spalten.',
        '',
        'Optional: Ein großer Powah-Reaktor aus &eReactor (Hardened)&r ist der bequeme Weg zu viel Strom.',
        'Für die Antimaterie reicht auch jede andere große Stromquelle, zum Beispiel der Spaltreaktor.']),

    # --- Mekanism ---
    'k_stahl': ('Stahl', [
        'Härter als Eisen, das Rückgrat jeder Maschine.',
        '',
        'Infundiere Eisen mit Kohle in der Metallurgischen Infusionsanlage und schmelze das Ergebnis zu &eStahlbarren&r.']),
    'k_cube': ('Strom verteilen', [
        'Ein Netz aus Kupferadern für deine Werkhalle.',
        '',
        '&eEinfache Universalkabel&r tragen Strom, der &eEinfache Energie-Würfel&r speichert ihn.']),
    'k_separator': ('Elektrolyse', [
        'Aus Wasser wird Gas.',
        '',
        'Der &eElektrolyseur&r spaltet Wasser in Wasserstoff und Sauerstoff.']),
    'k_x5': ('×5: Die volle Kette', [
        'Fünf Barren aus einem Erz. Nichts geht verloren.',
        '',
        'Optional: Bau die &eChemische Auflösungskammer&r. Auflösen, Waschen, Kristallisieren ergibt fünf Barren pro Erz.',
        'Tipp: Lohnt sich nur, wenn du noch viel siebst.']),
    'k_fortschritt': ('Bessere Schaltkreise', [
        'Feinere Bahnen, klügere Maschinen.',
        '',
        'Stell vier &eFortschrittliche Steuerschaltkreise&r her.',
        'Sie schalten die Fortgeschrittene Rohr Modifikation von Pipez frei.']),
    'k_meka': ('Werkzeug der Zukunft', [
        'Ein Werkzeug für alles, was im Weg steht.',
        '',
        'Der &eAtomic Disassembler&r ist Spitzhacke, Axt und Schaufel in einem und läuft mit Strom.']),
    'k_tiab': ('Zeit ist Geld', [
        'Die Erbauer konnten die Zeit biegen. Jetzt kannst du es auch.',
        '',
        '&eTime in a Bottle&r sammelt Zeit, solange es in deinem Inventar liegt.',
        'Rechtsklick auf eine Maschine beschleunigt sie, hier bis zu 8-fach.']),
    'z_meka': ('Die MekaSuit', [
        'Eine Rüstung aus Antimaterie und Stahl.',
        '',
        'Mit Antimaterie in der Hand baust du die &eMekaSuit Brustplatte&r.']),

    # --- Lagerung ---
    'l_rucksack': ('Der Rucksack', [
        'Die Taschen sind voll, das Sieb gibt weiter.',
        '',
        'Bau einen &eRucksack&r und ein &ePickup-Upgrade&r.',
        'Mit dem Upgrade füllt sich der Rucksack automatisch mit deinen Siebfunden.']),
    'l_fass': ('Lagerfässer', [
        'Ordnung beginnt mit dem ersten Fass.',
        '',
        'Bau ein Fass aus Sophisticated Storage. Fässer und Truhen lassen sich aufrüsten und haben einen Sortierknopf.']),
    'l_schubladen': ('Schubladen', [
        'Tausend Steine, ein Block.',
        '',
        'Functional Storage: &eSchubladen&r fassen viel von einer Sorte auf kleinem Raum. Stell vier davon auf.']),
    'l_controller': ('Die Schubladen-Wand', [
        'Eine Wand, ein Eingang, kein Suchen mehr.',
        '',
        'Der &eStorage Controller&r macht alle Schubladen zu einem Lager mit einem Eingang.',
        'Tipp: Das löst das Kistenchaos, bis AE2 steht.']),

    # --- AE2 ---
    'l_wireless': ('Kabellos', [
        'Das Netz folgt dir, wohin du auch fliegst.',
        '',
        'Mit der &eDrahtlosen Universalkonsole&r hast du dein ME-Netz in der Tasche.']),
    'l_appmek': ('Gase im Netz', [
        'Auch was man nicht anfassen kann, lässt sich lagern.',
        '',
        'Applied Mekanistics: Mit der &e1k ME Chemical Storage Cell&r speichert AE2 Mekanism-Gase und -Chemikalien.']),
    'l_mega': ('Riesenspeicher', [
        'Für alle, die nichts wegwerfen.',
        '',
        'MEGA Cells fassen Millionen Bytes. Bau eine &e1M MEGA Item Storage Cell&r.']),

    # --- Mystical Agriculture ---
    'm_kupfer': ('Kupfer und Kohle', [
        'Die ersten Erze, die aus der Erde sprießen.',
        '',
        'Stell Samen für Kupfer und Kohle her. Kohle ist Stufe 2, Kupfer Stufe 3 und braucht &eTertiumessenz&r.']),
    'm_gold': ('Gold und Redstone', [
        'Gold wächst nicht für jeden.',
        '',
        'Stell Samen für Gold und Redstone her. Redstone ist Stufe 3, Gold Stufe 4.',
        'Für Gold brauchst du &eImperiumessenz&r, und die gibt es nur mit Mekanism.']),
    'm_diamant': ('Diamanten vom Feld', [
        'Edelsteine als Ernte. Die Erbauer hätten gestaunt.',
        '',
        'Diamant-Samen sind Stufe 5 und brauchen &eSupremiumessenz&r, die erst mit AE2 möglich ist.']),
    'm_beschleuniger': ('Wachstumsbeschleuniger', [
        'Was unten glüht, wächst oben schneller.',
        '',
        'Stapel &eInferium-Wachstumsbeschleuniger&r unter das Ackerland. Die Pflanzen darüber wachsen schneller.']),
    'm_acker': ('Essenz-Ackerland', [
        'Der richtige Boden für die richtige Saat.',
        '',
        'Leg &eImperium-Ackerland&r an. Passendes Ackerland gibt Samen derselben Stufe mehr Ertrag.']),
    'z_insanium': ('Insanium-Ernte', [
        'Die höchste Stufe. Sie verlangt alles, was du gebaut hast.',
        '',
        'Insanium braucht neben Supremium einen &eUltimativen Steuerschaltkreis&r aus Mekanism.',
        '4 Supremium + 1 Schaltkreis ergeben 2 &eInsanium Essence&r.',
        'Tipp: Lass AE2 die Schaltkreise automatisch bauen.']),
    'z_netherstern': ('Sterne vom Feld', [
        'Was einst nur der Wither trug, wächst jetzt im Beet.',
        '',
        'Stell Samen für Nethersterne her. Dann wachsen Nethersterne auf dem Feld.']),
}

# 0.7.0: Die Notiz „Kraft aus der Leere“ steht jetzt beim Spaltreaktor (Hauptstory), hier eine eigene Stimmungszeile
QUESTS['s_reaktor'][1][0] = 'Kristall, Uraninit und Geduld. Dann summt die Insel.'
QUESTS['g_inferium'][1][3] = 'Damit beginnt Mystical Agriculture: An der Werkbank werden daraus die ersten Samen.'
```

## Datei: _src/texte_abenteuer.py
```py
"""Questtexte Magie, Abenteuer, Extras und Story, Stil siehe TEXTSTIL.md."""
GRUPPEN = {'haupt': 'Der Weg der Erbauer', 'mods': 'Handbuch der Mods', 'extras': 'Abseits des Weges'}
KAPITEL = {
    'ars': ('Ars Nouveau', ['Magie, die dir Arbeit abnimmt: Transport, Mob-Drops, Autocrafting.']),
    'bienen': ('Productive Bees', ['Rohstoffe, die summen.']),
    'dimensionen': ('Nether und End', ['Festungen über der Leere, Wither und Drache.']),
    'maschinengeist': ('Hostile Networks und IF', ['Mobs simulieren statt jagen, Erz per Laser.']),
    'story': ('Das Herz der Leere', [
        'Die Notizen des letzten Wächters, in der Reihenfolge der Geschichte.',
        'Jede Notiz liegt in ihrem Meilenstein und wird lesbar, sobald du ihn erreichst.']),
    'markt': ('Inselmarkt', [
        'Tausch deinen Überschuss gegen Beutekisten. Die Items werden beim Abgeben verbraucht.',
        'Jeder Tausch hat eine Abklingzeit. Kisten fallen selten auch von Monstern, Bosse lassen immer eine fallen.']),
    'sammler': ('Sammlerbuch', ['Optional: Sammle alles einmal.']),
    'bau': ('Baumeister', ['Optional: schön statt nur praktisch.']),
}
QUESTS = {
    # ---------------- Ars Nouveau ----------------
    'a_quelle': ('Stein, der Quelle trägt', [
        'Im Amethyst aus dem Sieb schläft eine alte Kraft.',
        '',
        'Leg Amethyst in die &eImbuement-Kammer&r, daraus wird Quellstein.',
        'Quellstein ist der Grundstoff aller Magie in Ars Nouveau.']),
    'a_buch': ('Das erste Zauberbuch', [
        'Ein leeres Buch, das darauf wartet, beschrieben zu werden.',
        '',
        'Taste C öffnet das &eZauberbuch für Anfänger&r. Dort steckst du Zauber aus Glyphen zusammen.',
        'Tipp: Projektil + Abbauen ergibt Fernabbau.']),
    'a_tisch': ('Der Tisch des Schreibers', [
        'Die Erbauer schrieben ihre Zauber Glyphe für Glyphe.',
        '',
        'Am &eTisch des Schreibers&r lernst du neue Glyphen.']),
    'a_glas': ('Quelle aus Wurzeln', [
        'Wo etwas wächst, fließt Quelle.',
        '',
        'Der &eAgronomische Quellenlink&r erzeugt Quelle aus wachsenden Pflanzen und füllt damit ein Quellglas.',
        'Tipp: Stell ihn direkt neben deine Felder.']),
    'a_archwood': ('Archwood', [
        'Bäume, die schon vor dem Zerbrechen alt waren.',
        '',
        'Archwood-Setzlinge findest du im Moos-Sieb. Ihre Früchte sind Zutaten für Rituale.']),
    'a_whirli': ('Der Gärtnergeist', [
        'Ein kleiner Geist, der Wurzeln zum Treiben bringt.',
        '',
        'Der Whirlisprig aus dem &eWirbelzweig-Charme&r lässt Pflanzen und Bäume in seiner Nähe schneller wachsen und erzeugt dabei Quelle.',
        'Tipp: Gut neben Feldern und Botany Pots, eine Alternative zu Wachstumsbeschleunigern.']),
    'a_crush': ('Zerkleinern ohne Hammer', [
        'Was der Hammer kann, schafft auch ein Zauber.',
        '',
        'Die Glyphe Crush macht aus Bruchstein Kies, aus Kies Sand und aus Sand Staub, genau wie der Hammer.',
        'Ein &eEinfacher Zauberturm&r mit Berühren + Crush vor einem Bruchstein-Generator zerkleinert von allein, mit Redstone-Takt.',
        'Tipp: Eine Alternative zum Mahlstein (Create) oder mechanischen Hammer. Du musst nicht beides bauen.']),
    'a_starbuncle': ('Der Logistiker', [
        'Kein Rohr, kein Band. Nur kleine Pfoten.',
        '',
        'Ein Starbuncle aus dem &eSternbunkel-Charme&r trägt Items sichtbar von A nach B.',
        'Zum Beispiel Siebfunde aus der Truhe unter dem Sieb in deine Lagertruhe.',
        'Tipp: Goldnuggets machen ihn glücklich.']),
    'a_drygmy': ('Beute ohne Blut', [
        'Er nimmt, was die Tiere tragen, und lässt sie leben.',
        '',
        'Ein Drygmy aus dem &eTrockenen Charme&r holt Mob-Drops von Tieren und Monstern in der Nähe, ohne sie zu töten.']),
    'a_wilden': ('Spuren der Wilden', [
        'Die Wilden sind fort. Ihre Reste nicht.',
        '',
        'In der Leere gibt es keine Wilden. &eWilden Horn&r, Wilden Spike und Wilden-Flügel findest du im Gold-Sieb.']),
    'a_apparat': ('Der Apparat', [
        'Ein Altar, an dem Quelle zu Form wird.',
        '',
        'Stell den &eBezaubernden Apparat&r auf einen Arkanen Kern.']),
    'a_ritual': ('Das Ritualbecken', [
        'Manche Magie braucht Feuer und einen festen Ort.',
        '',
        'Im &eRitual-Kohlenbecken&r führst du Rituale aus.']),
    'a_wixie': ('Die kleine Werkstatt', [
        'Eine Wixie vergisst kein Rezept.',
        '',
        'Setz die Wixie mit ihrem &eWixie-Charme&r auf einen Kessel. Daraus wird ein Wixie-Kessel.',
        'Leg Zutaten in Truhen daneben und zeig ihr das Rezept. Sie stellt es immer wieder her.',
        'Tipp: Für einfache Dinge (Fackeln, Bleche, Legierungen) ein früher Ersatz für AE2-Autocrafting. Für große Mengen bleibt AE2 stärker.']),
    'a_erzmagier': ('Erzmagier', [
        'Das stärkste Zauberbuch. Ab hier ist Magie kein Spielzeug mehr.',
        '',
        'Werte am Schreibtisch auf: Zauberbuch des Magiers, 3 Enderperlen, 2 Smaragde, 1 Diamantblock, 1 Netherstern (Wither) und 1 &eWilden-Tribut&r.',
        'Den Tribut lässt die &lWilden-Chimera&r fallen: Ritual „Beschwöre Wilden“ im Ritualbecken, verstärkt mit Wilden Horn, Wilden Spike und Wilden-Flügel.',
        '&cAchtung: Das Chimera-Ritual zerstört Blöcke rund um das Becken. Bau es auf einer eigenen Plattform weit weg von deiner Basis.&r']),
    # ---------------- Productive Bees ----------------
    'b_biene': ('Das erste Summen', [
        'Im Moos schläft noch Leben.',
        '',
        'Ein &eBienen-Spawn-Ei&r findest du beim Sieben von Moosblöcken.']),
    'b_stock': ('Ein besserer Stock', [
        'Ein Zuhause für ein Volk, das arbeitet.',
        '',
        'Der &efortgeschrittene Bienenstock&r ist produktiver als der normale und lässt sich mit Upgrades erweitern.']),
    'b_zentri': ('Die Zentrifuge', [
        'Jede Wabe birgt mehr als Honig.',
        '',
        'Die &eCentrifuge&r zerlegt Waben in Wachs, Honig und Rohstoffe.']),
    'b_nest': ('Nester bauen', [
        'Die Leere baut keine Nester. Du schon.',
        '',
        'Stell ein Nest wie das &eStone Nest&r selbst her und auf. Passende Wildbienen ziehen ein.']),
    'b_zucht': ('Bienen aus Erz', [
        'Mit Geduld und Zucker summt bald das Metall.',
        '',
        'Mit &eHoney Treat&r und dem richtigen Block züchtest du Bienen, die Eisen, Kupfer und mehr liefern.',
        'Tipp: JEI zeigt unter „Bienenzucht“, was geht.']),
    'b_upgrade': ('Fleißige Völker', [
        'Ein Stock, der mehr gibt, als er nimmt.',
        '',
        'Stell ein Upgrade für Produktivität her und setz es in deinen Bienenstock.']),
    # ---------------- Nether und End ----------------
    'j_shulker': ('Schalen aus Endstein', [
        'Keine Endstädte, aber der Staub erinnert sich.',
        '',
        'In der Leere gibt es keine Endstädte. &eShulker-Schalen&r findest du im Diamant- oder Netherit-Sieb aus zerkleinertem Endstein.']),
    # ---------------- Hostile Networks und IF ----------------
    'h_learner': ('Der Deep Learner', [
        'Jeder Kampf lehrt etwas. Hier wird es aufgeschrieben.',
        '',
        'Hostile Neural Networks: Der &eDeep Learner&r trainiert Datenmodelle, während du kämpfst.']),
    'h_modell': ('Das erste Datenmodell', [
        'Ein leerer Rahmen wartet auf ein Gesicht.',
        '',
        'Rechtsklick mit einem &eModel Framework&r auf einen Mob bindet das Modell an seine Art.']),
    'h_sim': ('Kämpfe im Kasten', [
        'Krieg ohne Schwert, nur Strom und Rechnung.',
        '',
        'Die &eSimulation Chamber&r simuliert Kämpfe mit Strom und erzeugt Prediction Matrix-Vorhersagen.']),
    'h_fab': ('Beute-Fabrikator', [
        'Der Feind muss nicht mehr kommen. Seine Beute schon.',
        '',
        'Der &eLoot Fabricator&r macht aus Vorhersagen echte Drops: Enderperlen, Lohenruten, Knochen und mehr.',
        'Ab hier kommen deine Mob-Drops aus der Maschine.']),
    'h_rahmen': ('Der erste Rahmen', [
        'Industrial Foregoing beginnt klein und klebrig.',
        '',
        'Bau ein &ePrimitives Maschinengehäuse&r. Der Weg führt über Latex aus Bäumen zu Plastik.']),
    'h_plastik': ('Plastik', [
        'Aus Baumsaft wird etwas, das die Erbauer nie hatten.',
        '',
        'Stell 16 &eKunststoff&r her.']),
    'h_laser': ('Erz aus dem Nichts', [
        'Ein Strahl in die Leere, und sie gibt Erz zurück.',
        '',
        'Die &eErz-Laserbasis&r mit Laserbohrern bohrt Erz aus dem Nichts.',
        'Tipp: Farbige Linsen bevorzugen bestimmte Erze.']),
    # ---------------- Inselmarkt ----------------
    'x_samen': ('Saatgut-Händler', [
        'Der Händler nimmt Samen, so viele du hast.',
        '',
        'Gib 256 &eWeizenkörner&r ab. Sie werden verbraucht. Zu viele Samen aus dem Sieb?',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_kies': ('Kieshändler', [
        'Kies hast du immer. Er zahlt trotzdem.',
        '',
        'Gib 256 &eKies&r ab. Er wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_cobble': ('Steinbruch', [
        'Der Generator läuft und läuft. Der Händler auch.',
        '',
        'Gib 512 &eBruchstein&r ab. Er wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_fleisch': ('Zombie-Abfall', [
        'Zu nichts gut, ehrlich gesagt. Er nimmt es trotzdem.',
        '',
        'Gib 128 &eVerrottetes Fleisch&r ab. Es wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_inferium': ('Essenz-Überschuss', [
        'Inferium wächst schneller, als du es brauchst.',
        '',
        'Gib 256 &eInferiumessenz&r ab. Sie wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_mehl': ('Müllerei', [
        'Feines Mehl, frisch vom Mahlstein.',
        '',
        'Gib 256 &eWeizenmehl&r ab. Es wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_seetang': ('Seetang-Kraftwerk', [
        'Getrockneter Seetang, gepresst zu Blöcken.',
        '',
        'Gib 64 &eGetrockneter Seetangblock&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_honig': ('Imkerei', [
        'Waben aus dem Bienenstock, noch warm.',
        '',
        'Gib 64 &eHonigwabe&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_warze': ('Netherwarzen-Farm', [
        'Netherwarzen wachsen auf Seelensand. Der Händler fragt nicht, woher.',
        '',
        'Gib 128 &eNetherwarze&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_knochen': ('Knochensammler', [
        'Von Skeletten oder vom Fischfang, ihm ist es gleich.',
        '',
        'Gib 128 &eKnochen&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_perlen': ('Enderhandel', [
        'Perlen aus Farm oder Simulation, gezählt und gewogen.',
        '',
        'Gib 32 &eEnderperle&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    'x_lohe': ('Lohenruten-Handel', [
        'Lohenruten im Überfluss? Er nimmt sie gern.',
        '',
        'Gib 32 &eLohenrute&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    'x_quelle': ('Quellstein-Handel', [
        'Quellsteine, die sich stapeln, finden hier einen Käufer.',
        '',
        'Gib 32 &eQuelljuwel&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    'x_polonium': ('Strahlender Handel', [
        'Er trägt Handschuhe. Du solltest es auch.',
        '',
        'Gib 4 &ePolonium Pellet&r ab, aus dem Fissionsreaktor oder dem Isotopen-Zentrifugen-Weg. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 3 Minecraft-Tage.']),
    'x_stern': ('Sternenhandel', [
        'Ein Stern gegen eine Sternkiste. Ein fairer Tausch.',
        '',
        'Gib 1 &eNetherstern&r ab. Er wird verbraucht.',
        'Wiederholbar: einmal alle 3 Minecraft-Tage.']),
    'x_supremium': ('Supremium-Handel', [
        'Supremium vom Feld, das Beste, was der Boden hergibt.',
        '',
        'Gib 8 &eSupremiumessenz&r ab. Sie wird verbraucht.',
        'Wiederholbar: einmal alle 3 Minecraft-Tage.']),
    'x_mechanik': ('Feinmechanik', [
        'Präzision vom Fließband, Stück für Stück geprüft.',
        '',
        'Gib 16 &ePräzisionsgetriebe&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    # ---------------- Sammlerbuch ----------------
    'p_essenzen': ('Alle Essenzen', [
        'Sechs Essenzen, sechs Abschnitte deines Weges.',
        '',
        'Sammle je eine Essenz jeder Stufe, von &eInferiumessenz&r bis Insanium Essence.',
        'Die Reihe erzählt deinen Weg: Feld, Create, Mekanism, AE2, Endgame.']),
    'p_netze': ('Alle Netze', [
        'Vom Faden bis zum Netherit.',
        '',
        'Sammle jedes Netz vom &eString Mesh&r bis zum Netherite Mesh. Jedes siebt andere Schätze.']),
    'p_archwood': ('Die vier Archwoods', [
        'Vier Bäume, vier Farben der alten Magie.',
        '',
        'Sammle alle vier &eArchwood-Setzlinge&r. Ihre Früchte sind Zutaten für Rituale.']),
    'p_trophaeen': ('Trophäen', [
        'Beweise, dass du die Wächter dieser Welt bezwungen hast.',
        '',
        'Sammle &eNetherstern&r, Drachenei und Wither-Skelettschädel.',
        'Tipp: Stell sie irgendwo schön aus.']),
    # ---------------- Baumeister ----------------
    'u_meissel': ('Der Meißel', [
        'Ein Block, viele Gesichter.',
        '',
        'Rechiseled: Mit dem &eChisel&r bekommt ein Block viele Muster, verbundene Texturen inklusive.']),
    'u_dach': ('Ein Dach über dem Kopf', [
        'Auch über der Leere regnet es.',
        '',
        'Macaw\'s Roofs, Doors und Windows: Dächer, Türen und Fenster in allen Holzarten.',
        'Bau 16 &eDachblöcke&r beliebiger Art.']),
    'u_moebel2': ('Einrichten', [
        'Eine Insel wird erst mit einem Stuhl zum Zuhause.',
        '',
        'Handcrafted und Macaw\'s Furniture: Stühle, Tische, Regale, Betten.',
        'Bau zwei &eStühle&r und einen Tisch.']),
    'u_bruecke2': ('Brücke ins Nichts', [
        'Ein Seil über dem Abgrund verbindet, was zerbrochen ist.',
        '',
        'Macaw\'s Bridges: &eHängebrücken&r zu deinen Nebeninseln.',
        'Tipp: Wege und Laternen gibt es in Macaw\'s Paths und Lights.']),
    'u_framed': ('Rahmenblöcke', [
        'Ein Block, der jedes Kleid trägt.',
        '',
        'FramedBlocks wie der &eFramed Cube&r nehmen das Aussehen jedes Blocks an.']),
    'u_gadget': ('Bau-Gadget', [
        'Ganze Flächen in einem Atemzug.',
        '',
        'Das &eBuilding Gadget&r baut ganze Flächen auf einmal. Es braucht Strom.']),
    'u_kopie': ('Inselarchitekt', [
        'Was du einmal gebaut hast, baust du nie wieder von Hand.',
        '',
        'Das &eCopy Paste Gadget&r speichert ganze Gebäude und baut sie woanders wieder auf.']),
}
STORY = {
    'w_start': ('Die erste Notiz', '„Wer das liest, steht auf einem Splitter unserer Welt. Darunter schläft das Herz der Leere.“'),
    'e_sieb': ('Sternenstaub', '„Einst siebten wir Sternenstaub. Du siebst Kies. Es ist derselbe Anfang.“'),
    'e_eisen': ('Der Funke', '„Das erste Metall. Wir nannten es den Funken, weil danach alles schneller brannte.“'),
    'g_autark': ('Zurück zum Leben', '„Eine Insel, die sich selbst nährt. So fängt der Weg zurück an.“'),
    'c_siebfabrik': ('Die erste Maschine', '„Unsere Maschinen liefen Tag und Nacht, bis sie verstummten. Du hast gerade die erste wieder geweckt.“'),
    'j_nether': ('Die zerbrochene Unterwelt', '„Auch die Unterwelt zerbrach. Unsere Festungen hängen dort noch in der Luft, leer wie wir.“'),
    's_reaktor': ('Kraft aus der Leere', '„Wir nahmen die Kraft aus der Leere, nicht aus Kohle. Wir nahmen zu viel, und der Boden riss.“'),
    'k_inject': ('Gier', '„Aus jedem Brocken das Vierfache. So reich waren wir. So gierig.“'),
    'l_auto': ('Netze, die denken', '„Unsere Netze dachten mit. Am Ende dachten sie schneller als wir.“'),
    'm_niemehr': ('Felder aus Erz', '„Als die Minen versiegt waren, ließen wir Erz auf Feldern wachsen. Wenigstens das war richtig.“'),
    'a_erzmagier': ('Maschine und Magie', '„Maschine und Magie waren für uns nie Gegensätze. Erst zusammen erreichten sie das Herz.“'),
    'h_fab': ('Feinde auswendig', '„Wir lernten unsere Feinde auswendig, bis wir sie nicht mehr bekämpfen mussten.“'),
    'j_drache': ('Der Wächter am Ende', '„Der Drache bewachte das Ende. Nicht für uns. Vor uns.“'),
    'z_sps': ('Der Herzschlag', '„Antimaterie, der Herzschlag der Leere in einer Kapsel. Behandle sie mit Respekt.“'),
    'z_herr': ('Das Erbe', '„Wer das Herz wieder schlagen lässt, trägt unser Erbe. Nimm nur, was du brauchst. Wir nahmen alles.“'),
}

# ---------------------------------------------------------------------
# 0.7.0: Story ohne Widerspruch (ein Weg genügt), Kern-Lore auf der Hauptstory, Akt II mit Notiz, Bienen ehrlich
# ---------------------------------------------------------------------
KAPITEL['story'] = ('Tagebuch des Wächters', KAPITEL['story'][1])   # Akt III heißt schon „Das Herz der Leere“
STORY['k_spalt'] = STORY.pop('s_reaktor')
STORY['c_alternator'] = ('Die Leitungen', '„Wir verlegten Leitungen bis unter die Wolken. Wenn der Strom floss, summte die ganze Insel.“')
STORY['z_weg'] = ('Ein Weg genügt', '„Wir wollten Maschine und Magie zugleich, und beide ganz. Einer der Wege hätte gereicht.“')
STORY['a_erzmagier'] = ('Das letzte Buch', '„Unsere Magier schrieben, bis die Seiten glühten. Nur dieses Buch hat das Zerbrechen überstanden.“')
QUESTS['b_zucht'] = ('Bienen aus Erz', [
    'Mit Geduld und Zucker summt bald das Metall.',
    '',
    'Erz-Bienen haben zwei Eltern: Ein &eQuartz Nest&r im Nether, mit Quarz gelockt, gibt die Kristallbiene.',
    'Ein &eGravel Nest&r in einem Fluss- oder Strandbiom (F3 zeigt das Biom) gibt die Ashy Mining Bee.',
    'Nester baust du selbst: Quartz Nest = Eisenschwert + Quartz in Netherrack, Gravel Nest = Holzschwert + Kies.',
    'Beide gekreuzt ergeben die Eisenbiene. Weitere Erze zeigt JEI unter „Bienenzucht“.'])
QUESTS['h_fab'][1].append('Für den Fabricator brauchst du einen &eNetheritbarren&r: Schwarzstein (Fass, siehe JEI) hämmern, den Schutt sieben (selten Antiker Schrott), dann 4 Netheritplatten + 4 Goldbarren.')

# ---------------------------------------------------------------------
# 0.8.0: Prüfungen der Leere (echte Aufgaben statt Haken), Deko-Tausch, Bienen prüfen die Eisenbiene
# ---------------------------------------------------------------------
KAPITEL['pruefungen'] = ('Prüfungen der Leere', ['Herausforderungen ohne Pflicht. Für Ingenieure, Magier und Mutige.'])
QUESTS['t_chimera'] = ('Die Chimera', [
    'Halb Horn, halb Flügel, ganz Zorn. Die Wilden haben eine Königin.',
    '',
    'Besiege die &eWilden-Chimera&r. Beschworen wird sie mit dem Ritual „Wilden beschwören“, verstärkt mit Horn, Stachel und Flügel.',
    '&cDas Ritual zerstört Blöcke rund um das Becken.&r Bau es auf einer eigenen Plattform.',
    'Belohnung: Such dir ein Item aus der Goldkiste aus.'])
QUESTS['t_speicher'] = ('Der Speicher der Erbauer', [
    'Die Erbauer maßen ihre Macht in Strom. Zeig, was deine Insel liefert.',
    '',
    'Stell einen &eAufgaben Bildschirm (1x1)&r auf (Eisen, Glas, Redstone), wähle diese Quest daran aus und speise 10 Millionen FE ein.',
    'Tipp: Kabel oder Pipez direkt an den Bildschirm anschließen.'])
QUESTS['t_fabrik'] = ('Tausend Barren', [
    'Eine Fabrik erkennt man daran, dass sie nicht aufhört.',
    '',
    'Hab 1024 &eEisenbarren&r gleichzeitig dabei (ein Rucksack hilft). Sie werden nicht verbraucht.'])
QUESTS['t_drache'] = ('Der zweite Drache', [
    'Der Wächter am Ende kehrt zurück, wenn man ihn ruft.',
    '',
    'Besiege den Enderdrachen ein zweites Mal. Vier Endkristalle auf dem Ausgangsportal rufen ihn zurück.',
    'Belohnung: Such dir ein Item aus der Sternkiste aus.'])
QUESTS['x_dach'] = ('Dachdecker', [
    'Der Händler baut eine neue Siedlung und braucht Ziegel.',
    '',
    'Gib 64 beliebige Dachblöcke (Macaw\'s Roofs) ab. Sie werden verbraucht.',
    'Wiederholbar: einmal pro Minecraft-Tag.'])
QUESTS['x_bruecke'] = ('Brückenbauer', [
    'Zwischen den Inseln fehlen Wege. Der Händler zahlt für jede Brücke.',
    '',
    'Gib 32 beliebige Hängebrücken (Macaw\'s Bridges) ab. Sie werden verbraucht.',
    'Wiederholbar: einmal pro Minecraft-Tag.'])
QUESTS['b_zucht'] = ('Bienen aus Erz', [
    'Mit Geduld und Zucker summt bald das Metall.',
    '',
    'Erz-Bienen haben zwei Eltern: Ein &eQuartz Nest&r im Nether, mit Quarz gelockt, gibt die Kristallbiene. Ein &eGravel Nest&r in einem Fluss- oder Strandbiom (F3 zeigt das Biom) gibt die Ashy Mining Bee.',
    'Nester baust du selbst: Quartz Nest = Eisenschwert + Quartz in Netherrack, Gravel Nest = Holzschwert + Kies.',
    'Beide gekreuzt ergeben die Eisenbiene. &lAufgabe:&r eine Wabe der Eisenbiene aus ihrem Stock.',
    'Tipp: Das Simulations-Upgrade hält Bienen im Stock. Das spart am Laptop viel Leistung.'])
```

## Datei: _src/bausteine.py
```py
"""Sky and Stone – Quest-Bausteine (Texte, Aufgaben, Belohnungen). Aufbau und Kapitel: _src/quests.py
Konzept: _src/QUESTS-KONZEPT.md · Gemini-Review: _src/GEMINI-QUESTS.md
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from questlib import *

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G, M, S = 'gear', 'hexagon', 'square'   # Meilenstein-Form, Kapitelziel, Info

# =====================================================================
# 1 Willkommen
# =====================================================================
willkommen = Chapter('willkommen', 'Willkommen', 'insel', 'ftbquests:book', sub='Kurz lesen, dann geht es los.', quests=[
    Q('w_start', 'Willkommen in der Leere', 0, 0, check(), shape=G, size=2.0, icon='ftbquests:book',
      sub='Sky and Stone', rewards=[crate('holz'), xp(10)],
      desc=['Unter dir: nichts. Um dich: nichts. Nur deine Insel.',
            '',
            'Dieses Buch führt dich durch alles, was das Pack kann: vom ersten Sieb bis zur Antimaterie. Die Kapitel verzweigen sich, du entscheidest, was du zuerst machst.',
            '',
            'Haken setzen = Quest erledigt. Belohnungen holst du mit einem Klick ab.']),
    Q('w_wachsen', 'Ducken lässt Pflanzen wachsen', -3, -1.5, check(), deps=['w_start'], icon='minecraft:oak_sapling', shape=S,
      rewards=[give('minecraft:bone_meal', 8)],
      desc=['Neben Setzlingen oder Feldern mehrmals ducken (Sneaken) beschleunigt das Wachstum.',
            'Klingt albern, spart am Anfang aber viel Wartezeit.']),
    Q('w_ernte', 'Ernten mit Rechtsklick', -3, 0, check(), deps=['w_start'], icon='minecraft:wheat', shape=S,
      desc=['Reife Pflanzen per Rechtsklick ernten: Die Pflanze wird automatisch neu gesetzt.']),
    Q('w_jei', 'Rezepte nachschlagen', -3, 1.5, check(), deps=['w_start'], icon='minecraft:crafting_table', shape=S,
      desc=['Taste R über einem Item zeigt das Rezept, U zeigt, wofür es gebraucht wird.',
            'Für Siebe zeigt JEI auch alle möglichen Funde mit Chancen.']),
    Q('w_ultimine', 'Ganze Adern abbauen', 3, -1.5, check(), deps=['w_start'], icon='minecraft:iron_pickaxe', shape=S,
      desc=['Taste ` (Gravis) gedrückt halten und abbauen: FTB Ultimine baut zusammenhängende Blöcke auf einmal ab.',
            'Praktisch für Bäume, Bruchstein und Kies.']),
    Q('w_karte', 'Karte und Wegpunkte', 3, 0, check(), deps=['w_start'], icon='minecraft:compass', shape=S,
      desc=['M öffnet die Weltkarte, B setzt einen Wegpunkt.',
            'Später verbinden Wegsteine (Waystones) deine Inseln.']),
    Q('w_team', 'Mit Freunden spielen', 3, 1.5, check(), deps=['w_start'], icon='minecraft:player_head', shape=S, optional=True,
      desc=['/skyblock invite <Name> holt Freunde auf deine Insel.',
            'Für gemeinsamen Quest-Fortschritt zusätzlich ein FTB-Team gründen (Taste im Inventar oben links).',
            'Im Team holt jeder seine Quest-Belohnungen selbst ab. Nur die Tauschgeschäfte im Inselmarkt geben eine Kiste pro Team.']),
    Q('w_los', 'Auf geht\'s!', 0, 3, check(), deps=['w_wachsen', 'w_ernte', 'w_jei'], shape=M, size=1.5, icon='exdeorum:crook',
      rewards=[give('exdeorum:crook'), xp(20)],
      desc=['Weiter geht es im Kapitel „Erde, Kies und Hoffnung“.']),
])

# =====================================================================
# 2 Erde, Kies und Hoffnung (Ex Deorum)
# =====================================================================
erde = Chapter('erde', 'Erde, Kies und Hoffnung', 'insel', 'exdeorum:oak_sieve', sub='Aus Nichts wird Erz.', quests=[
    Q('e_holz', 'Der Baum ist dein Freund', 0, 0, item('minecraft:oak_log', 8), deps=['w_los'], rewards=[xp(10)],
      desc=['Fäll den Baum, aber pflanz die Setzlinge wieder!', 'Ohne Holz geht hier gar nichts.']),
    # Ast A: Laub
    Q('e_haken', 'Mit dem Haken ins Laub', -3, -1.5, item('exdeorum:crook'), deps=['e_holz'], rewards=[xp(10)],
      desc=['Der Haken lässt Laub öfter Setzlinge fallen und findet manchmal Seidenraupen.']),
    Q('e_raupe', 'Seidenraupe', -6, -1.5, item('exdeorum:silkworm'), deps=['e_haken'], rewards=[give('exdeorum:silkworm', 2), xp(15)],
      desc=['Setz eine Seidenraupe auf Laub: Es wird langsam zu Spinnweben.', 'Spinnweben zerfallen beim Abbauen zu Faden.']),
    Q('e_faden', 'Faden', -9, -1.5, item('minecraft:string', 8), deps=['e_raupe'], rewards=[xp(15)],
      desc=['Faden brauchst du für das erste Siebnetz.']),
    # Ast B: Stein
    Q('e_fass', 'Kompostfass', -3, 1.5, item('exdeorum:oak_barrel'), deps=['e_holz'], rewards=[give('minecraft:bone_meal', 8), xp(10)],
      desc=['Wirf Laub, Setzlinge oder Essen hinein: Nach einer Weile wird daraus Erde.',
            'Fässer sammeln bei Regen auch Wasser.']),
    Q('e_cobble', 'Bruchstein-Generator', -6, 1.5, item('minecraft:cobblestone', 32), deps=['e_fass'], rewards=[xp(15)],
      desc=['Lava und Wasser so platzieren, dass sie neben einem freien Block zusammenfließen.',
            'Tipp: Mit dem Eis aus dem Startinventar baust du eine unendliche Wasserquelle (2×2-Becken).']),
    Q('e_hammer', 'Hammerzeit', -9, 1.5, item('exdeorum:stone_hammer'), deps=['e_cobble'], rewards=[xp(15)],
      desc=['Hämmer zerschlagen Blöcke: Bruchstein → Kies → Sand → Staub.',
            'Später übernimmt das der Create-Mühlstein.']),
    # Treffpunkt: Sieb
    Q('e_sieb', 'Das Sieb', -12, 0, [item('exdeorum:oak_sieve'), item('exdeorum:string_mesh')], deps=['e_faden', 'e_hammer'],
      shape=M, size=1.5, rewards=[crate('holz'), xp(30)],
      desc=['Das Herz jeder Skyblock-Insel. Netz einsetzen, Erde, Kies oder Sand drauf, Rechtsklick halten.',
            'Tipp: Stell bis zu 5×5 Siebe nebeneinander – ein Klick siebt alle gleichzeitig!']),
    Q('e_samen', 'Was in der Erde steckt', -15, -2, item('minecraft:wheat_seeds'), deps=['e_sieb'], rewards=[xp(10)],
      desc=['Erde mit dem Fadennetz gibt Samen, Setzlinge und mehr.', 'Weiter im Kapitel „Grünes Händchen“.']),
    Q('e_tiegel', 'Wasser aus Blättern', -15, 0, item('exdeorum:oak_crucible'), deps=['e_sieb'], rewards=[xp(15)],
      desc=['Der Holztiegel schmilzt Laub und Setzlinge zu Wasser.', 'Fürs Erste deine zweite Wasserquelle.']),
    Q('e_porzellan', 'Porzellan', -18, 0, item('exdeorum:porcelain_clay_ball', 4), deps=['e_tiegel'], rewards=[xp(15)],
      desc=['Staub im Wasserfass ergibt Ton. Ton + Knochenmehl = Porzellan.']),
    Q('e_lavatiegel', 'Lava aus Stein', -21, 0, item('exdeorum:porcelain_crucible'), deps=['e_porzellan'], rewards=[xp(25)],
      desc=['Der Porzellantiegel schmilzt Bruchstein zu Lava, wenn darunter eine Hitzequelle steht (Fackel, Lava, Feuer).',
            'Damit brauchst du deinen Lavaeimer nie wieder zu fürchten.']),
    Q('e_brocken', 'Erzbrocken', -15, 2, item('exdeorum:iron_ore_chunk', 4), deps=['e_sieb'], rewards=[xp(20)],
      desc=['Kies mit dem Feuersteinnetz (oder besser) gibt Erzbrocken.', '4 Brocken = 1 Erz zum Schmelzen.']),
    Q('e_feuernetz', 'Feuersteinnetz', -18, 2, item('exdeorum:flint_mesh'), deps=['e_brocken'], rewards=[xp(15)],
      desc=['Bessere Netze, bessere Funde.', 'Netze lassen sich mit Effizienz und Glück verzaubern!']),
    Q('e_eisen', 'Erster Eisenbarren', -21, 2, item('minecraft:iron_ingot', 4), deps=['e_feuernetz'], shape=G, size=2.0,
      rewards=[crate('eisen'), xp(50)],
      desc=['Geschafft: Metall aus dem Nichts.', 'Jetzt öffnen sich Create, Landwirtschaft und Werkzeuge.']),
    Q('e_kupfer', 'Kupfer und Zink', -24, 0.5, [item('minecraft:copper_ingot', 8), item('create:zinc_ingot', 4)], deps=['e_eisen'],
      rewards=[xp(30)],
      desc=['Kupfer- und Zinkbrocken kommen auch aus dem Kies.', 'Mit Zink startest du in Create. Mehr musst du von Hand nicht sieben!']),
    Q('e_eisennetz', 'Eisennetz', -24, 3.5, item('exdeorum:iron_mesh'), deps=['e_eisen'], rewards=[xp(20)],
      desc=['Mit dem Eisennetz tauchen Osmium-, Zinn-, Blei- und Silberbrocken auf.',
            'Auch Inferium-Essenz für Mystical Agriculture steckt in der Erde.']),
    Q('e_kanne', 'Bessere Gießkanne', -27, 2, item('exdeorum:iron_watering_can'), deps=['e_eisen'], rewards=[xp(15)], optional=True,
      desc=['Hält mehr Wasser und lässt Bäume schneller wachsen.']),
])

# =====================================================================
# 3 Grünes Händchen
# =====================================================================
gruen = Chapter('gruen', 'Grünes Händchen', 'insel', 'minecraft:wheat', sub='Essen, Holz und die ersten Samen.', quests=[
    Q('g_feld', 'Das erste Feld', 0, 0, item('minecraft:wheat', 16), deps=['e_samen'], rewards=[xp(15)],
      desc=['Weizen, Karotten, Kartoffeln – alles kommt aus dem Sieb.', 'Ducken neben dem Feld beschleunigt es.']),
    Q('g_brett', 'Schneidebrett', 3, -1.5, item('farmersdelight:cutting_board'), deps=['g_feld'], rewards=[xp(15)],
      desc=['Farmer\'s Delight: Schneiden gibt mehr aus deinen Zutaten heraus.']),
    Q('g_topf', 'Kochtopf', 6, -1.5, item('farmersdelight:cooking_pot'), deps=['g_brett'], rewards=[xp(20)],
      desc=['Gerichte aus dem Kochtopf machen lange satt und geben Boni.']),
    Q('g_tiere', 'Nutztiere', 3, 1.5, [item('minecraft:leather', 4), item('minecraft:egg', 4)], deps=['g_feld'], rewards=[xp(20)],
      desc=['Spawneier für Kuh, Schaf, Huhn und Schwein findest du beim Sieben von Erde.',
            'Zäune nicht vergessen – um dich ist nur Leere!']),
    Q('g_topf_pflanze', 'Botany Pot', 0, 3, item('botanypots:terracotta_botany_pot'), deps=['g_feld'], rewards=[xp(20)],
      desc=['Pflanzen und Bäume wachsen im Topf von allein.',
            'Mit Trichter-Topf wird geerntet und weitergereicht – deine erste Automatik.']),
    Q('g_baumtopf', 'Holz im Topf', 0, 6, item('botanypots:terracotta_hopper_botany_pot'), deps=['g_topf_pflanze'], rewards=[crate('holz'), xp(25)],
      desc=['Setzling + Erde in einen Trichter-Topf: unendlich Holz ohne Axt.']),
    Q('g_festessen', 'Sterneküche in der Leere', 9, 0, [item('farmersdelight:shepherds_pie_block'), item('farmersdelight:roast_chicken_block')],
      deps=['g_topf', 'g_tiere'], shape=M, size=1.5, rewards=[crate('eisen'), xp(60)],
      desc=['Zwei Festessen, komplett aus Inselzutaten.', 'Ab jetzt ist Hunger kein Thema mehr.']),
    Q('g_inferium', 'Inferium-Essenz', -3, 3, item('mysticalagriculture:inferium_essence', 16), deps=['g_feld'], rewards=[xp(20)],
      desc=['Erde mit dem Fadennetz (oder besser) gibt Inferium-Essenz.', 'Damit beginnt Mystical Agriculture.']),
    Q('g_autark', 'Autarke Insel', 0, 9, check(), deps=['g_baumtopf', 'g_festessen'], shape=G, size=2.0, icon='minecraft:hay_block',
      rewards=[crate('eisen'), xp(80)],
      desc=['Essen und Holz kommen von selbst. Haken setzen, wenn deine Insel sich selbst versorgt.']),
])

# =====================================================================
# 4 Kraft der Zahnräder (Create)
# =====================================================================
create = Chapter('create', 'Kraft der Zahnräder', 'technik', 'create:cogwheel', sub='Create: Sieben ohne Klicken.', quests=[
    Q('c_andesit', 'Andesitlegierung', 0, 0, item('create:andesite_alloy', 16), deps=['e_kupfer'], rewards=[xp(25)],
      desc=['Andesit + Zink- oder Eisennuggets. Andesit-Kiesel kommen aus dem Sieb – JEI (U auf Andesit) zeigt alle Wege.', 'Der Grundstoff für fast alles in Create.']),
    Q('c_rad', 'Wasserrad', 3, 0, item('create:water_wheel'), deps=['c_andesit'], rewards=[xp(20)],
      desc=['Fließendes Wasser dreht das Rad – deine erste Kraftquelle.', 'Alternativ: Windmühle mit Segeln.']),
    Q('c_muehle', 'Mühlstein statt Hammer', 6, -1.5, item('create:millstone'), deps=['c_rad'], rewards=[xp(25)],
      desc=['Der Mühlstein macht alles, was der Hammer konnte: Bruchstein → Kies → Sand → Staub.',
            'Ein Trichter oben drauf und das Mahlen läuft von allein.']),
    Q('c_sifter', 'Der Create-Sifter', 9, -1.5, [item('createsifter:sifter'), item('createsifter:string_mesh')], deps=['c_muehle'],
      shape=M, size=1.5, rewards=[crate('eisen'), xp(40)],
      desc=['Er siebt mit denselben Tabellen wie das Handsieb – nur ohne dich.',
            'Netze: Faden → Faden, Andesit → Feuerstein, Zink → Eisen, Messing → Gold.']),
    Q('c_netze', 'Bessere Sifter-Netze', 12, -1.5, [item('createsifter:andesite_mesh'), item('createsifter:zinc_mesh')], deps=['c_sifter'],
      rewards=[xp(25)], desc=['Andesit- und Zinknetz entsprechen Feuerstein- und Eisennetz.']),
    Q('c_extruder', 'Der Extruder', 9, -4, item('create_mechanical_extruder:mechanical_extruder'), deps=['c_muehle'], rewards=[xp(25)],
      desc=['Erzeugt Bruchstein (oder Basalt, Stein …) aus Lava und Wasser daneben.',
            'Zusammen mit Mühlstein und Sifter: eine Siebfabrik ohne Handarbeit.']),
    Q('c_presse', 'Mechanische Presse', 6, 1.5, item('create:mechanical_press'), deps=['c_rad'], rewards=[xp(20)],
      desc=['Presst Bleche – gebraucht für viele Bauteile.']),
    Q('c_fan', 'Waschen mit Wind', 9, 1.5, item('create:encased_fan'), deps=['c_presse'], rewards=[xp(25)],
      desc=['Ein Ventilator, der durch Wasser bläst, wäscht zerkleinerte Erze: mehr Nuggets!']),
    Q('c_mixer', 'Mixer und Becken', 9, 4, [item('create:mechanical_mixer'), item('create:basin')], deps=['c_presse'], rewards=[xp(25)],
      desc=['Mixer + Becken mischen Legierungen und Flüssigkeiten.']),
    Q('c_messing', 'Messing', 12, 4, item('create:brass_ingot', 16), deps=['c_mixer', 'c_brenner'], rewards=[crate('eisen'), xp(40)],
      desc=['Kupfer + Zink im beheizten Mixer: Unter das Becken gehört ein Lohenbrenner.']),
    Q('c_brenner', 'Lohenbrenner ohne Nether', 9, 7, item('create:blaze_burner'), deps=['c_mixer'], rewards=[xp(25)],
      desc=['Leerer Lohenbrenner + 4 Lohenpulver (aus dem Staub-Sieb) = Lohenbrenner.',
            'Mit Kohle oder Holz gefüttert heizt er dein Becken für Messing.']),
    Q('c_tertium', 'Tertium im Mixer', 15, 4, item('mysticalagriculture:tertium_essence', 4), deps=['c_messing', 'm_prudentium'],
      rewards=[xp(40)],
      desc=['4 Prudentium + 1 Messingbarren im Create-Mixer ergeben 2 Tertium-Essenz.',
            'Nur so kommst du an Stufe-3-Samen.']),
    Q('c_mechanismus', 'Präzisionsmechanismus', 15, 1.5, item('create:precision_mechanism'), deps=['c_messing', 'c_fan'], rewards=[xp(40)],
      desc=['Entsteht am Fließband mit Deployer und Presse – dein erster „Sequenced Assembly“-Weg.']),
    Q('c_alternator', 'Strom aus Drehung', 15, -1.5, item('createaddition:alternator'), deps=['c_mechanismus'], rewards=[xp(40)],
      desc=['Der Alternator (Create Crafts & Additions) macht aus Drehkraft Strom (FE).', 'Damit beginnt das Kapitel „Strom und Leitungen“.']),
    Q('c_siebfabrik', 'Die Siebfabrik', 18, -1.5, [item('minecraft:iron_ingot', 64), item('create:zinc_ingot', 32), item('minecraft:copper_ingot', 64)],
      deps=['c_netze', 'c_extruder', 'c_fan'], shape=G, size=2.0, rewards=[crate('gold'), xp(100)],
      desc=['Extruder → Mühlstein → Sifter → Waschen → Ofen, alles auf Förderbändern.',
            'Wenn die Barren von allein kommen, ist das Kapitel geschafft.']),
    Q('c_deployer', 'Deployer', 12, 7, item('create:deployer'), deps=['c_messing'], rewards=[xp(25)], optional=True,
      desc=['Eine Hand, die für dich klickt: Blöcke setzen, Items benutzen, Gegner schlagen.']),
    Q('c_crafter', 'Mechanische Werkbank', 15, 7, item('create:mechanical_crafter', 9), deps=['c_mechanismus'], rewards=[xp(25)], optional=True,
      desc=['Große Rezepte automatisch herstellen.']),
])

# =====================================================================
# 5 Strom und Leitungen (Powah, Pipez, Ex Deorum mechanisch)
# =====================================================================
strom = Chapter('strom', 'Strom und Leitungen', 'technik', 'powah:energy_cell_starter', sub='Powah, Pipez und Maschinen, die sieben.', quests=[
    Q('s_draht', 'Kupferdraht', 0, 0, item('createaddition:copper_spool'), deps=['c_alternator'], rewards=[xp(15)],
      desc=['Kabelrollen verbinden Akkus und Maschinen von Create Crafts & Additions.']),
    Q('s_akku', 'Akku', 3, 0, item('createaddition:modular_accumulator'), deps=['s_draht'], rewards=[xp(20)],
      desc=['Speichert Strom für windstille Zeiten.']),
    Q('s_mechsieb', 'Mechanisches Sieb', 3, -2, item('exdeorum:mechanical_sieve'), deps=['s_draht'], shape=M, size=1.3, rewards=[crate('eisen'), xp(40)],
      desc=['Das Ex-Deorum-Sieb mit Strom: Netz rein, Kies per Trichter rein, fertig.',
            'Braucht nur 20 FE pro Tick.']),
    Q('s_mechhammer', 'Mechanischer Hammer', 6, -2, item('exdeorum:mechanical_hammer'), deps=['s_mechsieb'], rewards=[xp(25)], optional=True,
      desc=['Zerkleinert Blöcke mit Strom.']),
    Q('s_paste', 'Dielektrische Paste', 3, 2, item('powah:dielectric_paste', 16), deps=['s_draht'], rewards=[xp(15)],
      desc=['Grundzutat für Powah: Ton, Kohle und Lava.']),
    Q('s_orb', 'Energizing Orb', 6, 2, [item('powah:energizing_orb'), item('powah:energizing_rod_starter', 2)], deps=['s_paste'], rewards=[xp(30)],
      desc=['Der Orb lädt Items mit Strom auf. Stäbe drumherum liefern die Energie.']),
    Q('s_stahl', 'Energetisierter Stahl', 9, 2, item('powah:steel_energized', 8), deps=['s_orb'], rewards=[xp(25)],
      desc=['Eisen + Gold im Orb. Für alle Powah-Maschinen.']),
    Q('s_furnator', 'Furnator', 9, 0, item('powah:furnator_starter'), deps=['s_orb'], rewards=[xp(20)],
      desc=['Verbrennt Kohle und Holz zu Strom – solide Grundversorgung.']),
    Q('s_solar', 'Sonnenkollektoren', 12, 0, item('powah:solar_panel_basic', 4), deps=['s_stahl'], rewards=[xp(25)],
      desc=['Strom ohne Brennstoff. Tagsüber.']),
    Q('s_kristall', 'Lohenkristall', 12, 2, item('powah:crystal_blazing', 4), deps=['s_stahl'], rewards=[xp(25)],
      desc=['Aus Lohenpulver im Orb. Lohenpulver gibt es im Staub-Sieb.']),
    Q('s_pipe', 'Rohre verlegen', 0, 4, [item('pipez:item_pipe', 8), item('pipez:energy_pipe', 8)], deps=['s_draht'], rewards=[xp(20)],
      desc=['Pipez: Items, Flüssigkeiten und Strom von A nach B.', 'Schraubenschlüssel öffnet die Einstellungen am Rohrende.']),
    Q('s_upgrade', 'Schnellere Rohre', 3, 4, [item('pipez:basic_upgrade'), item('pipez:improved_upgrade')], deps=['s_pipe'], rewards=[xp(20)],
      desc=['Basic und Improved Upgrades machen Rohre schneller und erlauben Filter.',
            'Advanced braucht Mekanism-Schaltkreise, Ultimate zusätzlich AE2-Prozessoren.']),
    Q('s_reaktor', 'Netzstrom', 15, 1, item('powah:reactor_basic', 36), deps=['s_kristall', 's_solar', 's_akku'], shape=G, size=2.0,
      rewards=[crate('gold'), xp(120)],
      desc=['Ein Powah-Reaktor (3×4×3 aus Reaktorteilen) mit Uraninit aus dem Gold-Sieb.',
            'Ab hier ist Strom kein Engpass mehr.']),
])

# =====================================================================
# 6 Mekanismus
# =====================================================================
mek = Chapter('mekanism', 'Mekanismus', 'technik', 'mekanism:metallurgic_infuser', sub='Mehr Erz aus jedem Brocken.', quests=[
    Q('k_osmium', 'Osmium', 0, 0, item('mekanism:ingot_osmium', 8), deps=['s_draht', 'e_eisennetz'], rewards=[xp(20)],
      desc=['Osmiumbrocken gibt es im Kies mit dem Eisennetz.']),
    Q('k_infuser', 'Metallurgic Infuser', 3, 0, item('mekanism:metallurgic_infuser'), deps=['k_osmium'], rewards=[xp(30)],
      desc=['Die wichtigste Mekanism-Maschine: Legierungen, Stahl, Schaltkreise.']),
    Q('k_stahl', 'Stahl', 6, -1.5, item('mekanism:ingot_steel', 16), deps=['k_infuser'], rewards=[xp(20)], desc=['Eisen + Kohle im Infuser, dann schmelzen.']),
    Q('k_schalt', 'Grundschaltkreis', 6, 1.5, item('mekanism:basic_control_circuit', 4), deps=['k_infuser'], rewards=[xp(20)],
      desc=['Osmium + Redstone. Steckt in fast jeder Maschine.']),
    Q('k_enrich', '×2: Anreicherung', 9, 0, item('mekanism:enrichment_chamber'), deps=['k_stahl', 'k_schalt'], rewards=[xp(30)],
      desc=['Ein Erz → zwei Staub. Der erste Schritt der Erzverarbeitung.']),
    Q('k_alloy', 'Infused Alloy', 9, 3, item('mekanism:alloy_infused', 8), deps=['k_infuser'], rewards=[xp(25)],
      desc=['Redstone + Eisen. Brauchst du auch für Imperium-Essenz (Mystical Agriculture).']),
    Q('k_purif', '×3: Reinigung', 12, 0, item('mekanism:purification_chamber'), deps=['k_enrich'], rewards=[xp(40)],
      desc=['Mit Sauerstoff aus dem Elektrolyse-Separator: drei Barren pro Erz.']),
    Q('k_separator', 'Elektrolyse', 12, -2.5, item('mekanism:electrolytic_separator'), deps=['k_enrich'], rewards=[xp(25)],
      desc=['Spaltet Wasser in Wasserstoff und Sauerstoff.']),
    Q('k_inject', '×4: Injektion', 15, 0, item('mekanism:chemical_injection_chamber'), deps=['k_purif'], shape=G, size=2.0,
      rewards=[crate('gold'), xp(120)],
      desc=['Vier Barren pro Erz! Braucht Chlorwasserstoff (Salz aus der Verdampfung + Wasserstoff).',
            'Meilenstein „Vierfach-Erz“: Damit ist Erz nie wieder knapp.']),
    Q('k_x5', '×5: Die volle Kette', 18, 0, item('mekanism:chemical_dissolution_chamber'), deps=['k_inject'], optional=True,
      rewards=[crate('gold'), xp(80)],
      desc=['Optional: Auflösen, Waschen, Kristallisieren – fünf Barren pro Erz.', 'Lohnt sich nur, wenn du noch viel siebst.']),
    Q('k_kabel', 'Universalkabel', 3, 3, item('mekanism:basic_universal_cable', 8), deps=['k_infuser'], rewards=[xp(15)],
      desc=['Mekanism-Kabel tragen Strom.']),
    Q('k_cube', 'Energiewürfel', 6, 4.5, item('mekanism:basic_energy_cube'), deps=['k_kabel'], rewards=[xp(20)], desc=['Großer Stromspeicher.']),
    Q('k_fortschritt', 'Fortgeschrittener Schaltkreis', 9, 6, item('mekanism:advanced_control_circuit', 4), deps=['k_alloy'], rewards=[xp(25)],
      desc=['Freischaltung: Pipez-Advanced-Upgrade.']),
    Q('k_jetpack', 'Erster Flug', 12, 6, item('ironjetpacks:jetpack'), deps=['k_fortschritt'], shape=G, size=2.0,
      rewards=[crate('gold'), xp(100)],
      desc=['Iron Jetpacks: Jetpack + Thruster + Kapsel. Mit Strom geladen trägt es dich über die Leere.',
            'Tipp: Lieber vorher noch einmal Fallschutz checken …']),
    Q('k_tiab', 'Zeit ist Geld', 15, 6, item('tiab:time_in_a_bottle'), deps=['k_jetpack'], rewards=[xp(50)],
      desc=['Time in a Bottle sammelt Zeit, solange es im Inventar ist.',
            'Rechtsklick auf eine Maschine beschleunigt sie – hier bis 8-fach.']),
    Q('k_meka', 'Werkzeug der Zukunft', 15, 3, item('mekanism:atomic_disassembler'), deps=['k_fortschritt'], rewards=[xp(40)], optional=True,
      desc=['Spitzhacke, Axt und Schaufel in einem – mit Strom.']),
])

# =====================================================================
# 7 Lagerhaus (Sophisticated/Functional + AE2)
# =====================================================================
lager = Chapter('lager', 'Lagerhaus', 'technik', 'ae2:controller', sub='Erst Ordnung, dann ein Netz, das mitdenkt.', quests=[
    Q('l_rucksack', 'Rucksack', 0, 0, item('sophisticatedbackpacks:backpack'), deps=['e_eisen'], rewards=[xp(20)],
      desc=['Mehr Platz zum Mitnehmen. Mit Upgrades sammelt er Items auf oder sortiert.']),
    Q('l_pickup', 'Aufsammel-Upgrade', 3, -1.5, item('sophisticatedbackpacks:pickup_upgrade'), deps=['l_rucksack'], rewards=[xp(20)],
      desc=['Füllt den Rucksack automatisch mit Siebfunden.']),
    Q('l_fass', 'Lagerfässer', 3, 1.5, item('sophisticatedstorage:barrel'), deps=['l_rucksack'], rewards=[xp(15)],
      desc=['Aufrüstbare Fässer und Truhen mit Sortierknopf.']),
    Q('l_schubladen', 'Schubladen', 6, 0, item('functionalstorage:oak_1', 4), deps=['l_fass'], rewards=[xp(20)],
      desc=['Functional Storage: viel von einer Sorte auf kleinem Raum.']),
    Q('l_controller', 'Schubladen-Wand', 9, 0, item('functionalstorage:storage_controller'), deps=['l_schubladen'], shape=M, size=1.4,
      rewards=[crate('eisen'), xp(40)],
      desc=['Der Controller macht alle Schubladen zu einem Lager mit einem Eingang.',
            'Löst das Kistenchaos, bis AE2 steht.']),
    Q('l_muell', 'Mülleimer', 6, -3, item('trashcans:item_trash_can'), deps=['l_fass'], rewards=[xp(10)], optional=True,
      desc=['Überschuss vom Sieb einfach vernichten. Ehrlich, du wirst ihn brauchen.']),
    # AE2-Ast
    Q('l_certus', 'Certus-Quarz', 0, 4, item('ae2:certus_quartz_crystal', 16), deps=['e_eisennetz'], rewards=[xp(20)],
      desc=['Sand mit Eisennetz gibt Certus-Quarz.']),
    Q('l_lader', 'Lader', 3, 4, [item('ae2:charger'), item('ae2:charged_certus_quartz_crystal', 4)], deps=['l_certus', 's_draht'], rewards=[xp(20)],
      desc=['Lädt Certus mit Strom auf.']),
    Q('l_fluix', 'Fluix', 6, 4, item('ae2:fluix_crystal', 16), deps=['l_lader'], rewards=[xp(20)],
      desc=['Geladener Certus + Redstone + Quarz in Wasser werfen.']),
    Q('l_inscriber', 'Inscriber und Prägeplatten', 9, 4, [item('ae2:inscriber'), item('ae2:logic_processor_press'), item('ae2:calculation_processor_press'),
      item('ae2:engineering_processor_press'), item('ae2:silicon_press')], deps=['l_fluix', 'k_stahl'], shape=M, size=1.4, rewards=[xp(40)],
      desc=['Ohne Meteoriten: Die Prägeplatten werden hier hergestellt (JEI zeigt wie).',
            'Freischaltung: Supremium-Essenz und Pipez-Ultimate.']),
    Q('l_prozessoren', 'Prozessoren', 12, 4, [item('ae2:logic_processor', 4), item('ae2:calculation_processor', 4), item('ae2:engineering_processor', 4)],
      deps=['l_inscriber'], rewards=[crate('gold'), xp(40)], desc=['Tipp: Inscriber mit Pipez füttern – sonst wird es mühsam.']),
    Q('l_netz', 'ME-Netz', 15, 4, [item('ae2:controller'), item('ae2:drive'), item('ae2:item_storage_cell_4k'), item('ae2:terminal')],
      deps=['l_prozessoren'], rewards=[xp(50)], desc=['Controller, Laufwerk, Zelle, Terminal: alles an einem Ort.']),
    Q('l_auto', 'Das Netz denkt mit', 18, 4, [item('ae2:pattern_provider'), item('ae2:molecular_assembler'), item('ae2:crafting_unit')],
      deps=['l_netz', 'l_controller'], shape=G, size=2.0, rewards=[crate('gold'), xp(150)],
      desc=['Autocrafting: Muster, Assembler und Crafting-CPU.', 'Ab jetzt bestellst du Dinge, statt sie zu bauen.']),
    Q('l_wireless', 'Kabellos', 21, 2.5, item('ae2wtlib:wireless_universal_terminal'), deps=['l_auto'], rewards=[xp(40)],
      desc=['Dein ME-Netz in der Tasche.']),
    Q('l_appmek', 'Gase im Netz', 21, 5.5, item('appmek:chemical_storage_cell_1k'), deps=['l_auto', 'k_separator'], rewards=[xp(30)], optional=True,
      desc=['Applied Mekanistics: AE2 speichert Mekanism-Gase und -Chemikalien.']),
    Q('l_mega', 'Riesenspeicher', 24, 4, item('megacells:item_storage_cell_1m'), deps=['l_wireless'], rewards=[crate('stern'), xp(100)], optional=True,
      desc=['MEGA Cells: Zellen mit Millionen Bytes. Für Leute, die nichts wegwerfen.']),
])

# =====================================================================
# 8 Mystische Landwirtschaft
# =====================================================================
ma = Chapter('ma', 'Mystische Landwirtschaft', 'natur', 'mysticalagriculture:inferium_seeds', sub='Erz, das auf Feldern wächst.', quests=[
    Q('m_altar', 'Infusionsaltar', 0, 0, [item('mysticalagriculture:infusion_altar'), item('mysticalagriculture:infusion_pedestal', 8)],
      deps=['g_inferium'], rewards=[xp(30)],
      desc=['Altar in die Mitte, 8 Sockel drumherum. Hier entstehen Samen.']),
    Q('m_inferium', 'Inferium-Samen', 3, 0, item('mysticalagriculture:inferium_seeds'), deps=['m_altar'], rewards=[xp(25)],
      desc=['Samen, die Essenz wachsen lassen. Ab jetzt wird Essenz geerntet statt gesiebt.']),
    Q('m_prudentium', 'Prudentium', 6, 0, item('mysticalagriculture:prudentium_essence', 16), deps=['m_inferium'], rewards=[xp(25)],
      desc=['4 Inferium → 1 Prudentium (Stufe 2).']),
    Q('m_eisen', 'Eisen vom Feld', 9, -1.5, item('mysticalagriculture:iron_seeds'), deps=['m_prudentium'], shape=M, size=1.4, rewards=[crate('eisen'), xp(50)],
      desc=['Der Moment, in dem das Sieben endet: Eisen wächst.']),
    Q('m_kupfer', 'Kupfer und Kohle', 9, 1.5, [item('mysticalagriculture:copper_seeds'), item('mysticalagriculture:coal_seeds')], deps=['m_prudentium'], rewards=[xp(30)]),
    Q('m_tertium', 'Stufe 3: Tertium', 12, 0, item('mysticalagriculture:tertium_essence', 16), deps=['m_eisen', 'c_tertium'], rewards=[xp(40)],
      desc=['Nur im Create-Mixer (Prudentium + Messing). Siehe Kapitel „Kraft der Zahnräder“.']),
    Q('m_gold', 'Gold, Redstone, Lapis', 15, -1.5, [item('mysticalagriculture:gold_seeds'), item('mysticalagriculture:redstone_seeds')], deps=['m_tertium'], rewards=[xp(40)]),
    Q('m_imperium', 'Stufe 4: Imperium', 15, 1.5, item('mysticalagriculture:imperium_essence', 16), deps=['m_tertium', 'k_alloy'], rewards=[xp(50)],
      desc=['Kreuz aus 4 Tertium um eine Infused Alloy (Mekanism).']),
    Q('m_diamant', 'Diamanten vom Feld', 18, 1.5, item('mysticalagriculture:diamond_seeds'), deps=['m_imperium'], shape=M, size=1.4, rewards=[crate('gold'), xp(80)]),
    Q('m_beschleuniger', 'Wachstumsbeschleuniger', 12, 3.5, item('mysticalagriculture:inferium_growth_accelerator', 4), deps=['m_tertium'], rewards=[xp(30)],
      desc=['Unter das Ackerland gestapelt: Pflanzen darüber wachsen schneller.']),
    Q('m_acker', 'Essenz-Ackerland', 15, 3.5, item('mysticalagriculture:imperium_farmland', 9), deps=['m_imperium'], rewards=[xp(30)],
      desc=['Passendes Ackerland gibt Samen derselben Stufe mehr Ertrag.']),
    Q('m_supremium', 'Stufe 5: Supremium', 21, 1.5, item('mysticalagriculture:supremium_essence', 8), deps=['m_imperium', 'l_prozessoren'], rewards=[xp(80)],
      desc=['Kreuz aus 4 Imperium um einen Engineering-Prozessor (AE2).']),
    Q('m_niemehr', 'Nie wieder sieben', 24, 0, [item('mysticalagriculture:osmium_seeds'), item('mysticalagriculture:certus_quartz_seeds'), item('mysticalagriculture:zinc_seeds')],
      deps=['m_supremium', 'm_diamant'], shape=G, size=2.0, rewards=[crate('stern'), xp(150)],
      desc=['Osmium, Certus und Zink wachsen jetzt auch. Dein Sieb darf in Rente.']),
    Q('m_insanium', 'Stufe 6: Insanium', 27, 0, item('mysticalagradditions:insanium_essence', 4), deps=['m_niemehr', 'z_elite'], rewards=[xp(100)],
      desc=['4 Supremium + 1 Ultimate-Schaltkreis (Mekanism) = 2 Insanium.',
            'Den Schaltkreis baust du aus Elite-Schaltkreisen und Atomlegierung. Weiter im Kapitel „Das Herz der Leere“.']),
])

# =====================================================================
# 9 Arkane Künste (Ars Nouveau)
# =====================================================================
ars = Chapter('ars', 'Arkane Künste', 'natur', 'ars_nouveau:novice_spell_book', sub='Magie, die Arbeit spart.', quests=[
    Q('a_quelle', 'Quellstein', 0, 0, item('ars_nouveau:source_gem', 8), deps=['e_eisen'], rewards=[xp(20)],
      desc=['Amethyst (aus dem Sieb) in der Imbuement Chamber wird zu Quellstein.']),
    Q('a_kammer', 'Imbuement Chamber', -3, 0, item('ars_nouveau:imbuement_chamber'), deps=['e_eisen'], rewards=[xp(15)]),
    Q('a_buch', 'Novizen-Zauberbuch', 3, 0, item('ars_nouveau:novice_spell_book'), deps=['a_quelle'], rewards=[xp(25)],
      desc=['C öffnet das Buch: Zauber aus Glyphen zusammenstecken.', 'Erster Tipp: Projektil + Abbauen = Fernabbau.']),
    Q('a_tisch', 'Schreibtisch', 6, -1.5, item('ars_nouveau:scribes_table'), deps=['a_buch'], rewards=[xp(20)], desc=['Hier lernst du neue Glyphen.']),
    Q('a_glas', 'Quellgefäß', 6, 1.5, [item('ars_nouveau:source_jar'), item('ars_nouveau:agronomic_sourcelink')], deps=['a_buch'], rewards=[xp(25)],
      desc=['Der Agronomic Sourcelink erzeugt Quelle aus wachsenden Pflanzen – perfekt neben deinen Feldern.']),
    Q('a_archwood', 'Archwood', 9, 1.5, item('ars_nouveau:blue_archwood_sapling'), deps=['a_glas'], rewards=[xp(25)],
      desc=['Archwood-Setzlinge kommen aus dem Moos-Sieb. Ihre Früchte sind Zutaten für Rituale.']),
    Q('a_starbuncle', 'Der magische Logistiker', 9, -1.5, item('ars_nouveau:starbuncle_charm'), deps=['a_tisch', 'l_controller'], shape=M, size=1.4,
      rewards=[crate('gold'), xp(60)],
      desc=['Ein Starbuncle trägt Items von A nach B – sichtbar statt in Rohren.',
            'Aufgabe: Lass ihn Funde von deinem Create-Depot in die Schubladen-Wand bringen. Goldnuggets machen ihn glücklich.']),
    Q('a_drygmy', 'Drygmy', 12, 1.5, item('ars_nouveau:drygmy_charm'), deps=['a_archwood'], rewards=[xp(40)],
      desc=['Drygmys holen Mob-Drops von Tieren und Monstern in der Nähe – ohne sie zu töten.']),
    Q('a_wilden', 'Wilden-Teile', 12, -1.5, [item('ars_nouveau:wilden_horn'), item('ars_nouveau:wilden_spike'), item('ars_nouveau:wilden_wing')],
      deps=['a_tisch'], rewards=[xp(30)], desc=['In der Leere gibt es keine Wilden – ihre Teile findest du im Gold-Sieb.']),
    Q('a_apparat', 'Verzauberungsapparat', 15, 0, [item('ars_nouveau:enchanting_apparatus'), item('ars_nouveau:arcane_core')], deps=['a_glas', 'a_tisch'], rewards=[xp(40)]),
    Q('a_ritual', 'Ritualbecken', 15, -3, item('ars_nouveau:ritual_brazier'), deps=['a_apparat'], rewards=[xp(30)]),
    # 0.5.0: Magie als echte Alternative zur Technik
    Q('a_crush', 'Der andere Weg: Zerkleinern', 9, -4, [item('ars_nouveau:glyph_crush'), item('ars_nouveau:basic_spell_turret')], deps=['a_tisch'],
      shape=M, size=1.3, rewards=[crate('eisen'), xp(40)],
      desc=['Die Glyphe „Crush“ macht aus Bruchstein Kies, aus Kies Sand und aus Sand Staub – genau wie der Hammer.',
            'Ein Zauberturm mit „Berühren + Crush“ vor einem Bruchstein-Generator zerkleinert von allein, mit Redstone-Takt.',
            'Alternative zum Mühlstein (Create) oder mechanischen Hammer – du musst nicht beides bauen.']),
    Q('a_wixie', 'Magisches Autocrafting', 18, -3, [item('ars_nouveau:wixie_charm'), item('ars_nouveau:wixie_cauldron')], deps=['a_apparat'],
      rewards=[crate('gold'), xp(50)],
      desc=['Eine Wixie am Kessel stellt ein Rezept immer wieder her, wenn Zutaten in Truhen daneben liegen.',
            'Für einfache Dinge (Fackeln, Bleche, Legierungen) ein früher Ersatz für AE2-Autocrafting. Für große Mengen bleibt AE2 stärker.']),
    Q('a_whirli', 'Whirlisprig', 9, 4, item('ars_nouveau:whirlisprig_charm'), deps=['a_glas'], rewards=[xp(30)],
      desc=['Der Whirlisprig lässt Pflanzen und Bäume in seiner Nähe schneller wachsen und erzeugt dabei Quelle.',
            'Gut neben Feldern und Botany Pots – eine magische Alternative zu Wachstumsbeschleunigern.']),
    Q('a_erzmagier', 'Erzmagier', 18, 0, item('ars_nouveau:archmage_spell_book'), deps=['a_apparat', 'a_wilden', 'a_drygmy'], shape=G, size=2.0,
      rewards=[crate('stern'), xp(150)],
      desc=['Das stärkste Zauberbuch. Magie ist ab jetzt kein Spielzeug mehr.']),
])

# =====================================================================
# 10 Bienenstaat (optional)
# =====================================================================
bienen = Chapter('bienen', 'Bienenstaat', 'natur', 'productivebees:advanced_oak_beehive', sub='Optional: Rohstoffe, die summen.', quests=[
    Q('b_biene', 'Die erste Biene', 0, 0, item('minecraft:bee_spawn_egg'), deps=['e_sieb'], rewards=[xp(20)],
      desc=['Bienen-Spawneier findest du beim Sieben von Moosblöcken.']),
    Q('b_stock', 'Fortgeschrittener Bienenstock', 3, 0, item('productivebees:advanced_oak_beehive'), deps=['b_biene'], rewards=[xp(25)],
      desc=['Produktiver als der normale Stock und mit Upgrades erweiterbar.']),
    Q('b_zentri', 'Zentrifuge', 6, 0, item('productivebees:centrifuge'), deps=['b_stock'], rewards=[xp(25)],
      desc=['Zerlegt Waben in Wachs, Honig und Rohstoffe.']),
    Q('b_nest', 'Nester bauen', 3, -2, item('productivebees:stone_nest'), deps=['b_stock'], rewards=[xp(20)], optional=True,
      desc=['In der Leere entstehen keine Nester – also selbst herstellen und hinstellen. Passende Wildbienen ziehen ein.']),
    Q('b_zucht', 'Ressourcen-Bienen', 9, 0, item('productivebees:honey_treat', 8), deps=['b_zentri'], shape=M, size=1.4, rewards=[crate('gold'), xp(60)],
      desc=['Mit Honigleckerlis und dem richtigen Block züchtest du Bienen, die Eisen, Kupfer und mehr liefern.',
            'JEI zeigt unter „Bienenzucht“, was geht.']),
    Q('b_upgrade', 'Produktivität', 12, 0, item('productivelib:upgrade_productivity'), deps=['b_zucht'], rewards=[xp(30)], optional=True),
])

# =====================================================================
# 11 Jenseits der Leere
# =====================================================================
jenseits = Chapter('jenseits', 'Jenseits der Leere', 'abenteuer', 'minecraft:obsidian', sub='Nether, End und der Drache.', quests=[
    Q('j_obsidian', 'Obsidian', 0, 0, item('minecraft:obsidian', 10), deps=['e_eisen'], rewards=[xp(20)],
      desc=['Wasser auf Lava-Quelle. Vorsicht beim Abbauen über der Leere!']),
    Q('j_nether', 'Ab in den Nether', 3, 0, dim('minecraft:the_nether'), deps=['j_obsidian'], rewards=[crate('eisen'), xp(40)],
      desc=['Auch der Nether ist leer – bis auf Netherfestungen. Die liegen frei in der Luft.']),
    Q('j_festung', 'Die Festung', 6, -1.5, item('minecraft:nether_bricks', 16), deps=['j_nether'], rewards=[xp(30)],
      desc=['Finde eine Netherfestung. Dort spawnen Lohen und Wither-Skelette.']),
    Q('j_lohe', 'Lohenruten', 9, -1.5, item('minecraft:blaze_rod', 8), deps=['j_festung'], rewards=[xp(30)],
      desc=['Für Brauen, Lohenbrenner (Create) und Enderaugen.']),
    Q('j_brenner', 'Superheizen', 12, -3, item('minecraft:blaze_rod', 16), deps=['j_lohe'], rewards=[xp(30)], optional=True,
      desc=['Mit Lohenkuchen (Create) wird der Brenner superheiß – für die besten Create-Rezepte.']),
    Q('j_hexe', 'Hexenwasser-Trick', 6, 1.5, item('minecraft:wither_skeleton_skull', 3), deps=['j_nether'], rewards=[xp(50)],
      desc=['Skelette, die in Hexenwasser (Ex Deorum) laufen, werden zu Wither-Skeletten.',
            'Drei Schädel für den Wither.']),
    Q('j_wither', 'Der Wither', 9, 1.5, item('minecraft:nether_star'), deps=['j_hexe'], shape=M, size=1.5, rewards=[crate('gold'), xp(100)],
      desc=['Bau ihn weit weg von deiner Insel. Sehr weit.']),
    Q('j_perlen', 'Enderperlen', 3, 3.5, item('minecraft:ender_pearl', 12), deps=['j_obsidian'], rewards=[xp(25)],
      desc=['Endermen spawnen nachts auf dunklen Plattformen – oder siebe Staub.']),
    Q('j_augen', 'Enderaugen', 6, 3.5, item('minecraft:ender_eye', 12), deps=['j_perlen', 'j_lohe'], rewards=[xp(25)]),
    Q('j_rahmen', 'Portalrahmen', 9, 3.5, item('minecraft:end_portal_frame', 12), deps=['j_augen'], rewards=[xp(40)],
      desc=['Ohne Festungen in der Leere stellst du die Rahmen selbst her: Obsidian, Enderauge, Endstein.']),
    Q('j_end', 'Das End', 12, 3.5, dim('minecraft:the_end'), deps=['j_rahmen'], rewards=[xp(50)]),
    Q('j_drache', 'Drachentöter', 15, 3.5, kill('minecraft:ender_dragon'), deps=['j_end'], shape=G, size=2.0, icon='minecraft:dragon_head',
      rewards=[crate('stern'), xp(200)],
      desc=['Die End-Hauptinsel ist da, mit Türmen und Kristallen. Viel Glück.']),
    Q('j_shulker', 'Shulker-Schalen', 15, 1, item('minecraft:shulker_shell', 2), deps=['j_end'], rewards=[xp(30)], optional=True,
      desc=['Keine Endstädte in der Leere: Shulker-Schalen gibt es im Diamant- oder Netherit-Sieb aus zerkleinertem Endstein.']),
])

# =====================================================================
# 12 Maschinengeist (HNN + IF)
# =====================================================================
geist = Chapter('geist', 'Maschinengeist', 'abenteuer', 'hostilenetworks:deep_learner', sub='Mobs simulieren statt jagen.', quests=[
    Q('h_learner', 'Deep Learner', 0, 0, item('hostilenetworks:deep_learner'), deps=['s_stahl'], rewards=[xp(25)],
      desc=['Hostile Neural Networks: Der Deep Learner trainiert Datenmodelle, während du kämpfst.']),
    Q('h_modell', 'Erstes Datenmodell', 3, 0, item('hostilenetworks:blank_data_model', 2), deps=['h_learner'], rewards=[xp(20)],
      desc=['Rechtsklick auf einen Mob bindet das Modell an seine Art.']),
    Q('h_sim', 'Simulationskammer', 6, -1.5, [item('hostilenetworks:sim_chamber'), item('hostilenetworks:prediction_matrix', 16)], deps=['h_modell'], rewards=[xp(40)],
      desc=['Simuliert Kämpfe mit Strom und erzeugt Vorhersagen.']),
    Q('h_fab', 'Beute-Fabrikator', 9, -1.5, item('hostilenetworks:loot_fabricator'), deps=['h_sim'], rewards=[crate('gold'), xp(40)],
      desc=['Macht aus Vorhersagen echte Drops: Enderperlen, Lohenruten, Knochen …']),
    Q('h_boss', 'Jagd ohne Jagd', 12, -1.5, check(), deps=['h_fab', 'j_wither'], shape=G, size=2.0, icon='minecraft:wither_skeleton_skull',
      rewards=[crate('stern'), xp(150)],
      desc=['Trainiere ein Boss-Modell (z. B. Wither) bis zur höchsten Stufe.', 'Haken setzen, wenn es „Self Aware“ ist.']),
    Q('h_rahmen', 'Maschinenrahmen', 3, 2.5, item('industrialforegoing:machine_frame_pity'), deps=['s_stahl'], rewards=[xp(20)],
      desc=['Industrial Foregoing beginnt mit Latex aus Bäumen und Plastik.']),
    Q('h_plastik', 'Plastik', 6, 2.5, item('industrialforegoing:plastic', 16), deps=['h_rahmen'], rewards=[xp(25)]),
    Q('h_laser', 'Laserbohrer', 9, 2.5, [item('industrialforegoing:ore_laser_base'), item('industrialforegoing:laser_drill', 4)], deps=['h_plastik'],
      shape=M, size=1.4, rewards=[crate('gold'), xp(60)],
      desc=['Bohrt Erz aus dem Nichts. Farbige Linsen bevorzugen bestimmte Erze.']),
])

# =====================================================================
# 13 Baumeister (optional)
# =====================================================================
bau = Chapter('bau', 'Baumeister', 'freizeit', 'rechiseled:chisel', sub='Optional: schön statt nur praktisch.', quests=[
    Q('u_meissel', 'Meißel', 0, 0, item('rechiseled:chisel'), deps=['e_eisen'], rewards=[xp(15)],
      desc=['Rechiseled: Ein Block, viele Muster. Verbundene Texturen inklusive.']),
    Q('u_haus', 'Ein Dach über dem Kopf', 3, -1.5, check(), deps=['u_meissel'], icon='mcwroofs:oak_roof', rewards=[crate('holz'), xp(30)],
      desc=['Bau dir ein richtiges Haus. Macaw\'s Roofs, Doors und Windows helfen.']),
    Q('u_moebel', 'Einrichten', 6, -1.5, check(), deps=['u_haus'], icon='handcrafted:oak_chair', rewards=[xp(30)],
      desc=['Handcrafted und Macaw\'s Furniture: Stühle, Tische, Regale.']),
    Q('u_bruecke', 'Brücke ins Nichts', 3, 1.5, check(), deps=['u_meissel'], icon='mcwbridges:rope_oak_bridge', rewards=[xp(30)],
      desc=['Verbinde zwei Inselteile mit einer Brücke.']),
    Q('u_garten', 'Garten', 6, 1.5, check(), deps=['u_bruecke'], icon='minecraft:poppy', rewards=[xp(30)],
      desc=['Blumen, Wege (Macaw\'s Paths), Laternen (Macaw\'s Lights).']),
    Q('u_framed', 'Rahmenblöcke', 9, -1.5, item('framedblocks:framed_cube', 8), deps=['u_moebel'], rewards=[xp(20)],
      desc=['FramedBlocks nehmen das Aussehen jedes Blocks an.']),
    Q('u_gadget', 'Bau-Gadget', 9, 1.5, item('buildinggadgets2:gadget_building'), deps=['u_garten', 's_draht'], rewards=[xp(40)],
      desc=['Baut ganze Flächen auf einmal. Braucht Strom.']),
    Q('u_meister', 'Inselarchitekt', 12, 0, check(), deps=['u_framed', 'u_gadget'], shape=G, size=1.8, icon='minecraft:bricks',
      rewards=[crate('gold'), xp(80)], desc=['Wenn deine Insel schöner ist als nötig: Haken setzen.']),
])

# =====================================================================
# 14 Herr der Leere (Endgame)
# =====================================================================
ende = Chapter('ende', 'Das Herz der Leere', 'freizeit', 'mekanism:pellet_antimatter', sub='Das Finale: Erbe der Ewigkeit.', quests=[
    Q('z_elite', 'Elite-Schaltkreis', 0, 0, item('mekanism:elite_control_circuit', 4), deps=['k_inject'], rewards=[xp(40)]),
    Q('z_ultimate', 'Ultimate-Rohre', 3, -1.5, item('pipez:ultimate_upgrade'), deps=['z_elite', 'l_prozessoren'], rewards=[xp(40)]),
    Q('z_strom', 'Großkraftwerk', 3, 1.5, item('powah:reactor_hardened', 36), deps=['s_reaktor', 'z_elite'], rewards=[crate('gold'), xp(80)],
      desc=['Vor der Antimaterie: Ein großer Reaktor, sonst wartest du ewig.']),
    Q('z_insanium', 'Insanium-Ernte', 6, -1.5, item('mysticalagradditions:insanium_essence', 32), deps=['m_insanium'], rewards=[xp(80)],
      desc=['Insanium braucht neben Supremium einen Ultimate-Schaltkreis (Mekanism): 4 Supremium + 1 Schaltkreis = 2 Insanium.',
            'Tipp: Lass AE2 die Schaltkreise automatisch bauen.']),
    Q('z_netherstern', 'Netherstern-Samen', 9, -1.5, item('mysticalagriculture:nether_star_seeds'), deps=['z_insanium', 'j_wither'], rewards=[crate('stern'), xp(100)],
      desc=['Nethersterne wachsen jetzt auf dem Feld.']),
    Q('z_sps', 'Antimaterie', 6, 1.5, item('mekanism:pellet_antimatter'), deps=['z_strom', 'l_auto'], shape=M, size=1.5, rewards=[crate('stern'), xp(150)],
      desc=['Polonium im SPS. Ein einziges Pellet reicht.']),
    Q('z_meka', 'Mekasuit', 9, 1.5, item('mekanism:mekasuit_bodyarmor'), deps=['z_sps'], rewards=[xp(100)], optional=True),
    Q('z_fabrik', 'Die ewige Fabrik', 9, 4.5,
      [item('mekanism:ultimate_control_circuit', 4), item('mysticalagriculture:supremium_essence', 32), item('minecraft:nether_star', 2)],
      deps=['z_netherstern', 'z_sps', 'l_auto'], shape=M, size=1.6, rewards=[crate('stern'), xp(200)],
      desc=['Zeig, dass alles zusammenläuft: Schaltkreise aus Mekanism, Supremium vom Feld, Nethersterne aus der Netherstern-Saat.',
            'Die Items werden nur vorgezeigt, nicht verbraucht. Wenn dein ME-Netz sie von allein nachbaut, hast du es geschafft.']),
    Q('z_versiegeln', 'Versiegeln statt beherrschen', 15, 3, check(), deps=['z_fabrik'], optional=True, icon='minecraft:crying_obsidian',
      rewards=[xp(150)],
      desc=['Optionale Herausforderung: Bau deine komplette Endgame-Anlage (Antimaterie, Netherstern-Feld, ME-Netz) auf höchstens 16×16 Blöcken.',
            'Selbst prüfen und Haken setzen. Die Erbauer haben es nicht geschafft, sich zu begrenzen. Du schon?']),
    Q('z_herr', 'Erbe der Ewigkeit', 12, 0, check(), deps=['z_fabrik', 'j_drache', 'm_niemehr', 'a_erzmagier'], shape=G, size=3.0,
      icon='minecraft:dragon_egg', rewards=[crate('stern'), crate('stern'), xp(500)],
      desc=['&oDie letzte Seite des Wächters: „Wer das Herz der Leere wieder schlagen lässt, trägt unser Erbe. Nimm nur, was du brauchst.“',
            '',
            'Maschinen, Magie und Felder arbeiten zusammen, und das Herz der Leere schlägt wieder ruhig.',
            'Aus einer Insel mit einem Baum ist eine Welt geworden. Danke fürs Spielen von Sky and Stone!']),
])

# =====================================================================
# 15 Inselmarkt – wiederholbare Tauschgeschäfte (Gemini-Loop Etappe 1)
# =====================================================================
TAG = 1200            # ein Minecraft-Tag in Sekunden
def tausch(key, title, x, y, it, n, kiste, cd, deps, desc):
    return Q(key, title, x, y, item(it, n, consume=True), deps=deps, rewards=[crate(kiste, team=True)], repeat=cd, icon=it,
             shape='rsquare', desc=[desc, '', (f'Wiederholbar: einmal alle {cd // TAG} Minecraft-Tage.' if cd >= 2 * TAG else 'Wiederholbar: einmal pro Minecraft-Tag.') if cd >= TAG else ''])

markt = Chapter('markt', 'Inselmarkt', 'freizeit', 'minecraft:emerald', sub='Überschuss gegen Kisten tauschen.', quests=[
    Q('x_markt', 'Der Inselmarkt', 0, 0, check(), deps=['e_eisen'], shape=G, size=1.6, icon='minecraft:emerald', rewards=[xp(10)],
      desc=['Hier tauschst du, was sich bei dir stapelt, gegen Beutekisten.',
            'Die Items werden beim Abgeben verbraucht. Jeder Tausch hat eine Abklingzeit – so bleibt es fair.',
            '',
            'Kisten fallen übrigens auch selten von Monstern (auch in Farmen), Bosse lassen immer eine Gold- oder Sternkiste fallen.']),
    # Holz
    tausch('x_samen', 'Saatgut-Händler', 3, -3, 'minecraft:wheat_seeds', 256, 'holz', TAG, ['x_markt'], 'Zu viele Samen aus dem Sieb?'),
    tausch('x_kies', 'Kieshändler', 4.5, -3, 'minecraft:gravel', 256, 'holz', TAG, ['x_markt'], 'Kies hast du immer.'),
    tausch('x_cobble', 'Steinbruch', 6, -3, 'minecraft:cobblestone', 512, 'holz', TAG, ['x_markt'], 'Der Bruchstein-Generator läuft und läuft.'),
    tausch('x_fleisch', 'Zombie-Abfall', 7.5, -3, 'minecraft:rotten_flesh', 128, 'holz', TAG, ['x_markt'], 'Verrottetes Fleisch, ehrlich gesagt zu nichts gut.'),
    tausch('x_inferium', 'Essenz-Überschuss', 9, -3, 'mysticalagriculture:inferium_essence', 256, 'holz', TAG, ['x_markt', 'm_inferium'], 'Inferium wächst schneller, als du es brauchst.'),
    # Eisen
    tausch('x_mehl', 'Müllerei', 3, -1, 'create:wheat_flour', 256, 'eisen', TAG, ['x_markt', 'c_muehle'], 'Mehl aus dem Mühlstein.'),
    tausch('x_seetang', 'Seetang-Kraftwerk', 4.5, -1, 'minecraft:dried_kelp_block', 64, 'eisen', TAG, ['x_markt'], 'Getrockneter Seetang in Blöcken.'),
    tausch('x_honig', 'Imkerei', 6, -1, 'minecraft:honeycomb', 64, 'eisen', TAG, ['x_markt', 'b_stock'], 'Waben aus dem Bienenstock.'),
    tausch('x_warze', 'Netherwarzen-Farm', 7.5, -1, 'minecraft:nether_wart', 128, 'eisen', TAG, ['x_markt'], 'Netherwarzen wachsen auf Seelensand.'),
    tausch('x_knochen', 'Knochensammler', 9, -1, 'minecraft:bone', 128, 'eisen', TAG, ['x_markt'], 'Skelette und Fischfang.'),
    # Gold
    tausch('x_perlen', 'Enderhandel', 3, 1, 'minecraft:ender_pearl', 32, 'gold', 2 * TAG, ['x_markt', 'j_perlen'], 'Enderperlen aus Farm oder Simulation.'),
    tausch('x_lohe', 'Lohenruten-Handel', 4.5, 1, 'minecraft:blaze_rod', 32, 'gold', 2 * TAG, ['x_markt', 'j_lohe'], 'Lohenruten im Überfluss.'),
    tausch('x_quelle', 'Quellstein-Handel', 6, 1, 'ars_nouveau:source_gem', 32, 'gold', 2 * TAG, ['x_markt', 'a_quelle'], 'Quellsteine, die sich stapeln.'),
    # Stern
    tausch('x_polonium', 'Strahlender Handel', 3, 3, 'mekanism:pellet_polonium', 4, 'stern', 3 * TAG, ['x_markt', 'k_inject'], 'Polonium aus dem Fissionsreaktor oder dem Isotopen-Zentrifugen-Weg.'),
    tausch('x_stern', 'Sternenhandel', 4.5, 3, 'minecraft:nether_star', 1, 'stern', 3 * TAG, ['x_markt', 'j_wither'], 'Ein Netherstern gegen eine Sternkiste.'),
    tausch('x_antimaterie', 'Antimaterie-Handel', 6, 3, 'mekanism:pellet_antimatter', 1, 'stern', 3 * TAG, ['x_markt', 'z_sps'], 'Das teuerste Pellet der Welt.'),
    tausch('x_supremium', 'Supremium-Handel', 7.5, 3, 'mysticalagriculture:supremium_essence', 32, 'stern', 3 * TAG, ['x_markt', 'm_supremium'], 'Supremium vom Feld.'),
    tausch('x_mechanik', 'Feinmechanik', 7.5, 1, 'create:precision_mechanism', 16, 'gold', 2 * TAG, ['x_markt', 'c_mechanismus'], 'Präzisionsmechanismen vom Fließband.'),
])

# =====================================================================
# 16 Prüfungen der Leere (0.5.0, alles optional)
# Haken-Quests, weil sich Bauformen nicht zuverlässig prüfen lassen: klare Regel, selbst prüfen.
# =====================================================================
pruefungen = Chapter('pruefungen', 'Prüfungen der Leere', 'freizeit', 'minecraft:spyglass', sub='Optional: für Ingenieure, Sammler und Mutige.', quests=[
    Q('p_start', 'Die Prüfungen', 0, 0, check(), deps=['e_eisen'], shape=G, size=1.6, icon='minecraft:spyglass', optional=True, rewards=[xp(10)],
      desc=['Alles hier ist freiwillig. Die Prüfungen haben Regeln, die du selbst kontrollierst: Ehrlich sein lohnt sich nur für dich.']),
    # Ingenieursprüfungen
    Q('p_kompakt', 'Kompakte Siebfabrik', 3, -3, check(), deps=['p_start', 'c_siebfabrik'], optional=True, icon='createsifter:sifter',
      rewards=[crate('gold'), xp(80)],
      desc=['Baue eine Siebfabrik (Bruchstein rein, Barren raus) in einem Würfel von höchstens 7×7×7 Blöcken.']),
    Q('p_ohnebrenn', 'Strom ohne Brennstoff', 6, -3, check(), deps=['p_start', 's_reaktor'], optional=True, icon='powah:solar_panel_basic',
      rewards=[crate('gold'), xp(80)],
      desc=['Versorge mindestens 5 Maschinen einen ganzen Minecraft-Tag lang nur mit Sonne, Wind, Wasser oder Reaktor – ohne Kohle, Holz oder Lava nachzulegen.']),
    Q('p_ohnerohr', 'Fabrik ohne Rohre', 9, -3, check(), deps=['p_start', 'a_starbuncle'], optional=True, icon='ars_nouveau:starbuncle_charm',
      rewards=[crate('gold'), xp(80)],
      desc=['Eine Produktionskette, die nur mit Förderbändern, Trichtern und Starbuncles auskommt – kein einziges Pipez- oder Mekanism-Rohr.']),
    Q('p_vierfach', 'Vollautomatisches Vierfach-Erz', 12, -3, check(), deps=['p_start', 'k_inject'], optional=True, icon='mekanism:chemical_injection_chamber',
      rewards=[crate('gold'), xp(100)],
      desc=['Erz rein, viermal so viele Barren raus – ohne dass du eine Maschine anfasst. Auch die Gase (Sauerstoff, Chlorwasserstoff) kommen von selbst.']),
    # Herausforderungen der Leere
    Q('p_nether', 'Inselbau im Nether', 3, 0, check(), deps=['p_start', 'j_nether'], optional=True, icon='minecraft:netherrack',
      rewards=[crate('eisen'), xp(60)],
      desc=['Baue im Nether eine kleine Außenstation mit Bett-Ersatz (Seelenanker oder Wegstein), Licht und Lager. Ohne Lavasturz.']),
    Q('p_ohnesieb', 'Kein Handsieb mehr', 6, 0, check(), deps=['p_start', 'm_eisen'], optional=True, icon='exdeorum:oak_sieve',
      rewards=[crate('eisen'), xp(60)],
      desc=['Schaff den Weg vom ersten Eisen-Samen bis zur Infused Alloy, ohne noch einmal ein Handsieb zu benutzen.']),
    Q('p_wither', 'Wither ohne Rüstung', 9, 0, check(), deps=['p_start', 'j_wither'], optional=True, icon='minecraft:wither_skeleton_skull',
      rewards=[crate('stern'), xp(120)],
      desc=['Besiege den Wither ohne Rüstung. Fallen, Zauber und Geschütze sind erlaubt.']),
    # Sammlerbuch
    Q('p_essenzen', 'Sammlerbuch: Alle Essenzen', 3, 3,
      [item('mysticalagriculture:inferium_essence'), item('mysticalagriculture:prudentium_essence'), item('mysticalagriculture:tertium_essence'),
       item('mysticalagriculture:imperium_essence'), item('mysticalagriculture:supremium_essence'), item('mysticalagradditions:insanium_essence')],
      deps=['p_start'], optional=True, icon='mysticalagriculture:supremium_essence', rewards=[crate('gold'), xp(80)],
      desc=['Je eine Essenz jeder Stufe. Die Reihe erzählt deinen Weg: Feld, Create, Mekanism, AE2, Endgame.']),
    Q('p_netze', 'Sammlerbuch: Alle Netze', 6, 3,
      [item('exdeorum:string_mesh'), item('exdeorum:flint_mesh'), item('exdeorum:iron_mesh'), item('exdeorum:golden_mesh'),
       item('exdeorum:diamond_mesh'), item('exdeorum:netherite_mesh')],
      deps=['p_start'], optional=True, icon='exdeorum:netherite_mesh', rewards=[crate('eisen'), xp(60)],
      desc=['Vom Faden bis zum Netherit: Jedes Netz siebt andere Schätze.']),
    Q('p_archwood', 'Sammlerbuch: Archwood', 9, 3,
      [item('ars_nouveau:blue_archwood_sapling'), item('ars_nouveau:red_archwood_sapling'), item('ars_nouveau:purple_archwood_sapling'),
       item('ars_nouveau:green_archwood_sapling')],
      deps=['p_start', 'a_archwood'], optional=True, icon='ars_nouveau:green_archwood_sapling', rewards=[crate('eisen'), xp(60)],
      desc=['Alle vier Archwood-Arten. Ihre Früchte sind Zutaten für Rituale.']),
    Q('p_trophaeen', 'Sammlerbuch: Trophäen', 12, 3,
      [item('minecraft:nether_star'), item('minecraft:dragon_egg'), item('minecraft:wither_skeleton_skull'), item('minecraft:totem_of_undying')],
      deps=['p_start', 'j_drache'], optional=True, icon='minecraft:dragon_egg', rewards=[crate('stern'), xp(100)],
      desc=['Netherstern, Drachenei, Wither-Schädel und ein Totem (aus Sternkisten). Stell sie irgendwo schön aus.']),
])

# =====================================================================
# Story „Das Herz der Leere“ – kurze Lore-Zeilen oben in Meilensteinen (0.5.0)
# =====================================================================
LORE = {
    'w_start':      'Notiz des letzten Wächters: „Wer das liest, steht auf einem Splitter unserer Welt. Darunter schläft das Herz der Leere.“',
    'e_sieb':       '„Wir siebten einst Sternenstaub. Jetzt siebst du Kies – es ist derselbe Anfang.“',
    'e_eisen':      '„Das erste Metall. Die Erbauer nannten es den Funken.“',
    'g_autark':     '„Eine Insel, die sich selbst nährt, ist der erste Schritt zurück.“',
    'c_siebfabrik': '„Unsere Maschinen arbeiteten Tag und Nacht. Du hast gerade die erste wieder geweckt.“',
    's_reaktor':    '„Wir nahmen die Kraft aus der Leere, nicht aus Kohle. Zu viel davon zerriss den Boden.“',
    'k_inject':     '„Aus jedem Brocken das Vierfache. So reich waren wir – und so gierig.“',
    'l_auto':       '„Unsere Netze dachten mit. Am Ende dachten sie schneller als wir.“',
    'm_niemehr':    '„Die Felder wuchsen Erz, als die Minen versiegt waren. Wenigstens das haben wir richtig gemacht.“',
    'a_erzmagier':  '„Maschine und Magie waren für uns nie Gegensätze. Erst zusammen erreichten sie das Herz.“',
    'j_nether':     '„Auch die Unterwelt zerbrach. Unsere Festungen hängen dort noch in der Luft.“',
    'j_drache':     '„Der Drache bewachte das Ende, nicht für uns, sondern vor uns.“',
    'h_boss':       '„Wir lernten unsere Feinde auswendig, bis wir sie nicht mehr bekämpfen mussten.“',
    'z_sps':        '„Antimaterie: der Herzschlag der Leere in einer Kapsel. Behandle sie mit Respekt.“',
}

def apply_lore(chapters):
    for c in chapters:
        for q in c.quests:
            if q.key in LORE and not (q.desc and q.desc[0].startswith('&o')):
                q.desc = ['&o' + LORE[q.key], ''] + q.desc

```

## Datei: _src/inseln.py
```py
"""Sky and Stone – erzeugt die wählbaren Startinseln für Skyblock Builder.

Aufruf:  python -I _src/inseln.py   (aus dem Pack-Ordner)
Ergebnis: config/skyblockbuilder/templates/islands/*.nbt + templates.json5
"""
import gzip, io, json, math, os, random, struct, sys
from collections import deque

DATA_VERSION = 3955  # Minecraft 1.21.1
PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(PACK, 'config', 'skyblockbuilder', 'templates', 'islands')

# ---------------- NBT ----------------
class Int(int): pass
class Byte(int): pass    # 0.10.0: für Block-Daten (Schild)
class TList(list):
    def __init__(self, tag, items): super().__init__(items); self.tag = tag

def _w_payload(buf, tag, v):
    if tag == 1: buf.write(struct.pack('>b', v))
    elif tag == 3: buf.write(struct.pack('>i', v))
    elif tag == 8:
        b = v.encode('utf-8'); buf.write(struct.pack('>H', len(b))); buf.write(b)
    elif tag == 9:
        buf.write(struct.pack('>bi', v.tag if len(v) else 0, len(v)))
        for x in v: _w_payload(buf, v.tag, x)
    elif tag == 10:
        for k, x in v.items():
            t = _tag(x); buf.write(struct.pack('>b', t)); _w_payload(buf, 8, k); _w_payload(buf, t, x)
        buf.write(b'\x00')
    else: raise ValueError(tag)

def _tag(v):
    if isinstance(v, TList): return 9
    if isinstance(v, Byte): return 1
    if isinstance(v, dict): return 10
    if isinstance(v, str): return 8
    if isinstance(v, int): return 3
    raise TypeError(type(v))

def write_nbt(path, root):
    buf = io.BytesIO(); buf.write(b'\x0a'); _w_payload(buf, 8, ''); _w_payload(buf, 10, root)
    with gzip.open(path, 'wb') as f: f.write(buf.getvalue())

# ---------------- Insel-Baukasten ----------------
LEAF_TYPES = ('leaves',)

class Island:
    def __init__(self, name):
        self.name = name; self.blocks = {}; self.nbt = {}   # nbt: Block-Daten je Position (Schild)
    def set(self, x, y, z, block, **props):
        self.blocks[(x, y, z)] = (block if ':' in block else 'minecraft:' + block, props)
    def get(self, x, y, z):
        b = self.blocks.get((x, y, z)); return b[0] if b else None
    def setif_air(self, x, y, z, block, **props):
        if (x, y, z) not in self.blocks: self.set(x, y, z, block, **props)

    # Rundes Inselstück: Oberfläche top, darunter filler, nach unten spitz zulaufend
    def disc(self, cx, cz, r, ytop, top, filler, depth, under='stone', seed=1):
        rnd = random.Random(seed)
        for x in range(cx - r - 1, cx + r + 2):
            for z in range(cz - r - 1, cz + r + 2):
                d = math.hypot(x - cx, z - cz)
                if d > r + 0.4: continue
                edge = d > r - 0.8
                if edge and rnd.random() < 0.35: continue
                col_depth = max(1, int(round(depth * (1 - (d / (r + 0.5)) ** 1.6))) + rnd.choice((0, 0, 1)))
                for i in range(col_depth):
                    y = ytop - i
                    blk = top if i == 0 else (filler if i <= 2 else under)
                    self.set(x, y, z, blk, **({'snowy': 'false'} if blk.endswith(('grass_block', 'mycelium', 'podzol')) else {}))

    def oak(self, x, y, z, log='oak_log', leaves='oak_leaves', h=5):
        for i in range(h): self.set(x, y + i, z, log, axis='y')
        top = y + h - 1
        for dy, r in ((-2, 2), (-1, 2), (0, 1), (1, 1)):
            for dx in range(-r, r + 1):
                for dz in range(-r, r + 1):
                    if r == 2 and abs(dx) == 2 and abs(dz) == 2: continue
                    if r == 1 and dy == 1 and abs(dx) + abs(dz) == 2: continue
                    self.setif_air(x + dx, top + dy, z + dz, leaves)

    def palm(self, x, y, z):
        for i in range(6): self.set(x + (1 if i >= 4 else 0), y + i, z, 'jungle_log', axis='y')
        tx, ty = x + 1, y + 6
        self.set(tx, ty, z, 'jungle_leaves')
        for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            for k in (1, 2):
                self.setif_air(tx + dx * k, ty - (1 if k == 2 else 0), z + dz * k, 'jungle_leaves')
        for dx, dz in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
            self.setif_air(tx + dx, ty, z + dz, 'jungle_leaves')

    def cherry(self, x, y, z):
        for i in range(4): self.set(x, y + i, z, 'cherry_log', axis='y')
        for i, (dx, dz) in enumerate(((1, 0), (-1, 0))):
            self.set(x + dx, y + 4, z, 'cherry_log', axis='x'); self.set(x + 2 * dx, y + 5, z, 'cherry_log', axis='y')
        for cx in (x - 2, x + 2):
            for dy, r in ((5, 2), (6, 2), (7, 1)):
                for dx in range(-r, r + 1):
                    for dz in range(-r, r + 1):
                        if abs(dx) == r and abs(dz) == r: continue
                        self.setif_air(cx + dx, y + dy, z + dz, 'cherry_leaves')

    def mushroom(self, x, y, z):
        for i in range(5): self.set(x, y + i, z, 'mushroom_stem', up='false', down='false', north='true', south='true', east='true', west='true')
        for dx in range(-3, 4):
            for dz in range(-3, 4):
                if abs(dx) == 3 and abs(dz) == 3: continue
                self.set(x + dx, y + 5, z + dz, 'brown_mushroom_block', up='true', down='false',
                         north=str(dz == -3 or (abs(dx) == 3 and dz == -2)).lower(), south=str(dz == 3 or (abs(dx) == 3 and dz == 2)).lower(),
                         west=str(dx == -3 or (abs(dz) == 3 and dx == -2)).lower(), east=str(dx == 3 or (abs(dz) == 3 and dx == 2)).lower())

    def finish_leaves(self):
        """Blätter: distance per Breitensuche vom nächsten Stamm, damit sie korrekt zerfallen."""
        dist = {}; q = deque()
        for p, (b, _) in self.blocks.items():
            if b.endswith('_log') or b.endswith('_stem') and 'mushroom' not in b:
                dist[p] = 0; q.append(p)
        while q:
            p = q.popleft()
            for d in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
                n = (p[0]+d[0], p[1]+d[1], p[2]+d[2])
                b = self.blocks.get(n)
                if b and b[0].endswith('_leaves') and n not in dist and dist[p] < 7:
                    dist[n] = dist[p] + 1; q.append(n)
        for p, (b, props) in list(self.blocks.items()):
            if b.endswith('_leaves'):
                d = dist.get(p)
                self.blocks[p] = (b, {'distance': str(d if d else 7), 'persistent': 'false' if d else 'true', 'waterlogged': 'false'})

    def save(self, spawn_rel):
        self.finish_leaves()
        xs = [p[0] for p in self.blocks]; ys = [p[1] for p in self.blocks]; zs = [p[2] for p in self.blocks]
        mn = (min(xs), min(ys), min(zs)); size = (max(xs) - mn[0] + 1, max(ys) - mn[1] + 1, max(zs) - mn[2] + 1)
        palette, pidx, blocks = [], {}, []
        for p, (b, props) in sorted(self.blocks.items()):
            key = (b, tuple(sorted(props.items())))
            if key not in pidx:
                pidx[key] = len(palette)
                e = {'Name': b}
                if props: e['Properties'] = {k: str(v) for k, v in props.items()}
                palette.append(e)
            e = {'pos': TList(3, [Int(p[0]-mn[0]), Int(p[1]-mn[1]), Int(p[2]-mn[2])]), 'state': Int(pidx[key])}
            if p in self.nbt: e['nbt'] = self.nbt[p]
            blocks.append(e)
        root = {'DataVersion': Int(DATA_VERSION), 'size': TList(3, [Int(s) for s in size]),
                'palette': TList(10, palette), 'blocks': TList(10, blocks), 'entities': TList(10, [])}
        write_nbt(os.path.join(OUT, self.name + '.nbt'), root)
        sp = [spawn_rel[0] - mn[0], spawn_rel[1] - mn[1], spawn_rel[2] - mn[2]]
        return size, sp, len(blocks)

# ---------------- Spuren der Erbauer (0.10.0) ----------------
SCHILD = ['Hier wachte', 'der letzte', 'Wächter.', 'Folge dem Buch.']
def ruine(i, spawn):
    """Kleine verfallene Säule mit Schild am Inselrand: Stelle möglichst weit vom Spawn, ohne Baum darüber."""
    oben = {}
    for (x, y, z), (b, _) in i.blocks.items():
        if b.endswith(('grass_block', 'dirt', 'sand', 'mycelium', 'podzol', 'stone', 'moss_block', 'coarse_dirt')):
            if (x, z) not in oben or y > oben[(x, z)]: oben[(x, z)] = y
    def frei(x, y, z):
        return all((x + dx, y + dy, z + dz) not in i.blocks for dx in (-1, 0, 1) for dz in (-1, 0, 1) for dy in (1, 2, 3))
    kand = [(x, y, z) for (x, z), y in oben.items() if (x, y, z) in i.blocks and frei(x, y, z)
            and all((x + dx, z + dz) in oben for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
    if not kand:   # zerklüftete Insel: ohne Nachbar-Bedingung, dafür muss das Schildfeld frei sein
        kand = [(x, y, z) for (x, z), y in oben.items() if (x, y, z) in i.blocks and frei(x, y, z)]
    if not kand: return None
    x, y, z = max(kand, key=lambda p: ((p[0] - spawn[0]) ** 2 + (p[2] - spawn[2]) ** 2, p))
    i.set(x, y + 1, z, 'mossy_stone_bricks'); i.set(x, y + 2, z, 'cracked_stone_bricks')
    i.set(x, y + 3, z, 'mossy_stone_brick_slab', type='bottom', waterlogged='false')
    # Schild auf der dem Spawn zugewandten Seite, Blick zum Spawn
    dx, dz = spawn[0] - x, spawn[2] - z
    sx, sz = (x + (1 if dx > 0 else -1), z) if abs(dx) >= abs(dz) else (x, z + (1 if dz > 0 else -1))
    rot = {(0, 1): 0, (-1, 0): 4, (0, -1): 8, (1, 0): 12}[(sx - x, sz - z)]
    i.set(sx, y + 1, sz, 'oak_sign', rotation=str(rot), waterlogged='false')
    txt = lambda zeilen: {'messages': TList(8, [json.dumps({'text': t}, ensure_ascii=False) for t in zeilen]),
                          'color': 'black', 'has_glowing_text': Byte(0)}
    i.nbt[(sx, y + 1, sz)] = {'id': 'minecraft:sign', 'front_text': txt(SCHILD), 'back_text': txt(['', '', '', '']),
                              'is_waxed': Byte(1)}
    return (sx, y + 1, sz)

# ---------------- Die Inseln ----------------
def klassisch():
    i = Island('klassisch')  # das L aus SkyBlock 2.1 – drei Schichten
    for x in range(6):
        for z in range(3):
            for y in range(3): i.set(x, y, z, 'grass_block' if y == 2 else 'dirt', **({'snowy': 'false'} if y == 2 else {}))
    for x in range(3):
        for z in range(3, 6):
            for y in range(3): i.set(x, y, z, 'grass_block' if y == 2 else 'dirt', **({'snowy': 'false'} if y == 2 else {}))
    i.set(5, 2, 0, 'dirt'); i.oak(5, 3, 0)
    i.set(1, 0, 4, 'bedrock')
    return i, (2, 3, 1)

def lichtung():
    i = Island('lichtung')  # Waldlichtung mit Teich
    i.disc(0, 0, 6, 0, 'grass_block', 'dirt', 6, seed=3)
    i.oak(-3, 1, -2); i.oak(3, 1, 2, log='birch_log', leaves='birch_leaves', h=6)
    for x, z in ((1, -2), (2, -2), (1, -3)): i.set(x, 0, z, 'water', level='0')
    for x, z, f in ((-1, 3, 'poppy'), (0, 4, 'dandelion'), (-4, 1, 'cornflower'), (2, 4, 'short_grass'), (-2, -4, 'short_grass'), (4, -1, 'oxeye_daisy')):
        i.set(x, 1, z, f)
    i.set(-3, 0, 3, 'coarse_dirt'); i.set(0, 0, 0, 'grass_block', snowy='false')
    return i, (0, 1, 0)

def oase():
    i = Island('oase')  # Wüsten-Oase: Sand, Palme, Zuckerrohr, Kakteen
    i.disc(0, 0, 6, 0, 'sand', 'sandstone', 5, under='sandstone', seed=7)
    for x, z in ((0, 0), (1, 0), (0, 1), (1, 1)): i.set(x, 0, z, 'water', level='0'); i.set(x, -1, z, 'sand')
    for x, z in ((-1, 0), (-1, 1), (2, 0), (2, 1), (0, -1), (1, 2)): i.set(x, 0, z, 'grass_block', snowy='false')
    for x, z in ((-1, 0), (2, 1)): i.set(x, 1, z, 'sugar_cane', age='0')
    i.palm(-3, 1, -3); i.set(-3, 0, -3, 'dirt')
    for x, z in ((4, -2), (-4, 3)): i.set(x, 1, z, 'cactus', age='0')
    i.set(3, 1, 3, 'dead_bush')
    return i, (0, 1, -2)

def kirschhain():
    i = Island('kirschhain')  # Kirschblüten auf Moos
    i.disc(0, 0, 5, 0, 'grass_block', 'dirt', 5, seed=11)
    for x, z in ((-3, 1), (-2, 2), (3, -2), (2, 3)): i.set(x, 0, z, 'moss_block')
    i.cherry(0, 1, 0)
    for x, z, n in ((-3, -3, 3), (3, 2, 2), (-1, 3, 4), (2, -3, 1)):
        i.set(x, 1, z, 'pink_petals', facing='north', flower_amount=str(n))
    return i, (-2, 1, 3)

def pilzinsel():
    i = Island('pilzinsel')  # Myzel mit Riesenpilz, kleines Grasstück für Bäume
    i.disc(0, 0, 5, 0, 'mycelium', 'dirt', 5, seed=5)
    i.mushroom(0, 1, 0)
    for x, z in ((3, 3), (4, 2), (3, 2)): i.set(x, 0, z, 'grass_block', snowy='false')
    i.set(-3, 1, 2, 'red_mushroom'); i.set(2, 1, -3, 'brown_mushroom'); i.set(-2, 1, -3, 'red_mushroom')
    return i, (3, 1, 3)

def felsbrocken():
    i = Island('felsbrocken')  # Gruß an StoneBlock: Felsen mit etwas Erz, oben Gras und Baum
    rnd = random.Random(42)
    for x in range(-5, 6):
        for y in range(-6, 3):
            for z in range(-5, 6):
                r = 5.2 - max(0, -y - 2) * 0.55 - (max(0, y) * 0.9)
                if math.hypot(x, z) + rnd.random() * 0.8 > r: continue
                b = rnd.choices(['stone', 'cobblestone', 'andesite', 'diorite', 'granite', 'tuff'], [10, 4, 2, 1, 1, 1])[0]
                i.set(x, y, z, b)
    for x in range(-2, 3):
        for z in range(-2, 3):
            if abs(x) + abs(z) <= 3:
                top = max(y for (px, y, pz) in i.blocks if px == x and pz == z)
                i.set(x, top, z, 'grass_block', snowy='false'); i.set(x, top - 1, z, 'dirt')
    for x, y, z, ore in ((-3, -2, 1, 'coal_ore'), (2, -3, -2, 'coal_ore'), (3, -1, 2, 'copper_ore'), (-1, -4, -2, 'iron_ore')):
        if (x, y, z) in i.blocks: i.set(x, y, z, ore)
    gy = max(y for (px, y, pz) in i.blocks if px == 0 and pz == 0)
    i.oak(0, gy + 1, 0)
    return i, (2, gy + 1, 1)

ISLANDS = [
    (klassisch, 'Klassisch', 'Das L aus Erde wie in SkyBlock 2.1. Wenig Platz, ehrlicher Start.'),
    (lichtung, 'Waldlichtung', 'Runde Grasinsel mit Eiche, Birke und kleinem Teich.'),
    (oase, 'Oase', 'Sand, Palme, Zuckerrohr und Kakteen am Wasser.'),
    (kirschhain, 'Kirschhain', 'Kirschbaum auf Gras und Moos, Blütenteppich.'),
    (pilzinsel, 'Pilzinsel', 'Myzel und Riesenpilz, kleines Grasstück für Setzlinge.'),
    (felsbrocken, 'Felsbrocken', 'Ein StoneBlock-Gruß: Steinbrocken mit Kohle, Kupfer und Eisen, oben Gras.'),
]

def main():
    os.makedirs(OUT, exist_ok=True)
    templates, spawns = [], {}
    for fn, title, desc in ISLANDS:
        isl, sp = fn()
        r = ruine(isl, sp)
        size, sp_rel, n = isl.save(sp)
        spawns[isl.name] = {'south': [sp_rel], 'west': [], 'north': [], 'east': []}
        templates.append({'name': title, 'desc': desc, 'file': isl.name + '.nbt', 'spawns': isl.name,
                          'surroundingBlocks': 'default', 'spreads': 'default'})
        print(f'{isl.name:12} Größe {size}  Blöcke {n:4}  Spawn {sp_rel}  Ruine/Schild {r}')
    cfg = {
        'defaultOffset': 0, 'mainSpawnIsland': None, 'netherSpreads': [],
        'spawnPointReferences': spawns,
        'spreadReferences': {'default': []},
        'surroundingBlockReferences': {'default': {}},
        'templateList': templates,
    }
    path = os.path.join(PACK, 'config', 'skyblockbuilder', 'templates.json5')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('// Sky and Stone: wählbare Startinseln (erzeugt von _src/inseln.py)\n')
        json.dump(cfg, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
```

## Datei: kubejs/server_scripts/sieben.js
```js
// Sky and Stone – weniger Sieb-Plackerei
// 1. Fehlende Rohstoffe der Mod-Technik ins Ex-Deorum-Sieb
// 2. Alle Ex-Deorum-Siebtabellen auch für den Create-Sifter (früh automatisierbar mit Wind/Wasserrad)
// 3. Hammer-Rezepte auch für Create-Mühlstein und Brechwalzen
// 4. Mechanisches Sieb früher baubar (Andesit-Gehäuse statt Eisenblöcke)

const MESH_TO_SIFTER = {
  'exdeorum:string_mesh': 'createsifter:string_mesh',
  'exdeorum:flint_mesh': 'createsifter:andesite_mesh',
  'exdeorum:iron_mesh': 'createsifter:zinc_mesh',
  'exdeorum:golden_mesh': 'createsifter:brass_mesh',
  'exdeorum:diamond_mesh': 'createsifter:advanced_brass_mesh',
  'exdeorum:netherite_mesh': 'createsifter:advanced_sturdy_mesh'
}

// [Eingabe, Sieb, Ergebnis, Chance]
const EXTRA_DROPS = [
  ['minecraft:dirt', 'string', 'mysticalagriculture:inferium_essence', 0.10],
  ['minecraft:dirt', 'flint', 'mysticalagriculture:inferium_essence', 0.15],
  ['minecraft:dirt', 'iron', 'mysticalagriculture:inferium_essence', 0.20],
  ['minecraft:dirt', 'diamond', 'mysticalagriculture:inferium_essence', 0.30],
  ['minecraft:gravel', 'flint', 'mysticalagriculture:prosperity_shard', 0.04],
  ['minecraft:gravel', 'iron', 'mysticalagriculture:prosperity_shard', 0.06],
  ['minecraft:gravel', 'golden', 'mysticalagriculture:prosperity_shard', 0.08],
  ['minecraft:gravel', 'diamond', 'mysticalagriculture:prosperity_shard', 0.10],
  ['minecraft:sand', 'iron', 'mekanism:fluorite_gem', 0.05],
  ['minecraft:sand', 'diamond', 'mekanism:fluorite_gem', 0.08],
  ['minecraft:gravel', 'golden', 'powah:uraninite_raw', 0.03],
  ['minecraft:gravel', 'diamond', 'powah:uraninite_raw', 0.05],
  ['minecraft:moss_block', 'string', 'minecraft:bee_spawn_egg', 0.02],
  ['minecraft:moss_block', 'iron', 'minecraft:bee_spawn_egg', 0.04],
  // Nutztiere (spawnen in der Leere kaum von selbst)
  ['minecraft:dirt', 'string', 'minecraft:cow_spawn_egg', 0.01],
  ['minecraft:dirt', 'string', 'minecraft:sheep_spawn_egg', 0.01],
  ['minecraft:dirt', 'string', 'minecraft:chicken_spawn_egg', 0.01],
  ['minecraft:dirt', 'string', 'minecraft:pig_spawn_egg', 0.01],
  // Shulker-Schalen (keine Endstädte in der Leere)
  ['exdeorum:crushed_end_stone', 'diamond', 'minecraft:shulker_shell', 0.02],
  ['exdeorum:crushed_end_stone', 'netherite', 'minecraft:shulker_shell', 0.04],
  // Wilden-Teile für Ars Nouveau (keine Archwood-Wälder in der Leere)
  ['minecraft:gravel', 'golden', 'ars_nouveau:wilden_horn', 0.03],
  ['minecraft:sand', 'golden', 'ars_nouveau:wilden_spike', 0.03],
  ['minecraft:dirt', 'golden', 'ars_nouveau:wilden_wing', 0.03]
]

// Ex-Deorum-Mengenangabe -> Liste von Create-Ergebnissen
function toResults(id, amount) {
  let expected = 1
  if (typeof amount === 'number') expected = amount
  else if (amount && amount.type === 'minecraft:constant') expected = amount.value
  else if (amount && amount.type === 'minecraft:binomial') expected = amount.n * amount.p
  else if (amount && amount.type === 'minecraft:uniform') {
    // 0.7.0: Ex Deorum 3.12 schreibt min/max (ältere Versionen min_inclusive/max_inclusive). Vorher ergab das NaN
    // und 8 Mühlstein-Rezepte (Stein, Steinziegel, Prismarin, Tropfstein) gaben gar nichts aus.
    const lo = amount.min !== undefined ? amount.min : amount.min_inclusive
    const hi = amount.max !== undefined ? amount.max : amount.max_inclusive
    expected = (lo + hi) / 2
  }
  if (!(expected > 0)) return []
  const out = []
  const whole = Math.floor(expected)
  if (whole > 0) out.push({ id: id, count: whole })
  const rest = Math.round((expected - whole) * 1000) / 1000
  if (rest > 0) out.push({ id: id, chance: rest })
  return out
}

ServerEvents.recipes(event => {
  // --- 1. Extra-Drops
  const sieveJsons = []
  EXTRA_DROPS.forEach(e => {
    const json = {
      type: 'exdeorum:sieve',
      ingredient: { item: e[0] },
      mesh: { item: 'exdeorum:' + e[1] + '_mesh' },
      result: { id: e[2], count: 1 },
      result_amount: { type: 'minecraft:binomial', n: 1, p: e[3] }
    }
    event.custom(json).id('skyandstone:sieve/' + e[2].split(':')[1] + '_' + e[0].split(':')[1] + '_' + e[1])
    sieveJsons.push(json)
  })

  // --- 2. Siebtabellen -> Create-Sifter
  event.forEachRecipe({ type: 'exdeorum:sieve' }, r => sieveJsons.push(JSON.parse(r.json.toString())))
  event.forEachRecipe({ type: 'exdeorum:compressed_sieve' }, r => sieveJsons.push(JSON.parse(r.json.toString())))

  const groups = {}
  sieveJsons.forEach(j => {
    if (j.by_hand_only) return
    const mesh = MESH_TO_SIFTER[j.mesh && j.mesh.item]
    if (!mesh) return
    const key = JSON.stringify(j.ingredient) + '|' + mesh
    if (!groups[key]) groups[key] = { ingredient: j.ingredient, mesh: mesh, results: [] }
    toResults(j.result.id, j.result_amount).forEach(x => groups[key].results.push(x))
  })

  // 0.7.0: Create Sifter 2.3.0 hat kein Rezept für das Zinc Mesh (Stufe des Eisennetzes) -> wie die anderen Netze
  event.shaped('createsifter:zinc_mesh', ['SSS', 'SCS', 'SSS'], { S: 'minecraft:stick', C: '#c:ingots/zinc' })
    .id('skyandstone:zinc_mesh')

  event.remove({ type: 'createsifter:sifting' })
  let n = 0
  Object.keys(groups).forEach(k => {
    const g = groups[k]
    event.custom({
      type: 'createsifter:sifting',
      input: g.ingredient,
      mesh: { id: g.mesh, count: 1 },
      processingTime: 200,
      results: g.results
    }).id('skyandstone:sifting/' + (n++))
  })
  console.info('[Sky and Stone] Create-Sifter-Rezepte aus Ex Deorum: ' + n)

  // --- 3. Hammer -> Mühlstein (+ Brechwalzen, wenn Create dort nichts hat)
  let m = 0
  event.forEachRecipe({ type: 'exdeorum:hammer' }, r => {
    const j = JSON.parse(r.json.toString())
    const ings = Array.isArray(j.ingredient) ? j.ingredient : [j.ingredient]
    const results = toResults(j.result.id, j.result_amount)
    if (!results.length) { console.warn('[Sky and Stone] Hammer-Rezept ohne Ergebnis übersprungen: ' + (r.getId ? r.getId() : '?')); return }
    ings.forEach(ing => {
      if (!ing.item) return
      event.remove({ type: 'create:milling', input: ing.item })
      event.custom({ type: 'create:milling', ingredients: [ing], processing_time: 100, results: results })
        .id('skyandstone:milling/' + (m++))
      if (!event.containsRecipe({ type: 'create:crushing', input: ing.item })) {
        const bonus = results.concat([{ id: j.result.id, chance: 0.25 }])
        event.custom({ type: 'create:crushing', ingredients: [ing], processing_time: 100, results: bonus })
          .id('skyandstone:crushing/' + m)
      }
    })
  })
  console.info('[Sky and Stone] Mühlstein-Rezepte aus Ex-Deorum-Hammer: ' + m)

  // --- 4. Mechanisches Sieb günstiger
  event.remove({ id: 'exdeorum:mechanical_sieve' })
  event.shaped('exdeorum:mechanical_sieve', ['AGA', 'IHI', 'I I'], {
    A: 'create:andesite_casing', G: '#c:glass_blocks', H: 'minecraft:hopper', I: 'minecraft:iron_bars'
  }).id('skyandstone:mechanical_sieve')
})
```

## Datei: kubejs/server_scripts/balance.js
```js
// Sky and Stone – Balance (Gemini-Prüfung 24.10.2026, von Claude umgesetzt)
// 1) Pipez: obere Upgrades brauchen Technik aus Mekanism/AE2
// 2) Mystical Agriculture: höhere Essenz-Stufen erst nach Create -> Mekanism -> AE2
//    (Ressourcen-Samen brauchen die jeweilige Stufen-Essenz, damit sind auch die Samen gesperrt)

ServerEvents.recipes(event => {
  // --- 1. Pipez
  event.remove({ id: 'pipez:advanced_upgrade' })
  event.shaped('pipez:advanced_upgrade', ['DCD', 'RUR', 'DCD'], {
    D: '#c:gems/diamond',
    C: 'mekanism:advanced_control_circuit',
    R: '#c:storage_blocks/redstone',
    U: 'pipez:improved_upgrade'
  }).id('skyandstone:pipez/advanced_upgrade')

  event.remove({ id: 'pipez:ultimate_upgrade' })
  event.shaped('pipez:ultimate_upgrade', ['NEN', 'PUP', 'NEN'], {
    N: '#c:ingots/netherite',
    E: 'mekanism:elite_control_circuit',
    P: 'ae2:engineering_processor',
    U: 'pipez:advanced_upgrade'
  }).id('skyandstone:pipez/ultimate_upgrade')

  // --- 2. Mystical Agriculture: Essenz-Stufen
  // Inferium -> Prudentium bleibt wie es ist (Frühspiel).

  // Tertium: nur im Create-Mixer (4 Prudentium + Messing -> 2 Tertium)
  event.remove({ id: 'mysticalagriculture:tertium_essence' })
  const p = { item: 'mysticalagriculture:prudentium_essence' }
  event.custom({
    type: 'create:mixing',
    ingredients: [p, p, p, p, { tag: 'c:ingots/brass' }],
    results: [{ id: 'mysticalagriculture:tertium_essence', count: 2 }]
  }).id('skyandstone:mixing/tertium_essence')

  // Imperium: braucht Mekanism (Infused Alloy aus dem Metallurgic Infuser)
  event.remove({ id: 'mysticalagriculture:imperium_essence' })
  event.shaped('mysticalagriculture:imperium_essence', [' T ', 'TAT', ' T '], {
    T: 'mysticalagriculture:tertium_essence',
    A: 'mekanism:alloy_infused'
  }).id('skyandstone:imperium_essence')

  // Supremium: braucht AE2 (Engineering Processor aus dem Inscriber)
  event.remove({ id: 'mysticalagriculture:supremium_essence' })
  event.shaped('mysticalagriculture:supremium_essence', [' I ', 'IPI', ' I '], {
    I: 'mysticalagriculture:imperium_essence',
    P: 'ae2:engineering_processor'
  }).id('skyandstone:supremium_essence')

  // Insanium (Stufe 6): verbindet das MA-Endgame mit dem Mekanism-Endgame (0.5.0).
  // Original: 4 Supremium + Infusionskristall -> 1. Neu: 4 Supremium + Ultimate-Schaltkreis -> 2.
  event.remove({ id: 'mysticalagradditions:insanium_essence' })
  event.shaped('2x mysticalagradditions:insanium_essence', [' S ', 'SCS', ' S '], {
    S: 'mysticalagriculture:supremium_essence',
    C: 'mekanism:ultimate_control_circuit'
  }).id('skyandstone:insanium_essence')

  // --- 3. Magie als Alternative: Ars-Nouveau-Glyphe „Crush“ kann Bruchstein -> Kies -> Sand,
  // hier fehlt nur Sand -> Staub (Ex Deorum). Damit ersetzt ein Zauberturm den Hammer komplett.
  event.custom({
    type: 'ars_nouveau:crush',
    input: { item: 'minecraft:sand' },
    output: [{ chance: 1.0, maxRange: 1, stack: { count: 1, id: 'exdeorum:dust' } }]
  }).id('skyandstone:crush/sand_to_dust')

  // --- 3b. Essenz-Verdopplung verhindern (0.7.0): Die Rückbau-Rezepte von MA geben 4 Essenzen der Stufe darunter.
  // Mit den Rezepten oben (4 Prudentium + Messing -> 2 Tertium, 4 Supremium + Schaltkreis -> 2 Insanium)
  // wird daraus eine Endlosschleife: 4 Prudentium -> 2 Tertium -> 8 Prudentium. Die übrigen Rückbauten verlieren
  // Material und bleiben erhalten.
  event.remove({ id: 'mysticalagriculture:tertium_essence_uncraft' })
  event.remove({ id: 'mysticalagradditions:insanium_essence_uncraft' })

  // --- 4. Erzmagier-Zauberbuch ohne Totem (Nachtschicht 0.6.3): In der Leere gibt es keine Plünderer,
  // das Totem käme nur per Glück aus der Sternkiste. Der Magie-Weg zum Finale (z_weg) soll planbar sein.
  // Ersatz: Diamantblock. Netherstern (Wither) und Wilden-Tribut (Chimera) bleiben die echten Hürden.
  event.remove({ id: 'ars_nouveau:archmage_book_upgrade' })
  event.custom({
    type: 'ars_nouveau:book_upgrade',
    category: 'misc',
    ingredients: [
      { item: 'ars_nouveau:apprentice_spell_book' },
      { tag: 'c:ender_pearls' }, { tag: 'c:ender_pearls' }, { tag: 'c:ender_pearls' },
      { tag: 'c:gems/emerald' }, { tag: 'c:gems/emerald' },
      { item: 'minecraft:diamond_block' },
      { item: 'minecraft:nether_star' },
      { item: 'ars_nouveau:wilden_tribute' }
    ],
    result: { count: 1, id: 'ars_nouveau:archmage_spell_book' }
  }).id('skyandstone:archmage_book_upgrade')

  console.info('[Sky and Stone] Balance-Rezepte geladen (Pipez, Mystical Agriculture, Insanium, Ars-Crush, Erzmagier, ohne Essenz-Verdopplung)')
})
```

## Datei: kubejs/server_scripts/luecken.js
```js
// Sky and Stone – Lücken, die es nur in einer Leere-Welt gibt

ServerEvents.recipes(event => {
  // Keine Strongholds -> Endportalrahmen herstellbar (12 Stück für ein Portal)
  event.shaped('minecraft:end_portal_frame', ['OEO', 'SSS'], {
    O: 'minecraft:obsidian', E: 'minecraft:ender_eye', S: 'minecraft:end_stone'
  }).id('skyandstone:end_portal_frame')

  // Messing braucht einen Lohenbrenner, Lohen gibt es erst im Nether ->
  // Brenner auch aus Lohenpulver (Staub-Sieb), damit Create nicht hinter dem Nether hängt
  event.shapeless('create:blaze_burner', ['create:empty_blaze_burner', 'minecraft:blaze_powder', 'minecraft:blaze_powder',
    'minecraft:blaze_powder', 'minecraft:blaze_powder']).id('skyandstone:blaze_burner_from_powder')

  // 0.8.0: Aufgabenbildschirm (FTB Quests) hat kein Rezept, wird aber für die Strom-Prüfung gebraucht
  event.shaped('ftbquests:screen_1', ['IGI', 'GRG', 'IGI'], {
    I: '#c:ingots/iron', G: '#c:glass_blocks', R: 'minecraft:redstone'
  }).id('skyandstone:task_screen')
})
```

## Datei: kubejs/server_scripts/gruppen.js
```js
// Sky and Stone – eigene Item-Gruppen für Quests ("irgendein Sieb", "irgendein Holztiegel" ...)
// Werden in den Quests über FTB Filter System als item_tag(skyandstone:...) abgefragt.

ServerEvents.tags('item', event => {
  // Ex-Deorum-Siebe aus allen Holzarten (ohne Kompressions- und mechanische Siebe)
  event.add('skyandstone:sieves', /^exdeorum:(?!.*compressed)(?!mechanical)[a-z_]+_sieve$/)
  // Holztiegel für Wasser (Nether-Holz und Porzellan sind Lava-Tiegel)
  event.add('skyandstone:water_crucibles', /^exdeorum:(?!porcelain|unfired|crimson|warped|hellbark)[a-z_]+_crucible$/)
  // Botany Pots mit Trichter (alle Farben)
  event.add('skyandstone:hopper_botany_pots', /^botanypots:[a-z_]*hopper_botany_pot$/)
  // Archwood-Setzlinge aller Farben
  event.add('skyandstone:archwood_saplings', /^ars_nouveau:[a-z_]*archwood_sapling$/)
  // Macaw's: Dächer und Hängebrücken aller Holzarten
  event.add('skyandstone:roofs', /^mcwroofs:[a-z_]+_roof$/)
  event.add('skyandstone:rope_bridges', /^mcwbridges:rope_[a-z_]+_bridge$/)
  // Weiche vor dem Finale: Magie ODER Mob-Technik
  event.add('skyandstone:weg_zum_herz', ['ars_nouveau:archmage_spell_book', 'hostilenetworks:loot_fabricator'])
  // 0.7.0: z_erz „Erz ohne Sieb“ – eins der drei Systeme reicht (Felder, Laserbohrer, Erz-Bienen)
  event.add('skyandstone:erz_ohne_sieb', ['mysticalagriculture:osmium_seeds', 'industrialforegoing:ore_laser_base', 'productivebees:nether_quartz_nest'])
})
```

## Datei: kubejs/server_scripts/willkommen.js
```js
// Sky and Stone 0.9.0 – Begrüßung beim ersten Betreten einer Welt (einmal pro Spieler, kein Tick-Skript)
PlayerEvents.loggedIn(event => {
  const p = event.player
  if (p.persistentData.getBoolean('skyandstone_begruesst')) return
  p.persistentData.putBoolean('skyandstone_begruesst', true)
  p.tell(Text.gold('Willkommen in Sky and Stone.'))
  p.tell(Text.gray('Unter dir die Leere, unter der Leere ein Herz, das nicht mehr schlägt.'))
  p.tell(Text.white('Das Questbuch in deinem Inventar führt dich. Rechtsklick zum Öffnen, Belohnungen selbst abholen.'))
  p.tell(Text.gray('Keine Insel, sondern eine normale Welt? Dann beim Erstellen den Welttyp „Skyblock“ wählen.'))
})
```

## Datei: kubejs/client_scripts/hinweise.js
```js
// Sky and Stone 0.9.0 – Hinweise im Spiel: Tooltips und JEI-Infoseiten für alles, was in der Leere anders funktioniert.
// Ziel: Der Spieler findet die Antwort dort, wo er sucht (am Item, in JEI mit U/R), nicht nur im Questbuch.

const HINWEISE = {
  'minecraft:netherrack': ['Ohne Nether: Wasserfass auf Myzel wird zu Hexenwasser.', 'Hexenwasser im Fass + Lava ergibt Netherrack.'],
  'exdeorum:witch_water_bucket': ['Entsteht, wenn ein Wasserfass auf Myzel steht.', 'Mit Lava im Fass wird daraus Netherrack.'],
  'exdeorum:mycelium_spores': ['Aus Erde gesiebt. Auf Erde gesetzt wird Myzel daraus.', 'Myzel unter einem Wasserfass macht Hexenwasser.'],
  'exdeorum:silkworm': ['Auf Laub setzen: Es wird nach und nach befallen.', 'Voll befallenes Laub nur mit dem Crook abbauen, dann fällt Faden.'],
  'exdeorum:crook': ['Laub abbauen: mehr Setzlinge, selten eine Seidenraupe.', 'Voll befallenes Laub gibt Faden (etwa jedes zweite).'],
  'create:blaze_burner': ['Ohne Nether: Leerer Lohenbrenner + 4 Lohenstaub (Staub sieben).'],
  'create:empty_blaze_burner': ['4 Eisenbleche um 1 Netherrack.', 'Mit 4 Lohenstaub wird ein Lohenbrenner daraus.'],
  'minecraft:end_portal_frame': ['Es gibt keine Festungen in der Leere: Der Rahmen ist herstellbar (Obsidian, Enderauge, Endstein).'],
  'minecraft:ancient_debris': ['Schwarzstein hämmern und den Schutt sieben gibt selten Antiken Schrott.'],
  'mysticalagriculture:inferium_seeds': ['Werkbank: 8 Inferiumessenz um einen Weizensamen. Kein Altar nötig.'],
  'mysticalagriculture:prudentium_essence': ['4 Inferiumessenz um einen Infusionskristall. Der Kristall bleibt erhalten.'],
  'mysticalagriculture:tertium_essence': ['Nur im Create-Mixer: 4 Prudentium + 1 Messingbarren = 2 Tertium.'],
  'mysticalagriculture:imperium_essence': ['4 Tertium um eine Infused Alloy (Mekanism).'],
  'mysticalagriculture:supremium_essence': ['4 Imperium um einen Engineering Processor (AE2).'],
  'createsifter:zinc_mesh': ['Stöcke um einen Zinkbarren. Siebt wie das Iron Mesh.'],
  'ftbquests:screen_1': ['Eisen, Glas, Redstone. Zeigt eine Quest an und nimmt Items oder Strom dafür an.'],
  'ftbquests:lootcrate': ['Rechtsklick öffnet die Kiste. Gibt es als Quest-Belohnung, selten von Monstern, immer von Bossen.'],
  'waystones:waystone': ['Reisen zwischen Wegsteinen kostet Erfahrung. Dafür ist XP in Sky and Stone da.']
}

ItemEvents.modifyTooltips(event => {
  Object.keys(HINWEISE).forEach(id => {
    event.add(id, HINWEISE[id].map(z => Text.gray(z)))
  })
})

RecipeViewerEvents.addInformation('item', event => {
  Object.keys(HINWEISE).forEach(id => {
    event.add(id, HINWEISE[id])
  })
})
```

## Datei: config/skyblockbuilder/starter_inventory.json5
```json5
// Sky and Stone: Startausrüstung (bekommt jedes neue Team)
{
  "items": [
    { "Item": { "id": "ftbquests:book", "count": 1 } },
    { "Item": { "id": "minecraft:torch", "count": 8 } },
    { "Item": { "id": "exdeorum:wooden_watering_can", "count": 1 } },
    { "Item": { "id": "exdeorum:crook", "count": 1 } },
    { "Item": { "id": "minecraft:bread", "count": 16 } },
    { "Item": { "id": "minecraft:lava_bucket", "count": 1 } },
    { "Item": { "id": "minecraft:water_bucket", "count": 1 } },
    { "Item": { "id": "minecraft:ice", "count": 1 } },
    { "Item": { "id": "minecraft:bone_meal", "count": 16 } },
    { "Item": { "id": "minecraft:oak_sapling", "count": 2 } }
  ]
}```

## Datei: options.txt
```txt
version:3955
lang:de_de
renderDistance:8
simulationDistance:6
maxFps:120
enableVsync:false
graphicsMode:0
renderClouds:"fast"
particles:1
biomeBlendRadius:1
entityDistanceScaling:0.75
mipmapLevels:2
ao:true
resourcePacks:["vanilla","mod_resources","file/Whimscape_1.20.2-1.21.11_r7.zip"]
```

## Mod-Liste
AdvancedAE;Applied Energistics 2;Almost Unified;AmbientSounds;AppleSkin;Applied Energistics 2 Wireless Terminals;Applied Mekanistics;Architectury API;Ars Nouveau;Balm;Bookshelf;Botany Pots;Building Gadgets;Carry On;Cloth Config API;Clumps;Collective;Controlling;Create Mechanical Extruder;Create Sifting;Create;Create Crafts & Additions;CreativeCore;Cucumber Library;Curios API;Double Doors;Dynamic FPS;Entity Culling;Ex Deorum;Farmer's Delight;FastFurnace;FastWorkbench;FerriteCore;Forgiving Void;FramedBlocks;FTB Filter System;FTB Library (NeoForge);FTB Quests (NeoForge);FTB Teams (NeoForge);FTB Ultimine (NeoForge);FTB XMod Compat;Functional Storage;Fusion (Connected Textures);Geckolib;GraveStone Mod;GuideME;Handcrafted;Hostile Neural Networks;ImmediatelyFast;Industrial Foregoing;Inventory Essentials;Iris Shaders;Iron Furnaces;Iron Jetpacks;Jade Addons (Neo/Forge);Jade 🔍;JamLib;Just Enough Items (JEI);KubeJS;Leaves Be Gone;LibX;Lithium;Macaw's Bridges;Macaw's Doors;Macaw's Fences and Walls;Macaw's Furniture;Macaw's Lights and Lamps;Macaw's Paths and Pavings;Macaw's Roofs;Macaw's Stairs;Macaw's Trapdoors;Macaw's Windows;Mechanicals Lib;MEGA Cells;Mekanism Generators;Mekanism Tools;Mekanism;MezzConfig;Mining Gadgets;ModernFix;Moonlight Lib;More Culling;Mouse Tweaks;Mystical Agradditions;Mystical Agriculture;Not Enough Animations;Packet Fixer;Pipez;Placebo;Polymorph;Powah!;Prickle;Productive Bees;Puzzles Lib;Rechiseled;Resourceful Lib;Rhino;RightClickHarvest;Searchables;Shulker Box Tooltip;Simple Backups;Skyblock Builder;Sodium Extra;Sodium;Sophisticated Backpacks;Sophisticated Core;Sophisticated Storage;spark;SuperMartijn642's Config Lib;SuperMartijn642's Core Lib;Supplementaries;Time in a bottle;Titanium;TorchMaster;Trash Cans;Waystones;Xaero's Minimap;Xaero's World Map;

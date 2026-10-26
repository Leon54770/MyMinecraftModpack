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

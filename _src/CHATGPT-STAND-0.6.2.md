# Sky and Stone – kompletter Stand (Version 0.6.2, 25.10.2026)

Ich baue ein eigenes Minecraft-Skyblock-Modpack „Sky and Stone“. Hier ist der komplette aktuelle Aufbau, damit du mich beraten kannst. Bitte gib mir Ideen und Einschätzungen, keinen fertigen Code.

---

## 1. Eckdaten
- **Minecraft 1.21.1, NeoForge 21.1.264, Java 21**
- Verwaltet mit **packwiz** (Mod-Liste als Dateien, Export als `.mrpack` für Modrinth/Prism)
- Gespielt im **Prism Launcher**, Instanz mit **Auto-Update**: vor jedem Start holt `packwiz-installer-bootstrap` den neuesten Stand aus meinem Projektordner. Eigene Einstellungen (`options.txt`) bleiben erhalten.
- **119 Einträge** (Mods + Bibliotheken), dazu 3 Ressourcenpakete
- Genre: klassischer Skyblock mit Technik **und** Magie, komplett **questgeführt**, alles auf **Deutsch**
- Vorbilder: SkyFactory 4/5, StoneBlock 3/4, ATM10 Sky
- Spielweise: allein oder mit Freunden (Teams über Skyblock Builder / FTB Teams)
- Hardware: Laptop (i5-1235U, Intel Iris Xe, 16 GB RAM, 5–6 GB für Minecraft) und Gaming-PC (Ryzen 7 3700X, RTX 3060 Ti, 8 GB für Minecraft). **Der Laptop ist der Maßstab für die Leistung.**
- Getestet wird jede Version auf einem lokalen Testserver: startet fehlerfrei, alle KubeJS-Skripte laden, 0 fehlgeschlagene Rezepte.

---

## 2. Spielstart
- Welttyp **„Skyblock“** (Skyblock Builder) muss beim Welt-Erstellen von Hand gewählt werden (lässt sich ohne Zusatz-Mod nicht als Standard setzen; Hinweis steht in der ersten Quest).
- **6 wählbare Startinseln** (selbst gebaut per Python-Skript als NBT):
  Klassisch (das L aus SkyBlock 2.1) · Waldlichtung (Teich, Eiche, Birke) · Oase (Sand, Palme, Zuckerrohr, Kakteen) · Kirschhain · Pilzinsel (Myzel, Riesenpilz) · Felsbrocken (StoneBlock-Anspielung mit etwas Erz)
- **Startinventar:** Questbuch, 8 Fackeln, Gießkanne, Haken (Crook), 16 Brot, Lava- und Wassereimer, 1 Eis, 16 Knochenmehl, 2 Eichensetzlinge
- **Sicherheit:**
  - *Forgiving Void:* Wer in die Leere fällt, fällt oben wieder herunter – kostet 3 Herzen, tötet nie.
  - *Simple Backups:* stündlich (nur geänderte Dateien, einmal täglich voll), die letzten 8 bleiben, max. 10 GB.
  - *GraveStone:* Grab mit Inventar beim Tod.

---

## 3. Ressourcen-Progression (der rote Faden)
1. **Sieben (Ex Deorum):** Haken → Seidenraupe/Faden → Kompostfass → Bruchstein → Hammer (Kies, Sand, Staub) → Sieb. Mit der Hand bis zu 5×5 Siebe gleichzeitig.
2. **Automatisches Sieben (Create):** Der **Create-Sifter** nutzt per KubeJS dieselben Siebtabellen wie Ex Deorum (132 eigene Rezepte). Netze: Faden, Andesit, Zink, Messing, fortgeschrittenes Messing, stabil. **Mühlstein/Brechwalzen** übernehmen die Hammer-Rezepte. Mechanisches Sieb von Ex Deorum ist billiger (Andesit-Gehäuse, halber Strom).
3. **Extra-Siebdrops:** Inferium-Essenz, Prosperity-Splitter, Fluorit, Uraninit, Bienen- und Nutztier-Spawneier, Shulker-Schalen, Wilden-Teile.
4. **Mystical Agriculture** ersetzt das Sieben Schritt für Schritt – aber die Essenz-Stufen sind an Technik gekoppelt (siehe Balance).
5. **Spätspiel:** Mekanism-Erzverarbeitung (×2 → ×4 …), AE2-Autocrafting, Hostile Neural Networks (Mob-Drops ohne Mobs), Productive Bees.

**Lückenschließer für Skyblock (KubeJS):**
- Endportalrahmen craftbar (Obsidian, Enderauge, Endstein), weil es keine Strongholds gibt
- Lohenbrenner aus leerem Brenner + 4 Lohenpulver, damit Create-Messing nicht hinter dem Nether hängt
- Ars-Nouveau-Glyphe „Crush“ kann Sand → Staub, damit ersetzt ein Zauberturm den Hammer komplett

---

## 4. Mod-Liste nach Bereichen

**Skyblock-Grundlage**
Skyblock Builder, Ex Deorum, Forgiving Void, Botany Pots, Squat Grow (Ducken lässt Pflanzen wachsen, gedämpft), RightClickHarvest

**Technik**
- Create 6.0.10 + Create Sifting, Create Crafts & Additions, Create Mechanical Extruder (Bruchstein/Erze aus Flüssigkeiten)
- Mekanism 10.7 + Mekanism Generators, Mekanism Tools
- Powah! (Strom), Pipez (Rohre), Industrial Foregoing, Iron Furnaces, FastFurnace/FastWorkbench

**Lagerung / Logistik**
- Applied Energistics 2 + AdvancedAE, AE2 Wireless Terminals, Applied Mekanistics, MEGA Cells
- Sophisticated Storage + Sophisticated Backpacks, Functional Storage, Trash Cans, Inventory Essentials

**Ressourcen / Automation**
Mystical Agriculture + Mystical Agradditions, Productive Bees, Hostile Neural Networks, Time in a Bottle (gedrosselt), Almost Unified (vereinheitlicht doppelte Metalle/Items)

**Magie**
Ars Nouveau (Startbuch beim Spawn abgeschaltet, kommt über Quests)

**Werkzeuge / Bewegung**
Iron Jetpacks, Building Gadgets 2, Mining Gadgets, FTB Ultimine, Waystones, Carry On, TorchMaster

**Bauen / Deko / Essen**
Rechiseled, alle Macaw's-Mods (Brücken, Türen, Zäune, Möbel, Lampen, Wege, Dächer, Treppen, Falltüren, Fenster), Handcrafted, FramedBlocks, Supplementaries, Farmer's Delight, Double Doors, Leaves Be Gone

**Quests**
FTB Quests, FTB Teams, FTB Library, FTB XMod Compat, FTB Filter System (Item-Gruppen in Quests, z. B. „irgendein Sieb“)

**Info / Komfort**
JEI, Jade + Jade Addons, Xaero's Minimap + World Map, AppleSkin, Shulker Box Tooltip, Mouse Tweaks, Controlling, Searchables, Polymorph (Rezeptkonflikte), Clumps

**Leistung**
Sodium + Sodium Extra, Lithium, ModernFix, FerriteCore, ImmediatelyFast, Entity Culling, More Culling, Dynamic FPS, Packet Fixer, spark (Messung). Iris (Shader) installiert, aber aus.
Bewusst **nicht** drin: Continuity und andere Fabric-Mods, die auf NeoForge den Sinytra Connector bräuchten.

**Optik / Sound**
Ressourcenpaket **Whimscape** (16x, Standard an) + Fusion (verbundene Texturen); zum Einschalten: Bare Bones, Vanilla Experience+. Not Enough Animations, AmbientSounds.

**Bibliotheken** (nur technisch nötig): Architectury, Balm, Bookshelf, Cloth Config, Collective, CreativeCore, Cucumber, Curios, Geckolib, GuideME, JamLib, KubeJS, Rhino, LibX, Mechanicals Lib, MezzConfig, Moonlight, Placebo, Prickle, Puzzles Lib, Resourceful Lib, Sophisticated Core, SuperMartijn642 Config/Core Lib, Titanium

**Voreinstellungen (options.txt):** Sichtweite 8, Simulationsdistanz 6, Grafik „Schnell“, weniger Partikel, Deutsch.

---

## 5. Balance (eigene KubeJS-Rezepte und Configs)
**Mystical Agriculture an Technik gekoppelt:**
- Tertium-Essenz nur im Create-Mixer (mit Messing)
- Imperium braucht Mekanism Infused Alloy
- Supremium braucht einen AE2-Engineering-Prozessor
- Insanium = 4 Supremium + 1 Mekanism-Ultimate-Schaltkreis → 2
- Ressourcen-Samen nach ihrer echten Stufe in den Quests: Eisen/Kupfer/Certus Stufe 3, Gold/Osmium Stufe 4, Diamant Stufe 5

**Weitere Regeln:**
- Pipez: Advanced-Upgrade braucht Mekanism-Schaltkreise, Ultimate zusätzlich Elite-Schaltkreise + AE2-Prozessoren
- Time in a Bottle: höchstens 8-fach, höchstens 24 h gespeicherte Zeit
- AE2-Prägeplatten gibt es nur über Certus-Essenz (Mystical Agriculture)

**KubeJS-Skripte (alle serverseitig):**
- `sieben.js` – Siebtabellen → Create-Sifter, Hammer → Mühlstein/Brechwalzen, billigeres mechanisches Sieb, Extra-Drops
- `luecken.js` – Endportalrahmen, Lohenbrenner
- `balance.js` – Mystical Agriculture, Pipez, Insanium, Crush-Glyphe
- `gruppen.js` – eigene Item-Gruppen für Quests (alle Siebe, alle Wassertiegel, alle Botany Pots mit Trichter, Archwood-Setzlinge, Dächer, Hängebrücken, „Weg zum Herz“)

---

## 6. Questbuch (FTB Quests)
Alles wird von einem eigenen Python-Generator erzeugt (prüft jede Item-ID gegen eine Item-Liste vom Testserver, findet Zyklen, verwaiste und blockierte Quests, verbietet Quests ohne Aufgabe).

**Umfang: 19 Kapitel, 174 Quests, davon 68 Hauptstory.** Belohnungen über 4 Kisten (Holz, Eisen, Gold, Stern) plus XP, automatisch nach Quest-Wichtigkeit.

### Hauptstory (3 Akte, als „Schlangenlinie“ angeordnet)
| Kapitel | Quests | Inhalt |
|---|---|---|
| Akt I: Die Insel | 27 | Holz, Haken, Sieb, erster Eisenbarren, Inferium-Samen, Kupfer/Zink, Andesitlegierung, Create-Sifter, Messing, „Die Siebfabrik“ |
| Akt II: Maschinen | 21 | Strom aus Drehung (Alternator), Osmium, Metallurgic Infuser, Erzverdopplung, Tertium, Nether, Lohenruten, erstes Jetpack, Inscriber + Prägeplatten, ME-Netz, Erz ×4 |
| Akt III: Das Herz der Leere | 20 | AE2-Autocrafting, Imperium, Supremium, „Nie wieder sieben“, Wither, Drache, Elite-/Ultimate-Schaltkreis, Insanium, Spaltreaktor + Polonium, Antimaterie, „Die ewige Fabrik“, Weiche „Maschine oder Magie“ (Erzmagier-Zauberbuch ODER Beute-Fabrikator), Finale **„Erbe der Ewigkeit“** (Drachenei) |

### Mod-Kapitel (vertiefen einzelne Mods, zeigen Hauptstory-Quests als Verweise)
| Kapitel | eigene Quests | Verweise |
|---|---|---|
| Ex Deorum: Sieben | 5 | 11 |
| Create | 2 | 12 |
| Energie und Rohre (Powah, Pipez) | 11 | 1 |
| Mekanism | 8 | 12 |
| Lagerung | 4 | 1 |
| Applied Energistics 2 | 3 | 6 |
| Mystical Agriculture | 7 | 9 |
| Ars Nouveau | 14 | 1 |
| Landwirtschaft und Küche | 9 | 1 |
| Productive Bees (optional) | 6 | 1 |
| Hostile Networks und IF | 7 | 1 |
| Nether und End | 1 | 11 |
| Baumeister (optional) | 7 | 0 |
| Sammlerbuch (optional) | 4 | 0 |

### Sonderkapitel
- **Inselmarkt** (18 Quests): wiederholbare Tauschgeschäfte (Überschuss → Belohnungskiste), Abklingzeit 1–3 Minecraft-Tage, eine Kiste pro Team, inkl. 3 Endgame-Tausche
- **Story: Das Herz der Leere** (15 Verweise): Die Erbauer verbanden Maschinen und Magie und zapften eine Energiequelle unter der Welt an, bis die Welt in Inseln zerbrach. Notizen des letzten Wächters stehen kursiv in den Meilensteinen der Hauptstory.
- **Beutekisten von Mobs:** ca. 1 % pro Monster (meist Holz, selten Eisen), Bosse immer Gold oder Stern. Sternkiste enthält keine gesperrten Essenzen.

---

## 7. Entwicklungsverlauf (kurz)
- 0.1.0 Grundpaket · 0.2.0 Rezept-Lücken geschlossen · 0.2.1 Ressourcenpaket
- 0.3.0 Startinseln, Questbuch, Balance-Skripte · 0.4.0 Forgiving Void, Backups, Mob-Kisten, Inselmarkt, Prism-Auto-Update
- 0.5.0 Story + Finale (Ideen teilweise von ChatGPT) · 0.5.1 Abschlussprüfung
- 0.6.0 Questbuch-Umbau in Hauptstory Akt I–III + Mod-Kapitel · 0.6.1 Logik-Prüfung (Samen-Stufen, verwaiste Quests, Spaltreaktor vor Antimaterie)
- **0.6.2 (aktuell)** – nach erstem Spieltest: Hauptstory auf 68 Quests, Pfad-Layout, Item-Gruppen über FTB Filter System, Story-Notizen in den Meilensteinen

**Gelernt beim ersten Spieltest:** FTB Quests hakt Quests ohne Aufgabe sofort ab, auch wenn Voraussetzungen offen sind – deshalb hat jetzt jede Quest eine echte Aufgabe. Die Ars-Nouveau-Manaleiste unten links ist nicht abschaltbar.

---

## 8. Was ich als Nächstes messen will (Spieltest)
1. **Frühspiel:** Minuten bis „Erster Eisenbarren“ – Ziel unter ~30 min
2. **Create-Einstieg:** Hängt es zwischen Sieb und Messing?
3. **Leistung am Laptop:** nach 10 min `/spark tps` und `/spark health --memory`, FPS bei Sichtweite 8 – Ziel 20 TPS, RAM unter 80 %
4. **Mystical Agriculture:** Wann ersetzt die erste Ressourcen-Saat das Sieben? Fühlt sich Tertium fair an?
5. **Belohnungen:** Wie viele Mob-Kisten nach 1 h Farm, wird der Inselmarkt genutzt?

**Bewusst nicht geplant:** noch mehr große Mods oder Inseln, Tick-Skripte (Laptop-Leistung), künstlicher Grind, Wettbewerbssystem.

---

## Fragen an dich
1. Wo siehst du Progressions-Risiken (zu schnell / zu zäh) in der Hauptstory Akt I–III?
2. Ist die Kopplung Mystical Agriculture ↔ Create/Mekanism/AE2 sinnvoll oder zu streng?
3. Was fehlt im Vergleich zu SkyFactory 4/5, StoneBlock 4 oder ATM10 Sky – ohne die Laptop-Leistung zu gefährden?
4. Ideen, wie die Mod-Kapitel mit wenigen eigenen Quests (Create, AE2, Nether/End) interessanter werden?
5. Worauf soll ich beim nächsten Spieltest besonders achten?

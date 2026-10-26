# Sky and Stone – Quest-Konzept

Stand: 25.10.2026 · Grundlage für `_src/quests.py` (erzeugt `config/ftbquests/quests/**`).

## Leitlinien (aus Reviews von SkyFactory 4, StoneBlock 3/4, ATM10 Sky)
1. **Verzweigen statt Schlauch.** Jedes Kapitel hat 2–3 Äste, die sich trennen und wieder treffen (StoneBlock-4-Lob). Wer keine Lust auf einen Ast hat, nimmt den anderen.
2. **Jedes Kapitel endet mit einem Meilenstein**, der sich wie ein Ziel anfühlt (großer Quest, eigene Form, gute Belohnung).
3. **Keine Abhak-Listen.** Jeder Quest erklärt kurz *warum* (was er freischaltet oder spart). Keine „hole 64 von X“-Quests ohne Zweck.
4. **Kein Grind bei Pflicht-Rohstoffen.** Sieben ist nur am Anfang Handarbeit, danach Create-Sifter, mechanisches Sieb, Samen, Bienen, Laserbohrer.
5. **Magie bleibt nützlich.** Ars Nouveau liefert echte Abkürzungen (Starbuncle-Transport, Drygmy-Mobdrops ohne Töten, Zauber zum Bauen).
6. **Freiraum:** Bauen, Bienen und Erkundung sind optionale Seitenkapitel. Belohnungen dort sind schön (Baublöcke, Deko), nicht Pflicht.
7. **Belohnungen** über Beutekisten (Holz → Eisen → Gold → Stern) plus XP, keine Item-Flut.

## Freischalt-Reihenfolge (Stufen)
| Stufe | Inhalt | Voraussetzung | Was es freischaltet |
|---|---|---|---|
| 0 Insel | Baum, Haken, Kompostfass, Bruchstein-Generator | Startinventar | Erde, Kies, Sand |
| 1 Sieb | Holzsieb + Fadennetz, Hammer, Tiegel | Seidenraupe, Bruchstein | Erzbrocken → Eisen/Kupfer/Zink, Samen, Saplings |
| 2 Eisen | Eisen-/Feuersteinnetz, Eisenwerkzeug, Ofen | Eisen aus Brocken | Osmium/Zinn/Blei/Silber-Brocken, Inferium-Essenz |
| 3 Create | Andesitlegierung, Wasserrad, Mühlstein, Create-Sifter, Mixer, Messing | Andesit (Hammer-Kies + Bruchstein), Zink | Automatisches Sieben, **Tertium** (Mixer + Messing) |
| 4 Strom | Alternator (Create Crafts & Additions), Powah Energizing, Pipez | Messing, Kupferdraht | FE-Strom, mechanisches Sieb |
| 5 Mekanism | Osmium, Metallurgic Infuser, Erzverdopplung ×2/×3 | Strom | Stahl, Schaltkreise, **Imperium** (Infused Alloy), Pipez Advanced |
| 6 AE2 | Certus, Inscriber, Prozessoren, ME-Netz | Mekanism-Strom, Certus aus Sand-Sieb | Autocrafting, **Supremium** (Engineering-Prozessor), Pipez Ultimate |
| 7 Nether/End | Portal, Festung, Lohen, Wither, Drache | Obsidian, Eisen | Lohenruten, Netherstern, End-Rahmen (Rezept) |
| 8 Endgame | Insanium, Antimaterie, Netherstern-Reaktor, MEGA-Zellen | Stufen 5–7 | Abschluss |

Mystical Agriculture zieht sich quer durch: Inferium (Stufe 2) → Prudentium → Tertium (Create) → Imperium (Mekanism) → Supremium (AE2) → Insanium (Endgame). Regeln dazu in `kubejs/server_scripts/balance.js`.

## Kapitel
**Gruppe „Die Insel“**
1. **Willkommen** – Questbuch, Inselwahl, Sneaken lässt Pflanzen wachsen, Rechtsklick-Ernte, JEI, FTB Ultimine, Karte. Kleiner Kreis, nur Haken-Quests.
2. **Erde, Kies und Hoffnung** (Ex Deorum) – Ast A „Baum“: Haken → Seidenraupe → Faden → Fadennetz. Ast B „Stein“: Bruchstein-Generator → Hammer → Kies → Sand → Staub. Treffen sich beim **Sieb**. Danach Tiegel (Wasser/Lava), Gießkanne, Porzellan, Erzbrocken. Meilenstein: **Erster Eisenbarren**.
3. **Grünes Händchen** – Samen aus dem Sieb, Farmer's Delight (Schneidebrett, Kochtopf), Tiere aus Spawneiern, Botany Pots, Inferium-Samen. Meilenstein: **Autarke Insel** (Essen + Holz automatisch).

**Gruppe „Technik“**
4. **Kraft der Zahnräder** (Create) – Andesit → Wasserrad/Windmühle → Mühlstein (ersetzt Hammer) → Create-Sifter (ersetzt Handsieben) → Waschen per Ventilator → Mixer → Messing → Tertium. Nebenast: Extruder für Bruchstein, Förderbänder, Deployer, Mechanical Crafter. Meilenstein: **Die Siebfabrik**.
5. **Strom und Leitungen** – Alternator, Akku, Powah (Energizing Orb, Dielectric Paste, Reaktor), Pipez-Rohre und Upgrades, mechanisches Sieb. Meilenstein: **Netzstrom**.
6. **Mekanismus** – Osmium, Infuser, Stahl, Schaltkreise, Erzverarbeitung ×2/×3/×4/×5, Generatoren, Fluorit/Uran, Werkzeuge, Jetpack. Meilenstein: **Fünffach-Erz**.
7. **Lagerhaus** – Ast A klassisch: Sophisticated Storage/Backpacks, Functional Storage, Mülleimer. Ast B AE2: Certus → Fluix → Inscriber → Prozessoren → Controller → Zellen → Autocrafting → Wireless → Applied Mekanistics → MEGA. Meilenstein: **Das Netz denkt mit** (erstes Autocrafting).

**Gruppe „Natur und Magie“**
8. **Mystische Landwirtschaft** – Infusionsaltar, Samen pro Stufe (mit Querverweisen auf Create/Mekanism/AE2), Wachstumsbeschleuniger, Essenz-Ackerland. Meilenstein: **Nie wieder sieben**.
9. **Arkane Künste** (Ars Nouveau) – Quellsteine, Zauberbuch, erste Zauber, Quellgefäß + Quelllinks, Archwood (aus dem Sieb), Starbuncle (Transport), Drygmy (Mobdrops), Ritual, Wilden-Boss. Meilenstein: **Erzmagier**.
10. **Bienenstaat** (optional, Productive Bees) – Bienen aus dem Moos, Bienenstock, Zentrifuge, Ressourcen-Bienen. Alternative Rohstoffquelle.

**Gruppe „Abenteuer“**
11. **Jenseits der Leere** – Obsidian, Netherportal, Festung, Lohen, Wither-Skelette (Hexenwasser!), Wither, Enderperlen, Endportal-Rahmen, Drache, Shulker. Meilenstein: **Drachentöter**.
12. **Maschinengeist** – Hostile Neural Networks (Deep Learner → Datenmodelle → Simulation), Industrial Foregoing (Laserbohrer), Mob-Farm. Meilenstein: **Jagd ohne Jagd**.

**Gruppe „Freizeit“**
13. **Baumeister** (optional) – Rechiseled, Macaw's, Handcrafted, FramedBlocks, Supplementaries, Building Gadgets, Haus/Brücke/Garten als Haken-Quests mit Deko-Belohnungen.
14. **Herr der Leere** (Endgame) – Insanium, Antimaterie, Mekasuit, Nitro-Reaktor, MEGA-Zelle, Netherstern-Samen. Finale: **Herr der Leere**.

## Belohnungs-Tabellen
- **Holzkiste:** Brot, Knochenmehl, Setzlinge, Faden, Fackeln
- **Eisenkiste:** Eisen/Kupfer/Zink-Barren, Andesitlegierung, Redstone
- **Goldkiste:** Diamanten, Messing, Prozessoren, Upgrades
- **Sternkiste:** Netherstern-Splitter, Supremium-Essenz, Elytra-Ersatz (Jetpack-Teile)

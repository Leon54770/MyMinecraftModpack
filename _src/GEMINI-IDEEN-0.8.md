# Gemini-Ideen für 0.8 (mit Claude-Bewertung)

Stand: 25.10.2026 · Gefragt: gemini-3.6-flash mit dem Stand 0.7.0 (Changelog, offene Punkte, Regeln). Briefing und Rohantwort unten.

## Bewertung
| # | Idee | Urteil | Grund |
|---|---|---|---|
| 1 | Tag-Harmonisierung | **übernehmen (als TODO-0.7-Item-Gruppen)** | Almost Unified vereinheitlicht schon die Rezepte; offen sind nur die Quest-Aufgaben (Barren, Certus, Bruchstein …) |
| 2 | Bienen-Prüfung über Item mit Komponenten | **übernehmen, vorher prüfen** | Beste Idee: Wabe/Bienenkäfig mit Bienen-Komponente als Aufgabe. Ob FTB Quests 2101 Komponenten exakt vergleicht, muss am Testserver getestet werden |
| 7 | Ersatz für „Prüfungen der Leere“ | **übernehmen, klein anfangen** | Kill-Aufgaben (Wither, Chimera) und Energie-Aufgabe (FTB Quests hat einen Strom-Aufgabentyp, Task Screen) sind echte, automatisch prüfbare Ziele |
| 6 | Deko-Tauschbörse | **übernehmen** | Gibt Bauen einen Wert. Gruppe heißt `skyandstone:roofs` (nicht `c:roofs`); vorher prüfen, ob „verbrauchen“ mit Gruppen-Aufgaben richtig abzieht |
| 10 | Logistik-/Leistungs-Hinweise | **teilweise** | Kein eigenes Kapitel; je ein Tipp in vorhandenen Quests (Rohre statt Item-Entities, Simulation-Upgrade für Bienen) |
| 5 | Blaupausen-Markt (Gadget mit Vorlage) | später | Vorlagen in Belohnungen sind aufwendig und schwer zu testen |
| 3 | Technomagischer Beschleuniger | nein | MA hat schon den Wachstumsbeschleuniger; neue Rezeptkette wäre künstlich |
| 4 | Ars-Source als Mekanism-Chemikalie | nein | Nennt Botania (nicht im Pack), KubeJS-Unterstützung unklar |
| 8 | Magisches Erz mit 3-fach-Ertrag | nein | Würde Vierfach-Erz (Mekanism) entwerten |
| 9 | Schwebende Baublöcke | nein | Bräuchte neue Blöcke per Startup-Skript; Gerüst und Forgiving Void decken das ab |

## Rohantwort Gemini
Hier sind 10 konkrete Ideen und Verbesserungen für **Sky and Stone 0.8**, sortiert nach dem Nutzen für das Spielerlebnis.

---

### 1. Tag-Harmonisierung für Erze, Metalle und Ressourcen
* **Nutzen:** [Offener Punkt] Beseitigt Frust bei der Automatisierung und im Rezept-Grid, indem Items aus verschiedenen Mods (AE2, Mekanism, Create) nahtlos ineinandergreifen.
* **Was/Warum:** Universelle Tags (`c:ingots/iron`, `c:gems/certus_quartz`, `c:dusts/glowstone`) sicherstellen und Rezepte so anpassen, dass das bevorzugte Mod-Item als Output entsteht. Verhindert verstopfte Inventare und kaputte Auto-Crafting-Muster.
* **Umsetzung:** KubeJS Server-Skript (`ServerEvents.tags('item', ...)`). Tags für alle betroffenen Erze/Barren/Stäube von Ex Deorum, Mekanism und AE2 vereinheitlichen.
* **Aufwand:** Mittel | **Risiko:** Gering (solange KubeJS-Syntax für 1.21.1 exakt eingehalten wird).

---

### 2. Funktionierende Bienen-Validation via NBT-Item-Task
* **Nutzen:** [Offener Punkt] Löst das Advancement-Problem bei Productive Bees und macht den Bienen-Zweig in "Erz ohne Sieb" endlich verlässlich prüfbar.
* **Was/Warum:** Statt kaputten Advancements verlangt die Quest ein genistetes Item (z. B. eine spezifische Bienen-Wabe oder das mit der Biene gefüllte *Bee Cage* mit entsprechendem NBT-Data).
* **Umsetzung:** FTB Quests `item`-Task mit NBT-Matching für das Bienen-Item (z.B. `productivebees:configurable_honeycomb` mit NBT-Typ `crystalline` oder `productivebees:bee_cage` mit der entsprechenden Biene).
* **Aufwand:** Klein | **Risiko:** Gering.

---

### 3. Technomagische Katalysatoren für Mystical Agriculture
* **Nutzen:** [Magie/Technik-Verbindung] Verknüpft die Essenz-Produktion sinnvoll mit Technologiefortschritt, ohne künstlichen Grind zu erzeugen.
* **Was/Warum:** Spieler können Wachstumsbeschleuniger oder Spezial-Erde herstellen, die Magie (Ars Nouveau Source) und Technik (Mekanism-Gase/Create-Druck) kombiniert, um Essenz-Samen effizienter zu machen.
* **Umsetzung:** KubeJS-Rezept für *Wachstums-Beschleuniger*: Ars Nouveau *Source Gem* + Mekanism *Enriched Refined Obsidian* + Mystical Agriculture *Essence Farmland* im Create *Sequenced Assembly*.
* **Aufwand:** Mittel | **Risiko:** Gering.

---

### 4. Botania/Ars Nouveau-getriebene Mekanism-Chemiefabriken
* **Nutzen:** [Magie/Technik-Verbindung] Bietet Spielern der Magie-Route eine Alternative zu reinen Mekanism-Infrastrukturen für die Spätspiel-Verarbeitung.
* **Was/Warum:** Das Erzeugen von komplexen Mekanism-Chemikalien (z. B. Schwefelsäure oder Fluor) erlaubt Magie-basierte Alternativen unter Nutzung von Ars Nouveau *Source* und *Glyphen*.
* **Umsetzung:** KubeJS-Fluid/Gas-Rezept: Ars Nouveau *Source* (über KubeJS-Integration/Fluid-Äquivalent) im Mekanism *Chemical Dissolution Chamber* verarbeiten, um seltene Gase direkt herzustellen.
* **Aufwand:** Mittel | **Risiko:** Mittel *(Uncertainty: Exakte API-Unterstützung von KubeJS 1.21.1 für Mekanism Chemical Transfer prüfen)*.

---

### 5. "Meister-Baumeister" Blaupausen-Markt
* **Nutzen:** [Freies Bauen/Sandbox] Belohnt ästhetisches Bauen im Skyblock und nimmt die Trägheit aus dem Basenbau im Midgame.
* **Was/Warum:** Bietet fertige Buildpaste-/Building-Gadget-Schematics über den Inselmarkt an. Spieler kaufen Bau-Blaupausen für schöne Insel-Module gegen überschüssige Baumaterialien.
* **Umsetzung:** FTB Quests im Kapitel „Abseits des Weges“: Trade-Quests (z. B. 64x Framed Blocks gegen ein Building Gadget mit geladener Template/Schematic via Quest-Reward NBT).
* **Aufwand:** Klein | **Risiko:** Gering.

---

### 6. Architekten-Tauschbörse im Inselmarkt
* **Nutzen:** [Freies Bauen/Sandbox] Gibt Dekoration (Macaw's, Handcrafted) einen spielerischen Wert im Wirtschaftssystem des Packs.
* **Was/Warum:** Wiederholbare Quests, bei denen große Mengen an Dekorationsblöcken abgegeben werden, um seltene Baumeister-Tools, Transport-Waystones oder Kosmetik-Beutel zu erhalten.
* **Umsetzung:** FTB Quests `repeatable`-Quests im Bereich „Abseits des Weges“. Task: 128x Beliebige Macaw-Dächer/Zäune (über Tag `c:roofs` etc.). Belohnung: Waystone oder spezielle Sammler-Kiste.
* **Aufwand:** Klein | **Risiko:** Gering.

---

### 7. Ersatz für "Prüfungen der Leere" durch echte Combat/Automation-Tasks
* **Nutzen:** [Offener Punkt] Ersetzt die gestrichenen Haken-Quests durch automatisierbare, messbare Meilensteine.
* **Was/Warum:** Statt manueller Haken erfordern die Prüfungen nun den Nachweis technischer/magischer Kapazität (z.B. Besiegen von Bossen via Hostile Neural Networks oder Bereitstellung gewaltiger Energiemengen).
* **Umsetzung:** FTB Quests: `kill`-Tasks (Bosse), `forge_energy`-Tasks (z. B. Speicher 100M FE in Powah-Netzwerk) und `item`-Tasks für HNN *Prediction Matrixes*.
* **Aufwand:** Klein | **Risiko:** Gering.

---

### 8. Erzgewinnung 2.0: Create-Sifter trifft Ars Nouveau Ritual
* **Nutzen:** [Magie/Technik-Verbindung] Bietet eine extrem performante, visuell ansprechende Erz-Vervielfachung für gemischte Basen.
* **Was/Warum:** Ein Ars Nouveau *Ritual of Awakening* verwandelt gesiebten Kies direkt in angereicherte Erze, die dann in Create-Mühlen ohne Zwischenschritte direkt verarbeitet werden können.
* **Umsetzung:** KubeJS-Crafting/Binding-Rezept: *Source Gem* + Sifter-Gravel ergibt im Create Mixer ein "Magisches Erzkrusten-Item", das beim Schmelzen den 3-fachen Ertrag liefert.
* **Aufwand:** Mittel | **Risiko:** Gering.

---

### 9. Vertikale Expansion: Antigravitations-Bausteine
* **Nutzen:** [Freies Bauen/Sandbox] Erleichtert das Bauen in der Leere ohne Absturzsicherheitsprobleme im frühen/mittleren Spielverlauf.
* **Was/Warum:** Spezielle Baumaterialien, die beim Platzieren in der Luft nicht fallen und dem Spieler kurzzeitig Levitation verleihen, wenn er daran baut (vor dem Iron Jetpack).
* **Umsetzung:** KubeJS-Rezept: Framed Block + Ars Nouveau Air-Essenz/Enderelement ergibt 16x "Schwebende Baufundamente".
* **Aufwand:** Klein | **Risiko:** Gering.

---

### 10. Performance-Orientiertes Logistik-Handbuch (Quest-Kapitel)
* **Nutzen:** [Performance & Orientierung] Verhindert Lag-Quellen auf Schwachbrust-Systemen (Iris Xe / 5GB RAM), bevor sie entstehen.
* **Was/Warum:** Eine Questreihe erklärt spielerisch, warum Pipez/AE2/Functional Storage massiven Tick-Lags durch riesige Item-Entitäten vorbeugen und belohnt lag-freie Logistik-Setups.
* **Umsetzung:** FTB Quests Orientierungs-Kapitel. Verlangt das Craften von Framed Storage Drawers und AE2-Kabeln anstelle von offenen Fließbändern/Trachtern; Belohnung: Pipez Upgrades.
* **Aufwand:** Klein | **Risiko:** Gering.
[gemini-3.6-flash · erste Antwort nach 6.5 s · gesamt 15.3 s, 2154 rein / 1986 raus]

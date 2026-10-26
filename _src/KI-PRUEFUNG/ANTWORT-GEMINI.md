### 1. Gesamturteil

„Sky and Stone“ befindet sich auf einem herausragenden Niveau und setzt sich im Modpack-Design deutlich von standardmäßigen Kitchen-Sink-Packs ab. Die technische Architektur (Python-Generator zur ständigen Validierung, deterministische Layout-Prüfung, Entkopplung von Daten und Sprache) sowie die KubeJS-Integration sind extrem professionell gelöst. Die Verflechtung der Mod-Mechaniken (Create-Mixer für Tertium, Mekanism-Legierungen für Imperium, AE2-Prozessoren für Supremium und Mekanism-Ultimate-Schaltkreise für Insanium) erzeugt einen roten Faden, der das Pack wie ein kohärentes, eigenständiges Spiel wirken lässt. Mit geringfügigen Korrekturen bei der Client-Optimierung und der Schärfung der Endgame-Progression besitzt dieses Pack das Potenzial, als Paradebeispiel für moderne NeoForge-Skyblocks (Minecraft 1.21.1) wahrgenommen zu werden.

---

### 2. Fehler und Risiken (höchstens 10)

1. **`sieben.js` (Zeilen 34–50): Mögliche Endlosschleife / Rezept-Duplizierung bei KubeJS-Reload**
   - *Was falsch ist / schiefgeht:* In `sieben.js` wird die Variable `sieveJsons` global außerhalb von Events deklariert, aber im `ServerEvents.recipes`-Event per `.push()` befüllt. Zudem wird bei jedem Aufruf von `event.forEachRecipe({ type: 'exdeorum:sieve' }, ...)` das Array erneut gefüllt. Ein manueller Reload via `/reload` oder KubeJS-Live-Reload im laufenden Spiel verdoppelt/vervielfacht die Einträge in `sieveJsons`, was zu extremen Memory-Leaks oder hunderte doppelten Create-Sifter-Rezepten führt.
   - *Fehler oder Vermutung:* Sicher ein Fehler.
   - *Behebung:* Mache `sieveJsons` zu einer lokalen Variable *innerhalb* der Event-Funktion (`const sieveJsons = []`).

2. **`options.txt` / Mod-Liste: Inkompatibilität von Sodium + Sodium Extra auf NeoForge**
   - *Was falsch ist / schiefgeht:* Sodium und Sodium Extra sind primär für Fabric/Quilt. Auf NeoForge wird in der Regel **Embeddium** oder der **Sinytra Connector** benötigt. Die Datei `README.md` erwähnt bewusst, dass Continuity weggelassen wurde, um den Sinytra Connector zu vermeiden. Falls Sodium/Sodium Extra direkt als NeoForge-Port vorliegt, führt dies oft zu Darstellungsfehlern mit Indium/Iris (Iris Shaders).
   - *Fehler oder Vermutung:* Vermutung (abhängig vom exakten NeoForge-Fork der Mod), aber hohes Absturzrisiko beim Starten des Clients.
   - *Behebung:* Ersetze Sodium/Sodium Extra im NeoForge-Kontext durch **Embeddium** (und ggf. Embeddium Extra), welches nativ und extrem stabil auf NeoForge 1.21.1 läuft.

3. **`balance.js` (Zeile 33–38): Rezept-Konflikt bei Imperium-Essenz**
   - *Was falsch ist / schiefgeht:* Imperium-Essenz nutzt das Crafting-Muster `' T '`, `'TAT'`, `' T '` mit `T = Tertium` und `A = mekanism:alloy_infused`. Das Standard-Rezept von Mystical Agriculture nutzt dieselbe Anordnung, aber meist mit dem Infusionskristall oder anderen Zudaten. Wenn Mystical Agriculture seine Rezepte spät registriert, kann es zu einem Silent Override oder JEI-Überlappungsfehler kommen.
   - *Fehler oder Vermutung:* Vermutung.
   - *Behebung:* Explizit `event.remove({ output: 'mysticalagriculture:imperium_essence' })` ausführen (nicht nur über Rezept-ID `mysticalagriculture:imperium_essence`), um sicherzustellen, dass das Vanilla-MA-Rezept restlos getilgt ist.

4. **`quests.py` / `sperren.py`: Zirkuläre Abhängigkeits-Anomalie bei `z_erz` und `m_niemehr`**
   - *Was falsch ist / schiefgeht:* `z_erz` verlangt `deps=['m_niemehr', 'h_laser', 'b_zucht']` mit `dep_any=True`. Gleichzeitig schaltet `m_niemehr` (Supremium) die Samen frei, die `z_erz` als Erfüllung anbietet (Osmium-Samen). Wenn der Spieler über Bienen oder Laserbohrer geht, schaltet er `z_erz` frei, *bevor* er `m_niemehr` erreicht. Das ist gewollt, jedoch ist `z_erz` in `z_herr` als Pflicht-Bedingung eingebunden.
   - *Fehler oder Vermutung:* Vermutung bezüglich der Logikabfolge im Questbuch.
   - *Behebung:* In `quests.py` sicherstellen, dass Quests, die Alternativen bieten, im Questbaum optisch klar abgekoppelt von linearen Essenzstufen-Strängen platziert werden, damit keine Verwirrung über Pflicht-Meilensteine entsteht.

5. **`options.txt`: Zu geringe Allokation von RAM / Chunk Rendering Performance auf Laptops**
   - *Was falsch ist / schiefgeht:* Sichtweite 8 / Simulation 6 ist gut für Intel Iris Xe, aber `mipmapLevels:2` und `ao:true` (Ambient Occlusion) erzeugen bei integrierten Grafikkarten (iGPU) massive Frametime-Spikes, sobald viele Create-Animationen und Pipez-Kabel im Blickfeld sind.
   - *Fehler oder Vermutung:* Vermutung (performanzbedingt).
   - *Behebung:* In `options.txt` standardmäßig `mipmapLevels:0` setzen. Mipmapping bringt bei integrierter Intel-Grafik kaum visuellen Gewinn, frisst aber massiv Bandbreite beim Grafikspeicher (Shared RAM).

---

### 3. Spielerlebnis

1. **Frühspiel & Werkzeug-Haptik:** Der Einstieg ist durch das Startinventar (Gießkanne, Haken, Setzlinge) exzellent geglättet. Die Mechanik mit der Seidenraupe und dem Crook ist schlüssig, leidet aber minimal unter der Minecraft-Eigenheit, dass Faden-Ausbeute sich ohne Ultimine zäh anfühlt.
2. **Der Übergang Hand-Sieb → Create Sifter:** Dies ist der stärkste Moment des Packs. Das Gefühl, vom doppelten Schmelzen und manuellen Rechtsklicken zu einer wind- oder wassergetriebenen Automatisierung überzugehen, vermittelt das echte Gefühl von technischem Fortschritt („Industrial Revolution“).
3. **Story-Integration & Notizen:** Die Notizen des Wächters sind stilistisch hervorragend geschrieben („Einst siebten wir Sternenstaub...“). Die Ausgabe von gedruckten Tagebuchseiten (`item('minecraft:paper')` mit benutzerdefinierten NBT/Lore-Tags) als Item-Belohnung fördert den Sammeltrieb ungemein.
4. **Belohnungs-Design:** Das Ersetzen von reinem XP-Spam durch kontextbezogene Themeneimer/Themenkisten (Kiste der Magie, Kiste der Technik, Kiste der Natur) stärkt die Motivation. Die Wahl-Möglichkeit bei großen Meilensteinen gibt Spielern Selbstbestimmung.
5. **Gleichwertigkeit von Technik und Magie:** Die Ergänzung der Ars-Nouveau-Glyphe „Crush“ (Sand zu Staub) und die Vereinfachung des Erzmagier-Zauberbuchs (Ersatz des Totems durch einen Diamantblock) setzt Ars Nouveau endlich gleichwertig neben Create/Mekanism. Es ist kein Beiwerk mehr, sondern ein vollwertiger Pfad.
6. **Entscheidungsfreiheit vor dem Finale:** Die Wahl-Quests „Maschine oder Magie“ (`z_weg`) sowie „Erz ohne Sieb“ (`z_erz`) brechen die Starrheit klassischer Expert-Modpacks. Der Spieler wird nicht gezwungen, *jede* Mod bis zum Maximum auszuquetschen, sondern darf Spezialisierung wählen.
7. **Bauen & Ästhetik:** Durch die Einbindung von Macaw’s Mods, FramedBlocks, Rechiseled und Handcrafted in Kombination mit der Vergabe von Themenkisten wird der Basisbau von einem funktionellen „Plattform-Aufbau“ zu einem optischen Erlebnis aufgewertet.
8. **Koop-Kompabilität:** Die Umstellung aller wiederholbaren Quests und Markt-Tausche auf pro-Team-Logik verhindert Exploits auf Servern, während Fortschrittsteilung Vergewisserung schafft.

---

### 4. Wie würdest du weitermachen? (Plan für die nächsten 3 Versionen)

#### Version 0.11.0: „Client-Feinschliff & Performance-Absicherung“
- **Embeddium-Migration:** Vollständige Umstellung der Performance-Renderer-Suite im Packwiz-Index von Sodium/Sodium Extra auf Embeddium + Embeddium Extra.
- **JEI-Kategorien bereinigen:** Verbergen unnutzbarer Platzhalter-Items (z. B. ungenutzte Erze anderer Mods, technische Platzhalterblöcke) via KubeJS-Client-Events (`RecipeViewerEvents.removeEntries`).
- **Options-Profil schärfen:** `options.txt` mit `mipmapLevels: 0` und optimierten Culling-Distanzen für Entity Culling fixieren.
- **KubeJS-Aufräumarbeiten:** Behebung des globalen Scopes in `sieben.js` zur Verhinderung von Memory-Leaks bei Reloads.

#### Version 0.12.0: „Visuals, Tutorials & Endgame-Komfort“
- **Ponder-Integration (Create):** Erstellung von eigenen Create-Ponder-Szenen (via KubeJS Ponder API) für das Ineinandergreifen von Create-Extruder, Mahlstein und Create-Sifter.
- **Automatisierte Markt-Station:** Hinzufügen einer speziellen Markt-Tausch-Mechanik über den FTB Task Screen, um die Markt-Quests physisch hübscher in der Welt zu platzieren.
- **Endgame-Balancing:** Überprüfung des Energiebedarfs des SPS (Supercritical Phase Shifter) für Antimaterie; Anpassung der Powah- und Mekanism-Generatoren-Rezepte, damit die Energieerzeugung fordernd, aber nicht in träges Warten ausartet.

#### Version 1.0.0: „Release Candidate & Polish“
- **Playtest-Auswertung:** Einarbeitung aller Datenpunkte aus den echten Client-Playtests (Zeit bis zum ersten Eisen, TPS-Verlauf nach 20 Spielstunden).
- **Insel-Feinschliff:** Letzter Schliff an den NBT-Vorlagen der Startinseln (sicherstellen, dass alle Ruinen-Schilder saubere Textformatierungen aufweisen).
- **Sound & Flair:** Kleine KubeJS-Sound-Effects beim Erreichen von Haupt-Story-Meilensteinen (z. B. Abspielen eines tiefen Gongs/Leere-Sounds beim Abschluss eines Akts).
- **Finaler Export:** Erstellung des Release-Builds für Modrinth/CurseForge via Packwiz.

---

### 5. Drei kreative Ideen für Alleinstellungsmerkmal

1. **Das „Relikt der Erbauer“ (Physische Notiz-Fragmente als Crafting-Zutat):**
   Die Tagebuchseiten der Wächter (17 Notizen) bleiben nicht nur reine Sammelobjekte aus Papier. Am Ende von Akt III können Spieler die 17 gesammelten Notizen im Infusionsaltar oder im Arkanen Kern zu einem magisch-technischen Katalysator („Wächter-Codex“) vereinen, der als unverbrauchbare Zutat für das Finale (`z_herr`) dient. Wer die Story liest und sammelt, schaltet das Finale physisch frei.

2. **„Echo-Singularitäten“ (KubeJS-Custom-Items für Magie/Technik-Synergie):**
   Erstelle über KubeJS ein Item namens *„Resonanz-Kristall“*. Dieser entsteht, indem man ein Create-Präzisionsgetriebe in einem Quellglas von Ars Nouveau mit Quelle auflädt. Dieser Kristall wird die zentrale Komponente für High-Tier-Upgrades (z. B. Pipez Ultimate Upgrade oder ME-Controller). Das zwingt den Spieler nicht zu Grind, kreiert aber eine wunderschöne, direkte Übersetzung des Lore-Mottos: „Maschine und Magie waren für uns nie Gegensätze.“

3. **Insel-Resonanz (Dynamische Welt-Events via KubeJS):**
   Wenn der Spieler wichtige Haupt-Meilensteine abschließt (z. B. `c_siebfabrik` oder `z_sps`), wird via KubeJS Server-Event ein einmaliger Partikel-Lichtsäulen-Effekt in den Himmel geschossen und ein sanftes Erdbeben (Kurzer Camera Shake / Sound-Effekt) ausgelöst. Dies vermittelt dem Spieler sofort visuell und akustisch: *Die Welt reagiert darauf, dass du das Herz der Leere wieder zum Schlagen bringst.*

# Anweisung: Sky and Stone 0.6.1 – spielbereit machen

Stand: 25.10.2026 · Basis 0.6.0 (19 Kapitel, 186 Quests) · erstellt von der Sitzung „Gemini API oder ChatGPT nutzen“
Quellen: Leons Entscheidungen zur Gemini-Endprüfung, ChatGPT-Auftrag „0.5.1 gezielte Qualitätsverbesserung“ (als Leitlinie), eigene Prüfung von 0.6.0, Gemini-Prüfung (gegengeprüft).

## Grundregeln (aus dem ChatGPT-Auftrag, an das Pack angepasst)
- Kleine, begründete Korrekturen statt Umbau. Keine neuen Mods, Inseln oder Systeme, keine Modversionen ändern.
- **Keine Balance-Änderungen ohne Spieldaten** (Sifter-Drops, MA-Stufen, Insanium-Rezept, Markt, Mob-Kisten). Dafür Messpunkte (Teil E).
- Quest-Schlüssel dürfen sich ändern (Leon startet mit neuer Welt), sollen aber stabil bleiben, wo es geht.
- Vorher sichern: `modpacks/_backups/sky-and-stone-0.6.0-<Zeit>/` (ohne .mrpack). Kein `rm` auf Variablenpfade.
- Prism zieht beim Start den Ordnerstand: `packwiz refresh` erst, wenn der Testserver mit dem neuen Stand fehlerfrei läuft.

## A) Leons Entscheidungen (umsetzen)
1. **Story-Kette lösen:** Jede `st_`-Notiz hängt nur an ihrem Meilenstein **und** an der vorherigen Notiz, **aber nur, wenn beide in der Hauptstory liegen**. Notizen zu Mod-Kapitel-Meilensteinen (`st_g_autark`, `st_a_erzmagier`, `st_h_fab`) werden Seitenäste: Sie hängen nur an ihrem Meilenstein, und keine andere Notiz hängt an ihnen. `st_z_herr` hängt nur an `z_herr` und `st_z_sps`.
2. **Spaltreaktor + Polonium vor der Antimaterie** (keine Sackgasse: Mekanism-Uran fällt im Sieb aus zerkleinertem Tiefenschiefer, dazu Uran-Samen):
   - neue Quest `k_spalt` „Spaltreaktor“: `mekanismgenerators:fission_reactor_casing` ×1 + `mekanismgenerators:fission_fuel_assembly` ×1, deps `z_elite` (im Mekanism-Kapitel, Verweis in Akt III). Text: Uran → Yellowcake → Uranhexafluorid → Spaltbrennstoff; Atommüll entsteht.
   - neue Quest `k_polonium` „Polonium“: `mekanism:pellet_polonium` ×1, deps `k_spalt`. Text: Atommüll im Solar Neutron Activator (braucht Tageslicht) zu Polonium.
   - `z_sps` deps: `k_polonium`, `l_auto`, `z_elite` (statt `z_strom`). Text: Polonium im SPS, viel Strom nötig.
3. **Mengen:** `z_insanium` 32 → 8. `c_siebfabrik` 64/32/64 → 32/16/32 (jede Aufgabe wird einzeln erkannt, mehr bringt nichts).
4. **Finale `z_herr`: Magie ODER Maschinen** (Leon, 25.10.2026): `a_erzmagier` aus den festen deps von `z_herr` nehmen. Neue Zwischen-Quest `z_weg` „Maschine oder Magie“ mit `dep_any=True` (FTB: `dependency_requirement: one_completed`), deps `a_erzmagier`, `h_fab`, Aufgabe z. B. `minecraft:nether_star` ×1 (oder eine andere automatisch erkennbare Aufgabe ohne Mehraufwand). `z_herr` deps: `z_fabrik`, `j_drache`, `m_niemehr`, `z_weg`. Text: „Die Erbauer brauchten beides. Dir reicht einer der Wege.“
   (Grund für die Zwischen-Quest: `dep_any` gilt für alle deps einer Quest. Direkt an `z_herr` würde sonst schon eine einzige der Bedingungen reichen.)
5. **`z_strom` optional** (`optional=True`). Text: „Jede große Stromquelle reicht – der Reaktor ist der bequeme Weg.“ Damit hängt keine Pflicht-Quest mehr daran (siehe Punkt 2).

## B) Gefundene Fehler (umsetzen)
6. **Vier Quests haben beim Zusammenlegen ihre Voraussetzung verloren** und stehen frei im Buch:
   - `e_lavatiegel` → deps `e_tiegel` (Porzellan-Schritt steckt jetzt in dieser Quest)
   - `g_topf` (Küche) → deps `g_feld`
   - `s_orb` (Energizing Orb) → deps `s_draht`
   - `k_cube` (Strom verteilen) → deps `k_infuser`
7. **Generator absichern** (`_src/quests.py`, am Ende von `main()` als Prüfung, Fehler = Abbruch):
   - Jede Quest außer `w_start` hat mindestens eine Abhängigkeit.
   - Keine Pflicht-Quest hängt an einer optionalen Quest.
   - `st_`-Quests hängen nur an Hauptstory-Quests, an ihrem eigenen Meilenstein oder an anderen `st_`-Quests der Hauptstory.
   - Keine Haken-Aufgabe (`checkmark`) mehr.
   - Kein Zyklus in den Abhängigkeiten.
   Danach `python -I _src/quests.py` muss 0 Fehler melden.

## C) Geprüft und bewusst NICHT ändern
- Questtexte für Endportalrahmen und Lohenbrenner: Die Hinweise sind schon vorhanden.
- `x_stern`: Der Tausch nimmt einen Netherstern und verkauft keinen, also gibt es keine Umgehung.
- `s_furnator`: Er ist selbst ein Generator und braucht keine Stromquelle davor.
- `m_supremium` hängt an `l_prozessoren`, und die verlangen den Engineering-Prozessor schon.
- Optionale Quests, die an Pflicht-Quests hängen (z. B. `e_kanne`), sind normal.
- Mob-Samen/Seelengefäß: Keine Quest verlangt Mob-Samen, also ist das keine Sackgasse.

## D) Prüfen nach dem Umbau
1. `python -I _src/quests.py` → 0 Fehler, Überlappungs-Check 0
2. Testserver mit neuem `config/ftbquests` + `kubejs`: „Loaded … chapters, … quests“ ohne Fehler, KubeJS 0 Fehler, 0 fehlgeschlagene Rezepte
3. Quest-Liste neu ausgeben (`QUEST-LISTE-0.6.1.txt`) und gegen A/B abhaken
4. `packwiz refresh`, Version **0.6.1**, `packwiz modrinth export`, Stichprobe: Export enthält neue Kapitel-Dateien, kein `_src`
5. README: Verlauf 0.6.1 + Abschnitt „Erster Spieltest“ (Teil E)
6. Nicht behaupten: Client-Start, Mehrspieler, FPS – das testet erst Leon

## E) Messpunkte für den ersten Spieltest (in README „Erster Spieltest“)
1. **Frühspiel:** Minuten bis „Erster Eisenbarren“ (`e_eisen`). Ziel unter ~30 min. Wenn deutlich mehr: Siebchancen/Startinventar prüfen.
2. **Create-Einstieg:** Gibt es einen Hänger zwischen Sieb und Messing (Lohenpulver, Lohenbrenner)? Notieren, wo.
3. **Leistung:** Nach 10 min `/spark tps` und `/spark health --memory`, FPS (F3) am Laptop mit Sichtweite 8. Ziel 20 TPS, RAM unter 80 %.
4. **Mystical Agriculture:** Wann ersetzt die erste Ressourcen-Saat das Sieben? Fühlt sich Tertium (Mixer + Messing) hart oder fair an?
5. **Belohnungen:** Wie viele Mob-Kisten nach 1 Stunde Mob-Farm? Wird der Inselmarkt überhaupt genutzt?

## Offen für Leon
- Nichts: Alle Entscheidungen sind getroffen (A1 lösen, A2 ja, A3 ja, A4 Magie oder Maschinen, A5 optional).

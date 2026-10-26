# Gemini: längere Hauptstory (Ziel 55–65 Quests)

Stand: 25.10.2026 · Gemini lief wegen Tageslimit (429) nur mit **gemini-3.5-flash-lite** · Eingabe: aktuelle Quest-Liste aus `quests.py` (189 Quests, AKT1–3 mit 35)
Gegencheck **[C]**: Vorschlag automatisch in eine Kopie von `_src` eingebaut (AKT1–3 ersetzt, Mod-Kapitel geben verschobene Quests ab), dann `pruefe_struktur()`, Reihenfolge-, Doppel- und Zyklus-Test sowie der komplette Generator inkl. Item-ID-Prüfung.

## [C] Ergebnis des Gegenchecks

**Geminis Vorschlag hat Fehler:**
1. **Zyklus:** `('m_altar', 'm_inferium')`, aber `m_inferium` hängt selbst an `m_altar` → Kreis. Richtig: Altar vor Inferium-Samen.
2. **`z_weg` fehlt** (Finale „Maschine oder Magie“) → „z_weg in keinem Kapitel“.
3. **`c_extruder` steht in Akt I hinter dem Lava-Tiegel**, braucht aber Mühlstein/Andesit (kommen später) → falsche Reihenfolge.
4. **Zählfehler:** Gemini schreibt 65, es sind **73** (29/25/19).

**Korrigierte Fassung (getestet: 0 Fehler, keine Zyklen, Reihenfolge ok, Generator läuft, 68 Hauptstory-Quests = 27/21/20):**
Gestrichen gegenüber Gemini (nicht nötig für den roten Faden, bleiben in den Mod-Kapiteln): `e_haken` (Haken im Startinventar, erledigt sich sofort), `k_separator`, `s_orb`, `s_stahl` (Powah ist ein Seitenweg), `m_kupfer`, `k_fortschritt` (Voraussetzung des Jetpacks, bleibt im Mekanism-Kapitel). Für genau 65: zusätzlich `e_lavatiegel`, `k_schalt`, `j_festung` herausnehmen.

```python
AKT1 = [
    ('w_start', None), ('e_holz', 'w_start'), ('e_raupe', 'e_holz'), ('e_fass', 'e_holz'), ('e_cobble', 'e_fass'),
    ('e_hammer', 'e_cobble'), ('e_sieb', 'e_hammer'), ('e_tiegel', 'e_sieb'), ('e_lavatiegel', 'e_tiegel'),
    ('e_brocken', 'e_sieb'), ('e_feuernetz', 'e_brocken'), ('e_eisen', 'e_feuernetz'),
    ('m_altar', 'e_eisen'), ('m_inferium', 'm_altar'), ('m_prudentium', 'm_inferium'),
    ('e_kupfer', 'e_eisen'), ('c_andesit', 'e_kupfer'), ('c_rad', 'c_andesit'), ('c_muehle', 'c_rad'), ('c_sifter', 'c_muehle'),
    ('c_extruder', 'c_muehle'), ('c_presse', 'c_rad'), ('c_fan', 'c_presse'), ('c_mixer', 'c_presse'), ('c_brenner', 'c_mixer'),
    ('c_messing', 'c_brenner'), ('c_siebfabrik', 'c_messing'),
]
AKT2 = [
    ('c_mechanismus', 'c_messing'), ('c_alternator', 'c_mechanismus'), ('k_osmium', 'c_alternator'), ('k_infuser', 'k_osmium'),
    ('k_alloy', 'k_infuser'), ('k_schalt', 'k_infuser'), ('k_enrich', 'k_infuser'), ('k_purif', 'k_enrich'), ('k_inject', 'k_purif'),
    ('m_tertium', 'c_messing'), ('m_eisen', 'm_tertium'),
    ('j_obsidian', 'e_eisen'), ('j_nether', 'j_obsidian'), ('j_festung', 'j_nether'), ('j_lohe', 'j_festung'),
    ('k_jetpack', 'k_alloy'),
    ('l_certus', 'e_eisen'), ('l_lader', 'l_certus'), ('l_inscriber', 'm_tertium'), ('l_prozessoren', 'l_inscriber'), ('l_netz', 'l_prozessoren'),
]
AKT3 = [
    ('l_auto', 'l_netz'), ('m_imperium', 'k_alloy'), ('m_supremium', 'm_imperium'), ('m_niemehr', 'm_supremium'),
    ('j_hexe', 'j_nether'), ('j_wither', 'j_hexe'), ('j_perlen', 'j_obsidian'), ('j_augen', 'j_perlen'), ('j_rahmen', 'j_augen'),
    ('j_end', 'j_rahmen'), ('j_drache', 'j_end'),
    ('z_elite', 'k_inject'), ('z_ultkreis', 'z_elite'), ('m_insanium', 'z_ultkreis'),
    ('k_spalt', 'z_elite'), ('k_polonium', 'k_spalt'), ('z_sps', 'k_polonium'),
    ('z_fabrik', 'z_sps'), ('z_weg', None), ('z_herr', 'z_fabrik'),
]
```

**Einbau-Hinweise:**
- Damit keine Quest doppelt in einem Kapitel steht, müssen Mod-Kapitel die Hauptstory-Quests abgeben. Im Test reichte in `kap()`: `if group == 'mods': keys = [k for k in keys if k not in <alle AKT-Schlüssel>]`.
- **Mod-Kapitel werden dadurch dünn** (Ex Deorum hätte nur noch 5 Quests). Empfehlung: Die abgegebenen Schlüssel automatisch als `links` (Verweise) im Mod-Kapitel anzeigen. Dann bleibt jedes Kapitel vollständig lesbar.
- `k_spalt` steht im Test in Akt III, also aus `mekanism`-Kapitelliste nehmen (passiert automatisch mit dem Filter oben).
- Story-Seitenäste prüfen: `st_` hängen nur an HAUPT_KEYS. Durch die neuen Hauptstory-Quests ändert sich das nicht (der Test meldet keine Story-Fehler).

---

## Geminis Originalantwort (unverändert)

```python
AKT1 = [
    ('w_start', None),
    ('e_holz', 'w_start'),
    ('e_haken', 'e_holz'),
    ('e_raupe', 'e_haken'),
    ('e_fass', 'e_raupe'),
    ('e_cobble', 'e_fass'),
    ('e_hammer', 'e_cobble'),
    ('e_sieb', 'e_hammer'),
    ('e_tiegel', 'e_sieb'),
    ('e_lavatiegel', 'e_tiegel'),
    ('c_extruder', 'e_lavatiegel'),
    ('e_brocken', 'e_sieb'),
    ('e_feuernetz', 'e_brocken'),
    ('e_eisen', 'e_feuernetz'),
    ('m_inferium', 'e_eisen'),
    ('m_altar', 'm_inferium'),
    ('m_prudentium', 'm_altar'),
    ('e_kupfer', 'e_eisen'),
    ('c_andesit', 'e_kupfer'),
    ('c_rad', 'c_andesit'),
    ('c_muehle', 'c_rad'),
    ('c_presse', 'c_rad'),
    ('c_fan', 'c_presse'),
    ('c_mixer', 'c_presse'),
    ('c_brenner', 'c_mixer'),
    ('c_sifter', 'c_muehle'),
    ('c_messing', 'c_brenner'),
    ('c_mechanismus', 'c_messing'),
    ('c_siebfabrik', 'c_messing'),
]

AKT2 = [
    ('c_alternator', 'c_mechanismus'),
    ('s_orb', 'c_alternator'),
    ('s_stahl', 's_orb'),
    ('k_osmium', 'c_alternator'),
    ('k_infuser', 'k_osmium'),
    ('k_alloy', 'k_infuser'),
    ('k_schalt', 'k_infuser'),
    ('k_enrich', 'k_infuser'),
    ('k_separator', 'k_enrich'),
    ('k_purif', 'k_enrich'),
    ('k_inject', 'k_enrich'),
    ('m_tertium', 'c_messing'),
    ('m_eisen', 'm_tertium'),
    ('m_kupfer', 'm_tertium'),
    ('j_obsidian', 'e_eisen'),
    ('j_nether', 'j_obsidian'),
    ('j_festung', 'j_nether'),
    ('j_lohe', 'j_festung'),
    ('k_fortschritt', 'k_alloy'),
    ('k_jetpack', 'k_fortschritt'),
    ('l_certus', 'e_eisen'),
    ('l_lader', 'l_certus'),
    ('l_inscriber', 'm_tertium'),
    ('l_prozessoren', 'l_inscriber'),
    ('l_netz', 'l_prozessoren'),
]

AKT3 = [
    ('l_auto', 'l_netz'),
    ('m_imperium', 'k_alloy'),
    ('m_supremium', 'l_prozessoren'),
    ('m_niemehr', 'm_supremium'),
    ('j_hexe', 'j_nether'),
    ('j_wither', 'j_hexe'),
    ('j_perlen', 'j_obsidian'),
    ('j_augen', 'j_lohe'),
    ('j_rahmen', 'j_augen'),
    ('j_end', 'j_rahmen'),
    ('j_drache', 'j_end'),
    ('z_elite', 'k_inject'),
    ('z_ultkreis', 'z_elite'),
    ('m_insanium', 'z_ultkreis'),
    ('k_spalt', 'z_elite'),
    ('k_polonium', 'k_spalt'),
    ('z_sps', 'k_polonium'),
    ('z_fabrik', 'z_sps'),
    ('z_herr', 'j_drache'),
]
```

### Hauptstory-Tabelle

| Schlüssel | Vorgänger | Warum in der Hauptlinie (max. 8 Wörter) |
|---|---|---|
| w_start | None | Start der Himmelsinsel. |
| e_holz | w_start | Holz vom ersten Eichenbaum. |
| e_haken | e_holz | Laub mit Haken abbauen. |
| e_raupe | e_haken | Seidenraupen für Fäden züchten. |
| e_fass | e_raupe | Kompostfass für Erde bauen. |
| e_cobble | e_fass | Bruchstein-Generator in der Leere. |
| e_hammer | e_cobble | Hammer zerkleinert Bruchstein. |
| e_sieb | e_hammer | Sieb für erste Erze. |
| e_tiegel | e_sieb | Tiegel schmilzt Wasser. |
| e_lavatiegel | e_tiegel | Lava für Generatoren gewinnen. |
| e_brocken | e_sieb | Erzbrocken aus dem Sieb. |
| e_feuernetz | e_brocken | Feuersteinnetz für Siebe. |
| e_eisen | e_feuernetz | Erster echter Eisenbarren. |
| m_inferium | e_eisen | Magische Inferium-Samen pflanzen. |
| m_altar | m_inferium | Infusionsaltar für Mystical Agriculture. |
| m_prudentium | m_altar | Aufwertung zu Prudentium. |
| e_kupfer | e_eisen | Kupfer und Zink schmelzen. |
| c_andesit | e_kupfer | Andesit-Legierung für Create. |
| c_rad | c_andesit | Wasserrad liefert Create-Kraft. |
| c_muehle | c_rad | Mühlstein zerkleinert Materialien. |
| c_extruder | e_lavatiegel | Mechanischer Extruder für Materialien. |
| c_presse | c_rad | Mechanische Presse formt Platten. |
| c_fan | c_presse | Gießkanten-Ventilator zum Waschen. |
| c_mixer | c_presse | Mixer mischt Legierungen. |
| c_brenner | c_mixer | Lohenbrenner beheizt Becken. |
| c_sifter | c_muehle | Create-Sifter automatisiert das Sieben. |
| c_messing | c_brenner | Messinglegierung für Maschinen. |
| c_mechanismus | c_messing | Präzisionsmechanismus für Getriebe. |
| c_siebfabrik | c_messing | Großes Sieb-Netzwerk aufbauen. |
| c_alternator | c_mechanismus | Stromerzeugung via Rotationskraft. |
| s_orb | c_alternator | Energizing Orb für Stahl. |
| s_stahl | s_orb | Energetisierter Stahl für Powah. |
| k_osmium | c_alternator | Osmium für Mekanism abbauen. |
| k_infuser | k_osmium | Metallurgic Infuser verarbeitet Metalle. |
| k_alloy | k_infuser | Infused Alloy für Upgrades. |
| k_schalt | k_infuser | Grundschaltkreis für Mekanism. |
| k_enrich | k_infuser | Enrichment Chamber verdoppelt Erze. |
| k_separator | k_enrich | Elektrolysezelle trennt Gase. |
| k_purif | k_enrich | Reinigunskammer für Stufe 3. |
| k_inject | k_enrich | Chemical Injection Chamber für Vierfach. |
| m_tertium | c_messing | Stufe 3: Tertium-Essenzen. |
| m_eisen | m_tertium | Eisensamen für endliche Rohstoffe. |
| m_kupfer | m_tertium | Kupfersamen für endliche Rohstoffe. |
| j_obsidian | e_eisen | Obsidian für Portale gießen. |
| j_nether | j_obsidian | Portal in den Nether öffnen. |
| j_festung | j_nether | Netherfestung erkunden. |
| j_lohe | j_festung | Lohenruten für Zauber und Tränke. |
| k_fortschritt | k_alloy | Fortgeschrittener Schaltkreis. |
| k_jetpack | k_fortschritt | Jetpack für Flugfähigkeit. |
| l_certus | e_eisen | Certus-Quarz für AE2 finden. |
| l_lader | l_certus | Charger und Fluix-Kristalle. |
| l_inscriber | m_tertium | Inscriber presst AE2-Prozessoren. |
| l_prozessoren | l_inscriber | AE2-Prozessoren herstellen. |
| l_netz | l_prozessoren | ME-Netzwerk zentralisiert Lagerung. |
| l_auto | l_netz | Crafting-System und Auto-Crafting. |
| m_imperium | k_alloy | Stufe 4: Imperium-Essenzen. |
| m_supremium | l_prozessoren | Stufe 5: Supremium-Essenzen. |
| m_niemehr | m_supremium | Ressourcensamen für alle Erze. |
| j_hexe | j_nether | Hexenwasser für Wither-Schmiede. |
| j_wither | j_hexe | Netherstern vom Wither boss. |
| j_perlen | j_obsidian | Enderperlen für Enderauge. |
| j_augen | j_lohe | Enderaugen für Endportal. |
| j_rahmen | j_augen | Portalrahmen aktivieren. |
| j_end | j_rahmen | Reise ins End-Dimension. |
| j_drache | j_end | Enderdrache besiegen. |
| z_elite | k_inject | Elite-Schaltkreis für High-Tech. |
| z_ultkreis | z_elite | Ultimate-Schaltkreis für Endgegner. |
| m_insanium | z_ultkreis | Stufe 6: Insanium-Essenz. |
| k_spalt | z_elite | Spaltreaktor erzeugt Radioaktivität. |
| k_polonium | k_spalt | Polonium-Pellets herstellen. |
| z_sps | k_polonium | Antimaterie im SPS erzeugen. |
| z_fabrik | z_sps | Die ultimative Fabrik errichten. |
| z_herr | j_drache | Erbe der Ewigkeit vollenden. |

**Gesamtzahl Quests in der Hauptstory:** 65 (Akt I: 29, Akt II: 25, Akt III: 19)

### 0–5 fehlende Schritte (optional)
*Keine fehlenden Schritte, da alle Lücken mit vorhandenen Schlüsseln geschlossen werden konnten.*

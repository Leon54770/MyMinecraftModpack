# Gemini zum Questbuch-Umbau

Stand: 25.10.2026 · Modell: gemini-3.6-flash (mit Nachdenken) · Eingabe: `_src/QUEST-LISTE-0.5.txt` + Leons 4 Wünsche
Von Claude gegengeprüft. **[C]** = Korrektur oder Urteil von Claude. Die Gemini-Texte darunter sind unverändert.

## [C] Korrekturen zuerst

**Aufgabe B (Hauptstory):**
1. **Messing ist zu spät.** `c_alternator` (Frühspiel Nr. 11) braucht `c_mechanismus`, und der braucht `c_messing`. Deshalb `c_brenner` → `c_messing` → `c_mechanismus` ins Frühspiel vor `c_alternator`, und `c_messing` aus „Mitte“ streichen.
2. **Insanium braucht den Ultimate-Schaltkreis**, nicht den Elite (balance.js 0.5.0). Im Endspiel nach `z_elite` einen Schritt „Ultimate-Schaltkreis“ (`mekanism:ultimate_control_circuit`) einfügen, dann `m_insanium`.
3. **Wither und Netherstern-Saat fehlen**, obwohl `z_fabrik` 2 Nethersterne verlangt. Ins Endspiel vor `z_fabrik`: `j_wither` (Netherstern) und `z_netherstern` (Netherstern-Samen, braucht Insanium).
4. Mitte: `m_tertium` (MA-Kapitel) statt `c_tertium` nehmen, denn Gemini legt beide in A ohnehin zusammen.
5. Finale `z_herr`: Gemini nennt in B „Erzmagier-Buch + 4 Ultimate-Schaltkreise“, in A „Drachenei“. Vorschlag: **Drachenei** (eindeutig, automatisch erkennbar). Die Abhängigkeiten von z_fabrik/j_drache/m_niemehr/a_erzmagier sorgen schon dafür, dass Technik und Magie dabei sind.

**Aufgabe A (Einordnung):**
6. `h_boss` → Geminis Ersatz `hostilenetworks:prediction` ist **ungeeignet**: Jede Vorhersage von jedem Mob zählt, die Stufe „Self Aware“ prüft das nicht. Entweder STREICHEN (h_fab bleibt Kapitelziel) oder eine Item-Aufgabe mit Komponenten-Abgleich auf das Wither-Datenmodell (nur wenn FTB Quests den Datenwert sicher prüfen kann, sonst streichen).
7. Tutorial-Haken (`w_wachsen`, `w_ernte`, `w_jei`, `w_ultimine`, `w_karte`, `w_team`): Streichen ist richtig, aber **die Tipps nicht verlieren**. Sie gehören in die Beschreibung von `w_start` bzw. der ersten passenden Item-Quest (z. B. Ultimine-Tipp bei `e_holz`, Ducken/Ernten bei `g_feld`).
8. `x_markt` streichen geht nur, wenn die Tausch-Quests stattdessen direkt von `e_eisen` abhängen. Die Kapitelbeschreibung übernimmt den Infotext.
9. Prüfungen (`p_kompakt` … `p_wither`, `z_versiegeln`): Streichen passt zu Wunsch (1). Die Sammlerbuch-Quests (Item-Aufgaben) bleiben, ihr Abhängigkeits-Start `p_start` wird durch `e_eisen` ersetzt.
10. Baumeister: Ohne `u_haus` … `u_meister` bleiben nur 3 Quests (`u_meissel`, `u_framed`, `u_gadget`). Vorschlag: ins Kapitel „Bauen“ oder als kleiner Ast in „Insel & Sieb“, kein eigenes Kapitel nötig.

Zahlen aus A: 202 Quests → 136 behalten, 37 Hauptstory-Kandidaten, 23 streichen, 6 zusammenlegen (Gemini schreibt oben fälschlich „176“, die Tabelle hat alle 202).

---

## Gemini: Aufgabe A – Einordnung aller Quests
Hier ist die vollständige Einordnung aller 176 Quests gemäß den Richtlinien. Alle Haken-Quests wurden entweder gestrichen oder durch konkrete Items/Aufgaben ersetzt.

### AUFGABE A: Quest-Einordnung

| Schlüssel | Urteil | Ziel-Kapitel bzw. Partner-Quest | Kurzgrund (max. 4 Worte) |
|---|---|---|---|
| **w_start** | HAUPTSTORY | Insel & Sieb | Neu: `minecraft:oak_sapling×1` |
| **w_wachsen** | STREICHEN | - | Unnötiges Tutorial |
| **w_ernte** | STREICHEN | - | Unnötiges Tutorial |
| **w_jei** | STREICHEN | - | Unnötiges Tutorial |
| **w_ultimine** | STREICHEN | - | Unnötiges Tutorial |
| **w_karte** | STREICHEN | - | Unnötiges Tutorial |
| **w_team** | STREICHEN | - | Unnötiges Tutorial |
| **w_los** | STREICHEN | - | Ersetzt durch e_holz |
| **e_holz** | HAUPTSTORY | Insel & Sieb | Grundressource Holz |
| **e_haken** | BEHALTEN | Insel & Sieb | Fadenbeschaffung |
| **e_raupe** | BEHALTEN | Insel & Sieb | Seidenraupe für Faden |
| **e_faden** | ZUSAMMENLEGEN | e_raupe | Redundant zu Raupe |
| **e_fass** | BEHALTEN | Insel & Sieb | Kompostierung |
| **e_cobble** | HAUPTSTORY | Insel & Sieb | Bruchstein-Basis |
| **e_hammer** | BEHALTEN | Insel & Sieb | Kies- und Sandgewinnung |
| **e_sieb** | HAUPTSTORY | Insel & Sieb | Kernelement Skyblock |
| **e_samen** | BEHALTEN | Landwirtschaft & Küche | Start Landwirtschaft |
| **e_tiegel** | BEHALTEN | Insel & Sieb | Wassererzeugung |
| **e_porzellan** | ZUSAMMENLEGEN | e_lavatiegel | Zwischenschritt Porzellan |
| **e_lavatiegel** | HAUPTSTORY | Insel & Sieb | Lavaerzeugung |
| **e_brocken** | BEHALTEN | Insel & Sieb | Erste Erze |
| **e_feuernetz** | BEHALTEN | Insel & Sieb | Sieb-Upgrade |
| **e_eisen** | HAUPTSTORY | Insel & Sieb | Meilenstein Eisen |
| **e_kupfer** | BEHALTEN | Insel & Sieb | Basis-Metalle |
| **e_eisennetz** | BEHALTEN | Insel & Sieb | Hohe Siebeffizienz |
| **e_kanne** | BEHALTEN | Landwirtschaft & Küche | Beschleunigung Pflanzen |
| **g_feld** | BEHALTEN | Landwirtschaft & Küche | Nahrungsproduktion |
| **g_brett** | BEHALTEN | Landwirtschaft & Küche | Küchen-Einstieg |
| **g_topf** | BEHALTEN | Landwirtschaft & Küche | Essenszubereitung |
| **g_tiere** | BEHALTEN | Landwirtschaft & Küche | Tierische Produkte |
| **g_topf_pflanze** | BEHALTEN | Landwirtschaft & Küche | Pflanzen-Automatisierung |
| **g_baumtopf** | BEHALTEN | Landwirtschaft & Küche | Automatische Holzgewinnung |
| **g_festessen** | BEHALTEN | Landwirtschaft & Küche | High-End Nahrung |
| **g_inferium** | HAUPTSTORY | Mystical Agriculture | Übergang Magie-Ackerbau |
| **g_autark** | STREICHEN | - | Unkonkrete Haken-Quest |
| **c_andesit** | HAUPTSTORY | Create | Create-Startkomponente |
| **c_rad** | BEHALTEN | Create | Kinetische Energie |
| **c_muehle** | BEHALTEN | Create | Automatisches Mahlen |
| **c_sifter** | BEHALTEN | Create | Automatisches Sieben |
| **c_netze** | ZUSAMMENLEGEN | c_sifter | Redundantes Netz-Upgrade |
| **c_extruder** | BEHALTEN | Create | Stein-Generierung |
| **c_presse** | BEHALTEN | Create | Metallverarbeitung |
| **c_fan** | BEHALTEN | Create | Waschen und Braten |
| **c_mixer** | HAUPTSTORY | Create | Legierungsherstellung |
| **c_messing** | HAUPTSTORY | Create | Meilenstein Messing |
| **c_brenner** | BEHALTEN | Create | Hitzequelle |
| **c_tertium** | ZUSAMMENLEGEN | m_tertium | Doppelung zu MA |
| **c_mechanismus** | HAUPTSTORY | Create | Präzisionsbauteile |
| **c_alternator** | BEHALTEN | Create | Strom aus Kinetik |
| **c_siebfabrik** | BEHALTEN | Create | Automatisierungs-Großprojekt |
| **c_deployer** | BEHALTEN | Create | Kinetische Interaktion |
| **c_crafter** | BEHALTEN | Create | Mechanisches Autocrafting |
| **s_draht** | HAUPTSTORY | Strom (Powah/Pipez) | Verkabelung |
| **s_akku** | BEHALTEN | Strom (Powah/Pipez) | Energiespeicherung |
| **s_mechsieb** | BEHALTEN | Strom (Powah/Pipez) | Elektrisches Sieben |
| **s_mechhammer** | BEHALTEN | Strom (Powah/Pipez) | Elektrisches Zerkleinern |
| **s_paste** | BEHALTEN | Strom (Powah/Pipez) | Powah-Grundstoff |
| **s_orb** | HAUPTSTORY | Strom (Powah/Pipez) | Powah-Fertigung |
| **s_stahl** | BEHALTEN | Strom (Powah/Pipez) | Energetisiertes Metall |
| **s_furnator** | BEHALTEN | Strom (Powah/Pipez) | Verbrennungsenergie |
| **s_solar** | BEHALTEN | Strom (Powah/Pipez) | Passive Solarenergie |
| **s_kristall** | BEHALTEN | Strom (Powah/Pipez) | Höheres Powah-Tier |
| **s_pipe** | BEHALTEN | Strom (Powah/Pipez) | Logistik-Leitungen |
| **s_upgrade** | BEHALTEN | Strom (Powah/Pipez) | Rohr-Upgrades |
| **s_reaktor** | HAUPTSTORY | Strom (Powah/Pipez) | Netzstrom-Reaktor |
| **k_osmium** | HAUPTSTORY | Mekanism | Mekanism-Einstieg |
| **k_infuser** | HAUPTSTORY | Mekanism | Basis-Maschine Mekanism |
| **k_stahl** | BEHALTEN | Mekanism | Mekanism-Stahl |
| **k_schalt** | HAUPTSTORY | Mekanism | Grundlegende Elektronik |
| **k_enrich** | BEHALTEN | Mekanism | Erzverdopplung |
| **k_alloy** | BEHALTEN | Mekanism | Veredelte Legierung |
| **k_purif** | BEHALTEN | Mekanism | Erzverdreifachung |
| **k_separator** | BEHALTEN | Mekanism | Gas-Gewinnung |
| **k_inject** | HAUPTSTORY | Mekanism | Erzvierfachung |
| **k_x5** | BEHALTEN | Mekanism | Erzfünffachung |
| **k_kabel** | BEHALTEN | Mekanism | Stromkabel |
| **k_cube** | BEHALTEN | Mekanism | Energiespeicher |
| **k_fortschritt** | BEHALTEN | Mekanism | Fortgeschrittene Schaltkreise |
| **k_jetpack** | BEHALTEN | Mekanism | Personentransport |
| **k_tiab** | BEHALTEN | Mekanism | Zeitbeschleunigung |
| **k_meka** | BEHALTEN | Mekanism | Multitool |
| **l_rucksack** | BEHALTEN | Lager & AE2 | Mobiles Lager |
| **l_pickup** | ZUSAMMENLEGEN | l_rucksack | Rucksack-Erweiterung |
| **l_fass** | BEHALTEN | Lager & AE2 | Einzelblock-Lagerung |
| **l_schubladen** | BEHALTEN | Lager & AE2 | Massengut-Lager |
| **l_controller** | BEHALTEN | Lager & AE2 | Zentrierte Schubladen-Steuerung |
| **l_muell** | BEHALTEN | Lager & AE2 | Items entsorgen |
| **l_certus** | HAUPTSTORY | Lager & AE2 | AE2-Einstiegsmaterial |
| **l_lader** | BEHALTEN | Lager & AE2 | Kristall-Aufladung |
| **l_fluix** | BEHALTEN | Lager & AE2 | AE2-Grundstoff |
| **l_inscriber** | HAUPTSTORY | Lager & AE2 | Prozessor-Pressen |
| **l_prozessoren** | HAUPTSTORY | Lager & AE2 | AE2-Prozessoren |
| **l_netz** | HAUPTSTORY | Lager & AE2 | Digitales Lagernetzwerk |
| **l_auto** | HAUPTSTORY | Lager & AE2 | Digitales Autocrafting |
| **l_wireless** | BEHALTEN | Lager & AE2 | Drahtloser Terminal-Zugriff |
| **l_appmek** | BEHALTEN | Lager & AE2 | Mekanism-Netzintegration |
| **l_mega** | BEHALTEN | Lager & AE2 | Endstufe Speicherzellen |
| **m_altar** | HAUPTSTORY | Mystical Agriculture | Essenz-Infusion |
| **m_inferium** | BEHALTEN | Mystical Agriculture | Basis-Samen |
| **m_prudentium** | BEHALTEN | Mystical Agriculture | Tier-2-Essenz |
| **m_eisen** | BEHALTEN | Mystical Agriculture | Erze anbauen |
| **m_kupfer** | BEHALTEN | Mystical Agriculture | Metalle anbauen |
| **m_tertium** | BEHALTEN | Mystical Agriculture | Tier-3-Essenz |
| **m_gold** | BEHALTEN | Mystical Agriculture | Edelmetalle anbauen |
| **m_imperium** | BEHALTEN | Mystical Agriculture | Tier-4-Essenz |
| **m_diamant** | BEHALTEN | Mystical Agriculture | Edelsteine anbauen |
| **m_beschleuniger** | BEHALTEN | Mystical Agriculture | Erntebeschleunigung |
| **m_acker** | BEHALTEN | Mystical Agriculture | Spezial-Ackerland |
| **m_supremium** | BEHALTEN | Mystical Agriculture | Tier-5-Essenz |
| **m_niemehr** | HAUPTSTORY | Mystical Agriculture | Vollständiger Sieb-Ersatz |
| **m_insanium** | BEHALTEN | Mystical Agriculture | Tier-6-Essenz |
| **a_quelle** | HAUPTSTORY | Ars Nouveau | Magie-Einstieg |
| **a_kammer** | BEHALTEN | Ars Nouveau | Magie-Infusion |
| **a_buch** | BEHALTEN | Ars Nouveau | Zaubersprüche |
| **a_tisch** | BEHALTEN | Ars Nouveau | Magische Schriftrollen |
| **a_glas** | BEHALTEN | Ars Nouveau | Quellenergie-Speicher |
| **a_archwood** | BEHALTEN | Ars Nouveau | Magisches Holz |
| **a_starbuncle** | BEHALTEN | Ars Nouveau | Magischer Itemtransport |
| **a_drygmy** | BEHALTEN | Ars Nouveau | Magische Mob-Farm |
| **a_wilden** | BEHALTEN | Ars Nouveau | Magische Beute |
| **a_apparat** | HAUPTSTORY | Ars Nouveau | Magische Rekonstruktion |
| **a_ritual** | BEHALTEN | Ars Nouveau | Ritualausführung |
| **a_crush** | BEHALTEN | Ars Nouveau | Magisches Zerkleinern |
| **a_wixie** | BEHALTEN | Ars Nouveau | Magisches Autocrafting |
| **a_whirli** | BEHALTEN | Ars Nouveau | Magische Ernte |
| **a_erzmagier** | HAUPTSTORY | Ars Nouveau | Höchste Magiestufe |
| **b_biene** | BEHALTEN | Bienen | Bienen-Einstieg |
| **b_stock** | BEHALTEN | Bienen | Bienenbehausung |
| **b_zentri** | BEHALTEN | Bienen | Wabenverarbeitung |
| **b_nest** | BEHALTEN | Bienen | Wildbienen-Nester |
| **b_zucht** | BEHALTEN | Bienen | Mutations-Futter |
| **b_upgrade** | BEHALTEN | Bienen | Bienenstock-Upgrades |
| **j_obsidian** | HAUPTSTORY | Nether & End | Torbau-Material |
| **j_nether** | HAUPTSTORY | Nether & End | Dimension betreten |
| **j_festung** | BEHALTEN | Nether & End | Festungsmaterial |
| **j_lohe** | HAUPTSTORY | Nether & End | Lohen-Material |
| **j_brenner** | ZUSAMMENLEGEN | j_lohe | Unnötiger Ressourcenverbrauch |
| **j_hexe** | BEHALTEN | Nether & End | Wither-Vorbereitung |
| **j_wither** | HAUPTSTORY | Nether & End | Boss-Kampf Wither |
| **j_perlen** | BEHALTEN | Nether & End | Teleportation |
| **j_augen** | BEHALTEN | Nether & End | Portalfindung |
| **j_rahmen** | BEHALTEN | Nether & End | Endportalbau |
| **j_end** | HAUPTSTORY | Nether & End | Das End betreten |
| **j_drache** | HAUPTSTORY | Nether & End | Kill: `minecraft:ender_dragon` |
| **j_shulker** | BEHALTEN | Nether & End | Shulker-Kisten |
| **h_learner** | BEHALTEN | Maschinengeist (HNN/IF) | Mob-Daten sammeln |
| **h_modell** | BEHALTEN | Maschinengeist (HNN/IF) | Unbeschriebenes Datenmodell |
| **h_sim** | BEHALTEN | Maschinengeist (HNN/IF) | Virtuelle Simulation |
| **h_fab** | BEHALTEN | Maschinengeist (HNN/IF) | Beutegenerierung |
| **h_boss** | BEHALTEN | Maschinengeist (HNN/IF) | Neu: `hostilenetworks:prediction×1` |
| **h_rahmen** | HAUPTSTORY | Maschinengeist (HNN/IF) | Industrial Foregoing Einstieg |
| **h_plastik** | BEHALTEN | Maschinengeist (HNN/IF) | IF-Kunststoff |
| **h_laser** | BEHALTEN | Maschinengeist (HNN/IF) | Erz-Laserbohrer |
| **u_meissel** | BEHALTEN | Bauen | Blockvariationen |
| **u_haus** | STREICHEN | - | Nicht automatisierbar |
| **u_moebel** | STREICHEN | - | Nicht automatisierbar |
| **u_bruecke** | STREICHEN | - | Nicht automatisierbar |
| **u_garten** | STREICHEN | - | Nicht automatisierbar |
| **u_framed** | BEHALTEN | Bauen | Benutzerdefinierte Formen |
| **u_gadget** | BEHALTEN | Bauen | Bauwerkzeug |
| **u_meister** | STREICHEN | - | Nicht automatisierbar |
| **x_markt** | STREICHEN | - | Rein dekorativ |
| **x_samen** | BEHALTEN | Markt | Handel: Saatgut |
| **x_kies** | BEHALTEN | Markt | Handel: Kies |
| **x_cobble** | BEHALTEN | Markt | Handel: Bruchstein |
| **x_fleisch** | BEHALTEN | Markt | Handel: Verrottetes Fleisch |
| **x_inferium** | BEHALTEN | Markt | Handel: Inferium |
| **x_mehl** | BEHALTEN | Markt | Handel: Weizenmehl |
| **x_seetang** | BEHALTEN | Markt | Handel: Getrockneter Seetang |
| **x_honig** | BEHALTEN | Markt | Handel: Honigwaben |
| **x_warze** | BEHALTEN | Markt | Handel: Netherwarzen |
| **x_knochen** | BEHALTEN | Markt | Handel: Knochen |
| **x_perlen** | BEHALTEN | Markt | Handel: Enderperlen |
| **x_lohe** | BEHALTEN | Markt | Handel: Lohenruten |
| **x_quelle** | BEHALTEN | Markt | Handel: Quellsteine |
| **x_polonium** | BEHALTEN | Markt | Handel: Polonium |
| **x_stern** | BEHALTEN | Markt | Handel: Nethersterne |
| **x_antimaterie** | BEHALTEN | Markt | Handel: Antimaterie |
| **x_supremium** | BEHALTEN | Markt | Handel: Supremium |
| **x_mechanik** | BEHALTEN | Markt | Handel: Präzisionsmechanismen |
| **p_start** | STREICHEN | - | Unnötige Checkmark |
| **p_kompakt** | STREICHEN | - | Nicht automatisierbar |
| **p_ohnebrenn** | STREICHEN | - | Nicht automatisierbar |
| **p_ohnerohr** | STREICHEN | - | Nicht automatisierbar |
| **p_vierfach** | STREICHEN | - | Nicht automatisierbar |
| **p_nether** | STREICHEN | - | Nicht automatisierbar |
| **p_ohnesieb** | STREICHEN | - | Nicht automatisierbar |
| **p_wither** | STREICHEN | - | Nicht automatisierbar |
| **p_essenzen** | BEHALTEN | Mystical Agriculture | Essenzen-Kollektion |
| **p_netze** | BEHALTEN | Insel & Sieb | Netze-Kollektion |
| **p_archwood** | BEHALTEN | Ars Nouveau | Baum-Kollektion |
| **p_trophaeen** | BEHALTEN | Nether & End | Trophäen-Kollektion |
| **z_elite** | BEHALTEN | Finale | Elite-Elektronik |
| **z_ultimate** | BEHALTEN | Finale | Maximale Rohr-Upgrades |
| **z_strom** | BEHALTEN | Finale | Großkraftwerk |
| **z_insanium** | BEHALTEN | Finale | Höchste Essenz-Menge |
| **z_netherstern** | BEHALTEN | Finale | Unendliche Sterne |
| **z_sps** | BEHALTEN | Finale | Antimaterie-Produktion |
| **z_meka** | BEHALTEN | Finale | Endgame-Rüstung |
| **z_fabrik** | HAUPTSTORY | Finale | Finale Endgame-Komponenten |
| **z_versiegeln** | STREICHEN | - | Nicht automatisierbar |
| **z_herr** | HAUPTSTORY | Finale | Neu: `minecraft:dragon_egg×1` |

---

## Gemini: Aufgabe B – Hauptstory-Vorschlag
Hier ist die dreiteilige Hauptstory-Linie, basierend ausschließlich auf den vorhanden Quests und unter Berücksichtigung aller Stufen-Sperren sowie automatischen Prüfungen.

---

### Kapitel 1: Frühspiel (Von der Leere zur Siebfabrik)

Nr | Schlüssel | Titel | Aufgabe | warum dieser Schritt
---|---|---|---|---
1 | `e_holz` | Der Baum ist dein Freund | `minecraft:oak_log×8` | Grundmaterial für Werkzeuge, Fässer und Siebe.
2 | `e_hammer` | Hammerzeit | `exdeorum:stone_hammer×1` | Zerkleinert Bruchstein zu Kies, Sand und Staub.
3 | `e_sieb` | Das Sieb | `exdeorum:oak_sieve×1, exdeorum:string_mesh×1` | Erste manuelle Gewinnung von Erzen aus Siebgut.
4 | `e_eisen` | Erster Eisenbarren | `minecraft:iron_ingot×4` | Schaltet die Eisenzeit und bessere Werkzeuge frei.
5 | `e_kupfer` | Kupfer und Zink | `minecraft:copper_ingot×8, create:zinc_ingot×4` | Notwendige Metalle für den Einstieg in Create.
6 | `c_andesit` | Andesitlegierung | `create:andesite_alloy×16` | Basiskomponente für alle kinetischen Create-Maschinen.
7 | `c_rad` | Wasserrad | `create:water_wheel×1` | Generiert erste kinetische Rotationsenergie.
8 | `c_presse` | Mechanische Presse | `create:mechanical_press×1` | Automatisierte Herstellung von Platten und Komponenten.
9 | `c_sifter` | Der Create-Sifter | `createsifter:sifter×1, createsifter:string_mesh×1` | Erster Schritt zur Automatisierung des Siebens.
10 | `c_siebfabrik` | Die Siebfabrik | `minecraft:iron_ingot×64, create:zinc_ingot×32, minecraft:copper_ingot×64` | Vollautomatisierte Erzeugung von Grundressourcen.
11 | `c_alternator` | Strom aus Drehung | `createaddition:alternator×1` | Wandelt Rotationsenergie erstmals in FE-Strom um.
12 | `s_draht` | Kupferdraht | `createaddition:copper_spool×1` | Grundlage für Leitungen und moderne Stromnetze.
13 | `s_reaktor` | Netzstrom | `powah:reactor_basic×36` | Stabile Basis-Stromversorgung für technologische Maschinen.

---

### Kapitel 2: Mitte (Erze, Dimensionen, Mystische Felder & AE2)

Nr | Schlüssel | Titel | Aufgabe | warum dieser Schritt
---|---|---|---|---
1 | `j_obsidian` | Obsidian | `minecraft:obsidian×10` | Benötigt für den Bau des Netherportals.
2 | `j_nether` | Ab in den Nether | `dimension` (Nether) | Eröffnet Zugang zu Nether-Ressourcen und Blaze Rods.
3 | `k_osmium` | Osmium | `mekanism:ingot_osmium×8` | Grundstoff für den Einstieg in Mekanism.
4 | `k_infuser` | Metallurgic Infuser | `mekanism:metallurgic_infuser×1` | Basismaschine zur Herstellung von Legierungen.
5 | `k_alloy` | Infused Alloy | `mekanism:alloy_infused×8` | Legierung für fortgeschrittene Maschinen & MA Imperium.
6 | `c_messing` | Messing | `create:brass_ingot×16` | Voraussetzung für Präzisionstechnik und Tertium-Essenz.
7 | `c_tertium` | Tertium im Mixer | `mysticalagriculture:tertium_essence×4` | Schaltet Mystical Agriculture Stufe 3 frei (braucht Messing).
8 | `m_imperium` | Stufe 4: Imperium | `mysticalagriculture:imperium_essence×16` | Schaltet Mystical Agriculture Stufe 4 frei (braucht Infused Alloy).
9 | `k_inject` | ×4: Injektion | `mekanism:chemical_injection_chamber×1` | Vervierfacht die Erzerträge aus der Siebfabrik.
10 | `l_certus` | Certus-Quarz | `ae2:certus_quartz_crystal×16` | Einstiegsmaterial für Applied Energistics 2.
11 | `l_prozessoren` | Prozessoren | `ae2:logic_processor×4, ae2:calculation_processor×4, ae2:engineering_processor×4` | Logikbausteine für AE2-Netze und Supremium-Essenz.
12 | `l_auto` | Das Netz denkt mit | `ae2:pattern_provider×1, ae2:molecular_assembler×1, ae2:crafting_unit×1` | Ermöglicht vollautomatisches Handwerk im ME-Netzwerk.
13 | `m_supremium` | Stufe 5: Supremium | `mysticalagriculture:supremium_essence×8` | Schaltet Mystical Agriculture Stufe 5 frei (braucht AE2-Prozessoren).

---

### Kapitel 3: Endspiel (Das End, Insanium & Das Herz der Leere)

Nr | Schlüssel | Titel | Aufgabe | warum dieser Schritt
---|---|---|---|---
1 | `j_augen` | Enderaugen | `minecraft:ender_eye×12` | Notwendig zum Auffinden und Aktivieren des End-Portals.
2 | `j_end` | Das End | `dimension` (End) | Betreten der finalen Dimension für Endgame-Ressourcen.
3 | `j_drache` | Drachentöter | `kill` (Enderdrache) | Bezwingung des Hauptbosses zur Freischaltung von End-Inhalten.
4 | `z_elite` | Elite-Schaltkreis | `mekanism:elite_control_circuit×4` | Hochtechnologische Schaltung für Insanium und Kraftwerke.
5 | `m_niemehr` | Nie wieder sieben | `mysticalagriculture:osmium_seeds×1, mysticalagriculture:certus_quartz_seeds×1, mysticalagriculture:zinc_seeds×1` | Kompletter Ersatz des Siebens durch essenzbasierte Landwirtschaft.
6 | `m_insanium` | Stufe 6: Insanium | `mysticalagradditions:insanium_essence×4` | Höchste Essenzstufe (braucht Elite-Schaltkreise via `z_elite`).
7 | `z_strom` | Großkraftwerk | `powah:reactor_hardened×36` | Bereitstellung extremer Energiemengen für Antimaterie.
8 | `z_sps` | Antimaterie | `mekanism:pellet_antimatter×1` | Das fortschrittlichste Synthesematerial des Modpacks.
9 | `z_fabrik` | Die ewige Fabrik | `mekanism:ultimate_control_circuit×4, mysticalagriculture:supremium_essence×32, minecraft:nether_star×2` | Meilenstein der kompletten High-Tech-Automatisierung.
10 | `z_herr` | Erbe der Ewigkeit | `ars_nouveau:archmage_spell_book×1, mekanism:ultimate_control_circuit×4` *(Ersatz für Checkmark)* | Finaler Nachweis der vollendeten Meisterschaft über Technik und Magie.

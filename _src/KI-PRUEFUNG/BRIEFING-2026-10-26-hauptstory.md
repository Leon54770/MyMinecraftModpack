# Brainstorming: Hauptstory von Sky and Stone spannender machen

Du bist ein preisgekrönter Modpack-Designer (SkyFactory 4, Stoneblock, GregTech New Horizons, Enigmatica Expert, ATM Sky).
Antworte auf Deutsch. Sei mutig und konkret, aber erfinde keine Mod-Mechaniken. Bei Unsicherheit „unsicher“ dazuschreiben.

## Problem (vom Spieler)
„Mir fehlt noch zu viel, es kann schnell langweilig werden, weil in der Hauptstory nur einfache Standardmods nacheinander benutzt werden. Ich will eine geile Quest, in der die ganzen Mods und Funktionen gut integriert sind.“

## Rahmen
- Minecraft 1.21.1 NeoForge, Skyblock (leere Inseln; Nether leer mit Festungen; End-Hauptinsel). Story: Die Welt ist in Inseln zerbrochen, unter allem schläft „das Herz der Leere“, der letzte Wächter hinterließ ein Tagebuch.
- Werkzeuge: FTB Quests (Aufgaben: Item, Kill, Dimension, Strom, Advancement, Beobachten, Ort), KubeJS 7 (eigene Items/Blöcke, eigene Rezepte für JEDE Mod-Maschine per JSON, Events: Rechtsklick, Tod von Mobs, Tick, Befehle), Datapacks (Advancements, Loot, Strukturen per /place template).
- Keine neuen Mods. Kein Grind als Pflicht. Technik und Magie gleichwertig. Keine Belohnung darf Stufen überspringen.
- Installierte Mods: ae2 almostunified ambientsounds appleskin applied-energistics-2-wireless-terminals applied-mekanistics arc architectury-api ars-nouveau balm better-combat bookshelf-lib botany-pots building-gadgets carry-on cloth-config clumps collective controlling create-mechanical-extruder create-sifting create createaddition creativecore cucumber curios double-doors dynamic-fps emotecraft enchantment-descriptions entityculling ex-deorum farmers-delight fastfurnace fastworkbench ferrite-core forgiving-void fragmentum framedblocks ftb-filter-system ftb-library-forge ftb-quests-forge ftb-teams-forge ftb-ultimine-forge ftb-xmod-compat functional-storage fusion-connected-textures geckolib gravestone-mod guideme handcrafted hostile-neural-networks immediatelyfast industrial-foregoing inventory-essentials iris iron-furnaces iron-jetpacks item-restrictions jade-addons-forge jade jamlib jei jobsplus kubejs leaves-be-gone libx lithium loot-journal lootr macaws-bridges macaws-doors macaws-fences-and-walls macaws-furniture macaws-lights-and-lamps macaws-paths-and-pavings macaws-roofs macaws-stairs macaws-trapdoors macaws-windows mechanicals-lib mega mekanism-generators mekanism mezzconfig modernfix moonlight moreculling mouse-tweaks mystical-agradditions mystical-agriculture not-enough-animations packet-fixer pehkui pipez placebo playeranimator polymorph powah prickle productivebees puzzles-lib rechiseled resourceful-lib rhino rightclickharvest searchables shulkerboxtooltip simple-backups skyblock-builder sodium-extra sodium sophisticated-backpacks sophisticated-core sophisticated-storage spark supermartijn642s-config-lib supermartijn642s-core-lib supplementaries time-in-a-bottle-universal titanium torchmaster trash-cans ui-lib waystones xaeros-minimap xaeros-world-map yaml-config

## Heutige Hauptstory (jede Quest = „besitze Item“)

akt1:
- Willkommen in der Leere: ftbquests:book x1
- Der erste Baum: minecraft:logs x5
- Seidenraupe und Faden: exdeorum:silkworm x1, minecraft:string x8
- Kompostfass: exdeorum:wooden_barrels x1
- Stein aus dem Nichts: minecraft:cobblestone x32
- Das erste Sieb: skyandstone:sieves x1, exdeorum:string_mesh x1
- Hammerzeit: exdeorum:stone_hammer x1
- Wasser aus Blättern: skyandstone:water_crucibles x1
- Feuer aus Stein: exdeorum:porcelain_crucible x1
- Erz im Kies: exdeorum:iron_ore_chunk x8
- Ein besseres Netz: exdeorum:flint_mesh x1
- Der Funke: minecraft:iron_ingot x2
- Samen der Essenz: mysticalagriculture:inferium_seeds x1
- Stufe 2: Prudentium: mysticalagriculture:prudentium_essence x16
- Der Infusionsaltar: mysticalagriculture:infusion_altar x1, mysticalagriculture:infusion_pedestal x8
- Kupfer und Zink: minecraft:copper_ingot x4, create:zinc_ingot x1
- Andesitlegierung: create:andesite_alloy x16
- Die erste Kraft: create:water_wheel x1
- Mühlstein statt Hammer: create:millstone x1
- Sieben ohne Hände: createsifter:sifter x1, createsifter:string_mesh x1, createsifter:andesite_mesh x1
- Der Extruder: create_mechanical_extruder:mechanical_extruder x1
- Die Presse: create:mechanical_press x1
- Waschen mit Wind: create:encased_fan x1
- Mixer und Becken: create:mechanical_mixer x1, create:basin x1
- Feuer ohne Nether: create:empty_blaze_burner x1, create:blaze_burner x1
- Messing: create:brass_ingot x16
- Die erste Maschine: minecraft:iron_ingot x32, create:zinc_ingot x16, minecraft:copper_ingot x32

akt2:
- Präzisionsarbeit: create:precision_mechanism x1
- Funken aus Drehung: createaddition:alternator x1, createaddition:copper_spool x1
- Osmium: mekanism:ingot_osmium x8
- Die Infusionsanlage: mekanism:metallurgic_infuser x1
- Infundierte Legierung: mekanism:alloy_infused x8
- Grundschaltkreis: mekanism:basic_control_circuit x4
- ×2: Anreicherung: mekanism:enrichment_chamber x1
- ×3: Reinigung: mekanism:purification_chamber x1
- Stufe 3: Tertium: mysticalagriculture:tertium_essence x16
- Eisen vom Feld: mysticalagriculture:iron_seeds x1
- Obsidian: minecraft:obsidian x10
- Die zerbrochene Unterwelt: minecraft:the_nether x1
- Die Festung: minecraft:nether_bricks x16
- Lohenruten: minecraft:blaze_rod x8
- Über der Leere: ironjetpacks:jetpack x1
- Certus-Quarz: c:gems/certus_quartz x16
- Lader und Fluix: ae2:charger x1, ae2:fluix_crystal x8
- Prägeplatten ohne Meteor: ae2:inscriber x1, ae2:logic_processor_press x1, ae2:calculation_processor_press x1, ae2:engineering_processor_press x1, ae2:silicon_press x1
- Prozessoren: ae2:logic_processor x4, ae2:calculation_processor x4, ae2:engineering_processor x4
- Das ME-Netz: ae2:controller x1, ae2:drive x1, ae2:item_storage_cell_4k x1, ae2:terminal x1
- Vierfach-Erz: mekanism:chemical_injection_chamber x1

akt3:
- Das Netz denkt mit: ae2:pattern_provider x1, ae2:molecular_assembler x1, ae2:crafting_unit x1
- Stufe 4: Imperium: mysticalagriculture:imperium_essence x16
- Stufe 5: Supremium: mysticalagriculture:supremium_essence x8
- Felder aus Erz: mysticalagriculture:osmium_seeds x1, mysticalagriculture:certus_quartz_seeds x1, mysticalagriculture:zinc_seeds x1
- Hexenwasser-Trick: minecraft:wither_skeleton_skull x3
- Der Wither: minecraft:nether_star x1
- Enderperlen: minecraft:ender_pearl x12
- Enderaugen: minecraft:ender_eye x12
- Portalrahmen: minecraft:end_portal_frame x12
- Das End: minecraft:the_end x1
- Der Wächter am Ende: minecraft:ender_dragon x1
- Elite-Schaltkreis: mekanism:elite_control_circuit x4
- Ultimate-Schaltkreis: mekanism:ultimate_control_circuit x2
- Stufe 6: Insanium: mysticalagradditions:insanium_essence x4
- Spaltreaktor: mekanismgenerators:fission_reactor_casing x4, mekanismgenerators:fission_fuel_assembly x1
- Polonium: mekanism:pellet_polonium x1
- Der Herzschlag: mekanism:pellet_antimatter x1
- Die ewige Fabrik: mekanism:ultimate_control_circuit x4, mysticalagriculture:supremium_essence x32, minecraft:nether_star x2
- Maschine oder Magie: skyandstone:weg_zum_herz x1
- Erz ohne Sieb: skyandstone:erz_ohne_sieb x1
- Das Erbe der Erbauer: minecraft:dragon_egg x1
- Weg der Magie: ars_nouveau:archmage_spell_book x1
- Weg der Maschine: hostilenetworks:loot_fabricator x1
- Weg der Felder: mysticalagriculture:osmium_seeds x1
- Weg des Lasers: industrialforegoing:ore_laser_base x1
- Weg der Bienen: productivebees:configurable_honeycomb x1

## Gesucht
1. Ein starkes Leitmotiv für die ganze Hauptstory, das alle Mods verbindet (kein Mod-für-Mod-Abhaken). 3 Varianten, je 4–6 Sätze, dann deine Empfehlung.
2. Für die Empfehlung: 8–10 konkrete Meilensteine von Start bis Finale. Je Meilenstein: was der Spieler TUT (nicht nur besitzt), welche 2–3 Mods zusammenspielen müssen, welche Maschine das eigene Story-Item herstellt.
3. 5 Ideen für Momente, an die man sich erinnert (Ereignis, Bosskampf, Entdeckung, Bau-Aufgabe), umsetzbar mit KubeJS/Datapack.
4. 3 Fehler, die solche Packs langweilig machen, und wie wir sie vermeiden.

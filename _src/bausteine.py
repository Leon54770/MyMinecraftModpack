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
      desc=['Weiter geht es im Kapitel „Akt I: Ein Splitter im Nichts“.']),
])

# =====================================================================
# 2 Erde, Kies und Hoffnung (Ex Deorum)
# =====================================================================
erde = Chapter('erde', 'Erde, Kies und Hoffnung', 'insel', 'exdeorum:oak_sieve', sub='Aus Nichts wird Erz.', quests=[
    Q('e_holz', 'Der Baum ist dein Freund', 0, 0, item('minecraft:oak_log', 5), deps=['w_los'], rewards=[xp(10)],
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
    Q('e_cobble', 'Bruchstein-Generator', -18, 3.5, item('minecraft:cobblestone', 32), deps=['e_eisen'], rewards=[xp(15)],
      desc=['Ein Eimer aus Eisen holt dir Wasser und Lava. Platzier beide so, dass sie neben einem freien Block zusammenfließen.',
            'Tipp: Eine 2×2-Wasserquelle macht den Bruchstein unendlich.']),
    Q('e_hammer', 'Hammerzeit', -9, 1.5, item('exdeorum:stone_hammer'), deps=['e_sieb'], rewards=[xp(15)],
      desc=['Hämmer zerschlagen Blöcke: Bruchstein → Kies → Sand → Staub.',
            'Später übernimmt das der Create-Mühlstein.']),
    # Treffpunkt: Sieb
    Q('e_sieb', 'Das Sieb', -12, 0, [item('exdeorum:oak_sieve'), item('exdeorum:string_mesh')], deps=['e_faden'],
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
    Q('e_brocken', 'Erzbrocken', -15, 2, item('exdeorum:iron_ore_chunk', 8), deps=['e_sieb'], rewards=[xp(20)],
      desc=['Kies mit dem Feuersteinnetz (oder besser) gibt Erzbrocken.', '4 Brocken = 1 Erz zum Schmelzen. Für 2 Eisenbarren brauchst du 8 Brocken.']),
    Q('e_feuernetz', 'Feuersteinnetz', -18, 2, item('exdeorum:flint_mesh'), deps=['e_brocken'], rewards=[xp(15)],
      desc=['Bessere Netze, bessere Funde.', 'Netze lassen sich mit Effizienz und Glück verzaubern!']),
    Q('e_eisen', 'Erster Eisenbarren', -21, 2, item('minecraft:iron_ingot', 2), deps=['e_feuernetz'], shape=G, size=2.0,
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
    Q('c_rad', 'Wasserrad', 3, 0, item('create:water_wheel'), deps=['c_andesit'], rewards=[give('create:andesite_casing', 2), xp(20)],
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
    Q('a_erzmagier', 'Erzmagier', 18, 0, item('ars_nouveau:archmage_spell_book'), deps=['a_apparat', 'a_wilden', 'a_drygmy', 't_chimera'], shape=G, size=2.0,
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
    Q('p_ohnerohr', 'Fabrik ohne Rohre', 9, -3, check(), deps=['p_start', 'l_controller'], optional=True, icon='functionalstorage:storage_controller',
      rewards=[crate('gold'), xp(80)],
      desc=['Eine Produktionskette, die nur mit Förderbändern, Trichtern und Schubladen auskommt – kein einziges Pipez- oder Mekanism-Rohr.']),
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


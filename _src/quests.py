"""Sky and Stone – Questbuch-Aufbau (0.6). Aufruf aus dem Pack-Ordner:  python -I _src/quests.py

Aufbau wie SkyFactory 4 / StoneBlock:
  * Hauptstory (3 Akte) mit den wichtigsten Schritten für Früh-, Mittel- und Endspiel
  * Ein Kapitel pro Mod bzw. Modbereich mit den Details (oben links Verweise auf die Hauptstory)
  * Extras: Story „Das Herz der Leere“ (läuft von allein mit), Inselmarkt, Sammlerbuch, Baumeister
Alle Aufgaben werden automatisch erkannt (keine Haken-Quests). Belohnungen holt man selbst im Questbuch ab (0.6.4).
Texte und Aufgaben der einzelnen Quests stehen in _src/bausteine.py, hier nur Struktur und Änderungen.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from questlib import *
import bausteine as B

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G, M = 'gear', 'hexagon'

ALLE = {q.key: q for c in [B.willkommen, B.erde, B.gruen, B.create, B.strom, B.mek, B.lager, B.ma, B.ars, B.bienen,
                           B.jenseits, B.geist, B.bau, B.markt, B.pruefungen, B.ende] for q in c.quests}

# ---------------------------------------------------------------------
# 1. Streichen oder zusammenlegen (alter Schlüssel -> Ersatz für Abhängigkeiten)
# ---------------------------------------------------------------------
ERSATZ = {
    # Willkommen: 7 Haken-Quests -> eine automatische Start-Quest mit allen Tipps
    'w_wachsen': 'w_start', 'w_ernte': 'w_start', 'w_jei': 'w_start', 'w_ultimine': 'w_start',
    'w_karte': 'w_start', 'w_team': 'w_start', 'w_los': 'w_start',
    # Zwischenschritte in ihr Ziel gelegt
    'e_porzellan': 'e_lavatiegel', 's_draht': 'c_alternator', 's_paste': 's_orb', 'l_fluix': 'l_lader',
    'a_kammer': 'a_quelle', 'k_kabel': 'k_cube', 'g_brett': 'g_topf',
    # Reine Beschäftigung / nicht automatisch prüfbar
    'l_muell': 'l_fass', 'j_brenner': 'j_lohe', 'h_boss': 'h_fab', 'x_markt': 'e_eisen', 'z_versiegeln': 'z_fabrik',
    'p_start': 'e_eisen', 'p_kompakt': 'c_siebfabrik', 'p_ohnebrenn': 's_reaktor', 'p_ohnerohr': 'l_controller',
    'p_vierfach': 'k_inject', 'p_nether': 'j_nether', 'p_ohnesieb': 'm_eisen', 'p_wither': 'j_wither',
    # Nicht lösbar: wilde Starbuncles spawnen nur in Taiga und Archwood-Wald, die Startinseln haben beides nicht (REZEPT-SIM.md, Befund 1)
    'a_starbuncle': 'l_controller',
    # Gemini-Umbau (GEMINI-UMBAU.md): doppelte/kleine Schritte zusammengelegt
    'e_faden': 'e_raupe', 'c_netze': 'c_sifter', 'c_tertium': 'c_messing', 'l_pickup': 'l_rucksack',
    # Baumeister-Haken -> neue Quests mit echten Aufgaben (unten)
    'u_haus': 'u_dach', 'u_moebel': 'u_moebel2', 'u_bruecke': 'u_bruecke2', 'u_garten': 'u_bruecke2', 'u_meister': 'u_kopie',
}
ORIG = dict(ALLE)   # Originale, auch der gestrichenen Quests (für ihre Abhängigkeiten)
for k in ERSATZ: ALLE.pop(k, None)

def _aufloesen(d, eigener, seen=()):
    """Abhängigkeit d auflösen. Wurde d in die eigene Quest gelegt (z. B. e_porzellan -> e_lavatiegel),
    erbt die Quest die Voraussetzungen von d – sonst stünde sie ohne Voraussetzung im Buch (Fehler in 0.6.0)."""
    if d not in ERSATZ: return [d]
    ziel = d
    while ziel in ERSATZ: ziel = ERSATZ[ziel]
    if ziel != eigener: return [ziel]
    if d in seen or d not in ORIG: return []
    out = []
    for dd in ORIG[d].deps: out += _aufloesen(dd, eigener, seen + (d,))
    return out

def ersetze_deps(q):
    neu = []
    for d0 in q.deps:
        for d in _aufloesen(d0, q.key):
            if d != q.key and d not in neu: neu.append(d)
    q.deps = neu

# ---------------------------------------------------------------------
# 2. Geänderte Quests
# ---------------------------------------------------------------------
A = ALLE
A['w_start'].tasks = [item('ftbquests:book')]
A['w_start'].desc = [
    'Unter dir: nichts. Um dich: nichts. Nur deine Insel.',
    '',
    '',
    'Dieses Buch führt dich durch alles. Die &lHauptstory&r zeigt dir die wichtigsten Schritte, die &lMod-Kapitel&r erklären jede Mod im Detail.',
    'Quests erledigen sich von selbst, sobald du die Items hast, und Belohnungen landen direkt bei dir.',
    '',
    '&lNützlich von Anfang an:&r',
    '- Ducken neben Setzlingen und Feldern lässt sie etwas schneller wachsen. Die Gießkanne kann das besser.',
    '- Reife Pflanzen per Rechtsklick ernten, sie werden neu gesetzt.',
    '- R zeigt das Rezept eines Items, U wofür es gebraucht wird (auch alle Siebfunde mit Chancen).',
    '- Taste ` (Gravis) halten und abbauen: ganze Bäume, Adern und Kiesflächen auf einmal.',
    '- M öffnet die Karte. Freunde holst du mit /skyblock invite <Name>.',
    '- Wer in die Leere fällt, landet oben wieder auf der Insel (kostet 3 Herzen).',
    '',
    '&cKeine Insel, sondern eine normale Welt?&r Dann wurde beim Erstellen der Welttyp nicht umgestellt. Neue Welt anlegen und unter „Welt“ → „Welttyp“ &lSkyblock&r wählen.']
A['w_start'].rewards = [crate('holz'), xp(10)]

A['c_alternator'].tasks = [item('createaddition:alternator'), item('createaddition:copper_spool')]
A['c_alternator'].desc = ['Der Alternator (Create Crafts & Additions) macht aus Drehkraft Strom (FE).',
                          'Mit Kupferdraht-Rollen verbindest du ihn mit Akkus und Maschinen. Ab hier gibt es Strom.']
A['s_orb'].tasks = [item('powah:energizing_orb'), item('powah:energizing_rod_starter', 2), item('powah:dielectric_paste', 8)]
A['s_orb'].desc = ['Dielektrische Paste (Ton, Kohle, Lava) ist die Grundzutat von Powah.',
                   'Der Orb lädt Items mit Strom auf, die Stäbe drumherum liefern die Energie.']
A['l_lader'].title = 'Lader und Fluix'
A['l_lader'].tasks = [item('ae2:charger'), item('ae2:fluix_crystal', 8)]
A['l_lader'].desc = ['Der Lader lädt Certus mit Strom auf.', 'Geladener Certus + Redstone + Quarz ins Wasser geworfen ergibt Fluix.']
A['l_inscriber'].deps = ['l_lader', 'k_stahl']
A['a_quelle'].tasks = [item('ars_nouveau:imbuement_chamber'), item('ars_nouveau:source_gem', 8)]
A['a_quelle'].desc = ['Amethyst (aus dem Sieb) in der Imbuement Chamber wird zu Quellstein.', 'Quellstein ist der Grundstoff aller Magie in Ars Nouveau.']
A['k_cube'].title = 'Strom verteilen'
A['k_cube'].tasks = [item('mekanism:basic_universal_cable', 8), item('mekanism:basic_energy_cube')]
A['k_cube'].desc = ['Universalkabel tragen Strom, der Energiewürfel speichert ihn.']
A['g_topf'].title = 'Die Küche'
A['g_topf'].tasks = [item('farmersdelight:cutting_board'), item('farmersdelight:cooking_pot')]
A['g_topf'].desc = ['Farmer\'s Delight: Das Schneidebrett holt mehr aus deinen Zutaten, der Kochtopf macht Gerichte, die lange satt machen.']
A['g_autark'].tasks = [item('botanypots:terracotta_hopper_botany_pot', 4)]
A['g_autark'].desc = ['Vier Trichter-Töpfe: Holz und Essen wachsen von selbst und landen in Truhen.',
                      'Ab jetzt versorgt sich deine Insel selbst.']
A['z_herr'].tasks = [item('minecraft:dragon_egg')]
A['z_herr'].desc = [d for d in A['z_herr'].desc if not d.startswith('&o')] + ['',
                    'Aufgabe: Bring das Drachenei nach Hause. Tipp: Das Ei teleportiert sich beim Schlagen – ein Kolben schiebt es herunter.']
A['e_raupe'].tasks = [item('exdeorum:silkworm'), item('minecraft:string', 8)]
A['e_raupe'].title = 'Seidenraupe und Faden'
A['e_raupe'].desc = ['Setz eine Seidenraupe auf Laub: Es wird langsam zu Spinnweben, die beim Abbauen zu Faden zerfallen.',
                     'Faden brauchst du für das erste Siebnetz.']
A['c_sifter'].tasks = [item('createsifter:sifter'), item('createsifter:string_mesh'), item('createsifter:andesite_mesh')]
A['l_rucksack'].tasks = [item('sophisticatedbackpacks:backpack'), item('sophisticatedbackpacks:pickup_upgrade')]
A['l_rucksack'].desc = ['Mehr Platz zum Mitnehmen. Das Aufsammel-Upgrade füllt den Rucksack automatisch mit Siebfunden.']
A['m_tertium'].desc = ['4 Prudentium + 1 Messingbarren im Create-Mixer ergeben 2 Tertium-Essenz.', 'Nur so kommst du an Stufe-3-Samen.']
A['h_fab'].shape, A['h_fab'].size = G, 2.0
A['h_fab'].desc = A['h_fab'].desc + ['Meilenstein: Ab jetzt kommen Mob-Drops aus der Maschine.']
for k in ('p_essenzen', 'p_netze', 'p_archwood', 'p_trophaeen'):
    A[k].optional = False   # das ganze Sammlerbuch-Kapitel ist optional
# Ex-Deorum-Startitems kommen jetzt aus dem Startinventar, der Haken also auch
A['e_haken'].desc = ['Den Crook stellst du aus vier Holzstäben her. Er lässt Laub öfter Setzlinge fallen und findet Seidenraupen.']

# Baumeister: echte Aufgaben statt Haken (jede Quest stellt eine Bau-Mod vor)
NEU = [
    Q('u_dach', 'Ein Dach über dem Kopf', 0, 0, item('mcwroofs:oak_roof', 16), deps=['u_meissel'], rewards=[crate('holz'), xp(20)],
      desc=['Macaw\'s Roofs, Doors und Windows: Dächer, Türen und Fenster in allen Holzarten.']),
    Q('u_moebel2', 'Einrichten', 0, 0, [item('handcrafted:oak_chair', 2), item('handcrafted:oak_table')], deps=['u_dach'], rewards=[xp(20)],
      desc=['Handcrafted und Macaw\'s Furniture: Stühle, Tische, Regale, Betten.']),
    Q('u_bruecke2', 'Brücke ins Nichts', 0, 0, item('mcwbridges:rope_oak_bridge', 8), deps=['u_meissel'], rewards=[xp(20)],
      desc=['Macaw\'s Bridges: Hängebrücken zu deinen Nebeninseln. Wege und Laternen gibt es in Macaw\'s Paths und Lights.']),
    Q('u_kopie', 'Inselarchitekt', 0, 0, item('buildinggadgets2:gadget_copy_paste'), deps=['u_gadget', 'u_framed', 'u_moebel2'], shape=G, size=1.8,
      rewards=[crate('gold'), xp(60)], desc=['Das Kopier-Gadget speichert ganze Gebäude und baut sie woanders wieder auf.']),
    Q('z_ultkreis', 'Ultimate-Schaltkreis', 0, 0, item('mekanism:ultimate_control_circuit', 2), deps=['z_elite'], rewards=[crate('gold'), xp(60)],
      desc=['Elite-Schaltkreise + Atomlegierung. Brauchst du für Insanium-Essenz und die ewige Fabrik.']),
]
NEU += [
    # 0.6.1 (ANWEISUNG-0.6.1.md A2): Antimaterie braucht Polonium, Polonium braucht einen Spaltreaktor
    Q('k_spalt', 'Spaltreaktor', 0, 0, [item('mekanismgenerators:fission_reactor_casing', 4), item('mekanismgenerators:fission_fuel_assembly')],
      deps=['z_elite'], rewards=[crate('gold'), xp(80)],
      desc=['Mekanism Generators: Ein Spaltreaktor macht aus Uran viel Strom – und Atommüll, den du gleich brauchst.',
            'Uran: Uranbrocken aus zerkleinertem Tiefenschiefer im Sieb oder Uran-Samen. Weg: Uran → Yellowcake → Uranoxid → Uranhexafluorid → Spaltbrennstoff.',
            'Vorsicht: Kühlung (Wasser) nicht vergessen und den Reaktor nie überhitzen lassen.']),
    Q('k_polonium', 'Polonium', 0, 0, item('mekanism:pellet_polonium'), deps=['k_spalt'], rewards=[crate('gold'), xp(80)],
      desc=['Atommüll aus dem Spaltreaktor wird im Solar Neutron Activator (braucht Tageslicht) zu Polonium.',
            'Polonium-Pellets sind die Zutat für Antimaterie im SPS.']),
    # A4: Finale „Maschine oder Magie“ – eins von beiden reicht
    # 0.6.2: echte Aufgabe statt keiner (Quests ohne Aufgabe gelten in FTB Quests sofort als erledigt)
    Q('z_weg', 'Maschine oder Magie', 0, 0,
      [tag('skyandstone:weg_zum_herz', icon='ars_nouveau:archmage_spell_book', title='Erzmagier-Zauberbuch oder Loot Fabricator')],
      deps=['a_erzmagier', 'h_fab'], dep_any=True, icon='ars_nouveau:archmage_spell_book',
      rewards=[xp(100)],
      desc=['Die Erbauer brauchten beides. Dir reicht einer der Wege:',
            '- &lMagie:&r das Erzmagier-Zauberbuch (Ars Nouveau)',
            '- &lMaschinen:&r der Beute-Fabrikator (Hostile Networks)',
            'Diese Quest erledigt sich von selbst, sobald du einen davon hast.']),
]
for q in NEU: A[q.key] = q
for q in A.values(): ersetze_deps(q)
A['m_insanium'].deps = [d for d in A['m_insanium'].deps if d != 'z_elite'] + ['z_ultkreis']
# 0.7.0 (Review): Insanium braucht keine Osmium-Samen. Sonst wäre m_niemehr über z_fabrik doch Pflicht und die Erz-Wahl wirkungslos.
A['m_insanium'].deps = [d for d in A['m_insanium'].deps if d != 'm_niemehr'] + (['m_supremium'] if 'm_supremium' not in A['m_insanium'].deps else [])

# ---------------------------------------------------------------------
# 0.6.1 Logik-Prüfung: Mystical-Agriculture-Samen nach ihrer echten Stufe (aus dem Mod-Code gelesen)
#   Stufe 2: Kohle, Silizium · Stufe 3: Eisen, Kupfer, Redstone, Certus · Stufe 4: Gold, Fluix, Osmium · Stufe 5: Diamant
#   Vorher hing m_tertium an m_eisen, obwohl Eisen-Samen selbst Tertium brauchen (Kreis).
# ---------------------------------------------------------------------
A['m_tertium'].deps = ['m_prudentium', 'c_messing']
A['m_eisen'].deps = ['m_tertium']
A['m_eisen'].desc = ['Eisen-Samen sind Stufe 3: Sie brauchen Tertium-Essenz (Create-Mixer).',
                     'Der Moment, in dem das Sieben endet: Eisen wächst.']
A['m_kupfer'].deps = ['m_tertium']
A['m_kupfer'].desc = ['Kohle ist Stufe 2, Kupfer Stufe 3 (Tertium).']
A['m_gold'].deps = ['m_imperium']
A['m_gold'].title = 'Gold und Redstone'
A['m_gold'].desc = ['Redstone ist Stufe 3, Gold Stufe 4: Dafür brauchst du Imperium-Essenz (Mekanism).']
A['m_diamant'].deps = ['m_supremium']
A['m_diamant'].desc = ['Diamant-Samen sind Stufe 5 und brauchen Supremium-Essenz (AE2).']
# AE2-Prägeplatten: in der Leere keine Meteoriten -> Mystical Agriculture (Certus-Essenz, Stufe 3)
A['l_inscriber'].deps = ['l_lader', 'k_stahl', 'm_tertium']
A['l_inscriber'].desc = ['In der Leere gibt es keine Meteoriten. Die vier Prägeplatten stellst du aus Certus-Quarz-Essenz her:',
                         'Zum Beispiel 8 Essenz um einen Goldbarren = Logik-Platte, 8 Essenz um Silizium = Silizium-Platte. Die anderen beiden zeigt JEI (U auf die Essenz).',
                         'Certus-Samen sind Stufe 3 (Tertium). Freischaltung danach: Supremium-Essenz und Pipez-Ultimate.']
# Wixie-Kessel entsteht erst in der Welt (Wixie auf einen Kessel setzen) und hat kein Rezept
A['a_wixie'].tasks = [item('ars_nouveau:wixie_charm'), item('minecraft:cauldron')]
A['a_wixie'].desc = ['Setz die Wixie mit ihrem Amulett auf einen Kessel: Daraus wird ein Wixie-Kessel.',
                     'Lege Zutaten in Truhen daneben und zeige ihr das Rezept: Sie stellt es immer wieder her.',
                     'Für einfache Dinge (Fackeln, Bleche, Legierungen) ein früher Ersatz für AE2-Autocrafting. Für große Mengen bleibt AE2 stärker.']
# Totem gibt es nur selten aus Sternkisten (keine Plünderer in der Leere) -> kein Glücksspiel im Sammlerbuch
A['p_trophaeen'].tasks = [t for t in A['p_trophaeen'].tasks if t[1] != 'minecraft:totem_of_undying']
A['p_trophaeen'].desc = ['Netherstern, Drachenei und Wither-Schädel. Stell sie irgendwo schön aus.']

# Voraussetzung muss garantieren, dass das verlangte Item erreichbar ist
A['x_polonium'].deps = ['k_polonium']                      # Polonium erst nach der Polonium-Quest
if 'j_wither' not in A['p_trophaeen'].deps: A['p_trophaeen'].deps.append('j_wither')   # Netherstern braucht den Wither

# ---------------------------------------------------------------------
# Nachtschicht 0.6.3 (NIGHT_REPORT.md): Befunde der Design-Prüfung
# ---------------------------------------------------------------------
# Erzmagier: Rezept ohne Totem (balance.js). Netherstern braucht den Wither, Tribut die Chimera.
A['a_erzmagier'].deps = A['a_erzmagier'].deps + ['j_wither']
A['a_erzmagier'].desc = ['Das stärkste Zauberbuch. Magie ist ab jetzt kein Spielzeug mehr.', '',
    '&lZutaten (Buch-Upgrade am Schreibtisch):&r Lehrlings-Zauberbuch, 3 Enderperlen, 2 Smaragde, 1 Diamantblock, 1 Netherstern (Wither) und 1 Wilden-Tribut.',
    'Den Tribut lässt die &lWilden-Chimera&r fallen: Ritual „Wilden beschwören“ im Ritualbecken, verstärkt mit Wilden-Horn, -Stachel und -Flügel.',
    '&cAchtung:&r Das Chimera-Ritual zerstört Blöcke rund um das Becken. Bau es auf einer eigenen Plattform weit weg von deiner Basis.']
# Ressourcen-Bienen sind ein Frühspiel-Seitenweg: Goldkiste (Messing, Osmium) wäre zu früh
A['b_zucht'].rewards = [crate('eisen'), xp(60)]
# Wiederholbare Gold-/Sterntausche erst ab Messing, sonst gibt es Messing (-> Tertium) und Osmium aus dem Markt
for k, q in A.items():
    if k.startswith('x_') and q.repeat and any(r[0] == 'table' and r[1] in ('gold', 'stern') for r in q.rewards):
        if 'c_messing' not in q.deps: q.deps.append('c_messing')
# Befunde Quest-Fluss (Frühspiel)
# Der leere Lohenbrenner braucht Netherrack, der Nether ist leer -> Weg über Hexenwasser erklären
A['c_brenner'].tasks = [item('create:empty_blaze_burner'), item('create:blaze_burner')]
A['c_brenner'].desc = ['1. &lLeerer Lohenbrenner:&r 4 Eisenbleche (Presse) um 1 Netherrack.',
    '2. Leerer Brenner + 4 Lohenpulver (Staub sieben) = Lohenbrenner. Mit Kohle oder Holz gefüttert heizt er dein Becken für Messing.',
    '',
    '&lNetherrack ohne Nether:&r Myzelsporen (Erde sieben) auf Erde ergeben Myzel. Ein Wasserfass auf Myzel wird nach gut einer Minute zu Hexenwasser.',
    'Hexenwasser im Fass + Lava ergibt Netherrack (genauer Aufbau in JEI: U auf Netherrack). Auf der Pilzinsel hast du Myzel schon.']
# Zink von Hand: 3,5-4 % pro Kies. 4 Barren wären ~400 Kies, gebraucht wird Zink erst für Messing (dann siebt Create)
A['e_kupfer'].tasks = [item('minecraft:copper_ingot', 4), item('create:zinc_ingot', 1)]
A['e_kupfer'].desc = ['Kupfer- und Zinkbrocken kommen auch aus dem Kies (Zink ist selten, etwa 4 %).',
    'Ein Zinkbarren reicht für den Anfang. Den Rest siebt später der Create-Sifter mit dem Eisennetz.']
# Seidenraupe: Der Haken findet sie nur mit ~1 % pro Laubblock -> eine gibt es zum Start, damit das erste Netz planbar ist
A['w_start'].rewards = [crate('holz'), give('exdeorum:silkworm'), xp(10)]
A['e_raupe'].rewards = [give('minecraft:string', 4), xp(15)]
A['e_raupe'].desc = ['Setz die Seidenraupe (Belohnung der Start-Quest) auf Laub: Es wird langsam zu Spinnweben, die beim Abbauen zu Faden zerfallen.',
    'Mit dem Haken findest du im Laub weitere Seidenraupen. Faden brauchst du für das erste Siebnetz.']
A['e_brocken'].desc = ['Schon das Fadennetz gibt aus Kies Eisen- (10 %) und Kupferbrocken (8 %).',
    'Das Feuersteinnetz bringt etwas mehr und dazu Andesit-Kiesel für Create.', '4 Brocken = 1 Erz zum Schmelzen.']
# Endgame-Tausche lohnen sich sonst nicht (Sternkiste ist weniger wert als 32 Supremium oder Antimaterie)
A['x_supremium'].tasks = [item('mysticalagriculture:supremium_essence', 8, consume=True)]
A.pop('x_antimaterie')

# ---------------------------------------------------------------------
# 0.7.0 (NIGHT_REPORT_0.7.0.md): Befunde der fünf Audits
# ---------------------------------------------------------------------
# Mystical Agriculture ohne Gold-Grind starten: Inferium-Samen sind ein Werkbank-Rezept (8 Essenz + Weizensamen),
# der Infusionsaltar (18 Goldbarren) wird erst für Stufe-3-Samen gebraucht. Inferium fällt beim Sieben von Erde.
A['g_inferium'].deps = ['e_sieb']
A['m_inferium'].deps = ['g_inferium']
A['m_altar'].deps = ['m_prudentium']
for k in ('m_eisen', 'm_kupfer', 'l_inscriber'):
    if 'm_altar' not in A[k].deps: A[k].deps.append('m_altar')
# Erst den Sifter, dann die Presse: Die Presse kostet einen Eisenblock, der Sifter kein Eisen
A['c_presse'].deps = ['c_sifter']
# Weizen kommt nur vom Feld; c:crops enthielt auch gesiebte Karotten/Kartoffeln, Kaktus, Netherwarze
GRUPPEN_FEST = {'g_feld'}
# Wixie: Goldkiste (8 Messing) vor Messing würde Tertium früher öffnen (wie b_zucht/a_starbuncle in 0.6.3)
A['a_wixie'].rewards = [crate('eisen'), xp(50)]
# Ressourcen-Bienen: echte Aufgabe statt 8 Honey Treat. Erz-Bienen = Kristallbiene (Netherquarz-Nest im Nether)
# x Ashy Mining Bee (Kiesnest in Fluss-/Strandbiom). Der Nether muss also offen sein.
A['b_zucht'].deps = A['b_zucht'].deps + ['j_nether']
# 0.8.0: Prüft jetzt die gezüchtete Eisenbiene über ihre Wabe (Komponente bee_type), nicht nur gebaute Nester
A['b_zucht'].tasks = [item('productivebees:configurable_honeycomb', 1, komponenten={'productivebees:bee_type': 'productivebees:iron'})]
A['b_zucht'].icon = 'productivebees:configurable_honeycomb'
# Zweite echte Wahl: Erz ohne Sieb – Felder (MA), Laserbohrer (IF) oder Bienen. Vorher waren IF und Bienen totes Holz.
NEU2 = [
    Q('z_erz', 'Erz ohne Sieb', 0, 0, [tag('skyandstone:erz_ohne_sieb', icon='industrialforegoing:ore_laser_base',
                                          title='Osmium-Samen, Erz-Laserbasis oder Netherquarz-Nest')],
      deps=['m_niemehr', 'h_laser', 'b_zucht'], dep_any=True, icon='industrialforegoing:ore_laser_base', shape=M, size=1.5,
      rewards=[crate('gold'), xp(100)]),
]
for q in NEU2: A[q.key] = q

# ---------------------------------------------------------------------
# 0.8.0: Prüfungen der Leere (Ersatz für die alten Haken-Quests) und Deko-Tausch im Markt
# ---------------------------------------------------------------------
PRUEF = [
    Q('t_chimera', 'Die Chimera', 0, 0, kill('ars_nouveau:wilden_boss'), deps=['a_ritual', 'c_messing'], shape=M, size=1.4,
      icon='ars_nouveau:wilden_tribute', rewards=[crate('gold', art='choice')]),
    Q('t_speicher', 'Der Speicher der Erbauer', 0, 0, energie(10_000_000), deps=['k_cube'], icon='mekanism:basic_energy_cube',
      rewards=[crate('gold')]),
    Q('t_fabrik', 'Tausend Barren', 0, 0, item('minecraft:iron_ingot', 1024), deps=['c_siebfabrik'], icon='minecraft:iron_block',
      rewards=[crate('eisen'), crate('eisen')]),
    Q('t_drache', 'Der zweite Drache', 0, 0, kill('minecraft:ender_dragon'), deps=['j_drache'], shape=M, size=1.4,
      icon='minecraft:dragon_head', rewards=[crate('stern', art='choice')]),
    # 26.10.2026: drei weitere Prüfungen (Idee teils aus der FreeLLMAPI-Zweitmeinung, _src/KI-PRUEFUNG/ANTWORT-2026-10-26-fusion.md,
    # geprüft: Festungen gibt es im leeren Nether, Enderman spawnen im End, Strom-Aufgabe mit max_input)
    Q('t_festung', 'Die Festung räumen', 0, 0, kill('minecraft:wither_skeleton', 50), deps=['j_festung', 'c_messing'],
      icon='minecraft:wither_skeleton_skull', rewards=[crate('gold')]),
    Q('t_schatten', 'Schattenjagd', 0, 0, kill('minecraft:enderman', 32), deps=['j_end', 'c_messing'],
      icon='minecraft:ender_eye', rewards=[crate('gold')]),
    Q('t_netz', 'Ein Netz ohne Ende', 0, 0, energie(1_000_000_000), deps=['t_speicher', 'z_sps'], shape=M, size=1.4,
      icon='mekanism:ultimate_energy_cube', rewards=[crate('stern', art='choice')]),
]
for q in PRUEF: A[q.key] = q
# Bauen bekommt einen Wert: Deko-Überschuss gegen Kisten. Verbrauchende Aufgaben nehmen keine Gruppe (Projektregel 4),
# deshalb eine feste Holzart (Eiche). Die Gruppen bleiben bei nicht verbrauchenden Aufgaben (u_dach, u_bruecke2).
DEKO = [
    B.tausch('x_dach', 'Dachdecker', 0, 0, 'mcwroofs:oak_roof', 64, 'eisen', B.TAG, ['u_dach', 'c_messing'], 'Eichen-Dachziegel im Überfluss.'),
    B.tausch('x_bruecke', 'Brückenbauer', 0, 0, 'mcwbridges:rope_oak_bridge', 32, 'holz', B.TAG, ['u_bruecke2'], 'Eichen-Hängebrücken für die Nachbarinseln.'),
]
for q in DEKO:
    A[q.key] = q

# ---------------------------------------------------------------------
# 0.11.0 „Die Wahl zählt“: Jeder Weg der beiden Wahlen hat eine eigene Quest mit eigener Belohnung (keiner sperrt etwas)
# ---------------------------------------------------------------------
WEGE = [
    Q('w_magie', 'Weg der Magie', 0, 0, item('ars_nouveau:archmage_spell_book'), deps=['a_erzmagier'], optional=True, shape=M,
      icon='ars_nouveau:archmage_spell_book', rewards=[crate('magie', art='choice'), give('ars_nouveau:source_gem_block', 4), give('ars_nouveau:enchanters_mirror')]),
    Q('w_maschine', 'Weg der Maschine', 0, 0, item('hostilenetworks:loot_fabricator'), deps=['h_fab'], optional=True, shape=M,
      icon='hostilenetworks:loot_fabricator', rewards=[crate('technik', art='choice'), give('create:brass_casing', 16)]),
    Q('w_felder', 'Weg der Felder', 0, 0, item('mysticalagriculture:osmium_seeds'), deps=['m_niemehr'], optional=True, shape=M,
      icon='mysticalagriculture:osmium_seeds', rewards=[crate('natur', art='choice'), give('minecraft:bone_meal', 64)]),
    Q('w_laser', 'Weg des Lasers', 0, 0, item('industrialforegoing:ore_laser_base'), deps=['h_laser'], optional=True, shape=M,
      icon='industrialforegoing:ore_laser_base', rewards=[crate('technik', art='choice'), give('minecraft:redstone', 32)]),
    Q('w_bienen', 'Weg der Bienen', 0, 0, item('productivebees:configurable_honeycomb', 1, komponenten={'productivebees:bee_type': 'productivebees:iron'}),
      deps=['b_zucht'], optional=True, shape=M, icon='productivebees:configurable_honeycomb',
      rewards=[crate('natur', art='choice'), give('productivelib:upgrade_simulator', 2)]),
]
for q in WEGE: A[q.key] = q
# 26.10.2026: Beide Zentrifugen-Rezepte brauchen Eisen (productivebees:centrifuge 7 Barren, centrifuge_cauldron über den
# Kessel, Rezept-Dump vom Testserver). Die Abhängigkeit macht das sichtbar; die 4 Eisenbarren als Belohnung überspringen
# damit nichts mehr (Prüfbericht: „Zentrifuge erfüllt Der Funke“).
A['b_zentri'].deps = ['b_stock', 'e_eisen']
# 26.10.2026: Ohne Eimer im Startinventar sind die Tiegel die einzige Wasser- und Lavaquelle auf der klassischen
# Insel (nur die Waldlichtung hat einen Teich). Prüfsuite (Spiellogik): Wasserrad, Lohenbrenner, Obsidian und alles
# danach brauchten den optionalen Holztiegel. Deshalb Pflicht und sichtbare Abhängigkeiten.
for _k, _d in (('c_rad', 'e_tiegel'), ('c_brenner', 'e_lavatiegel'), ('e_cobble', 'e_lavatiegel'),
               ('j_obsidian', 'e_lavatiegel'), ('e_lavatiegel', 'e_hammer')):
    if _d not in A[_k].deps: A[_k].deps.append(_d)

# A2/A5: Antimaterie hängt an Polonium statt am (jetzt optionalen) Großkraftwerk
A['z_sps'].deps = ['k_polonium', 'l_auto', 'z_elite']
A['z_sps'].desc = ['Polonium-Pellets im SPS (Supercritical Phase Shifter) werden zu Antimaterie. Ein einziges Pellet reicht.',
                   'Der SPS braucht sehr viel Strom: Spaltreaktor, Powah-Reaktor oder viele Generatoren.']
A['z_strom'].optional = True
A['z_strom'].desc = ['Optional: Ein großer Powah-Reaktor ist der bequeme Weg zu viel Strom.',
                     'Jede andere große Stromquelle (z. B. der Spaltreaktor) reicht für die Antimaterie auch.']
# A3: Mengen (jede Aufgabe wird einzeln erkannt, mehr bringt nichts)
A['z_insanium'].tasks = [item('mysticalagradditions:insanium_essence', 8)]
A['c_siebfabrik'].tasks = [item('minecraft:iron_ingot', 32), item('create:zinc_ingot', 16), item('minecraft:copper_ingot', 32)]
# A4: Finale braucht Magie ODER Maschinen
A['z_herr'].deps = ['z_fabrik', 'j_drache', 'm_niemehr', 'z_weg']
# 0.7.0: Erz-Wahl statt Pflicht-Felder (Felder bleiben über z_fabrik/z_netherstern trotzdem Teil des Endspiels)
A['z_herr'].deps = [d for d in A['z_herr'].deps if d != 'm_niemehr'] + ['z_erz']

# ---------------------------------------------------------------------
# 3. Hauptstory: (Schlüssel, Hauptstory-Vorgänger oder None)
#    Der Vorgänger wird als zusätzliche Abhängigkeit eingetragen, damit die Linie sichtbar ist.
#    None = nur die echten Voraussetzungen (Nebenzweig, z. B. Nether).
# ---------------------------------------------------------------------
# 0.6.2: erweitert auf 68 Quests (Spieltest: "zu wenig Quests in der Hauptstory"),
#        Vorschlag Gemini + Gegencheck der Parallel-Sitzung, siehe _src/GEMINI-HAUPTSTORY.md
# ---------------------------------------------------------------------
# 1.1.0 „Die sieben Splitter“ (_src/DESIGN-HERZ-DER-LEERE.md): Jeder Akt läuft auf Splitter des Herzens zu, die nur
# entstehen, wenn mehrere Mods zusammenarbeiten (Rezepte in kubejs/server_scripts/herz_rezepte.js). Danach Herz bauen,
# Wächter besiegen, Herz schlägt. Texte: texte_herz.py, Belohnungen: belohnungen.py.
# ---------------------------------------------------------------------
SP = 'skyandstone:'
HERZ = [
    Q('sp_rohling', 'Splitter-Rohling', 0, 0, item(SP + 'splitter_rohling', 2), deps=['c_messing'], icon=SP + 'splitter_rohling'),
    Q('sp_erde', 'Splitter der Erde', 0, 0, item(SP + 'splitter_erde'), deps=['c_siebfabrik', 'sp_rohling'], icon=SP + 'splitter_erde', size=2.0),
    Q('hz_werkstatt', 'Die vergessene Werkstatt', 0, 0, beobachte(SP + 'herzsockel_zerbrochen', 40), deps=['k_jetpack'],
      icon=SP + 'karte_werkstatt', shape=M, size=1.5),
    Q('sp_glut', 'Splitter der Glut', 0, 0, item(SP + 'splitter_glut'), deps=['j_lohe', 'sp_erde'], icon=SP + 'splitter_glut', shape=M, size=1.3),
    Q('sp_strom', 'Splitter des Stroms', 0, 0, item(SP + 'splitter_strom'), deps=['k_alloy', 's_orb', 'c_alternator', 'sp_erde'],
      icon=SP + 'splitter_strom', shape=M, size=1.3),
    Q('sp_ordnung', 'Splitter der Ordnung', 0, 0, item(SP + 'splitter_ordnung'), deps=['l_netz', 'sp_erde'], icon=SP + 'splitter_ordnung',
      shape=M, size=1.3),
    Q('hz_vier', 'Vier von Sieben', 0, 0, [item(SP + 'splitter_erde'), item(SP + 'splitter_glut'), item(SP + 'splitter_strom'),
                                          item(SP + 'splitter_ordnung')],
      deps=['sp_glut', 'sp_strom', 'sp_ordnung', 'hz_werkstatt'], icon=SP + 'herz_der_leere', size=2.0),
    Q('sp_essenz', 'Leerenessenz', 0, 0, item(SP + 'leerenessenz', 4), deps=['j_perlen', 'hz_vier'], icon=SP + 'leerenessenz'),
    Q('sp_leben', 'Splitter des Lebens', 0, 0, item(SP + 'splitter_leben'), deps=['m_imperium', 'b_biene', 'hz_vier'],
      icon=SP + 'splitter_leben', shape=M, size=1.3),
    Q('sp_geist', 'Splitter des Geistes', 0, 0, item(SP + 'splitter_geist'), deps=['j_wither', 'sp_essenz'], icon=SP + 'splitter_geist',
      shape=M, size=1.3),
    Q('sp_leere', 'Splitter der Leere', 0, 0, item(SP + 'splitter_leere'), deps=['j_drache', 'sp_essenz'], icon=SP + 'splitter_leere',
      shape=M, size=1.3),
    Q('hz_sockel', 'Der Herzsockel', 0, 0, item(SP + 'herzsockel'), deps=['hz_vier'], icon=SP + 'herzsockel'),
    Q('hz_herz', 'Das Herz der Leere', 0, 0, item(SP + 'herz_der_leere'), deps=['sp_leben', 'sp_geist', 'sp_leere', 'c_crafter'],
      icon=SP + 'herz_der_leere', shape=M, size=1.6),
    Q('hz_wache', 'Der letzte Wächter', 0, 0, fortschritt(SP + 'waechter_besiegt'), deps=['hz_herz', 'hz_sockel'],
      icon=SP + 'waechterkern', shape=M, size=1.8),
    Q('hz_schlag', 'Das Herz schlägt', 0, 0, fortschritt(SP + 'erster_herzschlag'), deps=['hz_wache'], icon=SP + 'herz_erwacht', size=1.5),
]
for q in HERZ: A[q.key] = q
A['c_crafter'].optional = False   # die Mechanische Handwerkseinheit baut das Herz (Pflicht)
A['z_herr'].deps.append('hz_schlag')

AKT1 = [
    ('w_start', None), ('e_holz', 'w_start'), ('e_raupe', 'e_holz'), ('e_fass', 'e_holz'), ('e_cobble', 'e_eisen'),
    # 26.10.2026: Sieb vor Hammer. Die klassische Insel hat keinen Stein (inseln.py), Bruchstein gibt es dort erst aus
    # 4 Stone Pebble vom Sieb (exdeorum:cobblestone). Kies (für Erzbrocken) kommt aus dem Hammer.
    ('e_sieb', 'e_fass'), ('e_hammer', 'e_sieb'), ('e_tiegel', 'e_sieb'), ('e_lavatiegel', 'e_tiegel'),
    ('e_brocken', 'e_hammer'), ('e_feuernetz', 'e_brocken'), ('e_eisen', 'e_feuernetz'),
    ('m_inferium', 'e_eisen'), ('m_prudentium', 'm_inferium'), ('m_altar', 'm_prudentium'),
    ('e_kupfer', 'e_eisen'), ('c_andesit', 'e_kupfer'), ('c_rad', 'c_andesit'), ('c_muehle', 'c_rad'), ('c_sifter', 'c_muehle'),
    ('c_extruder', 'c_muehle'), ('c_presse', 'c_sifter'), ('c_fan', 'c_presse'), ('c_mixer', 'c_presse'), ('c_brenner', 'c_mixer'),
    ('c_messing', 'c_brenner'), ('c_siebfabrik', 'c_messing'), ('sp_rohling', 'c_messing'), ('sp_erde', 'c_siebfabrik'),
]
AKT2 = [
    ('c_mechanismus', 'c_messing'), ('c_alternator', 'c_mechanismus'), ('k_osmium', 'c_alternator'), ('k_infuser', 'k_osmium'),
    ('k_alloy', 'k_infuser'), ('k_schalt', 'k_infuser'), ('k_enrich', 'k_infuser'), ('k_purif', 'k_enrich'),
    ('m_tertium', 'c_messing'), ('m_eisen', 'm_tertium'),
    ('j_obsidian', 'e_eisen'), ('j_nether', 'j_obsidian'), ('j_festung', 'j_nether'), ('j_lohe', 'j_festung'),
    ('k_jetpack', 'k_alloy'),
    ('l_certus', 'e_eisen'), ('l_lader', 'l_certus'), ('l_inscriber', 'm_tertium'), ('l_prozessoren', 'l_inscriber'), ('l_netz', 'l_prozessoren'),
    ('k_inject', 'k_purif'),
    ('hz_werkstatt', 'k_jetpack'), ('sp_glut', 'j_lohe'), ('sp_strom', 'k_alloy'), ('sp_ordnung', 'l_netz'), ('hz_vier', 'sp_glut'),
]
AKT3 = [
    ('l_auto', 'l_netz'), ('m_imperium', 'k_alloy'), ('m_supremium', 'm_imperium'), ('m_niemehr', 'm_supremium'),
    ('j_hexe', 'j_nether'), ('j_wither', 'j_hexe'), ('j_perlen', 'j_obsidian'), ('j_augen', 'j_perlen'), ('j_rahmen', 'j_augen'),
    ('j_end', 'j_rahmen'), ('j_drache', 'j_end'),
    ('z_elite', 'k_inject'), ('z_ultkreis', 'z_elite'), ('m_insanium', 'z_ultkreis'),
    ('k_spalt', 'z_elite'), ('k_polonium', 'k_spalt'), ('z_sps', 'k_polonium'),
    ('z_fabrik', 'z_sps'), ('z_weg', None), ('z_erz', None), ('z_herr', 'z_fabrik'),
    ('w_magie', None), ('w_maschine', None), ('w_felder', None), ('w_laser', None), ('w_bienen', None),
]
# 1.1.0: Akt IV „Sieben Splitter“ – die letzten drei Splitter, das Herz und der Wächter (eigenes Kapitel, Akt III war zu voll)
AKT4 = [
    ('sp_essenz', 'j_perlen'), ('sp_leben', 'm_imperium'), ('sp_geist', 'j_wither'), ('sp_leere', 'j_drache'), ('hz_sockel', 'hz_vier'),
    ('hz_herz', 'sp_leben'), ('hz_wache', 'hz_herz'), ('hz_schlag', 'hz_wache'),
]
HAUPT_KEYS = {k for akt in (AKT1, AKT2, AKT3, AKT4) for k, _ in akt}
for akt in (AKT1, AKT2, AKT3, AKT4):
    for k, v in akt:
        if v and v not in A[k].deps: A[k].deps.append(v)
for k, _ in AKT1[-1:] + AKT2[-1:] + AKT3[-1:] + AKT4[-1:]: A[k].shape = G

# ---------------------------------------------------------------------
# 0.6.2: Item-Gruppen statt einer festen Holzart/Farbe (Spieltest: "nur Eichenholz erlaubt").
#        Aufgaben mit diesen Items akzeptieren jedes Item der Gruppe (FTB Filter System, item_tag).
# ---------------------------------------------------------------------
GRUPPEN = {
    'minecraft:oak_log': ('minecraft:logs', 'Beliebige Holzstämme'),
    'minecraft:oak_sapling': ('minecraft:saplings', 'Beliebige Setzlinge'),
    'minecraft:wheat_seeds': ('c:seeds', 'Beliebige Samen'),
    'minecraft:wheat': ('c:crops', 'Beliebige Feldfrüchte'),
    'exdeorum:oak_barrel': ('exdeorum:wooden_barrels', 'Beliebiges Holzfass'),
    'exdeorum:oak_sieve': ('skyandstone:sieves', 'Beliebiges Sieb'),
    'exdeorum:oak_crucible': ('skyandstone:water_crucibles', 'Beliebiger Holztiegel'),
    'botanypots:terracotta_botany_pot': ('botanypots:botany_pots', 'Beliebiger Botany Pot'),
    'botanypots:terracotta_hopper_botany_pot': ('skyandstone:hopper_botany_pots', 'Beliebiger Trichter-Botany-Pot'),
    'functionalstorage:oak_1': ('functionalstorage:drawer', 'Beliebige Schubladen'),
    'handcrafted:oak_chair': ('handcrafted:chairs', 'Beliebige Stühle'),
    'handcrafted:oak_table': ('handcrafted:tables', 'Beliebiger Tisch'),
    'mcwroofs:oak_roof': ('skyandstone:roofs', 'Beliebige Dachblöcke'),
    'mcwbridges:rope_oak_bridge': ('skyandstone:rope_bridges', 'Beliebige Hängebrücke'),
    'ars_nouveau:blue_archwood_sapling': ('skyandstone:archwood_saplings', 'Beliebiger Archwood-Setzling'),
    'productivebees:advanced_oak_beehive': ('productivebees:advanced_beehives', 'Beliebiger fortgeschrittener Bienenstock'),
    # 0.8.0: Almost Unified vereinheitlicht Metalle schon (jeder Barren-Tag hat nur ein Mitglied); bei Certus zählt so auch geladener
    'ae2:certus_quartz_crystal': ('c:gems/certus_quartz', 'Certus-Quarz (auch geladen)'),
}
GRUPPEN_AUSNAHMEN = {'p_archwood'} | GRUPPEN_FEST   # Sammlerbuch: jede Farbe einzeln; g_feld: echter Weizen
for q in A.values():
    if q.key in GRUPPEN_AUSNAHMEN: continue
    q.tasks = [tag(GRUPPEN[t[1]][0], t[2], icon=t[1], title=GRUPPEN[t[1]][1]) if t[0] == 'item' and t[1] in GRUPPEN and not t[3] else t
               for t in q.tasks]

def kap(key, title, group, icon, keys, sub='', links=(), mode='baum'):
    keys = [k for k in keys if k not in ERSATZ]
    links = [l for l in links if l not in ERSATZ]
    if group == 'haupt':
        # Nachtschicht 0.6.3: Voraussetzungen aus Mod-Kapiteln als Verweis oben im Akt zeigen,
        # sonst ist eine Akt-Quest gesperrt, ohne dass man sieht, was fehlt (z. B. m_altar <- g_inferium).
        for k in keys:
            for d in A[k].deps:
                if d not in HAUPT_KEYS and d not in links: links.append(d)
    if group == 'mods':
        # Quests, die in der Hauptstory stehen, erscheinen im Mod-Kapitel als Verweis (nicht doppelt)
        for k in keys:
            if k in HAUPT_KEYS and k not in links: links.append(k)
        keys = [k for k in keys if k not in HAUPT_KEYS]
    return Chapter(key, title, group, icon, [A[k] for k in keys], sub=sub, links=links, mode=mode)

haupt = [
    kap('akt1', 'Akt I: Die Insel', 'haupt', 'exdeorum:oak_sieve', [k for k, _ in AKT1],
        sub=['Vom ersten Baum bis zur Siebfabrik.', 'Details zu jedem Schritt stehen in den Mod-Kapiteln.'], mode='pfad'),
    kap('akt2', 'Akt II: Maschinen', 'haupt', 'mekanism:metallurgic_infuser', [k for k, _ in AKT2],
        sub=['Strom, Mekanism, Nether, AE2 – die Insel wird zur Fabrik.'], mode='pfad'),
    kap('akt3', 'Akt III: Das Herz der Leere', 'haupt', 'mekanism:pellet_antimatter', [k for k, _ in AKT3],
        sub=['Autocrafting, Erz vom Feld, Bosse und Antimaterie.', 'Das Finale wartet, bis das Herz in Akt IV schlägt.'], mode='pfad'),
    kap('akt4', 'Akt IV: Sieben Splitter', 'haupt', 'skyandstone:herz_der_leere', [k for k, _ in AKT4],
        sub=['Leben, Geist und Leere. Dann das Herz und sein Wächter.', 'Jeder Splitter verlangt mehrere Mods zugleich.'], mode='pfad'),
]


# ---------------------------------------------------------------------
# 4. Mod-Kapitel
# ---------------------------------------------------------------------
mods = [
    kap('exdeorum', 'Ex Deorum: Sieben', 'mods', 'exdeorum:oak_sieve',
        ['e_haken', 'e_raupe', 'e_faden', 'e_fass', 'e_cobble', 'e_hammer', 'e_tiegel', 'e_lavatiegel', 'e_brocken', 'e_feuernetz',
         'e_eisennetz', 'e_kanne', 's_mechsieb', 's_mechhammer'],
        sub='Siebe, Netze, Tiegel und Gießkannen.', links=['e_holz', 'e_sieb', 'e_eisen']),
    kap('landwirtschaft', 'Landwirtschaft und Küche', 'mods', 'minecraft:wheat',
        ['e_samen', 'g_feld', 'g_topf', 'g_tiere', 'g_topf_pflanze', 'g_baumtopf', 'g_festessen', 'g_inferium', 'g_autark'],
        sub='Farmer\'s Delight, Botany Pots, Nutztiere.', links=['e_sieb']),
    kap('create', 'Create', 'mods', 'create:cogwheel',
        ['c_rad', 'c_muehle', 'c_netze', 'c_extruder', 'c_presse', 'c_fan', 'c_mixer', 'c_brenner', 'c_tertium', 'c_mechanismus',
         'c_deployer', 'c_crafter'],
        sub='Zahnräder, Mühlstein, Sifter, Messing.', links=['c_andesit', 'c_sifter', 'c_messing', 'c_siebfabrik']),
    kap('energie', 'Energie und Rohre', 'mods', 'powah:energy_cell_starter',
        ['s_akku', 's_orb', 's_stahl', 's_furnator', 's_solar', 's_kristall', 's_pipe', 's_upgrade', 's_reaktor', 'z_ultimate', 'z_strom'],
        sub='Create Crafts & Additions, Powah, Pipez.', links=['c_alternator']),
    kap('mekanism', 'Mekanism', 'mods', 'mekanism:metallurgic_infuser',
        ['k_stahl', 'k_schalt', 'k_alloy', 'k_cube', 'k_separator', 'k_purif', 'k_x5', 'k_fortschritt', 'k_meka', 'k_tiab', 'k_spalt', 'z_meka'],
        sub='Erzverarbeitung, Schaltkreise, Atomtechnik, Werkzeuge.',
        links=['k_osmium', 'k_infuser', 'k_enrich', 'k_inject', 'k_jetpack', 'z_elite', 'k_polonium', 'z_sps']),
    kap('lagerung', 'Lagerung', 'mods', 'functionalstorage:oak_1',
        ['l_rucksack', 'l_pickup', 'l_fass', 'l_schubladen', 'l_controller'],
        sub='Sophisticated Backpacks/Storage, Functional Storage.', links=['e_eisen']),
    kap('ae2', 'Applied Energistics 2', 'mods', 'ae2:controller',
        ['l_certus', 'l_lader', 'l_prozessoren', 'l_wireless', 'l_appmek', 'l_mega'],
        sub='ME-Netz, Autocrafting, kabellos.', links=['l_inscriber', 'l_netz', 'l_auto']),
    kap('mysticalag', 'Mystical Agriculture', 'mods', 'mysticalagriculture:inferium_seeds',
        ['m_altar', 'm_prudentium', 'm_eisen', 'm_kupfer', 'm_gold', 'm_diamant', 'm_beschleuniger', 'm_acker', 'z_insanium', 'z_netherstern'],
        sub=['Erz, das auf Feldern wächst.', 'Stufen: Inferium → Prudentium → Tertium (Create) → Imperium (Mekanism) → Supremium (AE2) → Insanium.'],
        links=['m_inferium', 'm_tertium', 'm_imperium', 'm_supremium', 'm_niemehr', 'm_insanium']),
    kap('ars', 'Ars Nouveau', 'mods', 'ars_nouveau:novice_spell_book',
        ['a_quelle', 'a_buch', 'a_tisch', 'a_glas', 'a_archwood', 'a_whirli', 'a_crush', 'a_starbuncle', 'a_drygmy', 'a_wilden',
         'a_apparat', 'a_ritual', 'a_wixie', 'a_erzmagier'],
        sub='Magie, die Arbeit spart: Transport, Mob-Drops, Autocrafting.', links=['e_eisen']),
    kap('bienen', 'Productive Bees', 'mods', 'productivebees:advanced_oak_beehive',
        ['b_biene', 'b_stock', 'b_zentri', 'b_nest', 'b_zucht', 'b_upgrade'],
        sub='Rohstoffe, die summen.', links=['e_sieb']),
    kap('dimensionen', 'Nether und End', 'mods', 'minecraft:obsidian',
        ['j_obsidian', 'j_festung', 'j_hexe', 'j_perlen', 'j_augen', 'j_rahmen', 'j_end', 'j_shulker'],
        sub='Festungen in der Leere, Wither und Drache.', links=['j_nether', 'j_lohe', 'j_wither', 'j_drache']),
    kap('maschinengeist', 'Hostile Networks und IF', 'mods', 'hostilenetworks:deep_learner',
        ['h_learner', 'h_modell', 'h_sim', 'h_fab', 'h_rahmen', 'h_plastik', 'h_laser'],
        sub='Mobs simulieren statt jagen, Erz per Laser.', links=['c_alternator']),
]

# ---------------------------------------------------------------------
# 5. Extras
# ---------------------------------------------------------------------
# Story: jede Notiz schaltet sich frei, wenn der passende Meilenstein erreicht ist (Quest ohne Aufgabe = erledigt sich selbst)
STORY = [
    ('w_start', 'Die erste Notiz', 'Notiz des letzten Wächters: „Wer das liest, steht auf einem Splitter unserer Welt. Darunter schläft das Herz der Leere.“'),
    ('e_sieb', 'Sternenstaub', '„Wir siebten einst Sternenstaub. Jetzt siebst du Kies – es ist derselbe Anfang.“'),
    ('e_eisen', 'Der Funke', '„Das erste Metall. Die Erbauer nannten es den Funken.“'),
    ('g_autark', 'Zurück zum Leben', '„Eine Insel, die sich selbst nährt, ist der erste Schritt zurück.“'),
    ('c_alternator', 'Die Leitungen', '…'),
    ('c_siebfabrik', 'Die erste Maschine', '„Unsere Maschinen arbeiteten Tag und Nacht. Du hast gerade die erste wieder geweckt.“'),
    ('sp_erde', 'Der erste Splitter', '…'),
    ('j_nether', 'Die zerbrochene Unterwelt', '„Auch die Unterwelt zerbrach. Unsere Festungen hängen dort noch in der Luft.“'),
    ('k_inject', 'Gier', '„Aus jedem Brocken das Vierfache. So reich waren wir – und so gierig.“'),
    ('hz_werkstatt', 'Die Werkstatt', '…'),
    ('hz_vier', 'Vier von sieben', '…'),
    ('l_auto', 'Netze, die denken', '„Unsere Netze dachten mit. Am Ende dachten sie schneller als wir.“'),
    ('m_niemehr', 'Felder aus Erz', '„Die Felder wuchsen Erz, als die Minen versiegt waren. Wenigstens das haben wir richtig gemacht.“'),
    ('k_spalt', 'Kraft aus der Leere', '„Wir nahmen die Kraft aus der Leere, nicht aus Kohle. Zu viel davon zerriss den Boden.“'),
    ('a_erzmagier', 'Maschine und Magie', '„Maschine und Magie waren für uns nie Gegensätze. Erst zusammen erreichten sie das Herz.“'),
    ('z_weg', 'Ein Weg genügt', '…'),
    ('h_fab', 'Feinde auswendig', '„Wir lernten unsere Feinde auswendig, bis wir sie nicht mehr bekämpfen mussten.“'),
    ('j_drache', 'Der Wächter am Ende', '„Der Drache bewachte das Ende, nicht für uns, sondern vor uns.“'),
    ('z_sps', 'Der Herzschlag', '„Antimaterie: der Herzschlag der Leere in einer Kapsel. Behandle sie mit Respekt.“'),
    ('hz_herz', 'Sieben in einem', '…'),
    ('hz_wache', 'Der letzte Wächter', '…'),
    ('z_herr', 'Das Erbe', '„Wer das Herz der Leere wieder schlagen lässt, trägt unser Erbe. Nimm nur, was du brauchst.“'),
]
# 0.6.2: Quests ohne Aufgabe gelten in FTB Quests sofort als erledigt (Spieltest). Darum steht jede Notiz jetzt
# oben im Meilenstein selbst, und das Story-Kapitel zeigt die Meilensteine als Verweis-Pfad. Fortschritt = echter Fortschritt.
# 0.6.4: Texte im Spielstil stehen in eigenen Dateien (_src/texte_*.py), Struktur und Aufgaben bleiben hier.
#        QUESTS = {schlüssel: (titel, [zeilen])}, KAPITEL = {kapitel: (titel, untertitel)}, STORY = {meilenstein: (titel, text)}
TEXT_FEHLER = []
SPAET_DEFINIERT = {'p_archiv'}
TEXT_MODULE = []
for _name in ('texte_hauptstory', 'texte_technik', 'texte_abenteuer', 'texte_herz'):
    try: TEXT_MODULE.append(__import__(_name))
    except ModuleNotFoundError: pass
_story = {ms: (t, x) for ms, t, x in STORY}
for _m in TEXT_MODULE:
    for k, (titel, zeilen) in getattr(_m, 'QUESTS', {}).items():
        if k in SPAET_DEFINIERT: continue   # Quests, die erst nach den Story-Seiten entstehen (Text kommt dort)
        if k not in A: TEXT_FEHLER.append(f'{_m.__name__}: unbekannte Quest {k}'); continue
        if any(z.startswith('&o') for z in zeilen): TEXT_FEHLER.append(f'{k}: Zeile beginnt mit &o (für Story-Notizen reserviert)')
        A[k].title, A[k].desc = titel, list(zeilen)
    for ms, (t, x) in getattr(_m, 'STORY', {}).items():
        if ms not in _story: TEXT_FEHLER.append(f'{_m.__name__}: unbekannte Story-Notiz {ms}'); continue
        _story[ms] = (t, x)
STORY = [(ms, t, x) for ms, (t, x) in _story.items()]
# 0.8.0: Belohnungen je Quest aus _src/belohnungen.py: ('item', id, n) · ('kiste', stufe) = Kiste zum Öffnen ·
#        ('wahl', stufe) = ein Item aus der Kiste aussuchen. Keine XP mehr. Markt-Tausche (x_*) behalten ihre Teamkiste.
try:
    import belohnungen as _bel
    for k, liste in _bel.BELOHNUNGEN.items():
        if k not in A: TEXT_FEHLER.append(f'belohnungen: unbekannte Quest {k}'); continue
        neu = []
        for r in liste:
            if r[0] == 'item': neu.append(give(r[1], r[2]))
            elif r[0] == 'kiste': neu.append(crate(r[1]))
            elif r[0] == 'wahl': neu.append(crate(r[1], art='choice'))
            else: TEXT_FEHLER.append(f'belohnungen: {k} unbekannte Art {r[0]}')
        A[k].rewards = neu
    for k, q in A.items():
        if k.startswith('x_'): continue
        q.rewards = [r for r in q.rewards if r[0] != 'xp']
except ModuleNotFoundError:
    pass
TEXT_FEHLER += [f'Story-Notiz {ms} hat noch keinen Text (Platzhalter …)' for ms, t, x in STORY if x.strip() in ('…', '...')]
story_q = []
import re as _re, textwrap as _tw
SEITEN = []
def tagebuchseite(nr, titel, text):
    j = lambda t, farbe, kursiv=False: json.dumps({'text': t, 'color': farbe, 'italic': kursiv}, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    zeilen = [j(f'Seite {nr} von {len(STORY)}', 'dark_purple')] + [j(z, 'gray', True) for z in _tw.wrap(text, 34)]
    return {'minecraft:custom_name': j(f'Tagebuch: {titel}', 'light_purple'), 'minecraft:lore': zeilen,
            'minecraft:enchantment_glint_override': __import__('ftbformat').Byte(1)}   # FTB schreibt 1b
def _woerter(t): return {w.lower() for w in _re.findall(r'[A-Za-zÄÖÜäöüß]{4,}', t)}
for ms, titel, text in STORY:
    rest = [d for d in A[ms].desc if not d.startswith('&o')]
    # 0.6.4: Wiederholt die erste Stimmungszeile nur die Notiz, fällt sie weg (sonst steht das Zitat doppelt da)
    if rest:
        a, b = _woerter(rest[0]), _woerter(text)
        if a and len(a & b) / len(a) >= 0.4:
            rest = rest[1:]
            if rest and rest[0] == '': rest = rest[1:]
    A[ms].desc = [f'&5&lNotiz: {titel}', '&o' + text, ''] + rest
    # 0.10.0: Jede Notiz gibt es zusätzlich als Tagebuchseite (Papier mit Titel und Text) zum Sammeln
    A[ms].rewards = A[ms].rewards + [give('minecraft:paper', 1, komponenten=tagebuchseite(len(SEITEN) + 1, titel, text))]
    SEITEN.append(ms)

# 0.11.0: Archiv des Wächters – wer alle 17 Seiten besitzt, bekommt den Codex (alle Notizen in einem Buch)
_seiten = {ms: tagebuchseite(n + 1, t, x) for n, (ms, t, x) in enumerate(STORY)}
_j = lambda d: json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
A['p_archiv'] = Q('p_archiv', 'Das Archiv des Wächters', 0, 0,
    [item('minecraft:paper', 1, komponenten={'minecraft:custom_name': _seiten[ms]['minecraft:custom_name']}) for ms, _, _ in STORY],
    deps=['z_herr'], shape=G, size=1.6, icon='minecraft:chiseled_bookshelf',
    rewards=[give('minecraft:written_book', 1, komponenten={'minecraft:written_book_content': {
                'author': 'Der letzte Wächter', 'resolved': __import__('ftbformat').Byte(1), 'title': {'raw': 'Codex der Erbauer'},
                'pages': [{'raw': json.dumps(t + chr(10) + chr(10) + x, ensure_ascii=False)} for _, t, x in STORY]}}),   # Minecraft speichert reinen Text als JSON-String
             give('minecraft:bookshelf', 16), give('minecraft:lectern', 1), give('minecraft:lantern', 4)])
for _m in TEXT_MODULE:
    if 'p_archiv' in getattr(_m, 'QUESTS', {}): A['p_archiv'].title, A['p_archiv'].desc = _m.QUESTS['p_archiv'][0], list(_m.QUESTS['p_archiv'][1])
extras = [
    Chapter('story', 'Story: Das Herz der Leere', 'extras', 'minecraft:writable_book', [],
            sub=['Die Notizen des letzten Wächters, in der Reihenfolge der Geschichte.',
                 'Jede Notiz steht im zugehörigen Meilenstein und wird lesbar, sobald du ihn erreichst.'],
            links=[ms for ms, _, _ in STORY], mode='pfad'),
    kap('markt', 'Inselmarkt', 'extras', 'minecraft:emerald', [k for k in A if k.startswith('x_')],
        sub=['Überschuss gegen Beutekisten tauschen. Die Items werden beim Abgeben verbraucht.',
             'Jeder Tausch hat eine Abklingzeit. Kisten fallen auch selten von Monstern, Bosse lassen immer eine fallen.']),
    kap('sammler', 'Sammlerbuch', 'extras', 'minecraft:book', ['p_essenzen', 'p_netze', 'p_archwood', 'p_trophaeen', 'p_archiv'],
        sub='Optional: Sammle alles einmal.'),
    kap('bau', 'Baumeister', 'extras', 'rechiseled:chisel', ['u_meissel', 'u_dach', 'u_moebel2', 'u_bruecke2', 'u_framed', 'u_gadget', 'u_kopie'],
        sub='Optional: schön statt nur praktisch.'),
    kap('pruefungen', 'Prüfungen der Leere', 'extras', 'minecraft:spyglass', [q.key for q in PRUEF],
        sub='Optional: Herausforderungen für Ingenieure und Mutige.'),
]

# 0.10.0: Themen-Kisten – in den Mod-Kapiteln passt der Inhalt zum Thema (Holz-/Eisenkisten werden ersetzt, wenn die Stufe passt)
THEMA = {'ars': 'magie', 'landwirtschaft': 'natur', 'bienen': 'natur', 'create': 'technik', 'energie': 'technik',
         'mekanism': 'technik', 'ae2': 'technik', 'lagerung': 'technik'}
import sperren as _sp
def _ahnen(k, s=None):
    s = set() if s is None else s
    for d in A[k].deps:
        if d not in s: s.add(d); _ahnen(d, s)
    return s
for c in mods:
    th = THEMA.get(c.key)
    if not th: continue
    gate = _sp.KISTE_AB.get(th)
    for q in c.quests:
        if gate and gate != q.key and gate not in _ahnen(q.key): continue
        q.rewards = [crate(th, r[2], r[3]) if r[0] == 'table' and r[1] in ('holz', 'eisen') else r for r in q.rewards]

# Meilenstein-Feier: Titel und Glockenton als Befehls-Belohnung. Die Funktionen liegen in
# kubejs/data/skyandstone/function/feier/<Schlüssel>.mcfunction. Nur Quests, die im Buch stehen und
# keine Story-Feier haben (e_eisen = funke, j_drache = drache, a_erzmagier = magie, s_reaktor = strom,
# l_auto = netz, m_niemehr = essenz). w_start hat die Begrüßung. Die Belohnungen oben werden erst
# hier vergeben, sonst überschreibt die Neuzuweisung aus belohnungen.py sie.
FEIER = ['g_autark', 'c_siebfabrik', 'k_inject', 'k_jetpack', 'z_herr', 'x_perlen', 'p_archiv']
for _key in FEIER:
    if _key not in ALLE:
        sys.exit(f'Feier: Quest {_key} fehlt')
    if not os.path.exists(os.path.join(PACK, 'kubejs', 'data', 'skyandstone', 'function', 'feier', _key + '.mcfunction')):
        sys.exit(f'Feier: Funktionsdatei für {_key} fehlt')
    ALLE[_key].rewards.append(('command', 'function skyandstone:feier/' + _key))

GROUPS = [('haupt', 'Hauptstory'), ('mods', 'Mods'), ('extras', 'Extras')]
CHAPTERS = haupt + mods + extras
_kap = {c.key: c for c in CHAPTERS}
for _m in TEXT_MODULE:
    for k, (titel, sub) in getattr(_m, 'KAPITEL', {}).items():
        if k not in _kap: TEXT_FEHLER.append(f'{_m.__name__}: unbekanntes Kapitel {k}'); continue
        _kap[k].title, _kap[k].sub = titel, sub
for _m in TEXT_MODULE:
    for k, problem in getattr(_m, 'PROBLEME', {}).items():   # 0.11.0: jedes Kapitel beginnt mit dem Problem, das es löst
        if k not in _kap: TEXT_FEHLER.append(f'{_m.__name__}: PROBLEME für unbekanntes Kapitel {k}'); continue
        sub = _kap[k].sub if isinstance(_kap[k].sub, list) else [_kap[k].sub]
        _kap[k].sub = ['&6' + problem] + sub
for _m in TEXT_MODULE:
    GROUPS = [(g, getattr(_m, 'GRUPPEN', {}).get(g, t)) for g, t in GROUPS]

def pruefe_struktur():
    fehler = []
    benutzt = {}
    for c in CHAPTERS:
        for q in c.quests:
            if q.key in benutzt: fehler.append(f'{q.key} in {benutzt[q.key]} und {c.key}')
            benutzt[q.key] = c.key
            if any(t[0] == 'checkmark' for t in q.tasks): fehler.append(f'{q.key}: Haken-Aufgabe')
            if not q.tasks: fehler.append(f'{q.key}: keine Aufgabe (FTB Quests hakt sie sofort ab)')
    for k in A:
        if k not in benutzt: fehler.append(f'{k} in keinem Kapitel')
    # B7 (0.6.1): Logik-Regeln, damit kein Stand mehr mit verwaisten oder blockierten Quests entsteht
    alle = {q.key: q for c in CHAPTERS for q in c.quests}
    for k, q in alle.items():
        if k != 'w_start' and not q.deps: fehler.append(f'{k}: keine Voraussetzung (steht frei im Buch)')
        if not q.optional:
            for d in q.deps:
                if d in alle and alle[d].optional and not q.dep_any: fehler.append(f'{k}: Pflicht-Quest hängt an optionaler Quest {d}')
        if k.startswith('st_'):
            for d in q.deps:
                ms = k[3:]
                if not (d == ms or d in HAUPT_KEYS or (d.startswith('st_') and d[3:] in HAUPT_KEYS)):
                    fehler.append(f'{k}: Story hängt an Nicht-Hauptstory-Quest {d}')
        if q.dep_any and len(q.deps) < 2: fehler.append(f'{k}: „eins von“ mit weniger als 2 Voraussetzungen')
    # 0.8.0: Belohnungen dürfen keine Stufe überspringen (_src/sperren.py)
    import sperren
    def ahnen(k, s=None):
        s = set() if s is None else s
        for d in alle.get(k).deps if k in alle else []:
            if d not in s: s.add(d); ahnen(d, s)
        return s
    fehler += sperren.pruefe(alle, ahnen)
    # Zyklen
    g = {q.key: q.deps for c in CHAPTERS for q in c.quests}
    seen, stack = set(), set()
    def dfs(k):
        if k in stack: fehler.append(f'Zyklus bei {k}'); return
        if k in seen: return
        seen.add(k); stack.add(k)
        for d in g.get(k, []): dfs(d)
        stack.discard(k)
    for k in g: dfs(k)
    return fehler

def pruefe_kisten_texte(tabellen, kisten):
    """TODO 10.6: Jede Lootkiste hat einen Text, und die Herkunftszeile stimmt mit den Drop-Gewichten überein."""
    f = []
    drops = {name + 'kiste': d.get('loot_crate', {}).get('drops', {}) for name, (_, d) in tabellen.items()}
    for k in kisten:
        if k not in drops: f.append(f'hinweise_daten.KISTEN: keine Belohnungstabelle mit string_id {k}')
    for k, d in drops.items():
        if k not in kisten: f.append(f'hinweise_daten.KISTEN: Text fehlt für {k}'); continue
        herkunft = kisten[k][1]
        for art, wort in (('boss', 'Bossen'), ('monster', 'Monstern'), ('passive', 'Tieren')):
            if (d.get(art, 0) > 0) != (wort in herkunft):
                f.append(f'hinweise_daten.KISTEN[{k}]: Herkunft „{herkunft}“ passt nicht zu Drops {art}={d.get(art, 0)}')
    return f

def schreibe_questindex(b):
    """26.10.2026: _src/questindex.json (Schlüssel -> Hex-ID, Kapitel, Titel). Die Prüfsuite liest nur die
    Questdateien (Hex-IDs); damit kann sie Schlüssel aus _src (z. B. sperren.py) zuordnen."""
    idx = {q.key: {'id': b.qids[q.key], 'kapitel': c.key, 'titel': q.title, 'optional': bool(getattr(q, 'optional', False))}
           for c in CHAPTERS for q in c.quests if q.key in b.qids}
    with open(os.path.join(PACK, '_src', 'questindex.json'), 'w', encoding='utf-8', newline=chr(10)) as f:
        json.dump(idx, f, ensure_ascii=False, indent=1, sort_keys=True)

def schreibe_hinweise():
    """0.11.0: kubejs/client_scripts/hinweise.js aus _src/hinweise_daten.py (eine Quelle, IDs geprüft in main)."""
    import hinweise_daten as H
    z = ['// ERZEUGT von _src/quests.py aus _src/hinweise_daten.py – nicht von Hand ändern.', 'const HINWEISE = {']
    z += [f'  {json.dumps(k)}: {json.dumps(v, ensure_ascii=False)},' for k, v in H.HINWEISE.items()]
    z += ['}', '', 'ItemEvents.modifyTooltips(event => {',
          '  Object.keys(HINWEISE).forEach(id => event.add(id, HINWEISE[id].map(t => Text.gray(t))))', '})', '',
          "RecipeViewerEvents.addInformation('item', event => {",
          '  Object.keys(HINWEISE).forEach(id => event.add(id, HINWEISE[id]))', '})', '']
    # TODO 10.6: Lootkisten sind alle dasselbe Item (ftbquests:lootcrate), die Art steht in der Komponente
    # ftbquests:loot_crate (String = string_id, aus dem FTB-Quests-Jar 2101.1.37). Deshalb dynamischer Tooltip.
    z += ['const KISTEN = {']
    z += [f'  {json.dumps(k)}: {json.dumps(list(v), ensure_ascii=False)},' for k, v in H.KISTEN.items()]
    z += ['}', '', 'ItemEvents.modifyTooltips(event => {',
          "  event.modify('ftbquests:lootcrate', t => t.dynamic('skyandstone_kiste'))", '})', '',
          "ItemEvents.dynamicTooltips('skyandstone_kiste', event => {",
          "  const m = String(event.item.componentString).match(/ftbquests:loot_crate\\s*=>?\\s*[\\\"']?([a-z0-9_]+)/)",
          '  const k = m ? KISTEN[m[1]] : null',
          '  if (!k) return',
          '  event.add([Text.gold(k[0]).italic(true), Text.darkGray(k[1])])', '})', '']
    with open(os.path.join(PACK, 'kubejs', 'client_scripts', 'hinweise.js'), 'w', encoding='utf-8', newline=chr(10)) as f:
        f.write(chr(10).join(z))

def schreibe_quest_tooltips():
    """0.10.0: Tooltip „Gebraucht für: <Quest>“ an jedem Aufgaben-Item (aus den Questdaten, deshalb immer aktuell)."""
    titel_kap = {q.key: c.title for c in CHAPTERS for q in c.quests}
    nutzung = {}
    for c in CHAPTERS:
        for q in c.quests:
            if q.repeat: continue                       # Markt-Tausche nicht, sonst stünde an jedem Rohstoff ein Händler
            for t in q.tasks:
                ids = [t[1]] if t[0] == 'item' else ([t[3]] if t[0] == 'tag' and t[3] else [])
                for i in ids:
                    nutzung.setdefault(i, [])
                    if q.title not in [x[0] for x in nutzung[i]]: nutzung[i].append((q.title, titel_kap[q.key]))
    zeilen = ['// ERZEUGT von _src/quests.py – nicht von Hand ändern. Zeigt an Aufgaben-Items, wofür sie im Questbuch gebraucht werden.',
              'const QUEST_NUTZUNG = {']
    for i in sorted(nutzung):
        n = nutzung[i]
        text = '; '.join(f'{t} ({k.split(":")[0]})' for t, k in n[:2]) + (f' und {len(n) - 2} weitere' if len(n) > 2 else '')
        zeilen.append(f'  {json.dumps(i)}: {json.dumps(text, ensure_ascii=False)},')
    zeilen += ['}', '', 'ItemEvents.modifyTooltips(event => {',
               '  Object.keys(QUEST_NUTZUNG).forEach(id => event.add(id, Text.darkAqua("Questbuch: " + QUEST_NUTZUNG[id])))',
               '})', '']
    pfad = os.path.join(PACK, 'kubejs', 'client_scripts', 'quest_tooltips.js')
    with open(pfad, 'w', encoding='utf-8', newline=chr(10)) as f: f.write(chr(10).join(zeilen))

def main():
    items = json.load(open(os.path.join(PACK, '_src', 'items.json'), encoding='utf-8'))['items']
    tags = json.load(open(os.path.join(PACK, '_src', 'tags.json'), encoding='utf-8'))
    b = Builder(os.path.join(PACK, 'config', 'ftbquests'), items, tags)
    # 0.8.0: jede Kiste gibt mehrere Items (loot_size), Inhalt passt zur Spielphase und hilft beim nächsten Schritt
    b.table('holz', 'Holzkiste', [('minecraft:string', 4, 10), ('minecraft:bone_meal', 12, 10), ('minecraft:flint', 4, 8),
        ('minecraft:oak_sapling', 2, 6), ('minecraft:birch_sapling', 2, 6), ('minecraft:baked_potato', 6, 8), ('minecraft:clay_ball', 8, 6),
        ('minecraft:iron_nugget', 6, 6), ('minecraft:torch', 12, 6), ('minecraft:dirt', 16, 6)],
        loot_size=3, crate=(0x8B5A2B, False, 3, 8, 0))
    b.table('eisen', 'Eisenkiste', [('minecraft:iron_ingot', 6, 10), ('minecraft:copper_ingot', 8, 10), ('create:zinc_ingot', 3, 8),
        ('create:andesite_alloy', 12, 8), ('minecraft:redstone', 12, 8), ('minecraft:coal', 12, 8), ('create:cogwheel', 6, 6),
        ('create:shaft', 8, 6), ('minecraft:lapis_lazuli', 8, 4), ('exdeorum:flint_mesh', 1, 4)],
        loot_size=3, crate=(0xC8C8C8, False, 0, 3, 0))
    b.table('gold', 'Goldkiste', [('minecraft:diamond', 2, 6), ('create:brass_ingot', 6, 8), ('mekanism:ingot_osmium', 6, 8),
        ('mysticalagriculture:prudentium_essence', 12, 6), ('minecraft:ender_pearl', 3, 6), ('minecraft:gold_ingot', 6, 8),
        ('minecraft:quartz', 16, 6), ('minecraft:glowstone_dust', 12, 6), ('mysticalagriculture:prosperity_shard', 8, 6)],
        loot_size=3, crate=(0xFFD700, False, 0, 0, 5))
    # 26.10.2026 (Entscheidung ohne Spieltest): Früh-Wahl bei Messing und Siebfabrik ohne Diamant und Osmium,
    # die sind Zwischenstufen der Mekanism- und Mystical-Ketten (AUDIT-BELOHNUNGEN-0.11.md, Befund 1).
    b.table('messing', 'Messing-Kiste', [('minecraft:iron_ingot', 6, 8), ('minecraft:copper_ingot', 6, 8), ('create:brass_ingot', 6, 8),
        ('mysticalagriculture:prudentium_essence', 12, 6), ('minecraft:ender_pearl', 3, 6), ('minecraft:gold_ingot', 6, 8),
        ('minecraft:quartz', 16, 6), ('minecraft:glowstone_dust', 12, 6), ('mysticalagriculture:prosperity_shard', 8, 6)],
        loot_size=3, crate=(0xB5A642, False, 0, 0, 0))   # 26.10.: eigene Messingfarbe, keine Boss-Drops (war Kopie der Goldkiste; Bosse geben wie vorher Gold/Stern)
    b.table('magie', 'Kiste der Magie', [('ars_nouveau:source_gem', 8, 10), ('ars_nouveau:magebloom_fiber', 4, 8), ('minecraft:amethyst_shard', 8, 8),
        ('minecraft:lapis_lazuli', 8, 8), ('minecraft:glowstone_dust', 8, 6), ('minecraft:experience_bottle', 4, 6),
        ('minecraft:gold_ingot', 3, 6), ('ars_nouveau:blue_archwood_sapling', 1, 4)], loot_size=3, crate=(0x7B3FB0, True, 0, 0, 0))
    b.table('technik', 'Kiste der Technik', [('create:andesite_alloy', 8, 10), ('create:cogwheel', 4, 8), ('create:shaft', 8, 8),
        ('create:iron_sheet', 4, 8), ('create:copper_sheet', 4, 6), ('create:belt_connector', 4, 6), ('minecraft:redstone', 12, 8),
        ('create:andesite_casing', 2, 6), ('create:fluid_pipe', 8, 4)], loot_size=3, crate=(0xB87333, False, 0, 0, 0))
    b.table('natur', 'Kiste der Natur', [('minecraft:bone_meal', 16, 10), ('minecraft:wheat_seeds', 8, 8), ('farmersdelight:cabbage_seeds', 4, 6),
        ('farmersdelight:tomato_seeds', 4, 6), ('minecraft:carrot', 6, 6), ('minecraft:potato', 6, 6), ('minecraft:sugar_cane', 4, 6),
        ('minecraft:oak_sapling', 2, 6), ('botanypots:terracotta_botany_pot', 2, 4), ('minecraft:cooked_beef', 4, 6), ('minecraft:honeycomb', 2, 4)],
        loot_size=3, crate=(0x4CAF50, False, 0, 0, 0))
    b.table('stern', 'Sternkiste', [('mysticalagradditions:nether_star_shard', 2, 4),
        ('minecraft:enchanted_golden_apple', 1, 3),
        # 26.10.2026 Leon: Netherit-Schrott 1 statt 4 (4 Schrott + 4 Gold = Netheritbarren, Pipez-Ultimate-Schranke)
        ('minecraft:netherite_scrap', 1, 5), ('minecraft:diamond', 8, 8), ('minecraft:totem_of_undying', 1, 3)],
        loot_size=2, crate=(0xA020F0, True, 0, 0, 5))
    fehler = pruefe_struktur() + TEXT_FEHLER
    import hinweise_daten as _H
    fehler += [f'hinweise_daten: unbekanntes Item {k}' for k in _H.HINWEISE if k not in items]
    fehler += pruefe_kisten_texte(b.tables, _H.KISTEN)
    errors = b.write(GROUPS, CHAPTERS, 'Sky and Stone', vorfehler=fehler)   # schreibt nur, wenn alles stimmt
    if not errors: schreibe_quest_tooltips(); schreibe_hinweise(); schreibe_questindex(b)
    nq = sum(len(c.quests) for c in CHAPTERS)
    print(f'{len(CHAPTERS)} Kapitel, {nq} Quests ({len(HAUPT_KEYS)} Hauptstory, {len(story_q)} Story), {len(b.tables)} Belohnungstabellen')
    kreuz = sum(len(r['kreuzt']) for r in b.layout.values())
    print(f'Layout: {len(b.hinweise)} Probleme (Linie durch Quest / Überlappung), {kreuz} Linienkreuzungen')
    for h in b.hinweise: print('HINWEIS:', h)
    for e in errors: print('FEHLER:', e)
    if errors: print('Nichts geschrieben – die Questdateien sind unverändert.')
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())

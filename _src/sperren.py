"""Items, die als Quest-Belohnung erst ab einem bestimmten Meilenstein erlaubt sind (0.8.0).

Der Generator prüft: Gibt eine Quest so ein Item, muss der Meilenstein die Quest selbst oder eine ihrer
(indirekten) Voraussetzungen sein. Sonst würde die Belohnung eine Stufe überspringen.
VERBOTEN: Items, die nie als Belohnung kommen sollen (Maschinen-Kerne, Stufen-Samen, Prägeplatten …).
"""
import re

AB = {
    # Create / Messing-Schwelle
    'create:brass_ingot': 'c_messing', 'create:brass_sheet': 'c_messing', 'create:brass_nugget': 'c_messing',
    'create:brass_casing': 'c_messing', 'create:precision_mechanism': 'c_mechanismus', 'createsifter:brass_mesh': 'c_messing',
    'create:blaze_burner': 'c_brenner', 'createsifter:zinc_mesh': 'c_sifter',
    # Mystical Agriculture: Essenz-Stufen
    'mysticalagriculture:prudentium_essence': 'm_inferium', 'mysticalagriculture:tertium_essence': 'm_tertium',
    'mysticalagriculture:imperium_essence': 'm_imperium', 'mysticalagriculture:supremium_essence': 'm_supremium',
    'mysticalagradditions:insanium_essence': 'm_insanium', 'mysticalagriculture:infusion_crystal': 'm_inferium',
    # Mekanism
    'mekanism:ingot_osmium': 'k_osmium', 'mekanism:alloy_infused': 'k_alloy', 'mekanism:alloy_reinforced': 'z_elite',
    'mekanism:alloy_atomic': 'z_elite', 'mekanism:basic_control_circuit': 'k_schalt', 'mekanism:advanced_control_circuit': 'k_alloy',
    'mekanism:elite_control_circuit': 'z_elite', 'mekanism:ultimate_control_circuit': 'z_ultkreis', 'mekanism:ingot_steel': 'k_stahl',
    # AE2
    'ae2:logic_processor': 'l_prozessoren', 'ae2:calculation_processor': 'l_prozessoren', 'ae2:engineering_processor': 'l_prozessoren',
    'ae2:fluix_crystal': 'l_lader', 'ae2:certus_quartz_crystal': 'l_certus',
    # Nether / End / Bosse
    'minecraft:blaze_rod': 'j_lohe', 'minecraft:nether_star': 'j_wither', 'mysticalagradditions:nether_star_shard': 'j_wither',
    'minecraft:netherite_ingot': 'j_nether', 'minecraft:netherite_scrap': 'j_nether', 'minecraft:ancient_debris': 'j_nether',
    'minecraft:ender_eye': 'j_augen', 'minecraft:end_portal_frame': 'j_rahmen', 'minecraft:shulker_shell': 'j_end',
    'minecraft:dragon_breath': 'j_drache', 'minecraft:elytra': 'j_drache',
}
VERBOTEN = [
    r'^mysticalagriculture:(?!inferium_seeds$).*_seeds$',   # Ressourcen-Samen sind der Fortschritt selbst
    r'^ae2:.*_press$', r'^ae2:controller$', r'^mekanism:pellet_', r'^mekanism:.*_reactor', r'^mekanismgenerators:',
    r'^hostilenetworks:', r'^industrialforegoing:(?!plastic$|dryrubber$|tinydryrubber$)', r'^ars_nouveau:.*_spell_book$',
    r'^ironjetpacks:jetpack$', r'^tiab:', r'^minecraft:(dragon_egg|totem_of_undying|enchanted_golden_apple)$',
    r'^skyandstone:(splitter_(?!rohling$).*|herz_der_leere|herz_erwacht|waechterkern)$',   # 1.1.0: Story-Objekte nur aus eigener Arbeit
]

# Kisten-Stufen: Goldkiste enthält Messing/Osmium, Sternkiste Endgame-Items. Bosse dürfen früher (großer Aufwand).
KISTE_AB = {'gold': 'c_messing', 'stern': 'c_messing',
            'technik': 'c_andesit', 'magie': 'a_quelle', 'natur': 'e_sieb'}   # Themen-Kisten (0.10.0)
KISTE_AUSNAHMEN = {'j_wither', 'j_drache', 't_drache',
                   'a_erzmagier', 'p_essenzen', 'p_trophaeen'}   # Aufgabe selbst verlangt Netherstern, Insanium bzw. Drachenei

def pruefe(alle, ahnen):
    """alle: {schlüssel: Q}, ahnen(k) -> Menge aller Voraussetzungen. Gibt Fehlerliste zurück."""
    fehler = []
    for k, q in alle.items():
        for r in q.rewards:
            if r[0] == 'table':
                gate = KISTE_AB.get(r[1])
                if gate and k not in KISTE_AUSNAHMEN and gate != k and gate not in ahnen(k):
                    fehler.append(f'{k}: {r[1]}-Kiste erst ab {gate}')
                continue
            if r[0] != 'give': continue
            i = r[1]
            if any(re.match(p, i) for p in VERBOTEN): fehler.append(f'{k}: Belohnung {i} ist gesperrt (sperren.VERBOTEN)')
            gate = AB.get(i)
            if gate and gate != k and gate not in ahnen(k):
                fehler.append(f'{k}: Belohnung {i} erst ab {gate} erlaubt (überspringt eine Stufe)')
    return fehler

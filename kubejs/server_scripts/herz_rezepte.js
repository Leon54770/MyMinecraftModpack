// Sky and Stone 1.1.0 „Die sieben Splitter“: Rezepte der neuen Hauptstory (Design: _src/DESIGN-HERZ-DER-LEERE.md).
// Jeder Splitter entsteht in der Maschine einer Mod aus Zutaten mehrerer anderer Mods. Formate aus den Mod-Jars
// übernommen (26.10.2026): create:mixing, powah:energizing, ae2:inscriber, farmersdelight:cooking,
// ars_nouveau:enchanting_apparatus/imbuement, industrialforegoing:dissolution_chamber, mekanism:nucleosynthesizing,
// create:mechanical_crafting. Mengen sind ein Entwurf: nach dem Spieltest nachjustieren (Balance nur nach Messung).

ServerEvents.recipes(event => {
  const S = id => ({ item: id })
  const R = 'skyandstone:splitter_rohling'
  const ergebnis = id => ({ count: 1, id: id })

  // Rohling: die Hülle für jeden Splitter. Glas + Amethyst (Flint Mesh auf Crushed Deepslate), Akt I.
  event.shaped(Item.of(R, 2), [' G ', 'GAG', ' G '], { G: 'minecraft:glass', A: 'minecraft:amethyst_shard' })
    .id('skyandstone:herz/rohling')

  // 1 Erde (Akt I): beheizter Create-Mixer. Ex Deorum (Kies, Sand, Staub), Mystical Agriculture, Messing.
  event.custom({
    type: 'create:mixing', heat_requirement: 'heated',
    ingredients: [S(R), S('minecraft:gravel'), S('minecraft:sand'), S('exdeorum:dust'),
      S('mysticalagriculture:prudentium_essence'), S('mysticalagriculture:prudentium_essence'),
      S('mysticalagriculture:prudentium_essence'), S('mysticalagriculture:prudentium_essence'),
      S('create:brass_ingot'), { type: 'neoforge:single', amount: 250, fluid: 'minecraft:water' }],
    results: [ergebnis('skyandstone:splitter_erde')]
  }).id('skyandstone:herz/splitter_erde')

  // 2 Glut (Akt II): überhitzter Mixer (Lohenkuchen im Brenner). Nether-Lohenruten, Netherrack aus dem Hammer, Obsidian, Lava.
  event.custom({
    type: 'create:mixing', heat_requirement: 'superheated',
    ingredients: [S(R), S('minecraft:blaze_rod'), S('minecraft:blaze_rod'),
      S('exdeorum:crushed_netherrack'), S('exdeorum:crushed_netherrack'), S('exdeorum:crushed_netherrack'),
      S('exdeorum:crushed_netherrack'), S('minecraft:obsidian'),
      { type: 'neoforge:single', amount: 250, fluid: 'minecraft:lava' }],
    results: [ergebnis('skyandstone:splitter_glut')]
  }).id('skyandstone:herz/splitter_glut')

  // 3 Strom (Akt II): Powah Energizing Orb. Mekanism (Legierung, Osmium), Create Crafts & Additions (Kupferspule), Redstone.
  event.custom({
    type: 'powah:energizing', energy: 500000,
    ingredients: [S(R), S('mekanism:alloy_infused'), S('mekanism:alloy_infused'), S('mekanism:ingot_osmium'),
      S('createaddition:copper_spool'), S('minecraft:redstone_block')],
    result: ergebnis('skyandstone:splitter_strom')
  }).id('skyandstone:herz/splitter_strom')

  // 4 Ordnung (Akt II): AE2-Gravurmaschine presst den Rohling zwischen Logik- und Kalkulationsprozessor.
  event.custom({
    type: 'ae2:inscriber', mode: 'press',
    ingredients: { top: S('ae2:logic_processor'), middle: S(R), bottom: S('ae2:calculation_processor') },
    result: ergebnis('skyandstone:splitter_ordnung')
  }).id('skyandstone:herz/splitter_ordnung')

  // 5 Leben (Akt III): Farmer's Delight Kochtopf. Productive Bees (Honigleckerli), Mystical Agriculture (Imperium),
  //   Farmer's Delight (Reiche Erde), Goldener Apfel.
  event.custom({
    type: 'farmersdelight:cooking', experience: 2.0, recipe_book_tab: 'misc',
    ingredients: [S(R), S('productivebees:honey_treat'), S('mysticalagriculture:imperium_essence'),
      S('mysticalagriculture:imperium_essence'), S('minecraft:golden_apple'), S('farmersdelight:rich_soil')],
    result: ergebnis('skyandstone:splitter_leben')
  }).id('skyandstone:herz/splitter_leben')

  // 6 Geist (Akt III), zwei gleichwertige Wege:
  //   Magie: Ars-Nouveau-Verzauberungsapparat mit Wilden-Teilen, Quellstein und Leerenessenz.
  event.custom({
    type: 'ars_nouveau:enchanting_apparatus', keepNbtOfReagent: false, sourceCost: 5000,
    reagent: S(R),
    pedestalItems: [S('ars_nouveau:wilden_horn'), S('ars_nouveau:wilden_wing'), S('ars_nouveau:wilden_spike'),
      S('ars_nouveau:source_gem_block'), S('skyandstone:leerenessenz'), S('skyandstone:leerenessenz')],
    result: ergebnis('skyandstone:splitter_geist')
  }).id('skyandstone:herz/splitter_geist_magie')
  //   Technik: Industrial-Foregoing-Auflösungskammer mit Hostile-Networks-Vorhersagen und flüssiger Essenz (Mob Crusher).
  event.custom({
    type: 'industrialforegoing:dissolution_chamber', processingTime: 400,
    input: [S(R), S('hostilenetworks:overworld_prediction'), S('hostilenetworks:overworld_prediction'),
      S('hostilenetworks:overworld_prediction'), S('hostilenetworks:nether_prediction'),
      S('hostilenetworks:nether_prediction'), S('hostilenetworks:nether_prediction'), S('skyandstone:leerenessenz')],
    inputFluid: { amount: 1000, fluid: 'industrialforegoing:essence' },
    output: ergebnis('skyandstone:splitter_geist')
  }).id('skyandstone:herz/splitter_geist_technik')

  // 7 Leere (Akt III), zwei Wege:
  //   Technik: Mekanism-Nukleosynthesizer mit Antimaterie (SPS).
  event.custom({
    type: 'mekanism:nucleosynthesizing', duration: 400, per_tick_usage: false,
    item_input: { count: 1, item: R },
    chemical_input: { amount: 100, chemical: 'mekanism:antimatter' },
    output: ergebnis('skyandstone:splitter_leere')
  }).id('skyandstone:herz/splitter_leere_technik')
  //   Magie: Ars-Imbuement-Kammer mit Drachenatem, Shulkerschale und Leerenessenz.
  event.custom({
    type: 'ars_nouveau:imbuement', source: 5000,
    input: S(R),
    pedestalItems: [S('minecraft:dragon_breath'), S('minecraft:shulker_shell'), S('skyandstone:leerenessenz')],
    output: ergebnis('skyandstone:splitter_leere')
  }).id('skyandstone:herz/splitter_leere_magie')

  // Herz der Leere: Create-Mechanische-Handwerkseinheit (5×5). Sieben Splitter, Leerenessenz, Obsidian.
  event.custom({
    type: 'create:mechanical_crafting', accept_mirrored: false, category: 'misc', show_notification: true,
    pattern: [' EAE ', 'EBOCE', 'DOOOF', 'EGOHE', ' E E '],
    key: {
      A: S('skyandstone:splitter_erde'), B: S('skyandstone:splitter_glut'), C: S('skyandstone:splitter_strom'),
      D: S('skyandstone:splitter_ordnung'), F: S('skyandstone:splitter_leben'), G: S('skyandstone:splitter_geist'),
      H: S('skyandstone:splitter_leere'), E: S('skyandstone:leerenessenz'), O: S('minecraft:obsidian')
    },
    result: ergebnis('skyandstone:herz_der_leere')
  }).id('skyandstone:herz/herz_der_leere')

  // Herzsockel: der Altar, auf dem das Herz geweckt wird.
  event.shaped('skyandstone:herzsockel', ['BTB', 'BBB', 'SSS'],
    { B: 'minecraft:stone_bricks', T: 'minecraft:enchanting_table', S: 'minecraft:smooth_stone' })
    .id('skyandstone:herz/herzsockel')
})

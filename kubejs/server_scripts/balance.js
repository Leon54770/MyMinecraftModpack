// Sky and Stone – Balance (Gemini-Prüfung 24.10.2026, von Claude umgesetzt)
// 1) Pipez: obere Upgrades brauchen Technik aus Mekanism/AE2
// 2) Mystical Agriculture: höhere Essenz-Stufen erst nach Create -> Mekanism -> AE2
//    (Ressourcen-Samen brauchen die jeweilige Stufen-Essenz, damit sind auch die Samen gesperrt)

ServerEvents.recipes(event => {
  // --- 0. Bienen-Zentrifuge: Essenz-Stufen 3-6 nur wie im Rezept der Essenz (sonst umgeht die Zentrifuge die Sperren)
  ['tertium', 'imperium', 'supremium', 'insanium'].forEach(t => {
    event.remove({ id: 'productivebees:centrifuge/mysticalagriculture/honeycomb_' + t })
  })

  // --- 1. Pipez
  event.remove({ id: 'pipez:advanced_upgrade' })
  event.shaped('pipez:advanced_upgrade', ['DCD', 'RUR', 'DCD'], {
    D: '#c:gems/diamond',
    C: 'mekanism:advanced_control_circuit',
    R: '#c:storage_blocks/redstone',
    U: 'pipez:improved_upgrade'
  }).id('skyandstone:pipez/advanced_upgrade')

  event.remove({ id: 'pipez:ultimate_upgrade' })
  event.shaped('pipez:ultimate_upgrade', ['NEN', 'PUP', 'NEN'], {
    N: '#c:ingots/netherite',
    E: 'mekanism:elite_control_circuit',
    P: 'ae2:engineering_processor',
    U: 'pipez:advanced_upgrade'
  }).id('skyandstone:pipez/ultimate_upgrade')

  // --- 2. Mystical Agriculture: Essenz-Stufen
  // Inferium -> Prudentium bleibt wie es ist (Frühspiel).

  // Tertium: nur im Create-Mixer (4 Prudentium + Messing -> 2 Tertium)
  event.remove({ id: 'mysticalagriculture:tertium_essence' })
  const p = { item: 'mysticalagriculture:prudentium_essence' }
  event.custom({
    type: 'create:mixing',
    ingredients: [p, p, p, p, { tag: 'c:ingots/brass' }],
    results: [{ id: 'mysticalagriculture:tertium_essence', count: 2 }]
  }).id('skyandstone:mixing/tertium_essence')

  // Imperium: braucht Mekanism (Infused Alloy aus dem Metallurgic Infuser)
  event.remove({ id: 'mysticalagriculture:imperium_essence' })
  event.shaped('mysticalagriculture:imperium_essence', [' T ', 'TAT', ' T '], {
    T: 'mysticalagriculture:tertium_essence',
    A: 'mekanism:alloy_infused'
  }).id('skyandstone:imperium_essence')

  // Supremium: braucht AE2 (Engineering Processor aus dem Inscriber)
  event.remove({ id: 'mysticalagriculture:supremium_essence' })
  event.shaped('mysticalagriculture:supremium_essence', [' I ', 'IPI', ' I '], {
    I: 'mysticalagriculture:imperium_essence',
    P: 'ae2:engineering_processor'
  }).id('skyandstone:supremium_essence')

  // Insanium (Stufe 6): verbindet das MA-Endgame mit dem Mekanism-Endgame (0.5.0).
  // Original: 4 Supremium + Infusionskristall -> 1. Neu: 4 Supremium + Ultimate-Schaltkreis -> 2.
  event.remove({ id: 'mysticalagradditions:insanium_essence' })
  event.shaped('2x mysticalagradditions:insanium_essence', [' S ', 'SCS', ' S '], {
    S: 'mysticalagriculture:supremium_essence',
    C: 'mekanism:ultimate_control_circuit'
  }).id('skyandstone:insanium_essence')

  // --- 3. Magie als Alternative: Ars-Nouveau-Glyphe „Crush“ kann Bruchstein -> Kies -> Sand,
  // hier fehlt nur Sand -> Staub (Ex Deorum). Damit ersetzt ein Zauberturm den Hammer komplett.
  event.custom({
    type: 'ars_nouveau:crush',
    input: { item: 'minecraft:sand' },
    output: [{ chance: 1.0, maxRange: 1, stack: { count: 1, id: 'exdeorum:dust' } }]
  }).id('skyandstone:crush/sand_to_dust')

  // --- 3b. Essenz-Verdopplung verhindern (0.7.0): Die Rückbau-Rezepte von MA geben 4 Essenzen der Stufe darunter.
  // Mit den Rezepten oben (4 Prudentium + Messing -> 2 Tertium, 4 Supremium + Schaltkreis -> 2 Insanium)
  // wird daraus eine Endlosschleife: 4 Prudentium -> 2 Tertium -> 8 Prudentium. Die übrigen Rückbauten verlieren
  // Material und bleiben erhalten.
  event.remove({ id: 'mysticalagriculture:tertium_essence_uncraft' })
  event.remove({ id: 'mysticalagradditions:insanium_essence_uncraft' })

  // --- 4. Erzmagier-Zauberbuch ohne Totem (Nachtschicht 0.6.3): In der Leere gibt es keine Plünderer,
  // das Totem käme nur per Glück aus der Sternkiste. Der Magie-Weg zum Finale (z_weg) soll planbar sein.
  // Ersatz: Diamantblock. Netherstern (Wither) und Wilden-Tribut (Chimera) bleiben die echten Hürden.
  event.remove({ id: 'ars_nouveau:archmage_book_upgrade' })
  event.custom({
    type: 'ars_nouveau:book_upgrade',
    category: 'misc',
    ingredients: [
      { item: 'ars_nouveau:apprentice_spell_book' },
      { tag: 'c:ender_pearls' }, { tag: 'c:ender_pearls' }, { tag: 'c:ender_pearls' },
      { tag: 'c:gems/emerald' }, { tag: 'c:gems/emerald' },
      { item: 'minecraft:diamond_block' },
      { item: 'minecraft:nether_star' },
      { item: 'ars_nouveau:wilden_tribute' }
    ],
    result: { count: 1, id: 'ars_nouveau:archmage_spell_book' }
  }).id('skyandstone:archmage_book_upgrade')

  console.info('[Sky and Stone] Balance-Rezepte geladen (Pipez, Mystical Agriculture, Insanium, Ars-Crush, Erzmagier, ohne Essenz-Verdopplung)')
})

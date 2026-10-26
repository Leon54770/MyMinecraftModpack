// Sky and Stone – Lücken, die es nur in einer Leere-Welt gibt

ServerEvents.recipes(event => {
  // Keine Strongholds -> Endportalrahmen herstellbar (12 Stück für ein Portal)
  event.shaped('minecraft:end_portal_frame', ['OEO', 'SSS'], {
    O: 'minecraft:obsidian', E: 'minecraft:ender_eye', S: 'minecraft:end_stone'
  }).id('skyandstone:end_portal_frame')

  // Messing braucht einen Lohenbrenner, Lohen gibt es erst im Nether ->
  // Brenner auch aus Lohenpulver (Staub-Sieb), damit Create nicht hinter dem Nether hängt
  event.shapeless('create:blaze_burner', ['create:empty_blaze_burner', 'minecraft:blaze_powder', 'minecraft:blaze_powder',
    'minecraft:blaze_powder', 'minecraft:blaze_powder']).id('skyandstone:blaze_burner_from_powder')


  // 0.21.0 Lücke: Certus-, Osmium- und Zink-Essenz haben im Datensatz nur einen Zirkel (Seed-Reprocessor braucht Certus-Seeds,
  // Seeds brauchen Certus-Essenz, seedCraftingRecipes = false). Beleg: IMPLEMENTATION_LOG Lauf 5.
  // Fallback über den Create-Mischer: 4 Certus-Quarz plus 1 Inferiumessenz ergeben 1 Certus-Essenz.
  // Gleiches Muster für Osmium und Zink (Seed-Reprocessor braucht Seeds, Seeds brauchen die Essenz).
  // Belege: Lauf 5 in IMPLEMENTATION_LOG. Jeweils 4 Metall plus 1 Inferiumessenz ergibt 1 Essenz.
  const fallbacks = [
    ['ae2:certus_quartz_crystal', 'mysticalagriculture:certus_quartz_essence', 'certus_quartz'],
    ['mekanism:ingot_osmium', 'mysticalagriculture:osmium_essence', 'osmium'],
    ['create:zinc_ingot', 'mysticalagriculture:zinc_essence', 'zinc']
  ]
  fallbacks.forEach(f => {
    const m = { item: f[0] }
    event.custom({
      type: 'create:mixing',
      ingredients: [m, m, m, m, { item: 'mysticalagriculture:inferium_essence' }],
      results: [{ id: f[1], count: 1 }]
    }).id('skyandstone:mixing/' + f[2] + '_essence')
  })

  // 0.8.0: Aufgabenbildschirm mit eigenem Rezept (Strom-Prüfung). FTB Quests hat ein eigenes Rezept, das ersetzen wir
  event.remove({ id: 'ftbquests:screen_1' })
  event.shaped('ftbquests:screen_1', ['IGI', 'GRG', 'IGI'], {
    I: '#c:ingots/iron', G: '#c:glass_blocks', R: 'minecraft:redstone'
  }).id('skyandstone:task_screen')
})

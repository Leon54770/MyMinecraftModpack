// Sky and Stone – eigene Item-Gruppen für Quests ("irgendein Sieb", "irgendein Holztiegel" ...)
// Werden in den Quests über FTB Filter System als item_tag(skyandstone:...) abgefragt.

ServerEvents.tags('item', event => {
  // Ex-Deorum-Siebe aus allen Holzarten (ohne Kompressions- und mechanische Siebe)
  event.add('skyandstone:sieves', /^exdeorum:(?!.*compressed)(?!mechanical)[a-z_]+_sieve$/)
  // Holztiegel für Wasser (Nether-Holz und Porzellan sind Lava-Tiegel)
  event.add('skyandstone:water_crucibles', /^exdeorum:(?!porcelain|unfired|crimson|warped|hellbark)[a-z_]+_crucible$/)
  // Botany Pots mit Trichter (alle Farben)
  event.add('skyandstone:hopper_botany_pots', /^botanypots:[a-z_]*hopper_botany_pot$/)
  // Archwood-Setzlinge aller Farben
  event.add('skyandstone:archwood_saplings', /^ars_nouveau:[a-z_]*archwood_sapling$/)
  // Macaw's: Dächer und Hängebrücken aller Holzarten
  event.add('skyandstone:roofs', /^mcwroofs:[a-z_]+_roof$/)
  event.add('skyandstone:rope_bridges', /^mcwbridges:rope_[a-z_]+_bridge$/)
  // Weiche vor dem Finale: Magie ODER Mob-Technik
  event.add('skyandstone:weg_zum_herz', ['ars_nouveau:archmage_spell_book', 'hostilenetworks:loot_fabricator'])
  // 0.7.0: z_erz „Erz ohne Sieb“ – eins der drei Systeme reicht (Felder, Laserbohrer, Erz-Bienen)
  event.add('skyandstone:erz_ohne_sieb', ['mysticalagriculture:osmium_seeds', 'industrialforegoing:ore_laser_base', 'productivebees:nether_quartz_nest'])
})

// Sky and Stone – weniger Sieb-Plackerei
// 1. Fehlende Rohstoffe der Mod-Technik ins Ex-Deorum-Sieb
// 2. Alle Ex-Deorum-Siebtabellen auch für den Create-Sifter (früh automatisierbar mit Wind/Wasserrad)
// 3. Hammer-Rezepte auch für Create-Mühlstein und Brechwalzen
// 4. Mechanisches Sieb früher baubar (Andesit-Gehäuse statt Eisenblöcke)

const MESH_TO_SIFTER = {
  'exdeorum:string_mesh': 'createsifter:string_mesh',
  'exdeorum:flint_mesh': 'createsifter:andesite_mesh',
  'exdeorum:iron_mesh': 'createsifter:zinc_mesh',
  'exdeorum:golden_mesh': 'createsifter:brass_mesh',
  'exdeorum:diamond_mesh': 'createsifter:advanced_brass_mesh',
  'exdeorum:netherite_mesh': 'createsifter:advanced_sturdy_mesh'
}

// [Eingabe, Sieb, Ergebnis, Chance]
const EXTRA_DROPS = [
  ['minecraft:dirt', 'string', 'mysticalagriculture:inferium_essence', 0.10],
  ['minecraft:dirt', 'flint', 'mysticalagriculture:inferium_essence', 0.15],
  ['minecraft:dirt', 'iron', 'mysticalagriculture:inferium_essence', 0.20],
  ['minecraft:dirt', 'diamond', 'mysticalagriculture:inferium_essence', 0.30],
  ['minecraft:gravel', 'flint', 'mysticalagriculture:prosperity_shard', 0.04],
  ['minecraft:gravel', 'iron', 'mysticalagriculture:prosperity_shard', 0.06],
  ['minecraft:gravel', 'golden', 'mysticalagriculture:prosperity_shard', 0.08],
  ['minecraft:gravel', 'diamond', 'mysticalagriculture:prosperity_shard', 0.10],
  ['minecraft:sand', 'iron', 'mekanism:fluorite_gem', 0.05],
  ['minecraft:sand', 'diamond', 'mekanism:fluorite_gem', 0.08],
  ['minecraft:gravel', 'golden', 'powah:uraninite_raw', 0.03],
  ['minecraft:gravel', 'diamond', 'powah:uraninite_raw', 0.05],
  ['minecraft:moss_block', 'string', 'minecraft:bee_spawn_egg', 0.02],
  ['minecraft:moss_block', 'iron', 'minecraft:bee_spawn_egg', 0.04],
  // Nutztiere (spawnen in der Leere kaum von selbst)
  ['minecraft:dirt', 'string', 'minecraft:cow_spawn_egg', 0.01],
  ['minecraft:dirt', 'string', 'minecraft:sheep_spawn_egg', 0.01],
  ['minecraft:dirt', 'string', 'minecraft:chicken_spawn_egg', 0.01],
  ['minecraft:dirt', 'string', 'minecraft:pig_spawn_egg', 0.01],
  // Shulker-Schalen (keine Endstädte in der Leere)
  ['exdeorum:crushed_end_stone', 'diamond', 'minecraft:shulker_shell', 0.02],
  ['exdeorum:crushed_end_stone', 'netherite', 'minecraft:shulker_shell', 0.04],
  // Wilden-Teile für Ars Nouveau (keine Archwood-Wälder in der Leere)
  ['minecraft:gravel', 'golden', 'ars_nouveau:wilden_horn', 0.03],
  ['minecraft:sand', 'golden', 'ars_nouveau:wilden_spike', 0.03],
  ['minecraft:dirt', 'golden', 'ars_nouveau:wilden_wing', 0.03]
]

// Ex-Deorum-Mengenangabe -> Liste von Create-Ergebnissen
function toResults(id, amount) {
  let expected = 1
  if (typeof amount === 'number') expected = amount
  else if (amount && amount.type === 'minecraft:constant') expected = amount.value
  else if (amount && amount.type === 'minecraft:binomial') expected = amount.n * amount.p
  else if (amount && amount.type === 'minecraft:uniform') {
    // 0.7.0: Ex Deorum 3.12 schreibt min/max (ältere Versionen min_inclusive/max_inclusive). Vorher ergab das NaN
    // und 8 Mühlstein-Rezepte (Stein, Steinziegel, Prismarin, Tropfstein) gaben gar nichts aus.
    const lo = amount.min !== undefined ? amount.min : amount.min_inclusive
    const hi = amount.max !== undefined ? amount.max : amount.max_inclusive
    expected = (lo + hi) / 2
  }
  if (!(expected > 0)) return []
  const out = []
  const whole = Math.floor(expected)
  if (whole > 0) out.push({ id: id, count: whole })
  const rest = Math.round((expected - whole) * 1000) / 1000
  if (rest > 0) out.push({ id: id, chance: rest })
  return out
}

ServerEvents.recipes(event => {
  // --- 1. Extra-Drops
  const sieveJsons = []
  EXTRA_DROPS.forEach(e => {
    const json = {
      type: 'exdeorum:sieve',
      ingredient: { item: e[0] },
      mesh: { item: 'exdeorum:' + e[1] + '_mesh' },
      result: { id: e[2], count: 1 },
      result_amount: { type: 'minecraft:binomial', n: 1, p: e[3] }
    }
    event.custom(json).id('skyandstone:sieve/' + e[2].split(':')[1] + '_' + e[0].split(':')[1] + '_' + e[1])
    sieveJsons.push(json)
  })

  // --- 2. Siebtabellen -> Create-Sifter
  event.forEachRecipe({ type: 'exdeorum:sieve' }, r => sieveJsons.push(JSON.parse(r.json.toString())))
  event.forEachRecipe({ type: 'exdeorum:compressed_sieve' }, r => sieveJsons.push(JSON.parse(r.json.toString())))

  const groups = {}
  sieveJsons.forEach(j => {
    if (j.by_hand_only) return
    const mesh = MESH_TO_SIFTER[j.mesh && j.mesh.item]
    if (!mesh) return
    // Enderperlen und Enderaugen bleiben Akt III (Endstein-Sieb wäre sonst eine frühe Abkürzung)
    if (j.result && (j.result.id === 'minecraft:ender_pearl' || j.result.id === 'minecraft:ender_eye')) return
    const key = JSON.stringify(j.ingredient) + '|' + mesh
    if (!groups[key]) groups[key] = { ingredient: j.ingredient, mesh: mesh, results: [] }
    toResults(j.result.id, j.result_amount).forEach(x => groups[key].results.push(x))
  })

  // 0.7.0: Create Sifter 2.3.0 hat kein Rezept für das Zinc Mesh (Stufe des Eisennetzes) -> wie die anderen Netze
  event.shaped('createsifter:zinc_mesh', ['SSS', 'SCS', 'SSS'], { S: 'minecraft:stick', C: '#c:ingots/zinc' })
    .id('skyandstone:zinc_mesh')

  event.remove({ type: 'createsifter:sifting' })
  let n = 0
  Object.keys(groups).forEach(k => {
    const g = groups[k]
    event.custom({
      type: 'createsifter:sifting',
      input: g.ingredient,
      mesh: { id: g.mesh, count: 1 },
      processingTime: 200,
      results: g.results
    }).id('skyandstone:sifting/' + (n++))
  })
  console.info('[Sky and Stone] Create-Sifter-Rezepte aus Ex Deorum: ' + n)

  // --- 3. Hammer -> Mühlstein (+ Brechwalzen, wenn Create dort nichts hat)
  let m = 0
  event.forEachRecipe({ type: 'exdeorum:hammer' }, r => {
    const j = JSON.parse(r.json.toString())
    const ings = Array.isArray(j.ingredient) ? j.ingredient : [j.ingredient]
    const results = toResults(j.result.id, j.result_amount)
    if (!results.length) { console.warn('[Sky and Stone] Hammer-Rezept ohne Ergebnis übersprungen: ' + (r.getId ? r.getId() : '?')); return }
    ings.forEach(ing => {
      if (!ing.item) return
      event.remove({ type: 'create:milling', input: ing.item })
      event.custom({ type: 'create:milling', ingredients: [ing], processing_time: 100, results: results })
        .id('skyandstone:milling/' + (m++))
      if (!event.containsRecipe({ type: 'create:crushing', input: ing.item })) {
        const bonus = results.concat([{ id: j.result.id, chance: 0.25 }])
        event.custom({ type: 'create:crushing', ingredients: [ing], processing_time: 100, results: bonus })
          .id('skyandstone:crushing/' + m)
      }
    })
  })
  console.info('[Sky and Stone] Mühlstein-Rezepte aus Ex-Deorum-Hammer: ' + m)

  // --- 4. Mechanisches Sieb günstiger
  event.remove({ id: 'exdeorum:mechanical_sieve' })
  event.shaped('exdeorum:mechanical_sieve', ['AGA', 'IHI', 'I I'], {
    A: 'create:andesite_casing', G: '#c:glass_blocks', H: 'minecraft:hopper', I: 'minecraft:iron_bars'
  }).id('skyandstone:mechanical_sieve')
})

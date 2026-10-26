// Sky and Stone 1.1.0 „Die sieben Splitter“: eigene Items und Blöcke der neuen Hauptstory.
// Design: _src/DESIGN-HERZ-DER-LEERE.md. Texturen erzeugt _src/texturen.py, Namen stehen in kubejs/assets/skyandstone/lang.
// Builder-API aus dem KubeJS-Jar geprüft (kubejs-neoforge-2101.7.2: ItemBuilder, BlockBuilder, ModelledBuilderBase).

const SPLITTER = ['erde', 'glut', 'strom', 'ordnung', 'leben', 'geist', 'leere']

StartupEvents.registry('item', event => {
  SPLITTER.forEach(s => {
    event.create('skyandstone:splitter_' + s).maxStackSize(16).rarity('rare').fireResistant()
  })
  event.create('skyandstone:splitter_rohling').maxStackSize(16)
  event.create('skyandstone:leerenessenz').rarity('uncommon')
  event.create('skyandstone:karte_werkstatt').unstackable().rarity('uncommon')
  event.create('skyandstone:waechterkern').unstackable().rarity('epic').fireResistant()
})

StartupEvents.registry('block', event => {
  // Das Herz: schlafend (aus den Splittern gebaut) und erwacht (nach dem Sieg über den Wächter, leuchtet, animiert)
  event.create('skyandstone:herz_der_leere')
    .stoneSoundType().hardness(25).resistance(1200).requiresTool(true)
    .lightLevel(0.3)
    .tagBlock('minecraft:mineable/pickaxe')
    .item(i => i.rarity('epic').fireResistant())
  event.create('skyandstone:herz_erwacht')
    .stoneSoundType().hardness(25).resistance(1200).requiresTool(true)
    .lightLevel(1.0)
    .tagBlock('minecraft:mineable/pickaxe')
    .item(i => i.rarity('epic').fireResistant())
  // Sockel: oben Ring, Seiten mit Runen (cube_bottom_top)
  event.create('skyandstone:herzsockel')
    .stoneSoundType().hardness(3).resistance(6).requiresTool(true)
    .tagBlock('minecraft:mineable/pickaxe')
    .parentModel('minecraft:block/cube_bottom_top')
    .textures({
      top: 'skyandstone:block/herzsockel_oben',
      bottom: 'skyandstone:block/herzsockel_unten',
      side: 'skyandstone:block/herzsockel_seite'
    })
  // Zerbrochener Sockel der vergessenen Werkstatt: nur Deko und Ziel der Beobachten-Aufgabe, gibt nichts
  event.create('skyandstone:herzsockel_zerbrochen')
    .stoneSoundType().hardness(3).resistance(6)
    .tagBlock('minecraft:mineable/pickaxe')
    .noDrops()
    .parentModel('minecraft:block/cube_bottom_top')
    .textures({
      top: 'skyandstone:block/herzsockel_zerbrochen_oben',
      bottom: 'skyandstone:block/herzsockel_unten',
      side: 'skyandstone:block/herzsockel_zerbrochen_seite'
    })
})

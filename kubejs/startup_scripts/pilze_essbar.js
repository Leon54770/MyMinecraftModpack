// Sky and Stone, TODO 9.4: Rohe Pilze sind in 1.21.1 kein Essen. Ohne Nährwert löst
// ItemEvents.foodEaten in pehkui_pilze.js nie aus (und die Fortschritte "Riesenpilz"/"Pilzgröße").
// Lösung (Entscheidung Leon, 26.10.2026): Pilze bekommen einen kleinen Nährwert und sind immer essbar.
// API aus dem Jar geprüft (kubejs-neoforge-2101.7.2: ItemModifications.kjs$modifyFood, FoodBuilder).
// Platzieren auf einem Block geht weiter vor (BlockItem.useOn), gegessen wird nur in die Luft.
ItemEvents.modification(event => {
  ;['minecraft:red_mushroom', 'minecraft:brown_mushroom'].forEach(id => {
    event.modify(id, item => {
      item.modifyFood(food => {
        food.nutrition(1)
        food.saturation(0.1)
        food.alwaysEdible()
      })
    })
  })
})

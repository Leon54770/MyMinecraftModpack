// NUR TESTSERVER (Meilenstein 1, Rezept-Simulation). Nicht in den Pack-Ordner kopieren.
// Liest den Rezeptmanager nach dem Laden aus und schreibt kubejs/dev_recipes.json.
// Eingaben laufen über den KubeJS-Wrapper Ingredient.of(...): Rhino findet auf Java-Objekten
// vom Typ Ingredient keine Methoden (auch nicht getClass), der Wrapper rechnet auf Java-Seite.
let DevRegs = Java.loadClass('net.minecraft.core.registries.BuiltInRegistries')

ServerEvents.loaded(event => {
  let server = event.server
  let access = server.registryAccess()
  let recipes = []
  let empty = 0
  let noOutput = 0
  let errors = 0

  server.recipeManager.getRecipes().forEach(holder => {
    let rec = holder.value()
    let entry = {
      id: String(holder.id()),
      type: String(DevRegs.RECIPE_TYPE.getKey(rec.getType())),
      ins: [],
      out: '',
      count: 0,
    }
    try {
      let ings = rec.getIngredients()
      for (let i = 0; i < ings.size(); i++) {
        let ids = []
        Ingredient.of(ings.get(i)).itemIds.forEach(id => ids.push(String(id)))
        if (ids.length == 0) empty++
        entry.ins.push(ids)
      }
    } catch (e) {
      entry.insError = String(e)
      errors++
    }
    try {
      let res = rec.getResultItem(access)
      if (res.isEmpty()) {
        noOutput++
      } else {
        entry.out = String(DevRegs.ITEM.getKey(res.getItem()))
        entry.count = res.getCount()
      }
    } catch (e) {
      entry.outError = String(e)
      errors++
    }
    recipes.push(entry)
  })

  JsonIO.write('kubejs/dev_recipes.json', { count: recipes.length, recipes: recipes })
  console.info('[DEV] Rezepte: ' + recipes.length + ', leere Eingaben: ' + empty + ', ohne Item-Ausgabe: ' + noOutput + ', Fehler: ' + errors)
})

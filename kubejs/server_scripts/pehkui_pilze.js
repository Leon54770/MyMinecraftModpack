// Sky and Stone, Sprint 9 (Pehkui-Gimmick): Pilze verändern die Spielergröße.
// Roter Pilz: klein (0,5). Brauner Pilz: groß (2,0). Chorusfrucht: zurück auf normal (1,0).
// Befehle laufen über den Server (Konsolenrechte) mit execute as, wie beim Handbuch.
// Syntax des Befehls "scale" aus der Pehkui-Befehlsklasse übernommen. Laufzeit im Spiel NICHT GETESTET.
const PILZ_GROESSE = {
  'minecraft:red_mushroom': { wert: '0.5', text: 'Du schrumpfst auf Pilzgröße.' },
  'minecraft:brown_mushroom': { wert: '2.0', text: 'Du wächst wie ein Riesenpilz.' },
  'minecraft:chorus_fruit': { wert: '1.0', text: 'Du bist wieder normal groß.' }
}

Object.keys(PILZ_GROESSE).forEach(item => {
  ItemEvents.foodEaten(item, event => {
    const p = event.player
    const eintrag = PILZ_GROESSE[item]
    Utils.server.runCommandSilent('execute as ' + p.username + ' run scale set base ' + eintrag.wert + ' @s')
    p.tell(Text.gray(eintrag.text))
    Utils.server.runCommandSilent('execute as ' + p.username + ' run title @s actionbar {"text":"' + eintrag.text + '","color":"gray"}')
  })
})

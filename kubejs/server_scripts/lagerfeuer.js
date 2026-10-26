// Sky and Stone, Sprint 8.1: Lagerfeuer-Rast. Einmal pro Spieler, Titel beim ersten Rechtsklick auf ein Lagerfeuer.
// Befehle laufen über den Server (Konsolenrechte), damit title auch ohne OP funktioniert.
// Laufzeit-Test im Spiel steht aus (NICHT GETESTET).
BlockEvents.rightClicked('minecraft:campfire', event => {
  const p = event.player
  if (p.persistentData.getBoolean('skyandstone_gerastet')) return
  p.persistentData.putBoolean('skyandstone_gerastet', true)
  const wer = 'execute as ' + p.username + ' run '
  Utils.server.runCommandSilent(wer + 'title @s times 10 60 20')
  Utils.server.runCommandSilent(wer + 'title @s title {"text":"Die Erbauer rasten","color":"gold","bold":true}')
  Utils.server.runCommandSilent(wer + 'title @s subtitle {"text":"Das Feuer brennt, solange du wartest.","color":"gray"}')
  // 9.5: ohne "at @s" entstand der Rauch am Welt-Spawn statt am Spieler
  Utils.server.runCommandSilent('execute as ' + p.username + ' at ' + p.username + ' run particle minecraft:campfire_cosy_smoke ~ ~1 ~ 0.3 0.3 0.3 0.01 20 force @s')
})

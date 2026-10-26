// Sky and Stone 0.9.0 (0.21.0: Handbuch-Buch) – Begrüßung beim ersten Betreten einer Welt (einmal pro Spieler, kein Tick-Skript)
PlayerEvents.loggedIn(event => {
  const p = event.player
  if (p.persistentData.getBoolean('skyandstone_begruesst')) return
  p.persistentData.putBoolean('skyandstone_begruesst', true)
  Utils.server.runCommandSilent('execute as ' + p.username + ' run function skyandstone:handbuch_buch')
  p.tell(Text.gold('Willkommen in Sky and Stone.'))
  p.tell(Text.gray('Unter dir die Leere, unter der Leere ein Herz, das nicht mehr schlägt.'))
  p.tell(Text.white('Das Questbuch in deinem Inventar führt dich. Rechtsklick zum Öffnen, Belohnungen selbst abholen.'))
  p.tell(Text.gray('Keine Insel, sondern eine normale Welt? Dann beim Erstellen den Welttyp „Skyblock“ wählen.'))
})

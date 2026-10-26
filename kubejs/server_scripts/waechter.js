// Sky and Stone, Sprint 6 (6.7): Wächter-Spruch nach dem Tod (beim Wiederbeleben). Eine Zufallszeile, nur an den Spieler, kein Tick-Skript.
// Laufzeit-Test im Spiel steht aus (NICHT GETESTET).
const WAECHTER_TOD = [
  'Der Wächter seufzt. Die Leere vergisst nichts, aber sie verzeiht.',
  'Du bist gefallen. Die Erbauer haben schlimmere Stürze überlebt.',
  'Die Insel hat dich zurückgeholt. Wieder einmal.',
  'Der Wächter notiert: Tod, Ursache unbekannt. Weitermachen.',
  'Kein Grund zur Sorge. Die Leere ist geduldig.',
  'Der Wächter fragt nicht, wie es passiert ist. Er fragt, ob du es wieder tust.',
  'Ein Stein fällt schneller als eine Ausrede. Probier es mit Vorsicht.',
  'Die Erbauer haben oft dasselbe gedacht. Sie sind trotzdem zurückgekehrt.'
]

PlayerEvents.respawned(event => {
  const zeile = WAECHTER_TOD[Math.floor(Math.random() * WAECHTER_TOD.length)]
  event.player.tell(Text.gray(zeile))
})

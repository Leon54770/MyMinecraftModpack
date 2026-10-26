// Sky and Stone 1.1.0 „Die sieben Splitter“: Interaktionen der neuen Hauptstory (Design: _src/DESIGN-HERZ-DER-LEERE.md).
//  1. Karte der Werkstatt: Rechtsklick in der Oberwelt setzt die vergessene Werkstatt 80 Blöcke in Blickrichtung.
//  2. Herz der Leere auf einem Herzsockel + Netherstern: ruft den letzten Wächter (function skyandstone:waechter/beschwoeren).
//  3. Erwachtes Herz: einmal pro Minecraft-Tag ein Herzschlag (Eile II, Regeneration, Glück für Spieler in der Nähe).
// Befehle laufen über den Server (wie handbuch/lagerfeuer), deshalb ohne OP-Rechte des Spielers.
// Nur Spieler/Block/ItemStack anfassen, keine Item-/Entity-Unterklassen (Rhino-Reflexion lädt sonst Client-Klassen).

const WERKSTATT_ABSTAND = 80   // Blöcke; bleibt in der Sichtweite (Chunks geladen), sonst geht /place template nicht
const WERKSTATT_HOEHER = 10
// Struktur werkstatt.nbt: 13×14×13, Ursprung (−6, −5, −6) relativ zur Mitte (_src/werkstatt.py)
const W_DX = -6, W_DY = -5, W_DZ = -6, W_GX = 13, W_GY = 14, W_GZ = 13

const istHaupthand = event => String(event.hand) === 'MAIN_HAND'
const ScoreHolder = Java.loadClass('net.minecraft.world.scores.ScoreHolder')

// Läuft der Kampf schon? Liest #aktiv aus dem Scoreboard sns_waechter (gesetzt von den Wächter-Funktionen).
// runCommandSilent gibt in KubeJS 2101.7.2 kein Ergebnis zurück (void, im Jar geprüft), deshalb direkt lesen.
function waechterAktiv(server) {
  try {
    const sb = server.scoreboard
    const obj = sb.getObjective('sns_waechter')
    if (!obj) return false
    const info = sb.getPlayerScoreInfo(ScoreHolder.forNameOnly('#aktiv'), obj)
    return info != null && Number(info.value()) === 1
  } catch (e) {
    console.warn('Sky and Stone: Wächter-Status nicht lesbar: ' + e)
    return false
  }
}

// Ist das Feld für die Werkstatt frei (nur Luft)? Prüft jeden Block, lädt dabei die Chunks.
function feldFrei(level, x1, y1, z1) {
  for (let x = x1; x < x1 + W_GX; x++)
    for (let y = y1; y < y1 + W_GY; y++)
      for (let z = z1; z < z1 + W_GZ; z++)
        if (String(level.getBlock(x, y, z).id) !== 'minecraft:air') return false
  return true
}
const grau = t => Text.gray(t)

ItemEvents.rightClicked('skyandstone:karte_werkstatt', event => {
  const p = event.player
  if (String(event.level.dimension) !== 'minecraft:overworld') {
    p.tell(grau('Die Karte zeigt eine Insel der Oberwelt. Hier ist sie nutzlos.'))
    return
  }
  const yaw = p.yRot * Math.PI / 180
  const mx = Math.floor(p.x - Math.sin(yaw) * WERKSTATT_ABSTAND)
  const mz = Math.floor(p.z + Math.cos(yaw) * WERKSTATT_ABSTAND)
  const my = Math.min(Math.floor(p.y) + WERKSTATT_HOEHER, 280)
  const x1 = mx + W_DX, y1 = my + W_DY, z1 = mz + W_DZ
  if (!feldFrei(event.level, x1, y1, z1)) {
    p.tell(grau('Dort ist kein Platz für die Werkstatt, etwas ist im Weg. Dreh dich in eine freie Richtung.'))
    return
  }
  event.server.runCommandSilent(`place template skyandstone:werkstatt ${x1} ${y1} ${z1}`)
  event.server.runCommandSilent(`execute positioned ${mx} ${my + 1} ${mz} run playsound minecraft:block.beacon.activate block @a[distance=..128] ~ ~ ~ 2 0.6`)
  if (!p.isCreative()) event.item.shrink(1)
  p.tell(Text.lightPurple('Die Karte zerfällt. Vor dir taucht eine Insel aus der Leere auf.'))
  p.tell(grau(`Die vergessene Werkstatt liegt bei ${mx} ${my} ${mz}, etwa ${WERKSTATT_ABSTAND} Blöcke in Blickrichtung.`))
  event.cancel()
})

BlockEvents.rightClicked('skyandstone:herz_der_leere', event => {
  if (!istHaupthand(event)) return
  const p = event.player, b = event.block
  const item = String(event.item.id)
  if (item !== 'minecraft:nether_star') {
    p.tell(grau('Das Herz schläft. Ein Netherstern könnte es wecken.'))
    return
  }
  if (String(b.down.id) !== 'skyandstone:herzsockel') {
    p.tell(grau('Das Herz braucht einen Herzsockel unter sich, bevor es erwachen kann.'))
    return
  }
  if (String(event.level.dimension) !== 'minecraft:overworld') {
    p.tell(grau('Das Herz gehört unter die Inseln der Oberwelt.'))
    return
  }
  if (waechterAktiv(event.server)) {
    p.tell(grau('Der Wächter ist schon gerufen.'))
    return
  }
  if (!p.isCreative()) event.item.shrink(1)
  event.server.runCommandSilent(`execute in minecraft:overworld positioned ${b.x} ${b.y} ${b.z} run function skyandstone:waechter/beschwoeren`)
  event.cancel()
})

BlockEvents.rightClicked('skyandstone:herz_erwacht', event => {
  if (!istHaupthand(event)) return
  const p = event.player, b = event.block
  const tag = Math.floor(Number(event.level.dayTime) / 24000)
  const daten = p.persistentData
  if (daten.contains('sns_herzschlag') && daten.getLong('sns_herzschlag') >= tag) {
    p.tell(grau('Das Herz ruht. Morgen schlägt es wieder.'))
    return
  }
  daten.putLong('sns_herzschlag', tag)
  const bei = `execute in ${event.level.dimension} positioned ${b.x} ${b.y} ${b.z} run`
  event.server.runCommandSilent(`${bei} effect give @a[distance=..16] minecraft:haste 600 1`)
  event.server.runCommandSilent(`${bei} effect give @a[distance=..16] minecraft:regeneration 600 0`)
  event.server.runCommandSilent(`${bei} effect give @a[distance=..16] minecraft:luck 600 0`)
  event.server.runCommandSilent(`${bei} playsound minecraft:block.beacon.power_select block @a[distance=..16] ~ ~ ~ 1 0.6`)
  event.server.runCommandSilent(`${bei} particle minecraft:heart ~ ~1.2 ~ 0.6 0.4 0.6 0 12 force`)
  event.server.runCommandSilent(`advancement grant ${p.username} only skyandstone:erster_herzschlag`)
  p.tell(Text.lightPurple('Das Herz schlägt. Seine Kraft fließt in alle, die bei ihm stehen.'))
  event.cancel()
})

# Läuft jeden Tick, solange #aktiv sns_waechter = 1 (aus tick.mcfunction).
execute store result bossbar skyandstone:waechter value run data get entity @e[tag=sns_waechter,limit=1] Health
execute store result score #hp sns_waechter run data get entity @e[tag=sns_waechter,limit=1] Health
execute at @e[tag=sns_herzmarker,limit=1] run bossbar set skyandstone:waechter players @a[distance=..48]
# Fällt der Wächter von der Insel (mehr als 32 Blöcke vom Herz), holt ihn das Herz zurück
execute as @e[tag=sns_waechter] at @s unless entity @e[tag=sns_herzmarker,distance=..32] at @e[tag=sns_herzmarker,limit=1,sort=nearest] run tp @s ~3 ~1 ~
execute if score #phase sns_waechter matches 0 if score #hp sns_waechter matches 1..266 run function skyandstone:waechter/phase1
execute if score #phase sns_waechter matches 1 if score #hp sns_waechter matches 1..133 run function skyandstone:waechter/phase2
# Wächter weg, Herz-Marker geladen: nach 3 s Abbruch (z. B. in Lava gestorben, kein Spieler-Kill → kein Sieg)
execute if entity @e[tag=sns_waechter] run scoreboard players set #fehlt sns_waechter 0
execute unless entity @e[tag=sns_waechter] if entity @e[tag=sns_herzmarker] run scoreboard players add #fehlt sns_waechter 1
execute if score #fehlt sns_waechter matches 60.. run function skyandstone:waechter/abbruch

# Ruft den letzten Wächter. Aufruf: execute positioned <Herz-Block> run function skyandstone:waechter/beschwoeren
# (herz_ritual.js, nach Netherstern auf dem Herz der Leere über einem Herzsockel)
summon minecraft:marker ~ ~ ~ {Tags:["sns_herzmarker"]}
summon minecraft:wither_skeleton ~3 ~1 ~ {Tags:["sns_waechter"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:'{"text": "Der letzte Wächter", "color": "dark_purple", "bold": true}',Health:400.0f,attributes:[{id:"minecraft:generic.max_health",base:400.0d},{id:"minecraft:generic.attack_damage",base:12.0d},{id:"minecraft:generic.knockback_resistance",base:0.9d},{id:"minecraft:generic.follow_range",base:48.0d},{id:"minecraft:generic.armor",base:10.0d}],HandItems:[{id:"minecraft:netherite_sword",count:1},{}],HandDropChances:[0.0f,0.0f],ArmorItems:[{},{},{},{id:"minecraft:netherite_helmet",count:1}],ArmorDropChances:[0.0f,0.0f,0.0f,0.0f]}
scale set pehkui:base 2.5 @e[tag=sns_waechter,distance=..10]
bossbar add skyandstone:waechter {"text": "Der letzte Wächter", "color": "dark_purple", "bold": true}
bossbar set skyandstone:waechter color purple
bossbar set skyandstone:waechter style notched_10
bossbar set skyandstone:waechter max 400
bossbar set skyandstone:waechter players @a[distance=..48]
scoreboard players set #phase sns_waechter 0
scoreboard players set #fehlt sns_waechter 0
scoreboard players set #aktiv sns_waechter 1
playsound minecraft:entity.wither.spawn hostile @a[distance=..64] ~ ~ ~ 1 0.8
particle minecraft:reverse_portal ~ ~1 ~ 1 1 1 0.5 300 force
title @a[distance=..64] times 10 80 30
title @a[distance=..64] title {"text": "Der letzte Wächter", "color": "dark_purple", "bold": true}
title @a[distance=..64] subtitle {"text": "„Zeig mir, dass du es wert bist.“", "color": "gray"}

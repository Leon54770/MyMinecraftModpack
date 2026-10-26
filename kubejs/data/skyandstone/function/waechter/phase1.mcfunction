# Zwei Drittel Leben: Leerenschatten
scoreboard players set #phase sns_waechter 1
execute at @e[tag=sns_waechter,limit=1] run summon minecraft:vex ~1 ~3 ~0 {Tags:["sns_schatten"],LifeTicks:600,CustomName:'{"text": "Leerenschatten", "color": "dark_gray"}'}
execute at @e[tag=sns_waechter,limit=1] run summon minecraft:vex ~-1 ~3 ~1 {Tags:["sns_schatten"],LifeTicks:600,CustomName:'{"text": "Leerenschatten", "color": "dark_gray"}'}
execute at @e[tag=sns_waechter,limit=1] run summon minecraft:vex ~0 ~3 ~-1 {Tags:["sns_schatten"],LifeTicks:600,CustomName:'{"text": "Leerenschatten", "color": "dark_gray"}'}
execute at @e[tag=sns_waechter,limit=1] run playsound minecraft:entity.evoker.prepare_summon hostile @a[distance=..48] ~ ~ ~ 1 0.6
execute at @e[tag=sns_herzmarker,limit=1] run title @a[distance=..48] actionbar {"text": "Der Wächter ruft die Schatten.", "color": "dark_purple"}

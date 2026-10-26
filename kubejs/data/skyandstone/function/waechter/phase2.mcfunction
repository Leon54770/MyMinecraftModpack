# Ein Drittel Leben: Zorn
scoreboard players set #phase sns_waechter 2
effect give @e[tag=sns_waechter] minecraft:speed 600 0 true
effect give @e[tag=sns_waechter] minecraft:strength 600 0 true
execute at @e[tag=sns_waechter,limit=1] run summon minecraft:vex ~2 ~3 ~0 {Tags:["sns_schatten"],LifeTicks:600,CustomName:'{"text": "Leerenschatten", "color": "dark_gray"}'}
execute at @e[tag=sns_waechter,limit=1] run summon minecraft:vex ~-2 ~3 ~0 {Tags:["sns_schatten"],LifeTicks:600,CustomName:'{"text": "Leerenschatten", "color": "dark_gray"}'}
execute at @e[tag=sns_herzmarker,limit=1] run effect give @a[distance=..32] minecraft:darkness 6 0
execute at @e[tag=sns_waechter,limit=1] run playsound minecraft:entity.warden.roar hostile @a[distance=..48] ~ ~ ~ 1 0.7
execute at @e[tag=sns_herzmarker,limit=1] run title @a[distance=..48] actionbar {"text": "Der Wächter wird wütend.", "color": "red"}

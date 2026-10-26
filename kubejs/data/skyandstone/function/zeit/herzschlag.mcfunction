# Herzschlag der Leere (einmal pro Tag)
scoreboard players operation #hb_day sky_timer = #day sky_timer
title @a times 10 60 20
title @a title {"text":"Das Herz schlägt","color":"dark_purple","bold":true}
title @a subtitle {"text":"Irgendwo unter dir pulsiert die Energie der Leere.","color":"gray"}
execute as @a at @s run playsound minecraft:block.beacon.ambient master @s ~ ~ ~ 0.6 0.5
execute as @a at @s run particle minecraft:soul ~ ~1 ~ 1 0.5 1 0.01 30 force @s

# Das Herz der Leere schlägt wieder (nach dem Sieg über den Wächter)
title @s times 10 80 30
title @s title {"text": "Das Herz schlägt", "color": "light_purple", "bold": true}
title @s subtitle {"text": "Unter allen Inseln pocht es wieder. Die Leere atmet ruhig.", "color": "gray"}
playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 0.6
playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1
particle minecraft:end_rod ~ ~2 ~ 1 1 1 0.1 120 force @s
summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:30,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;11953407,16737279],fade_colors:[I;16777215],has_trail:true,has_twinkle:true}]}}}}

# Sieg: läuft als der Spieler, der den Wächter besiegt hat (Advancement skyandstone:waechter_besiegt)
execute at @e[tag=sns_herzmarker,limit=1,sort=nearest] run setblock ~ ~ ~ skyandstone:herz_erwacht
execute at @e[tag=sns_herzmarker,limit=1,sort=nearest] run advancement grant @a[distance=..64] only skyandstone:herz_erwacht
execute at @e[tag=sns_herzmarker,limit=1,sort=nearest] as @a[distance=..64] at @s run function skyandstone:feier/herz_erwacht
give @s skyandstone:waechterkern
kill @e[tag=sns_schatten]
kill @e[tag=sns_herzmarker,limit=1,sort=nearest]
bossbar remove skyandstone:waechter
scoreboard players set #aktiv sns_waechter 0
weather clear 6000

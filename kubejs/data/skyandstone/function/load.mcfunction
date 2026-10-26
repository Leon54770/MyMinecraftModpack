# Sky and Stone: Zeit-Basis (Herzschlag, Sturm). Wird beim Laden des Datapacks ausgeführt.
scoreboard objectives add sky_timer dummy
execute unless score #tick sky_timer matches -2147483648.. run scoreboard players set #tick sky_timer 0
execute unless score #storm_cd sky_timer matches -2147483648.. run scoreboard players set #storm_cd sky_timer 3
# 1.1.0: Der letzte Wächter
scoreboard objectives add sns_waechter dummy

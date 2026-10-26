# Läuft jeden Tick. Die eigentliche Arbeit passiert alle 200 Ticks (10 Sekunden) in slow.
scoreboard players add #tick sky_timer 1
execute if score #tick sky_timer matches 200.. run function skyandstone:zeit/slow
# 1.1.0: Der letzte Wächter
execute if score #aktiv sns_waechter matches 1 run function skyandstone:waechter/tick

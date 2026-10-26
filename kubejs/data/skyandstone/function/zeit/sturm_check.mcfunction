# Einmal am Tag: Countdown bis zum nächsten Regen der Leere
scoreboard players operation #sturm_day sky_timer = #day sky_timer
scoreboard players remove #storm_cd sky_timer 1
execute if score #storm_cd sky_timer matches ..0 run function skyandstone:zeit/sturm

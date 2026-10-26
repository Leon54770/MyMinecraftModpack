# Alle 10 Sekunden: Tageszeit und Tag lesen, dann Herzschlag und Sturm prüfen.
scoreboard players set #tick sky_timer 0
execute store result score #daytime sky_timer run time query daytime
execute store result score #day sky_timer run time query day
# Herzschlag: einmal am Tag zur Dämmerung
execute if score #daytime sky_timer matches 12000..12600 unless score #hb_day sky_timer = #day sky_timer run function skyandstone:zeit/herzschlag
# Sturm: am Morgen prüfen, alle 3 Tage
execute if score #daytime sky_timer matches 0..600 unless score #sturm_day sky_timer = #day sky_timer run function skyandstone:zeit/sturm_check

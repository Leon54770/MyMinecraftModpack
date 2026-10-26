# Kampf ohne Sieg beendet: aufräumen, Herz bleibt schlafend, ein neuer Netherstern ruft ihn wieder
execute at @e[tag=sns_herzmarker,limit=1] run tellraw @a[distance=..64] {"text": "Der Wächter ist in der Leere verschwunden. Das Herz wartet auf einen neuen Netherstern.", "color": "gray"}
kill @e[tag=sns_schatten]
kill @e[tag=sns_herzmarker]
bossbar remove skyandstone:waechter
scoreboard players set #aktiv sns_waechter 0
scoreboard players set #fehlt sns_waechter 0

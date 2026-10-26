"""Sky and Stone 1.1.0 „Die sieben Splitter“: Datapack-Teil (Advancements, Feiern, Bosskampf) aus einer Quelle.

Aufruf (aus dem Pack-Ordner): python -I -X utf8 _src/herz_daten.py
Schreibt nach kubejs/data/skyandstone/:
  advancement/splitter_*.json, herz_gebaut.json, waechter_besiegt.json, herz_erwacht.json, erster_herzschlag.json
  function/feier/splitter_*.mcfunction, feier/herz_erwacht.mcfunction
  function/waechter/{beschwoeren,tick,phase1,phase2,sieg}.mcfunction
und ergänzt load/tick um den Wächter. Design: _src/DESIGN-HERZ-DER-LEERE.md.
"""
import json
import os

PACK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DP = os.path.join(PACK, 'kubejs', 'data', 'skyandstone')

# (Schlüssel, Titel, Beschreibung, Farbe, Vorgänger-Advancement)
SPLITTER = [
    ('erde', 'Splitter der Erde', 'Boden, Sieb und Messing im Mixer vereint. Der erste von sieben.', 'dark_green', 'skyandstone:messing'),
    ('glut', 'Splitter der Glut', 'Lohenfeuer, überhitzt bis der Splitter glüht.', 'gold', 'skyandstone:splitter_erde'),
    ('strom', 'Splitter des Stroms', 'Ein halbe Million FE, gefangen in Glas.', 'aqua', 'skyandstone:splitter_erde'),
    ('ordnung', 'Splitter der Ordnung', 'Zwischen zwei Prozessoren gepresst: ein Gedanke aus Kristall.', 'light_purple', 'skyandstone:splitter_erde'),
    ('leben', 'Splitter des Lebens', 'Honig, Essenz und ein goldener Apfel. Er fühlt sich warm an.', 'green', 'skyandstone:splitter_erde'),
    ('geist', 'Splitter des Geistes', 'Magie oder Maschine, der Geist ist derselbe.', 'white', 'skyandstone:splitter_erde'),
    ('leere', 'Splitter der Leere', 'Er wiegt nichts. Er wiegt alles.', 'dark_purple', 'skyandstone:splitter_erde'),
]
MARKER, BOSS, SCHATTEN, BAR = 'sns_herzmarker', 'sns_waechter', 'sns_schatten', 'skyandstone:waechter'


def schreibe(rel, text):
    p = os.path.join(DP, *rel.split('/'))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text if text.endswith('\n') else text + '\n')


def adv(icon, titel, text, parent, kriterium, belohnung=None, frame='goal', ansagen=True):
    d = {'display': {'icon': {'id': icon}, 'title': titel, 'description': text, 'frame': frame,
                     'show_toast': True, 'announce_to_chat': ansagen, 'hidden': False},
         'parent': parent, 'criteria': {'c': kriterium}, 'requirements': [['c']]}
    if belohnung:
        d['rewards'] = {'function': belohnung}
    return json.dumps(d, ensure_ascii=False, indent=2)


def hat_item(item):
    return {'trigger': 'minecraft:inventory_changed', 'conditions': {'items': [{'items': item}]}}


def titel(t, unter, farbe, ziel='@s'):
    return '\n'.join([
        f'title {ziel} times 10 80 30',
        f'title {ziel} title ' + json.dumps({'text': t, 'color': farbe, 'bold': True}, ensure_ascii=False),
        f'title {ziel} subtitle ' + json.dumps({'text': unter, 'color': 'gray'}, ensure_ascii=False),
    ])


def main():
    # ---- Splitter: Advancement + Feier ----
    for k, t, text, farbe, parent in SPLITTER:
        schreibe(f'advancement/splitter_{k}.json',
                 adv(f'skyandstone:splitter_{k}', t, text, parent, hat_item(f'skyandstone:splitter_{k}'),
                     f'skyandstone:feier/splitter_{k}'))
        schreibe(f'function/feier/splitter_{k}.mcfunction', '\n'.join([
            f'# Erster {t} (Advancement skyandstone:splitter_{k})',
            titel(t, 'Das Herz der Leere zuckt. Ein Splitter mehr.', farbe),
            'playsound minecraft:block.amethyst_block.resonate player @s ~ ~ ~ 1 0.7',
            'playsound minecraft:block.beacon.power_select player @s ~ ~ ~ 0.6 1.4',
            'particle minecraft:end_rod ~ ~1 ~ 0.4 0.8 0.4 0.05 40 force @s']))
    schreibe('advancement/herz_gebaut.json',
             adv('skyandstone:herz_der_leere', 'Sieben in einem', 'Das Herz der Leere ist ganz. Es schläft noch.',
                 'skyandstone:splitter_erde', hat_item('skyandstone:herz_der_leere'), frame='challenge'))
    schreibe('advancement/waechter_besiegt.json', adv(
        'skyandstone:waechterkern', 'Der letzte Wächter', 'Er hat dich geprüft. Du hast bestanden.', 'skyandstone:herz_gebaut',
        {'trigger': 'minecraft:player_killed_entity', 'conditions': {'entity': [
            {'condition': 'minecraft:entity_properties', 'entity': 'this', 'predicate': {'nbt': '{Tags:["%s"]}' % BOSS}}]}},
        'skyandstone:waechter/sieg', frame='challenge'))
    schreibe('advancement/herz_erwacht.json', adv(
        'skyandstone:herz_erwacht', 'Das Herz schlägt', 'Unter allen Inseln schlägt wieder etwas.', 'skyandstone:waechter_besiegt',
        {'trigger': 'minecraft:impossible'}, frame='challenge'))
    schreibe('advancement/erster_herzschlag.json', adv(
        'minecraft:heart_of_the_sea', 'Herzschlag', 'Das erwachte Herz teilt seine Kraft. Einmal am Tag.',
        'skyandstone:herz_erwacht', {'trigger': 'minecraft:impossible'}, frame='task', ansagen=False))

    # ---- Bosskampf ----
    name = json.dumps({'text': 'Der letzte Wächter', 'color': 'dark_purple', 'bold': True}, ensure_ascii=False)
    boss_nbt = ('{Tags:["%s"],PersistenceRequired:1b,CustomNameVisible:1b,CustomName:\'%s\',Health:400.0f,'
                'attributes:[{id:"minecraft:generic.max_health",base:400.0d},{id:"minecraft:generic.attack_damage",base:12.0d},'
                '{id:"minecraft:generic.knockback_resistance",base:0.9d},{id:"minecraft:generic.follow_range",base:48.0d},'
                '{id:"minecraft:generic.armor",base:10.0d}],'
                'HandItems:[{id:"minecraft:netherite_sword",count:1},{}],HandDropChances:[0.0f,0.0f],'
                'ArmorItems:[{},{},{},{id:"minecraft:netherite_helmet",count:1}],ArmorDropChances:[0.0f,0.0f,0.0f,0.0f]}') % (BOSS, name)
    schatten_name = json.dumps({'text': 'Leerenschatten', 'color': 'dark_gray'}, ensure_ascii=False)
    schatten = 'summon minecraft:vex ~%s ~3 ~%s {Tags:["%s"],LifeTicks:600,CustomName:\'%s\'}'
    schreibe('function/waechter/beschwoeren.mcfunction', '\n'.join([
        '# Ruft den letzten Wächter. Aufruf: execute positioned <Herz-Block> run function skyandstone:waechter/beschwoeren',
        '# (herz_ritual.js, nach Netherstern auf dem Herz der Leere über einem Herzsockel)',
        f'summon minecraft:marker ~ ~ ~ {{Tags:["{MARKER}"]}}',   # positioned <Blockkoordinaten> zentriert schon auf die Blockmitte
        f'summon minecraft:wither_skeleton ~3 ~1 ~ {boss_nbt}',
        f'scale set pehkui:base 2.5 @e[tag={BOSS},distance=..10]',
        f'bossbar add {BAR} {name}',
        f'bossbar set {BAR} color purple',
        f'bossbar set {BAR} style notched_10',
        f'bossbar set {BAR} max 400',
        f'bossbar set {BAR} players @a[distance=..48]',
        'scoreboard players set #phase sns_waechter 0',
        'scoreboard players set #fehlt sns_waechter 0',
        'scoreboard players set #aktiv sns_waechter 1',
        'playsound minecraft:entity.wither.spawn hostile @a[distance=..64] ~ ~ ~ 1 0.8',
        'particle minecraft:reverse_portal ~ ~1 ~ 1 1 1 0.5 300 force',
        titel('Der letzte Wächter', '„Zeig mir, dass du es wert bist.“', 'dark_purple', '@a[distance=..64]')]))
    schreibe('function/waechter/tick.mcfunction', '\n'.join([
        '# Läuft jeden Tick, solange #aktiv sns_waechter = 1 (aus tick.mcfunction).',
        f'execute store result bossbar {BAR} value run data get entity @e[tag={BOSS},limit=1] Health',
        f'execute store result score #hp sns_waechter run data get entity @e[tag={BOSS},limit=1] Health',
        f'execute at @e[tag={MARKER},limit=1] run bossbar set {BAR} players @a[distance=..48]',
        '# Fällt der Wächter von der Insel (mehr als 32 Blöcke vom Herz), holt ihn das Herz zurück',
        f'execute as @e[tag={BOSS}] at @s unless entity @e[tag={MARKER},distance=..32] at @e[tag={MARKER},limit=1,sort=nearest] run tp @s ~3 ~1 ~',
        'execute if score #phase sns_waechter matches 0 if score #hp sns_waechter matches 1..266 run function skyandstone:waechter/phase1',
        'execute if score #phase sns_waechter matches 1 if score #hp sns_waechter matches 1..133 run function skyandstone:waechter/phase2',
        '# Wächter weg, Herz-Marker geladen: nach 3 s Abbruch (z. B. in Lava gestorben, kein Spieler-Kill → kein Sieg)',
        f'execute if entity @e[tag={BOSS}] run scoreboard players set #fehlt sns_waechter 0',
        f'execute unless entity @e[tag={BOSS}] if entity @e[tag={MARKER}] run scoreboard players add #fehlt sns_waechter 1',
        'execute if score #fehlt sns_waechter matches 60.. run function skyandstone:waechter/abbruch']))
    schreibe('function/waechter/abbruch.mcfunction', chr(10).join([
        '# Kampf ohne Sieg beendet: aufräumen, Herz bleibt schlafend, ein neuer Netherstern ruft ihn wieder',
        f'execute at @e[tag={MARKER},limit=1] run tellraw @a[distance=..64] ' + json.dumps({'text': 'Der Wächter ist in der Leere verschwunden. Das Herz wartet auf einen neuen Netherstern.', 'color': 'gray'}, ensure_ascii=False),
        f'kill @e[tag={SCHATTEN}]',
        f'kill @e[tag={MARKER}]',
        f'bossbar remove {BAR}',
        'scoreboard players set #aktiv sns_waechter 0',
        'scoreboard players set #fehlt sns_waechter 0']))
    schreibe('function/waechter/phase1.mcfunction', '\n'.join([
        '# Zwei Drittel Leben: Leerenschatten',
        'scoreboard players set #phase sns_waechter 1',
        f'execute at @e[tag={BOSS},limit=1] run ' + schatten % ('1', '0', SCHATTEN, schatten_name),
        f'execute at @e[tag={BOSS},limit=1] run ' + schatten % ('-1', '1', SCHATTEN, schatten_name),
        f'execute at @e[tag={BOSS},limit=1] run ' + schatten % ('0', '-1', SCHATTEN, schatten_name),
        f'execute at @e[tag={BOSS},limit=1] run playsound minecraft:entity.evoker.prepare_summon hostile @a[distance=..48] ~ ~ ~ 1 0.6',
        f'execute at @e[tag={MARKER},limit=1] run title @a[distance=..48] actionbar ' + json.dumps({'text': 'Der Wächter ruft die Schatten.', 'color': 'dark_purple'}, ensure_ascii=False)]))
    schreibe('function/waechter/phase2.mcfunction', '\n'.join([
        '# Ein Drittel Leben: Zorn',
        'scoreboard players set #phase sns_waechter 2',
        f'effect give @e[tag={BOSS}] minecraft:speed 600 0 true',
        f'effect give @e[tag={BOSS}] minecraft:strength 600 0 true',
        f'execute at @e[tag={BOSS},limit=1] run ' + schatten % ('2', '0', SCHATTEN, schatten_name),
        f'execute at @e[tag={BOSS},limit=1] run ' + schatten % ('-2', '0', SCHATTEN, schatten_name),
        f'execute at @e[tag={MARKER},limit=1] run effect give @a[distance=..32] minecraft:darkness 6 0',
        f'execute at @e[tag={BOSS},limit=1] run playsound minecraft:entity.warden.roar hostile @a[distance=..48] ~ ~ ~ 1 0.7',
        f'execute at @e[tag={MARKER},limit=1] run title @a[distance=..48] actionbar ' + json.dumps({'text': 'Der Wächter wird wütend.', 'color': 'red'}, ensure_ascii=False)]))
    schreibe('function/waechter/sieg.mcfunction', '\n'.join([
        '# Sieg: läuft als der Spieler, der den Wächter besiegt hat (Advancement skyandstone:waechter_besiegt)',
        f'execute at @e[tag={MARKER},limit=1,sort=nearest] run setblock ~ ~ ~ skyandstone:herz_erwacht',
        f'execute at @e[tag={MARKER},limit=1,sort=nearest] run advancement grant @a[distance=..64] only skyandstone:herz_erwacht',
        f'execute at @e[tag={MARKER},limit=1,sort=nearest] as @a[distance=..64] at @s run function skyandstone:feier/herz_erwacht',
        'give @s skyandstone:waechterkern',
        f'kill @e[tag={SCHATTEN}]',
        f'kill @e[tag={MARKER},limit=1,sort=nearest]',
        f'bossbar remove {BAR}',
        'scoreboard players set #aktiv sns_waechter 0',
        'weather clear 6000']))
    schreibe('function/feier/herz_erwacht.mcfunction', '\n'.join([
        '# Das Herz der Leere schlägt wieder (nach dem Sieg über den Wächter)',
        titel('Das Herz schlägt', 'Unter allen Inseln pocht es wieder. Die Leere atmet ruhig.', 'light_purple'),
        'playsound minecraft:block.beacon.activate player @s ~ ~ ~ 1 0.6',
        'playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1',
        'particle minecraft:end_rod ~ ~2 ~ 1 1 1 0.1 120 force @s',
        'summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:30,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{flight_duration:1,explosions:[{shape:"star",colors:[I;11953407,16737279],fade_colors:[I;16777215],has_trail:true,has_twinkle:true}]}}}}']))

    # ---- load/tick ergänzen (idempotent) ----
    for datei, zeile in (('function/load.mcfunction', 'scoreboard objectives add sns_waechter dummy'),
                         ('function/tick.mcfunction', 'execute if score #aktiv sns_waechter matches 1 run function skyandstone:waechter/tick')):
        p = os.path.join(DP, *datei.split('/'))
        text = open(p, encoding='utf-8').read()
        if zeile not in text:
            with open(p, 'a', encoding='utf-8', newline='\n') as f:
                f.write(('' if text.endswith('\n') else '\n') + '# 1.1.0: Der letzte Wächter\n' + zeile + '\n')
    print('Herz-Daten geschrieben:', len(SPLITTER), 'Splitter, Bosskampf, Advancements')


if __name__ == '__main__':
    main()

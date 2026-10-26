"""Hinweise am Item (Tooltip + JEI-Infoseite) – EINE Quelle (0.11.0).
Der Generator (_src/quests.py) prüft jede ID und schreibt daraus kubejs/client_scripts/hinweise.js."""
HINWEISE = {
    'minecraft:netherrack': ['Ohne Nether: Wasserfass auf Myzel wird zu Hexenwasser.', 'Hexenwasser im Fass + Lava ergibt Netherrack.'],
    'exdeorum:witch_water_bucket': ['Entsteht, wenn ein Wasserfass auf Myzel steht.', 'Mit Lava im Fass wird daraus Netherrack.'],
    'exdeorum:mycelium_spores': ['Aus Erde gesiebt. Auf Erde gesetzt wird Myzel daraus.', 'Myzel unter einem Wasserfass macht Hexenwasser.'],
    'exdeorum:silkworm': ['Auf Laub setzen: Es wird nach und nach befallen.', 'Voll befallenes Laub nur mit dem Crook abbauen, dann fällt Faden.'],
    'exdeorum:crook': ['Laub abbauen: mehr Setzlinge, selten eine Seidenraupe.', 'Voll befallenes Laub gibt Faden (etwa jedes zweite).'],
    'create:blaze_burner': ['Ohne Nether: Leerer Lohenbrenner + 4 Lohenstaub (Staub sieben).'],
    'create:empty_blaze_burner': ['4 Eisenbleche um 1 Netherrack.', 'Mit 4 Lohenstaub wird ein Lohenbrenner daraus.'],
    'minecraft:end_portal_frame': ['Es gibt keine Festungen in der Leere: Der Rahmen ist herstellbar (Obsidian, Enderauge, Endstein).'],
    'minecraft:ancient_debris': ['Schwarzstein hämmern und den Schutt sieben gibt selten Antiken Schrott.'],
    'mysticalagriculture:inferium_seeds': ['Werkbank: 8 Inferiumessenz um einen Weizensamen. Kein Altar nötig.'],
    'mysticalagriculture:prudentium_essence': ['4 Inferiumessenz um einen Infusionskristall. Der Kristall bleibt erhalten.'],
    'mysticalagriculture:tertium_essence': ['Nur im Create-Mixer: 4 Prudentium + 1 Messingbarren = 2 Tertium.'],
    'mysticalagriculture:imperium_essence': ['4 Tertium um eine Infused Alloy (Mekanism).'],
    'mysticalagriculture:supremium_essence': ['4 Imperium um einen Engineering Processor (AE2).'],
    'createsifter:zinc_mesh': ['Stöcke um einen Zinkbarren. Siebt wie das Iron Mesh.'],
    'ftbquests:screen_1': ['Eisen, Glas, Redstone. Zeigt eine Quest an und nimmt Items oder Strom dafür an.'],
    'ftbquests:lootcrate': ['Rechtsklick öffnet die Kiste. Schleichen + Rechtsklick öffnet den ganzen Stapel.'],
    'waystones:waystone': ['Reisen zwischen Wegsteinen kostet Erfahrung. Dafür ist XP in Sky and Stone da.'],
    # 1.1.0 „Die sieben Splitter“
    'skyandstone:splitter_rohling': ['Die Hülle für alle sieben Splitter.', '4 Glas um eine Amethystscherbe ergibt 2 Stück.'],
    'skyandstone:splitter_erde': ['Splitter 1 von 7. Mechanischer Mixer, beheizt.'],
    'skyandstone:splitter_glut': ['Splitter 2 von 7. Mechanischer Mixer, überhitzt (Lohenkuchen).'],
    'skyandstone:splitter_strom': ['Splitter 3 von 7. Energizing Orb (Powah).'],
    'skyandstone:splitter_ordnung': ['Splitter 4 von 7. Gravurmaschine (AE2).'],
    'skyandstone:splitter_leben': ["Splitter 5 von 7. Kochtopf (Farmer's Delight)."],
    'skyandstone:splitter_geist': ['Splitter 6 von 7. Bezaubernder Apparat oder Auflösungsapparat.'],
    'skyandstone:splitter_leere': ['Splitter 7 von 7. Kernsynthesizer oder Imbuement-Kammer.'],
    'skyandstone:leerenessenz': ['Fällt von Endermen (etwa jeder dritte).', 'Drygmys und Mobfarmen bekommen sie auch.'],
    'skyandstone:karte_werkstatt': ['Rechtsklick in der Oberwelt: Die vergessene Werkstatt taucht', '80 Blöcke in Blickrichtung auf. Vorher in eine freie Richtung schauen.'],
    'skyandstone:herz_der_leere': ['Auf einen Herzsockel stellen und mit einem Netherstern anklicken.', 'Dann erscheint der letzte Wächter.'],
    'skyandstone:herz_erwacht': ['Rechtsklick: einmal pro Minecraft-Tag Eile, Regeneration', 'und Glück für alle in der Nähe.'],
    'skyandstone:herzsockel': ['Das Herz der Leere gehört darauf. Hier wird gekämpft.'],
    'skyandstone:waechterkern': ['Beweis, dass du den letzten Wächter besiegt hast.'],
}

# TODO 10.6 (26.10.2026): Stimmung und Herkunft je Lootkiste. Schlüssel = string_id der Belohnungstabelle
# (name + 'kiste' in questlib.table). Herkunft muss zu den Drop-Gewichten in quests.py passen (Generator prüft das).
KISTEN = {
    'holzkiste':    ('Treibholz aus dem Nichts, notdürftig vernagelt.', 'Aus dem Questbuch, manchmal von Tieren und Monstern.'),
    'eisenkiste':   ('Die Werkzeugkiste eines frühen Erbauers.', 'Aus dem Questbuch, selten von Monstern.'),
    'goldkiste':    ('Der Schatz einer Insel, die längst gefallen ist.', 'Aus großen Meilensteinen und von Bossen.'),
    'messingkiste': ('Rohstoffe für die ersten Fabriken.', 'Nur aus dem Questbuch (Messing, Siebfabrik).'),
    'magiekiste':   ('Riecht nach Quelle und altem Pergament.', 'Nur aus dem Questbuch.'),
    'technikkiste': ('Zahnräder und Wellen, noch ölig von alter Arbeit.', 'Nur aus dem Questbuch.'),
    'naturkiste':   ('Erde, Samen und etwas, das noch wachsen will.', 'Nur aus dem Questbuch.'),
    'sternkiste':   ('Sie summt leise, als hätte sie einen Herzschlag.', 'Von Bossen und aus den größten Taten.'),
}

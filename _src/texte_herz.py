"""Texte für Sky and Stone 1.1.0 „Die sieben Splitter“ (Stil: _src/TEXTSTIL.md, Design: _src/DESIGN-HERZ-DER-LEERE.md).

QUESTS = {schlüssel: (titel, [zeilen])}, STORY = {meilenstein: (titel, notiz)}.
Item-Namen wie im Spiel (_src/namen.json). Höchstens 6 Zeilen in der Hauptstory.
"""

QUESTS = {
    'sp_rohling': ('Splitter-Rohling', [
        'Ein Splitter braucht eine Hülle, bevor er etwas halten kann.',
        '',
        'Leg 4 Glas um eine &eAmethystscherbe&r: Das gibt 2 &eSplitter-Rohlinge&r.',
        'Amethyst siebst du mit dem Flint Mesh aus Crushed Deepslate.',
        'Tipp: Jeder der sieben Splitter beginnt mit so einem Rohling.']),
    'sp_erde': ('Splitter der Erde', [
        'Boden, Sieb und Messing. Daraus bestand die erste Welt.',
        '',
        'Im &eMechanischen Mixer&r über einem beheizten &eLohenbrenner&r: Rohling, Kies, Sand, Dust, 4 &ePrudentiumessenz&r, 1 &eMessingbarren&r und 250 mB Wasser.',
        'Tipp: R auf dem Splitter in JEI zeigt das Rezept.']),
    'hz_werkstatt': ('Die vergessene Werkstatt', [
        'Die Karte zeigt eine Insel, die auf keiner anderen steht.',
        '',
        'Die &eKarte der vergessenen Werkstatt&r gibt es für den ersten Flug. Rechtsklick in der Oberwelt lässt die Werkstatt 80 Blöcke in Blickrichtung auftauchen.',
        'Flieg hin und sieh dir den &eZerbrochenen Herzsockel&r in der Mitte an. Die Truhe dort gehört dir.',
        'Tipp: Schau vorher in eine freie Richtung, sonst passt die Insel nicht hin.']),
    'sp_glut': ('Splitter der Glut', [
        'Normales Feuer reicht nicht. Der Splitter will Lohenglut.',
        '',
        'Füttere den Lohenbrenner mit einem &eLohenkuchen&r: Er wird überhitzt (blaue Flamme).',
        'Dann im Mixer: Rohling, 2 &eLohenruten&r, 4 &eCrushed Netherrack&r, 1 &eObsidian&r und 250 mB Lava.']),
    'sp_strom': ('Splitter des Stroms', [
        'Die Erbauer fingen Strom in Glas. Du auch.',
        '',
        'Im &eEnergizing Orb&r (Powah) mit 500.000 FE: Rohling, 2 &eInfundierte Legierung&r, 1 Osmiumbarren, 1 &eKupfersuple&r, 1 Redstone-Block.',
        'Tipp: Den Orb speist du mit dem Alternator oder jedem anderen FE-Netz.']),
    'sp_ordnung': ('Splitter der Ordnung', [
        'Zwischen zwei Gedanken passt ein dritter.',
        '',
        'Die &eGravurmaschine&r presst den Rohling zwischen einem &eLogikprozessor&r (oben) und einem &eKalkulationsprozessor&r (unten).',
        'Beide Prozessoren werden dabei verbraucht.']),
    'hz_vier': ('Vier von Sieben', [
        'Erde, Glut, Strom und Ordnung. Das Herz zuckt zum ersten Mal.',
        '',
        'Halte die vier Splitter gleichzeitig. Sie werden nicht verbraucht.',
        'Was fehlt, ist schwerer: Leben, Geist und die Leere selbst.']),
    'sp_essenz': ('Leerenessenz', [
        'Endermen tragen ein Stück Leere in sich.',
        '',
        'Sammle 4 &eLeerenessenz&r. Sie fällt von Endermen (ungefähr jeder dritte).',
        'Drei Wege: selbst kämpfen, eine Mobfarm bauen oder einen Drygmy (Ars Nouveau) die Beute holen lassen.']),
    'sp_leben': ('Splitter des Lebens', [
        'Was wächst, will weiterwachsen. Auch in Glas.',
        '',
        'Im &eKochtopf&r über einer Hitzequelle: Rohling, 1 &eHoney Treat&r, 2 &eImperiumessenz&r, 1 &eGoldener Apfel&r, 1 &eReichhaltige Erde&r.',
        'Honig kommt von Bienen (Spawneier aus dem Sieb), Reichhaltige Erde aus Organischem Kompost.']),
    'sp_geist': ('Splitter des Geistes', [
        'Magie oder Maschine, der Geist ist derselbe.',
        '',
        '&lMagie:&r &eBezaubernder Apparat&r mit Rohling, darum Wilden Horn, Wilden-Flügel, Wilden Spike, Quelledelsteinblock und 2 Leerenessenz (5000 Quelle).',
        '&lTechnik:&r &eAuflösungsapparat&r mit Rohling, je 3 Overworld- und Nether-Predictions (Hostile Networks), 1 Leerenessenz und 1000 mB Essenz (Monsterschnetzler).']),
    'sp_leere': ('Splitter der Leere', [
        'Er wiegt nichts. Er wiegt alles.',
        '',
        '&lTechnik:&r &eAntiprotonischer Kernsynthesizer&r: Rohling und 100 mB Antimaterie.',
        '&lMagie:&r &eImbuement-Kammer&r mit Rohling, darum Drachenatem, Shulker-Schale und Leerenessenz (5000 Quelle).']),
    'hz_sockel': ('Der Herzsockel', [
        'Du hast den zerbrochenen gesehen. Bau einen, der hält.',
        '',
        'Werkbank: 5 Steinziegel, 1 &eZaubertisch&r in der Mitte oben, 3 Glatter Stein unten.',
        'Stell ihn dorthin, wo das Herz schlagen soll. Dort wird auch gekämpft.']),
    'hz_herz': ('Das Herz der Leere', [
        'Sieben Splitter, ein Herz. Es ist kalt und schwer.',
        '',
        'Die &eMechanische Handwerkseinheit&r (5×5) setzt es zusammen: die sieben Splitter, 8 Leerenessenz und 5 Obsidian. Muster in JEI.',
        'Tipp: Der Wächter kommt erst, wenn du ihn rufst. Bereite dich vor.']),
    'hz_wache': ('Der letzte Wächter', [
        'Jemand hat all die Notizen geschrieben. Er ist nie gegangen.',
        '',
        'Setz das &eHerz der Leere&r auf den Herzsockel und klick es mit einem &eNetherstern&r an. Besiege den Wächter.',
        '&cEr ist riesig, trägt Netherit und ruft Schatten.&r Kämpf auf einer großen, umzäunten Plattform.',
        'Tipp: Fällt er von der Insel, holt ihn das Herz zurück. Fällst du, rettet dich die Leere.']),
    'hz_schlag': ('Das Herz schlägt', [
        'Unter allen Inseln pocht es wieder.',
        '',
        'Klick das &eErwachte Herz der Leere&r an. Einmal pro Minecraft-Tag gibt es allen in der Nähe Eile, Regeneration und Glück.',
        'Tipp: Bau deine Werkstatt um das Herz herum.']),
}

STORY = {
    'sp_erde': ('Der erste Splitter',
                '„Das Herz ist nicht gestorben, es ist zersprungen. Sieben Splitter. Einen davon hältst du jetzt in der Hand. Er ist warm.“'),
    'hz_werkstatt': ('Die Werkstatt',
                     '„Hier haben wir das Herz geschmiedet, und hier ist es zersprungen. Ich konnte nur den Bauplan retten.“'),
    'hz_vier': ('Vier von sieben',
                '„Erde, Glut, Strom, Ordnung. Damit lief unsere Welt. Was fehlte, war das Schwerste: Leben, Geist und die Leere selbst.“'),
    'hz_herz': ('Sieben in einem',
                '„Das Herz ist ganz. Es wird erst schlagen, wenn ich weiß, dass du es nicht so behandelst wie wir.“'),
    'hz_wache': ('Der letzte Wächter',
                 '„Wenn du das liest, hast du mich besiegt. Gut. Ich habe lange genug gewacht. Jetzt wachst du.“'),
}

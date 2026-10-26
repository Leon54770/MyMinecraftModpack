"""Questtexte Magie, Abenteuer, Extras und Story, Stil siehe TEXTSTIL.md."""
GRUPPEN = {'haupt': 'Der Weg der Erbauer', 'mods': 'Handbuch der Mods', 'extras': 'Abseits des Weges'}
KAPITEL = {
    'ars': ('Ars Nouveau', ['Magie, die dir Arbeit abnimmt: Transport, Mob-Drops, Autocrafting.']),
    'bienen': ('Productive Bees', ['Rohstoffe, die summen.']),
    'dimensionen': ('Nether und End', ['Festungen über der Leere, Wither und Drache.']),
    'maschinengeist': ('Hostile Networks und IF', ['Mobs simulieren statt jagen, Erz per Laser.']),
    'story': ('Das Herz der Leere', [
        'Die Notizen des letzten Wächters, in der Reihenfolge der Geschichte.',
        'Jede Notiz liegt in ihrem Meilenstein und wird lesbar, sobald du ihn erreichst.']),
    'markt': ('Inselmarkt', [
        'Tausch deinen Überschuss gegen Beutekisten. Die Items werden beim Abgeben verbraucht.',
        'So tauschst du: Im Questbuch die Tausch-Quest öffnen und die Items aus deinem Inventar abgeben. Sie verschwinden, du bekommst eine Kiste. Im Team gibt es pro Tausch eine Kiste für alle.',
        'Jeder Tausch hat eine Abklingzeit. Kisten fallen selten auch von Monstern, Bosse lassen immer eine fallen.']),
    'sammler': ('Sammlerbuch', ['Freiwillig: Sammle alles einmal.']),
    'bau': ('Baumeister', ['Optional: schön statt nur praktisch.']),
}
QUESTS = {
    # ---------------- Ars Nouveau ----------------
    'a_quelle': ('Stein, der Quelle trägt', [
        'Im Amethyst aus dem Sieb schläft eine alte Kraft.',
        '',
        'Leg Amethyst in die &eImbuement-Kammer&r, daraus wird Quellstein.',
        'Quellstein ist der Grundstoff aller Magie in Ars Nouveau.']),
    'a_buch': ('Das erste Zauberbuch', [
        'Ein leeres Buch, das darauf wartet, beschrieben zu werden.',
        '',
        'Taste C öffnet das &eZauberbuch für Anfänger&r. Dort steckst du Zauber aus Glyphen zusammen.',
        'Tipp: Projektil + Abbauen ergibt Fernabbau.']),
    'a_tisch': ('Der Tisch des Schreibers', [
        'Die Erbauer schrieben ihre Zauber Glyphe für Glyphe.',
        '',
        'Am &eTisch des Schreibers&r lernst du neue Glyphen.']),
    'a_glas': ('Quelle aus Wurzeln', [
        'Wo etwas wächst, fließt Quelle.',
        '',
        'Der &eAgronomische Quellenlink&r erzeugt Quelle aus wachsenden Pflanzen und füllt damit ein Quellglas.',
        'Tipp: Stell ihn direkt neben deine Felder.']),
    'a_archwood': ('Archwood', [
        'Bäume, die schon vor dem Zerbrechen alt waren.',
        '',
        'Archwood-Setzlinge findest du im Moos-Sieb. Ihre Früchte sind Zutaten für Rituale.']),
    'a_whirli': ('Der Gärtnergeist', [
        'Ein kleiner Geist, der Wurzeln zum Treiben bringt.',
        '',
        'Der Whirlisprig aus dem &eWirbelzweig-Charme&r lässt Pflanzen und Bäume in seiner Nähe schneller wachsen und erzeugt dabei Quelle.',
        'Tipp: Gut neben Feldern und Botany Pots, eine Alternative zu Wachstumsbeschleunigern.']),
    'a_crush': ('Zerkleinern ohne Hammer', [
        'Was der Hammer kann, schafft auch ein Zauber.',
        '',
        'Die Glyphe Crush macht aus Bruchstein Kies, aus Kies Sand und aus Sand Staub, genau wie der Hammer.',
        'Ein &eEinfacher Zauberturm&r mit Berühren + Crush vor einem Bruchstein-Generator zerkleinert von allein, mit Redstone-Takt.',
        'Tipp: Eine Alternative zum Mahlstein (Create) oder mechanischen Hammer. Du musst nicht beides bauen.']),
    'a_drygmy': ('Beute ohne Blut', [
        'Er nimmt, was die Tiere tragen, und lässt sie leben.',
        '',
        'Ein Drygmy aus dem &eTrockenen Charme&r holt Mob-Drops von Tieren und Monstern in der Nähe, ohne sie zu töten.']),
    'a_wilden': ('Spuren der Wilden', [
        'Die Wilden sind fort. Ihre Reste nicht.',
        '',
        'In der Leere gibt es keine Wilden. &eWilden Horn&r, Wilden Spike und Wilden-Flügel findest du im Gold-Sieb.']),
    'a_apparat': ('Der Apparat', [
        'Ein Altar, an dem Quelle zu Form wird.',
        '',
        'Stell den &eBezaubernden Apparat&r auf einen Arkanen Kern.']),
    'a_ritual': ('Das Ritualbecken', [
        'Manche Magie braucht Feuer und einen festen Ort.',
        '',
        'Im &eRitual-Kohlenbecken&r führst du Rituale aus.']),
    'a_wixie': ('Die kleine Werkstatt', [
        'Eine Wixie vergisst kein Rezept.',
        '',
        'Setz die Wixie mit ihrem &eWixie-Charme&r auf einen Kessel. Daraus wird ein Wixie-Kessel.',
        'Leg Zutaten in Truhen daneben und zeig ihr das Rezept. Sie stellt es immer wieder her.',
        'Tipp: Für einfache Dinge (Fackeln, Bleche, Legierungen) ein früher Ersatz für AE2-Autocrafting. Für große Mengen bleibt AE2 stärker.']),
    'a_erzmagier': ('Erzmagier', [
        'Das stärkste Zauberbuch. Ab hier ist Magie kein Spielzeug mehr.',
        '',
        'Werte am Schreibtisch auf: Zauberbuch des Magiers, 3 Enderperlen, 2 Smaragde, 1 Diamantblock, 1 Netherstern (Wither) und 1 &eWilden-Tribut&r.',
        'Den Tribut lässt die &lWilden-Chimera&r fallen: Ritual „Beschwöre Wilden“ im Ritualbecken, verstärkt mit Wilden Horn, Wilden Spike und Wilden-Flügel.',
        '&cAchtung: Das Chimera-Ritual zerstört Blöcke rund um das Becken. Bau es auf einer eigenen Plattform weit weg von deiner Basis.&r']),
    # ---------------- Productive Bees ----------------
    'b_biene': ('Das erste Summen', [
        'Im Moos schläft noch Leben.',
        '',
        'Ein &eBienen-Spawn-Ei&r findest du beim Sieben von Moosblöcken.']),
    'b_stock': ('Ein besserer Stock', [
        'Ein Zuhause für ein Volk, das arbeitet.',
        '',
        'Der &efortgeschrittene Bienenstock&r ist produktiver als der normale und lässt sich mit Upgrades erweitern.']),
    'b_zentri': ('Die Zentrifuge', [
        'Jede Wabe birgt mehr als Honig.',
        '',
        'Die &eCentrifuge&r zerlegt Waben in Wachs, Honig und Rohstoffe.']),
    'b_nest': ('Nester bauen', [
        'Die Leere baut keine Nester. Du schon.',
        '',
        'Stell ein Nest wie das &eStone Nest&r selbst her und auf. Passende Wildbienen ziehen ein.']),
    'b_zucht': ('Bienen aus Erz', [
        'Mit Geduld und Zucker summt bald das Metall.',
        '',
        'Mit &eHoney Treat&r und dem richtigen Block züchtest du Bienen, die Eisen, Kupfer und mehr liefern.',
        'Tipp: JEI zeigt unter „Bienenzucht“, was geht.']),
    'b_upgrade': ('Fleißige Völker', [
        'Ein Stock, der mehr gibt, als er nimmt.',
        '',
        'Stell ein Upgrade für Produktivität her und setz es in deinen Bienenstock.']),
    # ---------------- Nether und End ----------------
    'j_shulker': ('Schalen aus Endstein', [
        'Keine Endstädte, aber der Staub erinnert sich.',
        '',
        'In der Leere gibt es keine Endstädte. &eShulker-Schalen&r findest du im Diamant- oder Netherit-Sieb aus zerkleinertem Endstein.']),
    # ---------------- Hostile Networks und IF ----------------
    'h_learner': ('Der Deep Learner', [
        'Jeder Kampf lehrt etwas. Hier wird es aufgeschrieben.',
        '',
        'Hostile Neural Networks: Der &eDeep Learner&r trainiert Datenmodelle, während du kämpfst.']),
    'h_modell': ('Das erste Datenmodell', [
        'Ein leerer Rahmen wartet auf ein Gesicht.',
        '',
        'Rechtsklick mit einem &eModel Framework&r auf einen Mob bindet das Modell an seine Art.']),
    'h_sim': ('Kämpfe im Kasten', [
        'Krieg ohne Schwert, nur Strom und Rechnung.',
        '',
        'Die &eSimulation Chamber&r simuliert Kämpfe mit Strom und erzeugt Prediction Matrix-Vorhersagen.']),
    'h_fab': ('Beute-Fabrikator', [
        'Der Feind muss nicht mehr kommen. Seine Beute schon.',
        '',
        'Der &eLoot Fabricator&r macht aus Vorhersagen echte Drops: Enderperlen, Lohenruten, Knochen und mehr.',
        'Ab hier kommen deine Mob-Drops aus der Maschine.']),
    'h_rahmen': ('Der erste Rahmen', [
        'Industrial Foregoing beginnt klein und klebrig.',
        '',
        'Bau ein &ePrimitives Maschinengehäuse&r. Der Weg führt über Latex aus Bäumen zu Plastik.']),
    'h_plastik': ('Plastik', [
        'Aus Baumsaft wird etwas, das die Erbauer nie hatten.',
        '',
        'Stell 16 &eKunststoff&r her.']),
    'h_laser': ('Erz aus dem Nichts', [
        'Ein Strahl in die Leere, und sie gibt Erz zurück.',
        '',
        'Die &eErz-Laserbasis&r mit Laserbohrern bohrt Erz aus dem Nichts.',
        'Tipp: Farbige Linsen bevorzugen bestimmte Erze.']),
    # ---------------- Inselmarkt ----------------
    'x_samen': ('Saatgut-Händler', [
        'Der Händler nimmt Samen, so viele du hast.',
        '',
        'Gib 256 &eWeizenkörner&r ab. Sie werden verbraucht. Zu viele Samen aus dem Sieb?',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_kies': ('Kieshändler', [
        'Kies hast du immer. Er zahlt trotzdem.',
        '',
        'Gib 256 &eKies&r ab. Er wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_cobble': ('Steinbruch', [
        'Der Generator läuft und läuft. Der Händler auch.',
        '',
        'Gib 512 &eBruchstein&r ab. Er wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_fleisch': ('Zombie-Abfall', [
        'Zu nichts gut, ehrlich gesagt. Er nimmt es trotzdem.',
        '',
        'Gib 128 &eVerrottetes Fleisch&r ab. Es wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_inferium': ('Essenz-Überschuss', [
        'Inferium wächst schneller, als du es brauchst.',
        '',
        'Gib 256 &eInferiumessenz&r ab. Sie wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_mehl': ('Müllerei', [
        'Feines Mehl, frisch vom Mahlstein.',
        '',
        'Gib 256 &eWeizenmehl&r ab. Es wird verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_seetang': ('Seetang-Kraftwerk', [
        'Getrockneter Seetang, gepresst zu Blöcken.',
        '',
        'Gib 64 &eGetrockneter Seetangblock&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_honig': ('Imkerei', [
        'Waben aus dem Bienenstock, noch warm.',
        '',
        'Gib 64 &eHonigwabe&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_warze': ('Netherwarzen-Farm', [
        'Netherwarzen wachsen auf Seelensand. Der Händler fragt nicht, woher.',
        '',
        'Gib 128 &eNetherwarze&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_knochen': ('Knochensammler', [
        'Von Skeletten oder vom Fischfang, ihm ist es gleich.',
        '',
        'Gib 128 &eKnochen&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal pro Minecraft-Tag.']),
    'x_perlen': ('Enderhandel', [
        'Perlen aus Farm oder Simulation, gezählt und gewogen.',
        '',
        'Gib 32 &eEnderperle&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    'x_lohe': ('Lohenruten-Handel', [
        'Lohenruten im Überfluss? Er nimmt sie gern.',
        '',
        'Gib 32 &eLohenrute&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    'x_quelle': ('Quellstein-Handel', [
        'Quellsteine, die sich stapeln, finden hier einen Käufer.',
        '',
        'Gib 32 &eQuelljuwel&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    'x_polonium': ('Strahlender Handel', [
        'Er trägt Handschuhe. Du solltest es auch.',
        '',
        'Gib 4 &ePolonium Pellet&r ab, aus dem Fissionsreaktor oder dem Isotopen-Zentrifugen-Weg. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 3 Minecraft-Tage.']),
    'x_stern': ('Sternenhandel', [
        'Ein Stern gegen eine Sternkiste. Ein fairer Tausch.',
        '',
        'Gib 1 &eNetherstern&r ab. Er wird verbraucht.',
        'Wiederholbar: einmal alle 3 Minecraft-Tage.']),
    'x_supremium': ('Supremium-Handel', [
        'Supremium vom Feld, das Beste, was der Boden hergibt.',
        '',
        'Gib 8 &eSupremiumessenz&r ab. Sie wird verbraucht.',
        'Wiederholbar: einmal alle 3 Minecraft-Tage.']),
    'x_mechanik': ('Feinmechanik', [
        'Präzision vom Fließband, Stück für Stück geprüft.',
        '',
        'Gib 16 &ePräzisionsgetriebe&r ab. Sie werden verbraucht.',
        'Wiederholbar: einmal alle 2 Minecraft-Tage.']),
    # ---------------- Sammlerbuch ----------------
    'p_essenzen': ('Alle Essenzen', [
        'Sechs Essenzen, sechs Abschnitte deines Weges.',
        '',
        'Sammle je eine Essenz jeder Stufe, von &eInferiumessenz&r bis Insanium Essence.',
        'Die Reihe erzählt deinen Weg: Feld, Create, Mekanism, AE2, Endgame.']),
    'p_netze': ('Alle Netze', [
        'Vom Faden bis zum Netherit.',
        '',
        'Sammle jedes Netz vom &eString Mesh&r bis zum Netherite Mesh. Jedes siebt andere Schätze.']),
    'p_archwood': ('Die vier Archwoods', [
        'Vier Bäume, vier Farben der alten Magie.',
        '',
        'Sammle alle vier &eArchwood-Setzlinge&r. Ihre Früchte sind Zutaten für Rituale.']),
    'p_trophaeen': ('Trophäen', [
        'Beweise, dass du die Wächter dieser Welt bezwungen hast.',
        '',
        'Sammle &eNetherstern&r, Drachenei und Wither-Skelettschädel.',
        'Tipp: Stell sie irgendwo schön aus.']),
    # ---------------- Baumeister ----------------
    'u_meissel': ('Der Meißel', [
        'Ein Block, viele Gesichter.',
        '',
        'Rechiseled: Mit dem &eChisel&r bekommt ein Block viele Muster, verbundene Texturen inklusive.']),
    'u_dach': ('Ein Dach über dem Kopf', [
        'Auch über der Leere regnet es.',
        '',
        'Macaw\'s Roofs, Doors und Windows: Dächer, Türen und Fenster in allen Holzarten.',
        'Bau 16 &eDachblöcke&r beliebiger Art.']),
    'u_moebel2': ('Einrichten', [
        'Eine Insel wird erst mit einem Stuhl zum Zuhause.',
        '',
        'Handcrafted und Macaw\'s Furniture: Stühle, Tische, Regale, Betten.',
        'Bau zwei &eStühle&r und einen Tisch.']),
    'u_bruecke2': ('Brücke ins Nichts', [
        'Ein Seil über dem Abgrund verbindet, was zerbrochen ist.',
        '',
        'Macaw\'s Bridges: &eHängebrücken&r zu deinen Nebeninseln.',
        'Tipp: Wege und Laternen gibt es in Macaw\'s Paths und Lights.']),
    'u_framed': ('Rahmenblöcke', [
        'Ein Block, der jedes Kleid trägt.',
        '',
        'FramedBlocks wie der &eFramed Cube&r nehmen das Aussehen jedes Blocks an.']),
    'u_gadget': ('Bau-Gadget', [
        'Ganze Flächen in einem Atemzug.',
        '',
        'Das &eBuilding Gadget&r baut ganze Flächen auf einmal. Es braucht Strom.']),
    'u_kopie': ('Inselarchitekt', [
        'Was du einmal gebaut hast, baust du nie wieder von Hand.',
        '',
        'Das &eCopy Paste Gadget&r speichert ganze Gebäude und baut sie woanders wieder auf.']),
}
STORY = {
    'w_start': ('Die erste Notiz', '„Wer das liest, steht auf einem Splitter unserer Welt. Darunter schläft das Herz der Leere.“'),
    'e_sieb': ('Sternenstaub', '„Einst siebten wir Sternenstaub. Du siebst Kies. Es ist derselbe Anfang.“'),
    'e_eisen': ('Der Funke', '„Das erste Metall. Wir nannten es den Funken, weil danach alles schneller brannte.“'),
    'g_autark': ('Zurück zum Leben', '„Eine Insel, die sich selbst nährt. So fängt der Weg zurück an.“'),
    'c_siebfabrik': ('Die erste Maschine', '„Unsere Maschinen liefen Tag und Nacht, bis sie verstummten. Du hast gerade die erste wieder geweckt.“'),
    'j_nether': ('Die zerbrochene Unterwelt', '„Auch die Unterwelt zerbrach. Unsere Festungen hängen dort noch in der Luft, leer wie wir.“'),
    's_reaktor': ('Kraft aus der Leere', '„Wir nahmen die Kraft aus der Leere, nicht aus Kohle. Wir nahmen zu viel, und der Boden riss.“'),
    'k_inject': ('Gier', '„Aus jedem Brocken das Vierfache. So reich waren wir. So gierig.“'),
    'l_auto': ('Netze, die denken', '„Unsere Netze dachten mit. Am Ende dachten sie schneller als wir.“'),
    'm_niemehr': ('Felder aus Erz', '„Als die Minen versiegt waren, ließen wir Erz auf Feldern wachsen. Wenigstens das war richtig.“'),
    'a_erzmagier': ('Maschine und Magie', '„Maschine und Magie waren für uns nie Gegensätze. Erst zusammen erreichten sie das Herz.“'),
    'h_fab': ('Feinde auswendig', '„Wir lernten unsere Feinde auswendig, bis wir sie nicht mehr bekämpfen mussten.“'),
    'j_drache': ('Der Wächter am Ende', '„Der Drache bewachte das Ende. Nicht für uns. Vor uns.“'),
    'z_sps': ('Der Herzschlag', '„Antimaterie, der Herzschlag der Leere in einer Kapsel. Behandle sie mit Respekt.“'),
    'z_herr': ('Das Erbe', '„Wer das Herz wieder schlagen lässt, trägt unser Erbe. Nimm nur, was du brauchst. Wir nahmen alles.“'),
}

# ---------------------------------------------------------------------
# 0.7.0: Story ohne Widerspruch (ein Weg genügt), Kern-Lore auf der Hauptstory, Akt II mit Notiz, Bienen ehrlich
# ---------------------------------------------------------------------
KAPITEL['story'] = ('Tagebuch des Wächters', KAPITEL['story'][1])   # Akt III heißt schon „Das Herz der Leere“
STORY['k_spalt'] = STORY.pop('s_reaktor')
STORY['c_alternator'] = ('Die Leitungen', '„Wir verlegten Leitungen bis unter die Wolken. Wenn der Strom floss, summte die ganze Insel.“')
STORY['z_weg'] = ('Ein Weg genügt', '„Wir wollten Maschine und Magie zugleich, und beide ganz. Einer der Wege hätte gereicht.“')
STORY['a_erzmagier'] = ('Das letzte Buch', '„Unsere Magier schrieben, bis die Seiten glühten. Nur dieses Buch hat das Zerbrechen überstanden.“')
QUESTS['b_zucht'] = ('Bienen aus Erz', [
    'Mit Geduld und Zucker summt bald das Metall.',
    '',
    'Erz-Bienen haben zwei Eltern: Ein &eQuartz Nest&r im Nether, mit Quarz gelockt, gibt die Kristallbiene.',
    'Ein &eGravel Nest&r in einem Fluss- oder Strandbiom (F3 zeigt das Biom) gibt die Ashy Mining Bee.',
    'Nester baust du selbst: Quartz Nest = Eisenschwert + Quartz in Netherrack, Gravel Nest = Holzschwert + Kies.',
    'Beide gekreuzt ergeben die Eisenbiene. Weitere Erze zeigt JEI unter „Bienenzucht“.'])
QUESTS['h_fab'][1].append('Für den Fabricator brauchst du einen &eNetheritbarren&r: Schwarzstein (Fass, siehe JEI) hämmern, den Schutt sieben (selten Antiker Schrott), dann 4 Netheritplatten + 4 Goldbarren.')

# ---------------------------------------------------------------------
# 0.8.0: Prüfungen der Leere (echte Aufgaben statt Haken), Deko-Tausch, Bienen prüfen die Eisenbiene
# ---------------------------------------------------------------------
KAPITEL['pruefungen'] = ('Prüfungen der Leere', ['Herausforderungen ohne Pflicht. Für Ingenieure, Magier und Mutige.'])
QUESTS['t_chimera'] = ('Die Chimera', [
    'Halb Horn, halb Flügel, ganz Zorn. Die Wilden haben eine Königin.',
    '',
    'Besiege die &eWilden-Chimera&r. Beschworen wird sie mit dem Ritual „Wilden beschwören“, verstärkt mit Horn, Stachel und Flügel.',
    '&cDas Ritual zerstört Blöcke rund um das Becken.&r Bau es auf einer eigenen Plattform.',
    'Belohnung: Such dir ein Item aus der Goldkiste aus.'])
QUESTS['t_speicher'] = ('Der Speicher der Erbauer', [
    'Die Erbauer maßen ihre Macht in Strom. Zeig, was deine Insel liefert.',
    '',
    'Stell einen &eAufgaben Bildschirm (1x1)&r auf (Eisen, Glas, Redstone), wähle diese Quest daran aus und speise 10 Millionen FE ein.',
    'Tipp: Kabel oder Pipez direkt an den Bildschirm anschließen.'])
QUESTS['t_fabrik'] = ('Tausend Barren', [
    'Eine Fabrik erkennt man daran, dass sie nicht aufhört.',
    '',
    'Hab 1024 &eEisenbarren&r gleichzeitig dabei (ein Rucksack hilft). Sie werden nicht verbraucht.'])
QUESTS['t_drache'] = ('Der zweite Drache', [
    'Der Wächter am Ende kehrt zurück, wenn man ihn ruft.',
    '',
    'Besiege den Enderdrachen ein zweites Mal. Vier Endkristalle auf dem Ausgangsportal rufen ihn zurück.',
    'Belohnung: Such dir ein Item aus der Sternkiste aus.'])
# 26.10.2026: drei weitere Prüfungen
QUESTS['t_festung'] = ('Die Festung räumen', [
    'In den leeren Festungen wachen noch die Knochen ihrer Besatzung.',
    '',
    'Besiege 50 &eWither-Skelette&r. Sie erscheinen nur in Netherfestungen.',
    'Tipp: Nebenbei fallen manchmal Wither-Skelettschädel für den Wither.'])
QUESTS['t_schatten'] = ('Schattenjagd', [
    'Im End starren dich die Schatten an. Starr zurück.',
    '',
    'Besiege 32 &eEnderman&r. Im End erscheinen sie auf dem Endstein.',
    'Tipp: Ein geschnitzter Kürbis als Helm hält sie ruhig, wenn du sie ansiehst.'])
QUESTS['t_netz'] = ('Ein Netz ohne Ende', [
    'Die Erbauer ließen ganze Inseln summen. Jetzt summt deine.',
    '',
    'Stell einen &eAufgaben Bildschirm (1x1)&r auf, wähle diese Quest daran aus und speise 1 Milliarde FE ein.',
    'Tipp: Ein großer Energiespeicher kann vorher sammeln und alles auf einmal abgeben.',
    'Belohnung: Such dir ein Item aus der Sternkiste aus.'])
QUESTS['x_dach'] = ('Dachdecker', [
    'Der Händler baut eine neue Siedlung und braucht Ziegel.',
    '',
    'Gib 64 Eichen-Dachblöcke (Macaw\'s Roofs) ab. Sie werden verbraucht.',
    'Wiederholbar: einmal pro Minecraft-Tag.'])
QUESTS['x_bruecke'] = ('Brückenbauer', [
    'Zwischen den Inseln fehlen Wege. Der Händler zahlt für jede Brücke.',
    '',
    'Gib 32 Eichen-Hängebrücken (Macaw\'s Bridges) ab. Sie werden verbraucht.',
    'Wiederholbar: einmal pro Minecraft-Tag.'])
QUESTS['b_zucht'] = ('Bienen aus Erz', [
    'Mit Geduld und Zucker summt bald das Metall.',
    '',
    'Erz-Bienen haben zwei Eltern: Ein &eQuartz Nest&r im Nether, mit Quarz gelockt, gibt die Kristallbiene. Ein &eGravel Nest&r in einem Fluss- oder Strandbiom (F3 zeigt das Biom) gibt die Ashy Mining Bee.',
    'Nester baust du selbst: Quartz Nest = Eisenschwert + Quartz in Netherrack, Gravel Nest = Holzschwert + Kies.',
    'Beide gekreuzt ergeben die Eisenbiene. &lAufgabe:&r eine Wabe der Eisenbiene aus ihrem Stock.',
    'Tipp: Das Simulations-Upgrade hält Bienen im Stock. Das spart am Laptop viel Leistung.'])

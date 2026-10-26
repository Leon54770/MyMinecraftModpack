"""Questtexte Mod-Kapitel Technik/Natur, Stil siehe TEXTSTIL.md."""
KAPITEL = {
    'exdeorum': ('Ex Deorum: Staub und Siebe', ['Siebe, Netze, Tiegel und Gießkannen. Was die Leere nahm, holst du dir Korn für Korn zurück.']),
    'landwirtschaft': ('Felder und Küche', ['Farmer\'s Delight, Botany Pots, Nutztiere. Eine Insel, die sich selbst nährt.']),
    'create': ('Create: Zahnrad und Messing', ['Zahnräder, Mühlstein, Sifter, Messing. Die Maschinen der Erbauer drehen sich wieder.']),
    'energie': ('Strom und Rohre', ['Create Crafts & Additions, Powah, Pipez. Kraft erzeugen, speichern und verteilen.']),
    'mekanism': ('Mekanism: Die Werkhalle', ['Erzverarbeitung, Schaltkreise, Atomtechnik, Werkzeuge.']),
    'lagerung': ('Lager und Rucksack', ['Sophisticated Backpacks, Sophisticated Storage, Functional Storage. Ordnung gegen das Kistenchaos.']),
    'ae2': ('Applied Energistics 2: Das Netz', ['ME-Netz, Autocrafting, kabellos.']),
    'mysticalag': ('Mystical Agriculture: Erzfelder', [
        'Erz, das auf Feldern wächst.',
        'Stufen: Inferium → Prudentium → Tertium (Create) → Imperium (Mekanism) → Supremium (AE2) → Insanium.']),
}

QUESTS = {
    # --- Ex Deorum ---
    'e_haken': ('Mit dem Haken ins Laub', [
        'Im Laub verstecken sich mehr Setzlinge, als man denkt.',
        '',
        'Den &eCrook&r stellst du aus vier Holzstäben her (zwei oben, je einer darunter). Brich damit Laub ab: Es lässt öfter Setzlinge fallen und gibt Seidenraupen.']),
    'e_eisennetz': ('Das Eisennetz', [
        'Feinere Maschen, seltenere Funde.',
        '',
        'Setz ein &eIron Mesh&r ins Sieb. Damit tauchen Osmium-, Zinn-, Blei- und Silberbrocken auf.',
        'Tipp: In der Erde steckt auch Inferiumessenz für Mystical Agriculture.']),
    'e_kanne': ('Die bessere Gießkanne', [
        'Mehr Wasser, schnellere Bäume.',
        '',
        'Bau eine &eIron Watering Can&r. Sie hält mehr Wasser und lässt Bäume schneller wachsen.']),
    's_mechsieb': ('Das Sieb mit Strom', [
        'Die Hand ermüdet. Die Maschine nicht.',
        '',
        'Das &eMechanical Sieve&r ist das Ex-Deorum-Sieb mit Strom: Netz einsetzen, Kies per Trichter hinein, den Rest erledigt es.',
        'Tipp: Es braucht nur 20 FE pro Tick.']),
    's_mechhammer': ('Hammer ohne Arm', [
        'Stein zu Kies, Kies zu Sand, ohne einen Schlag.',
        '',
        'Der &eMechanical Hammer&r zerkleinert Blöcke mit Strom.']),

    # --- Landwirtschaft ---
    'e_samen': ('Was in der Erde steckt', [
        'Die Erde der Insel ist voller vergessener Saat.',
        '',
        'Siebe Erde mit dem &eString Mesh&r. Dabei fallen Samen, Setzlinge und mehr heraus.',
        'Von hier aus geht es weiter zu Feldern, Küche und Tieren.']),
    'g_feld': ('Das erste Feld', [
        'Ein Streifen Grün über der Leere.',
        '',
        'Weizen, Karotten, Kartoffeln: Alles kommt aus dem Sieb. Leg ein Feld an und ernte &e16 Feldfrüchte&r.',
        'Tipp: Mit der Gießkanne wächst das Feld schneller.']),
    'g_topf': ('Die Küche', [
        'Wer gut isst, siebt länger.',
        '',
        'Bau ein &eSchneidebrett&r und einen &eKochtopf&r aus Farmer\'s Delight.',
        'Das Schneidebrett holt mehr aus deinen Zutaten, der Kochtopf macht Gerichte, die lange satt machen.']),
    'g_tiere': ('Nutztiere', [
        'Leben kehrt auf die Insel zurück.',
        '',
        'Spawneier für Kuh, Schaf, Huhn und Schwein findest du beim Sieben von Erde. Sammle Leder und Eier.',
        '&cZäune nicht vergessen: Um dich herum ist nur Leere.']),
    'g_topf_pflanze': ('Pflanzen im Topf', [
        'Ein Garten, der sich selbst pflegt.',
        '',
        'In einem &eBotany Pot&r wachsen Pflanzen und Bäume von allein.',
        'Tipp: Ein Trichter-Topf erntet selbst und reicht weiter. Deine erste Automatik.']),
    'g_baumtopf': ('Holz im Topf', [
        'Nie wieder Bäume fällen.',
        '',
        'Setzling und Erde in einen &eHopper Botany Pot&r: unendlich Holz ohne Axt.']),
    'g_festessen': ('Sterneküche in der Leere', [
        'Ein Festmahl, gewachsen auf einem Felsen im Nichts.',
        '',
        'Koch einen &eHirtenkuchen&r und ein &eBackhähnchen&r, beide komplett aus Inselzutaten.',
        'Damit ist Hunger kein Thema mehr.']),
    'g_inferium': ('Inferiumessenz', [
        'Ein grüner Schimmer im Siebgut. Er ist mehr als Staub.',
        '',
        'Siebe Erde mit dem String Mesh oder einem besseren Netz. Dabei fällt &eInferiumessenz&r.',
        'Damit beginnt Mystical Agriculture.']),
    'g_autark': ('Die autarke Insel', [
        '„Eine Insel, die sich selbst nährt, ist der erste Schritt zurück.“',
        '',
        'Stell vier &eHopper Botany Pots&r auf: Holz und Essen wachsen von selbst und landen in Truhen.',
        'Deine Insel versorgt sich jetzt selbst.']),

    # --- Create ---
    'c_deployer': ('Die mechanische Hand', [
        'Eine Hand aus Messing, die nie müde wird.',
        '',
        'Das &eEinsatzgerät&r klickt für dich: Blöcke setzen, Items benutzen, Gegner schlagen.']),
    'c_crafter': ('Werkbank im Großformat', [
        'Neun Einheiten, ein Rezept.',
        '',
        'Bau neun &eMechanische Handwerkseinheiten&r. Zusammen stellen sie große Rezepte automatisch her.']),

    # --- Energie ---
    's_akku': ('Strom auf Vorrat', [
        'Auch der Wind ruht manchmal.',
        '',
        'Der &eAkkumulator&r speichert Strom für windstille Zeiten.']),
    's_orb': ('Der Energizing Orb', [
        'Eine Kugel, die Metall mit Kraft tränkt.',
        '',
        '&eDielectric Paste&r aus Ton, Kohle und Lava ist die Grundzutat von Powah.',
        'Der &eEnergizing Orb&r lädt Items mit Strom auf. Die Energizing Rods drumherum liefern die Energie.']),
    's_stahl': ('Geladener Stahl', [
        'Eisen und Gold, verschmolzen durch Strom.',
        '',
        'Leg Eisen und Gold in den Orb. Heraus kommt &eEnergized Steel&r, die Basis für alle Powah-Maschinen.']),
    's_furnator': ('Feuer zu Strom', [
        'Alte Technik, ehrliche Kraft.',
        '',
        'Der &eFurnator&r verbrennt Kohle und Holz zu Strom. Solide Grundversorgung.']),
    's_solar': ('Licht über der Leere', [
        'Hier oben scheint die Sonne ungehindert.',
        '',
        'Vier &eSolar Panels&r liefern Strom ohne Brennstoff. Allerdings nur tagsüber.']),
    's_kristall': ('Glut im Kristall', [
        'Feuer, eingefangen in Stein.',
        '',
        'Lohenstaub im Orb ergibt &eBlazing Crystal&r. Lohenstaub findest du beim Sieben von Dust.']),
    's_pipe': ('Rohre verlegen', [
        'Was von selbst fließt, musst du nicht tragen.',
        '',
        'Pipez bringt Items, Flüssigkeiten und Strom von A nach B. Leg &eItem Rohre&r und &eStrom Rohre&r.',
        'Tipp: Der Schraubenschlüssel öffnet die Einstellungen am Rohrende.']),
    's_upgrade': ('Schnellere Rohre', [
        'Mehr Durchfluss, mehr Kontrolle.',
        '',
        'Die &eNormale&r und die &eVerbesserte Rohr Modifikation&r machen Rohre schneller und erlauben Filter.',
        'Die Fortgeschrittene braucht Mekanism-Schaltkreise, die Ultimative zusätzlich AE2-Prozessoren.']),
    's_reaktor': ('Netzstrom', [
        '„Wir nahmen die Kraft aus der Leere, nicht aus Kohle. Zu viel davon zerriss den Boden.“',
        '',
        'Bau einen Powah-Reaktor: 3×4×3 aus &eReactor (Basic)&r, befeuert mit Uraninite aus dem Gold-Sieb.',
        'Danach ist Strom kein Engpass mehr.']),
    'z_ultimate': ('Rohre ohne Grenzen', [
        'Das Beste aus Mekanism und AE2 in einem Rohr.',
        '',
        'Bau die &eUltimative Rohr Modifikation&r. Dafür brauchst du Elite-Schaltkreise aus Mekanism und Prozessoren aus AE2.']),
    'z_strom': ('Großkraftwerk', [
        'Genug Kraft, um Materie zu spalten.',
        '',
        'Optional: Ein großer Powah-Reaktor aus &eReactor (Hardened)&r ist der bequeme Weg zu viel Strom.',
        'Für die Antimaterie reicht auch jede andere große Stromquelle, zum Beispiel der Spaltreaktor.']),

    # --- Mekanism ---
    'k_stahl': ('Stahl', [
        'Härter als Eisen, das Rückgrat jeder Maschine.',
        '',
        'Infundiere Eisen mit Kohle in der Metallurgischen Infusionsanlage und schmelze das Ergebnis zu &eStahlbarren&r.']),
    'k_cube': ('Strom verteilen', [
        'Ein Netz aus Kupferadern für deine Werkhalle.',
        '',
        '&eEinfache Universalkabel&r tragen Strom, der &eEinfache Energie-Würfel&r speichert ihn.']),
    'k_separator': ('Elektrolyse', [
        'Aus Wasser wird Gas.',
        '',
        'Der &eElektrolyseur&r spaltet Wasser in Wasserstoff und Sauerstoff.']),
    'k_x5': ('×5: Die volle Kette', [
        'Fünf Barren aus einem Erz. Nichts geht verloren.',
        '',
        'Optional: Bau die &eChemische Auflösungskammer&r. Auflösen, Waschen, Kristallisieren ergibt fünf Barren pro Erz.',
        'Tipp: Lohnt sich nur, wenn du noch viel siebst.']),
    'k_fortschritt': ('Bessere Schaltkreise', [
        'Feinere Bahnen, klügere Maschinen.',
        '',
        'Stell vier &eFortschrittliche Steuerschaltkreise&r her.',
        'Sie schalten die Fortgeschrittene Rohr Modifikation von Pipez frei.']),
    'k_meka': ('Werkzeug der Zukunft', [
        'Ein Werkzeug für alles, was im Weg steht.',
        '',
        'Der &eAtomic Disassembler&r ist Spitzhacke, Axt und Schaufel in einem und läuft mit Strom.']),
    'k_tiab': ('Zeit ist Geld', [
        'Die Erbauer konnten die Zeit biegen. Jetzt kannst du es auch.',
        '',
        '&eTime in a Bottle&r sammelt Zeit, solange es in deinem Inventar liegt.',
        'Rechtsklick auf eine Maschine beschleunigt sie, hier bis zu 8-fach.']),
    'z_meka': ('Die MekaSuit', [
        'Eine Rüstung aus Antimaterie und Stahl.',
        '',
        'Mit Antimaterie in der Hand baust du die &eMekaSuit Brustplatte&r.']),

    # --- Lagerung ---
    'l_rucksack': ('Der Rucksack', [
        'Die Taschen sind voll, das Sieb gibt weiter.',
        '',
        'Bau einen &eRucksack&r und ein &ePickup-Upgrade&r.',
        'Mit dem Upgrade füllt sich der Rucksack automatisch mit deinen Siebfunden.']),
    'l_fass': ('Lagerfässer', [
        'Ordnung beginnt mit dem ersten Fass.',
        '',
        'Bau ein Fass aus Sophisticated Storage. Fässer und Truhen lassen sich aufrüsten und haben einen Sortierknopf.']),
    'l_schubladen': ('Schubladen', [
        'Tausend Steine, ein Block.',
        '',
        'Functional Storage: &eSchubladen&r fassen viel von einer Sorte auf kleinem Raum. Stell vier davon auf.']),
    'l_controller': ('Die Schubladen-Wand', [
        'Eine Wand, ein Eingang, kein Suchen mehr.',
        '',
        'Der &eStorage Controller&r macht alle Schubladen zu einem Lager mit einem Eingang.',
        'Tipp: Das löst das Kistenchaos, bis AE2 steht.']),

    # --- AE2 ---
    'l_wireless': ('Kabellos', [
        'Das Netz folgt dir, wohin du auch fliegst.',
        '',
        'Mit der &eDrahtlosen Universalkonsole&r hast du dein ME-Netz in der Tasche.']),
    'l_appmek': ('Gase im Netz', [
        'Auch was man nicht anfassen kann, lässt sich lagern.',
        '',
        'Applied Mekanistics: Mit der &e1k ME Chemical Storage Cell&r speichert AE2 Mekanism-Gase und -Chemikalien.']),
    'l_mega': ('Riesenspeicher', [
        'Für alle, die nichts wegwerfen.',
        '',
        'MEGA Cells fassen Millionen Bytes. Bau eine &e1M MEGA Item Storage Cell&r.']),

    # --- Mystical Agriculture ---
    'm_kupfer': ('Kupfer und Kohle', [
        'Die ersten Erze, die aus der Erde sprießen.',
        '',
        'Stell Samen für Kupfer und Kohle her. Kohle ist Stufe 2, Kupfer Stufe 3 und braucht &eTertiumessenz&r.']),
    'm_gold': ('Gold und Redstone', [
        'Gold wächst nicht für jeden.',
        '',
        'Stell Samen für Gold und Redstone her. Redstone ist Stufe 3, Gold Stufe 4.',
        'Für Gold brauchst du &eImperiumessenz&r, und die gibt es nur mit Mekanism.']),
    'm_diamant': ('Diamanten vom Feld', [
        'Edelsteine als Ernte. Die Erbauer hätten gestaunt.',
        '',
        'Diamant-Samen sind Stufe 5 und brauchen &eSupremiumessenz&r, die erst mit AE2 möglich ist.']),
    'm_beschleuniger': ('Wachstumsbeschleuniger', [
        'Was unten glüht, wächst oben schneller.',
        '',
        'Stapel &eInferium-Wachstumsbeschleuniger&r unter das Ackerland. Die Pflanzen darüber wachsen schneller.']),
    'm_acker': ('Essenz-Ackerland', [
        'Der richtige Boden für die richtige Saat.',
        '',
        'Leg &eImperium-Ackerland&r an. Passendes Ackerland gibt Samen derselben Stufe mehr Ertrag.']),
    'z_insanium': ('Insanium-Ernte', [
        'Die höchste Stufe. Sie verlangt alles, was du gebaut hast.',
        '',
        'Insanium braucht neben Supremium einen &eUltimativen Steuerschaltkreis&r aus Mekanism.',
        '4 Supremium + 1 Schaltkreis ergeben 2 &eInsanium Essence&r.',
        'Tipp: Lass AE2 die Schaltkreise automatisch bauen.']),
    'z_netherstern': ('Sterne vom Feld', [
        'Was einst nur der Wither trug, wächst jetzt im Beet.',
        '',
        'Stell Samen für Nethersterne her. Dann wachsen Nethersterne auf dem Feld.']),
}

# 0.7.0: Die Notiz „Kraft aus der Leere“ steht jetzt beim Spaltreaktor (Hauptstory), hier eine eigene Stimmungszeile
QUESTS['s_reaktor'][1][0] = 'Kristall, Uraninit und Geduld. Dann summt die Insel.'
QUESTS['g_inferium'][1][3] = 'Damit beginnt Mystical Agriculture: An der Werkbank werden daraus die ersten Samen.'

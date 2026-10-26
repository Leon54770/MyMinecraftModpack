"""Questtexte Hauptstory (Akt I–III), Stil siehe TEXTSTIL.md."""
KAPITEL = {
    'akt1': ('Akt I: Ein Splitter im Nichts', [
        'Vom ersten Baum bis zur Siebfabrik mit Create.',
        'Details zu jedem Schritt stehen in den Mod-Kapiteln.']),
    'akt2': ('Akt II: Die Maschinen erwachen', [
        'Strom, Mekanism, der zerbrochene Nether und das erste ME-Netz.']),
    'akt3': ('Akt III: Das Herz der Leere', [
        'Autocrafting, Erz vom Feld, Bosse, Antimaterie und das Finale.']),
}

QUESTS = {
    # ---------------- Akt I ----------------
    'w_start': ('Willkommen in der Leere', [
        'Unter dir nichts. Nur ein Splitter der alten Welt.',
        '',
        'Die &lHauptstory&r führt dich. Belohnungen holst du im Questbuch selbst ab: Quest anklicken.',
        '- In JEI zeigt &eR&r das Rezept, &eU&r wofür ein Item gebraucht wird.',
        '- Taste ` (Gravis) halten: ganze Bäume und Erzadern auf einmal abbauen. M öffnet die Karte.',
        '&cKeine Insel, sondern eine normale Welt?&r Neue Welt, Welttyp &lSkyblock&r.']),
    'e_holz': ('Der erste Baum', [
        'Ein Baum ist alles, was die Erbauer dir gelassen haben.',
        '',
        'Fäll den Baum und sammle 5 Holzstämme.',
        'Tipp: Pflanz die Setzlinge sofort wieder, sonst ist dein einziger Baum weg.']),
    'e_raupe': ('Seidenraupe und Faden', [
        'Aus Laub wird Seide, aus Seide wird dein erstes Netz.',
        '',
        'Setz die &eSilkworm&r aus der Start-Quest auf Laub. Es wird langsam zu Spinnweben, die beim Abbauen zu Faden zerfallen.',
        'Mit dem Haken findest du im Laub weitere Seidenraupen. Das String Mesh braucht 9 Faden.']),
    'e_fass': ('Kompostfass', [
        'Aus Abfall wird Boden. So wächst deine Insel.',
        '',
        'Bau ein Holzfass (z. B. &eOak Barrel&r) und wirf Laub, Setzlinge oder Essen hinein. Nach einer Weile wird daraus Erde.',
        'Tipp: Fässer sammeln bei Regen auch Wasser.']),
    'e_cobble': ('Stein aus dem Nichts', [
        'Wo Lava auf Wasser trifft, entsteht Stein. Unendlich viel.',
        '',
        'Bau dir einen &eEimer&r aus Eisen (3 Barren). Hol damit Wasser (Holztiegel oder Teich) und Lava (Porzellantiegel) und lass beide neben einem freien Block zusammenfließen. Bau 32 &eBruchstein&r ab.',
        '&cAchtung:&r Trifft Wasser die einzige Lava-Quelle, ist deine Lava weg. Obsidian bricht nur mit Diamantspitzhacke.']),
    'e_hammer': ('Hammerzeit', [
        'Stein ist nur Kies, der noch nicht zerschlagen wurde.',
        '',
        'Bau einen &eStone Hammer&r aus Bruchstein und Stöcken. Kein Stein auf der Insel? 4 &eStone Pebble&r aus dem Sieb ergeben 1 Bruchstein.',
        'Hämmer zerschlagen Blöcke: Bruchstein → Kies → Sand → Staub. Später übernimmt das der Mühlstein.']),
    'e_sieb': ('Das erste Sieb', [
        'Was die Leere verschluckt hat, gibt das Sieb zurück.',
        '',
        'Stell ein Sieb auf (z. B. &eOak Sieve&r), setz ein &eString Mesh&r ein (9 Faden) und leg Erde, Kies oder Sand darauf. Dann Rechtsklick halten.',
        'Tipp: Bis zu 5×5 Siebe nebeneinander siebst du mit einem Klick gleichzeitig.']),
    'e_tiegel': ('Wasser aus Blättern', [
        'Auch Laub trägt noch Wasser in sich.',
        '',
        'Bau einen Holztiegel (z. B. &eOak Crucible&r) und füll ihn mit Laub oder Setzlingen. Er schmilzt sie zu Wasser.',
        'Ohne Teich auf der Insel ist das deine einzige Wasserquelle, auch für das Wasserrad. Ein Eimer holt das Wasser heraus.']),
    'e_lavatiegel': ('Feuer aus Stein', [
        'Stein erinnert sich an das Feuer, aus dem er kam.',
        '',
        'Der &ePorcelain Crucible&r schmilzt Bruchstein zu Lava, wenn darunter eine Hitzequelle steht (Fackel, Lava, Feuer).',
        'Rezept: 7 Porzellanton im Muster „s s / s s / s m s“ ergibt den ungebrannten Tiegel. Den brennst du im Ofen.']),
    'e_brocken': ('Erz im Kies', [
        'Im Kies liegen Splitter der alten Minen.',
        '',
        'Schon das String Mesh gibt aus Kies Eisen- (10 %) und Kupferbrocken (8 %). Sammle 8 &eIron Ore Chunk&r.',
        '4 Brocken ergeben 1 Erz zum Schmelzen. 8 Brocken ergeben also 2 Erz.',
        'Tipp: Das Flint Mesh bringt etwas mehr und dazu Andesit-Kiesel für Create.']),
    'e_feuernetz': ('Ein besseres Netz', [
        'Feinere Maschen, reichere Funde.',
        '',
        'Bau ein &eFlint Mesh&r (5 Faden, 4 Feuerstein) und setz es statt des Fadennetzes ins Sieb.',
        'Tipp: Netze lassen sich mit Effizienz und Glück verzaubern.']),
    'e_eisen': ('Der Funke', [
        'Metall aus dem Nichts. Die Erbauer nannten es den Funken.',
        '',
        'Schmilz die 2 Erz im Ofen mit Kohle oder Holz zu 2 &eEisenbarren&r.',
        'Damit öffnen sich Create, Mystical Agriculture und bessere Werkzeuge.']),
    'm_altar': ('Der Infusionsaltar', [
        'Hier verbanden die Erbauer Erde und Essenz.',
        '',
        'Stell den &eInfusionsaltar&r in die Mitte und 8 &eInfusionssockel&r drumherum. Hier entstehen Samen.']),
    'm_inferium': ('Samen der Essenz', [
        'Was du bisher gesiebt hast, wächst jetzt auf dem Feld.',
        '',
        'Stell am Infusionsaltar die ersten Inferium-Samen her. Sie lassen Inferiumessenz wachsen.',
        'Von nun an wird Essenz geerntet statt gesiebt.']),
    'm_prudentium': ('Stufe 2: Prudentium', [
        'Jede Stufe Essenz ist dichter als die letzte.',
        '',
        '4 Inferiumessenz ergeben 1 Prudentium. Sammle 16 &ePrudentiumessenz&r.']),
    'e_kupfer': ('Kupfer und Zink', [
        'Zwei Metalle, ohne die keine Maschine läuft.',
        '',
        'Kupfer- und Zinkbrocken kommen auch aus dem Kies, Zink ist selten (etwa 4 %). Schmilz 4 &eKupferbarren&r und 1 &eZinkbarren&r.',
        'Ein Zinkbarren reicht für den Anfang. Den Rest siebt später der Create-Sifter mit dem Eisennetz.']),
    'c_andesit': ('Andesitlegierung', [
        'Der Grundstoff, aus dem fast alles in Create gebaut ist.',
        '',
        'Andesit + Zink- oder Eisennuggets ergeben &eAndesitlegierung&r. Stell 16 her.',
        'Tipp: Andesit-Kiesel kommen aus dem Sieb. U auf Andesit in JEI zeigt alle Wege.']),
    'c_rad': ('Die erste Kraft', [
        'Die Insel hat jetzt einen Puls: Drehkraft.',
        '',
        'Bau ein &eWasserrad&r und stell es in fließendes Wasser (aus dem Holztiegel oder dem Teich). Das ist deine erste Kraftquelle.',
        'Alternativ: eine Windmühle mit Segeln.']),
    'c_muehle': ('Mühlstein statt Hammer', [
        'Was du mit dem Hammer zerschlagen hast, mahlt jetzt die Mühle.',
        '',
        'Der &eMahlstein&r macht alles, was der Hammer konnte: Bruchstein → Kies → Sand → Staub.',
        'Setz einen Trichter oben drauf, dann läuft das Mahlen von allein.',
        'Tipp: Das &eAndesite Casing&r (entrindeter Stamm + Andesitlegierung) brauchst du für viele Maschinen.']),
    'c_sifter': ('Sieben ohne Hände', [
        'Das Sieb arbeitet weiter, auch wenn du schläfst.',
        '',
        'Der &eSifter&r siebt mit denselben Tabellen wie das Handsieb, nur ohne dich. Bau dazu ein String Mesh und ein Andesite Mesh.',
        'Netze: String → Faden, Andesite → Feuerstein, Zinc → Eisen, Brass → Gold.']),
    'c_extruder': ('Der Extruder', [
        'Stein, der aus dem Nichts nachwächst.',
        '',
        'Der &eMechanical Extruder&r erzeugt Bruchstein (oder Basalt, Stein …) aus Lava und Wasser daneben.',
        'Zusammen mit Mahlstein und Sifter wird daraus eine Siebfabrik ohne Handarbeit.']),
    'c_presse': ('Die Presse', [
        'Aus Barren werden Bleche, aus Blechen Maschinen.',
        '',
        'Bau eine &eMechanische Presse&r. Sie presst Bleche, die du für viele Bauteile brauchst.']),
    'c_fan': ('Waschen mit Wind', [
        'Wind und Wasser holen mehr aus jedem Erz.',
        '',
        'Ein &eUmmantelter Lüfter&r, der durch Wasser bläst, wäscht zerkleinerte Erze. Das gibt mehr Nuggets.']),
    'c_mixer': ('Mixer und Becken', [
        'Hier verschmelzen Metalle zu neuen Legierungen.',
        '',
        'Stell einen Mixer (&eMechanischer Mixer&r) über ein &eBecken&r. Zusammen mischen sie Legierungen und Flüssigkeiten.']),
    'c_brenner': ('Feuer ohne Nether', [
        'Der Nether ist fern. Sein Feuer holst du dir trotzdem.',
        '',
        '1. &eLeerer Lohenbrenner&r: 4 Eisenbleche (Presse) um 1 Netherrack.',
        '2. Leerer Brenner + 4 Lohenstaub (aus Staub gesiebt) = &eLohenbrenner&r. Mit Kohle oder Holz gefüttert heizt er dein Becken.',
        '&lNetherrack ohne Nether:&r Mycelium Spores (Erde sieben) auf Erde ergeben Myzel. Ein Wasserfass auf Myzel wird nach gut einer Minute zu Hexenwasser.',
        'Hexenwasser im Fass + Lava ergibt Netherrack (U auf Netherrack in JEI).']),
    'c_messing': ('Messing', [
        'Gold für Arme, aber Create liebt es.',
        '',
        'Gib Kupfer und Zink in den Mixer. Das Becken muss beheizt sein: Darunter gehört ein Lohenbrenner.',
        'Stell 16 &eMessingbarren&r her.']),
    'c_siebfabrik': ('Die erste Maschine', [
        'Die Maschinen der Erbauer arbeiteten Tag und Nacht. Deine jetzt auch.',
        '',
        'Verbinde Extruder → Mahlstein → Sifter → Waschen → Ofen mit Förderbändern.',
        'Wenn 32 &eEisenbarren&r, 16 Zinkbarren und 32 Kupferbarren von allein kommen, ist Akt I abgeschlossen.']),

    # ---------------- Akt II ----------------
    'c_mechanismus': ('Präzisionsarbeit', [
        'Die Erbauer bauten nichts von Hand, was ein Fließband bauen konnte.',
        '',
        'Das &ePräzisionsgetriebe&r entsteht am Fließband mit Einsatzgerät und Presse.',
        'Das ist dein erster Weg über „Sequenced Assembly“. JEI zeigt die einzelnen Schritte.']),
    'c_alternator': ('Funken aus Drehung', [
        'Drehkraft wird zu Strom. Die alten Leitungen erwachen.',
        '',
        'Der &eAlternator&r (Create Crafts & Additions) macht aus Drehkraft Strom (FE).',
        'Mit der &eKupfersuple&r verbindest du ihn mit Akkus und Maschinen.']),
    'k_osmium': ('Osmium', [
        'Ein schweres, blaues Metall. Mekanism ist darauf gebaut.',
        '',
        'Osmiumbrocken findest du im Kies mit dem Iron Mesh. Schmilz 8 &eOsmiumbarren&r.']),
    'k_infuser': ('Die Infusionsanlage', [
        'Die wichtigste Maschine von Mekanism.',
        '',
        'Bau eine &eMetallurgische Infusionsanlage&r. Sie macht Legierungen, Stahl und Schaltkreise.']),
    'k_alloy': ('Infundierte Legierung', [
        'Eisen, durchtränkt mit Redstone.',
        '',
        'Infundier Eisen mit Redstone zu 8 &eInfundierte Legierung&r.',
        'Tipp: Du brauchst sie auch für Imperiumessenz (Mystical Agriculture).']),
    'k_schalt': ('Grundschaltkreis', [
        'Ohne Schaltkreis bleibt jede Maschine stumm.',
        '',
        'Osmium + Redstone in der Infusionsanlage: Stell 4 &eEinfacher Steuerschaltkreis&r her.',
        'Er steckt in fast jeder Maschine.']),
    'k_enrich': ('×2: Anreicherung', [
        'Ein Erz, zwei Barren. Der erste Schritt zu mehr.',
        '',
        'Bau eine &eAnreicherungskammer&r. Sie macht aus einem Erz zwei Staub.']),
    'k_purif': ('×3: Reinigung', [
        'Sauerstoff wäscht noch mehr Metall aus dem Gestein.',
        '',
        'Bau eine &eKlärkammer&r. Mit Sauerstoff aus dem Elektrolyseur bekommst du drei Barren pro Erz.']),
    'm_tertium': ('Stufe 3: Tertium', [
        'Hier treffen Maschine und Essenz zum ersten Mal aufeinander.',
        '',
        '4 Prudentium + 1 Messingbarren im Create-Mixer ergeben 2 &eTertiumessenz&r. Sammle 16.',
        'Nur so kommst du an Stufe-3-Samen.']),
    'm_eisen': ('Eisen vom Feld', [
        'Hier endet das Sieben. Eisen wächst.',
        '',
        'Stell Eisen-Samen her. Sie sind Stufe 3 und brauchen Tertiumessenz aus dem Create-Mixer.']),
    'j_obsidian': ('Obsidian', [
        'Das Tor in die Unterwelt beginnt mit schwarzem Stein.',
        '',
        'Gieß Wasser auf eine Lava-Quelle und bau 10 &eObsidian&r ab. Obsidian braucht eine &eDiamantspitzhacke&r.',
        '&cVorsicht beim Abbauen über der Leere.&r']),
    'j_nether': ('Die zerbrochene Unterwelt', [
        'Auch die Unterwelt zerbrach. Nur die Festungen hängen noch in der Luft.',
        '',
        'Bau ein Netherportal aus Obsidian und betritt den Nether.',
        'Er ist leer bis auf die Netherfestungen, die frei in der Luft liegen.']),
    'j_festung': ('Die Festung', [
        'Alte Mauern über dem Nichts. Hier lebt noch etwas.',
        '',
        'Finde eine Netherfestung und bau 16 &eNetherziegel&r ab.',
        'Dort spawnen Lohen und Wither-Skelette.']),
    'j_lohe': ('Lohenruten', [
        'Gefangenes Feuer, das man in der Hand tragen kann.',
        '',
        'Besieg Lohen in der Festung und sammle 8 &eLohenrute&r.',
        'Du brauchst sie für Brauen, Lohenbrenner (Create) und Enderaugen.']),
    'k_jetpack': ('Über der Leere', [
        'Zum ersten Mal trägt dich nichts als deine eigene Maschine.',
        '',
        'Bau ein &eJetpack&r (Iron Jetpacks) aus Triebwerken, Kondensator und den übrigen Teilen (Rezept in JEI) und lade es mit Strom.',
        'Tipp: Prüf vorher lieber noch einmal deinen Fallschutz.']),
    'l_certus': ('Certus-Quarz', [
        'Kristalle, die Wissen speichern können.',
        '',
        'Siebe Sand mit dem Iron Mesh. Sammle 16 &eCertusquarzkristall&r.']),
    'l_lader': ('Lader und Fluix', [
        'Strom im Kristall, Kristall im Wasser.',
        '',
        'Das &eLadegerät&r lädt Certus mit Strom auf.',
        'Wirf geladenen Certus + Redstone + Quarz ins Wasser. Daraus wird &eFluixkristall&r. Sammle 8.']),
    'l_inscriber': ('Prägeplatten ohne Meteor', [
        'In der Leere fallen keine Meteoriten. Die Platten machst du selbst.',
        '',
        'Bau eine &eGravurmaschine&r. Die vier Prägeplatten stellst du aus Certus-Quarz-Essenz her.',
        'Beispiel: 8 Essenz um einen Goldbarren = Logik-Platte, 8 Essenz um Silizium = Silizium-Platte. Die anderen zwei zeigt JEI (U auf die Essenz).',
        'Certus-Samen sind Stufe 3 (Tertium). Danach frei: Supremiumessenz und Pipez-Ultimate.']),
    'l_prozessoren': ('Prozessoren', [
        'Die Gedanken des Netzes entstehen hier.',
        '',
        'Präg je 4 &eLogikprozessor&r, &eKalkulationsprozessor&r und &eKonstruktionsprozessor&r in der Gravurmaschine.',
        'Tipp: Füttere die Gravurmaschine mit Pipez, sonst wird es mühsam.']),
    'l_netz': ('Das ME-Netz', [
        'Alles, was du besitzt, an einem Ort.',
        '',
        'Bau &eME-Controller&r, ME-Laufwerk, eine 4k-ME-Speicherzelle und eine ME-Konsole und verbinde sie.']),
    'k_inject': ('Vierfach-Erz', [
        'Aus jedem Brocken das Vierfache. So reich waren die Erbauer, und so gierig.',
        '',
        'Die &eChemische Injektionskammer&r macht vier Barren pro Erz.',
        'Sie braucht Chlorwasserstoff aus Salz (Verdampfung) und Wasserstoff. Damit ist Erz nie wieder knapp.']),

    # ---------------- Akt III ----------------
    'l_auto': ('Das Netz denkt mit', [
        'Die Netze der Erbauer dachten mit. Am Ende schneller als sie.',
        '',
        'Autocrafting: Bau einen &eME Schablonen-Provider&r, einen Molekularassembler und eine Fertigungseinheit für die Crafting-CPU.',
        'Danach bestellst du Dinge, statt sie zu bauen.']),
    'm_imperium': ('Stufe 4: Imperium', [
        'Essenz, gebunden an Metall aus der Maschine.',
        '',
        'Leg 4 Tertium im Kreuz um eine Infundierte Legierung (Mekanism). Sammle 16 &eImperiumessenz&r.']),
    'm_supremium': ('Stufe 5: Supremium', [
        'Fast so rein wie das, was unter der Welt schläft.',
        '',
        'Leg 4 Imperium im Kreuz um einen Konstruktionsprozessor (AE2). Sammle 8 &eSupremiumessenz&r.']),
    'm_niemehr': ('Felder aus Erz', [
        'Die Felder wuchsen Erz, als die Minen versiegt waren.',
        '',
        'Stell Osmium-, Certus- und Zink-Samen her. Dann wächst alles, was du bisher gesiebt hast.',
        'Dein Sieb darf in Rente gehen.']),
    'j_hexe': ('Hexenwasser-Trick', [
        'Was im Hexenwasser läuft, kommt dunkler wieder heraus.',
        '',
        'Skelette, die durch Hexenwasser (Ex Deorum) laufen, werden zu Wither-Skeletten.',
        'Sammle 3 &eWither-Skelettschädel&r für den Wither.']),
    'j_wither': ('Der Wither', [
        'Manche Dinge baut man besser weit weg von zu Hause.',
        '',
        'Beschwör den Wither und besieg ihn für einen &eNetherstern&r.',
        '&cBau ihn weit weg von deiner Insel. Sehr weit.&r']),
    'j_perlen': ('Enderperlen', [
        'Die Endermen kommen auch in die Leere.',
        '',
        'Endermen spawnen nachts auf dunklen Plattformen. Alternativ siebst du Staub.',
        'Sammle 12 &eEnderperle&r.']),
    'j_augen': ('Enderaugen', [
        'Augen, die den Weg ans Ende kennen.',
        '',
        'Stell 12 &eEnderauge&r aus Enderperlen und Lohenstaub her.']),
    'j_rahmen': ('Portalrahmen', [
        'Ohne Festungen in der Leere baust du das Tor selbst.',
        '',
        'Stell 12 &eEndportalrahmen&r aus Obsidian, Enderauge und Endstein her.']),
    'j_end': ('Das End', [
        'Das letzte Tor steht offen.',
        '',
        'Bau die Endportalrahmen zum Portal zusammen, setz die Enderaugen ein und betritt das End.']),
    'j_drache': ('Der Wächter am Ende', [
        'Der Drache bewachte das Ende. Nicht für die Erbauer, sondern vor ihnen.',
        '',
        'Die End-Hauptinsel ist da, mit Türmen und Kristallen. Besieg den Enderdrachen.',
        'Viel Glück.']),
    'z_elite': ('Elite-Schaltkreis', [
        'Feinere Schaltkreise für größere Maschinen.',
        '',
        'Stell 4 &eElitärer Steuerschaltkreis&r her. Das Rezept zeigt JEI (R).']),
    'z_ultkreis': ('Ultimate-Schaltkreis', [
        'Der feinste Schaltkreis, den Mekanism kennt.',
        '',
        'Aus Elite-Schaltkreisen + &eAtomlegierung&r stellst du 2 Ultimativer Steuerschaltkreis her.',
        'Du brauchst ihn für Insanium Essence und die ewige Fabrik.']),
    'm_insanium': ('Stufe 6: Insanium', [
        'Die höchste Stufe. Mehr gibt der Boden nicht her.',
        '',
        '4 Supremium + 1 Ultimativer Steuerschaltkreis (Mekanism) = 2 &eInsanium Essence&r. Sammle 4.',
        'Den Schaltkreis baust du aus Elite-Schaltkreisen und Atomlegierung. Weiter geht es im Kapitel „Das Herz der Leere“.']),
    'k_spalt': ('Spaltreaktor', [
        'Die Erbauer spalteten Atome. Respekt ist angebracht.',
        '',
        'Mekanism Generators: Ein Spaltreaktor aus &eKernreaktorgehäuse&r und &eKernbrennstoffbaugruppe&r macht aus Uran viel Strom und Atommüll, den du gleich brauchst.',
        'Uran: Uranbrocken aus zerkleinertem Tiefenschiefer im Sieb oder Uran-Samen. Weg: Uran → Yellowcake → Uranoxid → Uranhexafluorid → Spaltbrennstoff.',
        '&cKühlung (Wasser) nicht vergessen und den Reaktor nie überhitzen lassen.&r']),
    'k_polonium': ('Polonium', [
        'Aus Müll wird der Stoff, der das Herz der Leere nährt.',
        '',
        'Atommüll aus dem Spaltreaktor wird im &eSolarneutronenaktivator&r (braucht Tageslicht) zu Polonium.',
        'Das &ePolonium Pellet&r ist die Zutat für Antimaterie im SPS.']),
    'z_sps': ('Der Herzschlag', [
        'Antimaterie: der Herzschlag der Leere in einer Kapsel.',
        '',
        'Polonium-Pellets im SPS (Supercritical Phase Shifter) werden zu Antimaterie. Ein einziges &eAntimaterie Pellet&r reicht.',
        'Der SPS braucht sehr viel Strom: Spaltreaktor, Powah-Reaktor oder viele Generatoren.']),
    'z_fabrik': ('Die ewige Fabrik', [
        'Maschinen, Felder und Netz laufen endlich als ein Ganzes.',
        '',
        'Zeig 4 &eUltimativer Steuerschaltkreis&r aus Mekanism, 32 Supremiumessenz vom Feld und 2 Nethersterne aus der Netherstern-Saat vor.',
        'Die Items werden nur vorgezeigt, nicht verbraucht. Wenn dein ME-Netz sie von allein nachbaut, hast du es geschafft.']),
    'z_weg': ('Maschine oder Magie', [
        'Die Erbauer brauchten beides. Dir reicht einer der Wege.',
        '',
        '&lMagie:&r das &eErzmagier-Zauberbuch&r (Ars Nouveau).',
        '&lMaschinen:&r der &eLoot Fabricator&r (Hostile Networks).',
        'Die Quest erledigt sich, sobald du eins davon hast.']),
    'z_herr': ('Das Erbe der Erbauer', [
        'Das Herz der Leere schlägt wieder ruhig. Du trägst jetzt ihr Erbe.',
        '',
        'Maschinen, Magie und Felder arbeiten zusammen. Aus einer Insel mit einem Baum ist eine Welt geworden.',
        'Letzte Aufgabe: Bring das &eDrachenei&r nach Hause.',
        'Tipp: Das Ei teleportiert sich, wenn du es schlägst. Ein Kolben schiebt es herunter.',
        'Danke fürs Spielen von Sky and Stone.']),
}

# ---------------------------------------------------------------------
# 0.7.0: Korrekturen aus den Audits (falsche Mechanik, fehlende Freischaltungen, Wahl Maschine/Magie, Erz-Wahl)
# ---------------------------------------------------------------------
KAPITEL['akt3'] = ('Akt III: Das Herz der Leere', [
    'Autocrafting, Erz vom Feld, Bosse, Antimaterie und das Finale.',
    'Fürs Finale brauchst du einen Weg: Magie (Ars Nouveau) oder Maschinen (Hostile Networks). Früh anfangen lohnt sich.'])
_q = QUESTS
_q['w_start'][1][2] = ('&lDer Weg der Erbauer&r führt dich durch die großen Schritte, das &lHandbuch der Mods&r erklärt jede Mod genauer. '
                       '&lAbseits des Weges&r liegt alles ohne Pflicht: Markt, Bauen, Sammeln.')
# Ziel und erster Schritt vor den Quest-Hinweisen (Index 3 = „Quests erledigen sich …“)
_q['w_start'][1][3:3] = [
    '&lDein Ziel:&r Die Leere verstehen. Der Weg führt über Erz, Strom und Magie bis zu den Wahlen in Akt III und dem Finale.',
    '&lDein erster Schritt:&r Fäll den Baum im Kapitel „Akt I: Ein Splitter im Nichts“. Danach bestimmst du selbst, was du zuerst machst.',
    '']
_q['e_holz'][1].append('Kein Baum auf deiner Insel? Pflanz die Setzlinge aus dem Startinventar auf Erde. Das Kompostfass gibt dir Knochenmehl für später.')
_q['e_raupe'] = ('Seidenraupe und Faden', [
    'Aus Laub wird Seide, aus Seide wird dein erstes Netz.',
    '',
    'Setz die &eSilkworm&r aus der Start-Quest auf Laub. Es wird nach und nach befallen und steckt Nachbarlaub an.',
    'Voll befallenes Laub mit dem &eCrook&r abbauen: etwa jedes zweite gibt Faden. Mit der Hand gibt es nichts.',
    'Tipp: Pflanz vorher einen zweiten Baum, damit dir das Laub nicht ausgeht.'])
_q['e_eisen'][1][3] = 'Freigeschaltet: Kupfer und Zink für Create, das &eIron Mesh&r und der Einstieg in Mystical Agriculture.'
_q['e_eisen'][1].append('Tipp: Abseits des Weges warten jetzt der Inselmarkt und der Baumeister.')
_q['e_kupfer'][1][3] = 'Ein Zinkbarren reicht für den Anfang. Den Rest siebt später der Create-Sifter mit dem &eZinc Mesh&r.'
_q['m_inferium'] = ('Samen der Essenz', [
    'Was du bisher gesiebt hast, wächst jetzt auf dem Feld.',
    '',
    'An der Werkbank: 8 &eInferiumessenz&r um einen Weizensamen ergeben Inferium-Samen. Pflanz sie auf Ackerboden.',
    'Von nun an wird Essenz geerntet statt gesiebt. Den Infusionsaltar brauchst du erst später.'])
_q['m_prudentium'] = ('Stufe 2: Prudentium', [
    'Jede Stufe Essenz ist dichter als die letzte.',
    '',
    '4 Inferiumessenz um einen &eInfusionskristall&r ergeben 1 Prudentium. Der Kristall bleibt erhalten.',
    'Kristall: 1 Diamant, 4 Prosperiumsplitter (Kies mit Flint Mesh) und 4 Inferiumessenz. Sammle 16 &ePrudentiumessenz&r.'])
_q['m_altar'] = ('Der Infusionsaltar', [
    'Hier verbanden die Erbauer Erde und Essenz.',
    '',
    'Stell den &eInfusionsaltar&r in die Mitte und 8 &eInfusionssockel&r drumherum. Zusammen kosten sie 18 Goldbarren.',
    'Gebraucht wird er für alle Samen außer Inferium, also ab Stufe 2 (z. B. Kohle). Gold sammelt sich nebenbei beim Sieben.'])
_q['c_sifter'][1][3] = 'Netze: String → Faden, Andesite → Feuerstein, Zinc → Eisen (Stöcke um einen Zinkbarren), Brass → Gold.'
_q['c_presse'][1].append('Tipp: Die Presse braucht einen ganzen Eisenblock. Lass vorher den Sifter laufen, dann kommt das Eisen von allein.')
_q['c_messing'][1].append('Freigeschaltet: Akt II, die Tertiumessenz und die Gold-Tausche im Inselmarkt.')
_q['c_siebfabrik'][1][3] = 'Wenn 32 &eEisenbarren&r, 16 Zinkbarren und 32 Kupferbarren von allein kommen, steht deine Fabrik.'
_q['c_siebfabrik'][1].append('Akt II ist schon seit dem Messing offen. Die Fabrik liefert das Metall dafür.')
_q['k_inject'][1].append('Weiter in Akt III: Elite-Schaltkreise, Autocrafting und die Wahl deines Weges.')
_q['m_insanium'][1][3] = ('Den Schaltkreis baust du aus Elite-Schaltkreisen und Atomlegierung. '
                          'Weiter geht es im Kapitel Mystical Agriculture: Insanium-Ernte und Sterne vom Feld.')
_q['z_weg'][1][0] = 'Zwei Wege führen zum Herz. Du musst nur einen gehen.'
_q['z_herr'][1][2] = 'Maschinen, Felder und dein gewählter Weg arbeiten zusammen. Aus einer Insel mit einem Baum ist eine Welt geworden.'
_q['z_erz'] = ('Erz ohne Sieb', [
    'Das Sieb hat dich weit getragen. Jetzt soll das Erz von selbst kommen.',
    '',
    'Wähl einen Weg, einer reicht:',
    '- &lFelder:&r Osmium-Samen (Mystical Agriculture)',
    '- &lLaser:&r die &eErz-Laserbasis&r (Industrial Foregoing)',
    '- &lBienen:&r ein &eQuartz Nest&r für Erz-Bienen (Productive Bees)'])

# 0.9.0: XP hat einen Zweck (Wegsteine kosten Erfahrung), Hinweise am Item
_q['w_start'][1].append('- Erfahrung (XP) brauchst du für Reisen mit Wegsteinen und für Verzauberungen. Wichtige Items erklären sich im Tooltip und in JEI (U).')

# 0.10.0: Koop und Tagebuchseiten
_q['w_start'][1].append('- Mit Freunden: Im Team teilt ihr den Questfortschritt, jeder holt seine Belohnungen selbst ab.')
_q['w_start'][1].append('- Jeder Meilenstein mit einer Notiz gibt eine &dTagebuchseite&r. Sammle alle 17.')
_q['w_start'][1].append('- 0.20.0: Lootr-Truhen gehören jedem Spieler einzeln. Im Team findet jeder seine eigene Beute.')
_q['w_start'][1].append('- 0.20.0: Jobs+ bringt freiwillige Berufe. Das Menü öffnest du mit der Taste „Open Jobs+ GUI“ (Steuerung → Jobs+). Dort wählst du „Start performing this job“. Die ersten 2 Berufe sind kostenlos, weitere kosten Münzen. EXP bekommst du durch die Tätigkeit des Berufs, „How To Get EXP“ zeigt die Wege.')

# ---------------------------------------------------------------------
# 0.11.0 „Die Wahl zählt“: eigene Quest je Weg, Archiv, jedes Kapitel beginnt mit seinem Problem
# ---------------------------------------------------------------------
_q['w_magie'] = ('Weg der Magie', ['Du hast den Weg der Magier gewählt. Ihre Bibliothek öffnet sich dir.', '',
    'Halte das &eErzmagier-Zauberbuch&r. Belohnung: ein Item deiner Wahl aus der Kiste der Magie, Quellsteinblöcke und ein Spiegel des Verzauberers.'])
_q['w_maschine'] = ('Weg der Maschine', ['Du hast den Weg der Maschinisten gewählt. Ihre Werkstatt steht dir offen.', '',
    'Halte den &eLoot Fabricator&r. Belohnung: ein Item deiner Wahl aus der Kiste der Technik und Messinggehäuse.'])
_q['w_felder'] = ('Weg der Felder', ['Das Erz wächst bei dir aus dem Boden.', '',
    'Halte &eOsmium-Samen&r. Belohnung: ein Item deiner Wahl aus der Kiste der Natur und viel Knochenmehl.'])
_q['w_laser'] = ('Weg des Lasers', ['Dein Strahl holt das Erz direkt aus der Leere.', '',
    'Halte die &eErz-Laserbasis&r. Belohnung: ein Item deiner Wahl aus der Kiste der Technik und Redstone.'])
_q['w_bienen'] = ('Weg der Bienen', ['Deine Bienen tragen Metall nach Hause.', '',
    'Halte eine Wabe der Eisenbiene. Belohnung: ein Item deiner Wahl aus der Kiste der Natur und zwei Simulations-Upgrades.'])
_q['z_weg'][1].append('Jeder Weg hat zusätzlich eine eigene Quest mit eigener Belohnung (Weg der Magie, Weg der Maschine). Du darfst auch beide gehen.')
_q['z_erz'][1].append('Jeder Weg hat eine eigene Belohnungs-Quest: Weg der Felder, des Lasers, der Bienen.')
_q['p_archiv'] = ('Das Archiv des Wächters', ['Siebzehn Seiten, eine Geschichte. Der Wächter hat sie für dich aufgeschrieben.', '',
    'Besitze alle 17 &dTagebuchseiten&r (sie werden nicht verbraucht).',
    'Belohnung: der &eCodex der Erbauer&r mit allen Notizen, dazu Bücherregale, ein Lesepult und Laternen für dein eigenes Archiv.'])

PROBLEME = {
    'akt1': 'Problem: Du hast eine Insel und nichts. Lösung: alles aus Erde, Kies und Holz gewinnen.',
    'akt2': 'Problem: Von Hand kommst du nicht weiter. Lösung: Strom, Maschinen und Vervielfachung.',
    'akt3': 'Problem: Zu viele Maschinen, zu wenig Überblick. Lösung: Netze, Autocrafting und Erz ohne Sieb.',
    'exdeorum': 'Problem: Kein Erz, keine Mine. Das Sieb holt alles aus Kies, Sand und Erde.',
    'landwirtschaft': 'Problem: Hunger und leere Truhen. Felder und Töpfe versorgen die Insel von selbst.',
    'create': 'Problem: Sieben kostet Zeit. Create sieht, mahlt und mischt für dich.',
    'energie': 'Problem: Maschinen brauchen Strom. Hier erzeugst und verteilst du ihn.',
    'mekanism': 'Problem: Ein Erz gibt nur einen Barren. Mekanism macht daraus bis zu vier.',
    'lagerung': 'Problem: Volle Truhen überall. Rucksäcke, Fässer und Schubladen schaffen Ordnung.',
    'ae2': 'Problem: Du findest nichts mehr. Das ME-Netz lagert, sucht und stellt her.',
    'mysticalag': 'Problem: Sieben ist endlich mühsam. Hier wächst das Erz auf dem Feld.',
    'ars': 'Problem: Nicht alles muss eine Maschine sein. Magie löst dieselben Aufgaben anders.',
    'bienen': 'Problem: Rohstoffe ohne Lärm. Bienen sammeln sie für dich.',
    'dimensionen': 'Problem: Lohe, Perlen und Sterne gibt es hier nicht. Nether und End haben sie.',
    'maschinengeist': 'Problem: Keine Monster in der Leere. Maschinen simulieren sie.',
}

# 0.21.0: Starttext neu gefasst (Spieltest: Jobs+-Taste unklar, Handbuch als Buch)
_q['w_start'] = ('Willkommen in der Leere', [
    'Unter dir nichts. Nur ein Splitter der alten Welt.',
    '',
    '&lDein Questbuch&r liegt im Inventar. Rechtsklick damit in der Hand öffnet es. Kapitel links, Quest anklicken.',
    '&lVerloren?&r Mit &e/function skyandstone:handbuch&r bekommst du Handbuch und Questbuch neu (Cheats an oder OP nötig).',
    '',
    '&lDein erster Schritt:&r Fäll den Baum (5 Stämme). Setz die Seidenraupe auf Laub.',
    '&lBelohnungen:&r Im Questbuch die Quest anklicken und abholen.',
    '&lInselmarkt:&r Tausch-Quest öffnen, Items abgeben, du bekommst eine Kiste.',
    '&lJobs+ (freiwillig):&r Das Menü öffnest du mit der Taste „Open Jobs+ GUI“. Die Taste steht unter Steuerung, Kategorie Jobs+. Dort „Start performing this job“ wählen. Die ersten 2 Berufe sind kostenlos.',
    '&lTeam:&r Jeder holt seine Belohnungen selbst ab. Markt-Kisten gibt es pro Team.',
    '',
    '&cKeine Insel, sondern eine normale Welt?&r Neue Welt anlegen und unter „Welt“ → „Welttyp“ &lSkyblock&r wählen.',
])

# 0.21.0 Fallback Felder aus Erz: Essenz im Mischer, falls der Seed-Zirkel (seedCraftingRecipes = false) blockiert
_q['z_erz'][1].append('Essenz ohne Zirkel: Certus-, Osmium- und Zink-Essenz gibt es im Create-Mischer. 4 Metall (Certus-Quarz, Osmium, Zink) plus 1 Inferiumessenz ergeben 1 Essenz.')

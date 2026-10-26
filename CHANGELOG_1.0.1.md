# Sky and Stone 1.0.1

Stand: 26.10.2026 · Basis 1.0.0 · Minecraft 1.21.1, NeoForge 21.1.264, Java 21

**Status:** Ladeprüfung im Testserver bestanden (siehe unten). Im Spiel ist 1.0.1 NICHT GETESTET.

## Fehler behoben
- **Akt I auf der klassischen Insel:** Die Insel hat weder Stein noch Wasser. Seit die Eimer aus dem Startinventar sind, gab es Bruchstein nur aus dem Sieb und Wasser nur aus dem Holztiegel, das Questbuch verlangte aber den Hammer vor dem Sieb und hatte die Tiegel als optional markiert. Neu: Sieb → Hammer → Erzbrocken; Holztiegel und Porzellantiegel sind Pflicht; das Wasserrad hängt am Holztiegel, Lohenbrenner, Bruchstein-Generator und Obsidian am Porzellantiegel. Die Texte nennen die Wege (4 Stone Pebble = 1 Bruchstein, Wasser aus Tiegel oder Teich). Gefunden von der Prüfsuite (Spiellogik), Quest-IDs unverändert.
- **„Der Speicher der Erbauer“ war nicht lösbar.** FTB Quests liest eine Strom-Aufgabe ohne `max_input` als 0, der Aufgabenbildschirm nimmt dann keinen Strom an (im FTB-Quests-Jar 2101.1.37 nachgesehen). Der Generator schreibt `max_input` jetzt immer, die Prüfsuite meldet fehlende Werte als FEHLER.
- **Pilz-Gimmick:** Rohe Pilze sind jetzt essbar (1 Hunger, immer essbar, `kubejs/startup_scripts/pilze_essbar.js`). Vorher lösten Größenänderung und die Fortschritte „Riesenpilz“/„Pilzgröße“ nie aus. Im Server-Register belegt, im Spiel NICHT GETESTET.
- **Markt:** „Dachdecker“ und „Brückenbauer“ verbrauchen feste Eichen-Items statt Item-Gruppen (Gruppen in verbrauchenden Aufgaben verletzen Projektregel 4).
- **Messing-Kiste:** eigene Farbe, fällt nicht mehr von Bossen (war eine Kopie der Goldkiste).
- **Belohnungen, die andere Quests sofort erledigten:** „Ein Dach über dem Kopf“ gibt 4 Laternen statt 8 Rahmenblöcken (die erledigten „Rahmenblöcke“). Die Zentrifuge hängt sichtbar am ersten Eisen (beide Rezepte brauchen Eisen). Der Mechanische Hammer gibt Sand statt Bruchstein (erledigte sonst „Stein aus dem Nichts“).

## Geändert
- **Startinventar:** ohne Eis, Knochenmehl, Lava- und Wassereimer. Der Bruchstein-Generator kommt nach dem ersten Eisen (Eimer) und den Tiegeln, der Hammer nach dem Sieb.
- **Akt I:** 5 statt 8 Stämme, 8 Erzbrocken für 2 Eisenbarren, kürzere Start-Quest mit JEI-Hinweis (R/U), Faden-Zahlen für String Mesh und Flint Mesh, Andesite-Casing-Hinweis plus 2 Casings beim Wasserrad, Porzellan-Rezept beim Lava-Tiegel, Namen wie im Spiel (Silkworm, Crook, Flint Mesh).
- **Wither:** 8 Erfahrungsfläschchen statt 2 Netherit-Schrott (Entscheidung Leon).
- **Holzkiste:** ohne String Mesh (übersprang die Faden-Schranke).
- **Lagerfeuer-Partikel** erscheinen beim Spieler, Pilz-Text in der Aktionsleiste.

## Neu
- **Lootkisten mit Tooltip:** Jede Kiste zeigt eine Zeile Stimmung und woher sie kommt (Questbuch, Monster, Bosse). Die Herkunft prüft der Generator gegen die Drop-Gewichte.
- **Erinnerungsstücke des Wächters:** Jede Ruinen-Truhe enthält eins von vier Fundstücken (Inselkarte, Liedscherbe, Wappen, Namensschild) mit Story-Zeile. Reiner Flavour, die übrige Beute bleibt gleich.
- **Drei neue Prüfungen der Leere:** „Die Festung räumen“ (50 Wither-Skelette), „Schattenjagd“ (32 Enderman), „Ein Netz ohne Ende“ (1 Milliarde FE). 188 Quests.

## Werkzeuge (nicht im Paket)
- `_src/testlauf.py`: Sync, Serverstart mit Eingabe-Pipe, Log-Prüfung, sauberer Stopp. Bericht `_src/pruefung/bericht/TESTLAUF.md`.
- `_src/ki_frage.py`: Zweitmeinung über das lokale KI-Gateway FreeLLMAPI (Modell `fusion` = mehrere Modelle plus Richter).
- Prüfsuite: Textprüfung (Farbcodes, Zahlen im Text gegen die Aufgabe, Textstil), Sperrliste gegen den neuen `_src/questindex.json`, Testserver-Log, Essbarkeit für `foodEaten`, Strom-Aufgaben. Register-Dump `zz_dev_pruefdaten.js` im Testserver.

## Prüfung (26.10.2026, 13:00–13:10)
- Testlauf `_src/testlauf.py`: Done (2.499s), KubeJS Startup 2/2 und Server 14/14 ohne Fehler, 0 fehlgeschlagene Rezepte, FTB Quests 20 Kapitel / 188 Quests / 8 Tabellen, 0 neue ERROR-Zeilen.
- Prüfsuite voll: 0 Fehler, 9 Warnungen (alle bekannt seit 25.10.: Einsatzgerät, Walzwerk, Mekanism-Maschinen für Polonium/Antimaterie, Netherit-Vorlage, Zwiebeln), 53 Hinweise, 3 akzeptiert. Selbsttest 213 OK.
- Quest-IDs: 0 entfallen, 3 neu. Export `Sky and Stone-1.0.1.mrpack` (7,5 MB, lokal).
- Details: `IMPLEMENTATION_LOG.md`, Einträge 26.10.2026 (Mittag, 13:10).

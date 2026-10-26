# Playtest Sky and Stone 0.11.0

Stand: 25.10.2026 · Eine normale erste Spielsession (1,5–2 h), keine Messkampagne. Werte einfach unten eintragen. Alles mit ____ ist noch **nicht gemessen**.

**Vorher:** Prism öffnen, Instanz „Sky and Stone“ starten. Der Pre-Launch holt 0.11.0 automatisch (kurzes packwiz-Fenster). RAM: 5 GB (Laptop 5–6 GB ok). Sichtweite 8, Simulation 6 so lassen.

## Vorbereitung (25.10.2026, vor dem Test)
- [ ] Prism-Instanz startet mit **0.11.1** (Index-Hash `8908473e…`, wie `pack.toml`). Stand 0.11.1: Index und `.mrpack` sind neu, Testserver noch nicht synchronisiert.
- [x] `bereinigung.js` (Rezept-Fehler ProductiveBees/Modularbees) steht im Index. Ohne sie erschien im Log der Fehler `honeycomb_imperial`, das Spiel lief aber weiter.
- [ ] Spark-Befehle funktionieren (`/spark tps`); Log-Pfad notieren, falls leer
- [ ] Testwelt: neue Welt, Welttyp Skyblock, Startinsel notieren (Abschnitt A1)

**Offene Fragen:** 36 Felder in den Abschnitten A bis I. Priorität für den Test:
1. **A5 und A6:** Zeit bis zum ersten Eisenbarren (Ziel 25–40 min) und Klarheit der nächsten Schritte. Das entscheidet über das Frühspiel.
2. **D:** Leistung (TPS, RAM, FPS). Bisher nichts gemessen.
3. **I:** Wahlen Akt III. Die Notiz `Analyse Revolution` vermerkt, dass die Wahlen ohne Folgen sind. Ob das als Mangel auffällt, zählt.
4. **B6:** Hexenwasser-Lava-Schritt. Bisher nur aus JEI-Rezeptdaten geprüft, nicht im Spiel.
5. Rest nach Zeit. Felder ohne Antwort bleiben leer, nicht schätzen.

**Nicht geprüft** (aus NIGHT_REPORT): Client-Start mit 0.8.0 und 0.11.0, Koop, Leistung auf dem Zielgerät.

## A. Erste 30 Minuten
1. Neue Welt → „Weitere Weltoptionen“ → **Welttyp: Skyblock** → Anpassen → eine der 6 Startinseln wählen. Gewählt: ____
2. Startinventar prüfen: Questbuch, Crook, Gießkanne, Fackeln, Brot, Lava-/Wassereimer, Eis, Knochenmehl, 2 Setzlinge.
3. Questbuch: Start-Quest erledigt sich sofort. **Belohnung selbst abholen** (Holzkiste + Silkworm). Klappt das Abholen? ____
4. Uhr starten. Weg: Baum → Kompostfass → Bruchstein-Generator → Stone Hammer → Faden → Sieb → Erzbrocken → **Der Funke** (4 Eisenbarren).
   - **Faden neu erklärt:** Silkworm auf Laub, voll befallenes Laub nur mit dem Crook abbauen. Stimmt das im Spiel? Wie lange dauert der Befall? ____
5. **Messen:** Minuten bis zum ersten Eisenbarren: ____ (Ziel ~30 min, Schätzung aus den Siebchancen 25–40 min)
6. War an jeder Stelle klar, was als Nächstes kommt? Wo nicht? ____

## B. Mystical Agriculture und Create
1. Inferiumessenz kommt jetzt direkt aus dem Erd-Sieb, die **Samen an der Werkbank** (kein Altar nötig). Hat das funktioniert? ____
2. Prudentium: Infusionskristall bauen (Diamant + 4 Prosperiumsplitter + 4 Inferium). Wann hattest du den Diamanten? ____
3. Create: Wasserrad → Mahlstein → **Sifter (vor der Presse)** → Presse. Kam das Eisen für die Presse schon aus dem Sifter? ____
4. **Zinc Mesh** an der Werkbank (Stöcke + Zinkbarren) und im Sifter einsetzen: geht das? ____
5. **Mühlstein mit Stein** füttern: kommen Kiesel heraus (in 0.6.4 kam nichts)? ____
6. Lohenbrenner über Netherrack (Myzel → Hexenwasser + Lava). Wie genau kommt die Lava ins Fass? Bitte in JEI nachsehen und notieren: ____
7. Messing herstellen. Hänger/Wartezeiten: ____

## C. Freies Spiel
- Ein Kapitel unter „Abseits des Weges“ oder im „Handbuch der Mods“ ausprobieren (z. B. Baumeister, Bienen, Ars Nouveau). Welches? ____
- Fühlt sich Bauen/Experimentieren neben der Hauptstory richtig an? ____
- Akt III kündigt zwei Wahlen an („Maschine oder Magie“, „Erz ohne Sieb“). Klingt das verständlich? ____

## D. Laptop-Leistung (nach ca. 10 Minuten aktivem Spiel)
- `/spark tps` → TPS: ____ (Ziel 20)
- `/spark health --memory` → RAM: ____ % (Ziel unter 80 %)
- `/spark gcmonitor` kurz laufen lassen → Auffälligkeiten: ____
- F3 → FPS: ____
- Ausgaben stehen auch in `%APPDATA%\PrismLauncher\instances\Sky and Stone\minecraft\logs\latest.log`.

## E. Wirtschaft (falls Zeit, sonst nächste Session)
- Nach ca. 1 h: Mob-Beutekisten bekommen: ____ · Inselmarkt genutzt? ____
- Ab wann ersetzt die erste Ressourcen-Saat das Sieben? ____ · Tertium (4 Prudentium + Messing im Mixer) fair? ____


## F. Neu in 0.8.0
- Belohnungen: Kommt bei Meilensteinen eine **echte Kiste** ins Inventar, und lässt sie sich öffnen? ____ Bei „Der Funke“ eine **Auswahl** aus der Eisenkiste? ____
- Passen die Item-Belohnungen zum nächsten Schritt? Was fühlt sich nutzlos an? ____
- Gießkanne statt Ducken: reicht das Wachstumstempo? ____
- Aufgabenbildschirm (Eisen, Glas, Redstone) herstellbar? ____ (für „Der Speicher der Erbauer“)
- Deko-Tausch (64 Dachblöcke): werden die Blöcke beim Abgeben richtig abgezogen? ____

## G. Neu in 0.9.0
- Beim ersten Betreten: Erscheint die Begrüßung im Chat? ____
- Tooltip am Crook / an der Seidenraupe sichtbar? JEI-Infoseite bei Netherrack (U)? ____

## H. Neu in 0.10.0
- Ruine mit Schild auf deiner Startinsel sichtbar und lesbar? ____
- Questbuch heißt „Tagebuch der Erbauer“? Tagebuchseite nach „Der Funke“ bekommen? ____
- Erfolgs-Einblendung oben rechts beim ersten Sieb? ____
- Tooltip „Questbuch: …“ an einem Aufgaben-Item? ____

## I. Neu in 0.11.0 (später im Spiel)
- Kapitel-Untertitel beginnen mit „Problem: …“ – hilft das bei der Orientierung? ____
- Weg-Quest nach Erzmagier-Buch bzw. Loot Fabricator: Auswahl-Kiste öffnet sich? ____
- Archiv: Werden die Tagebuchseiten als Aufgabe erkannt? Codex lesbar? ____

## Was schon geprüft ist (ohne Spieltest)
- Testserver 0.8.0: 7/7 Skripte, 0 fehlgeschlagene Rezepte, 180 Quests geladen, neue Formate werden byte-gleich zurückgespeichert. FTB Quests speichert das Buch byte-gleich zurück.
- Client-Start mit 0.6.4 ohne neue Fehler (Log 25.10. 02:00). 0.8.0 im Client noch **nicht** gestartet.

## Notizen
-

## Ergebnis Spieler 1 (25.10.2026)
- Startinsel: Standard (Klassisch).
- Eisenbarren nach Schätzung: 10 bis 25 min (nicht gemessen).
- Jobs+: Erklärung war nicht verständlich, Taste unklar. Starttext neu, Taste unter Steuerung → Jobs+.
- TPS /spark tps: 20, 20, 16, 19, 19.
- Vorschlag des Spielers: 1 oder 2 gute, etwas größere Inseln ohne wichtige Items. Umgesetzt: 2 Inseln (Klassisch, Waldlichtung). Klassisch ist mit 143 Blöcken klein, Lichtung ist größer.

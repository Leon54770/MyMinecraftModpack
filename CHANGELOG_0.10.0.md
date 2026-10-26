# Sky and Stone 0.10.0

Stand: 25.10.2026 · Basis 0.9.0 · Ziel: Das Pack soll sich wie ein eigenes Spiel anfühlen.

## Neu
- **Tagebuchseiten:** Jeder der 17 Story-Meilensteine gibt eine leuchtende Tagebuchseite (Papier mit Titel und Notiz als Beschreibung, „Seite 4 von 17“). Zum Sammeln und Ausstellen.
- **Ruinen der Erbauer:** Jede der 6 Startinseln hat am Rand eine verfallene Säule mit gewachstem Schild („Hier wachte der letzte Wächter. Folge dem Buch.“).
- **Eigene Namen:** Questbuch heißt „Tagebuch der Erbauer“, Beutekisten „Kiste der Leere“.
- **Quest-Tooltips:** An 195 Items steht, wofür sie im Questbuch gebraucht werden („Questbuch: Messing (Akt I)“). Erzeugt der Generator selbst, bleibt also immer aktuell (`kubejs/client_scripts/quest_tooltips.js`).
- **Themen-Kisten:** Kiste der Magie (Ars), der Technik (Create, Strom, Mekanism, AE2, Lager) und der Natur (Landwirtschaft, Bienen) in den Mod-Kapiteln statt allgemeiner Holz-/Eisenkisten.
- **12 Erfolge mit Einblendung** entlang der Geschichte: „Was die Leere zurückgibt“, „Der Funke“, „Messing“, „Die Maschinen erwachen“, „Der Wächter am Ende“, „Der Herzschlag“ …
- **Koop:** Start-Quest erklärt, dass ein Team den Fortschritt teilt und jeder seine Belohnungen selbst abholt.

## Gemessen
- Lasttest auf dem Laptop (Testserver, 140 Tiere/Bienen auf einer Plattform): 20 TPS, Tick-Median 1,5 ms, 95 % unter 3,4 ms, CPU 1–2 %. Ohne Grafik – FPS im Client sind noch offen.

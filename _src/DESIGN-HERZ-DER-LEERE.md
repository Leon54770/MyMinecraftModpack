# Design: „Die sieben Splitter“ – neue Hauptstory-Wirbelsäule (Version 1.1.0)

Stand: 26.10.2026 · Auftrag Leon: „Ich will eine geile Quest, in der die ganzen Mods und Funktionen gut integriert sind. Brainstorme, dann setz es ohne Eingabe von mir um.“

## 1. Problem und Ziel

**Heute:** 74 Hauptstory-Quests, fast alle „besitze Item X“, Mod für Mod nacheinander (Ex Deorum → Create → Mekanism → AE2 → Nether → End). Jede Mod steht für sich, die Story läuft nur als Notizen nebenher. Es gibt kein Ziel, auf das man hinarbeitet, und kaum Momente, an die man sich erinnert.

**Ziel:** Ein roter Faden von der ersten Minute bis zum Finale, bei dem
- jeder Akt auf ein **greifbares Story-Objekt** hinausläuft, das nur entsteht, wenn **mehrere Mods zusammenarbeiten** (Rezept in der Maschine einer Mod, Zutaten aus zwei bis drei anderen);
- es **Momente** gibt: eine Entdeckung (fremde Insel), ein Bosskampf mit eigenem Gegner, ein sichtbares Finale in der Welt;
- Technik und Magie **gleichwertig** bleiben: Wo ein Splitter Magie verlangt, gibt es einen Technik-Weg, und umgekehrt;
- der Spieler **etwas tut** (fliegen, finden, kämpfen, bauen), nicht nur Items abhakt.

**Nicht-Ziele:** keine neuen Mods, keine neue Dimension, keine Grind-Pflicht, keine Wirtschaft. Bestehende Quests bleiben (Quest-IDs = Fortschritt), sie bekommen nur ein Ziel.

**Anti-Ziele (wäre ein Fehlschlag, auch wenn es technisch läuft):** ein Splitter, der nur „noch ein Item mehr“ ist; Rezepte, die eine spätere Stufe überspringen; ein Boss, der in die Leere fällt oder die Insel zerstört; Story-Texte, die erklären statt zeigen.

## 2. Leitidee

> Das Herz der Leere ist nicht tot, es ist zersprungen. Seine sieben Splitter stecken in dem, was die Erbauer hinterlassen haben: im Boden, im Feuer, im Strom, in ihren Netzen, im Leben, im Geist und in der Leere selbst. Wer alle sieben zusammenfügt, kann das Herz wieder schlagen lassen. Der letzte Wächter wird prüfen, ob du es wert bist.

Jeder Splitter ist ein eigenes Item (KubeJS), hergestellt in der Maschine einer Mod mit Zutaten aus anderen Mods. Die Splitter sind die Akt-Meilensteine. Zusammen ergeben sie das **Herz der Leere** (Block). Auf dem **Herzsockel** platziert und mit einem Netherstern geweckt, ruft es den **letzten Wächter** (Bosskampf). Danach schlägt das Herz: Finale, Feier in der Welt und ein täglicher „Herzschlag“ als Belohnung für das Endspiel.

## 3. Die sieben Splitter

| # | Splitter | Akt | Maschine (Mod) | Zutaten aus | Technik/Magie |
|---|---|---|---|---|---|
| 1 | Splitter der Erde | I (nach der Siebfabrik) | Create-Mixer, beheizt | Ex Deorum (Kies, Sand, Staub), Mystical Agriculture (Prudentium), Create (Messing) | beides |
| 2 | Splitter der Glut | II (nach den Lohenruten) | Create-Mixer, überhitzt (Lohenkuchen) | Nether (Lohenrute, Magmacreme), Ex Deorum (Netherrack), Splitter-Rohling | Technik |
| 3 | Splitter des Stroms | II (nach der Infundierten Legierung) | Powah Energizing Orb | Mekanism (Osmium, Legierung), Create Crafts & Additions (Kupferspule), Redstone | Technik, führt Powah in die Hauptstory |
| 4 | Splitter der Ordnung | II (nach dem ME-Netz) | AE2 Gravurmaschine | AE2 (Fluix-Block, Prozessoren), Mekanism (Grundschaltkreis) | Technik |
| 5 | Splitter des Lebens | III (nach Imperium) | Farmer's Delight Kochtopf | Productive Bees (Honigleckerli), Mystical Agriculture (Imperium), Farmer's Delight, Goldener Apfel | Natur |
| 6 | Splitter des Geistes | III (nach dem Wither) | **entweder** Ars Nouveau Verzauberungsapparat **oder** Industrial-Foregoing-Auflösungskammer | Ars: Quellstein, Wilden-Teile · Technik: Hostile-Networks-Vorhersagen, Latex | Wahl Magie/Technik |
| 7 | Splitter der Leere | III (nach dem Drachen) | **entweder** Mekanism-Nukleosynthesizer (Antimaterie) **oder** Mystical-Agriculture-Erweckungsaltar | Drachenatem, Leerenessenz, Shulkerschale | Wahl Technik/Magie |

Dazu zwei Zwischenstoffe:
- **Splitter-Rohling** (Werkbank): 4 Glas um eine Amethystscherbe ergibt 2. Die Hülle, in die jeder Splitter gegossen wird. Ab Akt I (Amethyst: Flint Mesh auf Crushed Deepslate).
- **Leerenessenz**: fällt von Endermen (eigener Loot-Pool, ca. 35 %). Drei Wege: kämpfen (Better Combat), Mobfarm (Industrial Foregoing, Create), Drygmy (Ars, nutzt die Loot-Tabelle). Gebraucht für Splitter 5–7 und das Herz.

**Mengen** (Entwurf, nach Spieltest nachjustieren): je Splitter 1 Stück, Rezepte mit kleinen Mengen, Zeitaufwand entsteht durch die Kette, nicht durch Masse.

## 4. Momente

1. **Die vergessene Werkstatt (Akt II).** Belohnung von „Über der Leere“ (Jetpack): eine **Karte der Werkstatt**. Rechtsklick in der Oberwelt setzt eine Ruineninsel (eigene NBT-Struktur) 80 Blöcke in Blickrichtung, 10 Blöcke höher, und sagt die Koordinaten an (80 statt 120, damit die Chunks sicher geladen sind). Darauf: zerbrochene Werkstatt, ein **zerbrochener Herzsockel** (Deko-Block, Beobachten-Aufgabe), eine Lootr-Truhe mit Story-Fund (Tagebuchseite, Leerenessenz, Splitter-Rohlinge). Hinkommen: Jetpack, Brücken (Macaw's Bridges), Bauen. Quest „Die vergessene Werkstatt“: den Sockel ansehen.
2. **Splitter-Feiern.** Jeder Splitter löst beim ersten Mal ein Advancement mit Titel, Ton und Tagebuch-Zeile aus (bestehendes Feier-System).
3. **Der letzte Wächter (Finale).** Herz auf Herzsockel, Rechtsklick mit Netherstern: Blitz, Bossleiste, ein **riesiges Wither-Skelett** (Pehkui, Größe 2,5), 400 Leben, Netheritschwert. Phasen: bei 66 % und 33 % ruft er Leerenschatten (Endermiten/Vexe). Fällt er unter den Sockel, holt ihn das Skript zurück. Sieg: Drop **Wächterkern**, Herz wechselt auf „erwacht“ (leuchtet), Fortschritt „Das Herz schlägt“.
4. **Das Herz schlägt (Endspiel).** Das erwachte Herz gibt einmal pro Minecraft-Tag per Rechtsklick dem ganzen Team einen Herzschlag (Eile II, Regeneration I, Glück, 10 min) mit Ton und Partikeln. Kein Fortschritts-Item, nur Komfort.

## 5. Questbuch

- Neue Quests in den Akt-Kapiteln (neue Schlüssel, keine alten IDs fallen weg): `s_rohling`, `s_erde`, `s_glut`, `s_strom` (+ `s_orb` Powah-Einstieg), `s_ordnung`, `s_essenz`, `s_leben`, `s_geist`, `s_leere`, `h_karte`, `h_werkstatt`, `h_sockel`, `h_herz`, `h_wache`, `h_erwacht`.
- Akt-Abschlüsse hängen an den Splittern: Akt I endet mit dem Splitter der Erde, Akt II mit der Werkstatt und den Splittern 2–4, Akt III führt über 5–7 zum Herz.
- Finale `z_herr` hängt zusätzlich an `h_erwacht`.
- Aufgabentypen neu im Generator: `observation` (Block ansehen), `advancement` (Bosskampf, Herz erwacht).
- Texte nach TEXTSTIL, Story-Notizen für jeden Splitter (Tagebuch des Wächters).

## 6. Technik (Umsetzung)

- `kubejs/startup_scripts/herz_items.js`: Items (7 Splitter, Rohling, Leerenessenz, Karte, Wächterkern) und Blöcke (Herz der Leere mit Zustand erwacht, Herzsockel, zerbrochener Herzsockel).
- `kubejs/assets/skyandstone/textures/...`: eigene 16×16-Pixel-Art, erzeugt von `_src/texturen.py` (reines Python, eigener PNG-Schreiber). Modelle, Blockstates, `lang/de_de.json`, `en_us.json`.
- `kubejs/server_scripts/herz_rezepte.js`: alle Rezepte als Mod-JSON (`event.custom`), Formate aus den Mod-Jars.
- `kubejs/server_scripts/herz_ritual.js`: Karte (Struktur setzen), Herz wecken, Boss-Logik (Tick: Bossleiste, Phasen, Rückholung), Tod → Kern + Zustand + Advancement, Herzschlag mit Abklingzeit (persistentData).
- `kubejs/data/skyandstone/structure/werkstatt.nbt` aus `_src/inseln.py` (gleicher NBT-Schreiber), Loot `loot_table/werkstatt/fund.json`.
- `kubejs/data/minecraft/loot_table/entities/enderman.json`: Vanilla-Tabelle + Pool Leerenessenz.
- Advancements: `splitter_*`, `herz_erwacht`, `waechter_besiegt`.
- Generator: `observation`/`advancement` in `questlib.py`, neue Quests in `quests.py`, Texte in `texte_herz.py`, Belohnungen, Sperrliste (Splitter und Herz nie als Belohnung).
- Prüfung: Testlauf mit Befehlen (Items geben, Struktur setzen, Boss beschwören per Funktion, Log ohne Fehler), Rezept-Dump prüft, dass jedes neue Rezept geladen ist, volle Prüfsuite (Rezeptmodell sieht die neuen Rezepte).

## 7. Risiken und Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|---|---|
| Rezeptformat falsch → Rezept fehlt still | Rezept-Dump nach dem Lauf: jedes Splitter-Rezept muss drin sein (Prüfschritt) |
| Boss fällt in die Leere / despawnt | Persistenz, Rückholung unter Sockel-Höhe −20, Bossleiste nur solange er lebt |
| Boss zerstört Insel | Wither-Skelett zerstört keine Blöcke (kein Wither) |
| Struktur überschreibt Inseln anderer Spieler | Das Skript prüft jeden Block im Zielfeld (13×14×13) auf Luft, sonst Hinweis und die Karte bleibt erhalten |
| Stufen-Sprung durch Splitter-Zutaten | Zutaten nur aus Stufen, die die Quest voraussetzt; Prüfsuite (Spiellogik) prüft das |
| Client-Grafik/Tooltips ungetestet | ehrlich als NICHT GETESTET melden, Testplan für Leon |

## 7a. Umsetzungsstand (26.10.2026)
- Erzählerischer Dreh: Der Verfasser des Tagebuchs ist der letzte Wächter selbst. Er prüft dich am Ende und übergibt dir die Wacht.
- Quest-Schlüssel: `sp_*` (Splitter), `hz_*` (Herz), weil `s_` und `h_` schon belegt sind.
- KubeJS `runCommandSilent` liefert kein Ergebnis (void): Platzprüfung per Blockabfrage, Wächter-Status über das Scoreboard.
- Abbruch-Logik: Stirbt der Wächter nicht durch einen Spieler (Lava, Leere), beendet `waechter/abbruch` den Kampf nach 3 s; ein neuer Netherstern ruft ihn wieder.
- Zweitmeinung FreeLLMAPI (`_src/KI-PRUEFUNG/ANTWORT-2026-10-26-hauptstory.md`): bestätigt Rekonstruktion statt Töten und gekreuzte Rezepte. Abgelehnt: Schwerkraftverlust, Void-Explosion, Supremium als AE2-Strom (zu riskant/grindig). Gemerkt für später: zweiter Boss in den Nether-Festungen.

## 8. Offen für den Spieltest
Mengen der Splitter-Rezepte, Leerenessenz-Chance, Bosswerte (Leben, Schaden), Entfernung der Werkstatt.

# Sky and Stone 0.5.0 – Zielkonzept (aus dem ChatGPT-Auftrag)

Stand: 25.10.2026 · Basis 0.4.1 · Arbeitskopie `modpacks/_work-sky-and-stone`, Übernahme ins Pack erst nach Testserver-Lauf.

## A) Audit: Was 0.4.1 schon erfüllt (nicht doppelt bauen)
- Stufen-Sperren Create → Mekanism → AE2 über Mystical Agriculture (balance.js), Pipez-Upgrades, TIAB 8-fach
- 15 Kapitel, 185 Quests, Äste statt Schlauch, Meilenstein je Kapitel, optionale Kapitel (Bienen, Baumeister, Markt)
- Messing vor dem Nether (Lohenbrenner aus Lohenpulver), Endportalrahmen-Rezept, Shulker/Wilden/Spawneier per Sieb
- Mob-Kisten (~1,1 %/Monster, Bosse immer), Inselmarkt mit Abklingzeiten, Leere-Rettung, Backups
- Erste Fabrik (c_siebfabrik), Netzstrom (s_reaktor), Nie wieder sieben (m_niemehr), Lagerhaus/Autocrafting (l_auto) gibt es schon

## B) Gefundene Probleme (priorisiert)
| # | Problem | Ursache | Auswirkung | Lösung |
|---|---|---|---|---|
| 1 | Insanium braucht nur Supremium + Infusionskristall | Original-Rezept Agradditions | Das Endgame führt keine Systeme zusammen, Stufe 6 kommt „gratis“ nach AE2 | Insanium = 4 Supremium um 1 Mekanism-Ultimate-Schaltkreis → 2 Insanium (balance.js). Verbindet MA-Endgame mit Mekanism-Endgame |
| 2 | Sternkiste enthält 8 Imperium-Essenz | Belohnungstabelle | Sternkisten gibt es schon vom Wither (Boss-Drop) oder vom Erzmagier, also vor Mekanism → umgeht die Imperium-Sperre | Imperium raus, dafür 32 Prudentium + Elytra (in der Leere sonst nicht erhältlich, keine Endstädte) |
| 3 | Mehrspieler: Tausch-Quests | Belohnungen gelten pro Spieler | Im Team holt jeder Spieler bei jeder Wiederholung eine eigene Kiste | Markt-Belohnungen als Team-Belohnung (`team_reward`) |
| 4 | Keine Story | – | Kein roter Faden | Story „Das Herz der Leere“: kurze Lore-Zeilen an ~14 Meilensteinen |
| 5 | Ars Nouveau ist ein Insel-Kapitel | Keine Quests, die Magie als Alternative zeigen | Technik ist immer der einzige Weg | 3 Alternativ-Quests: Zerkleinern per Zauberturm (Crush), Wixie-Autocrafting, Whirlisprig-Wachstum |
| 6 | Finale ist nur eine Sammelliste | z_herr = Haken nach Abhängigkeiten | Kein echter Abschluss | Produktions-Meilenstein „Die ewige Fabrik“, optionale Herausforderung, Finale „Erbe der Ewigkeit“ mit Lore |
| 7 | Keine optionalen Herausforderungen/Sammelquests | – | Wenig Langzeitziele für Fortgeschrittene | Neues optionales Kapitel „Prüfungen der Leere“ (Ingenieursprüfungen, Herausforderungen, Sammlerbuch) |

Bewusst **nicht** umgesetzt (aus dem Auftrag):
- Keine neuen Mods, keine neuen Startinseln, keine Tick-/Welt-Skripte
- Keine Rezeptkostensteigerungen außer #1 (Gefahr von künstlichem Grind)
- Keine Bauform-Pflichtquests: Prüfungen sind Haken-Quests mit klarer Selbstprüfung
- Kein Wettbewerbssystem (bräuchte Mods oder Skripte); Teamhinweise im Willkommens-Kapitel reichen

## C) Story „Das Herz der Leere“
Die Erbauer verbanden Maschinen und Magie und zapften das Herz der Leere an, eine Energiequelle unter der Welt. Als sie zu viel nahmen, zerbrach die Welt in schwebende Inseln. Der letzte Wächter hinterließ Notizen. Der Spieler baut ihre Technik nach und entscheidet am Ende, ob er das Herz beherrscht oder versiegelt.
Lore steht als kursive Zeile (&o) oben in der Beschreibung des Meilensteins, höchstens 2 Sätze.

## D) Neue/geänderte Quests (Schlüssel bleiben stabil)
- Ars: `a_crush` „Der andere Weg: Zerkleinern“ (Glyphe Crush + Zauberturm), `a_wixie` „Magisches Autocrafting“ (Wixie + Kessel), `a_whirli` „Whirlisprig“
- Ende: Kapiteltitel „Das Herz der Leere“, neu `z_fabrik` „Die ewige Fabrik“ (8 Ultimate-Schaltkreise, 64 Supremium, 4 Nethersterne), `z_versiegeln` (optional), `z_herr` heißt jetzt „Erbe der Ewigkeit“ (Schlüssel bleibt)
- Neues Kapitel `pruefungen` „Prüfungen der Leere“ (Gruppe Freizeit, alles optional): 4 Ingenieursprüfungen, 3 Herausforderungen, 4 Sammlerbuch-Quests

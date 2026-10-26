# Abschlussbericht Sky and Stone 0.5.0

Stand: 25.10.2026 · Grundlage: ChatGPT-Auftrag „Progression, Quests, Balance & Spielerlebnis“ · Konzept: `KONZEPT-0.5.md`
Sicherung vorher: `modpacks/_backups/sky-and-stone-0.4.1-20261025-0037/` · Arbeitskopie: `modpacks/_work-sky-and-stone/` (kann gelöscht werden)

## 1. Wichtigste Probleme
1. Insanium (Stufe 6) brauchte nur Supremium + Infusionskristall, das Endgame führte also keine Systeme zusammen.
2. Die Sternkiste enthielt Imperium und ist schon vom Wither oder Erzmagier zu haben, also vor Mekanism. Damit ließ sich die Imperium-Sperre umgehen.
3. Im Team holte jeder Spieler bei jedem Markt-Tausch eine eigene Kiste (Vervielfältigung).
4. Es gab keine Story und kein echtes Finale (nur einen Haken nach einer Sammelliste).
5. Ars Nouveau war isoliert, Magie war nirgends eine Alternative zur Technik.
6. Es gab keine optionalen Langzeitziele für Fortgeschrittene.

Schon in 0.4.1 erfüllt und deshalb nicht neu gebaut: Stufen-Sperren, verzweigte Kapitel, Siebfabrik/Netzstrom/Nie-wieder-sieben/Autocrafting-Meilensteine, Inselmarkt, Mob-Kisten, Leere-Rettung, Backups.

## 2. Umgesetzt
- **Balance:** Insanium = 4 Supremium + Ultimate-Schaltkreis → 2. Pro Insanium braucht man jetzt weniger Supremium, dafür kommt Mekanism-Endgame dazu.
- **Belohnungen:** Sternkiste mit 32 Prudentium und einem verzauberten goldenen Apfel statt 8 Imperium. Markt-Kisten gibt es einmal pro Team.
- **Magie:** Neues Rezept für die Glyphe Crush (Sand → Staub). Ein Zauberturm ersetzt damit die Hammerkette.
- **Quests:** Neue Quests a_crush, a_wixie und a_whirli. Finale: z_fabrik „Die ewige Fabrik“ (Items nur vorzeigen), z_versiegeln (optional), z_herr heißt jetzt „Erbe der Ewigkeit“. Neues optionales Kapitel „Prüfungen der Leere“ mit 12 Quests.
- **Story „Das Herz der Leere“:** 14 kursive Lore-Zeilen an Meilensteinen plus Lore im Finale.

## 3. Geänderte Dateien
`kubejs/server_scripts/balance.js` · `_src/quests.py` · `_src/questlib.py` (team_reward) · `config/ftbquests/quests/**` (neu erzeugt) · `pack.toml` (0.5.0) · `README.md` · neu: `_src/KONZEPT-0.5.md`, `_src/BERICHT-0.5.md`

## 4. Bewusst nicht umgesetzt
- Keine neuen Mods, keine neuen Startinseln, keine Tick-Skripte (Laptop-Leistung)
- Keine weiteren Rezeptverteuerungen, weil es keinen belegten Grund gibt (Gefahr von künstlichem Grind)
- Kein Wettbewerbssystem, weil es mit FTB Quests allein nicht sauber geht
- Gemini-Vorschläge verworfen: Insanium sei zu teuer (falsch, pro Insanium braucht man weniger Supremium), Crush-Rezeptformat (falsch, so schreibt Ars die Rezepte selbst)

## 5. Tests
- `python -I _src/quests.py`: 16 Kapitel, 202 Quests, 0 Fehler bei der Item-ID-Prüfung
- Überlappungs-Check: 0
- Testserver: 5/5 KubeJS-Skripte, 0 Fehler, 244 Rezepte hinzugefügt / 46 entfernt, 0 fehlgeschlagen, FTB Quests lädt 16 Kapitel/202 Quests
- Export `Sky and Stone-0.5.0.mrpack` enthält das neue balance.js und alle 16 Kapitel, aber kein `_src`
- Gemini hat 3 Mal geprüft (Konzept, Technik, Ars-Funktionen) und wurde gegen die Mod-Dateien gegengeprüft

## 6. Offen / Spieltest nötig
- Nicht getestet: Client-Start, Darstellung der kursiven Lore (&o), Layout des neuen Kapitels
- Wixie-Autocrafting und Crush-Turm im Spiel ausprobieren (Quests sind so beschrieben, wie die Mod laut Rezepten arbeitet)
- Ob Insanium mit 1 Schaltkreis pro 2 Essenz im Spiel angenehm ist (sonst Ausbeute auf 4 erhöhen)
- Leistung am Laptop (spark) bleibt der wichtigste Test

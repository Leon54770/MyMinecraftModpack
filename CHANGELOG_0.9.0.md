# Sky and Stone 0.9.0

Stand: 25.10.2026 · Basis 0.8.0 · Ideen teils von Gemini (`scratchpad`-Antwort geprüft, falsche Fakten verworfen).

## Neu
- **Hinweise am Item** (`kubejs/client_scripts/hinweise.js`): Tooltips und JEI-Infoseiten (U/R) für alles, was in der Leere anders läuft – Netherrack, Hexenwasser, Myzelsporen, Seidenraupe und Crook, Lohenbrenner, Endportalrahmen, Antiker Schrott, Inferium-Samen, Essenz-Stufen (Prudentium bis Supremium), Zinc Mesh, Aufgabenbildschirm, Beutekisten, Wegsteine.
- **Begrüßung** beim ersten Betreten einer Welt (`kubejs/server_scripts/willkommen.js`): kurze Story-Zeile, Hinweis aufs Questbuch und auf den Welttyp Skyblock. Einmal pro Spieler.
- **XP hat einen Zweck:** Wegsteine kosten Erfahrung (bewusst so gelassen), die Start-Quest erklärt das.

## Bewusst nicht übernommen
- Wegstein-Kosten abschalten (dann wäre XP nutzlos), Forgiving-Void-/Backup-Werte (schon passend eingestellt), Flywheel-Backend erzwingen (Standard wählt selbst), neue Story-Items per Startup-Skript (würde neue Items registrieren).

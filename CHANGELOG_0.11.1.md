# Sky and Stone 0.11.1 – Bereinigung

Stand: 25.10.2026 · Basis 0.11.0 · Nur ein Patch, keine Spielinhalte geändert.

## Behoben
- **ProductiveBees-Rezept entfernt:** `productivebees:centrifuge/modularbees/honeycomb_imperial` verwies auf `modularbees:honey_jelly`. Modularbees ist nicht im Pack, das Rezept konnte nie gebaut werden und erzeugte beim Laden einen Fehler im Log. Entfernt in `kubejs/server_scripts/bereinigung.js`.

## Geprüft
- Testserver mit 0.11.0 plus diesem Skript: KubeJS 9/9 Skripte ohne Fehler, 0 fehlgeschlagene Rezepte, Serverstart `Done (0.991s)`, Rezept-Fehler nicht mehr im Log.
- Hinweis: Das Testserver-Log zeigt weiterhin zwei Curios-Meldungen (`example`, `feet`) und Mixin-Warnungen zu nicht installierten Mods. Ungeprüft, nicht geändert.

## Nicht geändert
- Quests, Story, Balance und Startinseln sind wie in 0.11.0.

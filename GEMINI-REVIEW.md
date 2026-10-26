# Gemini-Prüfung Sky and Stone 0.2.0

Stand: 24.10.2026 · Modell: gemini-3.6-flash (mit Nachdenken), danach von Claude gegengeprüft.
Gemini-Pro ist im kostenlosen API-Kontingent gesperrt (Limit 0).

## Gemini-Urteil (kurz)
Solides, gut optimiertes Pack. Die Übertragung der Ex-Deorum-Siebe auf den Create-Sifter löst das typische Skyblock-Frühspiel elegant.
Größte Schwäche: Ohne Quests und ohne Sperren wird es schnell zur unbalancierten Sandbox.

## Gegenprüfung

| Behauptung von Gemini | Ergebnis |
|---|---|
| `event.containsRecipe` in `sieben.js` ist ungültig und lässt das Skript abstürzen | **Falsch.** KubeJS-Log: 3/3 Skripte, 0 Fehler, 236 Rezepte hinzugefügt, 0 fehlgeschlagen |
| Create-Sifter braucht `item` statt `id` | **Falsch.** In 1.21.1 ist `id` richtig, alle Rezepte werden angelegt |
| FastWorkbench/FastFurnace sind durch ModernFix überflüssig | **Falsch.** ModernFix ersetzt sie nicht, beide laufen fehlerfrei |
| Flux Networks als Ergänzung | Auf Modrinth nicht für 1.21.1 NeoForge zu finden (höchstens CurseForge) |
| Time in a Bottle bricht die Balance | **Stimmt.** Über die Config abschwächen oder entfernen |
| Mystical Agriculture + Botany Pots entwerten Sieb/Create/Mekanism schnell | **Stimmt größtenteils.** Ist so gewollt („Samen ersetzen das Sieben“), könnte aber höhere Samen hinter Technik-Stufen sperren |
| Pipez-Upgrades sind zu billig | **Plausibel.** Die Übertragung ist nicht „unendlich“, aber das Ultimate-Upgrade ist sehr stark |
| Mekanism Tools füllt JEI mit Werkzeugen, die niemand braucht | Geschmackssache |
| MEGA Cells für großen AE2-Speicher | **Sinnvoll**, auf Modrinth für 1.21.1 NeoForge verfügbar (`mega`) |
| FTB Quests fehlt | **Stimmt**, war ohnehin als nächster Schritt geplant |

Nebenbefund im Log (nicht von Gemini): Bei zwei Iron-Furnaces-Upgrade-Rezepten (Unobtainium, Vibranium) weicht KubeJS auf das Vanilla-Format aus. Das ist nur eine Warnung, die Rezepte funktionieren.

## Sinnvolle nächste Schritte
1. Time in a Bottle in der Config drosseln oder entfernen
2. Teure Pipez-Upgrades per KubeJS verteuern
3. MEGA Cells hinzufügen
4. Höhere Mystical-Agriculture-Samen hinter Technik-Stufen sperren (optional, Geschmackssache)
5. FTB Quests (eigener Schritt)

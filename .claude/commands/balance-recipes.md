---
description: KubeJS-Skripte und Rezepte im Testserver prüfen, Fehler mit Log-Beleg beheben, Ore-Unification und Quest-Rezept-Verbindungen kontrollieren
---

# Rezepte prüfen und verbinden (Sky and Stone)

Zusatzauftrag (optional): $ARGUMENTS

Ziel: Rezeptfehler und Lücken finden, mit Log-Beleg beheben. Balance nicht anfassen. Vorher `CLAUDE.md` (Abschnitt KubeJS) und `TODO.md` lesen.

## Grenzen

- Balance-Werte (Mengen, Stufen, Kistenraten, Gewichte) nur ändern, wenn ein Messwert oder ein Spieltest-Befund vorliegt. Sonst nur melden.
- Keine Mods hinzufügen oder entfernen. Das braucht Freigabe von Leon.
- `config/ftbquests` nie von Hand ändern. Quest-Änderungen nur über `_src/` und den Generator.
- Im Spiel nicht geprüft heißt NICHT GETESTET.

## Ablauf

1. **Stand festhalten.** `pack.toml` lesen (Version). Sicherung anlegen: `C:\Projekte\modpacks\_backups\sky-and-stone-<version>-vor-rezepten-<JJJJMMTT>\` mit `kubejs`, `config\ftbquests` und `_src`. Vorhandene Sicherungen nie überschreiben.

2. **Testserver synchronisieren.** Im Ordner `C:\Projekte\modpacks\_testserver-sky-and-stone`:

   ```bash
   java -jar packwiz-installer-bootstrap.jar -g -s server "file:///C:/Projekte/modpacks/sky-and-stone/pack.toml"
   ```

3. **Testserver starten und Log lesen.** Vorher die alte `logs\latest.log` sichern, sie wird überschrieben. Start im Testserver-Ordner:

   ```bash
   java @user_jvm_args.txt @libraries/net/neoforged/neoforge/21.1.264/win_args.txt nogui
   ```

   Auf `Done (` im Log warten. Danach `stop` in die Konsole schreiben und auf das Ende des Prozesses warten. Dann im Log suchen nach: `ERROR`, `Exception`, `[KubeJS]`, `failed`, `Unknown`, `Missing`. Jede Fundstelle notieren mit Zeile und Quelle.

4. **Rezepte prüfen.**
   - Fehlerrezepte, die auf ein fehlendes Item oder Mod verweisen: entfernen wie in `bereinigung.js`.
   - Ore Unification: Almost Unified ist installiert und reduziert die Tags. Keine eigene Vereinheitlichung ohne Log-Beleg.
   - Rezept-Simulation (offen, `TODO.md` Phase 1): nur mit einem Testskript im Testserver (`kubejs/server_scripts/zz_dev_*.js`). Keine Java-Reflexion, das hat schon einen RuntimeDistCleaner-Fehler ausgelöst. Das Skript nie in den Quellordner kopieren.

5. **Rezepte mit Quests verbinden.** Jedes Item, das eine Quest verlangt (`_src/items.json`), muss herstellbar oder erhältlich sein. Bei einer Lücke:
   - Fehlendes Rezept: ergänzen in `kubejs/server_scripts/luecken.js` (Muster: Endportalrahmen, Lohenbrenner).
   - Nur der Questtext stimmt nicht: Text in `_src/texte_*.py` ändern, nicht die Quest-Datei.

6. **Ändern.** Nur in `kubejs/server_scripts/` im passenden Modul. Jede Änderung bekommt einen Kommentar mit Zweck und Beleg (Log-Zeile). Entfernen nur bei fehlendem Item oder Mod (Log-Beleg) oder bei Duplikat. Balance-Abkürzungen nicht selbst entscheiden, sondern in den Bericht.

7. **Prüfen.** Testserver neu synchronisieren und starten (Schritt 2 und 3). Erwartet:
   - `Done (` im Log
   - KubeJS-Skripte ohne Fehler
   - `0 fehlgeschlagene Rezepte`
   - Quest-Anzahl unverändert (186, falls keine Quest geändert wurde)

   Wurde eine Quest oder ein Text geändert: vorher `python -I -X utf8 _src/quests.py` laufen lassen, Ergebnis `0 Layoutprobleme`.

8. **Abschluss.** Im Pack-Ordner `..\tools\packwiz\packwiz.exe refresh` ausführen. Eintrag in `IMPLEMENTATION_LOG.md`: Datei, Zweck, Prüfstatus, Rückweg (Sicherungspfad).

9. **Bericht.** Zwei Tabellen:
   - Geändert: Datei | Änderung | Grund (Log-Beleg) | Prüfstatus
   - Gemeldet, nicht geändert: Befund | Warum nicht (Balance, Entscheidung von Leon, fehlende Messung)

   Status nur mit BESTANDEN, FEHLGESCHLAGEN, BLOCKIERT oder NICHT GETESTET. Keine Aussage über Spielbarkeit.

**Abbruch:** Startet der Testserver nicht oder bricht der Lauf ab, Änderungen aus der Sicherung zurückkopieren, `packwiz refresh` ausführen und im Bericht die Fehlerzeile nennen.

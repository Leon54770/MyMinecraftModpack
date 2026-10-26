---
description: Crash-Reports und Logs der Sky-and-Stone-Instanz analysieren und KubeJS- oder Config-Fehler direkt beheben
---

# Crash analysieren und beheben (Sky and Stone)

Zusatzauftrag (optional): $ARGUMENTS (Pfad zu einer bestimmten Datei. Ohne Angabe die neueste.)

Vorher `CLAUDE.md` (Abschnitt KubeJS und Pflichtprüfung) lesen.

## Quellen, neueste zuerst

1. **Testserver:** `C:\Projekte\modpacks\_testserver-sky-and-stone\crash-reports\` (neueste Datei) und `logs\latest.log`.
2. **Prism-Instanz (Client):** `%APPDATA%\PrismLauncher\instances\Sky and Stone\minecraft\crash-reports\` und `logs\latest.log`.
3. **Ältere Logs:** `logs\*.log.gz` im Testserver. Zum Lesen nach dem Scratchpad entpacken, nicht in den Projektordner.

Testserver und Client getrennt berichten. Ein Testserver-Absturz ist kein Befund für den Client.

## Ablauf

1. **Ursache finden.** Im Crash-Report nach `Caused by` und `Mod file` suchen, im Log nach `ERROR`, `Exception`, `[KubeJS]`, `Failed to load`, `Unknown`. Die erste Ursache zählt, nicht die letzte Folgezeile.

2. **Einordnen:**
   - **KubeJS-Skript** (Fehler in `kubejs/...`): Quelle beheben in `kubejs/server_scripts/` oder `kubejs/client_scripts/`.
   - **Quest-Daten** (`config/ftbquests`): nie von Hand. Ursache in `_src/` suchen, Generator neu laufen lassen.
   - **Config** (TOML, JSON5 in `config/`): Format prüfen, ohne BOM schreiben.
   - **Mod-Fehler oder fehlende Abhängigkeit:** nicht selbst beheben. Vorschlag an Leon, Mod ersetzen oder entfernen braucht Freigabe.
   - **Rezept-Fehler:** Ablauf aus `balance-recipes` nutzen.

3. **Sichern.** Vor jeder Änderung die betroffenen Dateien nach `C:\Projekte\modpacks\_backups\sky-and-stone-<version>-vor-crashfix-<JJJJMMTT>\` kopieren. Außerdem die Crash-Datei sichern, bevor ein neuer Start das Log überschreibt.

4. **Beheben.** Minimal, eine Ursache pro Änderung. Kommentar mit Log-Zeile.

5. **Prüfen.** Testserver synchronisieren und starten (wie in `balance-recipes`, Schritt 2 und 3). Erwartet: `Done (` im Log, kein neuer Crash, keine neuen ERROR-Zeilen aus dem Pack. Höchstens drei Durchläufe. Danach stoppen und berichten.

6. **Abschluss.** Im Pack-Ordner `..\tools\packwiz\packwiz.exe refresh`. Eintrag in `IMPLEMENTATION_LOG.md`: Datei, Zweck, Prüfstatus, Rückweg.

7. **Bericht:** Ursache (Datei und Zeile), Fix, Prüfstatus, Rückweg. Ein Client-Start im Spiel ist nicht geprüft, solange Leon ihn nicht bestätigt. Dann NICHT GETESTET schreiben.

**Mods nicht selbst starten oder ändern.** Die Entscheidung über Mods liegt bei Leon.

# Projekt-Audit Sky and Stone (Stand 0.20.0, 25.10.2026)

Phase A. Grundlage: Dateien im Pack-Ordner, Testserver-Logs, bestehende Notizen. Keine Client-Tests, kein Multiplayer.

## Fakten (geprüft)
- Minecraft 1.21.1, NeoForge 21.1.264. Test lief mit Java 25.0.4 (Prompt nennt Java 21, NeoForge 21 läuft auf beiden; Java 21 ist der dokumentierte Zielstand, im Test nicht ausprobiert).
- 124 Mod-Einträge in `mods/*.pw.toml`, davon neu in 0.20.0: Lootr, Jobs+, Arc Lib, Item Restrictions, UI Lib, YAML Config.
- Questbuch: 20 Kapitel, 186 Quests, 74 Hauptstory (Generator `_src/quests.py`, Ausgabe `config/ftbquests`).
- KubeJS: 9 Server-Skripte, 0 Fehler beim Start. 247 Rezepte hinzugefügt, 50 entfernt, 0 fehlgeschlagen.
- Startinseln: 6 (`_src/inseln.py`).
- Dokumentation: README, PLAN-0.20.0.md, AUDIT-BELOHNUNGEN-0.11.md, MORGEN-PLAYTEST.md, mehrere Changelogs (0.7.0 bis 0.20.0), GEMINI-*.md und CHATGPT-*.md aus früheren Sitzungen.
- Backups: `_backups/` mit Ständen vor jeder größeren Änderung. Das Projekt ist kein Git-Repo.
- Automatisierte Tests: keine Testdateien. Die Prüfungen laufen im Generator (`pruefe_struktur`, Layout, IDs, Zyklen) und im Testserver-Start.

## Bestätigte Fehler (behoben)
- ProductiveBees verweist auf `modularbees:honey_jelly`, Modularbees fehlt. Rezept entfernt (`bereinigung.js`, ab 0.11.1).
- YAML Config war als optional eingestuft, ist für Jobs+ Pflicht. Beim Testserver-Start aufgefallen, nachgerüstet.

## Bestätigte Warnungen (nicht behoben, ungeklärt)
- Curios: Slot-Typen `example` und `feet` nicht registriert. Herkunft unklar.
- Mixin-Warnungen zu Klassen aus nicht installierten Mods (Quark, ExtendedAE, Simulated, Sable). Wahrscheinlich optionale Mixins.
- When Dungeons Arise: zwei Fortschritts-Einträge laden nicht (`find_thornborn_towers`, `find_fishing_hut`). Mod nicht übernommen.

## Designschwächen (Vermutungen, nicht im Spiel belegt)
- Zwei Wahlen in Akt III (Maschine oder Magie, Erz ohne Sieb) geben nur Belohnungen, keine spürbaren Folgen.
- Goldkiste als Wahl bei Messing und Siebfabrik enthält Diamanten und Osmium. Mögliche Abkürzung. Siehe AUDIT-BELOHNUNGEN-0.11.md.
- Sternkiste bei Riesenspeicher (AE2) mit Netherit-Barren, ein Vorgriff auf Pipez-Ultimate.
- Koop: Team-Fortschritt ist nur im Inselmarkt geregelt. Mehrspieler nicht getestet.

## Strukturelle Risiken
- Quest-IDs hängen am Kapitelnamen. Umbenennen oder Verschieben löscht Fortschritt in bestehenden Welten.
- Die Texte von Quests stehen in mehreren Modulen (`texte_hauptstory.py`, `texte_abenteuer.py`, `texte_technik.py`) und werden teils per Listenposition überschrieben. Änderungen brauchen eine Diff-Kontrolle.
- Update-Adresse der Prism-Instanz zeigt auf `file:///C:/...`, nur auf diesem PC nutzbar.
- Performance: Serverstart etwa 1 Sekunde nach dem Laden (`Done`). Client-FPS und RAM unter Last sind nicht gemessen. Zielgerät Iris Xe, 5–6 GB RAM.

## Offene Prüfungen
- Spieltest mit Prism, Client-Start, Koop, Leistung (siehe TEST_REPORT.md).


## Abnahmeprüfung 25.10.2026 (Stand 0.20.0)

Systemweite Prüfung über Dateien, Testserver-Log und Mod-Liste. Nicht geprüft: das Zusammenspiel im Spiel.

### Konflikte und Warnungen (neu gefunden)
| Befund | Einordnung | Status |
|---|---|---|
| Curios: Slot-Typen „example“ und „feet“ nicht registriert (3 ERROR-Zeilen im Log) | Ungeklärt. config/curios-common.toml steht auf `slots = []`, Quelle nicht gefunden. | Ungeklärtes Risiko, nicht behoben |
| IronFurnaces: Upgrade-Rezepte upgrade_unobtainium und upgrade_vibranium fallen auf Vanilla zurück | Format-/Mod-Konflikt (Komponente pattern&lt;optional_ingredient&gt;). Kann Rezepte verändern. | Ungeklärtes Risiko |
| ExtendedAE: Rezept advanced_ae:quantum_processor_eae nutzt Typ extendedae:crystal_assembler, der nicht registriert ist | Fehler im Mod-Zusammenspiel. Kann eine AE2-Zwischenstufe betreffen. | Ungeklärtes Risiko |
| Mixin-Warnungen zu Klassen nicht installierter Mods (Quark, ExtendedAE, Simulated, Sable) | Vermutlich optionale Mixins, nicht bewiesen | Restrisiko |
| Lithium: „Cached BlockState Flags are disabled“ | Info, kein Fehler | Kein Handlungsbedarf |
| ModernFix: Serverstart 33,988 s in diesem Lauf | Warnung, Start selbst OK | Beobachten |

### Bereits behobene Probleme (frühere Stände)
- ProductiveBees/Modularbees-Rezept (bereinigung.js, ab 0.11.1)
- YAML Config als Pflicht für Jobs+ (ab 0.20.0)

### Designrisiken (Vermutung, nicht im Spiel belegt)
- Wahlen Akt III ohne spürbare Folge (PLAN-0.20.0.md Abschnitt 5a).
- Gold- und Sternkisten als mögliche Abkürzung (AUDIT-BELOHNUNGEN-0.11.md).
- Koop: Team-Fortschritt nur im Inselmarkt geregelt.

### Strukturelle Risiken
- Quest-IDs hängen am Kapitelnamen (Verschieben löscht Fortschritt).
- Update-Adresse file:/// (P9, blockiert).

### Abnahme-Entscheidung
**NICHT VOLLSTÄNDIG ABGENOMMEN.** Im Log wurde kein kritischer Fehler und kein Progressions-Softlock gefunden. Spielbarkeit, Balance, Koop und Performance sind aber nicht belegt. Die Rezept-Fallbacks (ironfurnaces, extendedae) sind ungeklärt. Details: TEST_REPORT.md, Abschnitt „Abnahmeprüfung 25.10.2026“.

## Endstand 25.10.2026 19:12
- AdvancedAE aus dem Pack entfernt (Fehler extendedae:crystal_assembler und Mixin-Warnungen für ExtendedAE verschwunden, weil das Mod-Set jetzt konsistent ist).
- Offene Punkte aus der Vollprüfung sind entschieden und umgesetzt (siehe IMPLEMENTATION_LOG.md, Abschnitt Entscheidungen).
- Restrisiken: Zeit bis zum Eisenbarren nicht gemessen, Mob-Kisten und Markt ohne Daten, Jobs+ im Spiel nicht geprüft, vollständige Rezept-Simulation offen.

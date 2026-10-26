# Prüfbericht Sky and Stone 1.0.0

Stand: 25.10.2026, 22:30 · Prüfung von Code und Logik, ohne Serverstart und ohne Spiel. Alles, was hier „geprüft“ heißt, ist mit einem Skript oder direkt in der Datei belegt. Im Spiel ist nichts davon getestet.

## 1. Was läuft gerade
- Keine Hilfsagenten mehr (Recherche und Startsimulation sind fertig).
- Der Testserver lief seit 22:05 weiter und ist jetzt beendet. Sein letzter Start war sauber: 13/13 Skripte mit 0 Fehlern, 0 fehlgeschlagene Rezepte, `Done (1.318s)`.

## 2. Stand des Packs
- **Version:** 1.0.0 (`pack.toml`), Minecraft 1.21.1, NeoForge 21.1.264. Lokaler Export: `Sky and Stone-1.0.0.mrpack`, nicht veröffentlicht.
- **Inhalt:** 128 Mods, 3 Ressourcenpakete. 20 Kapitel, 185 Quests (74 Hauptstory, 18 optional), 8 Belohnungstabellen, 19 Tausch-Quests, 7 Feier-Belohnungen.
- **Inseln:** Klassisch (198 Blöcke) und Waldlichtung (517 Blöcke), jeweils mit Ruine und Lootr-Truhe.
- **KubeJS:** 9 Server-Skripte (Balance, Bereinigung, Gruppen, Lücken, Sieben, Willkommen, Lagerfeuer, Wächter, Pilze) und 2 Client-Skripte.
- **Datenpaket:** 26 Funktionen, 19 Fortschritte, 1 Loot-Tabelle (Ruinenfund mit Bonusseite 18).
- **Sprache:** Deutsch. `en_us.snbt` ist eine Kopie von `de_de.snbt` (gewollt, `questlib.py`).

## 3. Prüfungen und Ergebnisse

| Prüfung | Werkzeug | Ergebnis |
|---|---|---|
| Quelltext und Questdateien gleich | Generator neu laufen lassen, Hash-Vergleich | Byte für Byte gleich |
| Inseln | `inseln.py`, Inhalt entpackt verglichen | Inhalt gleich (nur der Archiv-Zeitstempel war neu, Originale zurückgespielt) |
| Questgraph | eigenes Prüfskript | 0 fehlende Voraussetzungen, 0 Zyklen, 0 Quests ohne Aufgabe, 0 Haken-Aufgaben, alle 67 Tabellenverweise gültig, alle 96 Kapitel-Verweise gültig, de/en gleiche Schlüssel |
| Layout | Generator | 0 Probleme, 25 Linienkreuzungen |
| Rezepte | `rezept-sim/analyse.py` | 240 Item-Aufgaben, 0 unerreichbar, 0 unbekannte IDs |
| JavaScript-Syntax | `node --check` | 11/11 fehlerfrei |
| Datenpaket | eigenes Prüfskript | JSON gültig, alle Funktions-, Fortschritts- und Loot-Verweise vorhanden, keine verwaiste Funktion |
| Feier-Befehle | Abgleich Quests ↔ Funktionen | alle 7 Ziele vorhanden |

Der ältere Check `erreichbar.py` meldet viele Funde, ist aber zu grob. Er hält sogar normale Mystical-Agriculture-Samen für „nicht herstellbar“. Maßgeblich ist die Rezept-Simulation.

## 4. Was nicht zusammenpasst

### Logikfehler im Code (wirken im Spiel)
1. **Pilz-Gimmick löst nie aus.** `pehkui_pilze.js` hört auf `foodEaten` für rohe rote und braune Pilze. Die sind in 1.21.1 kein Essen, und kein Skript macht sie essbar. Damit fallen auch die versteckten Fortschritte „Riesenpilz“ und „Pilzgröße“ (`consume_item`) aus. Nur die Chorusfrucht funktioniert.
2. **Lagerfeuer-Rauch am falschen Ort.** `execute as <Spieler> run particle ~ ~1 ~` ohne `at @s` setzt den Rauch am Welt-Spawn ab.
3. **Pilz-Untertitel unsichtbar.** `title @s subtitle` ohne einen Titel zeigt Minecraft nicht an.
4. **Holzkiste überspringt eine Schranke.** `holz.snbt` enthält das String Mesh. Die Kiste kommt schon aus Q1. Das verstößt gegen Leitregel 5 („Belohnungen dürfen keine Schranke überspringen“).

### Logik der Startphase (Simulation, gegen Dateien geprüft)
5. **Q2 braucht 8 Stämme**, der Klassisch-Baum hat 5 (`inseln.py`, `h=5`). Die 8 Stämme müssen gleichzeitig im Inventar liegen.
6. **Seidenraupe ist ein Einzelpunkt.** Es gibt nur 1 Silkworm aus Q1. Nachschub kommt aus dem Crook mit 1 % (im Mod-Jar geprüft). Geht der Befall verloren, gibt es kaum noch Faden.
7. **Obsidian-Falle in Q5:** keine Warnung, und es gibt nur einen Lavaeimer.
8. **Faden:** Das String Mesh braucht 9 Faden (Jar geprüft), Q3 verlangt 8. Das Flint Mesh kostet 5 Faden und 4 Feuerstein. Es ist kein Upgrade, hier lag die Simulation falsch.
9. **Eisen:** Q10 verlangt 4 Brocken, Q12 braucht 8.
10. **Q1 hat 14 Zeilen** (TEXTSTIL erlaubt höchstens 6), JEI wird nicht eingeführt.
11. **Andesite Casing** wird nirgends erklärt, obwohl sechs Create-Maschinen es brauchen.
12. **Q25 verweist auf die gestrichene Pilzinsel.**
13. **Q8 und Q9 sind Sackgassen** und nicht als optional markiert.
14. **Namen uneinheitlich:** Seidenraupe/Silkworm, Feuernetz/Flint Mesh. Im Handbuch fehlt der Crook.
15. **Balance-Verdacht:** Kupfer/Zink in Q16 brauchen rund 100–200 Kies, Inferium in Q13 rund 1300 Laub.

### Dokumente
16. README, CLAUDE.md und TODO nennen 0.20.0, das Pack ist 1.0.0.
17. GAME_DESIGN nennt 17 Tausch-Quests, es sind 19. Die Zeilen zur Gold- und Sternkiste sind durch spätere Entscheidungen überholt.
18. Die Begründung für das Streichen von 8.3 (Sieb-Fundgrube) stimmt nicht. `sieben.js` nutzt bereits Zusatzrezepte mit derselben Zutat und demselben Netz.
19. `CHANGELOG_1.0.0.md` war im Paket. Seit heute steht die Datei in `.packwizignore`, das `.mrpack` enthält sie aber noch, bis zum nächsten Export.
20. Laut BACKLOG sollten bis zur Klärung von 7.1–7.3 keine neuen Gimmicks kommen. Sprint 6 hat trotzdem welche gebracht, auf Wunsch von Leon. Kein Fehler, aber der Satz im BACKLOG ist veraltet.

## 5. Was stimmt
- Quelltext, Generator und Questdateien sind synchron.
- Keine kaputten Verweise zwischen Quests, Tabellen, Funktionen, Fortschritten und Loot.
- Jede Item-Aufgabe ist über Rezepte erreichbar.
- Belohnungsfolge: Die Messing-Kiste ersetzt die zu frühe Goldkiste, die Sternkiste ist ohne Netherit.
- Die Server-Skripte laufen mit Konsolenrechten (`Utils.server.runCommandSilent`), also auch ohne OP.

## 6. Nächste Schritte
Alle Punkte stehen in `TODO.md`, Phase 9 (9.1–9.20). Reihenfolge: zuerst A (Blocker), dann B (Code), dann C (Texte). Bei D (Balance) nur die Zahlen, die sich aus Rezepten belegen lassen. Danach Generator, ID-Prüfung, `packwiz refresh`, Ladeprüfung, neuer Export. Koop-Test und Verteilen kommen kurz vor dem Release.

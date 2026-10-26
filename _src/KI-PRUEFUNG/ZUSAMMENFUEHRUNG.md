# KI-Prüfung 0.10.0 – Zusammenführung (Gemini · ChatGPT · Claude)

Stand: 25.10.2026 · Quellen: `ANTWORT-GEMINI.md` (hat alle Dateien gelesen), `ANTWORT-CHATGPT.md` (hat **nur den Prompt** bekommen, keine Dateien – urteilt allgemein), Claude gegen die echten Dateien und Mod-Jars geprüft.

## 1. Urteil in einem Satz
Beide sehen eine starke Grundlage (Generator, Stufen-Kopplung, Wahlen, Story). Einig sind sich alle drei: **Der wichtigste nächste Schritt ist ein echter Durchlauf im Client** – erst danach große Änderungen.

## 2. Gemeldete Fehler – Faktencheck
| Quelle | Behauptung | Urteil |
|---|---|---|
| Gemini | `sieben.js`: `sieveJsons` global → Reload verdoppelt Rezepte | **falsch** – die Liste wird innerhalb des Events neu angelegt |
| Gemini | Sodium läuft auf NeoForge nicht, Embeddium nötig | **falsch** – Sodium hat eine offizielle NeoForge-Version, der Client lief damit ohne Fehler |
| Gemini | Imperium-Rezept per ID entfernen reicht nicht | **falsch** – MA hat genau dieses eine Rezept (Audit 0.7.0, Jar geprüft) |
| Gemini | `z_erz`/`m_niemehr` verwirrend | kein Fehler (in 0.7.0 per Abhängigkeitsgraph geprüft) |
| Gemini | `mipmapLevels:2` kostet auf Iris Xe Leistung | **plausibel**, kleiner Gewinn, Optik minimal schlechter → Messung im Spieltest |
| ChatGPT | Stufen könnten über andere Rezepte umgangen werden | schon geprüft (0.7.0, alle Jars): keine anderen Wege; Rückbau-Exploit behoben |
| ChatGPT | Generator könnte kaputte Referenzen erzeugen | schon abgesichert (IDs, Verweise, Zyklen, Items, Gruppen, Layout, Sperren; Rückspeicher-Test byte-gleich) |
| ChatGPT | Hilfetexte können vom Rezept abweichen | **berechtigt** (Wartung): `hinweise.js` ist von Hand geschrieben |

Kein neuer echter Fehler gefunden.

## 3. Die besten Ideen (übernehmenswert)
1. **Echter Client-Durchlauf zuerst** (alle) – `MORGEN-PLAYTEST.md` liegt bereit.
2. **Wahlen spürbar machen** (ChatGPT, „Die zwei Vermächtnisse“): Bisher schalten „Maschine oder Magie“ und „Erz ohne Sieb“ nur das Finale frei. Neu: Jeder Weg gibt eine eigene, passende Belohnung (z. B. Magie → Kiste der Magie zur Auswahl + Ars-Komfort, Maschine → Kiste der Technik zur Auswahl), und das Finale nennt den gewählten Weg. Kein Weg sperrt etwas.
3. **Archiv des Wächters** (Gemini „Wächter-Codex“ + ChatGPT „Gedächtnis der Inseln“): Optionale Quest „Das Archiv“: alle 17 Tagebuchseiten abgeben (FTB prüft die Seiten über ihre Komponenten) → Belohnung „Codex der Erbauer“ (Buch mit allen Notizen) und Baumaterial für eine Bibliothek. Story wird Teil der Basis.
4. **Die Welt reagiert** (Gemini): Beim Abschluss eines Akts ein Ton und eine Titelzeile auf dem Bildschirm („Akt II: Die Maschinen erwachen“). Technisch prüfen: KubeJS-Ereignis für FTB-Quests-Abschluss.
5. **Jedes Kapitel beginnt mit einem Problem** (ChatGPT): Erste Quest jedes Akts/Kapitels erklärt, welches Problem die neue Technik löst (Durchsatz, Strom, Logistik). Nur Textarbeit in `texte_*.py`.
6. **Bauen ohne Pflicht anerkennen** (ChatGPT „Die Insel, die du hinterlässt“): optionale Bau-Themen (Werkstatt, Garten, Archiv) mit Baumaterial-Belohnung. Offene Frage: Solche Aufgaben lassen sich nicht automatisch prüfen → entweder Haken-Quests nur in diesem optionalen Kapitel oder Abgabe typischer Bau-Items.
7. **Hilfetexte aus einer Quelle** (ChatGPT): Generator erzeugt `hinweise.js` aus derselben Tabelle wie die Questtexte, damit nichts auseinanderläuft.

## 4. Verworfen
- Embeddium statt Sodium (beruht auf falscher Annahme).
- Eigene Create-Ponder-Szenen (bräuchten ein zusätzliches Add-on).
- Resonanz-Kristall als neue Pflichtzutat (neues Item + künstliche Rezeptkette; widerspricht „kein Grind“).
- Release auf Modrinth/CurseForge (CurseForge-Mods liegen im Paket, nur privat).

## 5. Vorschlag für die nächsten Versionen
- **0.11** „Die Wahl zählt“: Punkte 2, 3, 5, 7 (+ mipmap-Test). Alles mit vorhandenen Werkzeugen, testbar auf dem Testserver.
- **0.12** nach dem Spieltest: Korrekturen aus `MORGEN-PLAYTEST.md`, Punkt 4 (Akt-Effekte), Punkt 6 (Bau-Themen).
- **1.0**: Titelbildschirm mit Insel-Panorama, Regressionstest, finaler Export.

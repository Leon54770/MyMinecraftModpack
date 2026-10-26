# Gemini-Prüfloop Sky and Stone

Ablauf: Moonlight-Sitzung meldet je Etappe die geänderten Dateien → Gemini prüft nur diese → Claude prüft gegen und urteilt (übernehmen/ändern/verwerfen) → Moonlight entscheidet und setzt um.
Modell: gemini-3.6-flash mit Nachdenken. **[C]** = Urteil von Claude.

---

## 25.10.2026 · Etappe 1 (0.4.0) · Vorab: Inselmarkt-Tauschgeschäfte

Grundregel: Kein Tausch soll eine Kiste liefern, deren Inhalt man mit dem Abgabe-Material selbst günstiger herstellt. Unendliche Billig-Quellen (Botany Pots, Bruchstein-/Andesit-Generator) nicht gegen wertvolle Kisten tauschen.

| Nr | Abgabe | Kiste | Phase | Gemini-Begründung | [C] Urteil |
|---|---|---|---|---|---|
| 1 | Weizensamen ×256 | Holz | Insel | fällt beim Sieben massenhaft an | **übernehmen** |
| 2 | Kies ×256 | Holz | Sieb | Überschuss aus dem Zerkleinern | **übernehmen** |
| 3 | Verrottetes Fleisch ×128 | Holz | Insel/Mobfarm | Abfall aus Mobfallen | **übernehmen** |
| 4 | Weizenmehl (Create) ×128 | Eisen | Create | massenhaft aus Mühlstein | **ändern:** ×256, da Weizen aus Botany Pots unendlich ist |
| 5 | Andesit ×256 | Eisen | Create | Steingenerator-Überschuss | **verwerfen:** Extruder liefert Andesit unendlich, und die Eisenkiste enthält Andesitlegierung (Schleife). Ersatz: **Erde ×256 → Holz** oder **Seelensand ×64 → Eisen** |
| 6 | Getr. Seetangblock ×32 | Eisen | Create | Abfall aus Seetangfarm | **ändern:** ×64 (Seetang wächst schnell nach) |
| 7 | Biokraftstoff (Mekanism) ×512 | Gold | Mekanism | Pflanzenverarbeitung | **verwerfen:** Pflanzen sind unendlich, das wären unendlich Diamanten/Prozessoren. Höchstens ×512 → Eisen |
| 8 | Schwefelstaub (Mekanism) ×256 | Gold | Mekanism | Chemie-Nebenprodukt | **ändern:** Herkunft im Skyblock unklar (unsicher), erst im JEI prüfen. Sonst ×128 → Eisen |
| 9 | Certus-Quarz ×128 | Gold | AE2 | Kristallzucht-Überschuss | **verwerfen:** Die Goldkiste enthält Prozessoren, die aus Certus entstehen (Schleife). Ersatz: **Fluix-Kristall ×64 → Gold** nur, wenn Prozessoren aus der Goldkiste genommen werden |
| 10 | Polonium-Pellet ×4 | Stern | Endgame | Reaktor-Überschuss | **übernehmen** (teuer genug: Spaltreaktor + Verarbeitung) |

**[C] Eigene Ergänzungen** (passen zu den Kisten, nicht ausnutzbar):
- **Inferium-Essenz ×256 → Holz** (Frühspiel, MA-Überschuss)
- **Honigwabe (Productive Bees) ×64 → Eisen** (Bienen-Kapitel bekommt einen Zweck)
- **Quellquarz/Source Gem (Ars Nouveau) ×32 → Gold** (unsicher: Preis im Spiel prüfen)
- **Netherwarze ×128 → Eisen** (Nether-Farm-Überschuss)

**Allgemein:** Wiederholbare Tausch-Quests mit Abklingzeit (z. B. 1× pro Spieltag in FTB Quests) oder Limit pro Spieler bauen. Dann bleibt selbst ein leicht zu günstiger Tausch harmlos.

---

## 25.10.2026 · Etappe 1 (0.4.0) · Prüfung der gebauten Änderungen

Geprüft: `forgivingvoid-common.toml`, `simplebackups-common.toml`, `reward_tables/*.snbt`, `data.snbt` (Loot-Kisten), `_src/quests.py` Abschnitt 15 Inselmarkt.
Drop-Chancen laut Gewichten: pro Monster ~2,9 % (Holz 1,9 %, Eisen 0,8 %, Gold 0,19 %), passiv ~0,12 % Holz, Bosse immer (50 % Gold / 50 % Stern).

| Nr | Gemini-Punkt | [C] Urteil |
|---|---|---|
| 1 | Volle Backups alle 30 min erzeugen am Laptop CPU-/SSD-Ruckler → Intervall 60–120 min | **übernehmen (abgewandelt):** `timer = 60`, und wenn die Config es anbietet, `backupType = "MODIFIED_SINCE_FULL"` mit `fullBackupTimer = 1440` (1 Vollbackup pro Tag, sonst nur Änderungen). Optionsnamen im Config-Kommentar prüfen (unsicher) |
| 2 | IF Mob Crusher zählt evtl. als Spieler-Kill → Kisten aus Automatik-Farmen | **prüfen:** Ob FTB Quests Fake-Player-Kills ausschließt, ist unklar. Falls Kisten droppen: Gold-Gewicht für Monster 2 → 1 oder Gold nur von Bossen |
| 3 | Dropraten für normales Spielen gut, Abklingzeiten verhindern Ausnutzen | **übernehmen**, keine Änderung nötig |
| 4 | Endgame-Tausch fehlt (Supremium/Insanium, Antimaterie, Präzisionsmechanik) | **übernehmen:** Antimaterie-Pellet ×1 → Stern (3 Tage), Supremium-Essenz ×32 → Stern (3 Tage), Präzisionsmechanik ×16 → Gold (2 Tage) |
| 5 | Sternkiste kaum besser als Goldkiste, 2× Netherit-Schrott schwach | **übernehmen (optional):** Schrott 2 → 4 oder 1 Netheritbarren |
| 6 | 10 GB / 8 Backups sicher | ok |
| 7 | Forgiving Void leichtgewichtig | ok (Werte sinnvoll: 3 Herzen Schaden, kein Tod, nur Spieler) |

[C] Nebenbei: `x_stern` (Netherstern → Sternkiste) gibt teils Netherstern-Splitter zurück. Das ist eine kleine Schleife, aber durch 3 Tage Abklingzeit harmlos.

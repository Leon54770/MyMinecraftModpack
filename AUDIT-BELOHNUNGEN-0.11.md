# Audit: Belohnungen und Wirtschaft (Stand 0.11.1)

Stand: 25.10.2026 · Ergebnis einer Auswertung von `_src/bausteine.py`, `_src/quests.py`, `_src/texte_hauptstory.py`, `kubejs/server_scripts/*.js` und `tags.json`. Nichts am Spiel geändert. Gleichgewicht ändert man erst nach dem Spieltest.

## Was geprüft wurde
- Welche Quest welche Kiste (Holz, Eisen, Gold, Stern) gibt.
- Ob Kisten Items enthalten, die später als Schranke dienen (Diamant, Osmium, Netherit).
- Ob die Gruppen-Umstellung (TODO-0.7) einen Effekt hat.

## Befunde

**1. Goldkiste als Wahl schon früh (Messing, Siebfabrik).** `belohnungen.py` gibt bei `c_messing` und `c_siebfabrik` eine Wahl aus der Goldkiste (`wahl`, nicht zufällig). Die Auswahl umfasst u. a. Diamanten und Osmium-Barren. Osmium und Diamant sind Stufen der Mekanism- bzw. Mystical-Agriculture-Kette. Ob das eine Abkürzung ist, hängt von Auswahl und Kette ab. **Nicht bestätigt, nur Verdacht.** Prüfen im Spieltest: Welche Auswahl nimmt man, und was bleibt danach als Schranke übrig?

**2. Sternkiste mit Netherit mitten im Spiel.** `l_mega` (Riesenspeicher, AE2) gibt eine Sternkiste mit 1 Netheritbarren (Gewicht 8 von 40). Netherit ist die Eingangsgröße für den Pipez-Ultimate-Upgrade (`balance.js`). Ein Barren ist klein, aber der Schritt ist ein Vorgriff. **Verdacht, kein Fehler.**

**3. TODO-0.7 (Gruppen für Barren, Bruchstein, Honig, Leder, Eier) hat fast keinen Effekt.** In `tags.json` hat jeder Barren-Tag genau ein Mitglied (`c:ingots/iron` = `minecraft:iron_ingot`, usw.). Bruchstein (`c:cobblestones/normal`) und Leder/Eier haben ebenfalls je ein Mitglied. Der Nutzen wäre nur Absicherung, falls ein Umbenennungs-Mod fehlt. Honig (`c:honeycombs`, 5 Mitglieder) betrifft nur den Inselmarkt, der Verbrauch ist dort eigene Logik. **Empfehlung:** TODO-0.7 als erledigt bewerten, nur die Certus-Gruppe war nötig (schon umgesetzt in 0.8.0).

**4. Gruppen-Logik greift nur bei Aufgaben ohne Verbrauch.** `quests.py` ersetzt nur Aufgaben, die nicht `consume` sind. Das ist richtig, sonst würde eine Gruppe beim Abgeben falsch abgezogen. Tausch-Quests (Inselmarkt) nutzen eigene Logik.

**5. Keine Wegabhängigkeit der Belohnungen.** Die Wahl-Belohnungen (0.11.0) sind rein Kisten. Das passt zur offenen Frage „wegabhängige Rezepte“, siehe `PLAN-0.20.0.md` Abschnitt 5a.

## Empfehlungen (nach Spieltest)
1. Goldkiste in `c_siebfabrik` testen: Diamanten und Osmium früh prüfen. Wenn zu früh, Inhalt oder Stelle ändern.
2. Netherit aus der Sternkiste bei `l_mega` entfernen oder durch Eisen/Messing ersetzen. Den Pipez-Schritt nicht vorwegnehmen.
3. TODO-0.7 schließen, Notiz in `TODO`-Liste entsprechend ändern.

## Nicht geprüft
- Kistenwahrscheinlichkeiten im Spiel, die Zeit bis zu einer Kiste, die Wirkung im Mehrspieler.

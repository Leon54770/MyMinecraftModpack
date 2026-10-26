# Todo für Sky and Stone 0.7 – Item-Gruppen nur, wo es Sinn ergibt

**Status 25.10.2026: geschlossen.** Almost Unified reduziert die Barren-Tags auf ein Item, weitere Gruppen bringen keinen Nutzen mehr (`AUDIT-BELOHNUNGEN-0.11.md`, Empfehlung 3). Die Certus-Gruppe ist seit 0.8.0 umgesetzt.

Stand: 25.10.2026 · Anlass: Spieltest-Feedback zu 0.6.1 („nur Eichenholz erlaubt“). Erledigt in 0.6.2: 16 Aufgaben mit Holz-/Farbvarianten.

## Grundregel
Für jede Item-Aufgabe die Frage stellen: **Geht es um den Zweck/das Material oder um genau dieses Item?**
- **Gruppe nehmen**, wenn jede Variante denselben Zweck erfüllt und der Spieler sonst grundlos ein bestimmtes Item herstellen müsste
  (Holzart, Farbe, Material aus verschiedenen Mods, beliebige Samen/Feldfrüchte).
- **Festes Item lassen**, wenn die Stufe, die Art oder die Funktion zählt
  (Netz-Stufen, Schaltkreis-Stufen, Essenz-Stufen, bestimmte Samen, Maschinen, Werkzeuge, Gerichte, Bosse/Trophäen).

## Prüfliste (53 Items haben eine c:-Gruppe, 135 nicht – Analyse vom 25.10.2026)

### Umstellen (Gruppe ergibt Sinn)
| Item | Gruppe | Warum |
|---|---|---|
| Eisen-, Kupfer-, Zink-, Osmium-, Stahl-, Messingbarren | `c:ingots/<metall>` | Material zählt, nicht die Mod. Schützt auch, falls Almost Unified mal nicht greift. |
| Certus-Quarz | `c:gems/certus_quartz` | Material zählt (Sieb, Samen, AE2). |
| Bruchstein (Bruchstein-Generator, Inselmarkt) | `c:cobblestones/normal` | Vorher prüfen, dass kein Tiefenschiefer-Bruchstein mit drin ist. |
| Honigwaben (Inselmarkt) | `c:honeycombs` | Prüfen, ob Productive-Bees-Waben dazugehören. Wenn ja: jede Wabe tauschbar, sinnvoll. |
| Leder, Eier (Nutztiere) | `c:leathers`, `c:eggs` | Zweck: „du hast Tiere“. Andere Eier/Leder sind genauso gut. |
| Knochen (Inselmarkt) | `c:bones` | Überschuss-Tausch, Herkunft egal. |

### Bewusst fest lassen
| Item | Warum fest |
|---|---|
| Siebnetze (Faden … Netherit), Sifter-Netze | Die Stufe ist der Sinn der Quest. `c:meshes` mischt Stufen. |
| Mekanism-Schaltkreise | `c:circuits` mischt Basic bis Ultimate. |
| Mystical-Agriculture-Samen und -Essenzen | Jeder Samen/jede Stufe ist der eigentliche Fortschritt. |
| Obsidian | Für das Netherportal taugt nur normaler Obsidian (kein weinender). |
| Lohenruten, Enderperlen, Netherstern, Shulker-Schalen | Gruppe hätte nur ein Mitglied, kein Nutzen. |
| Kies (Inselmarkt) | Das Sieb verarbeitet nur normalen Kies. |
| Netherwarzen (Inselmarkt) | `c:crops` wäre zu breit. |
| Festessen (Shepherd's Pie, Brathähnchen) | Genau diese Gerichte sind die Aufgabe. |
| Alle Maschinen, Werkzeuge, Gadgets, Zauberbücher, Charms, Reaktorteile | Es gibt nur dieses eine Item. |
| Sammlerbuch-Quests | Sammeln heißt: jedes Item einzeln. |

### Zusätzlich prüfen
- Starter-Questbuch (`ftbquests:book`) als erste Aufgabe: Was passiert, wenn das Buch verloren geht? Ggf. durch „Holz“ ersetzen.
- Für jede neue Gruppe: Mitglieder in `_src/tags.json` ansehen, bevor sie in die Quest geht (Ausreißer wie Tiefenschiefer, weinender Obsidian).
- Titel der Gruppen-Aufgaben auf Deutsch („Beliebige Eisenbarren“), Icon = typisches Item.

## Umsetzung (Technik)
- In `_src/quests.py` die Tabelle `GRUPPEN` um die Einträge aus „Umstellen“ erweitern. Mehr ist nicht nötig, `tag()` und FTB Filter System sind schon eingebaut.
- Inselmarkt-Tausche verbrauchen Items (`consume`). Prüfen, ob FTB Quests bei Gruppen-Aufgaben richtig abzieht (Testserver bzw. Spieltest). Bis dahin überspringt `GRUPPEN` verbrauchende Aufgaben (`not t[3]`).
- Danach: `python -I _src/quests.py`, Testserver, Export 0.7.0.

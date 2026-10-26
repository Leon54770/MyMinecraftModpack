# Rezept-Simulation Sky and Stone (Meilenstein 1)

Stand: 25.10.2026 · Pack 0.20.0 · Nur Analyse. Am Pack wurde nichts geändert.

## Ergebnis

- **Rezepte im Dump:** 15.618 aus 117 Typen. Davon 1.539 ohne Item-Ausgabe (vor allem Mekanism-Chemie) und 50 Ars-Nouveau-Tome, deren Ausgabe nicht lesbar war.
- **Quest-Aufgaben mit Item:** 241, davon 20 Gruppen über das FTB Filter System. Alle Item-IDs sind registriert, alle Gruppen-Tags bekannt.
- **Erreichbare Gegenstände nach Rezeptgraph:** 13.141.
- **Lücken (Aufgabe nicht erreichbar):** 0, nachdem zwei Quellen von Hand geprüft wurden (siehe unten). Ohne Weltquellen-Abgleich waren es 12 Meldungen, u. a. Weizen und Netherstern.
- **Prüfstatus:** Analyse BESTANDEN. Im Spiel NICHT GETESTET.

## Befunde

1. **Starbuncle-Kette (`ars.snbt`, Charm-Quest) – offen, Risiko.** Das Charm braucht Starbuncle-Shards. Das einzige Shard-Rezept braucht selbst Shards, ist also zirkulär. Im Code gibt es zwei Quellen:
   - Zähmung wilder Starbuncles mit Goldklumpen (`Starbuncle.attemptTame` erzeugt die Shards).
   - Dungeon-Truhen (`DungeonLootTables`), die nur in Strukturen vorkommen.

   Nachtrag, aus den Ars-Daten: Wilde Starbuncles spawnen nur in den Biomen des Tags `ars_nouveau:berry_spawn` (`#minecraft:is_taiga` und `ars_nouveau:archwood_forest`). Die Testwelt hat weder Taiga noch Archwood-Wald, die Startinseln liegen in Ebene, Wald oder Hain. Ohne Shards ist die Quest `a_starbuncle` („Der magische Logistiker“) damit praktisch nicht lösbar. Sie ist nicht optional, „Fabrik ohne Rohre“ hängt optional daran. Entschieden 25.10.: Quest entfernt, „Fabrik ohne Rohre“ hängt jetzt an der Schubladen-Wand (`l_controller`).

2. **Netherstern – kein Befund, falscher Alarm.** Der Wither-Drop läuft im Code. Die Loot-Tabelle `entities/wither.json` enthält nur eine Zufalls-Sequenz. Ohne diesen Schritt hätte die Simulation 7 der 8 Meldungen nach Loot-Abgleich erzeugt (Akt III, Markt, Sammler, MA-Samen, Archmage-Buch).

3. **Mekanism Polonium-Pellet (`akt3.snbt`, `markt.snbt`) – kein Fehler, Spätspiel.** Das Pellet entsteht per Chemie-Reaktion aus Polonium-Gas, Wasser und Fluorit-Staub. Polonium-Gas wiederum entsteht aus Atommüll (Aktivierung). Atommüll hat kein Rezept, er kommt aus dem Fission-Reaktor (Multiblock aus Mekanism Generators). Die Kette ist also vorhanden, aber nur über den Reaktor erreichbar. Die Analyse führt das Pellet deshalb als „Rohstoff-Annahme“.

## Methode

- **Dump** (`zz_dev_recipes.js`): Liest den Rezeptmanager nach dem Laden. Eingaben laufen über den KubeJS-Wrapper `Ingredient.of(...)`. Direkter Zugriff auf Java-`Ingredient`-Objekte scheitert in Rhino (`Cannot find function getItems`, sogar `getClass`).
- **Gegenprobe:** Der Dump liest den fertigen Rezeptmanager. Pack-Ergänzungen sind enthalten, z. B. `skyandstone:end_portal_frame` (aus `luecken.js`) und die Sifter-Rezepte aus `sieben.js`.
- **Analyse** (`analyse.py`): Ein Gegenstand gilt als erreichbar, wenn einer dieser Punkte zutrifft:
  - er steht im Startinventar (`starter_inventory.json5`),
  - er kommt aus einer Mob- oder Block-Loot-Tabelle (`entities/`, `blocks/` aller Mod-Jars und Vanilla-Daten),
  - er ist manuell als Quelle bekannt (`BEKANNTE_QUELLEN`),
  - kein Rezept stellt ihn her (dann optimistisch als Rohstoff angenommen),
  - oder ein Rezept stellt ihn her und jede Eingabe-Gruppe hat mindestens einen erreichbaren Gegenstand.

  Das wird bis zum Fixpunkt iteriert.
- **Quest-Aufgaben:** `config/ftbquests/quests/chapters/*.snbt`, nur `type: "item"` unter `tasks`. Belohnungen sind ausgeschlossen.

## Grenzen

- **Chemie:** Mekanism-Ketten über Gas und Flüssigkeit sind nicht modelliert.
- **Tome:** 50 Ars-Nouveau-Tome ohne lesbare Ausgabe. Keine Quest-Aufgabe nennt ein Tome (Textsuche in den Kapiteln).
- **Aufgabenarten:** Nur Item-Aufgaben. Töten, Ort, Dimension und andere sind nicht geprüft.
- **Truhen:** Strukturs-Truhen zählen nicht als Quelle.
- **Code-Quellen:** nur für die zwei Fälle oben von Hand nachgesehen.
- **Ebene:** Die Simulation prüft Rezepte und Erreichbarkeit, nicht Mengen, Stufen oder Balance.

## Testserver-Hinweise

- **Echter Testserver war gesperrt.** Ein Java-21-Prozess (PID 9532, gestartet 19:57) hielt `world/session.lock`. Bei der Nachprüfung lief er nicht mehr. Beendet habe ich ihn nicht. Der Dump lief deshalb in einer Kopie im Scratchpad (eigene Welt, Port 25566, Heap 3 GB) mit den Mods des Testservers. Ein neuer Start des echten Testservers (PID 7520, 20:11:47, Argumente wie `run.bat nogui`) lief sauber: `Done (1.362s)`, KubeJS 10/10 Skripte ohne Ladefehler, 0 fehlgeschlagene Rezepte.
- **RuntimeDistCleaner-Meldungen** im Dump-Lauf stammen von Rhinos Zugriff auf Item-Klassen mit Client-Abhängigkeiten. Sie kommen vom Test-Skript, nicht vom Pack. Der Server lief trotzdem bis `Done`.
- **Altes Skript im echten Testserver:** `kubejs/server_scripts/zz_dev_recipejson.js` stammt nicht aus dieser Sitzung. Es läuft bei jedem Start mit und wirft dabei einen Fehler. Auf Wunsch von Leon bleibt es im Testserver.
- **Dump-Skript** liegt nur hier (`zz_dev_recipes.js`) und nicht im Testserver.

## Reproduktion

Analyse (aus dem Pack-Ordner):

```bash
python -I -X utf8 _src/rezept-sim/analyse.py _src/rezept-sim/dump/dev_recipes.json _src/rezept-sim/dump/dev_tags.json _src/rezept-sim/dump/dev_items.json ../_testserver-sky-and-stone
```

Die letzte Angabe ist ein Ordner mit `mods/` und `libraries/`, also der Testserver. Details der Lücken stehen in `luecken.txt`.

Dump neu erzeugen: `zz_dev_recipes.js` in eine Kopie des Testservers unter `kubejs/server_scripts/` legen, starten, danach `kubejs/dev_recipes.json`, `dev_tags.json` und `dev_items.json` übernehmen.

## Offen (für Leon)

1. Starbuncle im Spiel prüfen: Spawnen wilde Starbuncles auf einer Insel? Liefert Zähmung mit Goldklumpen Shards?
2. Polonium-Pellets in JEI nachsehen: Gibt es einen Weg?
3. Erledigt: Der echte Testserver läuft (PID 7520). Dass 9532 beendet wurde, war nicht mein Schritt.

## Status und Rückweg

- Analyse: BESTANDEN. Spiel: NICHT GETESTET.
- Keine Pack-Änderung, daher kein `packwiz refresh` nötig.
- Rückweg: Der Ordner `_src/rezept-sim/` kann ohne Folgen gelöscht werden.

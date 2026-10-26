# Sky and Stone 1.0.0

Stand: 25.10.2026 · Basis 0.20.0 · Minecraft 1.21.1, NeoForge 21.1.264, Java 21

**Status:** Release-Kandidat. Die Ladeprüfung im Testserver ist bestanden. Im Spiel ist 1.0.0 noch nicht getestet. Vor einer Veröffentlichung folgt der Smoke-Test aus `FEEDBACK-LOG.md`.

## Neu
- **Spaß-Mods:** Emotecraft (Emotes), Enchantment Descriptions (Verzauberungsbeschreibungen), Loot Journal (Pickup-Anzeige, nur Client), Better Combat (Kampfanimationen).
- **Lagerfeuer-Rast:** Titel „Die Erbauer rasten“ beim ersten Rechtsklick auf ein Lagerfeuer.
- **Herzschlag-Partikel** bei den Spielern am Herzschlag-Tag.
- **Wächter-Spruch** nach dem Wiederbeleben.
- **Advancements:** „Die Leere ruft“ (Sturz aus 30 Blöcken), „Schlaf der Erbauer“, „Fellfreund“ (erste Zähmung).
- **Feiern:** Feuerwerk bei allen Meilenstein-Feiern. Neu: „Enderhandel“ (Inselmarkt), „Das Archiv ist vollständig“ (Abschluss des Sammelbuchs), plus fünf Quest-Feiern (Autarke Insel, Siebfabrik, Vierfach-Erz, Über der Leere, Erbe der Erbauer).
- **Ruinen-Truhen** als Lootr-Truhen mit kleiner Frühspiel-Beute. Mit 5 % Chance eine versteckte Bonus-Tagebuchseite.

- **Pehkui-Gimmick:** Ein roter Pilz macht klein, ein brauner groß, eine Chorusfrucht setzt die Größe zurück (`kubejs/server_scripts/pehkui_pilze.js`). Im Spiel NICHT GETESTET, Befehlssyntax aus der Mod-Befehlsklasse übernommen.

- **Vier neue Advancements:** „Riesenpilz“, „Pilzgröße“, „Zurück zur Mitte“, „Feuerstelle“.
- **Pilz-Titel und Lagerfeuer-Rauch:** Rückmeldung bei jeder Größenänderung und beim Rasten am Lagerfeuer.
- **Wächter-Spruch:** drei weitere Zeilen (acht insgesamt).

## Geändert
- **Klassische Insel** vergrößert (9×3 oben, 3×6 unten, 198 Blöcke). Spawn unverändert.
- **Sternkiste:** Netheritbarren entfernt, damit die Pipez-Sperre nicht umgangen wird. Netherit-Schrott bleibt.
- **Startinventar:** ohne Haken.
- **Befehle für alle Spieler:** Handbuch und Lagerfeuer-Titel laufen über den Server, nicht über den Spieler. Ohne OP funktionieren sie damit trotzdem.
- **Herzschlag-Ton** hörbar für alle Spieler, nicht nur in der Nähe des Spawns.

- **Frühe Wahl bei Messing und Siebfabrik:** eigene Messing-Kiste ohne Diamanten und Osmium (vorher Goldkiste). Die Zwischenstufen kommen so nicht zu früh.

## Entfernt
- **Starbuncle-Quest „Der magische Logistiker“:** wilde Starbuncles spawnen nur in Taiga und Archwood-Wald, die Startinseln haben beides nicht.
- **Mekanism Tools** (Werkzeugstufen waren bewusst verworfen).
- **Mining Gadgets** (überschneidet FTB Ultimine, ohne Quest-Nutzen).

## Entschieden
- **Koop:** optional, keine Team-Pflicht. Team-Belohnungen nur im Inselmarkt.
- **Zielzeit bis zum Finale:** Arbeitsannahme 20 Stunden.
- **Klangkulisse:** Mod-Standard (AmbientSounds), keine Pack-Änderung.

## Geprüft
- **Mekanism-Ketten Akt II und III:** keine Sackgasse. Drei Quests hängen an der Reaktor-Kette (Spätspiel).
- **Quest-Graph:** 185 Quests, 20 Kapitel, keine Zyklen, 0 Layoutprobleme.
- **Testserver:** 12 KubeJS-Skripte ohne Fehler, 0 fehlgeschlagene Rezepte, `Done` ohne Fehler.

## Bekannte Einschränkungen
- Alles aus Sprint 6 bis 8 ist im Spiel nicht getestet. Insbesondere Emote-Taste, Pickup-Anzeige, Kampfgefühl, Feuerwerk, Wächter-Spruch und Lootr-Verhalten.
- Ein Spieltest mit zwei Spielern (Koop, Team-Fortschritt, Stufen-Spike) steht aus.
- Starbuncle-Begleiter fehlt, der Ersatz ist offen (Backlog 8.7).
- Pehkui-Befehle (`scale set base`) sind nicht im Spiel geprüft.
- Die Fundgrube nach Sieb-Glück (8.3) und Schatzkarten (8.6) sind nicht umgesetzt.
- Acht Mods kommen nur von CurseForge. Für eine spätere Verteilung ist das zu klären.
- Ressourcenpakete `bare-bones` und `vanilla-exp` sind mit dabei, werden aber nicht genutzt.

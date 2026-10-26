# Sky and Stone – Scrum-Backlog (Release 1.0)

Stand: 25.10.2026 · Product Owner: Leon · Team: Claude (Umsetzung), Leon (Spieltests am Ende)

## Ziel
Ein fertiges, final spielbares Modpack. Spieltests kommen erst ganz zum Schluss (Sprint 5), vorher nur automatisierte Prüfungen.

**Erweitert 25.10.2026 (Sprint 6): Spaß und Gimmicks.** Das Pack soll nebenbei Spaß machen: kleine Gimmicks im Spiel und Mods, die das Spielerlebnis verbessern oder unterhaltsamer machen. Regeln dafür:
- Kein Mod, der Fortschritt überspringt (keine Flug-Mounts, keine Wirtschaft, keine Abkürzungen über die Quests).
- Jeder Eintrag bekommt eine Ladeprüfung auf dem Testserver. Rein clientseitige Teile sind NICHT GETESTET, bis Leon sie im Spiel sieht.
- Neue Mods nur mit Abhängigkeiten, die der Paket-Manager auflöst, und mit Eintrag in `mods/*.pw.toml`.

## Definition of Done (für jeden Punkt)
1. Umsetzung in Quellen (`_src/`, `kubejs/`, `config/`, `data/`) und Generator läuft fehlerfrei.
2. Testserver startet (Java 21), KubeJS ohne Fehler, Quest-Anzahl stimmt, keine neuen Fehler im Log.
3. Eintrag in `IMPLEMENTATION_LOG.md` (Datei, Zweck, Status) und Prüfstatus (BESTANDEN / FEHLGESCHLAGEN / BLOCKIERT / NICHT GETESTET).
4. `packwiz refresh` ausgeführt, Rückweg dokumentiert.
5. Im Spiel nicht geprüft = NICHT GETESTET, nie als getestet melden.

## Sprint 1 – Einstieg und Orientierung (ohne Spieltest prüfbar)
| # | Punkt | SP | Status |
|---|---|---|---|
| 1.1 | Starttext und Handbuch-Buch (Befehl) | 3 | erledigt (Load-Test OK, Spiel NICHT GETESTET) |
| 1.2 | Startinseln auf zwei reduziert | 2 | erledigt |
| 1.3 | Jobs+ Erklärung, Taste unter Steuerung | 1 | erledigt (Taste nicht im Spiel abgelesen) |
| 1.4 | Wegweiser nach dem ersten Eisenbarren (Ausblick-Quest) | 2 | erledigt als Text im Quest „Der Funke“, keine neue Quest (Quest ohne Aufgabe hakt sofort ab) |
| 1.5 | Inseln: Klassisch vergrößern oder Platz-Hinweis | 3 | erledigt: Klassisch vergrößert (9×3 oben, 3×6 unten, 197 statt 143 Blöcke), Waldlichtung unverändert |
| 1.6 | ID-Stabilitätscheck (`_src/idcheck.py`) | 3 | erledigt: 828 IDs gegen Backup, 0 entfallen |

## Sprint 2 – Spielspaß-Schicht (Ereignisse, Feiern, Belohnungen)
Siehe `SPRINT2.md` (wird nach dem Brainstorming befüllt).

## Sprint 3 – Balance und Inhalte
- Fehlerliste aus der Vollprüfung (Rezept-Simulation vervollständigen)
- Bienen-/Essenz-Ausbeute entscheiden und dokumentieren

## Sprint 4 – Release-Kandidat
- Modpack-Version 1.0.0, Changelog, `.mrpack`-Export
- Vollständige Prüfung (Generator, Serverstart, Log-Analyse), Berichte

## Sprint 5 – Spieltest und Abnahme (Leon)
- Spieltest in Prism nach Checkliste (`MORGEN-PLAYTEST.md`)
- Auswertung, Bugfixes, Abnahme ABGENOMMEN / NICHT VOLLSTÄNDIG ABGENOMMEN

## Sprint-1-Nachtrag (25.10.2026)
- Neu 1.6 erledigt: `_src/idcheck.py <Referenz>` prüft, dass keine Quest-ID entfällt. Ergebnis gegen Backup vor 0.20.0: 828 IDs, 0 entfallen, 0 neu.
- TEST_REPORT.md: Java-21-Zeile korrigiert (Serverstart ist getestet).
- Offen aus Sprint 1: Rezept-Dump ohne Java-Reflexion, Wegweiser nach Eisenbarren, Klassisch-Insel, Curios-Quelle.

## Sprint 2 – Spielspaß (Stand 25.10.2026, Auswahl aus dem Brainstorm)
| # | Idee | Umfang | Status |
|---|---|---|---|
| 2.1 | Meilenstein-Feier: Titel und Glockenton bei den 11 Story-Erfolgen (Belohnungsfunktion) | S | erledigt (Ladetest OK, im Spiel NICHT GETESTET) |
| 2.2 | Sturm der Leere: alle 3 Tage 10 Minuten Regen (ohne Blitze) | S | erledigt (Ladetest OK, im Spiel NICHT GETESTET) |
| 2.7 | Herzschlag der Leere: einmal täglich zur Dämmerung Titel und Ton | S | erledigt (Ladetest OK, im Spiel NICHT GETESTET) |
| 2.3 | Ruinen-Truhen als Lootr-Truhen | S | erledigt (Ladetest OK), Beute als Standard, im Spiel NICHT GETESTET |
| 2.4 | Wächter-Begleiter (Starbuncle-Quest erweitern) | S-M | zurückgestellt: Starbuncle-Quest entfernt, wilde Starbuncles spawnen nur in Taiga und Archwood |
| 2.5 | Klangkulisse pro Insel (AmbientSounds) | S | Biome geprüft: AmbientSounds hat schon biomabhängige Regionen (Ebene, Wald u. a.), kein Eingriff nötig. Entscheidung: Mod-Standard, keine Pack-Änderung |
| 2.6 | Täglicher Gruß beim ersten Login | S | offen, Grind-Risiko |

Hinweis (aktualisiert 25.10.2026): Es gibt 17 Feiern, 11 Story-Erfolge und 6 Quest-Feiern. Die übrigen Meilensteine haben Story-Feiern oder sind bewusst ausgelassen (siehe Protokoll). Das ist ein offener Punkt für Sprint 3.

## Sprint 3 – Erreichbarkeit und Orientierung (Stand 25.10.2026, begonnen)
| # | Punkt | SP | Status |
|---|---|---|---|
| 3.1 | Erreichbarkeits-Check (_src/erreichbar.py, Heuristik über Rezept-Dump) | 5 | Werkzeug fertig. Ergebnis: 186/186 Quests über Abhängigkeiten erreichbar. 79 Aufgaben-Items ohne Weg laut Heuristik, überwiegend Fluid-, Energie- und Mystical-Rezepte, die die Heuristik nicht modelliert. Prüfen von Hand. |
| 3.2 | Rezept-Dump als Testserver-Skript (zz_dev_recipejson.js, JSON über forEachRecipe) | 2 | erledigt, Testserver only |
| 3.3 | Hauptpfad und Nebenpfade als Chapter Groups (FTB-Sichtbarkeit) | 3 | offen (Recherche-Vorschlag) |
| 3.4 | Begrüßungsbuch einmalig beim ersten Login | 2 | erledigt (willkommen.js gibt function skyandstone:handbuch_buch einmal pro Spieler; Testserver lädt, Spiel NICHT GETESTET) |
| 3.5 | Kapitel-Abschluss mit Story-Gate | 3 | offen |

Recherche (25.10.2026): Quellen überwiegend Wikis und SEO-Seiten. Übernommen als Richtung: Hauptpfad sichtbar, Nebenpfade freiwillig (SkyFactory 4, StoneBlock), Story-Figur als Wegweiser (StoneBlock Echo), Weltmeilensteine (StoneBlock World Engine), Startkette mit einem eindeutigen nächsten Schritt (Vault Hunters).

## Stand Umsetzung (25.10.2026, abschließend für diesen Lauf)
Umgesetzt: 1.6 ID-Check, 2.1 Meilenstein-Feier, 2.2 Sturm, 2.7 Herzschlag, 3.1 Erreichbarkeits-Check (Werkzeug), 3.2 Dump, 3.4 Begrüßungsbuch.
Offen, mit Grund:
- 3.3 Chapter Groups mit Sichtbarkeit: braucht Erweiterung von _src/ftbformat.py und einen Test im Spiel, Quest-Format ist nicht vollständig belegt.
- 3.5 Kapitel-Abschluss mit Story-Gate: braucht neue Gate-Quests, Texte und Balance-Entscheidung.
- 79 Aufgaben aus dem Erreichbarkeits-Check: von Hand prüfen, die meisten sind Fluid- und Energie-Fehlalarme.
- Ruinen-Truhen als Lootr: Lootr ist ungetestet, Ruinen-Generator ändert nur neu erzeugte Inseln.
- Wächter-Begleiter, Klangkulisse: Verhalten und Biome nicht geprüft.
- Täglicher Gruß: laut CLAUDE.md wegen Grind-Risiko zurückgestellt.
- Klassisch-Insel vergrößern: braucht Neugestaltung der Insel, nicht nur Parameter.
- Curios-Quelle: Industrial Foregoing, harmlos, Fix nicht bekannt.

## Lauf 2 (25.10.2026)
- Erreichbarkeits-Check erweitert: Weltquellen (Drops, Ernte, Bosse) werden getrennt ausgewiesen (WELT_QUELLEN in _src/erreichbar.py). 11 Items davon.
- Ergebnis: 186/186 Quests erreichbar. 111 Aufgaben-Items ohne Weg laut Heuristik. Davon 11 Weltquellen, Rest: Mekanism- und AE2-Chains, Mystical-Essenzen, Ars-Nouveau-Items, Farmers-Delight-Gerichte. Diese Ketten muss man im Spiel oder mit Rezept-Details prüfen. Die Heuristik kennt weder Fluids noch Energie noch Mod-Drops.
- Nächster Schritt: Rezept-Ketten Akt II und III Stück für Stück prüfen (Mekanism, AE2, Mystical), dann entscheiden, was echte Lücke ist.

## Lauf 3 (25.10.2026): Ursache der Fehlalarme gefunden
- Befund: zz_dev_recipejson.js läuft in ServerEvents.recipes. Rezepte, die Pack-Skripte per event.custom hinzufügen (sieben.js EXTRA_DROPS, Sifter, balance.js), erscheinen im Dump nicht. Beleg: 0 createsifter:sifting-Rezepte im Dump, 0 Sieb-Rezepte für mysticalagriculture:inferium_essence, obwohl sieben.js Z. 71-79 sie erzeugt.
- Folge: Die 111 Aufgaben-Items ohne Weg enthalten Fehlalarme, die das Pack selbst liefert (z. B. Inferium-Essenz).
- Zweiter Befund: Rezepte, die nur Fluids oder Chemikalien als Eingabe haben (Mekanism, Infusion), fallen aus dem Graph, weil _src/erreichbar.py nur Item-Zutaten sammelt. Betrifft z. B. mekanism:basic_control_circuit.
- Nächster Schritt (Sprint 3.6): Dump so umbauen, dass er nach allen Recipe-Events läuft (z. B. Server-Load-Event mit Java-RecipeManager und Codec-Serialisierung), dann Check neu. Fluid-Rezepte als Optimismus modellieren und getrennt ausweisen.
- Bis dahin: Befunde des Checks NICHT als Lücken melden.

## Sprint 3.6 erledigt (25.10.2026)
- Testserver-Dump jetzt in ServerEvents.afterRecipes, Serialisierung über den Mojang-Codec (JsonOps). 15467 Rezepte, 151 nicht serialisierbar.
- Erreichbarkeits-Check neu: 13360 Rezepte mit Ergebnis, 4116 herstellbare Item-IDs. 186/186 Quests erreichbar. Aufgaben ohne Weg: 111 -> 92. Pack-eigene Rezepte (Inferium-Sieb, Sifter) werden jetzt gesehen.
- Offen: Fluid- und Chemikalien-Rezepte (Mekanism) fehlen weiterhin im Graph. 151 nicht serialisierbare Rezepte prüfen.

## Sprint 6 – Spaß und Gimmicks (25.10.2026, auf Wunsch von Leon)
Ziel: Das Pack soll nebenbei Spaß machen. Kleine Gimmicks und Mods, die das Spielerlebnis verbessern. Regeln stehen im Ziel oben (kein Fortschritts-Überspringen, Ladeprüfung je Eintrag).
| # | Punkt | Umfang | Status |
|---|---|---|---|
| 6.1 | Emotes (Emotecraft 2.4.12, beide Seiten, Abhängigkeit player-animation-lib) | S | erledigt, Ladeprüfung OK. Emote-Menü per Taste: im Spiel NICHT GETESTET |
| 6.2 | Verzauberungsbeschreibungen (Enchantment Descriptions 21.1.11) | S | erledigt, Ladeprüfung OK, Spiel NICHT GETESTET |
| 6.3 | Pickup-Anzeige (Loot Journal 6.2.2, nur Client, Abhängigkeit Fragmentum 5.4.0) | S | erledigt, Ladeprüfung OK, Client NICHT GETESTET |
| 6.4 | Kampfanimationen (Better Combat 2.4.0, Abhängigkeit playerAnimator 2.0.4) | M | erledigt, Ladeprüfung OK ohne Duplikat-Fehler. Im Spiel NICHT GETESTET. Kann das Kampfgefühl ändern, nach dem Spieltest prüfen |
| 6.5 | Feuerwerk bei allen 16 Meilenstein-Feiern (Partikel im Datenpaket) | S | erledigt, Ladeprüfung OK. Die Ausführung im Spiel NICHT GETESTET |
| 6.6 | Alex's Mobs (Kreaturen) | M | nicht verfügbar: Modrinth hat für 1.21.1 NeoForge keine gültige Version. Zurückgestellt |
| 6.7 | Wächter-Spruch nach dem Wiederbeleben (`kubejs/server_scripts/waechter.js`, fünf Zufallszeilen) | S | erledigt, Ladeprüfung OK (11/11 Skripte). Die Nachricht im Spiel NICHT GETESTET |
| 6.8 | Gimmick-Ideen für später | — | Lagerfeuer am Spawn, Fundgrube-Ereignis nach Sieben-Glück, Titel bei Inselmarkt-Sammelziel |

## Sprint 7 – Fehlendes bis zum Release (25.10.2026, Gesamtbild)
Analyse des Projekts gegen das Ziel „fertiges, final spielbares Modpack“, ergänzt durch eine Recherche zu Release-Checklisten (Quellen: [pinehosting: CurseForge-Update ohne Server-Bruch](https://pinehosting.com/blog/curseforge-modpack-update-strategy-how-to-avoid-breaking-multiplayer-servers/), [Terra Firma Greg: Release-Veröffentlichung](https://wiki.terrafirmagreg.team/modern/en_us/developer/publishing), [itzg docker-minecraft-server: packwiz](https://mintlify.com/itzg/docker-minecraft-server/mods-plugins/packwiz), [Simple Modpack Update Checker](https://modrinth.com/mod/smuc)). Die fünf wichtigsten Lücken:

| # | Lücke | Warum sie zählt | Erste Schritte | Status |
|---|---|---|---|---|
| 7.1 | Kein Spieltest-Fundament: Frühspiel-Zeit, Leistung und Smoke-Tests sind nicht gemessen | Ohne Messung kann niemand sagen, ob das Pack spielbar ist. Die Recherche nennt Smoke-Tests in einer neuen Welt und Leistungsprüfung als Standard | `FEEDBACK-LOG.md` mit Vorlage und Smoke-Test-Checkliste angelegt. Messung durch Leon | Vorbereitet, wartet auf Spieler |
| 7.2 | Mehrspieler ungetestet: Team-Fortschritt, Lootr pro Spieler, Spike mit zwei Spielern | Koop ist im Pack vorgesehen, aber nie ausprobiert. Das ist die häufigste Fehlerquelle bei Modpacks | Koop-Testprotokoll in `FEEDBACK-LOG.md`. Entscheidung Koop optional steht (`GAME_DESIGN.md`) | Protokoll vorbereitet, Test offen |
| 7.3 | Quest-Sackgassen nicht vollständig ausgeschlossen: Chemie- und Reaktor-Ketten (Mekanism, 151 Rezepte nicht lesbar) | Die Starbuncle-Kette hat gezeigt, dass solche Sackgassen vorkommen. Die Simulation sieht Chemie nicht | Mekanism-Ketten Akt II und III von Hand prüfen, danach Sprint 3.6 abschließen | Offen |
| 7.4 | Endgame nach dem Finale ist nicht entworfen, Wahlen haben keine Folgen | Wiederspielwert und der letzte Spannungsbogen fehlen, siehe `GAME_DESIGN.md` (Endgame, offen) | Konzeptentwurf „Nach dem Finale“ und Vorschlag für Wahl-Folgen | Entwurf offen |
| 7.5 | Kein Weg zum Verteilen: Update-Adresse (P9), Release-Version 1.0.0, Changelog, Installationsanleitung, Server-Pack | Ohne Update-Adresse kann kein anderer PC oder Koop-Freund das Pack bekommen. Die Recherche zeigt: Update über eine `pack.toml`-URL, Versionsabgleich, Java 21 und Server-Pack | Release-Checkliste und Installationsanleitung vorbereiten. Hosting-Entscheidung (Repo) liegt bei Leon | Vorbereitet, Hosting offen |

Ausdrücklich nicht in Sprint 7: neue Mods. Neue Gimmicks sind seit Sprint 6 erlaubt, aber nur mit Ladeprüfung je Eintrag und ohne Fortschritts-Überspringen. Der Fokus liegt auf Stabilität und Spielbarkeit.

**Stand 25.10.2026 (Nachtrag):** 7.4 Endgame-Entwurf steht in `GAME_DESIGN.md` (drei Vorschläge A, B, C, Umfang offen). 7.3 teilweise: Der Fission-Reaktor ist als Quelle für Atommüll bestätigt (Polonium-Pellet, Antimaterie). Die Akt-II- und Akt-III-Ketten von Mekanism sind noch nicht Stück für Stück geprüft. 7.1, 7.2, 7.5 bleiben wie oben.

## Sprint 8 – Ideen-Backlog (Brainstorming 25.10.2026, nicht freigegeben)
Ideen, nach Aufwand (S, M, L) und Wirkung sortiert. Nichts davon ist gebaut. Mods brauchen eine Freigabe.

| # | Idee | Art | Aufwand | Wirkung | Anmerkung |
|---|---|---|---|---|---|
| 8.1 | Lagerfeuer am Spawn: Sitzen am Feuer gibt einen kurzen Titel „Die Erbauer rasten“ | Datenpaket | S | mittel | Keine Belohnung, nur Atmosphäre |
| 8.2 | Versteckte Tagebuchseite 18 in einer Ruine, nur mit Hinweis aus dem Archiv | Quest/Lore | S | hoch | Passt zur Story-Ebene |
| 8.3 | (gestrichen, siehe GAME_DESIGN) Fundgrube nach Sieb-Glück: 1 % Chance auf eine goldene Zusatzkiste mit Titel | KubeJS | M | hoch | Balance-Risiko klein, Chance niedrig |
| 8.4 | Herzschlag-Partikel am Spawn bei Dämmerung (Puls aus Feier 2.7) | Datenpaket | S | mittel | Baut auf vorhandenem Herzschlag auf |
| 8.5 | Titel beim Erreichen von Inselmarkt-Sammelzielen | KubeJS/Datenpaket | S | mittel | Aus 6.8 |
| 8.6 | (gestrichen, siehe GAME_DESIGN) Schatzkarte aus Ruinen: Karte mit Markierung einer weiteren Ruine | Datenpaket | M | mittel | Hilft bei Sechs-Inseln-Welt |
| 8.7 | (entschieden: kein Begleiter, siehe GAME_DESIGN) Ersatz-Begleiter für die Logistik (Vogel statt Starbuncle) | Mod oder Quest | M | mittel | Ersetzt die entfernte Starbuncle-Quest |
| 8.8 | Pehkui: Größenänderung als Gimmick-Trank (Freigabe nötig) | Mod | M | hoch | Lustig, aber Testaufwand im Mehrspieler |
| 8.9 | (abgelehnt, siehe GAME_DESIGN) Leere-Nebel am Inselrand (Client-Effekt) | Ressourcenpaket | M | mittel | Nur Atmosphäre, Client |
| 8.10 | Achievements mit Titeln für kuriose Aktionen (z. B. erstes Jetpack-Flug-Ende) | Datenpaket | S | niedrig | Kleine Belohnung für Entdecker |
| 8.11 | Post-Finale-Titel (GAME_DESIGN 7.4, Vorschlag A) | Datenpaket | S | mittel | Erst nach Entscheidung von Leon |

**Stand Umsetzung (25.10.2026, Sprint 8):** Ladeprüfung im Testserver: 12/12 KubeJS-Skripte ohne Fehler, 6400 Advancements, `Done (1.261s)`, 185 Quests. Im Spiel NICHT GETESTET.
- 8.1 erledigt: `kubejs/server_scripts/lagerfeuer.js`. Titel „Die Erbauer rasten“ beim ersten Rechtsklick auf ein Lagerfeuer, einmal pro Spieler. Kein Sitz-Erkennung.
- 8.2 erledigt: Tagebuchseite 18 „zerrissen“ in der Ruinen-Beute, 5 % pro Truhe. Der Text ist ein Entwurf, Leon prüft die Story-Passung.
- 8.4 erledigt: Herzschlag-Partikel bei allen Spielern am Herzschlag-Tag (`zeit/herzschlag.mcfunction`). Nicht am Spawn, sondern bei den Spielern.
- 8.5 erledigt: Feier beim Enderhandel (`x_perlen`), wiederholbar. Ein Sammelziel pro Tausch.
- 8.10 erledigt: drei Advancements „Die Leere ruft“ (Sturz aus 30 Blöcken), „Schlaf der Erbauer“, „Fellfreund“ (Zähmung).
- 8.3 nicht umgesetzt: braucht einen Ereignis-Haken auf die Sieb-Ausgabe von Ex Deorum. Nächster Schritt: prüfen, ob Ex Deorum einen Ereignis-Hook bietet.
- 8.6 zurückgestellt: Schatzkarten brauchen Strukturen, die Skyblock-Welt nicht hat.
- 8.11 nicht umgesetzt: wartet auf die Entscheidung über den Umfang (GAME_DESIGN, Endgame A oder B).

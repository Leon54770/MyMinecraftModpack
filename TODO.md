# TODO – Sky and Stone

Stand: 25.10.2026 · Pack 1.0.0 · Priorisierte Gesamtliste.

Sprint-Plan und Definition of Done stehen in `SCRUM/BACKLOG.md`. Befunde und Prüfberichte stehen in `TEST_REPORT.md`, `PROJECT_AUDIT.md` und `IMPLEMENTATION_LOG.md`. Diese Datei sortiert nur, sie ersetzt keine davon.

**Legende:** `[ ]` offen · `[B]` blockiert (Spieltest oder Entscheidung von Leon nötig) · `[x]` erledigt.

---

## Phase 1 – Aufräumen ohne Spieler

Claude kann das allein erledigen. Jeder Schritt mit Pflichtprüfung aus `CLAUDE.md`.

- [x] `.packwizignore` um `CLAUDE.md`, `TODO.md` und `.claude/` ergänzt (sonst landen sie im Paket).
- [x] Log-Reste als bekannt dokumentiert (`TEST_REPORT.md`, `PROJECT_AUDIT.md`), nicht ohne Beleg ändern: Curios-Slots `example` und `feet` (Quelle laut Vollprüfung Industrial Foregoing, harmlos), ironfurnaces-Bedingungsrezepte (`allthemodium` fehlt, vermutlich harmlos), Mixin-Warnungen zu nicht installierten Mods.
- [x] Rezept-Simulation abgeschlossen: 0 Lücken nach Quellenabgleich. Bericht in `_src/rezept-sim/REZEPT-SIM.md`. Starbuncle-Quest `a_starbuncle` entfernt (25.10.). Polonium-Pellets sind kein Fehler, die Kette läuft über den Fission-Reaktor (Spätspiel).
- [x] Wegweiser nach dem ersten Eisenbarren: steht als Text im Quest „Der Funke“ (Überschreibung in `_src/texte_hauptstory.py`, im Testserver geladen). Keine neue Quest, denn eine Quest ohne Aufgabe hakt sofort ab.
- [x] TODO-0.7 (Item-Gruppen) geschlossen. Begründung: Almost Unified reduziert jeden Barren-Tag auf ein Item (`AUDIT-BELOHNUNGEN-0.11.md`, Empfehlung 3). Vermerk in `_src/TODO-0.7.md`.
- [x] Meilenstein-Feier für Quest-Meilensteine: 6 neue Feiern (`g_autark`, `c_siebfabrik`, `k_inject`, `k_jetpack`, `z_herr`, `x_perlen`) über eine Befehls-Belohnung (`FEIER` in `_src/quests.py`). Ausgelassen: 6 Meilensteine mit Story-Feier oder eigener Begrüßung, 4 Haken-Quests, die nicht im Buch stehen.

## Phase 2 – Entscheidungen von Leon

Ohne diese Antworten ist die Arbeit an Phase 4 und 5 blockiert.

- [x] **Koop:** Entschieden 25.10.: optional, keine Team-Pflicht. Team-Belohnungen bleiben beim Inselmarkt (`GAME_DESIGN.md`, Arbeitsannahmen).
- [x] **Zielzeit bis zum Finale:** Arbeitsannahme 20 Stunden, nach dem Spieltest korrigieren (`GAME_DESIGN.md`, Arbeitsannahmen).
- [B] **Update-Adresse** für Prism und andere PCs (privates Repo oder Host statt `file:///C:/...`). Ohne Adresse kein Update auf anderen Rechnern. (P9)
- [x] **Sprint 1.5:** Klassische Insel vergrößert (9×3 oben, 3×6 unten, 197 Blöcke, Spawn unverändert). Waldlichtung unverändert.

## Phase 3 – Spieltest (Leon, Prism) – messen statt raten

Vorlage: `MORGEN-PLAYTEST.md` (noch für 0.11.0 geschrieben, vor dem Test auf 0.20.0 anpassen). Ergebnisse direkt dort eintragen.

- [B] **Klassische Insel ohne Eimer (26.10.):** Sieb → Stone Pebbles → Bruchstein → Hammer → Kies; Wasser nur aus dem Holztiegel. Im Spiel prüfen, ob das ohne Eimer flüssig geht (Holztiegel-Wasser kommt erst mit dem Eisen-Eimer heraus, bis dahin Regen im Fass).
- [B] **Frühspiel-Zeit:** Minuten bis zum ersten Eisenbarren messen. Ziel 25–40 min. Bisher nur die Schätzung 10–25 min.
- [B] **Leistung auf dem Laptop:** `/spark tps`, RAM in Prozent, F3-FPS nach ca. 10 min. Ziel 20 TPS und RAM unter 80 %. Bisher nur TPS 20/20/16/19/19.
- [B] **Lootr:** Hat jeder Spieler seine eigene Truhe, und funktioniert das in der Skyblock-Welt? (0.20.0, ungeprüft)
- [B] **Jobs+:** Taste „Open Jobs+ GUI“ und Befehl `/help job` im Spiel prüfen. Der Befehl ist nur aus der Mod-Klasse abgeleitet.
- [B] **Handbuch und Meilenstein-Feier:** `/function skyandstone:handbuch` (braucht OP) und die 11 Story-Feiern sowie die 5 neuen Quest-Feiern im Spiel testen. Die neuen laufen über die Befehls-Belohnung mit Berechtigung 2 als Spieler.
- [B] **Gruppen-Aufgaben (Stuck-Quest-Test, P3):** Holz- oder Barren-Aufgabe abgeben und prüfen, ob die Quest abschließt.
- [B] **Goldkiste** bei Messing und Siebfabrik: Kommen Diamanten und Osmium zu früh? (`AUDIT-BELOHNUNGEN-0.11.md`, Befund 1)
- [B] **Mob-Kisten und Inselmarkt:** Nach 1 h Farm prüfen, ob Kisten kommen und ob der Markt genutzt wird.
- [B] **Spike Stufen-Abfrage (P4):** Zwei Spieler, einer mit Stufe `spike_test`, einer ohne. Dazu eine Maschine mit `StageBarrierBlock`. Ergebnis in `PLAN-0.20.0.md` Abschnitt 5a eintragen.

## Phase 4 – Balance nach Messung

Nur mit Messwert oder Spieltest-Befund. Vermutungen bleiben stehen.

- [x] **Goldkiste** bei Messing und Siebfabrik: eigene Messing-Kiste ohne Diamanten und Osmium (Entscheidung ohne Spieltest, Begründung in `AUDIT-BELOHNUNGEN-0.11.md`, Befund 1). Die übrige Goldkiste bleibt.
- [B] **Netherit-Schrott:** Entscheidung Leon 26.10.: nur beim Wither ersetzen (jetzt 8 Erfahrungsfläschchen), Fabrik und Sternkiste bleiben. Korrektur nach der Entscheidung: Die Sternkiste gibt bei einem Treffer 4 Schrott (Gewicht 5 von 23, 2 Ziehungen, ca. 40 % je Kiste), nicht „selten 1“. Mit 4 Gold ergibt das einen Netheritbarren. Neu entscheiden: Sternkiste auf 1–2 Schrott senken oder lassen.
- [ ] **Frühspiel-Schritte** (Eisenbarren-Menge steht auf 2) nach gemessener Zeit nachjustieren (P6).
- [ ] **Mob-Kisten-Rate** (1 %) und **Inselmarkt-Mengen und Abklingzeiten** nach Daten anpassen.
- [ ] **Mystical-Agriculture-Ausbeute:** Ist Tertium mit Messing im Mixer fair? (`MORGEN-PLAYTEST.md`, Abschnitt E)
- [ ] **Team-Fortschritt (P5)** umsetzen, sobald die Koop-Entscheidung aus Phase 2 steht.

## Phase 5 – Wahlen mit Folgen

Nur bauen, wenn der Spike aus Phase 3 positiv ist. Sonst Fallback.

- [B] **Spike vollständig testen** (zwei Spieler, siehe Phase 3).
- [ ] **Bei positivem Spike:** Wahl-Folgen über `StageReward` und `StageTask` (FTB Quests und FTB Teams) bauen. Nicht durch globales Entfernen von Rezepten, das würde alle Teams treffen.
- [ ] **Bei negativem Spike:** Folgen über Quest-Gates und Belohnungen bauen (Fallback aus `PLAN-0.20.0.md` Abschnitt 5a).
- [ ] **Finale auf den Wahlen aufbauen:** Finale-Text und Belohnung (`GAME_DESIGN.md`, Endgame).
- [x] **Kapitel „Prüfungen der Leere“:** 7 Quests mit echten Aufgaben. 26.10.2026 neu: „Die Festung räumen“ (50 Wither-Skelette), „Schattenjagd“ (32 Enderman), „Ein Netz ohne Ende“ (1 Mrd. FE). Dabei gefunden und behoben: Strom-Aufgaben ohne `max_input` nehmen keinen Strom an („Der Speicher der Erbauer“ war unlösbar).
- [ ] **Wahl-Folgen ohne Stufen (Idee aus der FreeLLMAPI-Zweitmeinung 26.10., `_src/KI-PRUEFUNG/ANTWORT-2026-10-26-fusion.md`):** Jeder Weg schaltet eine kleine optionale Folge-Questreihe frei (z. B. „Werkstatt der Maschine“, „Zirkel der Magie“), beide münden in dieselbe Hauptstory. Nur bauen, wenn der Spike negativ ist (Fallback).
- [ ] **Archiv des Wächters:** Verlustrisiko der einmaligen Tagebuchseiten entscheiden (Vollprüfung, Entscheidung 10 – bisher belassen).

## Phase 6 – Erweiterungen (nur mit Nutzen)

Kandidaten aus dem Brainstorming in `SCRUM/BACKLOG.md`. Jede Erweiterung braucht vorher einen Ladetest und einen Spieltest.

- [x] **Sturm der Leere** (Regen-Ereignis alle 3 Tage) – Sprint 2.2 erledigt, Ladetest OK, im Spiel nicht getestet.
- [x] **Herzschlag der Leere** (Titel und Ton zur Dämmerung) – Sprint 2.7 erledigt, Ladetest OK, im Spiel nicht getestet.
- [x] **Ruinen-Truhen als Lootr-Truhen** – Sprint 2.3: Lootr-Truhe neben jedem Ruinen-Schild, Beute `skyandstone:ruinen/fund`. Ladetest OK, Spieltest offen (Phase 3).
- [ ] **Wächter-Begleiter** (Starbuncle-Quest erweitern) – Sprint 2.4, zurückgestellt. Die Quest „Der magische Logistiker“ (`a_starbuncle`) ist seit 25.10. entfernt, weil wilde Starbuncles nur in Taiga und Archwood-Wald spawnen (`_src/rezept-sim/REZEPT-SIM.md`, Befund 1).
- [x] **Klangkulisse** (AmbientSounds) – Sprint 2.5: Biome geprüft. Der Mod hat schon biomabhängige Regionen, Ebene und Wald der Startinseln sind abgedeckt, ohne Eingriff. Eine Klangkulisse pro Insel gäbe es nur über `centeredBiomes` in der Weltgenerierung (Entscheidung 25.10.: Mod-Standard, keine Pack-Änderung). Details im Protokoll.
- [x] **Spaß-Features (Sprint 6):** Emotes (Emotecraft), Verzauberungsbeschreibungen, Pickup-Anzeige (Loot Journal), Better Combat, Feuerwerk bei den Meilenstein-Feiern, Wächter-Spruch nach dem Wiederbeleben. Ladeprüfung OK, im Spiel NICHT GETESTET (`SCRUM/BACKLOG.md`, Sprint 6).
- [ ] **Werkzeugstufen** (Melded) prüfen, nur wenn ein Nutzen belegt ist.
- [ ] **When Dungeons Arise:** nicht übernommen (zwei Fortschritts-Einträge laden nicht). Nur mit eigenem Test wieder prüfen.
- [ ] **Täglicher Gruß** (Sprint 2.6): zurückstellen, Grind-Risiko.

## Phase 7 – Release 1.0

- [ ] **Vollständige Prüfung:** Generator, Serverstart, Log-Analyse, Berichte (`SCRUM/BACKLOG.md` Sprint 4).
- [x] **Version 1.0.0**, Changelog (`CHANGELOG_1.0.0.md`) und `.mrpack`-Export (`Sky and Stone-1.0.0.mrpack`, lokal). Im Spiel noch nicht getestet.
- [ ] **Eigener Titelbildschirm** (Panorama der Insel), braucht Screenshots aus dem Spiel.
- [ ] **Update-Adresse** eintragen (Phase 2, P9), bevor andere PCs spielen.
- [ ] **Abnahme** nach Spieltest: ABGENOMMEN oder NICHT VOLLSTÄNDIG ABGENOMMEN (`SCRUM/BACKLOG.md` Sprint 5).

---

## Phase 8 – Fehlendes bis zum Release (Sprint 7)

Die fünf wichtigsten Lücken, abgeleitet aus Projektstand und Release-Recherche (Details in `SCRUM/BACKLOG.md`, Sprint 7).

- [ ] **7.1 Spieltest-Fundament:** Smoke-Test und Messprotokoll liegen in `FEEDBACK-LOG.md`. Durchführung durch Leon. [B]
- [ ] **7.2 Mehrspieler:** Koop-Testprotokoll (Lootr, Inselmarkt, Startinventar, Spike) in `FEEDBACK-LOG.md`. Test mit zwei Spielern. [B]
- [x] **7.3 Quest-Sackgassen:** Mekanism-Ketten Akt II und III geprüft (25.10.2026). Keine Sackgasse. Drei Quests (Polonium-Pellet, Herzschlag/Antimaterie, MekaSuit) laufen über den Fission-Reaktor (Spätspiel, herstellbar).
- [x] **7.4 Endgame:** Entwurf in `GAME_DESIGN.md`. Vorschlag A umgesetzt: Abschluss-Feier „Das Archiv ist vollständig“ (`p_archiv`). B ist mit den Prüfungen der Leere (4 Quests) bereits vorhanden. C offen (Spike).
- [ ] **7.5 Verteilen:** Release-Checkliste und Installationsanleitung vorbereiten. Update-Adresse (P9) und Hosting-Entscheidung liegen bei Leon. [B]

---

## Phase 9 – Einzelspieler-Start und Spielspaß (Prüfung 25.10.2026, 22:30)

Quelle: Simulation der ersten 60 Minuten (aus Dateien, nicht gespielt), Gesamtprüfung von Code und Logik, Recherche erfolgreicher Modpacks. Details in `PRUEFBERICHT_1.0.0.md`. Koop folgt erst kurz vor dem Release (7.2).

**A Blocker in den ersten 30 Minuten**
- [x] **9.1 Holz:** Q2 „Der erste Baum“ verlangt 5 Stämme (`bausteine.py`), Questtext und beide Handbuch-Funktionen auf 5 gesetzt. Umgesetzt 26.10.2026, Generator 0 Layoutprobleme, nicht im Spiel geprüft.
- [x] **9.2 Seidenraupe:** Q3 „Seidenraupe“ gibt bereits 2 Silkworm (`bausteine.py`, `e_raupe`), der Startquest ebenfalls 1. Kein Code nötig, im Spiel prüfen.
- [x] **9.3 Obsidian:** Warnzeile zur einzigen Lava-Quelle und Hinweis „Diamantspitzhacke“ in `j_obsidian` ergänzt (`texte_hauptstory.py`). Umgesetzt 26.10.2026, nicht im Spiel geprüft.

**B Logikfehler im Code**
- [x] **9.4 Pilz-Gimmick:** Entscheidung Leon 26.10.: Pilze essbar machen. `kubejs/startup_scripts/pilze_essbar.js` (1 Hunger, immer essbar, API im KubeJS-Jar geprüft). Server-Register (`dev_pruefdaten.json`) zeigt beide Pilze als Essen, Prüfsuite prüft das (`daten.pruefe_essen`). Im Spiel NICHT GETESTET.
- [x] **9.5 Lagerfeuer:** Partikel jetzt mit `execute as … at <Spieler>` (`lagerfeuer.js`). Umgesetzt 26.10.2026, NICHT im Spiel geprüft.
- [x] **9.6 Pilz-Text:** Untertitel auf `title … actionbar` umgestellt (`pehkui_pilze.js`). Umgesetzt 26.10.2026, NICHT im Spiel geprüft.
- [x] **9.7 Holzkiste:** `exdeorum:string_mesh` aus der Holzkiste in `quests.py` entfernt. Generator neu gelaufen, `holz.snbt` ohne Eintrag. Umgesetzt 26.10.2026.

**C Texte und Rezepthinweise (Akt I)**
- [x] **9.8** Q1 hat 14 Zeilen (TEXTSTIL erlaubt 6). Kürzen, JEI einführen (R = Rezept, U = Verwendung). Jobs+, Markt und Team stehen schon im Handbuch.
  Q1 auf 4 Zeilen gekürzt, JEI-Hinweis (R/U) drin. Jobs+ und Markt stehen im Handbuch, die Tipps zu Bäumen und Wasser entfallen. 26.10.2026, nicht im Spiel geprüft.
- [x] **9.9** Faden: Das String Mesh braucht 9 Faden, Q3 verlangt 8. Das Flint Mesh kostet 5 Faden und 4 Feuerstein und ist kein Upgrade. Beides in Q3, Q7 und Q11 nennen.
  Faden-Zahlen in Q3 (String Mesh 9 Faden), Q7 (9 Faden) und Q11 (Flint Mesh 5 Faden + 4 Feuerstein, kein Upgrade) ergänzt. 26.10.2026.
- [x] **9.10** Eisen: Q10 verlangt 4 Brocken, Q12 braucht 8 (2 Barren). Zahl angleichen, Ofen und Brennstoff nennen.
  Q10 verlangt 8 Erzbrocken (vorher 4). Das ergibt 2 Erz für die 2 Eisenbarren in Q12. Ofen und Brennstoff stehen im Text. 26.10.2026.
- [x] **9.11** Create: Kein Text erklärt das Andesite Casing (entrindeter Stamm + Andesitlegierung). Hinweis in Q19, 2 Casings als Belohnung in Q18.
  Andesite Casing als Hinweis in Q19 (Mühlstein) und 2 Casings als Belohnung in Q18 (Wasserrad). Rezept aus TODO übernommen, nicht im Jar geprüft. 26.10.2026.
- [x] **9.12** Q25 verweist auf die gestrichene Pilzinsel. Satz streichen.
  Satz über die Pilzinsel aus Q25 gestrichen. 26.10.2026.
- [x] **9.13** Q8 und Q9 sind Sackgassen: als optional markieren. In Q9 das Rezept nennen (Clay + Knochenmehl).
  Q8 (Tiegel) und Q9 (Lava-Tiegel) als optional markiert. Q9 nennt jetzt das Rezept: Porzellanton (Tonkugel + Knochenmehl) im Muster, gegen exdeorum-Jar geprüft. 26.10.2026.
- [x] **9.14** Namen vereinheitlichen: Silkworm, Flint Mesh, Crook. Im Handbuch steht noch „Seidenraupe“ und „Feuernetz“, der Crook fehlt dort.
  Handbuch nutzt Silkworm, Flint Mesh und Crook wie die Questtexte. 26.10.2026.

**D Balance (Verdacht, erst messen)**
- [B] **9.15** Q16 Kupfer und Zink: rund 100–200 Kies. Kupfer auf 2 senken oder den Bedarf im Text nennen.
  Verdacht, nicht geändert. Kupfer und Zink brauchen eine Messung (Spieltest), siehe Phase 4.
- [B] **9.16** Q13 Inferium: 16 Essenz kosten rund 160 Erde, also etwa 1300 Laub. Aufgabe auf 8 senken oder die Siebchance erhöhen.
  Verdacht, nicht geändert. Inferium-Kosten brauchen eine Messung (Spieltest), siehe Phase 4.

**E Dokumente**
- [x] **9.17** README, CLAUDE.md und TODO nennen noch 0.20.0. `pack.toml` steht auf 1.0.0.
  Versionsangaben in README, CLAUDE.md und TODO auf 1.0.0 gesetzt (laut pack.toml). 26.10.2026.
- [x] **9.18** GAME_DESIGN nennt 17 Tausch-Quests (Ist: 19). Die Zeilen zur Gold- und Sternkiste sind veraltet.
  GAME_DESIGN nennt 19 Tausch-Quests. Zeilen zu Goldkiste (Messing-Kiste seit 25.10.) und Sternkiste (Netheritbarren entfernt) aktualisiert. 26.10.2026.
- [x] **9.19** Die Begründung für 8.3 ist falsch: `sieben.js` hängt bereits Zusatzrezepte mit derselben Zutat und demselben Netz an (Inferium aus Erde). Die Entscheidung neu bewerten.
  Begründung für 8.3 neu geprüft: Die alte Begründung stimmt nicht, sieben.js hängt schon Zusatzrezepte mit gleicher Zutat und gleichem Netz an. Die Entscheidung ist damit nicht mehr belegt. Neubewertung durch Leon offen.
- [x] **9.20** `CHANGELOG_1.0.0.md` war im Paket. Seit 25.10. in `.packwizignore`. Beim nächsten `refresh` und Export fällt die Datei weg.
- [x] **9.21** `SCRUM/BACKLOG.md`, Zeile 127: Der Satz „keine neuen Gimmicks bis 7.1 bis 7.3 geklärt sind“ ist ersetzt. Neue Gimmicks sind jetzt erlaubt, mit Ladeprüfung je Eintrag. Umgesetzt 26.10.2026.

**F Prinzipien aus der Recherche** (SkyFactory 4, StoneBlock, ATM, FTB Revelation u. a.)
- Schneller, belohnender Einstieg, ohne unerklärte Schritte (→ A und C).
- Kurze Questtexte, die das Rezept nennen (→ C).
- Spürbare Meilensteine (Feiern sind vorhanden), nützliche Belohnungen (→ 9.2, 9.11).
- Kein Grind als Pflicht (→ D), Stabilität vor Effekten.

## Phase 10 – Startausrüstung, Lootkisten und Beute (Wunsch Leon, 25.10.2026)

Ziel: Der Einstieg soll mit passenden Startitems beginnen, überflüssige und spielbrechende Items fallen weg, und Lootkisten werden spannender mit mehr seltener, thematischer Beute. Balance-Regeln bleiben: Gewichte und Preise erst nach Messung oder Spieltest, Entfernen nur mit Beleg (CLAUDE.md, Regeln 2 und 9).

**A Startausrüstung**
- [ ] **10.1 Startitems auswählen:** Nur Items, die den ersten Schritt tragen (Baum, Sieb, erster Eisenbarren). Pro Startinsel (Klassisch, Waldlichtung) prüfen, ob das Item dort gebraucht wird. Startinventar bleibt `spawn` (pro Spieler).
- [x] **10.2 Überflüssige Startitems streichen:** Eis aus dem Startinventar entfernt (kein Quest braucht es, `erreichbar.py` angepasst). Crook steht nicht im Startinventar, der Eintrag in der Vault-Liste war falsch. Lava- und Wassereimer sind ebenfalls raus (26.10., Entscheidung umgesetzt): Der Bruchstein-Schritt braucht jetzt einen Eisen-Eimer (3 Barren), siehe Phase-1-Punkt „Klassische Insel ohne Eimer“.
- [ ] **10.3 Schrankencheck:** Jedes neue oder behaltene Startitem gegen `_src/sperren.py` und die Stufenliste aus `GAME_DESIGN.md` prüfen. Kein Startitem darf eine spätere Schranke überspringen (Regel 8).

**B Überflüssige und spielbrechende Items entfernen**
- [ ] **10.4 Liste mit Belegen:** Stand 26.10.2026, aus Dateien geprüft (nicht im Spiel). Gefunden:
  - `exdeorum:string_mesh` in der Holzkiste (`reward_tables/holz.snbt`, Zeile 109). Überspringt die Faden-Schranke. Dubletten zu 9.7, dort erledigen.
  - `minecraft:netherite_scrap` in der Sternkiste (`reward_tables/stern.snbt`, Zeile 38) und als Belohnung bei `j_wither` und `z_fabrik` (`_src/belohnungen.py`). Netheritbarren wurden schon entfernt (`IMPLEMENTATION_LOG.md`, Zeile 329), der Schrott bleibt, weil er die Pipez-Sperre `#c:ingots/netherite` nicht erfüllt. Der alte Punkt „Netherit aus der Sternkiste“ in Phase 4 ist damit teilweise veraltet. Entscheidung offen, ob der Schrott bleibt.
  - Startinventar (`config/skyblockbuilder/starter_inventory.json5`): `minecraft:lava_bucket`, `minecraft:water_bucket`, `minecraft:ice`. Eis und beide Eimer sind jetzt raus (Stand 26.10.). Im Questbuch (`data.snbt`) fand die Suche nach Eimer, Eis und Lava keinen Treffer, Kapitel-Dateien sind noch nicht geprüft.
  - Startinventar: `minecraft:bone_meal` ×16 und `exdeorum:wooden_watering_can`. Prüfen, ob sie den Baum (9.1) oder das Sieb überspringen.
  - Kein Crook im Startinventar. Die Crook-Erwähnung in 10.2 bezieht sich auf die Vault-Liste und muss dort korrigiert werden.
  - Noch offen: Die Rezeptsimulation (`_src/rezept-sim/REZEPT-SIM.md`) auf unbegrenzte Quellen prüfen. Erst danach ist die Liste vollständig.
- [x] **10.5 Entfernen umsetzen** (Teil 26.10.2026: Eis aus Startinventar und `erreichbar.py`, `string_mesh` aus der Holzkiste; Bruchstein-Schranke unverändert). Offen bleiben die Punkte aus 10.4 mit Entscheidung (Netherit-Schrott, Eimer): In `bereinigung.js` bzw. `_src/sperren.py` mit Kommentar und Beleg. Danach Pflichtprüfung: Generator, Testserver-Start, `0 fehlgeschlagene Rezepte`, `packwiz refresh`, Eintrag in `IMPLEMENTATION_LOG.md`.

**C Lootkisten aufwerten (Lootkosten)**
- [ ] **10.6 Lootkisten-Gestaltung:** Namen, Tooltips und Hinweise für Lootkisten und Lootr-Truhen im Stil von `_src/TEXTSTIL.md` ausbauen, damit jede Kiste nach einer Kiste aussieht und einen Anlass hat.
  - [x] Umgesetzt 26.10.2026 (Freigabe Leon): Tooltip je Kiste (Stimmung + Herkunft) aus `_src/hinweise_daten.py` (`KISTEN`), erzeugt in `kubejs/client_scripts/hinweise.js` über einen dynamischen Tooltip auf die Komponente `ftbquests:loot_crate`. Der Generator prüft die Herkunft gegen die Drop-Gewichte. Client-Skript im Spiel NICHT GETESTET.
- [x] **10.7 Lootkosten-Modell:** Entscheidung Leon 26.10.: kein Preis.

**D Mehr spezielle, coole Beute**
- [ ] **10.8 Seltene Beute je Akt:** Stand 26.10.2026: nicht umgesetzt, weil neue Tabellen Gewichte und Designentscheidungen brauchen (Regel 9). Vorschlag zur Freigabe: je Akt eine kleine Zusatztabelle für Ruinen-Truhen (`skyandstone:ruinen/fund`), Items nur aus bestehenden Mods, Gewicht erst nach Messung. Vorher Liste mit Leon abstimmen. Ursprünglicher Plan: Eigene Beutetabellen mit seltenen, thematischen Items pro Akt (Ruinen-Truhen, Mob-Kisten, Sternkiste). Nur Items aus bestehenden Mods, keine neuen Mods ohne Freigabe (CLAUDE.md).
- [x] **10.9 Story-Beute:** 26.10.2026: eigener Pool in `ruinen/fund.json`, jede Ruinen-Truhe gibt eins von vier Erinnerungsstücken (Inselkarte/Papier, Liedscherbe/Plattenfragment 5, Wappen/Globus-Bannervorlage, Namensschild) mit Story-Zeile. Übrige Pools unverändert. Im Spiel NICHT GETESTET.
- [B] **10.10 Reihenfolge:** Entscheiden, welche Beutequelle zuerst ausgebaut wird. Gewichte erst nach Messung der Mob-Kisten-Rate (Phase 4) ändern.

---

## Phase 11 – „Die sieben Splitter“ (Version 1.1.0, Wunsch Leon 26.10.2026)

Ziel: Die Hauptstory bekommt einen roten Faden, in dem alle großen Mods zusammenarbeiten. Design: `_src/DESIGN-HERZ-DER-LEERE.md`.

- [x] **11.1 Eigene Items und Blöcke** (`kubejs/startup_scripts/herz_items.js`): 7 Splitter, Rohling, Leerenessenz, Karte, Wächterkern, Herz (schlafend/erwacht), Herzsockel (heil/zerbrochen). Eigene Pixel-Art (`_src/texturen.py`), Namen de/en.
- [x] **11.2 Cross-Mod-Rezepte** (`kubejs/server_scripts/herz_rezepte.js`): Create-Mixer (beheizt, überhitzt), Powah-Orb, AE2-Gravurmaschine, Farmer's-Delight-Kochtopf, Ars-Apparat/Imbuement oder IF-Auflösungsapparat/Mekanism-Kernsynthesizer, Create-Mechanical-Crafting fürs Herz. 12 Rezepte im Server geladen.
- [x] **11.3 Die vergessene Werkstatt**: Struktur (`_src/werkstatt.py`), Karte als Belohnung für den ersten Flug, Lootr-Truhe mit Bauplan des Herzens.
- [x] **11.4 Der letzte Wächter**: Bosskampf (riesiges Wither-Skelett über Pehkui, 400 Leben, Bossleiste, zwei Phasen mit Leerenschatten, Rückholung, Abbruch). Sieg setzt das Herz auf „erwacht“. Täglicher Herzschlag (Eile, Regeneration, Glück). Datapack aus `_src/herz_daten.py`, Skript `herz_ritual.js`.
- [x] **11.5 Questbuch**: 15 neue Quests (`sp_*`, `hz_*`) in Akt I–III, 5 neue Tagebuch-Notizen, Aufgabentypen Beobachten und Fortschritt.
- [B] **11.6 Spieltest**: Splitter-Rezepte im Spiel herstellen, Werkstatt per Karte setzen, Bosskampf auf einer echten Insel (Schwierigkeit, Rückholung, Bossleiste), Herzschlag, Tooltips/Texturen im Client. Mengen nach Messung anpassen.
- [ ] **11.7 Ideen für später** (aus Brainstorming und FreeLLMAPI): zweiter Boss in den Nether-Festungen („Der Archivar“), Wahl-Folgen als eigene Questreihen je Weg, Leerenschatten-Nächte als optionales Ereignis.

---

## Erledigt (zur Kontrolle, nicht neu anfassen)

- ProductiveBees-Rezept mit fehlendem Modularbees-Item entfernt (`bereinigung.js`, 0.11.1).
- Erster Eisenbarren: 2 statt 4 (`_src/bausteine.py`, Quest `e_eisen`).
- Startinventar bleibt `spawn` (pro Spieler), Entscheidung aus der Vollprüfung.
- Bienen-Zentrifuge: Mystical-Essenz-Rezepte entfernt (`balance.js`).
- AdvancedAE entfernt (Fehler `extendedae:crystal_assembler`).
- Lootr und Jobs+ mit Abhängigkeiten (0.20.0), Testserver-Start bestanden.
- Startinseln auf zwei reduziert.
- Quest-ID-Prüfung: 828 IDs, 0 entfallen (`_src/idcheck.py`).
- Erzmagier-Buch hängt zusätzlich an der Chimera-Quest. Sammlerbuch-Untertitel auf „Freiwillig“.
- Serverstart auf Java 21 bestanden (`TEST_REPORT.md`).
- Spike-Ladeteil bestätigt (Skript lädt ohne Fehler). Wirkung nicht geprüft.
- Wirtschaftsmods bewusst nicht eingeführt (würden mit den Quest-Belohnungen konkurrieren).

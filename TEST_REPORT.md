# Testbericht Sky and Stone (Phase E, Stand 25.10.2026)

> Korrekturhinweis 25.10.2026 (21:40): Die Tabellen unten sind Protokoll und enthalten ältere Stände (186 Quests, 6 Startinseln, 17 JSON-Dateien). Aktuell: 185 Quests, 2 Startinseln, 19 Tausch-Quests. Ein Singleplayer-Lauf in Prism am 25.10. (19:18–19:44, Spieler LAB6, integrierter Server 1.21.1) ist im Prism-Protokoll belegt. Er wurde aber nicht als Test ausgewertet.

Nur aufgeführt, was tatsächlich ausgeführt wurde. Alles andere steht unter „Nicht ausgeführt“.

## Ausgeführt

| Prüfung | Stand | Ergebnis | Quelle |
|---|---|---|---|
| Quest-Generator (`python -I -X utf8 _src/quests.py`) | 0.11.2 und 0.20.0 | 186 Quests, 20 Kapitel, 0 Layoutprobleme. Ablehnung bei Haken-Aufgaben in zwei Versuchen korrekt ausgelöst. | Konsolenausgabe |
| Testserver-Start, Pack-Stand 0.11.0 | 25.10. ~11:12 | `Done (0.991s)`, 0 fehlgeschlagene Rezepte, Rezeptfehler ProductiveBees/Modularbees sichtbar | `logs/latest.log` |
| Testserver-Start, 0.11.1 mit `bereinigung.js` | 25.10. ~13:33 | `Done (2.240s)`, Rezeptfehler weg, KubeJS 9/9 ohne Fehler | Startlog |
| Testserver-Start, 0.11.2 (Starttext) | 25.10. 17:08 | `Done (1.012s)`, 186 Quests geladen, KubeJS 9/9 ohne Fehler, 0 fehlgeschlagene Rezepte | Startlog |
| Testserver mit Lootr allein | 25.10. 17:31 | `Done (1.644s)`, keine Fehler | Startlog |
| Testserver mit Jobs+ | 25.10. 17:34 | Start brach ab: YAML Config fehlte (Pflicht). Nach Nachrüstung 17:40 `Done (1.317s)`. Zwei Fortschritts-Fehler von When Dungeons Arise (nicht übernommen). | Startlog |
| Testserver-Start, Pack-Stand 0.20.0 | 25.10. 17:47 | `Done (1.053s)`, 186 Quests, KubeJS 9/9, 0 fehlgeschlagene Rezepte, Lootr/Jobs+/Arc/UI Lib/Item Restrictions geladen | Startlog |
| Spike Stufen-Abfrage (KubeJS-Skript) | 25.10. 16:43 | Skript lädt, 0 Fehler beim Start. Craft-Handler nicht ausgelöst. | Startlog |
| Downloads von Modrinth | 25.10. | SHA-1 jedes Downloads gegen API-Angabe geprüft, alle stimmen | Shell |
| packwiz refresh und Mrpack-Export | 0.11.1, 0.11.2, 0.20.0 | Index aktualisiert, Mrpack exportiert, Inhalt geprüft (Skript im Archiv) | Shell |

## Nicht ausgeführt
- **Client-Start in Prism:** nicht möglich in dieser Umgebung. Wenn der Start im Spiel klappt, ist das noch nicht geprüft.
- **Multiplayer und Koop:** kein zweiter Spieler.
- **Java 21:** Test lief mit Java 25.0.4. Das Zielniveau 21 ist nicht getestet.
- **Performance unter Last:** keine RAM- oder FPS-Messung. Die Werte aus dem Playtest sind offen.
- **Lootr im Spiel:** ob jeder Spieler eigene Beute bekommt, ist nicht geprüft.
- **Jobs+ im Spiel:** Bedienung und Balance nicht geprüft.
- **Gameplay-Balance:** Mittel-Frühspiel-Zeit, Goldkiste, Sternkiste, Inselmarkt. Alles nur Verdacht aus Code und Daten.
- **Stufen-Abfrage für wegabhängige Rezepte:** Spike nur teilweise.
- **Automatisierte Tests:** Es gibt keine Testdateien im Projekt. Prüfungen laufen über den Generator und den Serverstart. Eine Testsuite wäre ein eigenes Arbeitspaket.

## Bekannte Warnungen im Log (nicht bearbeitet)
- Curios: Slot-Typen `example` und `feet` nicht registriert.
- Mixin-Warnungen zu Klassen von nicht installierten Mods (Quark, ExtendedAE, Simulated, Sable).

## Fazit
Der Serverstart ist für den aktuellen Stand stabil. Ob das Spiel im Client angenehm läuft und die Balance stimmt, ist nicht bewiesen und braucht den Spieltest.


## Abnahmeprüfung 25.10.2026 (Stand 0.20.0)

Gesamturteil: **NICHT VOLLSTÄNDIG ABGENOMMEN.** Grund: kein Client-Test, kein Spieltest, keine Lastmessung. Unten steht nur, was tatsächlich ausgeführt wurde.

### Ausgeführte Prüfungen

| # | Prüfung | Ergebnis | Status |
|---|---|---|---|
| 1 | JavaScript-Syntax aller 8 Server-/Client-Skripte (`node --check`) | Keine Fehler | BESTANDEN |
| 2 | JSON-Parse aller 17 JSON-Dateien in kubejs/ und config/ | 0 Fehler | BESTANDEN |
| 3 | `python -I -X utf8 _src/layoutcheck.py` | Exit 0, keine Ausgabe | BESTANDEN (Exit-Code; keine Detailausgabe) |
| 4 | Testserver-Log latest.log (Lauf 17:53, Stand 0.20.0) | 20 Kapitel, 186 Quests, 7 Belohnungstabellen geladen. KubeJS Server 9/9 Skripte ohne Fehler, 0 fehlgeschlagene Rezepte. 6 Startinseln geladen. | BESTANDEN |
| 5 | Mod-Abgleich mods/*.pw.toml gegen Testserver-Jars | 124 Pack-Einträge, 111 Server-Jars. Die 13 fehlenden sind Client-Mods (Sodium, Iris, Mouse Tweaks u. a.). | BESTANDEN |
| 6 | Serverstart mit Lootr und Jobs+ | Start im Log bestätigt, `Done (1.618s)` | BESTANDEN |
| 7 | Serverlog auf ERROR und Exception | 3 ERROR-Zeilen: Curios „example“ und „feet“ nicht registriert. Keine Exceptions. | FEHLGESCHLAGEN (Warnung, nicht behoben) |
| 8 | Rezept-Warnungen | ironfurnaces upgrade_unobtainium und upgrade_vibranium fallen auf Vanilla zurück (Komponente pattern&lt;optional_ingredient&gt;). advanced_ae quantum_processor_eae übersprungen (unbekannter Typ extendedae:crystal_assembler). KubeJS meldet trotzdem 0 fehlgeschlagene Rezepte. | FEHLGESCHLAGEN (ungeklärt) |
| 9 | Mixin-Warnungen | 5 Klassen von nicht installierten Mods (Quark, ExtendedAE, Simulated, Sable). | NICHT GETESTET (Auswirkung offen) |
| 10 | Spike Stufen-Abfrage (spike/zz_spike_stages.js) | Skript lädt. Craft-Handler und Stufen-Wert nicht geprüft. | NICHT GETESTET |

### Blockiert oder nicht durchführbar

| Prüfung | Status | Grund |
|---|---|---|
| Client-Start in Prism, Welt betreten, Quest-Konfiguration laden | BLOCKIERT | Kein Client in dieser Umgebung |
| Spielstart, erste Ressourcenproduktion, Maschinenketten, Questfreischaltungen, Automatisierung, Endgame | NICHT GETESTET | Nur mit Spieler im Spiel möglich |
| Stuck-Quest-Test bei Item-Gruppen | NICHT GETESTET | Braucht Spieler |
| Wahlen Akt III (Stufen-Folgen) | BLOCKIERT | Spike unvollständig |
| Multiplayer, Koop, Questteams | NICHT GETESTET | Kein zweiter Spieler |
| Performance: 16 GB, 5–6 GB Minecraft-RAM, Iris Xe, Sichtweite 8, Simulation 6, 140 Mobs, 20 TPS | BLOCKIERT | Keine Zielhardware, kein Client, keine reproduzierbare Messung. Ein Serverstart ist keine TPS-Messung. |
| Java 21 (Zielversion) | BESTANDEN (Serverstart, Stand 25.10. 19:12 und später) | Frühere Läufe mit Java 25; ab Abnahme-Lauf Java 21 im Testserver |
| Lootr-Truhen und Jobs+ im Spiel | NICHT GETESTET | Spieltest |

### Fehler und Restrisiken
- Curios-Slot-Typen „example“ und „feet“: Herkunft nicht gefunden. Nicht behoben.
- Rezept-Fallbacks ironfurnaces und extendedae: Auswirkung im Spiel unbekannt.

### Keine Stabilitäts-, Multiplayer- oder Performancegarantie
Diese Prüfung trifft keine Aussage zu Stabilität, Multiplayer oder TPS im Spiel.

## Endstand Prüfung 25.10.2026 19:12 (nach Entscheidungen)
- Testserver (Java 21, ohne AdvancedAE-Jar, ohne Test-Dump-Skript zz_dev_recipes.js): Done 1.167s, KubeJS 9/9 ohne Fehler, 186 Quests, 20 Kapitel.
- Verbleibende Warnungen: Curios example/feet (Industrial Foregoing, harmlos), ironfurnaces upgrade_unobtainium/vibranium (Bedingungsrezept, allthemodium nicht installiert, Vermutung harmlos).
- RuntimeDistCleaner-Fehler war Folge des Test-Dump-Skripts (Rhino-Reflexion auf Create-Klasse), nicht des Packs. Nach Entfernen weg.
- Nicht getestet: Gesamtrezept-Simulation (kein vollständiger Dump), Spieltest, Koop.

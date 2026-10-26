# Feedback-Log Sky and Stone

Stand: 25.10.2026 · Gehört zu Sprint 7 (7.1 und 7.2) in `SCRUM/BACKLOG.md`.

Hier steht jeder Befund aus Spieltests, mit Version. Ein Befund ohne Version ist wertlos, weil Quests und Balance sich zwischen den Versionen ändern.

## Smoke-Test (vor jedem Spieltest, ca. 15 Minuten)
1. Prism startet die Instanz „Sky and Stone“ und holt den aktuellen Stand (Pre-Launch-Hook ohne Fehler).
2. Neue Welt mit Welttyp „Skyblock“ und einer der beiden Startinseln (Klassisch, Waldlichtung).
3. Questbuch öffnet sich, die Start-Quest ist nicht sofort erledigt.
4. Eine Quest mit Gegenstandsabgabe lässt sich abschließen, Belohnung ist abholbar.
5. Meilenstein-Feier (Titel, Ton, Feuerwerk) bei einer Quest mit Feier.
6. Tod und Wiederbelebung: Der Wächter-Spruch erscheint.
7. Log (`latest.log` der Instanz): keine neuen ERROR-Zeilen aus dem Pack. Bekannt: Curios-Slots „example“ und „feet“.
8. Leistung nach 10 Minuten: `/spark tps`, RAM in Prozent, F3-FPS. Ziel 20 TPS, RAM unter 80 %.

## Koop-Test (Sprint 7.2, zwei Spieler auf einem Server)
- Team anlegen, zweiter Spieler tritt bei.
- Lootr: Jeder Spieler bekommt eigene Beute aus derselben Truhe?
- Inselmarkt: Eine Kiste pro Team bei Tausch, Abklingzeit gilt für beide.
- Startinventar: Bekommt jeder Spieler sein Startinventar (`spawn`, pro Spieler)?
- Spike Stufen-Abfrage (`spike/zz_spike_stages.js`): Spieler A mit Stufe, Spieler B ohne.

## Befunde
| Datum | Version | Wer | Befund | Schwere (hoch / mittel / niedrig) | Status |
|---|---|---|---|---|---|
| 25.10.2026 | 0.20.0 | Claude (Vorprüfung) | Starbuncle-Quest war nicht lösbar, entfernt | hoch | erledigt |
| | | | | | |

## Spieler-Feedback (Leon)
| Datum | Version | Befund | Schwere | Status |
|---|---|---|---|---|
| 25.10.2026 | 0.11.0 | Jobs+-Erklärung unverständlich, Taste unklar | mittel | erledigt (Starttext neu) |
| 25.10.2026 | 0.11.0 | Startinseln: Klassisch zu klein | mittel | erledigt (Klassisch vergrößert, Sprint 1.5) |

Prüfbericht: Minecraft-Modpack „Sky and Stone“ – Version 0.10.0
Prüfmaßstab: Game Design, Progression, technische Zuverlässigkeit, Wartbarkeit und Spielbarkeit im Solo- und Koop-Modus
1. Gesamturteil
„Sky and Stone“ hat das Potenzial, ein eigenständiges Progression-Modpack zu werden, statt nur eine gut zusammengestellte Modsammlung zu sein. Die stärkste Grundlage ist die Verbindung aus einer nachvollziehbaren Weltgeschichte, gezielt veränderten Rezepten, einem generierten Questbuch und mehreren bewussten Entscheidungen vor dem Finale. Besonders die Kopplung von Mystical Agriculture an Create, Mekanism und AE2 kann dafür sorgen, dass unterschiedliche Mods tatsächlich Teile eines gemeinsamen Spiels werden. Gleichzeitig ist Version 0.10.0 noch eher ein technisch vielversprechender Prototyp als ein nachweislich rundes Spielerlebnis: Der Serverstart und die Rezeptprüfungen sind wertvoll, aber ohne echten Client-Spieltest sind Questfluss, Verständlichkeit, Bedienbarkeit und Frustpotenzial noch nicht ausreichend validiert. Meine Empfehlung: keine neuen großen Inhalte hinzufügen, bevor ein vollständiger Durchlauf vom ersten Sieb bis zum Finale funktioniert und die zentralen Systeme im tatsächlichen Spiel zusammenpassen.

Eine wichtige Einschränkung vorweg: Du hast die Projektstruktur und den aktuellen Stand ausführlich beschrieben, aber nicht die tatsächlichen Dateien angehängt. Ich kann deshalb eine fundierte Architektur- und Designprüfung durchführen, jedoch keine konkreten Zeilennummern, Python-Funktionen, JSON-Ausgaben oder KubeJS-Aufrufe verifizieren. Wo ich einen möglichen Fehler benenne, unterscheide ich ausdrücklich zwischen einem aus der Beschreibung ableitbaren Risiko und einem Fehler, der erst durch Prüfung der Dateien nachweisbar wäre.
2. Fehler und Risiken – nach Schwere geordnet
1 · Hoch
Kein vollständiger Client-Durchlauf

Betroffen: gesamtes Projekt; insbesondere quests.py, questlib.py, ftbformat.py, sieben.js, balance.js

Status: Sicher bestehende Prüflücke, kein nachgewiesener Modfehler.

Ein erfolgreicher Serverstart und null fehlgeschlagene Rezepte beweisen nicht, dass das Pack spielbar ist. Sie sagen beispielsweise nichts darüber aus, ob Questbedingungen auslösbar sind, Items korrekt erkannt werden, Maschinenrezepte im richtigen Arbeitsablauf funktionieren oder Fortschrittsdaten nach einem Neustart erhalten bleiben.

Behebung: Einen echten Durchlauf mit einem frischen Spielerprofil durchführen. Mindestens Startinsel, Sieben, Create-Sifter, Stromversorgung, Essenzstufen, AE2-Autocrafting und Finale müssen jeweils praktisch abgeschlossen werden.



2 · Hoch
Progressionssperren könnten an der falschen Stelle greifen

Betroffen: sperren.py, belohnungen.py, quests.py

Status: Vermutung; anhand der Beschreibung nicht nachweisbar.

Die Sperren gegen übersprungene Stufen sind eine gute Idee. Sie können aber nur zuverlässig sein, wenn sie nicht bloß Belohnungen, sondern auch alternative Bezugswege und Rezeptvarianten berücksichtigen. Ein Rezept, das eine gesperrte Komponente umgeht, macht eine korrekte Questbelohnungskontrolle wirkungslos.

Behebung: Eine zentrale Progressionsmatrix als maschinenlesbare Quelle anlegen. Für jede Stufe werden Voraussetzungen, erlaubte Herstellungsmethoden, Questfreischaltungen und verbotene Umgehungen definiert. Die Tests prüfen nicht nur Belohnungen, sondern auch erreichbare Herstellungswege.



3 · Hoch
Die Essenzstufen hängen möglicherweise an zu wenigen Rezepten

Betroffen: balance.js, sieben.js, quests.py, hinweise.js

Status: Konkretes Designrisiko, kein bestätigter Fehler.

Tertium über Create, Imperium über Mekanism, Supremium über AE2 und Insanium über einen Ultimate-Schaltkreis zu führen, verbindet die Mods sinnvoll. Entscheidend ist aber, ob diese Bindung über alle tatsächlich verfügbaren Rezepte hinweg gilt. Wenn ein alternativer Crafting-Weg, ein Duplikat oder ein unerwarteter Bezugsweg die Stufe umgeht, wird die beabsichtigte Progression unterlaufen.

Behebung: Alle Rezeptvarianten der vier Stufen aus den geladenen Rezeptdaten prüfen. Zusätzlich gezielt nach alternativen Quellen für Zwischenprodukte und Endprodukte suchen. JEI-Informationen müssen die tatsächlich gültigen Wege erklären.



4 · Hoch
FTB-Quests-Ausgabe kann strukturell korrekt, aber inhaltlich inkonsistent sein

Betroffen: ftbformat.py, questlib.py, layoutcheck.py, quests.py

Status: Vermutung.

Der eigene Generator ist langfristig ein großer Vorteil. Er ist aber auch eine zentrale Fehlerquelle: falsche Referenzen, doppelte IDs, nicht vorhandene Abhängigkeiten, ungültige Aufgabenbedingungen oder inkonsistente Kapitelverweise können eine Ausgabe erzeugen, die teilweise geladen wird, aber nicht wie beabsichtigt funktioniert.

Behebung: Nach jedem Build zusätzlich IDs auf Eindeutigkeit, alle Referenzen auf Existenz, Voraussetzungen auf gültige Ziele und Aufgaben auf definierte Item- oder Eventbedingungen prüfen. Die generierten Dateien anschließend unabhängig vom Generator erneut einlesen und validieren.



5 · Hoch
Die beiden Entscheidungsquests könnten nur erzählerische Entscheidungen sein

Betroffen: quests.py, belohnungen.py, sperren.py, gegebenenfalls balance.js

Status: Offene Designfrage.

„Maschine oder Magie“ und „Erz ohne Sieb“ sind starke Ansatzpunkte. Wenn beide Wege aber anschließend dieselben Kosten, dieselben Freischaltungen und dieselben Belohnungen liefern, fühlt sich die Wahl nicht wirklich bedeutsam an. Umgekehrt wäre eine dauerhaft schlechtere Route problematisch.

Behebung: Für jede Option festhalten, was sie konkret verändert: Produktionsmethode, Ressourcenkosten, Komfort, Bauaufwand oder spätere Questbelohnungen. Beide Wege sollten lebensfähig bleiben und unterschiedliche Vorteile bieten.



6 · Mittel
Die Startinseln könnten unterschiedliche Startbedingungen erzeugen

Betroffen: inseln.py, Skyblock Builder, quests.py

Status: Vermutung; abhängig von den sechs tatsächlichen Inseldefinitionen.

Sechs Startinseln sind eine Chance zur Personalisierung. Wenn sie jedoch unterschiedliche Ressourcen, Blockmengen oder zugängliche Rohstoffe enthalten, kann die frühe Progression unbeabsichtigt leichter oder schwerer werden.

Behebung: Alle sechs Inseln mit einem gemeinsamen Mindeststandard testen: notwendige Startressourcen, Überlebensfähigkeit, erreichbare Grundrezepte, Questlösbarkeit und Rückkehrmöglichkeiten. Unterschiede sollten bewusst gewählte Spielstile ermöglichen, keine versteckten Schwierigkeitsgrade.



7 · Mittel
Leistung im echten Spiel ist noch nicht belegt

Betroffen: Modpack-Konfiguration, Leistungsmods, Maschinen- und Mob-Setups

Status: Sicher bestehende Prüflücke.

20 TPS bei 140 Mobs sind ein positives Signal für diesen Lasttest, aber keine allgemeine Performance-Garantie. Große Create-Anlagen, automatisierte Mekanism-Prozesse, viele Bienen, AE2-Netzwerke und zahlreiche Pflanzen können andere Engpässe verursachen. Auch TPS allein beschreibt nicht die Client-Framerate.

Behebung: Auf dem Ziel-Laptop mit 5–6 GB Minecraft-RAM eine reproduzierbare Testbasis schaffen. Framerate, Frametime-Spitzen, RAM-Belegung, Garbage Collection und Server-TPS bei typischen Anlagen messen. Erst dann über zusätzliche Optimierung entscheiden.



8 · Mittel
KubeJS-Änderungen könnten sich zwischen Versionen unbemerkt verschieben

Betroffen: sieben.js, balance.js, luecken.js, gruppen.js, hinweise.js

Status: Allgemeines Wartungsrisiko.

Rezeptänderungen, Item-Gruppen, Tooltips und Sonderrezepte berühren verschiedene Teile des Spielerlebnisses. Ein Rezept kann korrekt geladen werden, während ein Tooltip oder eine JEI-Infoseite weiterhin einen inzwischen ungültigen Weg beschreibt.

Behebung: Rezeptdaten und Hilfetexte aus derselben zentralen Definition speisen, wo das praktikabel ist. Bei jedem Build zusätzlich auf veraltete Item-IDs, fehlende Rezeptreferenzen und widersprüchliche Hinweise prüfen.



9 · Mittel
Automatische Aktualisierung kann Versionsstände auseinanderlaufen lassen

Betroffen: packwiz, Prism Launcher, Server- und Client-Packdateien

Status: Bedingtes Betriebsrisiko.

Der Auto-Update-Ablauf ist bequem. Wenn Client und Server jedoch unterschiedliche Modpack-Stände verwenden oder eine Aktualisierung inkompatible Änderungen einführt, können Multiplayer-Probleme entstehen. Das ist keine Behauptung über einen konkreten packwiz-Fehler, sondern ein Risiko des Veröffentlichungsprozesses.

Behebung: Jede veröffentlichte Version eindeutig markieren, Manifest und Konfigurationen archivieren und einen bekannten funktionierenden Stand behalten. Vor Änderungen an Rezepten, Mods oder Weltdaten einen kontrollierten Update-Test mit Client und Server durchführen.



10 · Mittel
Story und Questtext könnten im Spielkontext untergehen

Betroffen: texte_*.py, quests.py, hinweise.js

Status: Designrisiko, kein Textfehler nachgewiesen.

Siebzehn Notizen sind nicht automatisch siebzehn erinnerungswürdige Momente. Wenn sie nur zwischen Rezeptanforderungen stehen, können Spieler sie überspringen oder als Pflichttext wahrnehmen.

Behebung: Jede Notiz braucht einen eigenen Zweck: eine neue Erkenntnis, einen Rückblick, einen Konflikt oder einen Ausblick. Questtexte sollten kurz genug sein, dass sie beim Spielen gelesen werden, und längere Lore sollte optional bleiben.



3. Spielerlebnis: Wo das Pack noch kein geschlossenes Spiel ist
Die entscheidende Frage ist nicht, ob jede Mod etwas zu tun hat. Sie ist, ob sich jede neue Mechanik wie eine Antwort auf ein vorheriges Problem anfühlt.









1. Frühspiel: Der erste echte Erfolg muss schnell kommen
Hohe Priorität
Sieben, Hammer und Create-Sifter bilden einen nachvollziehbaren Einstieg. Die Gefahr liegt darin, dass neue Spieler zu lange nur Materialien umwandeln, ohne einen sichtbaren Fortschritt zu erleben. Der erste automatische Produktionskreislauf sollte früh erreichbar sein und sich wie eine echte Errungenschaft anfühlen.

Mein Ansatz: Eine kleine, handgeführte Anfangsquest, danach möglichst schnell eine einfache Automatisierung. Erkläre den Unterschied zwischen Sieben und Sifter, aber nicht jede spätere Maschine im Voraus.












2. Übergänge: Aus Rezepten müssen Produktionsprobleme werden

Das größte Progressionsrisiko.

Tertium, Imperium, Supremium und Insanium sind eine interessante Möglichkeit, Systeme zu verbinden. Aber vier gesperrte Herstellungsrezepte ergeben noch keine vier spannenden Spielphasen.

Jede Stufe sollte ein neues Problem lösen: Durchsatz, Energieversorgung, Logistik oder Automatisierung. So ist der Spieler nicht bloß gezwungen, eine Maschine zu bauen, sondern versteht, warum sie jetzt sinnvoll ist.












3. Story: Die Weltgeschichte muss mit dem Spielen zusammenhängen

17 Notizen sind ausreichend – wenn sie etwas verändern.

„Das Herz der Leere“ besitzt einen brauchbaren thematischen Kern: Maschinen und Magie haben gemeinsam eine Katastrophe verursacht. Die Geschichte sollte diesen Gedanken nicht nur erzählen, sondern durch die Progression erlebbar machen.

Wenn eine Notiz die Erbauer für ihre Abhängigkeit von einer Energiequelle kritisiert, sollte die nächste Spielphase beispielsweise genau diese Abhängigkeit untersuchen. Das Finale sollte eine Antwort auf den Konflikt liefern, nicht nur die letzte Maschine freischalten.












4. Belohnungen: Weniger Loot, mehr neue Möglichkeiten

Eine Belohnung sollte einen Engpass erleichtern, eine neue Idee ermöglichen oder ein Bauprojekt unterstützen. Zufällige Mengen beliebiger Ressourcen können zwar angenehm sein, werden aber schnell bedeutungslos, sobald die Produktion automatisiert läuft.

Empfehlung: Werkzeuge, gezielte Baumaterialien, kleine Mengen eines gerade relevanten Rohstoffs und optionale kosmetische Belohnungen bevorzugen. Kritische Progressionsmaterialien sollten nicht in Mengen verschenkt werden, die eine ganze Produktionsstufe überspringen.












5. Technik und Magie: Gleichwertigkeit braucht echte Anwendungsfälle

Ars Nouveau und Mystical Agriculture auf der einen Seite, Create, Mekanism und AE2 auf der anderen, ergeben noch keine gleichwertigen Spielstile.

Wenn Magie hauptsächlich Kampf, Dekoration und einige Komfortfunktionen liefert, während Technik alle Ressourcen produziert, ist Technik objektiv wichtiger. Magie sollte deshalb mindestens einen eigenen, dauerhaften Nutzen bieten – etwa bei Erkundung, Mobilität, Ressourcenverarbeitung oder Baukomfort.

Beide Seiten müssen nicht identisch stark sein. Sie sollten aber jeweils Probleme lösen, für die es sich lohnt, sie zu lernen.












6. Bauen: Freiraum allein erzeugt noch keinen Bauanreiz

Macaw's, Handcrafted und FramedBlocks bieten eine gute Grundlage für individuelle Basen. Wenn das Questbuch jedoch ausschließlich Maschinen, Items und Mengen zählt, wird Bauen zum optionalen Zeitvertreib ohne spielerische Anerkennung.

Ich würde keine Pflicht einführen, eine bestimmte Anzahl Blöcke zu platzieren. Stattdessen sollten Bauquests optionale Themen, erkennbare Gestaltungsideen und Belohnungen anbieten, die Bauprojekte unterstützen. Der Spieler entscheidet, ob er daraus eine kleine Werkstatt oder eine ganze Himmelsstadt macht.












7. Koop: Gemeinsamer Fortschritt braucht eine gemeinsame Sprache

FTB Teams und Quests bieten die nötige Grundlage, aber das Spielerlebnis hängt auch davon ab, wie Aufgabenfortschritt und Belohnungen für mehrere Spieler funktionieren.

Ein Spieler sollte Maschinen bauen können, während ein anderer Magie erforscht, ohne dass der zweite dauerhaft auf Questfreischaltungen warten muss. Testet gemeinsam insbesondere geteilte Fortschritte, einmalige Belohnungen und den Umgang mit Aufgaben, die nur ein Teammitglied erledigt hat.












8. Endgame: Ein Ziel ist noch kein Grund, weiterzuspielen

Antimaterie, „Die ewige Fabrik“ und der Drache bieten einen nachvollziehbaren Endpunkt. Es fehlt aber noch ein erkennbarer Grund, weshalb das Ende emotional oder spielerisch besonders ist.

Die finale Aufgabe sollte die Geschichte der Erbauer aufgreifen und die Systeme verbinden, die der Spieler selbst aufgebaut hat. Danach sollte die Welt weiter nutzbar bleiben – ohne einen künstlichen zweiten Grind als vermeintlichen Nachfolger des Endes.



4. Wie ich weitermachen würde: Versionen 0.11.0 bis 0.13.0
Ich würde die nächsten drei Versionen bewusst unterschiedlich ausrichten: erst Zuverlässigkeit, dann Spielgefühl, anschließend Identität und Endgame. Neue große Mods oder Dimensionen sind dafür nicht nötig.
Version 0.11.0 – „Der vollständige Durchlauf“
Priorität: höchste
Ziel: Ein unbekannter Spieler kann vom Start bis zum Endgame kommen, ohne dass der Ersteller eingreifen muss.
1. Automatisierte Generatorprüfungen erweitern

In questlib.py, ftbformat.py und sperren.py eindeutige IDs, gültige Referenzen, Abhängigkeiten, Belohnungen und Progressionsstufen prüfen. Die Prüfung soll den Build mit einer verständlichen Fehlermeldung abbrechen, wenn ein harter Fehler gefunden wird.


2. Eine durchgängige Rezept- und Progressionsmatrix erstellen

In balance.js und sieben.js alle kritischen Rezepte systematisch erfassen. Dazu gehören nicht nur die vorgesehenen Herstellungswege, sondern auch bekannte alternative Quellen, Nebenprodukte und mögliche Umgehungen. Kritische Items werden anschließend mit echten Spieltests überprüft.


3. Einen vollständigen Testlauf dokumentieren

Mit einem frischen Clientprofil und einer frischen Welt vom ersten Sieb bis zum Finale spielen. Für jede Hauptphase notieren: Voraussetzungen, benötigte Ressourcen, Zeitaufwand, unklare Schritte, Sackgassen und tatsächlich benötigte Maschinen.


4. Sechs Startinseln vergleichen

inseln.py und die Inseldefinitionen gegen dieselbe Checkliste testen. Jede Insel muss den Einstieg erlauben, alle vorgesehenen Startziele unterstützen und eine verständliche Ausgangssituation vermitteln.


5. Leistung am Zielgerät messen

Ein reproduzierbares Testprofil mit einer kleinen, mittleren und größeren Anlage einrichten. Die Ergebnisse für Frametime, RAM und TPS festhalten. Optimieren, wo tatsächlich ein Engpass gemessen wird, statt vorsorglich weitere Mods hinzuzufügen.



Abnahmekriterium: Ein frischer Spieler kann die Hauptprogression ohne Entwicklerhilfe abschließen. Alle kritischen Rezeptwege sind getestet, und es gibt keine bekannten blockierenden Fehler.
Version 0.12.0 – „Ein Spiel statt einer Checkliste“
Ziel: Die Hauptprogression bekommt Rhythmus, verständliche Übergänge und echte Wahlmöglichkeiten.
1. Jedes Hauptkapitel mit einem klaren Spielziel beginnen

quests.py und texte_*.py so gestalten, dass jedes Kapitel zuerst das Problem erklärt und anschließend eine passende Lösung anbietet. Beispielsweise: Ressourcenknappheit lösen, Strom stabilisieren oder automatisierte Herstellung ermöglichen.


2. Die beiden Entscheidungen mechanisch unterscheiden

„Maschine oder Magie“ und „Erz ohne Sieb“ müssen unterschiedliche Wege eröffnen. Eine Route könnte effizienter sein, eine andere flexibler oder baulich interessanter. Beide bleiben bis zum Endgame konkurrenzfähig.


3. Belohnungen nach Nutzen überarbeiten

belohnungen.py auf redundante Items, überflüssige Rohstoffpakete und Belohnungen untersuchen, die neue Produktionsstufen vorwegnehmen. Lieber sinnvolle Werkzeuge und kleine, gezielte Engpasshilfen vergeben als große Mengen beliebiger Materialien.


4. Die 17 Notizen dramaturgisch verteilen

texte_*.py und quests.py so überarbeiten, dass jede Notiz eine neue Erkenntnis liefert. Die Geschichte soll nicht alle paar Quests unterbrechen, sondern die Neugier auf die nächste Entwicklungsstufe erhöhen.


5. Solo und Koop parallel testen

Zwei Personen spielen verschiedene Rollen, beispielsweise Technik und Magie. Dabei werden Teamfortschritt, Questbelohnungen und gegenseitige Abhängigkeiten getestet. Aufgaben, die nur gemeinsam oder nur allein sinnvoll sind, werden bewusst gekennzeichnet.



Abnahmekriterium: Ein Testspieler kann erklären, warum die nächste Stufe existiert, welche Alternativen er hat und was seine bisherigen Entscheidungen bewirkt haben.
Version 0.13.0 – „Das Herz der Leere“
Ziel: Das Pack erhält einen erinnerungswürdigen Höhepunkt und einen sinnvollen Abschluss.
1. Die ewige Fabrik als selbst gestaltetes Meisterwerk inszenieren

Mit Create, Mekanism, AE2 und den vorhandenen Baublöcken entsteht eine optionale oder erzählerisch eingebundene Endgame-Anlage. Nicht eine vorgegebene Maschine zum Nachbauen, sondern ein System, dessen Layout und Aufbau der Spieler selbst entwirft.


2. Die Entscheidungen im Finale wieder aufgreifen

Die zuvor gewählten Wege sollen im Finale unterschiedliche Aufgaben, Hilfsmittel oder Dialoge ermöglichen. Keine Route darf das eigentliche Finale dauerhaft ausschließen.


3. Magie und Technik für eine letzte gemeinsame Aufgabe verbinden

Die Geschichte der Erbauer sollte sich in einer Aufgabe spiegeln, die beide Systeme sinnvoll einsetzt. Mit bestehenden Rezepten, Questbedingungen und KubeJS-Anpassungen lässt sich das umsetzen, ohne eine neue Dimension einzuführen.


4. Optionale Bau- und Erkundungsquests ergänzen

Eine eigene Insel, ein Archiv, ein Labor oder ein Garten können zusätzliche Belohnungen bieten. Die Aufgaben dürfen den Fortschritt nicht blockieren und müssen keine festen Bauvorgaben erzwingen.


5. Release-Kandidaten auf Regressionen prüfen

Generator, Rezepte, Clientstart, Koop, Sicherungen und Updateprozess erneut testen. Die Version erst veröffentlichen, wenn die kritischen Pfade reproduzierbar funktionieren und die Story vom Anfang bis zum Ende nachvollziehbar ist.



Abnahmekriterium: Das Finale löst den zentralen Konflikt der Geschichte, die Entscheidungen sind spürbar und Spieler können nach dem Abschluss weiterbauen und automatisieren.
5. Drei kreative Ideen, die „Sky and Stone“ einzigartig machen könnten
Die folgenden Ideen sind bewusst so konzipiert, dass sie sich mit den vorhandenen Mods, KubeJS 7, FTB Quests und deinem Python-Generator umsetzen lassen.









Idee 1: Das Gedächtnis der Inseln
Weltgeschichte als spielbarer Forschungsprozess

Die siebzehn Notizen des Wächters sind Fragmente eines größeren Berichts. Jede Hauptphase enthüllt nicht nur einen Text, sondern auch einen konkreten Hinweis auf die Vergangenheit: eine fehlerhafte Maschine, eine misslungene Energieumwandlung oder eine Entscheidung, die zum Zerfall der Welt führte.

Über Questbelohnungen und vorhandene Baumaterialien erhalten Spieler nach und nach die Möglichkeit, ein eigenes Archiv zu bauen. Der Spieler entscheidet, ob es eine Bibliothek, ein Labor oder eine magische Gedenkstätte wird.

Warum das funktioniert: Die Story wird Teil der Basis. Das Archiv wächst mit dem Fortschritt und gibt dem Spieler einen Ort, an dem die Reise sichtbar bleibt.

Umsetzung: Storyquests in quests.py, Texte in texte_*.py, gezielte Baubelohnungen in belohnungen.py. Keine neue Mod erforderlich.












Idee 2: Die zwei Vermächtnisse
Technik und Magie als unterschiedliche Antworten auf dasselbe Problem

Die Erbauer haben nicht nur eine Technologie hinterlassen, sondern zwei konkurrierende Philosophien. Die technische Schule versucht, die Welt durch präzise Automatisierung zu stabilisieren. Die magische Schule setzt auf Anpassungsfähigkeit und einen anderen Umgang mit Energie.

In der Questreihe „Maschine oder Magie“ entscheidet sich der Spieler für einen Schwerpunkt. Der gewählte Weg schaltet einen kleinen Satz exklusiver Komfortbelohnungen und eine eigene Variante einer späteren Aufgabe frei. Die andere Schule bleibt spielbar und kann weiterhin genutzt werden.

Warum das funktioniert: Die Wahl verändert die Identität der Basis, ohne eine ganze Modlinie zu sperren. Ein Create- und Mekanism-Spieler und ein Spieler mit Schwerpunkt Ars Nouveau können sich im Koop sinnvoll ergänzen.

Umsetzung: Alternative Questzweige, eigene Belohnungstabellen und gezielte Rezeptvarianten. Wichtig: Die Exklusivität betrifft Komfort und Spielstil, nicht unverzichtbare Endgame-Ressourcen.












Idee 3: Die Insel, die du hinterlässt
Bauen als freiwilliges Vermächtnis

Nach wichtigen Meilensteinen bietet das Questbuch optionale Bauaufgaben an: eine funktionierende Werkstatt, einen Garten für die Magie, eine Produktionsinsel oder einen Ort des Gedenkens. Die Spieler erhalten Inspiration, eine thematisch passende Geschichte und eine kleine Belohnung für den Baufortschritt.

Es gibt keine Bewertung nach Blockanzahl und keine vorgeschriebene Architektur. Das Ziel ist, dass der Spieler seine eigene Interpretation der Geschichte in der Welt sichtbar macht. Im Koop können Mitspieler gemeinsam an einem solchen Vermächtnis arbeiten.

Warum das funktioniert: Die Welt ist nicht nur eine Maschine zur Ressourcenerzeugung. Sie wird zum Ergebnis der Entscheidungen des Spielers. Das passt besonders gut zu einem Skyblock, in dem jede Insel bewusst gestaltet werden muss.

Umsetzung: Optionale FTB-Quests-Kapitel, kreative Baumaterialien als Belohnungen und Storytexte, die verschiedene Bauideen anregen. Wenn echte Bauobjekte nicht zuverlässig automatisch geprüft werden können, bleiben die Aufgaben bewusst selbstbestimmt statt künstlich automatisiert.



Mein abschließendes Urteil
Ich würde „Sky and Stone“ nicht durch weitere Mods größer machen, sondern durch Tests, klare Entscheidungen und eine stärkere Verbindung zwischen den vorhandenen Systemen besser.

Die Architektur mit Python-Generator, zentralisierten Questdefinitionen, KubeJS-Rezeptänderungen und automatisierten Prüfungen ist eine solide Grundlage für ein langfristig wartbares Pack. Der nächste große Qualitätssprung wird aber nicht durch weitere 50 Quests entstehen, sondern durch einen Spieler, der das Pack zum ersten Mal startet, die Geschichte versteht, eine eigene Basis entwickelt und ohne Hilfe erkennt, warum die nächste Stufe sinnvoll ist.

Wenn ich nur eine Sache für 0.11.0 auswählen dürfte: einen vollständig dokumentierten, frischen Durchlauf von der Startinsel bis zum Finale – mit echten Clienttests, klar protokollierten Sackgassen und anschließenden Korrekturen. Erst danach würde ich größere Änderungen an Story, Belohnungen und Endgame vornehmen.

Und für eine tatsächliche Codeprüfung brauche ich als Nächstes die Projektdateien: insbesondere quests.py, questlib.py, ftbformat.py, sperren.py, belohnungen.py, sieben.js, balance.js sowie die relevanten Configs und generierten Questdaten. Damit ließen sich die hier genannten Risiken in konkrete, überprüfbare Befunde mit Datei, Funktion, betroffener Stelle und Lösung überführen.
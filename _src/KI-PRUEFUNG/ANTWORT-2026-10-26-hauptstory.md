<!-- FreeLLMAPI, Modell fusion, 296 s -->
### Leitmotiv: Die Reparatur der Weltmaschine

Die Welt ist nicht einfach nur leer, sondern ein kollabiertes mechanisches Uhrwerk. Das „Herz der Leere“ unter der Insel ist der Kern einer gigantischen, interdimensionalen Maschine, die durch eine Überladung zerrissen wurde. Der Spieler ist ein „Flicker“, der die Bruchstücke der Maschine repariert, um die Welt wieder in Gang zu bringen. Jede Mod ist ein Werkzeug, um ein Teil der Maschine zu reparieren: Create baut das physikalische Getriebe zusammen, Mekanism liefert den zerstörten Reaktor und AE2 verbindet die neuronale Schnittstelle. Am Ende wird das Herz nicht getötet, sondern reaktiviert oder endgültig abgeschaltet.

### Meilensteine: Von Schrott zu System

1. **Der erste Funke**
   - **Was der Spieler tut:** Er filtert Schutt aus dem Nichts und baut eine primitive Verbrennungs-Crucible, um mit Blättern die ersten Wassertropfen zu kochen.
   - **Mod-Zusammenspiel:** Ex Deorum (Sieben/Hämmern) + Vanilla (Ofen) + KubeJS (Das erste manuell gekochte „Unstable Water“ schaltet die Quest frei).
   - **Story-Item (KubeJS):** `skyandstone:schrott_filter` (Muss im Inventar sein, um den Fortschritt zu triggern).

2. **Das erste Zahnrad der Welt**
   - **Was der Spieler tut:** Er automatisiert das Sieben und Erzzerkleinern erstmals über physische Wasserkraft statt durch rohe Handarbeit.
   - **Mod-Zusammenspiel:** Create (Wasserrad, Mühlstein) + Ex Deorum (Sieb).
   - **Maschine:** `create:millstone` (Erzeugt per KubeJS-Rezept spezifische „Schrott-Erze“ statt Standard-Materialien).

3. **Der Puls der Tiefe**
   - **Was der Spieler tut:** Er errichtet eine Create-Press- und Mix-Anlage, um die ersten legierten Bauteile zu gießen, die den Grunddruck der Leere aushalten.
   - **Mod-Zusammenspiel:** Create (Mechanical Press, Basin, Blaze Burner) + Mystical Agriculture (Inferium als thermischer Katalysator).
   - **Maschine:** `create:basin` (Stellt das KubeJS-Item `skyandstone:druck_legierung` her).

4. **Der alchemistische Reaktor**
   - **Was der Spieler tut:** Er verbindet Getriebe-Energie mit magischen Essenzen, um organische Ressourcen (Erze/Metalle) aus künstlich erschaffener Erde zu züchten.
   - **Mod-Zusammenspiel:** Mystical Agriculture (Infiltration) + Create (Konstante Rotation zur Beschleunigung des Altars via KubeJS-Event).
   - **Maschine:** `mysticalagriculture:infusion_altar` (Muss von Create-Wellen angetrieben werden, um zu funktionieren – per KubeJS erzwungen).

5. **Der Funke aus der Drehung**
   - **Was der Spieler tut:** Er wandelt mechanische Rotationsenergie in die ersten elektrischen Impulse um, um die antiken Maschinen von Mekanism zu starten.
   - **Mod-Zusammenspiel:** Create Addition (Alternator) + Mekanism (Metallurgic Infuser).
   - **Maschine:** `createaddition:alternator` (Erzeugt Forge Energy, die zwingend in den Infuser geleitet werden muss).

6. **Die doppelte Realität**
   - **Was der Spieler tut:** Er baut eine automatisierte Erz-Verdopplung auf, die mechanische Sortierung mit chemischen Bädern von Mekanism koppelt.
   - **Mod-Zusammenspiel:** Mekanism (Enrichment Chamber, Metallurgic Infuser) + Pipez (Effizienter Energie- und Item-Transport).
   - **Maschine:** `mekanism:enrichment_chamber` (Verarbeitet KubeJS-„Roherze“ zu reinen Pulvern).

7. **Das neuronale Netz**
   - **Was der Spieler tut:** Er presst antike Prozessoren und verbindet sie mit dem Mekanism-Netzwerk, um den ersten zentralen Datenspeicher zu errichten.
   - **Mod-Zusammenspiel:** AE2 (Inscriber, Charger) + Mekanism (Energiespeicherung).
   - **Maschine:** `ae2:inscriber` (Erfordert massig FE von Mekanism, um die Logik-Chips zu prägen).

8. **Der Riss im Untergrund**
   - **Was der Spieler tut:** Er nutzt das AE2-Netzwerk und Autocrafting, um portalstabilisierende Komponenten zu berechnen und das leere Nether zu betreten, um Lohen zu jagen.
   - **Mod-Zusammenspiel:** AE2 (Pattern Provider, Assembler) + Vanilla/Nether (Festung).
   - **Maschine:** `ae2:molecular_assembler` (Stellt das KubeJS-Item `skyandstone:portal_stabilisator` her).

9. **Der Herzschlag der Fabrik**
   - **Was der Spieler tut:** Er kurbelt einen vollautomatischen Fission-Reactor an, dessen Kühlung und Brennstoffversorgung komplett über ein AE2-Subnetz gesteuert wird.
   - **Mod-Zusammenspiel:** Mekanism Generators (Fission Reactor) + AE2 (Export/Import von Abfall und Brennstoff).
   - **Maschine:** `mekanismgenerators:fission_reactor_casing` (Das Multiblock-Setup muss per KubeJS-Tick-Event überwacht werden; bei Fehler droht eine Void-Explosion).

10. **Die Rekonstruktion**
    - **Was der Spieler tut:** Er führt Magie (Ars Nouveau), Höchsttechnologie (Antimaterie/Laser) und das Drachenei zusammen, um das „Herz der Leere“ endgültig zu reparieren, statt es zu töten.
    - **Mod-Zusammenspiel:** Alle Mods (Ende, Mekanism, AE2, Ars Nouveau).
    - **Maschine:** Ein custom KubeJS-Block in der End-Hauptinsel, der alle End-Endprodukte (Antimaterie, Insanium, Erz-Laser) in einer finalen Sequenz verbraucht.

### Unvergessliche Momente

1. **Der Schock beim ersten Hämmern**
   - **Ereignis:** Wenn der Spieler zum ersten Mal einen Stein mit dem Ex-Deorum-Hammer zerschlägt, bebt die Insel (Camera Shake via Pehkui/KubeJS), und ein kurzer Text im Chat erscheint: *„Etwas in der Tiefe hat sich bewegt.“*

2. **Der Instabilitäts-Alarm**
   - **Entdeckung/Bau-Aufgabe:** Sobald der Mekanism-Fission-Reaktor das erste Mal läuft, droht bei falscher Kühlung keine normale Minecraft-Explosion, sondern die Insel verliert für 10 Sekunden die Schwerkraft (Pehkui: Spieler schweben, Blöcke fallen nach oben ins Nichts, wenn nicht stabilisiert).

3. **Der Wächter im leeren Nether**
   - **Bosskampf:** Das Nether ist leer – bis auf schwebende Festungsruinen. Nähert sich der Spieler dem Zentrum einer Festung, triggert ein KubeJS-Abstandssensor das Spawnen eines gebufften Wither-Skeletts („Der Archivar“), das beim Tod das zwingend nötige Folianten-Teil droppt.

4. **Das AE2-Erwachen**
   - **Entdeckung:** Das erste Einschalten des AE2-Controllers erfordert keinen normalen Strom, sondern das Opfern eines Mystical-Agriculture-Supremium-Items direkt im Charger. Ein Blitz schlägt ein (Vanilla-Befehl via KubeJS), und das Terminal „spricht“ zum Spieler (Chat-Nachricht mit Schreibmaschineneffekt).

5. **Die Stille des Endes**
   - **Entdeckung:** Auf der End-Hauptinsel gibt es keinen Enderdrachen im klassischen Sinne, sondern ein riesiges, schlafendes mechanisches Herz (Gebaut aus Mekanism-Casing und Create-Teilen per `/place template`). Der Spieler muss es mit Lasern und Magie „füttern“, statt es totzuprügeln.

### Fehler vermeiden

1. **Crafting-Wüsten**
   - **Problem:** Der Spieler muss 10.000 Eisen farmen, um weiterzukommen.
   - **Lösung:** Automatisierungs-Zwang statt Mengen-Zwang. Die Quests fordern niemals „Besitze 1000 Eisen“, sondern „Baue eine Maschine, die X pro Sekunde produziert“.

2. **Mod-Silos**
   - **Problem:** Man spielt erst Create durch, vergisst es komplett, baut dann Mekanism, vergisst das und baut AE2.
   - **Lösung:** Gekreuzte Rezepte (Cross-Mod-Recipes). Man kann Mekanism nicht bauen, ohne Create-Getriebe zu nutzen; man kann AE2 nicht betreiben, ohne Mystical-Agriculture-Essenzen als Leiter zu verwenden.

3. **Unsichtbare Wände und linearer Frust**
   - **Problem:** Wenn ein Spieler bei einem Schritt festhängt und das Questbuch keinen Hinweis gibt, wie die Mods greifen, bricht das Pack ab.
   - **Lösung:** In-Game-Logik und Quest-Verknüpfungen. Das Questbuch (FTB Quests) fungiert als das „Tagebuch des letzten Wächters“. Jede Quest erklärt nicht nur das *Was*, sondern über Lore-Text das *Warum*. Dazu helfen JEI-Beschreibungen (per KubeJS hinzugefügt), die bei jedem veränderten Rezept sofort zeigen, welche Maschine aus Mod A für Mod B gebraucht wird.

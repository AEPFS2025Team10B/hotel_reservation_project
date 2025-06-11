Das README.md-File sollte Folgendes enthalten:

Name und Vorname der Teammitglieder, die am Projekt mitgearbeitet haben
Teammitglieder B-10:  Germann David, 
                      Lutz Reto, 
                      Nathan Jeremy

Eine kurze Übersicht, wer zu welchen Projekt-Themen beigetragen hat 
(also z. B. zu welchen User-Stories, Files, Projektphasen, Rollen innerhalb des Teams etc.). 
Themen, die durch mehrere Teammitglieder bearbeitet wurden, dürft ihr bei allen jeweiligen 
Teammitgliedern aufführen.

Instruktion für uns, wie eure Applikation benutzt werden muss (Schritt-für-Schritt-Anleitung, 
insb. welche Notebooks oder Files ausgeführt werden müssen).
Annahmen und Interpretationen, falls welche vorhanden sind.


Alle User Stories und wer jeweils involviert war (Reihenfolge ist relevant):

Minimale User Stories
1. Als Gast möchte ich die verfügbaren Hotels durchsuchen
  1.1 Ich möchte alle Hotels in einer Stadt durchsuchen, um ein Hotel an meinem bevorzugten Standort auszuwählen.
  1.2 Ich möchte Hotels in einer Stadt nach der Anzahl der Sterne (z.B. mindestens 4 Sterne) durchsuchen.
  1.3 Ich möchte Hotels finden, die Zimmer haben, die meiner Gästezahl entsprechen (nur 1 Zimmer pro Buchung).
  1.4 Ich möchte Hotels sehen, die während meines Aufenthalts verfügbar sind (Check-in- und Check-out-Datum).
  1.5 Ich möchte Wünsche kombinieren können (z.B. Gästezahl, Sterne, Verfügbarkeit).
  1.6 Ich möchte die folgenden Informationen pro Hotel sehen: Name, Adresse, Anzahl der Sterne.
Involviert: Reto Lutz, Jeremy Nathan, David Germann

2. Als Gast möchte ich Details zu verschiedenen Zimmertypen sehen 
  2.1 Ich möchte für jedes Zimmer den Typ, die maximale Gästezahl, die Beschreibung, die Ausstattung, den Preis pro Nacht und den Gesamtpreis sehen.
  2.2 Ich möchte nur verfügbare Zimmer sehen, wenn ich meinen Aufenthalt spezifiziert habe.
Involviert: Reto Lutz

3. Als Admin möchte ich Hotelinformationen pflegen
  3.1 Neue Hotels zum System hinzufügen.
  3.2 Hotels aus dem System entfernen.
  3.3 Informationen bestimmter Hotels aktualisieren (z.B. Name, Anzahl Sterne).
Involviert: Reto Lutz, David Germann

4. Als Gast möchte ich ein Zimmer in einem Hotel buchen
	buchen
Involviert: Jeremy Nathan, David Germann

5. Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten
Involviert: Jeremy Nathan

6. Als Gast möchte ich meine Buchung stornieren
Involviert: Jeremy Nathan

7. Als Gast möchte ich dynamische Preise basierend auf Nachfrage sehen
Involviert: Jeremy Nathan

8. Als Admin möchte ich alle Buchungen aller Hotels sehen
Involviert: Reto Lutz

9. Als Admin möchte ich eine Liste der Zimmer mit Ausstattung sehen
Involviert: Reto Lutz

10. Als Admin möchte ich Stammdaten verwalten
Involviert: Reto Lutz


User Stories mit Datenbankschema-Änderung
3. Als Gast möchte ich nach meinem Aufenthalt Hotelbewertungen abgeben
Involviert: David Germann

4. Als Gast möchte ich Hotelbewertungen vor der Buchung lesen David
Involviert: David Germann


User Stories mit Datenvisualisierung
2. Als Admin möchte ich eine Aufschlüsselung der Gäste-Demografie sehen
Involviert: David Germann


  Erwähnenswert:
  add_example_data.py: Reto Lutz, David Germann
  app.py: Reto Lutz
  Datenbank: David Germann
  Grundstruktur: Reto Lutz
  Visual Paradigm: Jeremy Nathan

Man kann bei uns erkenne, dass wir zu Beginn der Arbeit, ein bisschen durcheinander gearbeitet haben.
Man sieht, dass wir später, die Aufgaben besser verteilt haben. Danach konnten wir effizienter arbeiten, 
weil wir uns nicht mehr überschnitten haben.

Kurze Instruktion wie die Applikation aufgebaut ist und wie sie verwendet werden muss:
Jede User Story ist in unterschiedliche .py Dateien unterteilt(ausser wenn Code wiederverwendet werden konnte).
Da es um die bedienung zu vereinfachen, haben wir die app.py Datei eingeführt.

Sie können also die Datei app.py ausführen und dann die gewünschte User Story auswählen und ausführen lassen.
wenn SIe eine User Story direkt ausführen wollen (über Current File), wird das nicht gehen.
Ansonsten müssen Sie keine Dateien ausführen, auch die Datenbank ist bereits fertig vorbereitet.
Für gewisse ausnahmen, spezialfälle, können Sie sich anzeigen lassen, was eingegeben werden muss, 
um diese hervorzurufen.
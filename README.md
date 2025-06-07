# FS25 Anwendungsentwicklung mit Python

## General
- **Hotel reservation system:** 
- **Germann David, Lutz Reto, Nathan Jeremy:** 
- **Date:** 
- **Business Artificial Intelligence  / Anwendungsentwiklung python:** 

## Abstract
A short summary of the report (around half a page).

## Table of Contents
- [Introduction](#introduction)
- [Theoretical Background](#theoretical-background)
- [Methods](#methods)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [Outlook](#outlook)
- [Appendix](#appendix)
- [References](#references)

## Introduction
- Background / context
- Problem statement
- Objectives
- Structure of the report

Im vergangenen Semester entwickelten wir das Datenbankschema für ein Hotelreservierungssystem. 
In diesem Semester bauten wir darauf auf und realisierten ein voll funktionsfähiges System zur 
Hotelreservierung, angelehnt an Plattformen wie Booking.com. Dabei stellten sich verschiedene 
Herausforderungen, insbesondere im Hinblick auf eine durchdachte Projektstruktur sowie eine 
effiziente technische Umsetzung.

Für eine saubere und wartbare Entwicklung kamen verschiedene Methoden der Softwareentwicklung 
zum Einsatz. Auch die Zusammenarbeit im Team war ein zentraler Faktor. Obwohl es zeitlich nicht 
immer einfach war, gelang es uns in der Regel, einmal pro Woche ein Scrum-Meeting durchzuführen, 
in dem wir Aufgaben verteilten und den Projektfortschritt besprachen.

Zu Beginn lag der Fokus stärker auf dem theoretischen Austausch, unter anderem durch wöchentliche 
Übungen. Mit dem Start der eigentlichen Implementierungsphase arbeiteten wir zunehmend strukturiert 
und konnten durch die regelmäßigen Meetings unsere Arbeit gut koordinieren.

Insgesamt ermöglichte uns dieser iterative und kooperative Ansatz, das Projekt effizient und 
zielgerichtet umzusetzen.

## Theoretical Background *(optional)*
- Theories, models, or frameworks relevant to the topic

## Methods
- Approach and methodology
- Tools, frameworks, and technologies used

Zu Beginn haben wir uns im Team darauf geeinigt, dass wir mit dem Projekt noch etwas warten, 
da uns das Wissen noch gefehlt hat. Wir haben jedoch die Übungen jede Woche gemacht und uns 
ausgetauscht. 
Als wir dann richtig begonnen haben, war es uns wichtig, dass wir flexibel arbeiten können.
Daher haben wir uns darauf geeinigt, dass alle, in jedem Bericht mithelfen, wir haben uns 
dann eine kurze Nachricht auf WhatsApp zukommen lassen. Jemand anderes hat dann meist dort 
weitergemacht, wo die Person vorhin aufgehört hat.
So konnten alle in jedem Bereich seine eigenen Erfahrungen sammeln und diese teilen.

Für die Umsetzung des Projekts haben wir viele verschiedene Programme verwendet. Für das Programm
selbst haben wir die Programmiersprache Python 3.12 verwendet. Als Entwicklungsumgebung haben wir 
uns auf PyCharm von Jetbrains geeinigt, wir hätten auch das jupiter Notebook Deepnote verwenden 
können. Die Arbeitsumgebung von PyCharm hat uns aber mehr zugesagt. Die Datenbank selber haben wir 
mithilfe von SQLite3 erstellt.
Begonnen haben wir aber mit VisualParadigm, um unsere Modelle korrekt zu visualisieren.

- Data sources or experimental setup

## Results
- Key findings
- Charts, tables, and important observations

Im Laufe des Projekts konnten wir ein funktionierendes Hotelreservierungssystem programmieren, das 
die wichtigsten Anforderungen erfüllt. Die Anwendung erfüllt unter anderem:
- Hotelsuche nach Stadt, Sternebewertung, Anzahl der Gäste und Verfügbarkeit
- Anzeige von Hoteldetails inklusive Adresse und Sterne
- Verwaltung von Hotels (Hinzufügen, Bearbeiten, Löschen)

Zentrale Erkenntnisse:
- Die Trennung von Datenzugriff (DataAccessLayer), Geschäftslogik (BusinessLogicLayer) und 
Benutzerschnittstelle(UI) hat sich als sehr nützlich herausgestellt, auch wenn es am Anfang kompliziert 
schien.
- Durch die modulare Struktur konnten wir parallel arbeiten und einzelne Komponenten unabhängig entwickeln 
und testen.
- Die Nutzung von Objektorientierung (z. B. für Hotel, Adresse, Buchung) hat den Umgang mit komplexen 
Datenmodellen vereinfacht.

Beobachtungen:
- Die Implementierung der dreischichtigen Architektur führte zu einer klaren Trennung der Verantwortlichkeiten
- Die Verwendung von SQLite3 erwies sich als effiziente Lösung für die Datenhaltung
- Die Konsolen-basierte Benutzeroberfläche ermöglichte eine schnelle Entwicklung und Testung
- Die modulare Struktur erleichterte das Debugging und die Wartung des Codes
- Die Implementierung von Fehlerbehandlung und Eingabevalidierung verbesserte die Benutzerfreundlichkeit
- Die Verwendung von Git für die Versionskontrolle unterstützte die parallele Entwicklung im Team

## Discussion
- Interpretation of the results
- Challenges encountered
- Were objectives achieved?

Interpretation der Ergebnisse
Die im Projekt implementierten Funktionen zeigen, dass ein einfaches, aber effektives 
Hotelreservierungssystem mit den verwendeten Technologien erfolgreich umgesetzt werden kann. Die Hauptziele,
wie die Suche nach Hotels, Verwaltung von Hotels und Adressdaten sowie einfache Buchungslogik, konnten in 
funktionierender Form realisiert werden. Besonders die modulare und objektorientierte Umsetzung hat sich 
positiv auf Lesbarkeit, Testbarkeit und Erweiterbarkeit ausgewirkt.

Herausforderungen
Während der Entwicklung traten verschiedene Herausforderungen auf:
- Adressverwaltung: Die Trennung von Hotel- und Adressdatenbanktabellen erforderte eine saubere Verknüpfung 
und erhöhte zunächst die Komplexität im Code.
- Fehlermeldungen und Debugging: Einige Fehler, z. B. bei der Übergabe von Argumenten an Konstruktoren, 
waren schwer zu identifizieren, insbesondere bei komplexeren Methodenketten.
- Teamkoordination: Durch unterschiedliche Verfügbarkeiten im Team war es manchmal schwierig, kontinuierlich 
im gleichen Tempo zu arbeiten. Die wöchentlichen Scrum-Meetings haben jedoch geholfen, Aufgaben zu klären 
und Fortschritte zu sichern.

Zielerreichung
Die meisten im Vorfeld gesetzten Ziele wurden erreicht:
- Die Suchfunktionen sind implementiert und getestet.
- Hotels können korrekt hinzugefügt, bearbeitet und gelöscht werden.
- Adressen werden eigenständig gespeichert und sind mit Hotels verknüpft.
- Die Benutzerführung erfolgt schrittweise und robust gegen fehlerhafte Eingaben.


## Conclusion
- Summary of key findings
- Reflection: what went well and what could be improved

Zusammenfassung zentraler Erkenntnisse
- Die Einführung einer modularen Schichtenarchitektur (UI, Business Logic, Data Access, Models) 
  hat zu sauberer Trennung von Verantwortlichkeiten geführt.
- Der Umgang mit SQLite und Python, wurde deutlich verbessert.
- Die Fehlerbehandlung, insbesondere bei Benutzereingaben, wurde systematisch ausgebaut.
- Git und GitHub wurden für Versionskontrolle, Teamarbeit und Problemanalyse effizient genutzt.

Was ging gut: 
- Git-Workflow wurde sinnvoll angewendet (Commit/Push/Pull, Branching, Konfliktlösung).
- Die Teamarbeit / die Kommunikation hat stets gut funktioniert.
- Wir konnten uns gut an die, im Unterricht, gelernten Konzepte halten. 
- Fehler wurden gemeinsam analysiert und lösungsorientiert behoben.
- Wir konnten neue Python-Kenntnisse anwenden (z. B. Properties, Klassenstruktur, 
  Try-Except-Blöcke).
- Trotz Herausforderungen mit der Datenbankanbindung wurde eine funktionierende 
  Lösung gefunden.

Was hätte man besser machen können
- Datenbankzugriff zentralisieren: Mehr Wiederverwendung von Methoden im base_data_access, 
  um Redundanzen zu vermeiden.
- Validierungen früher implementieren (z. B. für Eingaben, Konsistenzprüfungen in model-Klassen).
- Projektstruktur standardisieren, z. B. einheitlichere Benennung, klarere Trennung von 
  Test- und Produktivdaten.
- Frühzeitigeres Testing: Einzelne Funktionen hätten mit Unit-Tests früher auf Fehler überprüft 
  werden können.
- Wir haben uns zu Beginn etwas zu viel zeig gelassen. Wir wollten abwarten, bis wir alle konzepte 
  gelernt haben. Im Nachhinein, hätten wir früher beginnen sollen und einfach mit falschen Datenbanken

## Outlook *(optional)*
- Future work
- Further research suggestions

## Appendix *(optional)*
- Raw data
- Code snippets
- Extra charts or figures

## References
- Full list of all sources (books, articles, websites)

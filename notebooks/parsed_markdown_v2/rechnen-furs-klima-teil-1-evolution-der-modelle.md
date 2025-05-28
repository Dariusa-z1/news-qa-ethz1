# rechnen-furs-klima-teil-1-evolution-der-modelle.html

**Source:** de_news_events/2015/10/rechnen-furs-klima-teil-1-evolution-der-modelle.html

## Eine Frage der Auflösung

Prognosen des Wetters und – in einem grösseren Rahmen – des Klimas sind ein komplexer Prozess. Dabei fliessen aktuelle lokale und globale Beobachtungen in spezialisierte Computerprogramme ein, die dann die künftigen meteorologischen Bedingungen modellieren. Die Ergebnisse solcher Simulationen sind nicht nur wichtig für den täglichen Wetterbericht; sie geben auch Antworten auf Fragen des Klimawandels, etwa bezüglich Anpassung (wie sollen wir mit dem künftigen Klima umgehen?) und Schutzmassnahmen (wie können wir den Klimawandel eindämmen?).

Der britische Mathematiker und Meteorologe Lewis F. Richardson versuchte schon 1917, das Wetter «zu berechnen». Seine Rechenleistung bestand aus einem gedachten Mitarbeiterbestand von 64’000 Personen, die zusammen den ersten massiv-parallelen «Computer» darstellten. Richardson entwickelte einen umfangreichen Satz an Tabellen, die als einfacher verteilter Speicher dienten (wobei die einzelnen «Computer» die Zahlen handschriftlich eintragen sollten). Dazu befasste er sich mit Parallelisierung, Kommunikation und Synchronisation – alles zentrale Themen der modernen Klimasimulation.

## Bessere Rechenmodelle entwickeln

Bereits Richardson bildete die Atmosphäre mit einem dreidimensionalen Rechengitter ab, um eine vereinfachte Form der fluid-dynamischen Gleichungen auf einem rotierenden Planeten zu lösen – sprich: das Wetter zu berechnen – ganz ähnlich, wie wir das heute tun. Die ersten realistischen Simulationen kamen aber erst später, in den 50er-Jahren. Man arbeitete damals noch mit einer Auflösung von rund 800 km. Ein grosser Durchbruch gelang in den späten 70er-Jahren, als die Auflösung in globalen Modellen auf ungefähr 100 km verfeinert wurde. Das ermöglichte Wettervorhersagen von bis zu fünf Tagen, weil man zum ersten Mal Hoch- und Tiefdrucksysteme angemessen behandeln konnte. Davor waren nur Vorhersagen für einen Tag möglich.

Heute stehen wir nun vor der nächsten Herausforderung: Ab einer Auflösung von 1 km wird es möglich, konvektive Wolken (die Gewitter und Regenschauer verursachen) eindeutig abzubilden. Die Dynamik dieser feinskalierten atmosphärischen Systeme repräsentieren wir nunmehr mit physikalischen Gesetzen statt wie früher mit halb-empirischen Näherungsverfahren. Solche kilometergenaue Simulationen kommen bereits bei der operativen Wettervorhersage und vermehrt auch in der Klimaforschung zum Einsatz. Zahlreiche Studien zeigen, dass damit der Wasserzyklus und seine Extremerscheinungen angemessen dargestellt werden können. Zudem hofft man, dass die kilometergenaue Auflösung die Genauigkeit der Klimamodelle erhöhen wird. Jüngste Resultate einer Simulation über Europa [1] verdeutlichen die Vorteile hoher Auflösung und untermauern diese Zukunftsperspektiven (siehe Abbildung).

Diese Simulationen wurden mit dem Modell COSMO durchgeführt [2]. COSMO ist ein komplexes Computerprogramm, das hunderte Forscher in internationaler Zusammenarbeit über Jahrzehnte hinweg entwickelten. Das Programm läuft auf Hochleistungsrechnern und umfasst über 300 ’ 000 Zeilen Quellode. Es wird von vielen europäischen Wetterzentren – einschliesslich MeteoSchweiz – sowie von rund 200 Wissenschaftlern an verschiedenen Universitäten und Klimazentren eingesetzt, etwa dem Center for Climate Systems Modelling C2SM an der ETH Zürich.

## Bessere Rechenmodelle entwickeln

Hochleistungsrechner, auch Supercomputer genannt, reizen die Möglichkeiten dessen aus, was wir berechnen können. Dabei nutzen sie spezialisierte Mehrkernprozessoren und Grafikprozessoren (GPUs). Auf solchen massiv-parallelen Systemen höchste Leistung zu erreichen, ist eine zentrale Herausforderung in der Informatik. Durch Spezialisierung lässt sich zudem sehr viel Geld und Energie einsparen: Mit der Umstellung auf eine heterogene GPU-basierte Architektur im Piz-Kesch-System [3] konnte der Schweizerische Wetterdienst MeteoSchweiz beispielsweise die Energieeffizienz seiner operativen Vorhersagen um mehr als den Faktor drei verbessern. Diese Rechenmaschine wird nun für die tägliche Wetterprognose eingesetzt.

Dennoch: Heterogene Rechnersysteme effizient zu programmieren, stellt nach wie vor eine grosse Herausforderung dar – neue Erkenntnisse und Instrumente sind dafür nötig. Die GPU-Architektur folgt komplett anderen Designprinzipien als traditionelle Prozessoren und zwingt den Programmierer, die massive Parallelität in einer spezialisierten Sprache wie etwa CUDA auszudrücken. Das unterscheidet sich grundlegend von der Art und Weise, wie wir in den letzten 30 Jahren Code geschrieben haben. Meine Gruppe, das «Scalable Parallel Computing Laboratory» SPCL , will die erzielte Leistung weiter steigern und arbeitet an Methoden, um im Rahmen des Projekts «Platform for Advanced Scientific Computing» (PASC) [4] hochskalierende heterogene Supercomputer zu programmieren. PASC hat zum Ziel, das Hochleistungsrechnen (High-Performance Computing, HPC) in der Schweiz zu modernisieren. Die Resultate werden an der jährlichen, gleichnamigen Konferenz diskutiert. [5]

Torsten Hoefler hat diesen Blogbeitrag zusammen mit Christoph Schär (ETH Zürich) und Oliver Fuhrer (MeteoSchweiz) geschrieben. In ihrem nächsten Beitrag, « Rechnen fürs Klima (Teil 2) », erklären die Autoren, wie moderne Klimamodelle funktionieren.

## Weiterführende Informationen

[1] Leutwyler, D., O. Fuhrer, X. Lapillonne, D. Lüthi, C. Schär, 2015: Continental-Scale Climate Simulation at Kilometer-Resolution. ETH Zurich online resource. externe Seite Short description and animation , Climate Science Visuals: externe Seite Online video .

[2] externe Seite COSMO model

[3] externe Seite Piz Kesch

[4] externe Seite PASC

[5] externe Seite PASC Konferenz

Assistenzprofessor für Informatik, Scalable Parallel Computing Laboratory (SPCL), ETH Zürich


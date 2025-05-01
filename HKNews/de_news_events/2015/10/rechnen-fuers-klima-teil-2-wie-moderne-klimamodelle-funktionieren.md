# rechnen-fuers-klima-teil-2-wie-moderne-klimamodelle-funktionieren

**Source:** de_news_events/2015/10/rechnen-fuers-klima-teil-2-wie-moderne-klimamodelle-funktionieren.html

## Rechnen auf dreidimensionalen Gittern

Computersimulationen ermöglichen die tägliche Wettervorhersage und sind enorm wichtig, wenn es darum geht, den Herausforderungen des Klimawandels zu begegnen. Um das Verhalten des Klimasystems verstehen und vorhersagen zu können, konstruieren und nutzen Wissenschaftler komplexe Rechenmodelle, welche die relevanten chemischen und physikalischen Eigenschaften der Erdoberfläche (Land und Ozeane) in vereinfachter Form berücksichtigen. Aber wie funktionieren Klimamodelle genau, und welche Implikationen für die Informatik bringen sie mit sich?

Ähnlich den frühen Bemühungen von Richardson (siehe Teil 1 dieses Zweiteilers) spannen moderne Klimamodelle ein dreidimensionales Rechengitter über die Erde. Das erlaubt es, die physikalischen Gesetze zu berechnen, welche die Atmosphäre beeinflussen: In jeder Gitterzelle gibt es Werte für Windgeschwindigkeit, Temperatur, Druck, relative Luftfeuchtigkeit und Konzentrationen atmosphärischer Bestandteile (insbesondere Wasserdampf, aber auch andere Gase und Aerosole), die zusammen den aktuellen Zustand der Atmosphäre in diesem Bereich definieren. Je kleiner die Gitterzelle, desto höher ist die Auflösung des Modells. Unter Berücksichtigung der physikalischen Gesetze berechnet ein Computerprogramm dann Schritt für Schritt alle Werte für zukünftige atmosphärische Zustände. Um die Werte in einer bestimmten Zelle zu aktualisieren, benötigt die Software auch Informationen aus den benachbarten Zellen. Solche Programme werden oft als Stencilprogramme bezeichnet [1]. Da die Berechnungszeit und der Speicherbedarf linear mit der Anzahl Gitterzellen wachsen, ist die effiziente parallele Implementierungen von Stencilprogrammen ein wichtiges Forschungsthema des Scalable Parallel Computing Laboratory SPCL . Unter den folgenden Referenzen findet sich eine Einführung zu Klimamodellen sowie eine Tornado-Simulation: [2], [3].

## Millionen von Prozessoren auf Trab halten

Wenn wir einen Klima- und Wettercode auf einer hochskalierenden Maschine wie dem Piz Daint am Centro Svizzero di Calcolo Scientifico externe Seite CSCS implementieren, müssen wir das Stencilprogramm so parallelisieren, dass es auf Millionen von Verarbeitungselementen ausgeführt werden kann. In Zusammenarbeit mit MeteoSchweiz und dem CSCS hat ein Student am SPCL, Tobias Gysi, eine spezialisierte Programmiersprache entwickelt, die es Meteorologen erlaubt, Stencilprogramme sehr einfach anzupassen, und es Informatikern gleichzeitig ermöglicht, die Ausführung der Programme zu parallelisieren und zu optimieren. Diese domänenspezifische Sprache (DSL, «domain-specific language») trennt so die Arbeit des Meteorologen, der das eigentliche wissenschaftliche Rechenproblem definiert, von jener des Informatikers, der die auszuführende Berechnung optimiert. Solche domänenspezifische Sprachen effizient und automatisch für heterogene Hardware zu optimieren stellt eine wichtige Forschungsaufgabe für die Informatik dar.

Eine weiteres Forschungsgebiet ist das Speichern und Verwalten der gewaltigen Datenmengen, die schon während einer einzigen Simulation anfallen. Parameter wie Druck und Windgeschwindigkeit werden für jeden Gitterpunkt und jeden Zeitschritt gespeichert. Man geht davon aus, dass das Datenvolumen in naher Zukunft Exabytes erreichen könnte (10 18 Bytes, das entspricht 1’000’000 1-TB-Festplatten). Dafür sind neue leistungsstarke Techniken für die Datenerzeugung und -verwaltung sowie für Online-Analysen nötig. Diese Herausforderungen gehen MeteoSchweiz, das CSCS und die ETH Zürich in einer Kollaboration an, die der Schweizerische Nationalfonds im Rahmen des Programms Sinergia finanziert. [4]

## Den Klimawandel über den Alpen und Europa modellieren

Kürzlich wurde eine umfangreiche Simulation des europäischen Sommers fertiggestellt [5], [4]. Sie verwendet ein Rechennetz von 500 x 500 x 60 Gitterpunkten bei einer horizontalen Auflösung von 2,2 km und deckt einen Zeitraum von 30 Jahren ab. Um die damit verbundenen enormen Datenmengen effizient zu verwalten, wurde nur ein kleiner Teil der Ausgabe gespeichert. Dennoch umfasst das Archiv mehr als 120 TB. Die Simulation erfolgte mit einer konventionellen Version des COSMO-Modells und konsumierte über eineinhalb Jahre Rechenzeit auf dem Supercomputer Monte Rosa am CSCS.

Als nächstes wollen wir ähnliche Simulationen mit der GPU-fähigen Version von COSMO durchführen; diesmal aber soll die Modellierung den gesamten europäischen Kontinent mit einem zehnmal grösseren Rechengebiet abdecken (siehe Abbildung und Animation in Teil 1 ). Dabei soll auch eine neuere Hardware-Architektur zum Einsatz kommen (Cray XC30, Piz Daint) [3]. Piz Daint weist eine beachtliche Spitzenleistung von 6 x 10 15 Flop/s (Gleitkommaoperationen pro Sekunde, «floating point operations per second») auf und verfügt über insgesamt 5‘272 Rechenknoten. Da unsere aktuelle Implementierung der COSMO-GPU-Version nur 144 Knoten benötigt (das heisst drei Prozent), ist die geplante Ausdehnung des Rechengebietes ein sehr realistisches Ziel.

## Kooperation fördert Klimawissenschaften

Mit diesen Berechnungen möchten wir den Wasserzyklus einschliesslich extremer Starkniederschlagsereignisse besser verstehen und vorhersagen. Simulationen im alpinen Raum haben bereits interessante Ergebnisse zu Tage gebracht, die kaum glaubhaft wären, wenn sie auf semi-empirischen Annahmen basieren würden. Die Resultate deuten nämlich darauf hin, dass die durchschnittliche Sommerniederschlagsmenge bis Ende des Jahrhunderts um rund 30 Prozent sinken wird, während die Häufigkeit heftiger Gewitter und Regenschauer erheblich ansteigen wird. Anders gesagt geht man davon aus, dass Extremfälle an beiden Enden des Spektrums, also sowohl Dürren wie auch Sturzfluten, zunehmen werden. Erkenntnisse aus solchen Experimenten können für die Anpassung an den Klimawandel interessant sein: Denn kurzfristige Starkniederschlagsereignisse haben Konsequenzen für die Art und Weise, wie wir Wasservorräte verwalten und uns vor Hochwasser schützen sollten.

Für die Vorhersage des Wetters und des Klimas sind nicht nur leistungsfähige Computer nötig, es bedarf auch einer engen Zusammenarbeit zwischen den Klimawissenschaften und der Informatik. Heterogene Hardware-Architekturen sind unerlässlich für moderne Simulationen, sie erfordern aber einen grundlegend neuen Ansatz in der Softwareentwicklung. Die aktuelle Version des COSMO-Modells ist das weltweit einzige verfügbare regionale Wetter- und Klimamodell, das vollständig auf GPUs laufen kann. Dieser Fortschritt und die daraus entstandenen Perspektiven sind die Früchte einer engen interdisziplinäre Zusammenarbeit zwischen dem CSCS, MeteoSchweiz, dem C2SM und der Departemente Informatik und Umweltsystemwissenschaften der ETH Zürich.

## Weiterführende Informationen

Torsten Hoefler hat diesen Blogbeitrag zusammen mit Christoph Schär (ETH Zürich) und Oliver Fuhrer (MeteoSchweiz) geschrieben.

[1] externe Seite Stencil code

## Zum Autor

[2] An introduction to externe Seite climate models

[3] Tornado externe Seite simulation

[4] crCLIM : Convection-resolving climate modeling on future supercomputing platforms. A Sinergia project funded by the SNF.

[5] Ban N., J. Schmidli and C. Schär, 2015: Heavy precipitation in a changing climate: Does short-term summer precipitation increase faster? Geophys. Res. Lett. , 42 (4), 1165–1172 externe Seite doi .

[6] Fuhrer, O., C. Osuna, X. Lapillonne, T. Gysi, B. Cumming, M. Bianco, A. Arteaga and T. C. Schulthess, 2014. Towards a performance portable, architecture agnostic implementation strategy for weather and climate models. Supercomputing Frontiers and Innovations, 1 (1), 45-62

Assistenzprofessor für Informatik, Scalable Parallel Computing Laboratory (SPCL), ETH Zürich


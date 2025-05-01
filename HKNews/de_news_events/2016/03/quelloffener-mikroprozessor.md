# quelloffener-mikroprozessor

## Prozessor für tragbare Mikrosysteme

Quelltexte von Software und Baupläne von Hardware sind in der Regel gut gehütete Geschäftsgeheimnisse. Nicht so bei Open-Source-Produkten. Der Code von Open-Source-Software beispielsweise ist allen frei zugänglich. Bekanntestes Beispiel ist das Betriebssystem Linux. Interessierten Entwicklern ist es möglich, die Software nicht nur zu nutzen, sondern sie auch weiterzuentwickeln und ihren Bedürfnissen anzupassen.

Auch im Hardware-Bereich gibt es solche Open-Source-Produkte. Beispiele sind grundsätzlich quelloffene Einplatinencomputer wie Arduino oder Raspberry Pi, von denen Baupläne verfügbar sind. Allerdings basieren diese auf kommerziellen Chips, deren interne Architektur nicht Open-Source ist. Vor wenigen Tagen haben nun Wissenschaftler der ETH Zürich und der Universität Bologna unter der Leitung von ETH-Professor Luca Benini den Bauplan eines von ihnen entwickelten Mikroprozessorsystems veröffentlicht – und zwar so, dass die Freiheit anderer Entwickler, das System zu nutzen und verändern, maximal ist, wie Benini betont. «Es ist nun möglich, Open-Source-Hardware wirklich von Grund auf zu konstruieren.»

«Bei vielen bisherigen Beispielen von Open-Source-Hardware ist die Nutzung durch exklusive Vermarktungsrechte und Konkurrenzverbote eingeschränkt», sagt Benini. «Bei unserem System hingegen sehen die Lizenzbedingungen keine solche Einschränkungen vor.» Die Rechenbefehle, welche der Mikroprozessor ausführen kann, sind ebenfalls Open Source: Die Wissenschaftler machten den Prozessor kompatibel mit einem Open-Source-Befehlssatz – RISC-V –, der an der University of California in Berkeley entwickelt wurde.

## Gemeinsame Weiterentwicklung

Der neuentwickelte Prozessor heisst Pulpino und ist für batteriebetriebene Geräte mit äusserst geringem Energiebedarf vorgesehen – Pulp steht für «parallel ultra low power». Dies könnten Chips für kleine Geräte wie Smartwatches sein, für Sensoren zur Überwachung von Körperfunktionen (die mit einer Pulsuhr kommunizieren können) oder für neuartige Sensoren für das Internet der Dinge.

Benini gibt ein Beispiel aus der aktuellen Forschung in seinem Labor: «Wir entwickeln mit dem Pulpino-Prozessor eine mit Elektronik und einer Mikrokamera bestückte Smartwatch. Sie kann visuelle Informationen auswerten und daraus den Aufenthaltsort des Benutzers bestimmen. Die Idee ist, dass eine solche Smartwatch dereinst etwa Heimelektronik ansteuern könnte.» Dies alles auf kleinstem Raum auf einem Mikroprozessor unterzubringen mit einer winzigen Leistung von nur wenigen Milliwatt, sei eine Herausforderung, zumal die Rechenkapazität für die Bildauswertung ausreichend gross sein müsse.

Auch in anderen Forschungsprojekten, die Benini mit Schweizer und europäischen Forschungseinrichtungen unterhält, unter anderem mit der Universität Cambridge, kommt Plupino zum Einsatz. Davon, dass der Prozessor nun Open Source ist, erhofft sich der ETH-Professor viel: «Solche Forschungsprojekte kamen bisher vor allem aufgrund von persönlichen Kontakten zustande, und für jedes Projekt mussten die beteiligten Partner die jeweiligen Nutzungsverträge von neuem aushandeln. Nun ist Pulpino viel besser verfügbar. Wir hoffen, dass es in Zukunft mehr Zusammenarbeiten gibt und diese auch einfacher werden.»

## Interessant für die Industrie

So möchten die Wissenschaftler gemeinsam mit anderen Projektpartnern akademisch interessante Erweiterungen zu Pulpino entwickeln. Diese wären dann ebenfalls Open Source. Auf diese Weise würde die Zahl der Funktionskomponenten der Hardware stetig wachsen.

Doch Pulpino soll auch dem für die Schweiz und Europa so typischen KMU-Umfeld zugutekommen. «Die Produktion von Mikrochips ist in den letzten Jahren billig geworden, weil Halbleiterhersteller grosse Produktionskapazitäten aufgebaut haben, die sie auslasten müssen», erklärt Benini. Teurer ist die Entwicklung der Prozessoren: «Es wäre viel zu aufwendig, einen komplexen Chip von Grund auf neu zu entwickeln, insbesondere für KMU. Stattdessen kaufen Entwickler in der Regel einzelne Funktions-Komponenten ein, welche sie ins Chip-Design integrieren. Die Lizenzgebühren für diese Komponenten sind oft ein wesentlicher Teil der gesamten Entstehungskosten.»

Mit dem Open-Source-Chip, für den keine Lizenzgebühren anfallen, sinken die Entwicklungskosten deutlich, wovon die KMU profitieren, aber auch die ETH, wie Benini betont: «Es könnten so neue Forschungs- und Entwicklungspartnerschaften mit der Industrie entstehen, um gemeinsam auf der Basis von Pulpino neuartige Chip-Komponenten zu entwickeln.» Die Entwickler von Pulpino planen daher, ihren Mikroprozessor in diesem Jahr der Open-Source-Hardware-Gemeinschaft noch besser bekannt zu machen.


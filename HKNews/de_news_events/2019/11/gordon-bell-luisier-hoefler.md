# gordon-bell-luisier-hoefler

## ETH-Team erhielt Gordon Bell Preis

Chip-Hersteller verbauen Transistoren, die nur wenige Nanometer klein sind. Ihr Durchmesser beträgt nicht einmal ein Tausendstel eines menschlichen Haares, der bei feinem Haar etwa 20'000 Nanometer misst. Der Bedarf an immer leistungsfähigeren Hochleistungsrechnern treibt die Industrie an, noch kleinere und zugleich leistungsstärkere Bauteile zu entwickeln.

Neben physikalischen Gesetzmässigkeiten, die den Bau der winzigen Transistoren erschwert, weist das Problem der steigenden Selbsterhitzung die Hersteller jedoch zunehmend in ihre Schranken - unter anderem auch, weil der Kühlbedarf und infolgedessen der Energiebedarf enorm ansteigen. In einigen Rechenzentren mache die Kühlung der Rechner schon bis zu 40 Prozent des Strombedarfes aus, schreiben die Forschungsgruppen der ETH-Professoren Torsten Hoefler und Mathieu Luisier einer aktuellen Studie, mit der sie einen Verbesserungsansatz liefern wollen. Mit ihrer Studie wurden die Forscher gestern mit dem prestigeträchtigen ACM Gordon Bell Prize geehrt, dem wichtigsten Preis im Bereich des Hochleistungsrechnen, der alljährlich auf der Supercomputing-Tagung (SC) in den USA vergeben wird.

Um heutige Nano-Transistoren effizienter zu machen, simuliert die Forschungsgruppe von Luisier vom Institut für Integrierte Systeme (IIS) der ETH Zürich Transistoren mit Hilfe der Software «OMEN», einem sogenannten Quantentransportsimulator.

## Optimierte Simulation verbessert Transistoren

OMEN ermöglicht eine realitätsnahe atomare Auflösung des Transistors auf quantenmechanischer Ebene. Die Simulation macht sichtbar, wie der elektrische Strom durch den Nanotransistor fliesst und die Elektronen mit Kristallschwingungen wechselwirken. Die Forscher können darüber die Stellen, wo Hitze produziert wird, identifizieren. Die Simulation gibt somit wertvolle Hinweise auf Verbesserungsmöglichkeiten.

Mit herkömmlichen Programmiermethoden und Supercomputern war es bis anhin nur möglich, die Erhitzung von Transistoren aus rund 1000 Atomen zu simulieren, da die Datenkommunikation zwischen den Prozessoren und Speicheranforderungen eine realistische Simulation grösserer Objekte verunmöglichten.

Die meisten Computerprogramme verwenden einen Grossteil der Zeit damit, Daten zwischen Prozessoren, Hauptspeicher und externen Schnittstellen zu bewegen. In nur einem geringen Teil der Zeit rechnen sie. Auch in OMEN gab es laut den Wissenschaftlern einen ausgeprägten, die Leistung schmälernden Flaschenhals in der Kommunikation. «Die Software wird heute in der Halbleiterindustrie benutzt, hat aber ein grosses Verbesserungspotential bei den numerischen Algorithmen und der Parallelisierung», sagt Luisier.

## Datenzentrierte Programmierung

Bisher sei die Parallelisierung von OMEN nach der Physik des elektrothermischen Problems konzipiert worden, erklärt er. Nun schauten sich der Doktorand Alexandros Ziogas und der Postdoc Tal Ben-Nun unter Leitung von Torsten Hoefler, der das Scalable Parallel Computing Laboratory der ETH Zürich leitet, nicht die Physik, sondern die Abhängigkeiten zwischen den Daten an.

Sie reorganisierten die Rechenoperationen entsprechend dieser Abhängigkeiten, quasi ohne die Physik zu berücksichtigen. Bei der Optimierung des Codes hatten die Forscher Unterstützung von zwei der leistungsstärksten Supercomputern der Welt, von «Piz Daint» vom Nationalen Hochleistungsrechenzentrum der Schweiz (CSCS) und «Summit» vom Oak Ridge National Laboratory in den USA. Laut den Forschern führt der optimierte Code zu gleich präzisen Ergebnissen in der Simulation wie die ursprüngliche Software OMEN.

Mit dem neuen Code namens DaCe-OMEN sei es erstmals möglich, auf derselben Anzahl Prozessoren zehn Mal grössere Transistoren, bestehend aus 10'000 Atomen, realitätsnah zu simulieren – und das bis zu vierzehn Mal schneller als die ursprüngliche Methode für 1000 Atome brauchte. Insgesamt ist DaCe-OMEN um zwei Grössenordnungen effizienter als OMEN: Auf «Summit» konnte unter anderem ein realistischer Transistor bei einer kontinuierlichen Rechnerleistung (sustained performance) von 85,45 Petaflop pro Sekunde bis zu 140 Mal schneller berechnet werden. Dies auf 4'560 Rechnerknoten in doppelter Genauigkeit (double precision). Diese extreme Beschleunigung des Rechenvorgangs brachte den Forschern den externe Seite Gordon Bell Prize ein.

## Literaturhinweis

Die Optimierung erreichten die Wissenschaftler, indem sie Prinzipien der datenzentrischen parallelen Programmierung nutzten, die Hoeflers Forschungsgruppe entwickelte. Ziel ist, den Datentransport und somit die Kommunikation zwischen den Prozessoren so klein wie möglich zu halten. «Mit dieser Art von Programmierung können wir auf verschiedenen Ebenen eines Programms sehr genau feststellen, wo diese Kommunikation verbessert werden kann», sagt Ben-Nun. «Aber auch wie wir spezifische rechenintensive Abschnitte, sogenannte Computational Kernels, innerhalb der Berechnung eines einzelnen Zustands abstimmen können». Diese mehrstufige Sichtweise ermögliche es, eine Anwendung auf allen Ebenen zu optimieren, ohne diese jedes Mal neu schreiben zu müssen.

Die Datenbewegung wird dabei optimiert, ohne die ursprüngliche Berechnung zu verändern – und das für jede beliebige Computerarchitektur. «Wenn wir den Code für die Zielarchitektur optimieren, ändern wir diesen nur in der Ansicht des Performance-Ingenieurs, und nicht mehr in der des Programmierers, also des Forschers, der das wissenschaftliche Problem im Code formuliert», sagt Hoefler. Dadurch etabliere sich eine einfache Schnittstelle zwischen Informatikern und interdisziplinären Programmierern.

Die Anwendung von DaCe-OMEN zeigte, dass die grösste Hitze nahe am Kanalende eines Nanotransistor entsteht, wie sie sich von dort ausbreitet und auf das gesamte System wirkt. Die Wissenschaftler sind überzeugt, dass sie das neue Verfahren zur Simulation solcher elektronischen Komponenten vielseitig anwenden können, beispielsweise auch beim Bau von Lithiumbatterien, deren Überhitzung für unliebsame Überraschungen sorgen kann.

Dieser Text von Simone Ulmer erschien in Englisch auf der Website des externe Seite CSCS .

Ziogas AN, Ben-Nun T, Fernández GI, Schneider T, Luisier M & Hoefler T: A Data-Centric Approach to Extreme-Scale Ab initio Dissipative Quantum Transport Simulations, Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis (SC19), November 2019.


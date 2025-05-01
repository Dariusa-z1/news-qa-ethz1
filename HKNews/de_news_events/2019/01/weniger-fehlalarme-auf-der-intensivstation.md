# weniger-fehlalarme-auf-der-intensivstation

**Source:** de_news_events/2019/01/weniger-fehlalarme-auf-der-intensivstation.html

## Kombination von Daten

Piiiep, piiiep, piiiep. Dauernd schlägt auf der Intensivstation irgendein Messgerät Alarm. Sei es, weil das Blut eines Patienten zu wenig Sauerstoff enthält, bei der Patientin nebenan der Druck im Schädel gestiegen oder bei jemandem der Blutdruck abgesackt ist. Oder aber einfach nur deshalb, weil sich ein Patient im Bett bewegt hat.

Solche Fehlalarme sind häufig. Sie halten das medizinische Personal auf Trab, und es besteht die Gefahr, dass die echten Alarme in der Flut von Fehlalarmen untergehen. Pflegende und Ärzte haben daher ein Interesse, dass sich die Zahl von falschen Alarmen deutlich reduziert. Forscher der ETH Zürich haben nun in Zusammenarbeit mit Wissenschaftlern der Neurochirurgischen Intensivstation des Universitätsspitals Zürich eine Methode des maschinellen Lernens geschaffen, welche genau dieses Ziel verfolgt.

Im Rahmen einer Machbarkeitsstudie nutzten die Forschenden umfassende Datenaufzeichnungen dieser Intensivstation. Für ein Datenwissenschafts-Projekt ( externe Seite ICU Cockpit ) werden dort die Messungen der Vitalfunktionen in hoher zeitlicher Auflösung sowie die Alarme mit Zustimmung der Patienten systematisch gespeichert.

Wie es auch auf anderen Intensivstationen die Regel ist, funktionieren die verschiedenen Geräte zur Kreislaufüberwachung, künstlichen Beatmung und der Aufzeichnung eines Elektroenzephalogramms unabhängig voneinander. Ebenso schlagen sie unabhängig voneinander Alarm, nämlich dann, wenn der Messwert einen definierten Schwellenwert unter- oder überschreitet. Die Forschenden kombinierten und synchronisieren daher die Daten der Messgeräte, um mithilfe von maschinellem Lernen medizinisch nicht-relevante Alarme zu identifizieren.

«Damit der Computer lernen kann, müssen üblicherweise zuvor Menschen eine bestimme Zahl von Alarmen als relevant oder nicht-relevant beurteilen», erklärt Walter Karlen, Professor für mobile Gesundheitssysteme an der ETH Zürich. «Computersysteme können diese Informationen dann nutzen, um das Prinzip der Klassifizierung zu verstehen und schliesslich selbst Alarme beurteilen zu können.»

Die Klassifizierung von Alarmen auf einer Intensivstation durch einen Menschen ist allerdings Sisyphusarbeit, zumal sie für jeden Patienten individuell gemacht werden muss. Ausserdem hat das Personal auf einer Intensivstation kaum Zeit, neben der Betreuung von Patienten einen Computer zu unterrichten.

Wünschenswert für den Einsatz auf einer Intensivstation wäre daher ein System, das selbst dann lernfähig ist, wenn Pfleger oder Ärztinnen nur wenige Alarme klassifizieren. Genau dies kann die von Karlen und seinen Kollegen geschaffene Machine-Learning-Methode besonders gut.

Die Wissenschaftler testeten ihre Methode anhand eines kleinen Datensatzes aus der Zürcher Intensivstation: der Aufzeichnung von Vitalparametern und Alarmen von 14 Patienten während mehrerer Tage. Im Schnitt schlugen die Geräte knapp 700-mal pro Patient und Tag Alarm, also durchschnittlich alle zwei Minuten. Obschon in dem Datensatz nur 1'800 (13 Prozent) der insgesamt 14'000 Alarme manuell klassifiziert waren, konnte der Algorithmus auch die restlichen Alarme in echte, beziehungsweise falsche Alarme einteilen. Liessen die Wissenschaftler dem System eine Fehlerquote von fünf Prozent zu, sortierte das System 77 Prozent aller Fehlalarme aus.

Wie die Wissenschaftler ausserdem zeigen konnten, funktioniert die Methode sogar mit weit weniger manueller Hilfestellung: Schon 25 oder 50 manuelle Beurteilungen durch Experten reichen aus, um einen Grossteil der Fehlalarme auszusortieren. Insbesondere bei einer solch geringen manuellen Hilfestellung ist die neue Methode anderen existierenden Machine-Learning-Methoden überlegen, wie die Forscher ebenfalls zeigten.

Bei dieser Arbeit wurden klinische Daten retrospektiv analysiert. Die Forscher erwägen nun, die Leistungsfähigkeit ihres Algorithmus in einer vorausblickenden (prospektiven) klinischen Studie zu überprüfen.

## Literaturhinweis

Schwab P, Keller E, Muroi C, Mack DJ, Strässle C, Karlen W: externe Seite Not to Cry Wolf: Distantly Supervised Multitask Learning in Critical Care . Proceedings of the 35th International Conference on Machine Learning, Stockholm, 2018


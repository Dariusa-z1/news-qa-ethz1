# kuenstliche-intelligenz-versteht-den-klang-gesunder-maschinen.html

**Source:** de_news_events/2022/02/kuenstliche-intelligenz-versteht-den-klang-gesunder-maschinen.html

## Defekte frühzeitig erkennen

Ob Eisenbahnräder oder Generatoren in einem Kraftwerk, ob Pumpen oder Ventile – sie alle machen Geräusche. Für geübte Ohren haben diese Geräusche sogar eine Bedeutung: Bauteile, Maschinen, Anlagen oder Rollmaterial klingen nämlich anders, wenn sie einwandfrei funktionieren, als wenn sie einen Mangel oder Fehler haben.

Die Geräusche, die sie erzeugen, geben den Fachleuten somit nützliche Hinweise, ob sich eine Maschine sich in einem gutem – oder «gesunden» – Zustand befindet, oder ob sie schon bald eine Wartung benötigt oder dringend zu reparieren ist. Wer rechtzeitig erkennt, dass eine Maschine fehlerhaft tönt, kann einem kostspieligen Defekt zuvorkommen und eingreifen, bevor sie kaputtgeht. Folgerichtig gewinnen die Überwachung und Untersuchung von Geräuschen an Bedeutung für den Betrieb und die Instandhaltung technischer Infrastruktur – zumal das Aufnehmen von Tönen, Geräuschen und akustischen Signalen mit modernen Mikrophonen vergleichsweise kostengünstig ist.

Um die benötigte Information aus solchen Geräuschen herauszuziehen, haben sich bewährte Methoden der Signalverarbeitung und Datenanalyse etabliert. Zu ihnen zählt die sog. Wavelet-Transformation. Mathematisch lassen sich Töne, Klänge, Geräusche als Wellen darstellen. Bei der Wavelet-Transformation wird eine Funktion in eine Menge von Wavelets zerlegt. Das sind wellenartige Schwingungen, die zeitlich verortet sind. Die zugrundeliegende Idee dabei ist es, zu bestimmen, wie viel von einem Wavelet in einem Signal enthalten ist. Obwohl solche Verfahren recht erfolgreich sind, erfordern sie oft viel Erfahrung und eine manuelle Einstellung der Parameter.

## Defekte frühzeitig erkennen

Nun haben ETH-Forschende ein maschinelles Lernverfahren entwickelt, das die Wavelet-Transformation vollständig lernen kann. Der neue Ansatz eignet sich besonders für hochfrequente Signale wie Schall- und Vibrationssignale. Er macht es möglich, automatisch zu erkennen, ob eine Maschine «gesund» klingt oder nicht.

Der Ansatz, den die Postdoktoranden Gabriel Michau, Gaëtan Frusque, und Olga Fink, Professorin für Intelligente Instandhaltungssysteme, entwickelt und nun in der Zeitschrift PNAS veröffentlicht haben, verbindet Ansätze der Signalverarbeitung und des maschinellen Lernens auf eine neue Art und Weise. Mit dem neuen Ansatz kann ein intelligenter Algorithmus, also eine Rechenregel, die akustische Überwachung und Klanganalyse von Maschinen automatisch durchführen. Aufgrund seiner Ähnlichkeit zur bewährten Wavelet-Transformation lassen sich die Ergebnisse des vorgeschlagenen maschinellen Lernansatzes auch sehr gut interpretieren.

Das Ziel der Forschenden ist es, dass Fachpersonen, die in der Industrie Maschinen betreiben schon in naher Zukunft ein Tool nutzen können, das die Apparaturen automatisch überwacht und sie – ohne dass spezielle Vorkenntnisse erforderlich wären – rechtzeitig warnt, wenn in den Geräten auffällige, abnormale oder «ungesunde» Geräusche auftreten. Das neue maschinelle Lernverfahren lässt sich nicht nur auf unterschiedliche Maschinentypen anwenden, sondern auch auf verschiedene Arten von Signalen, Geräuschen oder Vibrationen. Zum Beispiel erkennt es auch Schallfrequenzen, die Menschen – wie Hochfrequenz-Signale oder Ultraschall – von Natur aus nicht hören können.

Das Lernverfahren schlägt jedoch nicht alle Arten von Signalen über eine Leiste. Vielmehr haben es die Forschenden so entworfen, dass es die feinen Unterschiede der verschiedenen Geräusche feststellen und maschinenspezifische Befunde erstellen kann. Das ist nicht trivial, da der Algorithmus keine Beispiele von defekten Signalen zum Lernen hat.

## Auf «gesunde» Geräusche fokussiert

In realen industriellen Anwendungen lassen sich meist nämlich gar nicht so viele aussagekräftige Geräuschbeispiele von defekten Maschinen sammeln, da Defekte nur selten auftreten. Daher ist es auch nicht gut möglich, dem Algorithmus beizubringen, wie die Geräuschdaten von Fehlern klingen und wie sie sich von den gesunden Geräuschen unterscheiden. Die ETH-Forschenden trainierten die Algorithmen deshalb so, dass der maschinelle Lernalgorithmus lernte, wie eine Maschine normalerweise klingt, wenn sie einwandfrei läuft, und dann erkennt, wenn ein Geräusch vom Normalfall abweicht.

Dabei verwendeten sie eine Vielzahl von Geräuschdaten von Pumpen, Ventilatoren, Ventilen und Gleitschienen und wählten einen Ansatz des «unüberwachten Lernens», bei dem nicht sie einem Algorithmus «sagten», was er lernen soll, sondern der Computer lernte ohne Anleitung und selbstständig die relevanten Muster. Auf diese Weise befähigten Olga Fink und ihr Team das Lernverfahren, verwandte Geräusche innerhalb eines bestimmten Maschinentyps zu erkennen und auf dieser Grundlage zwischen bestimmten Fehlertypen zu unterscheiden.

## Literaturhinweis

Selbst wenn den Forschenden ein Datensatz mit Geräuschdaten von Fehlern zur Verfügung gestanden hätte, und sie dadurch in der Lage gewesen wären, ihre Algorithmen sowohl mit gesunden als auch mit defekten Bespielen zu trainieren, hätten sie nie sicher sein können, dass eine solcherlei gekennzeichnete Datensammlung tatsächlich alle gesunden und fehlerhaften Varianten enthielte. Ihr Sample wäre womöglich unvollständig gewesen und ihr Lernverfahren hätte je nachdem wichtige Fehlergeräusche nicht erkannt. Zudem kann derselbe Maschinentyp – je nach Nutzungsintensität oder Standortklima – sehr verschiedene Geräusche erzeugen, sodass mitunter selbst technisch fast identische Defekte je nach Maschine sehr unterschiedlich klingen.

## Lernen von Vogelstimmen

Der Algorithmus lässt sich beileibe nicht nur auf die Geräusche von Maschinen anwenden. Die Forschenden testeten ihre Algorithmen auch zur Unterscheidung zwischen verschiedenen Vogelstimmen. Dabei verwendeten sie Aufnahmen von Vogelliebhabern. Die Algorithmen mussten lernen, verschiedene Vogelstimmen einer bestimmten Vogelart zu unterscheiden – und zwar so, dass die Art des verwendeten Mikrophones keine Rolle spielte: «Das maschinelle Lernen soll die Vogelstimmen erkennen, nicht die Aufnahmetechnik bewerten», sagt Gabriel Michau.

Dieser Lerneffekt ist auch bei technischer Infrastruktur wichtig: Auch bei den Maschinen müssen die Algorithmen die blossen Hintergrundgeräusche und sowie die Einflüsse der Aufnahmetechnik ausschliessen, um die relevanten Geräusche zu erfassen. Für eine Anwendung in der Industrie, ist es wichtig, dass das maschinelle Lernen die feinen Unterschiede zwischen den Geräuschen erkennen kann. Damit es für die Fachpersonen in der Praxis nützlich und vertrauenswürdig ist, darf es weder zu oft Alarm schlagen noch relevante Geräusche überhören.

«Mit unserer Forschung konnten wir aufzeigen, dass unser Ansatz des maschinellen Lernens die Anomalien unter den Geräuschen erkennt, und dass er so flexibel ist, dass man ihn für verschiedene Signale und verschiedene Aufgaben anwenden kann», schliesst Olga Fink. Ein wichtiges Merkmal ihrer Lernmethode ist, dass sie auch in der Lage ist, die Entwicklung der Klänge zu überwachen, so dass sie aus der Art und Weise, wie sich die Klänge im Laufe der Zeit entwickeln, Hinweise auf mögliche Fehler erkennen kann. Dies eröffnet mehrere interessante Anwendungsmöglichkeiten.

Michau G, Frusque, G, Fink, O. Fully learnable deep wavelet transform for unsupervised monitoring of high-frequency time series. Proceedings of the National Academy of Sciences PNAS, Feb 2022, 119 (8) e2106598119; DOI: externe Seite 10.1073/pnas.2106598119 .


# kuenstliche-intelligenz-verbessert-bildgebung

**Source:** de_news_events/2019/09/kuenstliche-intelligenz-verbessert-bildgebung.html

## Bildverzerrungen korrigiert

Wissenschaftler der ETH Zürich und der Universität Zürich haben Methoden des maschinellen Lernens eingesetzt, um die optoakustische Bildgebung zu verbessern. Mit diesem relativ jungen Verfahren der medizinischen Bildgebung können zum Beispiel Blutgefässe im Körperinnern sichtbar gemacht, die Gehirnaktivität untersucht oder Brustkrebs und Hautkrankheiten diagnostiziert werden. Die Bildqualität, die ein Gerät liefert, hängt allerdings stark von seiner Anzahl Sensoren und ihrer Verteilung ab: Je mehr davon, desto besser die Bildqualität. Der neue Ansatz der ETH-Forschenden ermöglicht, die Zahl der Sensoren bei gleichbleibender Bildqualität deutlich zu reduzieren. Dadurch können die Gerätekosten reduziert, die Bildgebungsgeschwindigkeit erhöht oder die Diagnose verbessert werden.

Die Optoakustik (siehe Kasten) hat gewisse Ähnlichkeiten zur Ultraschallbildgebung. Bei Letzterer sendet eine Sonde Ultraschallwellen in den Körper, die das Gewebe reflektiert. Sensoren in der Sonde detektieren die zurückgeworfenen Schallwellen, und aus diesen lässt sich ein Bild des Körperinneren erzeugen. Bei der optoakustischen Bildgebung hingegen werden extrem schnelle Laserpulse ins Gewebe geschickt, die dort absorbiert und in Ultraschallwellen umgewandelt werden. Diese werden dann ähnlich wie bei der Ultraschallbilgebung detektiert, um daraus ein Bild zu erstellen.

Die Forschenden unter der Leitung von Daniel Razansky, Professor für biomedizinische Bildgebung an der Universität Zürich und der ETH Zürich, suchten nach einer Möglichkeit, die Bildqualität von kostengünstigen Optoakustik-Geräten, die nur wenige Ultraschallsensoren besitzen, zu erhöhen.

## Ärzten die Arbeit erleichtern

Sie nutzten dazu zunächst ein von ihnen selbst entwickeltes hochwertiges Optoakustik-Gerät mit 512 Sensoren, das qualitativ hochstehende Bilder lieferte. Diese liessen sie von einem sogenannten künstlichen neuronalen Netzwerk analysieren. Dabei lernte das Netzwerk die Merkmale der hochwertigen Bilder.

Anschliessend schalteten die Forschenden einen Grossteil der Sensoren aus, so dass nur noch 128 beziehungsweise 32 Sensoren übrigblieben, mit entsprechend negativen Auswirkungen auf die Bildqualität: Weil es an Daten mangelte, durchzogen streifenartige Störsignale das Bild. Wie sich jedoch herausstellte, war das zuvor trainierte Machine-Learning-System mit seinem Algorithmus in der Lage, diese Verzerrungen zu korrigieren. Dadurch erhöhte sich die Bildqualität deutlich und war vergleichbar mit der Qualität einer Messung mit 512 Sensoren.

Bei der Optoakustik erhöht sich die Bildqualität nicht nur mit der Anzahl benutzter Sensoren, sondern auch, wenn das Untersuchungsobjekt aus möglichst vielen unterschiedlichen Richtungen erfasst wird: je grösser der Sektor, in dem die Sensoren rund um das Untersuchungsobjekt angeordnet sind, desto besser die Qualität. Der entwickelte Algorithmus war auch in der Lage, die Qualität von Bildern, die aus nur einem engumfassten Sektor aufgenommen wurden, deutlich zu verbessern. «Dies ist bei klinischen Anwendungen von Bedeutung, denn die benutzten Laserpulse durchdringen nicht den ganzen menschlichen Körper, und die meisten oberflächennahen Teile des menschlichen Körpers kann man nur aus einer Richtung erfassen», erklärt Razansky.

## Die Funktion des Gewebes sichtbar machen

Wie die Wissenschaftler betonen, ist ihr Ansatz nicht auf die optoakustische Bildgebung beschränkt. Weil die Technik nicht die Rohdaten analysiert, sondern die fertigen Bilder, eignet sie sich auch für andere Bildgebungsverfahren. «Generell kann man sie dazu verwenden, um mit weniger Rohdaten Bilder von guter Qualität herzustellen», sagt Razansky. Ärzte seien gelegentlich mit Bildgebungsdaten von schlechter Qualität konfrontiert, die sie interpretieren müssten. «Wir zeigen, dass sich mit Methoden der künstlichen Intelligenz solche Bilder verbessern lassen, wodurch sich die Interpretation vereinfacht.»

Für Razansky ist diese Forschungsarbeit ein gutes Beispiel, wozu die derzeit existierenden Methoden der künstlichen Intelligenz angewandt werden können. «Viele Leute meinen, dass KI die menschliche Intelligenz ersetzen könnte. Dies wird meiner Meinung nach jedoch überschätzt, jedenfalls was heutige KI-Methoden angeht», sagt er. «Mit diesen kann man nicht die menschliche Kreativität ersetzen, aber sie eignen sich, um dem Menschen mühsame repetitive Arbeiten abzunehmen.»

Für diese Forschungsarbeit nutzten die Wissenschaftler ein auf kleine Tiere zugeschnittenes Optoakustik-Tomographiegerät, und sie trainierten das Machine-Learning-System mit Bildern von Mäusen. Als nächstes gehe es darum, die Methode bei Optoaktustik-Bildern von Geweben des Menschen anzuwenden, sagt Razansky.

## Literaturhinweis

Anders als die Optoakustik (oder Photoakustik) bilden viele Bildgebungsverfahren – darunter Ultraschall, Röntgen und MRI – nur die Strukturen des Körperinnern ab. Um zusätzlich funktionelle Informationen zu erhalten, zum Beispiel zum Stoffwechsel, müssen dem Patienten vor der Bildgebung Kontrastmittel oder radioaktive Tracer verabreicht werden. Die optoakustische Methode hingegen liefert auch ohne Kontrastmittel funktionelle und molekulare Informationen, etwa lokale Veränderungen der Blutsauerstoffkonzentration – eine wichtige Information bei der Früherkennung von Krebs – oder den Lipidgehalt von Blutgefässwänden, was der Diagnose von Herzkreislauferkrankungen dient.

Weil die bei der optoakustischen Bildgebung genutzten Lichtwellen im Gegensatz zu anderen Wellen den Körper nicht vollständig durchdringen, eignet sich die Methode allerdings nur, um Gewebe bis in eine Tiefe von wenigen Zentimetern unter der Haut zu untersuchen.

Davoudi N, Deán-Ben XL, Razansky D: Deep learning optoacoustic tomography with sparse data, Nature Machine Intelligence, 16. September 2019, doi: externe Seite 10.1038/s42256-019-0095-3


# praezise-schneemessung-dank-ki-und-satelliten.html

**Source:** de_news_events/2023/12/praezise-schneemessung-dank-ki-und-satelliten.html

## In Kürze

- ETH-Forschende haben zusammen mit der Schweizer Firma ExoLabs ein KI-gestütztes Schneemesssystem entwickelt, das die Schneehöhe täglich und genauer als bisher bestimmen kann.

- Durch die Verwendung von Satellitenbildern kann die Schneehöhe sogar aktualisiert werden, ohne dass dafür neue Messdaten am Boden benötigt werden.

- Ein weiterer Vorteil der neuen Technologie ist, dass sie etwa Wintersportler:innen oder Kraftwerksbetreibern die Unsicherheit der Schätzung mitliefert.

## Satellitendaten der Europäischen Weltraumorganisation

Wie viel Schnee liegt wo in den Bergen? Diese Frage ist für den Wintertourismus und Betreiber von Wasserkraftwerken gleichermassen relevant wie für Wintersportler:innen, die die Lawinengefahr einschätzen wollen. Doch die Messung der Schneehöhe ist mit einigen Herausforderungen verbunden: Sie kann sich je nach Wetterlage schnell ändern, hängt stark vom Gelände ab und ist auf Luftbildern nicht direkt erkennbar.

Die Schneeüberwachung in der Schweiz stützt sich heute vor allem auf die Daten von Messstationen. Da es für die ganze Schweiz nur rund 400 Stationen gibt, sind die Schneeangaben für viele Orte eher ungenau. Das könnte sich nun ändern: ETH-Forschende um Konrad Schindler, ETH-Professor für Photogrammetrie und Fernerkundung, haben zusammen mit der Schweizer Firma ExoLabs, einem Spin-off der Universität Zürich, eine Technologie entwickelt, die mit Hilfe von Satellitenbildern und künstlicher Intelligenz die Schneehöhe schneller und genauer als bisher ermittelt.

«Während die besten bestehenden Schneekarten der Schweiz eine effektive Auflösung von etwa 250 mal 250 Meter haben, kann man in unsere Karten bis auf 10 mal 10 Meter hineinzoomen, um die Schneehöhe abzulesen», sagt Schindler. Zudem sind regelmässige Aktualisierungen zur Schneehöhe in Zukunft nicht mehr unbedingt auf neue Messdaten am Boden angewiesen. Öffentlich zugängliche Satellitenbilder reichen bei gutem Wetter aus.

## Satellitendaten der Europäischen Weltraumorganisation

Schindlers Forschungsgruppe hat viel Erfahrung mit Satellitenbildern: Sie nutzt sie, um die Bevölkerungsdichte in Krisengebieten vorherzusagen, um Kriegsschäden an Gebäuden in der Ukraine zu ermitteln oder um weltweit die Höhe von Wäldern zu vermessen. Doch wie liest eine künstliche Intelligenz die Schneehöhe von Satellitenbildern ab?

Sie braucht dafür zunächst Millionen von Beispielen: Für ihre Technologie verwendeten die Forschenden optische Aufnahmen und Infrarotbilder von Sentinel-2-Satelliten der Europäischen Weltraumorganisation (ESA). Diese Satelliten nehmen alle fünf Tage jeden Ort der Erde mit einer Auflösung von bis zu 10 mal 10 Metern pro Pixel auf. Das sind die detailliertesten Bilder, die derzeit kostenlos und unbeschränkt zugänglich sind. Dadurch erkennt die KI, wann in der Schweiz wo Schnee liegt und wie sich die Schneegrenze wöchentlich verändert.

Doch das allein reicht nicht: «Von den weissen Flächen in den Satellitenbildern können wir nicht direkt auf die Schneehöhe schliessen. Dafür braucht es noch weitere Daten», sagt ETH-Professor Schindler.

## Lernen durch Vergleich mit Realität

Neben den Satellitenbildern fütterten die Forschenden der KI daher umfassende Geländedaten der Schweiz. Denn an einem steilen Südhang schmilzt bei Sonnenschein mehr Schnee als in einer schattigen Mulde. Detaillierte Geländedaten dieser Art sind in den öffentlichen Daten von Swisstopo sehr gut zugänglich.

Die Forschenden trainierten das KI-System darauf, die Schneehöhe aus Satelliten- und Geländedaten abzuleiten. Dazu liessen sie das System die Schneehöhen schätzen und verglichen die Ergebnisse mit realen Schneemessungen. «Wir haben an jedem Rasterpunkt festgestellt, wie weit die KI mit ihrer Schätzung daneben lag, und das System schrittweise so angepasst, dass die Fehler kleiner wurden», erklärt Schindler. In der Fachsprache heisst diese Methode supervised learning.

In einer ersten Trainingsrunde verwendeten die ETH-Forschenden die Schneekarten von ExoLabs, die sehr gut mit den Daten der Schneemessstationen in der Schweiz übereinstimmen. Diese Karten basieren neben den Satellitenbildern von Sentinel-2 auch auf Bildern anderer Satellitenmissionen, die zwar räumlich weniger genau sind, dafür aber tägliche Aufnahmen liefern. Anhand der Schneekarten von ExoLabs prägte sich die KI vor allem die Muster der kleinräumigen Schneeverteilung ein, die über das eher grobmaschige Netz an Messstationen nicht erfasst werden kann.

## Finetuning mit Daten aus dem Dischmatal

Das Finetuning der KI erfolgte dann mit sehr detaillierten Schneedaten, die das WSL-Institut für Schnee-und Lawinenforschung SLF lediglich im Bündner Dischmatal erhebt. Durch diese Daten lernte die KI, dass sich die Schneehöhe je nach Gelände innerhalb von wenigen Metern ändern kann. Diese räumlichen Zusammenhänge kann sie dann in der ganzen Schweiz anwenden und auch dort die Schneehöhe genau vorhersagen, wo keine detaillierten Messdaten durch Messtationen vorliegen.

Ein weiterer Vorteil der neuen Technologie ist, dass sie den Nutzer:innen auch die Unsicherheit der Schätzung mitliefert. Wenn es zum Beispiel länger bewölkt ist und neue Satellitenbilder keine brauchbaren Informationen liefern, steigt die Unsicherheit der Schätzung.

## Neuer Standard für die Schneehöhenmessung

Die ETH-Forschenden haben die KI-gestützte Schneemessung bereits während zweier Wintersaisonen erfolgreich getestet. «Wir gehen davon aus, dass wir damit einen neuen Standard für die Schneehöhenmessung in der Schweiz setzen», sagt Schindler.

Um die Vermarktung der Technologie kümmert sich die Schweizer Firma ExoLabs. Das Start-up bietet hochaufgelöste Schneekarten in verschiedenen Apps an, unter anderem in den Anwendungen von Outdooractive, Strava, Skitourenguru, Hüttenbuch oder über die swisstopo-App. Geht es nach Reik Leiterer, CEO von ExoLabs, sollen die verbesserten Schneekarten in Zukunft auch für Gebiete ausserhalb der Alpen erhältlich sein, zum Beispiel in Skandinavien, den Pyrenäen, oder für Nord- und Südamerika.

## Innosuisse Projekt «DeepSnow»

Dieses Forschungsprojekt wurde von Innosuisse finanziert. Weitere Projektpartner waren neben ExoLabs das WSL-Institut für Schnee- und Lawinenforschung SLF, Outdooractive und MountaiNow.

externe Seite Weitere Informationen zum Projekt

Daudt R, Wulf H, Hafner E, Bühler Y, Schindler K, Wegner J: Snow depth estimation at country-scale with high spatial and temporal resolution, ISPRS Journal of Photogrammetry and Remote Sensing 197 (2023) 105–121: doi: externe Seite 10.1016/j.isprsjprs.2023.01.017


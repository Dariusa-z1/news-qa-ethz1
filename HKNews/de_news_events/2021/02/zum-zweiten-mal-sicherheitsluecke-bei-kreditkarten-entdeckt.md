# zum-zweiten-mal-sicherheitsluecke-bei-kreditkarten-entdeckt

**Source:** de_news_events/2021/02/zum-zweiten-mal-sicherheitsluecke-bei-kreditkarten-entdeckt.html

**Date processed:** 2025-05-01

## Sicherheitsschranke doppelt überlistet

Die von den Forschern genutzte Methode orientiert sich unter anderem am «man-in-the-middle»-Prinzip. Dabei manipuliert der Angreifer den Datenaustausch zwischen zwei Kommunikationspartnern, in diesem Fall zwischen Karte und Karten-Terminal. Die Forscher brauchten dafür eine eigens kreierte Android-App und zwei NFC-fähige Mobiltelefone. Die App signalisierte dem Karten-Terminal in unwahrer Weise, dass erstens kein PIN nötig sei, und dass zweitens der Karteninhaber verifiziert wurde. In einem ersten Schritt funktionierte die Methode nur bei Visa-Karten, da andere Anbieter ein anderes Protokoll verwenden (ein Protokoll regelt die Datenübertragung).

Die Idee, die der zweiten erfolgreichen PIN-Code-Überlistung zugrundliegt, wirkt auf den ersten Blick simpel: «Unsere Methode lässt den Terminal annehmen, dass eine Mastercard-Karte eine VISA-Karte sei», erzählt Jorge Toro, Mitarbeiter bei der Professur für Informationssicherheit und einer der Autoren des Papers. Das sei in der Realität deutlich komplexer als es klingt, fügt der Informatiker an. Zwei Sitzungen müssen gleichzeitig laufen, damit es gelingt. Mit dem Karten-Terminal wird eine Visa-Transaktion durchgeführt, während mit der Karte eine Mastercard-Transaktion läuft. Die Forscher wendeten diese Methode bei zwei Mastercard-Kreditkarten sowie zwei Maestro-Debitkarten von vier verschiedenen Banken an.

## EMV-Standard als Fehlerquelle

Die geschilderten Sicherheitslücken bei kontaktlosen Bezahlkarten hängen vor allem mit dem sogenannten EMV-Standard zusammen, einem internationalen Protokollstandard, der diesen Karten zugrundliegt. Logische Fehler in diesem Regelwerk sind schwer auffindbar, nur schon wegen seiner schieren Länge von über 2'000 Seiten. Die ETH-Forscher betonen auf ihrer Projektwebsite, dass solche Systeme vermehrt automatisch geprüft werden müssen, da sie für Menschen zu komplex seien.


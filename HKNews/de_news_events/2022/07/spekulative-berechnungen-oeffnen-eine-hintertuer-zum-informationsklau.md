# spekulative-berechnungen-oeffnen-eine-hintertuer-zum-informationsklau

## Spekulatives Rechnen macht Computer schneller

Manchmal blutet ein Computer aus seinem Herzen und gibt tröpfchenweise private Informationen preis. Das trifft auf die heute öffentlich gemachte Hardware-Sicherheitslücke «Retbleed» zu: Diese Sicherheitslücke entsteht in den Mikroprozessoren, welche die Anweisungen eines Computerprogramms ausführen und die entsprechenden Berechnungen durchführen.

Zum Teil führen die Prozessoren – namentlich die zentralen Recheneinheiten (engl. «central processing units», CPU) – auch spezielle Rechenschritte aus, die die Rechenzeit verkürzen und den Rechenvorgang insgesamt beschleunigen. Dabei hinterlassen sie Spuren im Speicher, die Hacker ausnutzen könnten, um unbefugt Zugriff auf beliebige Informationen im System zu erhalten – zum Beispiel könnten sie Verschlüsselungscodes oder sicherheitsrelevante Passwörter entwenden. Dies ist besonders riskant in Cloud-Umgebungen, in denen mehrere Unternehmen gemeinsam Computersysteme nutzen. Das Nationale Zentrum für Cybersicherheit in Bern erachtet die Schwachstelle als schwerwiegend, da die betroffenen Prozessoren weltweit im Einsatz sind. Jedoch haben die Hersteller bereits erste Massnahmen ergriffen, um die Sicherheitslücke zu schliessen.

Entdeckt haben die Sicherheitslücke der Doktorand Johannes Wikner und Kaveh Razavi, ETH-Professor für Computersicherheit. Der Name «Retbleed» bezieht sich auf eine bestimmte Art von Programmanweisungen, die sogenannten Returns. Ein Computerprogramm besteht aus Folgen von Anweisungen oder Befehlen (engl. «instruction» oder «command»), die in Funktionen organisiert sind, mit denen die Prozessoren die jeweils erwünschten Berechnungen durchführen. Nachdem eine Funktion ausgeführt wurde, veranlasst ein Return-Befehl den Prozessor, zu dem Punkt im Computerprogramm zurückzukehren (engl. «to return»), der unmittelbar auf den ursprünglichen Befehl folgt, der die Funktion verwendet hat.

## Ungeschützte Return-Befehle

Man kann sich den Ablauf eines Computerprogramms wie einen Fluss mit verschiedenen Verzweigungen vorstellen. An den Verzweigungen treffen die Computerprogramme oft Entscheidungen, welchen Lauf sie wählen. Manchmal dauern diese Entscheidungen lange und können die Ausführung verlangsamen. Gefragt sind jedoch schnelle Rechenprozesse. Herkömmlicherweise führt ein Computerprogramm die Anweisungen sequenziell und in der Reihenfolge des Programms aus – also einen Rechenschritt nach dem anderen.

Mit den CPU-Prozessorarchitekturen von heute lassen sich jedoch Berechnungen vorziehen und gleichzeitig ausführen. «Eine CPU kann die Anweisungen in einer anderen Reihenfolge als der Programmreihenfolge ausführen, um die Rechenleistung zu verbessern», sagt Kaveh Razavi. In Computerkreisen sprich man von «ausserplanmässigen Ausführungen» (engl. «out-of-order executions»). Seit Januar 2018 ist bekannt, dass es bei dieser Art der Ausführung Sicherheitslücken geben kann. Während der Befehlsausführung könnte ein unerlaubter Zugriff auf den Cache-Speicher der CPU erfolgen, der es Hacker:innen ermöglicht, sensible Informationen aus dem Betriebssystem zu stehlen. Diese Sicherheitslücke ist unter dem Namen «Meltdown» bekannt und betrifft spezifische Probleme bei Intel-CPUs.

Mit den Out-of-order-Ausführungen eng verwandt sind die «spekulativen Ausführungen» (engl. «speculative executions»), für die ebenfalls seit 2018 ähnliche Sicherheitsprobleme bekannt sind. «‹Retbleed› ist ein Problem der spekulativen Ausführung», sagt Johannes Wikner. Solche spekulativen Rechenschritte dienen dazu, die Verlangsamung der Berechnungen zu vermeiden, indem bestimmte Rechenschritte vorgezogen werden, bevor klar ist, ob sie tatsächlich gebraucht werden. Spekulative Berechnungen finden zum Beispiel statt, wenn ein Prozessor zu erraten versucht, welchen Weg die Befehlskette an einer Verzweigung einschlägt, bevor dies bekannt ist. «Dabei ‹raten› die CPUs, welche Richtung sie an einer Verzweigung einschlagen sollen und führen die Anweisungen aufgrund ihrer Vermutung spekulativ aus», erklärt Razavi.

## Lösungsansatz für Vorkehrungsmassnahmen

Mithilfe solcher Spekulationen wird der Fluss der Befehlskette verbessert und die Rechenleistung der Prozessoren erhöht. Falls die spekulative Berechnungen nicht benötigt werden, werden sie rückgängig gemacht. Auch diese Spekulationen hinterlassen Spuren im Cache-Speicher, die eine Hintertür für Hacker:innen öffnen. Diese Sicherheitslücke wurde ebenfalls im Januar 2018 unter dem Namen «Spectre» öffentlich gemacht und betrifft die Prozessoren der Hersteller Intel und AMD. Seither haben Intel und AMD sowie grosse Software-Hersteller wie Microsoft Vorkehrungsmassnahmen ergriffen. Die Schwachstellen der spekulativen Berechnungen sind jedoch bis heute weder abschliessend erforscht noch behoben.

Wie Razavi und Wikner nun herausgefunden haben, gibt es tatsächlich ein bisher nicht behobenes Sicherheitsproblem: «Wir haben gezeigt, dass bei spekulative Berechnungen besonders viele Return-Anweisungen ungeschützt sind und missbraucht werden können», sagt Johannes Wikner. Im Prinzip funktioniert «Retbleed» wie die Variante 2 von «Spectre» und betrifft die Mikroprozessoren von Intel und AMD. «Da die bisher getroffenen Vorkehrungsmassnahmen die Return-Anweisungen nicht berücksichtigten, sind die meisten bestehenden Mikroprozessoren und Computersysteme für ‹Retbleed› anfällig», ergänzt Razavi. «Es braucht jedoch einiges an Computerfachwissen, um sich den Speicherzugriff zu verschaffen und Information zu stehlen», sagt Wikner.

Im Februar haben Razavi und Wikner den Nachweis erbracht (engl. «Proof of Concept»), dass «Retbleed» ein ernsthaftes Problem darstellt. Inzwischen sind ihre Ergebnisse sie einem Fachartikel veröffentlicht, der als externe Seite Konferenzbeitrag der USENIX Security 2022 akzeptiert worden ist. In diesem Artikel haben Wikner und Razavi den ersten Ansatz von Intel und AMD zur Lösung dieses Problems untersucht.

## CVE-Identifikationsnummer für Retbleed

Dieser Ansatz setzt dabei an, dass die Befehle, wenn der Mikroprozessor an einer Verzweigung spekuliert, manchmal falsch ausgeführt werden. Dann führt die Berechnung nicht zum richtigen Ziel und eröffnet ein Leck, durch das Hacker:innen Zugriff zu den Informationen im Speicher erhalten. Derzeit besteht die Lösung darin, zu verhindern, dass Hacker:innen die Entscheidung der Mikroprozessoren für Ziele der Return-Befehle beeinflussen. Leider geht dies mit einem erheblichen Leistungsverlust einher, der Computer um 12 bis 28 Prozent langsamer macht.

Wie in solchen Fällen üblich, haben die Sicherheitsforschenden zuerst die betroffenen Hersteller AMD und Intel informiert, bevor die Sicherheitslücke veröffentlicht wird. Da die konkreten Sicherheitsrisiken auch von der unternehmensspezifischen Prozessorarchitektur abhängen, benötigen die Hersteller Zeit, um vertiefte Vorkehrungen zu ergreifen. Seither haben unter anderem Microsoft, Oracle, Google, Linux, Intel, AMD, ARM an Schutzmassnahmen gearbeitet, bevor «Retbleed» heute öffentlich bekannt gemacht wurde. Ein Intel-Mikroprozessor, der 3 bis 6 Jahre alt ist, oder ein AMD-Prozessor, der 1 bis 11 Jahre alt ist, ist aller Wahrscheinlichkeit nach betroffen.

Das Nationale Zentrum für Cybersicherheit (NCSC) in Bern hat heute für die Sicherheitslücke “Retbleed” in Zusammenarbeit und in Absprache mit den Forschenden der ETH Zürich die CVE-Nummern CVE-2022-29900 (für Prozessoren des Herstellers AMD) und CVE-2022-29901 (für Prozessoren des Herstellers Intel) vergeben. Die Zuordnung einer CVE (Common Vulnerabilities and Exposure) ermöglicht eine weltweit eindeutige Identifizierung von Schwachstellen. Seit September 2021 ist das NCSC als die Schweizer Zulassungsbehörde anerkannt, die CVE-​Nummern vergibt.

## Literaturhinweis

Weitere Informationen finden Sie in dem Bericht auf der NSCS-​Website unter der Rubrik « externe Seite Eingegangene Meldungen ».

Wikner, J; Razavi, K. RETBLEED: Arbitrary Speculative Code Execution with Return Instructions. Paper accepted at the 31st USENIX Security Symposium, August 10–12, 2022, at the Boston Marriott Copley Place in Boston, MA, USA.

Wikner und Razavi werden ihre Ergebnisse auf der externe Seite USENIX Security '22 am 12. August 2022, 13.30-2.30 Uhr, vorstellen.


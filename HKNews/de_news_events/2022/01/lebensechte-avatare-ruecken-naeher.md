# lebensechte-avatare-ruecken-naeher

**Source:** de_news_events/2022/01/lebensechte-avatare-ruecken-naeher.html

## Computermodell kann sogar Überschlag darstellen

Spätestens seit der Corona-Pandemie starren wir noch häufiger in den Bildschirm. Sitzungen, Gespräche mit Arbeitskolleg:innen oder Konferenzen finden per Videotelefonie statt. Geht es nach den grossen Tech-Unternehmen, sollen wir uns dagegen schon ab nächstem Jahr in einer virtuellen Erlebniswelt, dem sogenannten Metaversum, treffen können – mittels 3D-Brillen und spezialisierten Computerprogrammen.

Der Schlüssel zu einem möglichst natürlichen Nutzererlebnis in Virtual-Reality-Anwendungen sind sogenannte Avatare, also computergenerierte, plastische Darstellungen von Menschen. Je realistischer die Avatare aussehen und sich verhalten, desto eher stellt sich das Gefühl einer echten sozialen Interaktion ein.

Einen Menschen detailgetreu und in Bewegung zu modellieren, fordert die Entwickler:innen solcher Anwendungen jedoch nach wie vor heraus. Heute können Grafikprogramme zwar schon fotorealistische, statische Avatare erstellen. Um aber beispielsweise ein lachendes Gesicht zu animieren, müssen Grafikdesigner:innen fast jedes Einzelbild am Computer nochmals von Hand bearbeiten; sie bessern Nuancen wie Falten und den Schattenwurf aus.

Wie es einfacher geht, zeigten Forscher um Otmar Hilliges, Professor für Computerwissenschaften an der ETH Zürich, in einer neuen Studie, die sie an der externe Seite Internationalen Konferenz für Computer Vision im Herbst 2021 veröffentlichten. Anstatt jedes Detail zu modellieren, nutzen die Wissenschaftler intelligente Algorithmen, die basierend auf 3D-Bildern von Menschen in einigen wenigen Posen lernen, animierte Ganzkörper-Avatare in allen erdenklichen Posen automatisch darzustellen.

## Beliebig neue Gesichter mit nur einem Bild

Computerprogramme, die mithilfe künstlicher Intelligenz (KI) lebensechte virtuelle Menschen erstellen, existieren erst seit wenigen Jahren. Damit diese Programme die verschiedenen Körperpositionen realistisch abbilden können, werden sie mit sogenannten 3D-Scans eines realen Menschen trainiert, die ein komplexes Kamerasystem vorgängig aufgenommen hat.

Die KI-Algorithmen verarbeiten die Scans, indem sie unzählige Punkte ausserhalb und innerhalb des Körpers vermessen und so dessen Konturen als mathematische Funktion definieren. Sie erstellen dabei eine erste Darstellung des Menschens in der Grundposition. Die Algorithmen berechnen nun jeweils den Weg von einer bewegten Pose zurück in diese Grundposition. Auf diese Weise bauen sie ein Computermodell auf, das Avatare in Bewegung versetzen kann.

Extreme Posen ausserhalb des bekannten Bewegungsrepertoires überfordern solche Modelle jedoch und es entstehen gut sichtbare Fehler in den Darstellungen: Die Arme sind losgelöst vom Körper oder die Gelenke am falschen Ort positioniert. Heutige Modelle werden daher mit möglichst vielen verschieden Posen trainiert, was einen riesigen Aufwand für die Bilderfassung bedeutet und eine enorme Rechenleistung voraussetzt.

Gerade für interaktive Anwendungen sind KI-Avatare daher bislang kaum verwendbar. «Es ist unmöglich und vor allem ineffizient, das gesamte Bewegungsrepertoire im Bild einzufangen», sagt Xu Chen, ETH-Doktorand und Erstautor der Studie.

## Wer genau hinschaut, kann Deepfakes entlarven

Die von Chen entwickelte neue Methode verfolgt hingegen den umgekehrten Ansatz: Ausgehend von der Grundposition berechnen die KI-Algorithmen den Weg zu einer bewegten Pose. Weil auf diese Weise der Ausgangspunkt der Berechnungen immer der gleiche bleibt, lernen die Algorithmen besser, Bewegungen zu verallgemeinern.

Ein solches Computermodell ist erstmals in der Lage, auch neue Bewegungsmuster problemlos darzustellen. Selbst akrobatische Bewegungen wie einen Überschlag oder eine Rückenbrücke kann es erzeugen.

Noch lassen sich die neuen Ganzkörper-Avatare nicht personalisieren; die Darstellungen beschränken sich auf den Menschen, von dem die 3D-Bilder stammen. Chen und seine Kollegen möchten daher das Computermodell dahingehend weiterentwickeln, dass es beliebig neue Identitäten erschaffen kann.

Um die Gesichter von Avataren zu personalisieren und beliebig abzuändern, hat Marcel Bühler, ebenfalls Doktorand in Hilliges Gruppe, bereits eine Lösung gefunden. Wie auch Chen in seinen Ganzkörpermodellen nutzte Bühler intelligente Algorithmen, die aus der Kombination von einem 3D-Gesichtsmodell und einer grossen Palette von Porträtfotos neue animierte Gesichter zu kreieren.

## Literaturhinweis

Während bisherige Computerprogramme bereits gute Animationen von Gesichtern in der Frontalansicht liefern, kann das Modell von Bühler auch Gesichter in der seitlichen Ansicht sowie von oben und unten realistisch darstellen.

Besteht die Gefahr, dass mit der neuen Technik bald noch realistischere Deepfake-Videos kursieren, um beispielsweise eine Rede eines wichtigen Politikers vorzugaukeln? «Deepfake-Videos sind noch lange nicht perfekt», erklärt Bühler. Die meisten Computerprogramme würden oft nur für ein bestimmtes Setting gute Resultate liefern. So kann das neue Gesichtsmodell beispielsweise Details wie Haare noch nicht realistisch darstellen.

«Wer genau hinschaut, findet nach wie vor Fehler», sagt der ETH-Doktorand. Er findet es wichtiger, die Öffentlichkeit über den aktuellen Stand der Dinge zu informieren und sie zu sensibilisieren. Wenn Forschungsarbeiten zu 3D-Darstellungstechniken wie auch deren Schwachstellen öffentlich zugänglich seien, könnte dies Cybersecurity-Expert:innen dabei helfen, Deepfake-Videos im Web leichter aufzuspüren, so Bühler.

Für interaktive Virtual-Reality-Anwendungen bringt die Arbeit der ETH-Forscher grosse Fortschritte. Gut möglich, dass Tech-Unternehmen wie Facebook und Microsoft die neu entwickelten Techniken der beiden Doktoranden in ihre Avatare implementieren werden.

Chen X, Zheng Y, Black M, Hilliges O, Geiger A. externe Seite SNARF: Differentiable Forward Skinning for Animating Non-Rigid Neural Implicit Shapes . International Conference on Computer Vision (ICCV), online publiziert am 11. Oktober 2021.

Bühler M, Meka A, Li G, Beeler T, Hilliges O. externe Seite VariTex: Variational Neural Face Textures . International Conference on Computer Vision (ICCV), online publiziert am 11. Oktober 2021.


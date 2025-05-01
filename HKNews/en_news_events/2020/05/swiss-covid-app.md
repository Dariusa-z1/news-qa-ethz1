# swiss-covid-app

## Many are following the Swiss idea

People in Switzerland are gradually returning to their everyday routines and their work now that the peak of the coronavirus crisis seems to have passed. But the easing of the lockdown also fuels fears about a second wave of infection. Strict adherence to health and safety rules is the best strategy for protecting ourselves against COVID-19 infection. In addition, the government intends to provide the Swiss population with a tracing app as soon as possible that should help to stem the spread of the virus. The app is being developed as part of the DP-3T project by ETH Zurich and EPF Lausanne, working together with international researchers.

## Cooperation with Google and Apple

ETH scientists are actively involved in the design, security assessment, data protection and performance of the SwissCovid app. Srdjan Čapkun, Professor for Systems and Network Security, one of the developers of the SwissCovid app, stresses: "This is not 'only' a smartphone app, but a complex distributed contact tracing system. Its main purpose is to notify people of exposure to infected persons. But it is also designed to preserve user privacy, enable roaming between countries, and work on top of existing smartphone software and hardware."

## How does the app work?

Many projects and countries have taken the same route in developing their own tracing apps. Some are using parts of the DP-3T code, while others are implementing it independently and adapting it to their own country. But the underlying concept is the same. “This is an experiment for all of us. Something like this has never been attempted before,” says Čapkun.

## What happens at the end of the pilot phase?

Some people might be concerned about privacy issues, given the involvement of the two tech giants Google and Apple. Čapkun, who himself attaches great importance to data protection, is reassuring: "In our design, information is processed locally and all data are automatically deleted after 21 days. In addition, no user personal data is stored centrally, and contact tracing data never leaves the phone unless authorized by the user.” The SwissCovid app is also open sourced, so that its design and implementation will be available for public inspection. “All of us are trying to build a contact tracing system on top of software and hardware that was not designed for this purpose. Bluetooth was not developed for this kind of large-scale distance measurement. Making sure that we can use it in this way requires a lot of engineering skill and collaboration, including collaboration with Apple and Google,” says Čapkun. Switzerland is the first country in the world to use APIs from Google and Apple for the tracing app. "It also means that we are the first to have to deal with the teething troubles of the program. We therefore need feedback from users before we start the national rollout in June," says Čapkun.

## Don't miss the latest news

The app uses Bluetooth beaconing technology to detect nearby smartphones that are also running the app. When two such devices are in close proximity, they exchange random beacons – a kind of private keys. The app is configured to inform users if they have spent more than 15 minutes within 2m of infected people. These parameters have been set by the epidemiologists and will be fine-tuned if new information about the virus would make it necessary.

When a user is tested positive for COVID-19, they will receive a code from the cantonal medical service, which will allow them to anonymously inform others about the infection. All other users will be able to check if they have spent significant time in close proximity with infected people, without learning their identity or the location of the possible infection. Since the project has many legal and ethical dimensions, the researchers are also working with the federal offices, the FOPH and the FOITT.

The main purpose of the pilot phase is to thoroughly test the functionality of all the system components and of course their interaction. One of the challenges is to make sure that we can accurately detect proximity between people based on Bluetooth signals. For example, distinguishing between distances of two and four metres based on these signals is not always possible. Clearly, the probability of infection depends not only on distance but also on many other factors. "Working with epidemiologists, we therefore came up with risk scores that aim to reduce false positives and false negatives."

And what happens if bugs in the app are detected? "That's the exact purpose of this pilot phase – anything we can correct or improve now will make the app work much better later,” says Čapkun. "I want to especially mention two ETH members of my group, Dr Marc Roschlin and Patrick Leu, who spent many hours working on these measurements and their analysis."

The pilot phase is covered by a provisional ordinance passed by the government and will run till the end of June at the latest. However, the development team hopes that the pilot will produce results much sooner, and that parliament will be able to pass draft legislation in its next session at the start of June to allow the SwissCovid app to be rolled out quickly to the entire Swiss population.


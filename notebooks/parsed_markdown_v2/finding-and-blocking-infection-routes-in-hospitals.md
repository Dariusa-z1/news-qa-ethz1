# finding-and-blocking-infection-routes-in-hospitals.html

**Source:** en_news_events/2024/02/finding-and-blocking-infection-routes-in-hospitals.html

## In brief

- In partnership with an ETH-spinoff, researchers develope an ultra-wideband wearable to track proximity contacts in infection networks in hospitals more accurately.

- In Switzerland, Kenya, and Ivory Coast, the research team tested the device that tracks contact distances between hospital employees.

- The results help investigate potential hot spots for risk and the effect of measures like mask types on infection routes. They also help to adapt technologies and processes to cultural differences.

## Measurement accuracy improves preparedness

Hospital-acquired infections are an immense problem. “During the COVID-19 pandemic, many infections occurred in hospitals. Not only did this put vulnerable patients in danger, but many facilities experienced major staffing problems because lots of their employees were ill at the same time,” says Onicio Batista Leal Neto.

Leal Neto was until recently Senior Researcher in the Systems Security Group at the Department of Computer Science at ETH Zurich and is now starting as Assistant Research Professor for Digital Epidemiology at the University of Arizona. He and other researchers wanted to find out how to better identify outbreaks of infection and prevent the infections from spreading. To be able to interrupt the chains of infection in a targeted manner, it is necessary to understand the interactions between people. An individual’s social network shows the possible routes along which an infection could spread.

## Measurement accuracy improves preparedness

In the Wearable Proximity Platform project, computer scientists and epidemiologists from ETH Zurich, EPFL, ISI Foundation and the ETH spinoff 3db Access, developed a proximity tracking system that can measure distance to evaluate an exposure risk to an infection such as namely in a hospital environment. The technological heart of the system takes the form of special badges. These work by combining 3db Access’s UWB (ultra-wideband) radio technology with the integrated software and the experience of the SocioPatterns co-operation led by the ISI Foundation. ISI is an interdisciplinary European research centre near Turin. Over the last decade, this collaboration has carried out measurements of human proximity networks in a variety of contexts relevant to the spread of infectious diseases, spanning schools, hospitals, social gatherings and low-resource rural settings worldwide.

“When it comes to mapping infection networks, a more precise distance measurement could make a decisive difference, if not for COVID, then at least for many other diseases,” explains Leal Neto. During the COVID-19 pandemic, for example, it was established that a coronavirus infection is very likely to be passed on if an encounter lasts at least 15 minutes and takes place at a distance of less than 150 centimetres. Similar to the SwissCovid app during the pandemic, the new system therefore has the potential to improve the detection of chains of infection based on contact duration and distance.

## Cultural factors are decisive

The research team has tested its solution in a variety of environments such as a Swiss hospital and healthcare facilities in Africa, as well as in two rural villages in Kenya and the Ivory Coast.

However, the technology and its possibilities are only one aspect of the system, context is another. “Understanding the cultural environment is just as important for the success of an application like this,” as Leal Neto knows from experience of numerous projects in collaboration with the SocioPatterns group, including in Brazil and Malawi.

The data the system provides, needs to be interpreted differently depending on the circumstances. One consideration is exactly how the sensors are worn. Garments made of thick fabric, for example, can affect the signal quality. With this in mind, Leal Neto and the research team have already put the system through its paces at an early stage, with initial pilot deployments in Switzerland, Kenya and Ivory Coast.

## Identifying risk situations

In Switzerland, badges were issued to almost all of the 40 employees in the infectious diseases outpatient centre at the Kantonsspital St. Gallen – from nurses and medical teams to the administrative staff – for one working day. Four fixed sensors were also installed at the coffee machine, in the lounge and at the hand hygiene dispensers in two patient rooms. “Although the system is still in its infancy, the initial results are already extremely revealing. These kinds of applications have great potential in hospitals,” says Philipp Kohler, who supervised the study as the hospital’s senior physician.

In hospitals, what such systems enable above all is much more effective prevention. “If we know where and under what circumstances risky contacts take place, we can take targeted action, for example by making masks mandatory in certain situations,” Kohler explains. It should also be possible to investigate questions such as the effect on the infection rate of different mask types or hand disinfection routines.

## More challengingfor village communities

In Kenya and the Ivory Coast, the research team partnered with two local organisations to set up tests in rural areas. These partners were the Centre Suisse de Recherches Scientifiques (CSRS) in Côte d’Ivoire and the Center for Public Development (CPDH) in Kenya. For Onicio this collaboration with local organisations was a key step: “If you want people to participate, your project must incorporate the local social fabric and the social norms of the communities.” A total of 340 employees in healthcare facilities and villagers took part.

## Scientific alliance for social good

Findings showed that the system works well for hospital staff in Kenya and the Ivory Coast. However, the system proved to be less suitable to village communities. Their compliance with the devices wasn’t consistent. For Leal Neto, the tests show that the entire cultural context must always be taken into account when introducing technological systems. He is convinced that this is also an issue for higher education: “If students want to develop successful systems, they need to understand the cultural factors affecting a solution just as much as the technical interdependencies.”

That is precisely what motivates him most: “I want my work to help ensure that underserved communities can also benefit from modern technologies.”

Regarding the application of this technology, the research team sees scope for two main improvements in the future. First, the sensors will use Bluetooth Low Energy for mutual identification in order to further reduce their energy consumption, as seen in other existing platforms. The more energy intensive UWB will then only have to determine the exact distance between sensors. Second, they want to use the particular energy efficient LoRa (from “long range”) technology, which was developed for the Internet of Things (IoT), to transmit the data.

This project is part of the overarching research initiative "EPFL COVID-19 Real-Time Epidemiology." This initiative, spearheaded by EPFL, and including ETH Zurich's Department of Computer Science, 3db Access, TU Delft, University College London ( UCL ) and ISI Foundation, aims to deliver a secure, open-source, and privacy-enhancing toolset tailored to epidemiologists and public health practitioners. The project is funded by the Fondation Botnar.

The Department of Computer Science at ETH Zurich has played a pivotal role in the Ultra-wide band technology's architectural development. "Our research into UWB technology has so far mainly focused on its security applications. I am excited to see our results now being also used in the context of epidemic preparedness," says Srdjan Čapkun, Professor of Computer Science at ETH Zurich.

For its part, the ISI Foundation developed the on-board sensor software as well as the data analysis and visualisation pipeline. With partial support by the CRT Foundation, it leveraged its experience in leading the SocioPatterns collaboration, an international effort that over the last 15 years has achieved some of the largest human contact network measurements using attenuation-based proximity sensors and released open datasets that have been used in more than two thousand scientific papers. "We believe that this technology is a promising technical evolution beyond attenuation-based proximity sensors, and it will afford higher-quality measurements of contact patterns in several environment of interest," says Ciro Cattuto, Scientific Director at the ISI Foundation.

In addition to spearheading the multi-institutional consortium, EPFL has shaped the strategic roadmap for the WPP device, marking its influence in both technological and ethical arenas. EPFL has also contributed key insights into human-computer interface evaluation and plans for future integration of the open DP-3T (Decentralised Privacy-Preserving Proximity Tracing) protocol, which was developed during the COVID-19 pandemic to facilitate digital contact tracing of infected individuals. “When during the pandemic we worked on the contact tracing apps, we often had to constrain our designs to the boundaries allowed by Google and Apple. Having an independent platform such as the WPP will allow us to help in pandemics prevention without intervention from technology giants,” says Carmela Troncoso, Professor and Head of the SPRING Lab at EPFL.


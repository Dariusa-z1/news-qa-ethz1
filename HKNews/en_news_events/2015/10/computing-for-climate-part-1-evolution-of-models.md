# computing-for-climate-part-1-evolution-of-models

## A Question of Resolution

Predicting the weather and – on a larger scale – the climate is a complex process involving current local and global observations that are fed into specialized computer programs, which in turn model the future meteorological conditions. Results from such simulations are not only important for daily weather bulletins, but also provide guidance on climate change in terms of adaptation (how to cope with future climate) and mitigation (how to limit climate change by reducing greenhouse gas emissions).

As early as 1917, the British mathematician and meteorologist Lewis F. Richardson tried to “compute the weather”. Richardson’s compute power consisted of an imagined workforce of 64,000 humans, each of them forming a piece of the first massively parallel “computer”. He designed a complex set of computing forms that served as a simple distributed memory (the “computers” were supposed to enter the numbers in handwriting), and he addressed parallelization, communication and synchronization – key issues of modern climate simulation.

## Developing better Models of Computation

Richardson already used a three-dimensional computational grid mapping the atmosphere to solve a simplified form of the fluid-dynamical equations on a rotating planet; in short, he calculated the weather – and not too differently from how we do today. The first realistic simulations were later conducted in the 1950s using a grid spacing of about 800 km. A major breakthrough was achieved in the late 1970s, when the resolution in global models could be refined to roughly 100 km. This enabled weather forecasts to be extended from one-day to five-day, as for the first time the low and high-pressure systems could be dealt with adequately.

The next challenge now lies ahead of us: at resolutions of around 1 km, it becomes feasible to explicitly represent convective clouds (thunderstorms and rain showers). The dynamics of these fine-scale atmospheric systems is represented using physical laws, rather than semi-empirical approximate methodologies. Nowadays, km-scale simulations are used in operational weather forecasting, and increasingly in climate research. Many studies show that this enables a more appropriate representation of the water cycle including its extreme events, and it is hoped that km-scale resolution will reduce the uncertainties of climate models. Recent results from a European-scale simulation [1] show the value of high resolution and demonstrate these prospects (see figure).

## Further information

These simulations were conducted using the COSMO model [2]. This model is a complex computer program developed in an international effort spanning many decades, with hundreds of contributing researchers. The code runs on high-performance computers and has more than 300 thousand lines of code. It is used by many European weather centres including MeteoSwiss, and by about 200 researchers at numerous universities and climate centres, such as the ETH-based Center for Climate Systems Modelling C2SM .

High-performance computers, also known as supercomputers, push the limits of what we can compute by utilizing specialized processors such as many-core processors and graphics processing units (GPUs). Achieving highest performance on such massively-parallel systems is a major challenge in computer science. Specialization leads to immense savings in cost and energy: for example, by switching to a GPU-based architecture in the Piz Kesch system [3] the Swiss national weather service MeteoSwiss was able to increase the energy efficiency of its operational forecast by a factor of more than three. This machine is now used for day-to-day weather prediction.

## About the author

Yet, efficient programming of heterogeneous machines remains a challenging problem and requires new insights and tools. GPU architectures follow completely different design principles than traditional processors and require the program to expose massive parallelism in a specialized language such as CUDA. This specification is fundamentally different from how we used to write code in the last 30 years. My group, the Scalable Parallel Computing Laboratory SPCL , is developing new techniques to improve the performance further and to program large scale heterogeneous supercomputers in the context of the Platform for Advanced Scientific Computing (PASC) program [4]. PASC is a program to modernize High-Performance Computing (HPC) applications in Switzerland; its results are discussed in the yearly conference of the same name [5].

Torsten Hoefler wrote this blog together with Christoph Schär (ETH Zurich) and Oliver Fuhrer (MeteoSchweiz). In their next post, “ Computing for Climate (part 2) ”, the authors explain how modern climate models work.

[1] Leutwyler, D., O. Fuhrer, X. Lapillonne, D. Lüthi, C. Schär, 2015: Continental-Scale Climate Simulation at Kilometer-Resolution. ETH Zurich online resource. Short description and animation , Climate Science Visuals: Online video .

Assistant Professor for Computer Science, Scalable Parallel Computing Laboratory (SPCL), ETH Zürich


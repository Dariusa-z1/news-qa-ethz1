# computing-for-climate-part-2-how-climate-models-work

**Source:** en_news_events/2015/10/computing-for-climate-part-2-how-climate-models-work.html

## 3D-computational grids

Computer simulations lie at the heart of everyday weather forecast, and they are of great importance when it comes to addressing the challenges of climate change. To understand and predict the behaviour of the climate system, scientists build und use complex computational models. These include the relevant chemical and physical properties of the earth’s surface (land and oceans) and of the atmosphere, in a simplified way. But how do climate models work, and what are the implied challenges for Computer Science?

Similar to the early efforts of Richardson (see the first part of this series), modern climate models span a three-dimensional computational grid over the Earth on which the physical laws governing the evolution of the state of the atmosphere are computed. In each grid cell, values for wind speed, temperature, pressure, relative humidity and concentrations of atmospheric constituents (in particular water vapour, but also other gaseous constituents and aerosols) determine the current state of the atmosphere. The smaller the grid cell, the higher the resolution of the model. Using governing physical laws, a computer program then advances these values forward in time, step-by-step. To update the values in a specific cell, the computer program also requires information from neighbouring cells. Such computer programs are often referred to as stencil code [1]. Since computing time and memory consumption grow linearly with the number of cells, efficient parallel implementations of stencil programs are an important research topic at the Scalable Parallel Computing Laboratory SPCL . An introduction to climate models and a tornado simulation can be found here: [2], [3].

## Keeping Millions of Processors at Work

When implementing a climate and weather code for a large-scale machine like Piz Daint at the Swiss National Supercomputing Centre CSCS , we need to parallelize the stencil program to be executed on millions of processing elements. In collaboration with MeteoSwiss and CSCS, one of my students, Tobias Gysi, has developed a special language that enables simple specification of stencil programs by meteorologists and also enables computer scientists to parallelize and optimize the execution at the same time. This domain-specific language (DSL) enables simple, textbook-like implementations and thus allows a clean separation of concerns between the meteorologist who defines the computational science problem, and the computer scientist who defines the optimizations. Efficient automatic optimization of DSLs to heterogeneous hardware is a huge computer science research task.

Another major challenge in climate research is storing and managing the vast amount of data produced during a single simulation. Parameters such as pressure and velocity are stored for each grid point, at each time step. Predictions indicate that the data volume may reach Exabytes (10 18 bytes, as many as 1,000,000 1 TB hard drives) in the near future. This requires new techniques for data management, generation, and online analysis at extreme scales. These challenges are addressed in a collaboration between MeteoSwiss, CSCS, and ETH, funded through an SNF Sinergia grant [4].

## Modelling Climate Change over the Alps and Europe

Recently a large simulation regarding the European summer climate was completed [5], [4]. The simulation covers 30 years on a computational mesh with 500x500x60 grid points at a horizontal resolution of 2.2 km. To manage the huge data storage associated with this simulation, only little output is stored, but nevertheless the archive includes more than 120 TB. Finalizing these simulations took more than one and a half years on the Monte Rosa (Cray XE5 and XE6) supercomputer at the Swiss National Supercomputing Center CSCS , using a conventional version of the COSMO model.

One of the next targets is to exploit the GPU-enabled COSMO version to carry out similar numerical experiments, but covering the whole of the European continent on a 10 times larger domain (see figure and animation in part 1 of this blog), using a more recent hardware architecture (Cray XC30, Piz Daint) and the GPU-enabled COSMO version [3]. Piz Daint has an astounding peak performance of 6x10 15 Flop/s (floating point operations per second) on a total of 5272 compute nodes. As our current implementation of COSMO-GPU uses only 144 nodes (i.e., 3%), further expansion of the computational domain is a very realistic target.

## Strong Collaboration to drive Climate Science

The purpose of these simulations is to better understand and project the water cycle including extreme heavy precipitation events. Simulations on the Alpine scale have already provided interesting results that would be hard to trust if based on semi-empirical assumptions. They project mean summer precipitation amounts to decrease by about 30 per cent by the end of the century, whereas heavy thunderstorms and rain showers are projected to increase substantially. In other words, the extremes at both ends, i.e., droughts and flash floods, are expected to increase. Information from such experiments is of potential interest for climate change adaptation, since short-term heavy precipitation events are of key importance for water resource management and flood protection.

Predicting weather and climate requires not only strong computers but also strong collaboration between climate and computer science. Utilizing heterogeneous hardware architectures is imperative for modern simulation codes but often requires a fundamentally new approach to software development. The current version of the COSMO model is the only regional weather and climate model available worldwide which can run fully on GPUs. This progress and the emerging prospects have been made possible by close interdisciplinary cooperation between CSCS, MeteoSwiss, C2SM, and the Computer Science and the Environmental Systems Science Department at ETH.

## Further information

Torsten Hoefler wrote this blog together with Christoph Schär (ETH Zurich) and Oliver Fuhrer (MeteoSchweiz).

[2] An introduction to climate models

## About the author

[3] Tornado simulation

[4] crCLIM : Convection-resolving climate modeling on future supercomputing platforms. A Sinergia project funded by the SNF.

[5] Ban N., J. Schmidli and C. Schär, 2015: Heavy precipitation in a changing climate: Does short-term summer precipitation increase faster? Geophys. Res. Lett. , 42 (4), 1165–1172 doi .

[6] Fuhrer, O., C. Osuna, X. Lapillonne, T. Gysi, B. Cumming, M. Bianco, A. Arteaga and T. C. Schulthess, 2014. Towards a performance portable, architecture agnostic implementation strategy for weather and climate models. Supercomputing Frontiers and Innovations, 1 (1), 45-62

Assistant Professor for Computer Science, Scalable Parallel Computing Laboratory (SPCL), ETH Zurich


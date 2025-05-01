# clouds-in-three-dimensions

**Source:** en_news_events/2018/04/clouds-in-three-dimensions.html

## Three-dimensional cloud visualisation

Visualisation plays a huge role in the study of weather data, such as temperature, air pressure and the cloud water content of the atmosphere. Displaying this data graphically is quite natural, since it has clear spatial reference points and is very simple to superimpose on maps.

Two-dimensional representations are currently the standard in meteorology, both in research and for the purposes of weather forecasts. These simple visualisations are adequate in most cases. However, some processes, such as the vertical formation of clouds over time, are difficult to study in two dimensions.

This is why computer graphics specialists in a team led by ETH computer science professor Markus Gross have developed approaches based on numerical weather simulations to visualise the formation and dynamics of clouds and air currents three dimensionally at high resolution.

The researchers presented their work at two international expert conferences. According to Tobias Günther, a senior scientist in Gross’ team, the new 3D visualisation methods were well received by attendees. For his bachelor’s thesis, Noël Rimensberger, supervised by Günther, developed and expanded the methodology and calculated the visualisations on the computer.

## Exploring new possibilities

Rimensberger’s visualisations were based on wind, cloud and rain data made freely available to the scientific community as part of the international IEEE Scientific Visualization Contest. The underlying simulation recreates the weather conditions on the evening of 26 April 2013 and was developed as part of a large-scale meteorology research project called HD(CP)², in which more than 100 researchers from 19 institutions participated.

The computer science student combined existing algorithms to visualise cloud formation and air currents, applying recent methods used in the research field of scientific visualisation.

Rimensberger emphasises that he was less interested in developing viable predictive tools for meteorology than in exploring the possibilities of “representing weather data in a relatively simple, comprehensible way”. The value for science is that the 3D graphics reveal something that is not visible with 2D graphics, and thus provide a better overall picture.

For example, Rimensberger’s visualisations show how clouds form over Germany and change over time, how they are carried upwards by updrafts and then transported by winds in the troposphere more than 10 kilometres above the ground. Cloud zones with an identical water and ice content are shown in different colours.

## Revealing hidden structures

The computer science student also analysed air currents. The lines represent the paths of air parcels, and their colours indicate how much an air parcel rotates around its own axis. The length of the lines provides information on the distance travelled, and thus visualises the flow velocity. Ascending clouds create turbulences that cause stronger vorticity or changes in trajectory. Both can be read from the path lines.

Rimensberger also superimposed the flight paths of passenger aircraft taking off on the cloud formation simulations. “I wanted to find out if and how storm zones affect air traffic,” he says.

The flight paths of planes taking off from Frankfurt, however, cross right through the simulated thunderstorm cells. Only one plane, taking off from Munich, just avoids a rain cell over Regensburg. Rimensberger concludes that the storms were not strong enough to warrant rerouting air traffic or that too little measurement data was available.

The new visualisations simplify the classification of cloud formations as they can “reveal” clouds that are unobservable from satellites above or from the ground. A comparison with today’s conventional 2D categorisation showed that the new algorithms can also reveal stacked cloud structures.

## Reference

“The scientific value of our visualisation lies in the fact that we make something visible that was impossible to see with the existing tools,” says Rimensberger. It is not quite ready for real-time simulations, however. Complex graphics like those of the air currents across all Germany, for example, have not yet become conventional practice. “The calculations required for this are still too slow. We are trying to improve this with better algorithms,” adds Günther. “But it would be possible to integrate some of the visualisations or, for instance, cloud classifications into existing tools now.”

For air traffic control, the visualisation of regions of turbulence or regions with strong updrafts and storm development could also be of interest.

Follow-up projects are planned or already in progress, such as the interactive analysis of large meteorological datasets. The computer graphics specialists are also working to make key structures in this data more visible and speeding up the complex visualisations of air currents. And who knows, perhaps one day the TV weather presenter will point at 3D weather maps based on ETH’s algorithms.

Rimensberger N, Gross M, Günther T: Visualization of Clouds and Atmospheric Air Flows. IEEE Scientific Visualization (SciVis 2016), Phoenix, AZ, USA, October 1-5, 2017. DOI: 10.3929/ethz-b-000237747


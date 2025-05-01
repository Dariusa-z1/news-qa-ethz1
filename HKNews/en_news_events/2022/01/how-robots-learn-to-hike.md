# how-robots-learn-to-hike

**Source:** en_news_events/2022/01/how-robots-learn-to-hike.html

## Perceiving the environment accurately

Steep sections on slippery ground, high steps, scree and forest trails full of roots: the path up the 1,098-metre-high Mount Etzel at the southern end of Lake Zurich is peppered with numerous obstacles. But ANYmal, the quadrupedal robot from the Robotic Systems Lab at ETH Zurich, overcomes the 120 vertical metres effortlessly in a 31-minute hike. That’s 4 minutes faster than the estimated duration for human hikers – and with no falls or missteps.

This is made possible by a new control technology, which researchers at ETH Zurich led by robotics professor Marco Hutter recently presented in the journal Science Robotics . “The robot has learned to combine visual perception of its environment with proprioception – its sense of touch – based on direct leg contact. This allows it to tackle rough terrain faster, more efficiently and, above all, more robustly,” Hutter says. In the future, ANYmal can be used anywhere that is too dangerous for humans or too impassable for other robots.

## A virtual training camp

To navigate difficult terrain, humans and animals quite automatically combine the visual perception of their environment with the proprioception of their legs and hands. This allows them to easily handle slippery or soft ground and move around with confidence, even when visibility is low. Until now, legged robots have been able to do this only to a limited extent.

“The reason is that the information about the immediate environment recorded by laser sensors and cameras is often incomplete and ambiguous,” explains Takahiro Miki, a doctoral student in Hutter’s group and lead author of the study. For example, tall grass, shallow puddles or snow appear as insurmountable obstacles or are partially invisible, even though the robot could actually traverse them. In addition, the robot’s view can be obscured in the field by difficult lighting conditions, dust or fog.

## Use under extreme conditions

“That’s why robots like ANYmal have to be able to decide for themselves when to trust the visual perception of their environment and move forward briskly, and when it is better to proceed cautiously and with small steps,” Miki says. “And that’s the big challenge.”

Thanks to a new controller based on a neural network, the legged robot ANYmal, which was developed by ETH Zurich researchers and commercialized by the ETH spin-off ANYbotics , is now able to combine external and proprioceptive perception for the first time. Before the robot could put its capabilities to the test in the real world, the scientists exposed the system to numerous obstacles and sources of error in a virtual training camp. This let the network learn the ideal way for the robot to overcome obstacles, as well as when it can rely on environmental data – and when it would do better to ignore that data.

## Reference

“With this training, the robot is able to master the most difficult natural terrain without having seen it before,” says ETH Zurich Professor Hutter. This works even if the sensor data on the immediate environment is ambiguous or vague. ANYmal then plays it safe and relies on its proprioception. According to Hutter, this allows the robot to combine the best of both worlds: the speed and efficiency of external sensing and the safety of proprioceptive sensing.

Whether after an earthquake, after a nuclear disaster, or during a forest fire, robots like ANYmal can be used primarily wherever it is too dangerous for humans and where other robots cannot cope with the difficult terrain.

In September of last year, ANYmal was able to demonstrate just how well the new control technology works at the DARPA Subterranean Challenge , the world’s best-known robotics competition. The ETH Zurich robot automatically and quickly overcame numerous obstacles and difficult terrain while autonomously exploring an underground system of narrow tunnels, caves, and urban infrastructure. This was a major part of why the ETH Zurich researchers, as part of the CERBERUS team, took first place with a prize of 2 million dollars.

Miki T, Lee J, Hwangbo J, Wellhausen L: Learning robust perceptive locomotion for quadrupedal robots in the wild, Science Robotics 2022, doi: 10.1126/scirobotics.abk2822


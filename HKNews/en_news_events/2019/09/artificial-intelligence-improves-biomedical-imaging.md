# artificial-intelligence-improves-biomedical-imaging

**Source:** en_news_events/2019/09/artificial-intelligence-improves-biomedical-imaging.html

## Correcting for image distortions

Scientists at ETH Zurich and the University of Zurich have used machine learning methods to improve optoacoustic imaging. This relatively young medical imaging technique can be used for applications such as visualizing blood vessels, studying brain activity, characterizing skin lesions and diagnosing breast cancer. However, quality of the rendered images is very dependent on the number and distribution of sensors used by the device: the more of them, the better the image quality. The new approach developed by the ETH researchers allows for substantial reduction of the number of sensors without giving up on the resulting image quality. This makes it possible to reduce the device cost, increase imaging speed or improve diagnosis.

Optoacoustics (see box) is similar in some respects to ultrasound imaging. In the latter, a probe sends ultrasonic waves into the body, which are reflected by the tissue. Sensors in the probe detect the returning sound waves and a picture of the inside of the body is subsequently generated. In optoacoustic imaging, very short laser pulses are instead sent into the tissue, where they are absorbed and converted into ultrasonic waves. Similarly to ultrasound imaging, the waves are detected and converted into images.

The team led by Daniel Razansky, Professor of Biomedical Imaging at the University of Zurich and ETH Zurich, searched for a way to enhance image quality of low-cost optoacoustic devices that possess only a small number of ultrasonic sensors.

## Correcting for image distortions

To do this, they started off by using a self-developed high-end optoacoustic scanner having 512 sensors, which delivered superior-quality images. They had these pictures analysed by an artificial neural network, which was able to learn the features of the high-quality images.

Next, the researchers discarded the majority of the sensors, so that only 128 or 32 sensors remained, with a detrimental effect on the image quality. Due to the lack of data, distortions known as streak type artefacts appeared in the images. It turned out, however, that the previously trained neural network was able to largely correct for these distortions, thus bringing the image quality closer to the measurements obtained with all the 512 sensors.

Scientists at ETH Zurich and the University of Zurich have used machine learning methods to improve optoacoustic imaging. This relatively young medical imaging technique can be used for applications such as visualizing blood vessels, studying brain activity, characterizing skin lesions and diagnosing breast cancer. However, quality of the rendered images is very dependent on the number and distribution of sensors used by the device: the more of them, the better the image quality. The new approach developed by the ETH researchers allows for substantial reduction of the number of sensors without giving up on the resulting image quality. This makes it possible to reduce the device cost, increase imaging speed or improve diagnosis.

## Facilitating clinical decision making

Optoacoustics (see box) is similar in some respects to ultrasound imaging. In the latter, a probe sends ultrasonic waves into the body, which are reflected by the tissue. Sensors in the probe detect the returning sound waves and a picture of the inside of the body is subsequently generated. In optoacoustic imaging, very short laser pulses are instead sent into the tissue, where they are absorbed and converted into ultrasonic waves. Similarly to ultrasound imaging, the waves are detected and converted into images.

The team led by Daniel Razansky, Professor of Biomedical Imaging at the University of Zurich and ETH Zurich, searched for a way to enhance image quality of low-cost optoacoustic devices that possess only a small number of ultrasonic sensors.

To do this, they started off by using a self-developed high-end optoacoustic scanner having 512 sensors, which delivered superior-quality images. They had these pictures analysed by an artificial neural network, which was able to learn the features of the high-quality images.

## Revealing tissue function

Next, the researchers discarded the majority of the sensors, so that only 128 or 32 sensors remained, with a detrimental effect on the image quality. Due to the lack of data, distortions known as streak type artefacts appeared in the images. It turned out, however, that the previously trained neural network was able to largely correct for these distortions, thus bringing the image quality closer to the measurements obtained with all the 512 sensors.

In optoacoustics, the image quality increases not only with the number of sensors used, but also when the information is captured from as many directions as possible: the larger the sector in which the sensors are arranged around the object, the better the quality. The developed machine learning algorithm was also successful in improving quality of images that were recorded from just a narrowly circumscribed sector. “This is particularly important for clinical applications, as the laser pulses cannot penetrate the entire human body, hence the imaged region is normally only accessible from one direction,” according to Razansky.

The scientists stress that their approach is not limited to optoacoustic imaging. Because the method operates on the reconstructed images, not the raw recorded data, it is also applicable to other imaging techniques. “You can basically use the same methodology to produce high-quality images from any sort of sparse data,” Razansky says. He explains that physicians are often confronted with the challenge of interpreting poor quality images from patients. “We show that such images can be improved with AI methods, making it easier to attain more accurate diagnosis.”

## Reference

For Razansky, this research work is a good example of what existing methods of artificial intelligence can be used for. “Many people think that AI could replace human intelligence. This is probably exaggerated, at least for the currently available AI technology,” he says. “It can’t replace human creativity, yet may release us from some laborious, repetitive tasks.”

In their current research, the scientists used an optoacoustic tomography device customised for small animals, and trained the machine learning algorithms with images from mice. The next step will be to apply the method to optoacoustic images from human patients, Razansky says.

Unlike optoacoustics (also known as photoacoustics), many imaging techniques, such as ultrasound, X-ray or MRI, are mainly suitable for visualizing anatomical alterations in the body. To receive additional functional information, for instance concerning blood flow or metabolic changes, the patient has to be administered contrast agents or radioactive tracers before the imaging. In contrast, the optoacoustic method can visualize functional and molecular information without introducing contrast agents. One example is local changes in tissue oxygenation – an important landmark of cancer that can be used for early diagnosis. Lipid content in blood vessels is yet another potential disease marker, which can aid an early detection of cardiovascular diseases.

It should be noted, however, that because the light waves used in optoacoustic imaging, unlike other waves, do not fully penetrate the human body, the method is only suitable for investigating tissues to a depth of a few centimetres beneath the skin.

Davoudi N, Deán-Ben XL, Razansky D: Deep learning optoacoustic tomography with sparse data, Nature Machine Intelligence, 16 September 2019, doi: 10.1038/s42256-019-0095-3


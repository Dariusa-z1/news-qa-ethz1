# one-step-closer-to-lifelike-avatars

**Source:** en_news_events/2022/01/one-step-closer-to-lifelike-avatars.html

**Date processed:** 2025-05-01

## Main article

These days, people stare at their screens ever more frequently – especially since the onset of the coronavirus pandemic. Conferences, meetings and discussions with work colleagues all take place via video call. If the big tech companies have their way, such encounters will become an immersive experience in the so-called metaverse as early as next year, thanks to 3D glasses and specialised computer programs.

The key to permitting a natural user experience in VR and AR applications is to create what are known as avatars, which are computer-generated, dynamic representations of people. The more realistic the avatars’ appearance and behaviour, the more likely it is that people will gain a sense of real social interaction.

However, modelling a human being in detail and in motion is a task that continues to challenge the developers of these applications. Today’s graphics programs can already create photorealistic, static avatars. But to animate a smiling face, say, graphic designers have to manually edit almost every single image on the computer to correct nuances such as wrinkles and shadows.

Researchers led by Otmar Hilliges, Professor of Computer Science at ETH Zurich, showed how to do this more easily at the International Conference on Computer Vision in October 2021. Instead of modelling every last detail, they use intelligent algorithms that learn to automatically render animated avatars in every conceivable pose by observing 3D images of humans in just a few poses.

## Computer model can even handle handsprings

Computer programs that use artificial intelligence to create lifelike virtual humans have existed only for a few years. These programs learn to realistically depict different body positions using 3D scans of a real person, which are recorded beforehand using a complex camera system.

The AI algorithms process the scans by measuring countless points inside and outside the person’s body to define its contours as a mathematical function. In this way, the algorithms build a template shape of the person. To move the avatar to new poses, the algorithms learn to memorize the path from the moving pose back to the template.

However, for extreme poses outside the known repertoire of movements, such algorithms do not have the knowledge and predict wrong paths, leading to clearly visible artifacts: the arms might be detached from the body or the joints located in the wrong place. This is why today’s models are trained on as many different poses as possible – which entails a huge effort for 3D scanning and requires enormous computing power.

To date, AI avatars are hardly applicable, especially for interactive applications. “It’s impractical to capture the entire possible repertoire of movements,” says Xu Chen, a doctoral student and lead author of the study.

## Any number of new faces from just one image

The new method Chen has developed takes the opposite approach: the model computes the path from the template to the moving poses. Since this means the calculations always have the same starting point, it lets the intelligent algorithms learn better how to generalise movements.

Indeed, for the first time, it puts such a computer model in a position to easily represent new motion patterns as well. It can even produce acrobatic movements such as a somersault or a back bridge.

The new full-body avatars can’t yet be personalised; the representations are limited to the person scanned in the original 3D images. Chen and his colleagues would like to further develop their computer model so that it can create new identities at will.

Marcel Bühler, another doctoral student in Hillige’s group, has already found a solution for personalising avatar faces and changing them as desired. Like Chen in his full-body models, Bühler used intelligent algorithms to create new animated faces from a combination of a 3D face model and a large collection of portrait photos.

## A close look can unmask deepfakes

While previous computer programs already provided good animations of faces from the front, Bühler’s model can also realistically represent faces from the side as well as from above and below.

Is there a danger that the new technology will soon allow even more realistic deepfake videos to circulate, for example to fake a speech by an important politician? “Deepfake videos are still far from perfect,” Bühler says. Most computer programs, he points out, achieve good results only for a particular setting. For example, the new face model can’t yet realistically represent details such as hair.

“Anyone who looks closely will still find artifacts,” Bühler says. He thinks it is more important to keep the public informed and aware of the current state of affairs. Making the research on 3D rendering techniques, as well as their vulnerabilities, publicly available could help cybersecurity experts more easily detect deepfake videos on the web, he adds.

For interactive virtual reality applications, the work of these ETH researchers represents enormous progress. It’s quite possible that tech companies like Facebook and Microsoft will implement the two doctoral students’ newly developed techniques in their avatars.

## Reference

Chen X, Zheng Y, Black M, Hilliges O, Geiger A. SNARF: Differentiable Forward Skinning for Animating Non-Rigid Neural Implicit Shapes . International Conference on Computer Vision (ICCV), published online on October 11th, 2021.

Bühler M, Meka A, Li G, Beeler T, Hilliges O. VariTex: Variational Neural Face Textures . International Conference on Computer Vision (ICCV), published online on October 11th, 2021.


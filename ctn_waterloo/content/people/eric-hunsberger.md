name: Eric Hunsberger
email: ehunsber@uwaterloo.ca
one_liner: Vision
group: Grad students
title: PhD student
picture: static/img/placeholder.png

Just prior to the Mayan apocalypse,
I transferred from the Master's program into the PhD program
to continue my research
with Chris Eliasmith and Jeff Orchard (my co-supervisors)
on the human visual system.

For my PhD research, I will focus on the problem of depth-from-motion,
which describes how people can infer the depth of objects in the environment
from how these objects move relative to one another.
A simple example is how, as you walk through a room,
objects close to you will move quickly in your visual field
and objects far away will remain mostly stationary.
To infer depth information from motion,
your visual system first determines the motion
of objects in the incoming visual stimulus;
this is called optical flow.
Optical flow, along with other information that your brain
gets from your vestibular (inner ear) and proprioceptive (muscular) systems,
is used by your brain to infer your motion in the environment.
Your brain can then combine your motion and the motion of the objects
around you to infer the depth of those objects.

I plan to model this process from start to finish.
My model will ultimately run in simulated spiking neurons,
meaning that the model is constrained to use the same tools as the brain.
By constraining the model like this,
I will be able to select between the many various algorithms
for performing optical flow and depth-from-motion,
since any algorithm I choose must be implementable in neurons.
Neurons are very flexible computational devices,
but are better suited to some types of computations than others,
a distinction which helps greatly in choosing between algorithms.
Ultimately, if and when the model runs in spiking neurons,
it will demonstrate not necessarily *the* way that the brain performs
depth-from motion, but will present *a* way that the brain *could*
perform depth-from-motion.
Ideally, the model will make both behavioural and neuroscientific
predictions that can be tested to help validate the model.

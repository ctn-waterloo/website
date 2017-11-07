name: Eric Hunsberger
email: ehunsber@uwaterloo.ca
one_liner: Vision
group: Grad students
title: PhD candidate
picture: http://compneuro.uwaterloo.ca/files/people/eric-hunsberger.jpg

I am a PhD candidate with Chris Eliasmith and Jeff Orchard (CS).
I want to understand how the human visual system works,
with a specific focus on the problem of object recognition.

The visual system uses deep hierarchical layers of neurons
to generate representations of the visual field.
As we move into the deeper layers,
these representations progressively become
more invariant to transformations like translation, rotation, and lighting.
They also become more selective to properties of specific objects.
For example, an early visual neuron may detect edges,
and will become active for an edge of the right orientation and thickness
no matter what type of object this edge belongs to.
In the middle layers, a neuron might be sensitive to the "ownership" of the edge,
that is, it only becomes active if the edge belongs to a foreground object.
In the later layers, neurons are much more selective to specific categories of objects.
This is not a one-to-one mapping, however,
but rather a distributed representation,
with each neuron being selective to a number of different categories of objects.

I attempt to model this process using a combination of computational neuroscience
and machine learning techniques.
Deep artificial neural networks have recently been quite successful
at allowing computers to recognize complex objects.
These networks are called "artificial" because
they lack most of the biological details present
in the brains of humans and other animals.
My work brings more biological constraints into these models.
Biological neurons communicate using spikes---
sudden bursts of electricity that cause a neuron to release neurotransmitter,
which then creates electrical currents in other neurons.
My models run using simulated spiking neurons
that model real neuron behaviour much more accurately
than the non-spiking and overly-simplistic idea of a neuron used in
artificial neural networks.
Not only does this help us to better understand
how these networks function in the brain,
it allows them to be implemented on specialized computer hardware
for simulating spiking neural networks.
This hardware---called neuromorphic hardware---
is much more energy-efficient than traditional computer chips.
This will allow these algorithms to be implemented on devices
with limited power availability,
such as cell phones or mobile robots.

Another aspect of my work looks at learning in the brain.
Artificial neural networks are trained on large sets of images,
similar to how a baby or young child
learns to see the world by being exposed
to many different types of visual stimuli.
But artificial neural networks use a number of tricks and "cheats",
methods for training that work well on a computer,
but that would not work in a biological system like the brain.
To address this, I am examining alternative learning algorithms
that the brain *would* be able to implement.
These models will help us to better understand how we learn,
and the large number of neural processes
that are happening in our brain to facilitate this learning.
They may also help to bring some ideas from our brains back to computers,
to help computers learn to perform a variety of tasks
more quickly and accurately.
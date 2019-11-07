title: Representing Time and Space
author: Brent Komer
date: 2019-07-01 17:00

Lots of exciting new research to share!

First up, computing functions across time in a spiking neural network.
[Aaron](/people/aaron-r-voelker.html) has developed a way to represent windows of history in a population of spiking neurons, which allows the computations of accurate delays and higher-order synapses while maintaining desired lower level properties.
This work also gives a novel explanation of time cells found in a variety of tasks involving delays.
Check out the first paper [here](/publications/voelker2018.html)!

Since this inaugural publication, the network structure that provides this window of history representation has been named a Legendre Memory Unit (LMU).

Beyond modelling biological neural systems, LMUs have proven to be a useful in the world of Deep Learning as a memory cell for Recurrent Neural Networks (RNN).
A recent paper accepted to NeurIPS compares LMUs to the commonly used LSTM and shows significant improvement across a variety of tasks.
The full paper can be found [here](/publications/voelker2019lmu.html).


Another recent area of work focusses on representations of space.
A common way to represent a discrete position in a Semantic Pointer is to bind a displacement vector with itself some number of times to indicate its order in a sequence.
This notion of self-binding can be extended to inlucde fractional binding, allowing representations of continuous space with semantic pointers.
Vectors constructed in this manner for use in the SPA are called Spatial Semantic Pointers (SSP).

This representation allows many spatial operations to be performed efficiently in a spiking neuron network, including representing the location of collections of objects, performing spatial queries on a memory, and shifting the locations of objects in memory.
The first papers describing SSPs and their applications were presented at CogSci this year by [Brent](/publications/komer2019.html) and [Thomas](/publications/lu2019.html).

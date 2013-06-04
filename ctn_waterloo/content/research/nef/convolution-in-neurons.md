title: Convolution in neurons

The following video shows the neural activity of a network that combines two
25-dimensional vectors into a single new 25-dimensional vector using the
circular convolution. This operation is the basis of our approach to
conceptual combination (binding symbols together). The resulting vector acts
as a new symbol, with the added property that it can be broken down into the
original components if needed. The two original vectors are represented by the
two left-hand groups of neurons (1600 neurons each). The far left shows a
pictorial version of the vector, but these vectors could be images, sounds,
somatosensory data, or anything else that could be represented using a vector.
The far right show a pictorial version of the resulting convolved vector. The
shading of the neurons indicates their membrane voltage. When a neuron reaches
its firing threshold (pure black), it spikes (yellow), sending current to any
neurons it is connected to. The two neural groups on the left both have
connections to an intermediate group of neurons (not shown). This intermediate
group consists of 6400 neurons. These neurons then connect to the neural group
shown on the right. After one minute in the video (0.1 seconds of simulated
time), we change the input to the top group of neurons. The system now
performs the convolution using this new vector. Importantly, synaptic
connection weights are not changed in any way. This demonstrates that this
system can convolve any two given vectors, rather than requiring special
dedicated synaptic connections for each possible combination. After two
minutes (0.2 seconds of simulated time), the input to the bottom group is also
changed.

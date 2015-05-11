title: Demonstration Videos

A collection of videos for demonstrating aspects of the Neural Engineering
Framework. See also our
[Nengo tutorial videos and Spaun demonstrations](http://nengo.ca/videos)

### Fly through of several models

<iframe width="100%" height="400" src="https://www.youtube.com/embed/q4jxI26gUtA" frameborder="0" allowfullscreen></iframe>

This video was used at our NIPS demo display.

### Multidimensional representation

<iframe width="100%" height="400" src="https://www.youtube.com/embed/bVLu_V0deC0" frameborder="0" allowfullscreen></iframe>

What does it look like to represent a high-dimensional vector using neurons?
Here is a video of 2500 neurons representing a 25-dimensional vector. The
vector is shown as an image at the top of the screen, but the vector being
represented does not need to be an image. The shading of the neurons indicates
their membrane voltage: the start white, then become darker as the voltage
builds up. Eventually, they fire (yellow), resetting their voltage back to the
beginning. We have organized the neurons so that ones with similar preferred
direction vectors are near each other.

### Oscillators

<iframe width="100%" height="400" src="https://www.youtube.com/embed/GAg2-EpPlvI" frameborder="0" allowfullscreen></iframe>

Several different 2-dimensional neural oscillators running in
Nengo. The recurrent connections implement a simple, square, and
controlled oscillator.

### Convolution in neurons

<iframe width="100%" height="400" src="https://www.youtube.com/embed/bbdz-TGepMM" frameborder="0" allowfullscreen></iframe>

This video shows the neural activity of a network that combines two
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

### Neural Production System

<iframe width="100%" height="400" src="https://www.youtube.com/embed/jVWrGEmQJlo" frameborder="0" allowfullscreen></iframe>

Part of our ongoing research involves implementing symbolic rule-following in
neurons. This would form a neural implementation of a production system, which
is a common component of many cognitive architectures. For a full paper on
this model, see [here](http://compneuro.uwaterloo.ca/files/publications/stewart.2009b.pdf).

In this demonstration, the large neural group represents
the current state (the buffers in ACT-R terms). The five neural groups below
it represent five different productions. Each production has a particular
state it should be applied in. When this state occurs, these neurons begin to
fire. When the neurons fire, they in turn affect the buffer state, changing
it. These five productions are configured to each change the state in a cycle:
p1$\rightarrow$p2$\rightarrow$p3$\rightarrow$p4$\rightarrow$p5$\rightarrow$p1$\rightarrow$etc. The only external input to this model is an
initial current to set the buffer to initially hold the first state. After
that, all changes are due to the synaptic connections between the shown
neurons. The synaptic connections are simulated GABAA connections, which have
a synaptic time constant of ~10ms. It is this timing which governs the speed
of the cycling between states. In this model, the average time to transition
between states is 46.6ms, very close to the 50ms generally assumed.

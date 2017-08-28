title: SYDE 556 Possible Projects

The purpose of these projects is to have you apply what you learn in the
course to constructing a novel simulation of some neural system. 
The topics listed here and on the Nengo modelling page
are not exclusive, feel free to propose your own topic.

The project is worth 40% of your final mark. People in 556 can do a either an 
"extension project" or a "research project", those in 750 must do a "research project."

Another excellent source (other than below) for ideas is the [Nengo Modelling Ideas repository](https://github.com/ctn-waterloo/modelling_ideas).  This repository has a bunch of advanced and simple modelling suggestions.  You can
use Nengo for your final project, so they are all doable.  However, be sure to talk to me before starting, as some
are not especially relevant for the course.

## Expectations

There are two main things needed for the project:

1. build a simulation of a neurobiological system
2. evaluate its behaviour

You will produce a written report on your system using the steps outlined in chapter 1 of the book. This should be 10-20 pages, with lots of diagrams, graphs, and code.

To evaluate the behaviour of the system, the idea is to vary some aspect of the model and see how that affects its behaviour. To do this, you must:

1. Define some measurable aspect of the system's behaviour (e.g. accuracy of representation, or number of errors, or speed of response); and
2. Change an aspect of the model (e.g. number of neurons, or neuron model, or maximum firing rates, or post-synaptic time constants, etc., etc.), and see how that affects the measurement. 

Note that because there is randomness in the creation of a neuron model, you will generally have to measure a model multiple times.

## Example Extension Projects 

1. ([Dora Angelaki](http://thalamus.wustl.edu/Neuroweb/angelaki.htm)): Dora contributed the data for the model of the vestibular system found in the textbook. This model could be used as a starting point for a project. Because there are many possible implementations of this network, it would be useful to implement the transformation in a few different ways and see if there are predictions that could determine which of the models is most like the real network. Or, an indepth examination of the derivative signal, $\dot{A}(t)$, could be undertaken, with attempts to design networks that can compute a derivative effectively. Right now, this signal is not part of the neural model. Or constructing a model that includes both tVOR and regular VOR. Or...
2. Lamprey swimming: The model of lamprey swimming in the textbook could be extended in two ways: 1) make the model 3-dimensional; 2) include control signals for yaw, roll, and pitch.
3. Statistical inference: more compex distributions, multiple steps in inference, temporal inference for slowly changing statistics, higher-dimensional representations could all be explored.
4. Working memory: The model of working memory in the text is for parietal areas. A similar model could be construct for frontal working memory. More sophisticated representations than that used here could be implemented in a similar model. For instance, ramping function representation (i.e. function representations with temporal dynamics), or just higher-d functions than are used in the book. As well, additional working memory functions, like 'loading' a new memory, or 'erasing' an old memory could be examined.

## Example Research Projects

1. (Pieter Medendorp, was at [Doug Crawford's lab](http://www.yorku.ca/jdc/)): Developing a simulation of how visual information is updated for eye and head motion, including how perceptual representations are transformed. Pieter and others have derived a simple set of differential equations to describe this updating. However, they do not have a neural level model of the circuit.
2. ([James Danckert](http://watarts.uwaterloo.ca/~jdancker/)): James' research focusses on parietal control of movement and lesions to these areas (resulting in hemineglect, for instance). Here are some questions he is interested in: How does the right inferior parietal cortex contribute to the spatial control of movements of either limb and how do left and right parietal cortices interact in movement control? Given that superior parietal lesions lead to unilateral motor deficits how do the right inferior and superior parietal regions communicate? Can modeling help disentangle the functional contributions of the superior temporal gyrus and inferior parietal cortex? Where in the brain is prism adaptation having its primary effect?
3. Statistical inference: Higher-D repn; gaussian and non-gaussian estimates (Tennenbaum); implementing empirical bayes net (Karl Friston), modeling non-stationary signals, motor control (Dan Wolpert).
5. Kalman filter: The Kalman filter (as discussed at the end of the book) has been proposed as a means of explaining the function of the hippocampus as well as visual areas. A neurally plausible implementation of this filter could have important consequences for our understanding of visual processing (for instance).
7. Symbolic processing: There are good ways to implement symbolic processing using distributed representations. Specifically, tensor product and holographically reduced representations can be used to explain binding, and various logical operations. Looking at novel applications is usually pretty interesting.

## Extended Example

To give an idea of what the process is like for doing this sort of project, let's consider this paper ([Flexible control of mutual inhibition: a neural model of two-interval discrimination](http://www.sciencemag.org/content/307/5712/1121.long), Science, 2005).

Task: hear a tone, remember it, hear another tone, respond as to which of the two was higher pitch

![Comparison image](http://imgur.com/lKZiCLT.png)

Their model:

![Comparison model](http://imgur.com/use1fQO.png)

Their model's data:

![Model data](http://imgur.com/3Q7sI0A.png)

Our approach:

- System Description:
 - Sensory area stores ss, the current stimulus
 - PFC stores dd, the difference between the two stimuli (before the second stimulus is shown, it just stores the first stimulus)
 - Some other area stores xx, whether we're on the first (x=1x=1) or second (x=−1x=−1) sound
 - Connection from Sensory to PFC is d=s∗xd=s∗x
 - Connection from PFC to PFC is the identity function (to store information over time)
- Design Specification:
 - All the neural details from the paper (firing rates, distributions of tuning)
 - Note that what they call S+S+ and S−S− are just two different encoders
- They vary noise and see what happens
 - more errors when tones are close to each other
 - also vary connection weights (decreasing and increasing excitation and inhibition)
- Other things we could do
 - how could we deal with tones of different lengths?
 - higher dimensional input (frequency and volume), with different questions being asked
 - different sensory systems using the same comparison system?
- Now that we've done this translation, this model could be used by someone in the class as an extension project, not a research project



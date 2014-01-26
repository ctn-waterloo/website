title: SYDE 556 Possible Projects

The purpose of these projects is to have you apply what you learn in the
course to constructing a novel simulation of some neural system. As you can
see below, there are a wide range of topics. I encourage you to contact an
experimentalists, who can help you by guiding you to relevant neural data.
Some of the topics below have specific people associated with them. For those
that don't I will do my best to find a mentor. Also, the topics listed below
are not exclusive, feel free to propose your own topic.

The project is worth 40% of your final mark. For undergraduates only, the 556
project can be done in groups of 2 (let me know if you are going to work in a
group). People in 556 can do a either an "extension project" or a "research
project", those in 750 must do a "research project."

## Extension Projects

1. Eye control (NPH): 2D vector control instead of the 1D control described in the book. Even better, 3D (i.e. pitch, yaw, rotation).
2. Statistical inference: more compex distributions, multiple steps in inference, temporal inference for slowly changing statistics, higher-dimensional representations.
3. ([Dora Angelaki](http://thalamus.wustl.edu/Neuroweb/angelaki.htm)): Dora contributed the data for the model of the vestibular system found in the textbook. This model could be used as a starting point for a project. Because there are many possible implementations of this network, it would be useful to implement the transformation in a few different ways and see if there are predictions that could determine which of the models is most like the real network. Or, an indepth examination of the derivative signal, $\dot{A}(t)$, could be undertaken. Right now, this signal is not part of the neural model. Or constructing a model that includes both tVOR and regular VOR. Or something similar?
4. Lamprey swimming: The model of lamprey swimming in the textbook could be extended in two ways: 1) make the model 3-dimensional; 2) include control signals for yaw, roll, and pitch.
5. Working memory: The model of working memory in the text is for parietal areas. A similar model could be construct for frontal working memory. More sophisticated representations than that used here could be implemented in a similar model. For instance, ramping function representation (i.e. function representations with temporal dynamics), or just higher-d functions than are used in the book.

## Research Projects

1. (Pieter Medendorp, was at [Doug Crawford's lab](http://www.yorku.ca/jdc/)): Developing a simulation of how visual information is updated for eye and head motion, including how perceptual representations are transformed. Pieter and others have derived a simple set of differential equations to describe this updating. However, they do not have a neural level model of the circuit.
2. ([James Danckert](http://watarts.uwaterloo.ca/~jdancker/)): James' research focusses on parietal control of movement and lesions to these areas (resulting in hemineglect, for instance). Here are some questions he is interested in: How does the right inferior parietal cortex contribute to the spatial control of movements of either limb and how do left and right parietal cortices interact in movement control? Given that superior parietal lesions lead to unilateral motor deficits how do the right inferior and superior parietal regions communicate? Can modeling help disentangle the functional contributions of the superior temporal gyrus and inferior parietal cortex? Where in the brain is prism adaptation having its primary effect?
3. Statistical inference: Higher-D repn; gaussian and non-gaussian estimates (Tennenbaum); implementing empirical bayes net (Karl Friston), modeling non-stationary signals, motor control (Dan Wolpert).
4. ([Colin Ellard](http://www.arts.uwaterloo.ca/~cellard/)): Colin's interest deal with prey-predator interactions, especially predator recognition and avoidance. More generally, he is interested in visually-guided navigation (especially neural mechanisms involved in computing time-to-collision).
5. Kalman filter: The Kalman filter (as discussed at the end of the book) has been proposed as a means of explaining the function of the hippocampus as well as visual areas. A neurally plausible implementation of this filter could have important consequences for our understanding of visual processing (for instance). Such an implementation has not yet been done (e.g., as model of rat location or as model of visual input)
6. ([David Reddish](http://www.neurosci.umn.edu/faculty/redish.html)) Hippocampus/head-direction: The head direction system found in the hippocampus has often been modeled as a ring attractor (much like working memory). However, the details of the neural responses in hippocampus reveal more subtle changes in the response functions than a ring attractor allows. David Reddish has a lot of experience modeling this area and these subtleties.
7. Symbolic processing: There are good ways to implement symbolic processing using distributed representations. Specifically, tensor product and holographically reduced representations can be used to explain binding, and various logical operations. However, we have only recently implemented this, looking at novel applications would be quite interesting.

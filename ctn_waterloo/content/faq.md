title: Frequently asked questions

After the release of our [paper about Spaun](/publications/eliasmith2012.html)
in the journal Science, we hosted an
[Ask Me Anything thread](http://www.reddit.com/r/IAmA/comments/147gqm/we_are_the_computational_neuroscientists_behind/)
on reddit. We got a lot of great questions,
the most common of which we have archived on this page.

* * *

#### Basic summary of the model:

Xuan: Spaun is comprised of different modules (parts of the brain if you
will), that do different things. There is a vision module, a motor
module, memory, and a decision making module.

The basic run-down of how it works is: It gets visual input, processes
said visual input, and based on the visual input, decides what to do
with it. It could put it in memory, or change it in some way, or move
the information from one part of the brain to another, and so forth. By
following a set of appropriate actions it can answer basic tasks: e.g. -
get visual input - store in memory - take item in memory, add 1, put
back in memory - do this 3 times - send memory to output.

The cool thing about Spaun is that it is simulated entirely with spiking
neurons, the basic processing units in the brain.

You can find a picture of the high-level architecture of
Spaun[ ](http://nengo.ca/build-a-brain)[here](http://nengo.ca/build-a-brain).

The stuff in the memory modules of spaun are points in a high
dimensional space. If you think about a point on a 2D plane, then on a
3D plane. Now extend that to a 512D hyperspace. It's hard to imagine.

Terry: "Functional" here means that it does tasks. There are eight
different tasks (memorizing lists, adding digits, completing a pattern,
etc) and we can tell it different tasks to do by showing it different
visual stimuli. It takes in visual input, routes it to the relevant
brain areas, combines results, and produces motor responses, all using
spiking neurons. Projects like IBM Synapse and Blue Brain are definitely
working in that direction, but they're generally starting with doing one
particular brain component in great detail, rather than our approach of
doing less-detailed models of many brain areas, and then connecting them
all together.

#### What is your hardware/software setup?

Xuan: The core simulation code is in Java. Done so mainly for
cross-compatibility between different operating systems. The model
itself is coded in Python (because Python is so much easier to write),
and all it does it hook into the Java code and construct the model that
way.

To simulate Spaun, we used both an in-house GPU server, as well as the
supercomputing resource that we have available in Ontario,
Canada.[ ](https://www.sharcnet.ca/my/front/)[Sharcnet](https://www.sharcnet.ca/my/front/) if
you want to know what it is. It's available to all universities in
Ontario I believe.

Terry: The core research software is just a simple Java application
[[http://nengo.ca](http://nengo.ca)], so that it can be easily run by
any researcher anywhere (we do tutorials on it at various conferences,
and there's tutorials online).

But, once we've got a model defined, we can that run that model on
pretty much any hardware we feel like. We have a CUDA version for GPUs,
we're working on an FPGA version, a Theano
[[http://deeplearning.net/software/theano/](http://deeplearning.net/software/theano/)]
version (Python compiled to C), and we can upload it into SpiNNaker
[[http://apt.cs.man.ac.uk/projects/SpiNNaker/](http://apt.cs.man.ac.uk/projects/SpiNNaker/)],
which is a giant supercomputer filled with ARM processors.

Terry: We're actually working directly with Kwabena Boahen, and have a
paper with him using this sort of model to do brain-machine interfacing
for prosthetic limbs:
[[http://books.nips.cc/papers/files/nips24/NIPS2011\_1225.pdf](http://books.nips.cc/papers/files/nips24/NIPS2011_1225.pdf)]

The great thing is that there are a whole bunch of projects right now to
build dedicated hardware for simulating neurons extremely quickly.
Kwabena takes one approach (using custom analog chips that actually
physically model the voltage flowing in neurons), while others like
SpiNNaker
[[http://apt.cs.man.ac.uk/projects/SpiNNaker/](http://apt.cs.man.ac.uk/projects/SpiNNaker/)]
just put a whole bunch of ARM processors together into one giant
parallel system. We're definitely supporting both approaches.

I should also note that, while there is a lot of work building these
large simulators, the question we are most interested in is figuring out
what the connections should be set to in order to produce human-like
behaviour. Once we get those connections figured out, then we can feed
those connections into whatever large-scale computing hardware is
around.

#### How do I get into your field?

Travis: I would say that your best bet is to find the neuroscience
people at your school and start attending talks. Approaching and asking
if there's a way you can get involved too is a great idea. It won't be
anything fancy, but especially if you have good programming skills
you'll be useful in some way off the bat, and as you develop a rapport
with the people in the lab you'll be able to work on more interesting
things and have good recommendations for when you apply to grad school!
And that's huge.

I would start by learning Python, it's a straightforward language with
really nice syntax. And you can look up simple reinforcement learning
algorithm cat vs mouse examples and the such! Just throw it into google
and a million tutorials / courses will pop up!  It'd be a great place to
start. Find projects that interest you and then figure out how to do
them. Being able to implement your own models / ideas is clutch in this
stuff.

The math you’ll need to learn will depend a bit on the kinds of modeling
you're going to be doing specifically, but calculus in general is always
useful, especially when you're modeling dynamical systems, and
probability theory / stats understanding will definitely come in handy
for the electrophysiology work! Anything you can do to start giving
yourself a leg up now you'll really appreciate later. Things like
watching Khan academy videos on intro to calculus is a big help.

Travis: Dr. Eliasmith's book 'The Neural Engineering Framework' is
definitely on all our reading lists, but we take a course with him to
get through it. And it's very painful. Aside from that, as more of an
introductory book I'm a fan of this bad boy by
Kandel[ ](http://www.amazon.com/Search-Memory-Emergence-Science-Mind/dp/0393329372)[http://www.amazon.com/Search-Memory-Emergence-Science-Mind/dp/0393329372](http://www.amazon.com/Search-Memory-Emergence-Science-Mind/dp/0393329372) It's
an easy read / intro to neuroscience. Most of what we do here is reading
papers and then coding up ideas / models that we develop, as things are
becoming more open access or if you have access to a campus internet
connection you can definitely do these things on your own as well to get
into things! For more specific reading list though, I would recommend
checking out our lab page, looking through our member's list and then if
someone's work interests you send them an email! Should be able to
provide a nice set of papers related to their area.

#### How can I get involved in this project?

Trevor: Oh boy! Lots of people wanting to help! Well, the first step is
to (attempt to) learn[ ](http://nengo.ca/docs/html/tutorial.html)[our
software](http://nengo.ca/docs/html/tutorial.html), and
the[ ](http://nengo.ca/docs/html/nef_algorithm.html)[theory behind
it](http://nengo.ca/docs/html/nef_algorithm.html). There's a course for
doing this at the University of Waterloo -- we're looking into ways that
we can offer this to people outside of the university in something like
Coursera (not for credit). Take an experimental neuroscience paper and
try to model it!

Trevor: Our simulator is up
on[ ](https://github.com/ctn-waterloo/nengo/)[github](https://github.com/ctn-waterloo/nengo/) and
our models are
up[ ](http://models.nengo.ca/)[here](http://models.nengo.ca/). We would
definitely welcome code contributions! Start with
the[ ](http://nengo.ca/docs/html/tutorial.html)[tutorials](http://nengo.ca/docs/html/tutorial.html) and
go from there!

#### What’s next?

Travis: One of the major focuses of the lab right now is incorporating
more learning into the model. A couple of us are specifically looking at
hierarchical reinforcement learning and building systems that are
capable of completing novel tasks using previously learned solutions,
and adding learned solutions to its repertoire!

One of the profs at UWaterloo is actually working on incorporating
robotics into our models, and having robot eyes / arm being controlled
by the spiking neuron models built in Nengo!

Terry: The project I'm currently working on is getting a bit more
linguistics into the model. The goal is to be able to describe a new
task to the model, and have it do that. Right now it's "hard-coded" to
do particular tasks (i.e. we manually set the connections between the
cortex and the basal ganglia to be what they would be if someone was
already an expert at those tasks).

Xuan: It has always been my goal to make a system navigate a maze, with
only visual input from a screen (or video device of some sort), and
motor output to a mouse (or similar device).

#### What's your opinion on the Singularity?  When will we have human-level AI?

Xuan: This is a rather hard question to answer. The definition of
"Singularity" is different everywhere. If you are asking when we are
going to have machines that have the same level of intelligence as a
human being, I'd have to say that we are still a long ways away from
that. (I don't like to make predictions about this, because my
predictions would most certainly be wrong.

Terry: Who knows. This sort of research is more about understanding
human intelligence, rather than creating AI in general. Still, I believe
that trying to figure out the algorithms behind human intelligence will
definitely help towards the task of making human-like AI. A big part of
what comes out of our work is finding that some algorithms are very easy
to implement in neurons, and other algorithms are not. For example,
circular convolution is an easy operation to implement, but a simple
max() function is extremely difficult. Knowing this will, I believe,
help guide future research into human cognition.

Terry: I would be extremely surprised if the first human-equivalent AI
happened in the next 20 years. I have two main reasons for this.

1.  We've only just begun to try to pin down the algorithms that
    different parts of the brain are using. They don't look anything
    like standard computing algorithms (they're much closer to control
    theory), and it's a very interesting challenge to try to map those
    on to psychological phenomena. So it feels to me like we're at the
    beginnings of a field, rather than in the "quickly ramping up" part.
2.  AI has constantly been "20 years away". There are predictions of AI
    being 20 years away all the way back to when this field started.

That said, the main reason that I got extremely excited about this work
and joined this lab is that I think this approach of actually building
complex biologically realistic models is the way forward. And I think
that if it turned out that everything we're doing in Spaun is right
(unlikely) and if all the other researchers in this field abandoned what
they were doing and started building Spaun-type models (even more
unlikely), then it feels to me human-level AI could happen in 20 years.
But, as I make that prediction, I'm very aware that I may be falling
into the prediction trap that lots of other AI researchers have made in
the past.

#### How did you train it? Is this just a giant backprop network?

Xuan: Only the visual system in Spaun is trained, and that is so that it
could categorize the handwritten digits. More accurately though, it
grouped similar looking digits together in a high dimensional vector
space. We trained it on the MNIST database (I think it was on the order
of 60,000 training examples; 10,000 test examples).

The rest of Spaun is however, untrained. We took a different approach
than most neural network models out there. Rather than have a gigantic
network which is trained, we infer the functionality of the different
parts of the model from behavioural data (i.e. we look at a part of the
brain, take a guess at what it does, and hook it up to other parts of
the brain).

The analogy is trying to figure out how a car works. Rather than
assembling a random number of parts and swapping them out until they
work, we try to figure out the necessary parts for a working car and
then put those together. While this might not give us a 100% accurate
facsimile, it does help us understand the system a whole lot better than
traditional "training" techniques.

Additionally, with the size of Spaun, there are no techniques right now
that will allow us to train that big of a model in any reasonable amount
of time.

Terry: There's a bit of tension right now between machine learning and
computational neuroscience. For the most part, machine learning is just
focused on solving problems, rather than figuring out how the brain
solves those problems. So ML tends to ignore neuroscience, but then
every now and then someone in ML uses neuroscience inspiration to make
the next big machine learning algorithm breakthrough (I'm thinking right
now of Geoff Hinton's deep belief networks
[[http://www.cs.toronto.edu/\~hinton/]](http://www.cs.toronto.edu/%7Ehinton/%5D)).
I also think computational neuroscience needs to be very familiar with
ML, so we can make use of any algorithms that show up there that might
be a good hypothesis for what the brain is doing.

The model is not started with a blank slate -- in fact, our approach is
pretty unique in terms of neural modelling in that we compute what the
connection weights should be, rather than rely on a learning rule
(although we can also add in a learning rule afterward).

#### How is this approach similar/dissimilar to things like the Blue Brain project?

Trevor: We definitely know of the Blue Brain project, but we don't have
any collaborations with them; they are trying to build a brain
bottom-up, figuring out all the details and simulating it. We are trying
to build a brain top-down, figuring out the functions we want it to
perform and building that with biologically plausible tools. Eventually
I hope that both projects will meet somewhere in the middle and it will
the best collaboration ever.

Travis: The Blue Brain project really has a different goal than our
work, I think. Their goal (as I understand it) is to simulate, as
realistically as possible, the number of neurons in a human brain. What
we're more concerned with here is how to hook up those neurons to each
other such that we get interesting function out of our models, so we're
very concerned with the overall system architecture and structure. And
that's how we can get out these really neat results with only 2.5
million neurons (which is just a fraction of the 10 billion a human
brain has). We are definitely interested in scaling up the number of
neurons we can simulate, but it's secondary to producing function.

Xuan: In order to understand the brain (or any complex system), there
are multiple ways of approaching the problem.  There is the bottom-up
approach - this is similar to the approach used by the Blue Brain
project - build as detailed and as complex a model as possible and hope
something meaningful emerges. There is the top-down approach - this is
the approach used by philosophers and psychologists. These models are
usually high level abstractions of behavioural data.

Then there are approaches that come in from the middle, i.e., everything
else in between.

You could say that our properties are "weakly constrained", but all of
the neuron properties are within those found in a real brain. The main
question we were trying to answer was "can we use what we understand
functionally about how the brain does things to construct a model that
does these things?"

It's similar to understanding how a car works. You can

1.  Replicate it in as much detail as possible and hope it works.
2.  Attempt to understand how each part of the car works, and what
    function each part has, and then construct your own version of it.
    The thing is, your construct may not be a 100% accurate facsimile,
    but it does tell us about our understanding of how a car works.

#### How do you model individual neurons?

Xuan: The models in spaun are simulated using a leaky-integrate-and-fire
(LIF) neuron model. All of the neuron parameters (max firing rate, etc)
are chosen from a random distribution, but no extra randomness is added
in calculating the voltage levels within each cell.

Travis: Our neural simulation uses Leaky Integrate and Fire neurons, but
yes! It is possible to use more complex neural models, and it's actually
been something we've been considering, to make it possible to
communicate with programs like Neuron that simulate on a much more
realistic level. But the LIF neurons do capture like 95% of the features
of better simulations, so we are content to use them (as they are also
very fast to simulate!)

Terry: The main thing we worry about for neuron types is the
neurotransmitter reabsorption rate. This varies wildly across different
types of neurons (from 2ms to 200ms), and that's very important for our
model. However, right now other than that we have all one neuron type:
the standard leaky-integrate-and-fire neuron. We've done some exploring
of other neuron types, but that work's not part of Spaun yet.

#### Ethical questions:

Terry: Being able to simulate a particular person's brain is incredibly
far away. There aren't any particularly good ideas as to how we might be
able to reasonably read out that sort of information from a person's
brain.

That said, there are also lots of uses that a repressive state would
have for any intelligent system (think of automatically scanning all
surveillence camera footage). But, you don't want a realistic model of
the brain to do that -- it'd get bored exactly as fast as people do.
That's part of why I a) feel that the vast majority of direct
medium-term applications of this sort of work are positive (medicine,
education), and b) make sure that all of the work is open-source and
made public, so any negative uses can be identified and publicly
discussed.

My biggest hope, though, is that by understanding how the mind works, we
might be able to figure out what is it about people that lets repressive
states take them over, and find ways to subvert that process.

#### Do you know Jeff Hawkins’ work and Numenta? How does this compare?

Terry: Definitely, and I've even fiddled with some of his Hierarchical
Temporal Memory models. It may be possible to build interesting AI out
of his version of cortical columns (although my instinct is that that
sort of processing is only one of many types of processing found in the
brain). But our goal is to try to understand how the human brain works,
not build brain-like AI in general. We're working at the level of
neurons (rather than cortical columns) because a) neurons are pretty
well understood, and b) there seems to be a lot of representational
power in the sorts of distributed representations neurons use.

Of course, future models may have to include even finer details about
proteins and whatnot, if those details turn out to have important
behavioural effects for understanding human cognition.

#### Reddit AMA, with lots more questions and answers

[http://www.reddit.com/r/IAmA/comments/147gqm/we\_are\_the\_computational\_neuroscientists\_behind/](http://www.reddit.com/r/IAmA/comments/147gqm/we_are_the_computational_neuroscientists_behind/)

* * * * *

Less frequently asked questions
===============================

#### What are your thoughts on the connectome project?

Terry: We're definitely keeping a close eye on the connectome project.
My hope is that it'll progress along to a point where we might be able
to compare the connections that we compute are needed to the actual
connections for a particular part of the brain. However, right now the
main thing we can get from the connectome project is the sort of
high-level gross connectivity (part A connects to part B, but not to
part C) rather than the low-level details (neuron \#1,543,234 connects
to neuron \# 34,213,764 with strength 0.275).

#### How is your work different than Jeff Krichmar’s work on neurorobotics?

Terry: Jeff's work focuses on real-time robotics. We focus on trying to
figure out how the human brain works. We do this by making sure the
components in the model (simulated neurons) map on to components in the
real brain (neurons), so that we can use the simulation as a way of
testing our understanding. So our models are constrained to have the
same organization as the human brain, and since we have more realistic
neurons, the models run slower.

We also have components in our model specifically for doing human-style
reasoning (memorizing lists, finding patterns in numbers, adding by
counting), which aren't a priority for Jeff's group.

#### What do you think is the nature of the connection between the cells? Would you say they are best characterized as a computational symbol manipulation network or would a connectionist neural network actually be more appropriate?

Terry: We go with a third approach, and we actually have a paper in the
Oxford Handbook of Compositionality on exactly this topic:
[[http://ctnsrv.uwaterloo.ca/cnrglab/node/276](http://ctnsrv.uwaterloo.ca/cnrglab/node/276)].
Basically, we're making use of a neural representation approach that
allows for symbol-like manipulations while still being completely
connectionist. But when building the models, it makes more sense to
think about it as symbol-like, rather than neural.

#### How can the brain be thought of as a computer and how this might be consistent with things like emotion and consciousness?

Terry: It definitely cannot be thought of as a classical computer (or at
least it's not useful to think of it as a classical computer). Building
these sorts of models severely stretches what we think of as a
"computer".

I also think it will be possible to model emotions with these systems
(especially since most of the emotional centres in the brain are pretty
old in evolutionary terms, so they may be simpler than the more complex
recent things like language). We're not researching in that direction at
the moment, but I don't see why these techniques wouldn't apply.

That said, even if we build these full simulations of the brain, we're
still going to be left with the response "well, it's just behaving as if
it had emotions, but it doesn't really feel anything". To which there's
always the reply "well, how do I know you really feel anything and
aren't just behaving as if you feel things?" When/if researchers ever
get to that stage, that'll be a very interesting debate to have, and I
tend to fall on the side of "a difference that makes no difference is no
difference” -- so there's no difference between actually having feelings
and behaving as if you have feelings.

#### What is currently the limiting the power of SPAUN?

Terry: The limit is what brain parts we know how to model. There's all
sorts of parts of the brain that don't exist in Spaun. So we need to get
a better theoretical understanding of what those parts do, write that as
a mathematical algorithm, derive how neurons could do that computation,
and then add it to the model.

There's also a lot of adaptability (i.e. learning) going on in many
parts of the brain that we still don't have a good handle on, even for
the parts that are in Spaun.

I think those things are limiting us much more than computational power.
That said, more computational power will let us try out different
algorithms more easily, which will help with the real problems.

#### What's your response to Noam chomsky's critique of Modern day neuroscience in this [Atlantic article](http://www.theatlantic.com/technology/archive/2012/11/noam-chomsky-on-where-artificial-intelligence-went-wrong/261637/)?

Terry: I pretty much agree with Chomsky that we need to have a
theoretical understanding of what's going on in the brain, instead of
just throwing stats at it. I'm a bit more positive on the stats approach
than Chomsky lays out in that article, but that's because the main thing
that we do is figure out how to combine the two. To understand the brain
we need to figure out what the underlying structures and algorithms are,
and one of the most important aspects we need to understand for human
brains is how to represent and manipulate structured information. The
core part of how Spaun works is a proof-of-concept of how it is possible
for neurons to store and manipulate structured information, which is
something that's been traditionally very difficult for neural (and
statistical) approaches.

#### What are the hypotheses that you are testing at the moment? Anything related to the binding problem?

Terry: Good question. The main part of the research was just getting it
to run and give vaguely realistic results. We did find a good match to
human performance for recognizing hand-written digits and serial recall
(forgetting items in the middle of a list more than the ends). For more
detailed predictions, we're looking at things like the spiking patterns
of neurons in particular areas when guessing a number (and comparing
that to spiking patterns in rats when guessing which lever to press).

As for the binding problem, that's actually a very big part of this
research -- it's what lets us do things like memorize a series of
numbers (for those that don't know, the binding problem is the question
of how the brain manages to represent multiple things at once at keep
them straight. For example, if I have "8, 4, 7", I have to represent 8
in position 1, 4 in position 2, and 7 in position 3" all at the same
time, and keep that distinct from "4, 7, 8" and other orderings). A lot
of neuroscientists make the assumption that this is done by neural
oscillations: first the pattern for "8 in position 1" appears, then "4
in position 2", then "7 in position 3" appears, all in a fraction of a
second.

That's not what we do. Instead, we use the approach taken by Vector
Symbolic Architectures
[[http://cogprints.org/3983/](http://cogprints.org/3983/)], which shows
a way to combine patterns to get new patterns that you can decompress
back to the original patterns. This operation (we use circular
convolution) turns out to be really easy to implement in neurons.

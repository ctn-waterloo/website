title: Neural Cognitive Architecture

Cognitive science has developed a wide variety of theories about human
cognition. While some of these theories are merely _descriptive_ (i.e. they
describe human cognitive behaviour), many are _mechanistic_, in that they
postulate a set of internal components which interact over time to produce the
observed behaviour. These components can be referred to as a _cognitive
architecture_.

The most successful and widely used cognitive architecture is
[ACT-R](http://act-r.psy.cmu.edu/). This includes components for memory,
vision, motor behaviour, time estimation, and central executive control. These
same components have been used for models of mental arithmetic, problem
solving, task switching, car driving, phone dialing, sequence memory, GUI
usage, and so on (see [here](http://act-r.psy.cmu.edu/publications/index.php)
for more examples and related publications). These models come from many
different people and many different labs, making it the most widely used and
tested cognitive archicture.

The focus of ACT-R research has been to develop this common setof components
for modelling cognitive activities. By re-using these same components, they
can minimize the amount of parameter fitting and model-tweaking needed to
match human behaviour on all these tasks. However, they have been focussed on
_what_ the brain does, not _how_ it does it. That is, they want to identify
the algorithms behind cognition, not how neurons implement that algorithm.

Recently, John Anderson (the core person behind ACT-R) has been doing a lot of
work with fMRI to try to identify the neurological correlates to the various
components of ACT-R. The intent here is to bring in neural evidence to help
constrain ACT-R theory, which right now is mostly constrained by psychology
data (i.e. the model's behaviour has to match human reaction times, error
rates, and so on). Adding in neural constraints can help to suggest
modifications to ACT-R, or provide support for some of the ACT-R assumptions.
This has led to a work comparing the activity of particular brain areas to
various ACT-R components, in tasks such as the [Tower of
Hanoi](http://act-r.psy.cmu.edu/publications/pubinfo.php?id=606), and [mental
symbol manipulation](http://act-r.psy.cmu.edu/publications/pubinfo.php?id=500)
(for more, see
[here](http://act-r.psy.cmu.edu/publications/index.php?subtopic=37)). There's
also a short overview of this approach
[here](http://act-r.psy.cmu.edu/publications/pubinfo.php?id=800). and for a
more complete overview, see John Anderson's book "[How Can the Human Mind
Occur in the Physical Universe?](http://www.amazon.com/Physical-Universe-
Oxford-Cognitive-Architectures/dp/0195324250)".

It is definitely promising to see a degree of correlation between ACT-R
predictions of BOLD signals and real data. However, without an explicit
implementational story for the various components, many assumptions have to be
made to create these BOLD predictions. Furthermore, if we had a fully neural
implementation of these components, we could also bring in a lot of other
neural evidence involving spiking patterns, connectivity, neurotransmitter
use, drug effects, and even DBS.

Our goal is to create a fully neural implementation of each of the components
of ACT-R, using realistic spiking neurons constrained by known neural anatomy.

We have chosen ACT-R as an interesting minimal target for building large-scale
neural systems. If we can build a neural system with components that can
perform the few basic functions needed by ACT-R, then we can relate the
resulting neural model to a wide range of behavioural data, while still being
able to look at low-level neural effects.

Currently, we are focusing on the basal ganglia, which for the ACT-R people
correlates to a production system, along with a reinforcement learning system
to use reward feedback to control action selection. This certainly doesn't
completely capture everything about the basal ganglia, but there seems to be
enough evidence that it's at least in the right general ballpark. It fits in
nicely with the dimensionality reduction ideas, and the dopamine/reinforcement
learning connection.

This basic model of this system is currently at a stage where it can do basic
action selection based on the current context, choose an action that will
modify the current context, modify that context, and choose a new action.
Interestingly, constraining the neural model to use GABA results in a model
that requires about 50ms to make a choice, which is the experimental best-fit
to a wide range of behavioural data.

## Publications

  * [Spiking neurons and central executive control: The origin of the 50-millisecond cognitive cycle](http://arts.uwaterloo.ca/~cnrglab/?q=node/568)

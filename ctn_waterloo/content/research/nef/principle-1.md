title: Principle 1

## Principle 1

> Neural representations are defined by the combination of nonlinear encoding
(exemplified by neuron tuning curves) and weighted linear decoding.

Quantitatively, we can write the encoding:

![](http://arts.uwaterloo.ca/~cnrglab/?q=system/files/eqn1.gif)

and the decoding:

> ![](http://arts.uwaterloo.ca/~cnrglab/?q=system/files/eqn2.gif)

where

![](http://arts.uwaterloo.ca/~cnrglab/?q=system/files/eqn3.gif)

In these equations, _a_ is the activity of a neuron, _i_, encoding a vector
signal **x**(_t_), in a spike train (represented as a sum of delta functions,
with each spike indexed by _n_). The encoding is defined by the nonlinear
function, _G_, and parameterized by a gain, \_alpha_, and a bias, _J_^_bias_.
The encoding vector _\tilde\phi _determines the neuron's preferred stimulus in
the signal (the elements inside the square brackets determine the soma
current). An estimate of the signal is recovered through linear population
decoding, using the vectors _\phi_ and linear temporal decoding using the
filter _h_(_t_). These can be combined to give a population-temporal decoder,
_\phi_i(t-t_in)_.

Principle 1 emphasizes the importance of identifying both encoding and
decoding when defining neural representation. Moreover, this principle
highlights the central assumption that, despite a nonlinear encoding, linear
decoding is valid (see Rieke et al. 1997, pp. 7687). As discussed in detail
by Rieke et al., a nonlinear response function like that of typical neurons
is, in fact, unrelated to whether or not the resulting signal can be linearly
decoded. That is, the nature of the input/output function (i.e., encoding) of
a device is independent of the decoder that is needed to estimate its input.
This means that a nonlinear encoding could need a linear or nonlinear
decoding, and vice versa. This is because the decoding depends on the
conditional probability of input given the output and on the statistics of the
noise (hence our addendum). Perhaps surprisingly, linear decoding works quite
well in many neural systems. Specifically, the additional information gained
with nonlinear decoding is generally less than 5%.

Of course, nonlinear decoding is able to do as well or better than linear
decoding at extracting information, but the price paid in biological
plausibility is generally thought to be quite high (see, e.g., Salinas and
Abbott 1994). Furthermore, even if there initially seems to be a case in which
nonlinear decoding is employed by a neural system, that decoding may, in the
end, be explained by linear decoding. This is because, as we discuss in
section 6.3 (this and all subsequent section references are to the book),
nonlinear transformations can be performed using linear decoding. Thus,
assuming linear decoding at the neuron (or sub-neuron, see section 6.3) level
can well be consistent with nonlinear decoding at the network (or neuron)
level. So, especially in combination with principle 2, linear decoding is a
good candidate for describing neural decoding in general.

It is important to emphasize that analyzing neurons as decoding signals using
(optimal) linear or nonlinear filters does not mean that neurons are presumed
to explicitly use opti-mal filters. In fact, according to our account, there
is no directly observable counterpart to these optimal decoders. Rather, the
decoders are embedded in the synaptic weights between neighboring neurons.
That is, coupling weights of neighboring neurons indirectly reflect a
particular population decoder, but they are not identical to the population
decoder, nor can the decoder be unequivocally read-off of the weights. This
is because connection weights are determined by both the decoding of incoming
signals and the encoding of the outgoing signals (see, e.g., section 6.2).
Practically speaking, this means that changing a connection weight both
changes the transformation being performed and the tuning curve of the
receiving neuron. As is well known from work in artificial neural networks and
computational neuroscience, this is exactly what should happen. In essence,
the encoding/decoding distinction is not one that neurobiological systems need
to respect in order to perform their functions, but it is extremely useful in
trying to understand such systems and how they do, in fact, manage to perform
those functions.

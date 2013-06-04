title: Quantitative summary of the NEF

This is slightly modified from the section of our book (Neural Engineering,
MIT Press) that describes each of the three principles of the NEF using
equations.

**Three principles of neural engineering quantified**

In order for the principles of neural engineering to underwrite a theory of
neurobiology, they must be quantitatively expressed. As we have shown that
each of scalars, vectors, and functions can be treated as vector
representation (in the book), we only present these principles as they relate
to vectors.

_Principle 1_

Neural representations are defined by the combination of nonlinear encoding
and weighted linear decoding.

Neural encoding is defined by

[inline:newfile10x.png]

Neural decoding is defined by

[inline:newfile11x.png]

where

[inline:newfile12x.png]

In both cases, _i_ indexes neurons in population and _n_ indexes spikes
transmitted from one population to another.

_Principle 2_

Transformations of neural representations are functions of the variable that
is represented by the population. Transformations are determined using an
alternately weighted linear decoding.

Assuming the encoding in principle 1, we can estimate a function of x(t) as

[inline:newfile13x.png]

where, ai(x(t)) is defined as before. The only difference between this
decoding and the representational decoding are the decoders themselves, Ď.

_Principle 3_

Neural dynamics are characterized by considering neural representations as
control theoretic state variables. Thus, the dynamics of neurobiological
systems can be analyzed using control theory.

Allowing x(t) to be a state variable and u(t) to be the input, we have the
following general expression for the encoding:

[inline:newfile14x.png]

To get a better understanding of how these principles can be used together,
please refer to the various examples on the website. For several simple
applications, see [this paper](http://compneuro.uwaterloo.ca/cnrglab/f/eliasmi
th.2005.controlling.attractors.neurcomp.pdf).

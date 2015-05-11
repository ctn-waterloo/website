title: Overview of the NEF

### Introduction

The framework we have developed for understanding neurobiological systems is
summarized below by what we call _"Principles of Neural Engineering"_. We have
used these principles to define a methodology for constructing simulations of
neural systems (the methodology is also discussed in more detail below). We
have had great success in applying both the principles and the related
methodology to constructing models of perceptual, motor, and cognitive
systems.

### Principles of Neural Engineering

  1. Neural representations are defined by the combination of nonlinear encoding (exemplified by neuron tuning curves) and weighted linear decoding. [[further discussion](/research/nef/principle-1.html)]
  2. Transformations of neural representations are functions of variables that are represented by neural populations. Transformations are determined using an alternately weighted linear decoding (i.e., the transformational decoding as opposed to the representational decoding). [[further discussion](/research/nef/principle-2.html)]
  3. Neural dynamics are characterized by considering neural representations as control theoretic state variables. Thus, the dynamics of neurobiological systems can be analyzed using control theory. [[further discussion](/research/nef/principle-3.html)]

_Addendum_

> Neural systems are subject to significant amounts of
> noise. Therefore, any analysis of such systems must account for the
> effects of noise. [[further discussion](/research/nef/addendum.html)]

### Methodology

Relying on these four principles for understanding the information processing
characteristics of neurobiological systems has lead us to develop the
following methodology for constructing simulations of neural systems.

#### Step 1: System description

The main goal of the first step is to describe the neural system of interest
in such a way that the principles outlined previously are directly applicable
to it. In particular, available neuroanatomical data and a good functional
understanding (hypothetical or otherwise) are used to describe the
architecture, function, and representations of the neural system. This
description should include at least interconnectivity between subsystems,
neuron response functions, neuron tuning curves, subsystem functional
relations, and overall system behavior.

Next, we express the functional description in mathematical terms. In
particular, the relevant mathematical variables should be specified in such a
way that they can be used to write mathematical transformations that describe
the previously specified functions. The goal here is to translate the
functional description provided in neurobiological terms into a description in
mathematical terms. This mathematical description may be highly abstract
(e.g., describing a swimming eel as instantiating a kind of sine function; see
the lamprey example in the book; or see this
[summary [PDF]](http://compneuro.uwaterloo.ca//files/lamprey.pdf)), so long as it is complete.

#### Step 2: Design specification

The second step of the methodology consists in precisely specifing the real-
world limitations on that are known or assumed for the neural system of
interest. Implementational constraints are of paramount importance when
modeling neurobiological systems. This second step in the methodology helps
make these constraints central to generating a good model. First, the
appropriate kind of representation for each variable (e.g., scalar, vector,
vector field, probability density function, etc.) must be determined. Then,
the dynamic range, precision, and signal-to-noise ratio for each degree of
freedom of variable specified in the preceding step must be determined.
Similarly, the temporal characterisitics, such as bandwidth and power
spectrum, must be specified. All such specifications should be made on the
basis of available data, if possible.

Together, these specifications will clearly define the real-world operating
constraints that the system must satisfy in order to successfully perform its
function. Not surprisingly, these specifications can significantly affect the
final model that is generated. If, for example, the signal-to-noise ratio must
be extremely high, the neural system will have to be composed of many neurons.

#### Step 3: Implementation

The third and last step of our methodology involves generating the model
itself. Given the system description and design specification, this step
combines them to determine appropriate encoding and decoding rules needed to
implement the desired behavior. There are two sets of encoding and decoding
rules: the first relates higher-order representations (e.g., vectors) to
lower-order representations (e.g., neuron firing rates); and the second set of
rules determines transformations of representations at a given level of
representation. In this step, we can compute the linear decoding that meets
the design specifications and also determine the connection weights between
neurons in our model network.

As well, at this step it is possible to determine which aspects of the system
will be simulated with the greatest detail and which will be simulated with
less detail. We can, in other words, construct models that are simulated
partly at the level of spiking conductance-based neurons and partly at the
level of, for example, neuronal groups. This is extremely useful when we have
limited computational power and large models.

### Summary

Together, these three steps provide a kind of algorithm for generating models
of neurobiological systems. However, applying these steps to real systems is
seldom a straightforward task. Although we have presented the methodology as
three consecutive steps, we have found that it is better practice to iterate
over these steps than to simply follow them in serial order. Often, the
behaviors of an initial implementation can help inform a reworking of the
initial system description. Similarly, design specifications can serve to
modify initial system descriptions. A large part of the reason for this kind
of interplay between steps is the preponderance of gaps in our knowledge about
the systems we are modeling. Of course, one of the greatest benefits of a good
simulation can be determining precisely what the knowledge is that we are
missing.

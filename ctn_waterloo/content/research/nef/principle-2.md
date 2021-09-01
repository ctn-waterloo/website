title: Principle 2

> Transformations of neural representations are functions of variables
> that are represented by neural populations. Transformations are
> determined using an alternately weighted linear decoding (i.e., the
> transformational decoding asopposed to the representational
> decoding).

Quantitatively, we assume the same encoding as described in principle 1 and
define the decoding:

$$\hat{f}(\mathbf{x}(t)) = \sum_i a_i (\mathbf{x}(t)) \phi_i^f$$

This decoding is the similar to that in principle 1, except the decoders are
determined such that a function, $f$, of the original input signal is
estimated.

The comments in principle 1 about representational decoders apply equally to
transformational decoders. This should be no surprise given our prior
discussion (in section 1.3; this and all subsequent section references are to
the book) in which we noted that defining a transformation is just like
defining a representation (although with different decoders). However, we did
not previously emphasize the kinds of transformations that can be supported
with linear decoding.

It has often been argued that nonlinear transformations are by far the most
common kind of transformations found in neurobiological systems (see, e.g.,
Freeman 1987). This should not be surprising to engineers, as most real-world
control problems require complex, nonlinear control analyses; a good
contemporary example being the remote manipulator system on the international
space station. This should be even less of a surprise to neuroscientists who
study the subtle behavior of natural systems. As Pouget and Sejnowski (1997)
note, even a relatively simple task, such as determining the head-centered
coordinates of a target given retinal coordinates, requires nonlinear
computation when considered fully (i.e., including the geometry of rotation in
three dimensions). Thus, it is essential that we be able to account for
nonlinear as well as linear transformations. In section 6.3 we discuss how to
characterize nonlinear transformations in general. We provide a
neurobiological example of a nonlinear transformation (determining the cross
product) that allows us to account for a number of experimental results (see
section 6.5). Thus we show that assumptions about the linearity of decoding do
not limit the possible functions that can be supported by neurobiological
systems.

This result will not be surprising to researchers familiar with current
computational neuroscience. It has long been known that linear decoding of
nonlinear basis functions can be used to approximate nonlinear functions
(see section 7.4). Nevertheless, our analysis sheds new light on standard
approaches. Specifically, we: 1) show how observations about neural systems
can determine which nonlinear functions can be well-approximated by those
systems (section 7.3); 2) apply these results to large-scale, fully spiking
networks (section 6.5); and 3) integrate these results with a characterization
of neural dynamics and representation (section 8.1.3).

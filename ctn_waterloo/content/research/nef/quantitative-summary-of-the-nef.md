title: Quantitative summary of the NEF

This is slightly modified from the section of our book (Neural Engineering,
MIT Press) that describes each of the three principles of the NEF using
equations.

### Three principles of neural engineering quantified

In order for the principles of neural engineering to underwrite a theory of
neurobiology, they must be quantitatively expressed. As we have shown that
each of scalars, vectors, and functions can be treated as vector
representation (in the book), we only present these principles as they relate
to vectors.

#### Principle 1

Neural representations are defined by the combination of nonlinear encoding
and weighted linear decoding.

Neural encoding is defined by

$$\sum_n \delta(t - t_{in}) = G_i \left[\alpha_i \langle
  \tilde{\phi_i} \mathbf{x}(t) \rangle_m + J_i^{bias} \right]$$

Neural decoding is defined by

$$\mathbf{\hat{x}}(t) = \sum_i a_i(\mathbf{x}(t)) \phi_i^{\mathbf{x}},$$

where

\begin{align}
  a_i(\mathbf{x}(t)) &= \sum_n h_i(t) * \delta(t - t_{in}) \\\\
  &= \sum_n h_i (t - t_{in}).
\end{align}

In both cases, $i$ indexes neurons in population and $n$ indexes spikes
transmitted from one population to another.

#### Principle 2

Transformations of neural representations are functions of the variable that
is represented by the population. Transformations are determined using an
alternately weighted linear decoding.

Assuming the encoding in principle 1, we can estimate a function of $\mathbf{x}(t)$ as

$$\hat{f}(\mathbf{x}(t)) = \sum_i a_i (\mathbf{x}(t)) \phi_i^f,$$

where $a_i(\mathbf{x}(t))$ is defined as before. The only difference between this
decoding and the representational decoding are the decoders themselves.

#### Principle 3

Neural dynamics are characterized by considering neural representations as
control theoretic state variables. Thus, the dynamics of neurobiological
systems can be analyzed using control theory.

Allowing $\mathbf{x}(t)$ to be a state variable
and $\mathbf{u}(t)$ to be the input, we have the
following general expression for the encoding:

$$\sum_n \delta(t - t_{in}) = G_i \left[ \alpha_i
  \left\langle \tilde{\phi_i}
  \left( h_i(t) * \left[ \mathbf{A}' \mathbf{x}(t)
  + \mathbf{B}' \mathbf{u}(t) \right] \right)
  \right\rangle_m + J_i^{bias} \right]$$

To get a better understanding of how these principles can be used together,
please refer to the various examples on the website. For several simple
applications, see [this paper](http://compneuro.uwaterloo.ca/files/eliasmith.2005.controlling.attractors.neurcomp.pdf).

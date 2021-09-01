title: Principle 3

> Neural dynamics are characterized by considering neural
> representations as control theoretic state variables. Thus, the
> dynamics of neurobiological systems can be analyzed using control
> theory.

Quantitatively, we can write the following general expression for the
encoding:

$$\sum_n \delta(t - t_{in}) = G_i \left[ \alpha_i
  \left\langle \tilde{\phi_i}
  \left( h_i(t) * \left[ \mathbf{A}' \mathbf{x}(t)
  + \mathbf{B}' \mathbf{u}(t) \right] \right)
  \right\rangle_m + J_i^{bias} \right]$$

Here we have introduced the neural dynamics matrix,
$\mathbf{A}'$,
and input matrix $\mathbf{B}'$.
These matrices define the dynamics of the system,
and can be related to the standard dynamics
and input matrices in linear control theory using:

\begin{align}
  \mathbf{A}' &= \tau \mathbf{A} + \mathbf{I} \\\\
  \mathbf{B}' &= \tau \mathbf{B}.
\end{align}

The signal $\mathbf{u}(t)$ is the input
and $\mathbf{x}(t)$ is the neural population's represented state vector.
Note: $*$ indicates convolution.

As noted in section 1.3 (this and all subsequent section references are to the
book), we can adapt standard control theory to be useful for modeling
neurobiological systems by accounting for intrinsic neuron dynamics. There are
a number of features of control theory that make it extremely useful for
modeling neurobiological systems. First, the general form of control systems,
captured by the state-space equations, can be used to relate to the dynamics
of non-biological systems (with which engineers may be more familiar) to the
dynamics of neurobiological systems. Second, the engineering community is very
familiar with the state-space approach for describing the dynamic properties
of physical systems, and thus has many related analytical tools for
characterizing such systems. Third, modern control theory can be used to
relate the dynamics of *external* variables, like actual joint angles, to
*internal* variables, like desired joint angles. This demonstrates how one
formalism can be used to span internal and external descriptions of behavior.

Adopting this perspective on neural dynamics allows us to develop a
characterization of what we call a "generic neural subsystem."  This
multi-level, quantitative characterization of neural systems serves to
unify our discussions of neural representation, transformation, and
dynamics (section 8.1.3). Given our previous discussion regarding the
importance of nonlinear computations, a focus on standard control
theory, which deals mainly with linear dynamics, may seem
unwarranted. However, contemporary nonlinear control theory, which may
prove more valuable in the long run, depends critically on our current
understanding of linear systems. Thus, showing how linear control
theory relates to neurobiological systems has the effect of showing
how nonlinear control theory relates to neurobiological systems as
well. In fact, many of the examples we provide are of nonlinear
dynamic systems (see sections 6.5 and 8.2).

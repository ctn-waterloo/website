title: Neural Engineering book to do list

On this page, we have collected some unresolved issues regarding neural signal
processing, ordered them by the chapter of the Neural Engineering book that
they relate to, and provided brief descriptions of them.

### Chapter 2

- Comparison to nonlinear decoding/encoding methods. Note that estimates of nonlinear decoding can be done using multiple linear decoders (since we can estimate nonlinear functions of the input signal: i.e., $\hat{x}=\sum _{i}\phi ^{x}_{i}a_{i} + \sqrt{\phi _{i}^{x^{2}}a_{i}}+...$). It would be useful to see if a biologically plausible nonlinear decoder could be constructed that gave significant information transfer gain.

- It should be possible to analytically demonstrate the we expect the error due to noise to decrease as $1/N^2$, as shown numerically.

### Chapter 4

- There needs to be more work done on what kinds of PSCs to expect in certain conditions, and what kinds of computations certain PSCs are best suited too. We have treated PSCs as rather generic, which they aren't. Different dynamics for PSCs (and modulating those dynamics) are no doubt important for the range of neural dynamics actually seen.

- We need to finish developing methods for optimal population decoder generation that includes timing information too (e.g. for adapting neurons). In other words, the optimal filters should depend on the detailed temporal dynamics of the different cellular models, not just a LIF approximation to their tuning curves.

- It should be possible to include ion channel dynamics in the framework. This would facilitate inclusion of bursting and other more complex intrinsic cell dynamics.

### Chapter 6

- In the discussion of the negative weights problem, it would be useful to provide an analytic proof that we can always find scaling factors to make all weights positive. We have only shown this numerically.

- Similarly, it would be useful to determine if/when ensembles violate the half-plane constraint for negative weights.

- Our brief discussion of embedding nonlinearities into dendrites using the framework leaves much room for expansion. Specific examples, and dealing with issues of dendritic subgroups, and details of implementation are essential.

- It is essential to understand the relation between nonlinearities and noise, which we have not addressed. The large fluctuations observed in cortical firing could be due either to noisy intrinsic processes (i.e. Poisson processes), or the ubiquity of nonlinearities (i.e. deterministic, but nonlinear). The relation between the two needs to be examined.

### Chapter 8

- Most obviously, it would be valuable to adopt a better synaptic model and do a similar derivation to find the neural equivalent of standard control structures (i.e. $1/1+s\tau$ is a first-order approximation).

- Our current analysis (though not the models) assumes the same PSC for each connection between populations. It would be useful to relax this assumption and see how the analysis is affected.

- We are not entirely satisfied with having to define $g(t)=h(t)*h(t)$ in order to complete the analysis. It would be cleaner if this was not done.

- It would be useful to demonstrate more typical control theoretic analyses on an example system (perhaps the neural integrator). That is, explore open and closed loop gain, show the Bode plot, etc. in general, doing signal/control analyses more extensively.

- The lamprey model raises the possibility of including oscillators directly in framework. That is, explicitly incorporating cellular variables and ion channel dynamics (see chapter 4 to do list).

- To examine more general attractor networks, it would be useful to explore systems with more complex attractors using the framework (like torus and chaotic attractors (see Freeman)).

- A good example: Simon Giszter and his colleagues have done excellent work on frog spinal reflexes and their use during motor control. In terms of the framework, they have identified the basis functions that are used for generating locomotion. Deriving control systems, decoders, etc. could be explored by adopting this approach.

### Chapter 9

- Foremost, it would help to relate the discussion of statistical inference to more realistic neurobiological examples.

- The Kalman filter, is the only example we relate to neurobiology in much detail. It would be useful to both generalize (along the lines indicated during that discussion) and implement the Kalman filter in the two forms discussed. This could help generate predictions and perhaps suggest experiments and elaboration of the circuit.

- As mentioned in this chapter, integrating learning poses the greatest challenge to the framework. We need a more complete analysis of the relation between our approach and learning, and more specific neurobiological examples that include learning.

- The biggest challenge is to derive local learning rules that will result in the complex control circuits that describe neural function.

- An example: The neural integrator receives an error signal (retinal slip) that is probably used to tune the weights in the network. This could be incorporated into the current model.

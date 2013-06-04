title: Correlations, network structure and the NEF

A collaboration page for work with Eric Shea-Brown's lab at the University of
Washington.

**Question:** What is the character of network correlations in learned and NEF-generated networks of spiking LIF neurons.

**Approach:**

Simulate a few basic networks (i.e. communication channel and integrator), and
examine the correlational structure. Compare and contrast the NEF weights with
learned weights.

  * We can do the simulations of the networks (i.e. generate files with spike times over populations of cells)
  * Eric's group has good methods for doing the correlational analyses.

**Points to discuss:**

_Parameters of the simulations_

  * How long should runs be? 1000s
  * How many neurons in the network? 100/layer
  * What kinds of cells and parameters? LIF; 20ms membrane; 2ms refractory; max firing 10-100hz;
  * What kind of input? Bandlimited white noise, to 30hz (?)

_Other_

**Extensions:**

  * If there is a mismatch, can we enforce correlational structure while generating desired weights in the NEF?

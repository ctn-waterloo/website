title: Non Linear Pyramidal Cells

Pyramidal Cells are present in the cerebral cortex and the hippocampus. They
exhibit non linear summation of inputs, with dendritic compartments acting as
individual subunits capable of producing their own spikes. These dendrites
then project to the cell body, where all dendritic signals are summed and
integrated to determine the spiking behavior of the Pyramidal Cell body. Thus,
Pyramidal Cells are multi-subunit structures, capable of computations which
are far more complex than those of a linear point neuron. Properties of
Pyramidal Cells useful for modeling are outlined below. Note that there are
several different types of pyramidal cell depending on which region of the
brain one is considering. Although they are expected to behave similarly, they
do have some differences. It is for this reason that information will be given
for individual pyramidal cell types.

## Structural Summary

Primary references: Megias et al., 2001; Spruston, 2008; Marenco et al., 2009

- All pyramidal cells contain the same basic structure.
  They are composed of a pyramidal shaped cell body, and a single, heavily branching axon projecting from the base.
- The dendrites of a pyramidal neuron can be divided into two domains: basal and apical.
- The basal dendritic tree is composed of 3-5 primary dendrites.
  Each of these divides to form branches of progressively thinning length.
- The apical tree, which also splits several times, ends in a largely branched section known as the apical tuft.
- The dendrites of pyramidal cells are covered with tiny branches known as dendritic spines.
  As one moves distal to the soma, the number of spines increases.
  These spines increase the surface area, and are believed to be where the majority of synapses arrive at the dendrites.
- From a modeling perspective, both basal and apical branches contain proximal, medial, and distal compartments.
  These can be viewed as individual computational subunits.
  In addition, CA1 pyramidal neurons contain oblique medial and oblique distal branches,
  which arise from the medial apical and medial distal dendrites respectively.

## Input Connections

Primary reerence: Spruston, 2008

* **Layer II/III and V**
  * Proximal Apical and Basal Dendrites: Layer IV and local circuits
  * Apical Tuft: Cortical and Thalamic areas, **CA1**
  * Proximal Apical and Basal Dendrites: CA3
  * Apical Tuft: Entorhinal cortex and thalamic nucleus reuniens

## Resting Membrane Potentials

* **CA1 Pyramidal Cell** (Gasparini et al., 2004)
  * Soma: approximately -65 $\pm$ 1 mV
  * Dendrites: approximately -66 mV

## Spiking

* **CA1 Pyramidal Cell** (Gasparini et al., 2004)
  * Soma Threshold: -56 $\pm$ 1 mV
  * Dendrite Threshold: -48 $\pm$ 1 mV
  * Current Required: ≥ 3 nA
  * Spike Amplitude: 67 $\pm$ 1 mV

## Dendritic Summation

* **Cortical Pyramidal Cells** (Polsky et al., 2004)
  * Between branches: linear summation of inputs
  * Within a dendritic branch: Sigmoidal summation of inputs
  * Weak stimulus: linear summation
  * Intermediate stimulus: superlinear summation
  * Strong stimulus: sublinear summation
  * Threshold potential:
    * Single pulse: 5.3 $\pm$ 1.7 mV -> 185 $\pm$ 60% amplification
    * Paired pulse: 3.3 $\pm$ 0.6 mV -> 263 $\pm$ 104% amplification
  * Maximum paired pulse distance for superlinear summation: 40 µm
  * Possible superlinear summation distances: Between 45 and 80 µm
  * Required combined depolarization: 6.9 $\pm$ 2.4 mV
  * Leads to an EPSP that is 1.28 $\pm$ 0.16 times as strong as the expected linear response.

## Modelling Suggestions

### Two Layer Neural Network (Poirazi et al., 2003)

A pyramidal neuron can be simplified to a two layer network,
where the first layer is composed of dendritic subunits capable of spiking,
and the second layer is the soma, acting as an integrating center.
The firing rate is then characterized by the equation:

$$g(x) = \frac{0.96x}{1 + 1509e^{-0.26}x}$$

where

* $x = \sum \alpha_i s(n_i)$
* $n_i$ - net number of excitatory synapses driving the $i$th subunit
* $\alpha_i$ - weight of the $i$th subunit
* $s(n)$ - subunit response function, best characterized by the sigmoid function:

$$s(n) = \frac{1}{1 + e^{(3.6 - n) / 2}} + 0.30n + 0.0114 n^2$$

### Two Layer Model (Mel, 2007)

Similar to the two layer neural network,
this model treats pyramidal neurons as cells composed of two layers.
The first layer is composed of many individual subunits (the dendrites),
in which a set of terms is calculated based on the input vector.
These terms are then summed up in the second layer,
giving the cells overall sub threshold activity level.

Overall activity level is defined as:

$$a(x) = \sum u_i s(x, w_i)$$

where

* $x$: input
* $w_i$: parameters for the $i$th subunit
* $u_i$: weight of the $i$th subunit
* $s$: subunit onlinearity (product of inputs or sigmoid function of inputs)

In addition, an output nonlinearity $g$ may be applied to $a(x)$,
giving $y = g(a)$.
While this model is more realistic than a point neuron,
it only characterizes subthreshold activity,
and is therefore not useful when analyzing spiking behaviour.

### Three Layer Network (Mel, 2007)

This model is nearly identical to the two layer model,
however now the Apical Tuft is being taken into consideration.
The Apical Tuft serves as a third layer of computation
which calculates a gain factor that is transmitted to the soma.
This gain factor is simply a multiplier to the somatic output
calculated in the Two Layer Model.
At the Apical Tuft Itself,
dendritic branches calculate a sigmoid function of their inputs,
acting much like the typical dendritic subunits of the Two Layer Model.
These responses are then summed at an integrating center,
and converted into a gain factor, which is then transmitted to the soma.

### Clusteron Model (Mel, 2007)

This model came about from studies showing that the 
largest postsynaptic response in a pyramidal cell occured when activated
synapses were all located within clusters of an intermediate size. In the
model, these clusters are treated as neuron-like subunits called clusterons.
Each synapse has a region of distance $D$ centered over it. If two synapses are
activated, and the distance between them is less than $D/2$, then they are
considered to be in the same subunit, and a multiplicative interaction occurs
between the two of them. In particular, consider an input $x_j$ with a region of
$D_j$ surrounding it.

On its own, the response of the region $D_j$ would be

$$a_j = w_j x_j$$

where $w_j$ is the weight of the synapse.

Now, consider another region $D_i$, with 3 inputs.
If the inputs from $D_i$ are separated from the input $x_j$ by a
distance of less than $D_j / 2$, then the inputs are considered to be a part of the
same subunit, and a multiplicative interaction occurs between the two of them.
In particular, the response of subunit $j$ is now

$$a_j = w_j x_j(\sum_i \epsilon D_j w_i x_i)$$

where $w_i$ is the weight of synapse $i$,
and $x_i$ is the input at that synapse.
At the cell body, inputs from all subunits are added together, and a global output
nonlinearity is applied. Therefore, the overall response of the cell is
$y = g(\sum-j a_j)$

A major drawback to this model is that it only considers excitatory
inputs, and does not take into consideration spatial characteristics of the
branching dendritic tree.

## Coincidence Detection (Stuart and Hausser, 2001)

Coincidence detection is believed to be important in the induction of synaptic
plasticity and long term potentiation (LTP). Following a somatic action
potential, a Back Propagating Action Potential (BPAP) sends a wave of
depolarization towards the distal dendrites of the cell. If the BPAP reaches
the dendrite at the same time as an EPSP is induced (or slightly before), the
depolarization caused by the BPAP and the EPSP becomes much greater than their
expected linear sum. This depolarization is mediated by dendritic sodium
channels which open when EPSP's bring the dendritic membrane potential into a
range where a BPAP will cause a threshold to be crossed.This wave of
depolarization can then travel back to the soma, and while it will not affect
the initial action potential amplitude, it causes a large afterdepolarization
which may induce the soma to fire another action potential (leading to burst
firing). The time window between the arrival of a BPAP and the EPSP for
coincidence detection to occur appears to be similar to the time window
between pre and post synaptic neuron firing in the induction of LTP (the
strengthening of a synapse when pre and postsynaptic neurons fire
simultaneously). This implies that coincidence detection may be important in
LTP, synaptic plasticity, and long term memory.

Useful coincidence detection data:

* EPSP must occur simultaneously with, or less than 10 - 15 ms
  before somatic action potential for coincidence detection to occur.
* Maximal amplification of BPAP occurs when EPSP occurs less than 3 ms
  before a somatic action potential.
*  BPAP amplification was only observed at dendritic distances greater than 450 μm.

## Glossary

* BPAP: Back Propagating Action Potential
* EPSP: Excitatory Post Synaptic Potential
* LTD: Long Term Depression
* LTP: Long Term Potentiation
* Threshold Potential: A threshold voltage for superlinear summation on individual dendrites.
  This threshold potential is measured at the soma,
  and is defined as the somatic potential at which the combined response exceeds
  the expected linear prediction by 25%. (Polsky et al.,2004)

## Primary Sources

* Gasparini, S., Migliore, M., and Magee., J.C. (2004). On the Initiation and Propagation of Dendritic Spikes in CA1 Pyramidal Neurons. The Journal of Neuroscience, 24(49):11046-11056.
* Marenco, L.N., Crasto, C., Nadkami, P.M., Miller, P.L., Shepherd, G.M. (2009). Neuron Database - HOME PAGE. Center for Medical Informatics: Section of Neurobiology. Yale University School of Medicine. <http://senselab.med.yale.edu/neurondb/default.asp>
* Megias, M., Emri, ZS., Freund, T.F., and Guly, A. i. (2001) Total number and distribution of inhibitory and excitatory synapses on hippocampal CA1 pyramidal cells. Neuroscience, 102, 3:527-540.
* Mel, B.W. (2007). Why Have Dendrites? A Computational Perspective. Deparment of Biomedical Engineering. University of Southern Californa. Los Angeles, California
* Poirazi, P., Brannon, T., and Mel, B.W. (2003). Pyramidal Neuron as Two-Layer Neural Network. Neuron, 37, 989-999.
* Polsky, A., Mel, B.W., and Schiller, J. (2004). Computational subunits in thin dendrites of pyramidal cells. Nature neuroscience, 7, 6:621-627.
* Spruston, N. (2008). Pyramidal neurons: dendritic structure and synaptic integration. Nature neuroscience reviews. 9:206-221.
* Stuart G.J., and Hausser, M. (2001). Coincidence Detection of EPSPS and Action Potentials. Nature Vol 4. 1:63-71

## Secondary Sources

## Potential Sources

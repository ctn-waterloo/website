title: What do we mean by 'whole brain' modelling?

### Introduction

For various practical reasons, most people choose a brain subsystem (or often
function) in order to build a model. This has the advantage of being doable,
but the disadvantage of considering component parts in isolation from the
entire system (which usually leads to mischaracterizing the part -- often
seriously). An excellent book on how to decompose & analyze complex systems is
Bechtel & Richardson's Discovering Complexity. I won't repeat their arguments
here, but the speak to the importance of 'reintegrating' a system (i.e.
synthesis) after decomposition (i.e. analysis).

Given our commitment to constructing methods that should help build
arbitrarily large, complex models at various levels of neural detail, I think
it is somewhat natural to consider the question of how to integrate all of the
various modelling projects going on in the lab.

Right now, I take the major divisions to be:

### Perception

  * Perceptual integration includes multi-modal integration, as well as including both top-down and bottom-up effects on processing.

  * Perception is hierarchical and recurrent; dimensionality decreases as we progress up the hierarchy

  * Perception attempts to reduce dimensionality by inferring reasonable causal models

### Action

  * Action integration typically means integrating action with perception

  * Action is hierarchical and recurrent; dimensionality increases as we progress down the hierarchy

  * Action attempts to perform optimal control in a hierarchy, where the top of the hierarchy has the most general specification of a motor goal (e.g. goto position x).

### Cognition

  * Cognitive integration means tying cognition to action and perception in appropriate ways. Sometimes this means doing less with the cognitive system (and allowing the other systems to be 'smart').

  * I suspect cognition is abstract perception and action, hence part of the same hierarchies.

### Motivation

  * The Litt et al (2008) paper is our only real foray into this area.

  * It extremely important for us to better understand learning, motivation, etc. I'm thinking mainly of TD-learning types of models (or Q-learning, etc.), which have been usefully mapped to dopamine and serotonin subsystems found in brainstem and basal ganglia.

  * 'Old' valuation systems (midbrain) must be integrated with 'new' evaluation systems (cortex), as in the Litt paper.

### An overall view

(unfinished) * Hierarchies in and out, with linking the two & motivation
guiding resource allocation * Nested (hierarchical) controllers strike me as a
fruitful avenue of understanding integration and neural organization

title: Cognition
picture: http://i.imgur.com/DIDdp7P.jpg
intro: >
    Research into neural mechanisms behind many cognitive phenomena, 
    including working memory, syntactic generalization, structured representations, 
    associative memory, and more.
people:
    - Daniel Rasmussen
toc:
    - Cognitive Robotics
    - Large-scale neural and cognitive simulation
    - Modelling problem solving in Raven's Progressive Matrices
    - - Demo
      - Project Status
      - Results
    - Neural Cognitive Architecture
    - Symbolic Reasoning in Spiking Neurons

We have done work on [working memory](?q=taxonomy/term/11), that some may
consider cognitive, but we are now more focused on methods for building
cognitive architectures in general.

As such, we are working on a novel cognitive architecture that combines our
interest in VSAs with the vector processing capabilities of the NEF. [Early
work](236) focused on doing inferential symbolic processing in a biologically
plausible, spiking neural network. This work demonstrates syntactic
generalization (generalizing over syntactic structure despite sensitivity to
semantic information) -- what has often be called a hallmark of cognitive
function.

We have now extended this work significantly in two ways: 1. we are addressing
issues of scalability (which seems to be the major strength of not adopting a
classical architecture); and 2. we are incorporating a [biologically plausible
clean-up memory](15) (a kind of associative memory).

Details of our work on cognitive modelling are forthcoming in a currently
submitted paper. For now you can read this [summary](202), which was written
for a grant application to NSERC.

You can also watch some demonstration videos related to this work, including
[convolution/binding in neurons](229), [a neural production system](230), and
[high-dimensional representation](228)

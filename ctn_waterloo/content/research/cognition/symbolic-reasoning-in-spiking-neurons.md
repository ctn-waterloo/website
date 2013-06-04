title: Symbolic Reasoning in Spiking Neurons

  * Talk and paper presented at the 32nd Annual Meeting of the Cognitive Science Society (CogSci 2010)
    * by Terrence C. Stewart, Xuan Choo, and Chris Eliasmith; Centre for Theoretical Neuroscience, University of Waterloo
    * Slides available in [[pdf](f/2010-SymbolicReasoning-talk.pdf)] and [[odp](f/2010-SymbolicReasoning-talk.odp)]

## Goal

  * To create a neural cognitive architecture
    * that is biologically realistic
      * (spiking neurons, anatomical constraints, neural parameters, etc.)
    * and supports high-level cognition
      * (symbol manipulation, cognitive control, etc.)
  * Advantages
    * Connect cognitive theory to neural data
    * Neural implementation imposes constraints on theory

## Required Components

  * Representation
    * Distributed representation of high-dimensional vectors
  * Transformation
    * Manipulate and combine representations
  * Memory
    * Store representations over time
  * Control
    * Apply the right operations at the right time

## Representation

  * Assumption: Cognition uses high-dimensional vectors for representation
    * [2,4,-3,7,0,2,...]
  * Forms the top level of many hierarchical object recognition models
  * The vector is compressed information
  * Different vectors for each thing that can be represented
    * including DOG, CAT, SQUARE, TRIANGLE, RED, BLUE, SENTENCE, etc.

## How can a group of neurons represent vectors?

  * We know how this happens in visual and motor cortex
    * (e.g. Georgopoulos et al., 1986)
  * Representing a spatial (x,y) location (2-dimensional vector)
    * Distributed representation
    * Each neuron has a preferred direction
      * One direction it fires most strongly for
      * Uniformly distributed around the circle

You do not have the latest version of Flash installed. Please visit this link
to download it: [http://www.adobe.com/products/flashplayer/](http://www.adobe.
com/products/flashplayer/)

[[avi](f/v/2dencode.avi)]

  * Neural representation
    * Using Leaky Integrate-and-Fire (LIF) neurons
    * Input current is the dot product of the represented vector with the preferred vector times the neuron gain (randomly chosen) plus a constant bias current (randomly chosen)
  * How good is this representations?

    * We know how to go from vector to spikes
    * Can we go the other way around?
    * Use the post-synaptic current to recover the original vector
  * Linear decoding

    * Take a weighted sum of neuron outputs to approximate the original input
    * Need decoding weights for optimal estimate
    * (see Eliasmith & Anderson, 2003 for calculations)
    * Extends to higher dimensions
      * Forms the basis of the Neural Engineering Framework
      * Decrease error by increasing number of neurons
      * Distributed representation
      * Robust to noise, neuron loss

You do not have the latest version of Flash installed. Please visit this link
to download it: [http://www.adobe.com/products/flashplayer/](http://www.adobe.
com/products/flashplayer/)

[[avi](f/v/2ddecode.avi)]

## Transformation

You do not have the latest version of Flash installed. Please visit this link
to download it: [http://www.adobe.com/products/flashplayer/](http://www.adobe.
com/products/flashplayer/)

[[avi](f/v/communicate.avi)]

You do not have the latest version of Flash installed. Please visit this link
to download it: [http://www.adobe.com/products/flashplayer/](http://www.adobe.
com/products/flashplayer/)

[[avi](f/v/convolve1.avi)]

You do not have the latest version of Flash installed. Please visit this link
to download it: [http://www.adobe.com/products/flashplayer/](http://www.adobe.
com/products/flashplayer/)

[[avi](f/v/convolve2.avi)]

## Memory

## Control

## Sequential Action

## Information Routing

## Question Answering

## Results

## Conclusions

title: Nengo 2.0 released
author: Trevor Bekolay
date: 2015-01-19 09:00

The [Nengo team](https://github.com/nengo/nengo/blob/master/CONTRIBUTORS.rst)
is pleased to announce the release of Nengo 2.0,
a Python library for building and simulating
large-scale neural models.
Nengo can create sophisticated neural simulations
with sensible defaults in few lines of code,
yet is extensible and flexible enough to
use spiking and non-spiking neuron types
in the same model, get input directly
from hardware, drive robots,
and simulate models on diverse computing resources.

This is the first release of Nengo that is implemented
entirely in Python, and integrates
well with tools like Matplotlib and IPython.
Currently, it is designed to be used programmatically,
but a browser-based graphical interface is under active development.

### Features

Nengo has support for models using the following neuron types,
which can be combined in the same model.

- Rectified linear
- Sigmoid
- Leaky integrate-and-fire (spiking and non-spiking)
- Adaptive leaky integrate-and-fire (spiking and non-spiking)
- Izhikevich
- Direct mode (in which mathematical functions are computed directly, rather than approximated from neural activity)

Nengo does not require online learning
in the form of synaptic weight changes;
however, learning rules do exist for situations when
the objective function is not known ahead of time.
Nengo has support for the following learning rules:

- PES rule (minimizes an error signal)
- BCM rule
- Oja rule

See the documentation and example models
for

### Changes in Nengo 2.0

Nengo 2.0 is a completely new code base
that implements all commonly used features
of [Nengo 1.4](http://nengo.ca/).

### Links

- [Install from PyPI](https://pypi.python.org/pypi/nengo)
- [Source on Github](https://github.com/nengo/nengo)
- [Documentation](https://pythonhosted.org/nengo)
- [Example models](https://pythonhosted.org/nengo/examples.html)

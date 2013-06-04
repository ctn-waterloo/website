title: Whole brain simulation

The NEF methods are really ideal for doing extremely large scale neural simulations.  Here are several reasons why:

1. Ability to swap single cell models of arbitrary precision
2. Ability to analytically determine population connectivity
3. Ability to add/remove learning as desired
4. Ability to abstract over spiking neurons (to rate neurons)
5. Ability to abstract over rate neurons (to populations)
6. Ability to abstract over populations (to control models)
7. Ability to abstract over inhibitory/excitatory connections

It might make something of a technical splash to run a simulation of 100 million neurons that actually do something (as opposed to the splash made by Izchevich which just ran that size of network).

To summarize, we have very adjustable simulation scales, which can be exploited by many people other than us.  As well, the simulation scales can be adjusted independently for different parts of the model.  People really don't know how to do this in general.  There is a big desire to extract computational principles from brain models.  There is also a converse but equally large desire to make large models highly detailed so as to compare them to neural data.  The NEF provides a smooth means of doing both.

title: Neural Production System

Part of our ongoing research involves implementing symbolic rule-following in
neurons. This would form a neural implementation of a production system, which
is a common component of many cognitive architectures. For a full paper on
this model, see [here](http://terrystewart.ca/sites/default/files/2009-50Milli
seconds_final.pdf). In this demonstration, the large neural group represents
the current state (the buffers in ACT-R terms). The five neural groups below
it represent five different productions. Each production has a particular
state it should be applied in. When this state occurs, these neurons begin to
fire. When the neurons fire, they in turn affect the buffer state, changing
it. These five productions are configured to each change the state in a cycle:
p1->p2->p3->p4->p5->p1->etc. The only external input to this model is an
initial current to set the buffer to initially hold the first state. After
that, all changes are due to the synaptic connections between the shown
neurons. The synaptic connections are simulated GABAA connections, which have
a synaptic time constant of ~10ms. It is this timing which governs the speed
of the cycling between states. In this model, the average time to transition
between states is 46.6ms, very close to the 50ms generally assumed.

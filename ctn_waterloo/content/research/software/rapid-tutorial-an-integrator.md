title: Rapid tutorial - An integrator

In this tutorial, you will construct a neural integrator. This is a circuit
that uses feedback to maintain its own state, functioning as a memory.

1. Open the partially completed integrator

  * Goto **File->open from file** and select [partial neural integrator.nef](?q=system/files/partial+neural+integrator.nef_.zip).

2. Connect the network

![](?q=system/files/rapidIntegrator1.png)

  * The basic components of the network have been constructed for you. Connecting these components tells the system to compute the necessary synaptic connection weights to optimally realize the desired function.
  * Connect the **origin** of the **input** to the termination called **input** of the **integrator**
  * Connect the **X** origin of the **integrator** to its own **feedback** termination.

3. Run the network

  * Right-click on the background in the Network Viewer and select **Interactive plots**. 
  * Click the **play** button (in the bottom-right corner). The grey squares show the firing rates of the neurons.
  * The first second of input is defined for you. Press **reset** (the arrow in the bottom left) to repeat this sequence. The network will compute the integral of this input over time.
  * Move the slider to provide your own input. Set it to a large number. Notice that the network integrates this value up to a certain point, but then can go no higher. This is because the neurons have saturated: they are firing as fast as they can. Every group of neurons has a particular range over which they are optimized to represent. Moving outside of this range results in saturation.

4. Adjust the network

  * Return to the black **Network Viewer** screen.
  * To make the system into a low-pass filter (leaky integrator), do the following: 
    * Right-click the **feedback** termination on the **integrator** population and select **configure**. 
    * At the bottom, double-click **transform**, double-click the value (1.0) and set to a smaller value (e.g. 0.9). The smaller the value, the 'leakier' the integrator will be. Click **Save** and **Done**. 
    * Return to the **Interactive plots** and click **reset** and **play** to view the results.
  * In the **Network Viewer** screen, disconnect the **feedback** connection. This will eliminate the recurrent connections which allows the network to have a memory. Return to the **Interactive plots** and examine the results. Now when you move the controller between extremes, the output is merely a scaled version of the input.



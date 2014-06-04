title: Rapid tutorial - Nonlinear transformations

In this tutorial, you will connect groups of neurons to create a system that
can multiply two numbers together. You will then modify this network to
compute a new function.

1. Open the partially completed multiplication network

  * Go to **File->Open from file** and select [partial multiplication.nef](/files/partial multiplication.nef.zip).

2. Connect the network

![](/files/rapidMulti1.png)

  * The basic components of the network have been constructed for you. Connecting components tells the system to compute the necessary synaptic connection weights to optimally realize the desired function.
  * Connect **input 1** and **input 2** to the inputs for neural ensembles **A** and **B**.
  * Connect **A** and **B** to the two inputs of **H**.
  * Connect the **product** output of **H** to the input of **Z**.

3. Run the network

  * Right-click on the background in the Network Viewer and select **Interactive plots**.
  * Click the **play** button (in the bottom-right corner). The grey squares show the firing rates of the neurons.
  * The graph displays the decoded output of the network. This should be approximately 40, since the input sliders are currently set to 8 and 5.
  * Move the sliders up and down to adjust this input. The output will change accordingly.

4. Change the function being computed

  * Close the Interactive Plots window.
  * Right-click on the **H** population and select **Add decoded origin**. Change the name to `my function` and click **Set functions** (dimension should be 1). Select **user-defined function** from the drop down and click **set**.
  * Type in a new function. Try `x0*x0+cos(x1)`. You can also use your own function, but the neurons in this example are only optimized for representing values between -100 and 100. Click OK three times.
  * Disconnect the **product** projection from **H** to **Z** and connect the new origin called **my function** in its place. 
  * Right-click on the Network Viewer and select **Interactive plots**. 
  * Adjust the sliders to confirm that the new function is being calculated.
  * To compare the behaviour of neurons to the ideal calculation of this function, we can switch simulation modes. Click on the down-arrow at the bottom of the interactive plots. Change the **mode** from **default** to **direct**. This will bypass the neurons, producing an exact result.



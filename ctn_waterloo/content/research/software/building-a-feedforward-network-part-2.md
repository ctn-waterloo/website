title: Building a feedforward network (part 2)

This tutorial assumes you've completed [Building a feedforward network (part
1)](?q=node/591).

## Scaling the input signal

1. Right-click on the **input** to the **B** population and select
**Configure**.

2. At the bottom of this panel double-click **transform**. This is the weight
you set to 1 when constructing the termination. Change this value to `0.5` to
scale the input down to half its original value.

3. Re-run the simulation (or go to **interactive plots**), and see that
changing this value scales the input as expected.

## Combining inputs linearly

![](/files/p2-20.png) To add two values, you must create another
termination on the **B** population and project to it as well. Before doing
this, set the **A** to **B** transformation back to 1.

1. Create a termination on the **B** population called `input 2` with weight
`1`.

2. Create a new ensemble **C**.

3. Create a projection from **C**'s **X** origin to **input 2** by dragging.

4. Create a new constant **Function input** and set its value to `-0.7`.

  * Add an input termination on **C** and connect the **Function input** to the **C** ensemble.
  * Add a probe to the new **Function input**.
  * Run the simulation and plot the values for the three probes ![](/files/p2-21.png)
  * The **X** value for the **B** probe should indicate the result of `0.5-0.7=-0.2` (A+C=B). Note: This looks noisier than before because of the scale of the plot.

## Congratulations, you can build linear brains!

You can now compute any linear transformation in a neural circuit. Exactly the
same steps as above can be followed for vector representations, where the
transformation weight becomes a matrix. For more on vector representation, see
the [motor cortex](?q=node/595) tutorial.

## Nonlinear transformations

Of course, nonlinearities are essential for interesting computation. We begin
with simple examples here before moving on to more interesting examples in
part 3.

1. Revert the simulation to a communication channel

  * Right-click on the **C** population and select **remove model**. Answer **Yes** to delete the population.
  * Do the same to the the second **Function input** and the **input 2** termination on the **B** population (right-click just on the termination).

2. Define the nonlinear function you want to compute

  * For one-dimensional ensembles, we can calculate arbitrary 1-dimensional functions (e.g. f(x)=x2, f(x)=θ(x) (thresholding); f(x)=√x, etc.).
  * To perform a non-linear operation, we need to define a new origin. Right-click on the **B** ensemble and select **Add decoded origin**. Set the name to `square` and dimension to `1`. 
  * Click on **Set Functions**, select **User-defined Function** and press **Set**.
  * For the Expression, enter `x0*x0`. We refer to the represented value as `x0`. When when have vectors the values are `x0`, `x1`, `x2`, etc. Press **Ok**, **Ok**, and **Ok**.

3. Collect data from the new output

  * Add a probe for the new origin by right-clicking on the ensemble and selecting **Add probe->square - Function of NEFEnsemble state**

4. Set the input function to something useful

  * Click on the input function that is currently a constant value. You can change this in two ways, through the configure panel or the script console. Let's do the second for variety. ![](/files/p3-9d.png)
  * Open the **Script Console** from the menu bar (under **View**).
  * With the function input selected type the following in the console:

` that.functions=[InterpolatedFunction([0,1],[-1,1])] `

  * This creates an input that starts at -1 and grows linearly to 1

5. Run the model and view the probe data. The output of the network will
approximate x2. Note that there is an initial start-up transient in the graph
(shown above). You can also use the **Interactive plots** to manually control
the input. See the [interactive plots reference sheet](?q=node/594).



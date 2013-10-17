title: Motor Control
picture: http://compneuro.uwaterloo.ca/files/9Muscle3LinkArmPic.png
intro: Developing a biologically plausible framework for models of neural control of movement.
people:
    - Travis DeWolf
toc:
    - 2 link arm models
    - 3 link arm model
    - 6-muscle 3-link arm model
    - 9-muscle 3-link arm model
    - Neural integrator learning demo

<!--[Relevant publications]() from the lab on motor control.-->

As part of the research in our lab we are looking at biological mappings of a hierarchical optimal control framework behind motor control in the brain. Travis DeWolf has been working on developing a biologically plausible framework for models of neural control of movement, to read an abbreviated description of this model, please click here: [NOCH framework](http://compneuro.uwaterloo.ca/files/NOCH-1.pdf).

Recent work in the lab has focused on the development of operational space control and adaptive control models implemented in neurons.

To read more about motor control discussion you can check out related [motor control blog posts](http://studywolf.wordpress.com/category/motor-control/).

## **Motor Control Projects**

### **Arm models**

As part of building models of the motor control system it was necessary to develop simulations with realistic dynamics to control. Simpler one and two link arm models are common, and easy to find online, but more complicated models quickly become much more complicated to develop. The models here were developed with MapleSim, and they can be accessed both from Python and Matlab.

[1 link arm models](motor-control/1-link-arm-models.html)

[2 link arm models](motor-control/2-link-arm-models.html)

[3 link arm models](motor-control/3-link-arm-models.html)

[6 muscle 3 link arm model](motor-control/6-muscle-3-link-arm-model.html)

[9 muscle 3 link arm model](motor-control/9-muscle-3-link-arm-model.html)

### **Controllers**

#### **Operational space controllers**

Controllers based on the operational space control framework by Dr. Oussama Khatib, presented in [this paper](http://cs.stanford.edu/groups/manips/images/pdfs/Khatib_1987_IJRA.pdf). An introduction to OSC can be found in [this tutorial](http://www.stanford.edu/~smenon/code/rppbot/MathTutorial_01_RPPBot.htm) by Samir Menon. 

For more discussion and slower walk through of the development of OSControllers you can check out [related OSC blog posts](http://studywolf.wordpress.com/category/robotics/).

[1 link arm operational space controllers](motor-control/1-link-arm-osc-controllers.html)

[2 link arm operational space controllers](motor-control/2-link-arm-osc-controllers.html)

<!--#### **Adaptive controllers**

Adaptive controllers that are able to learn the dynamics and kinematics of the system being controlled

[2 link arm adaptive controllers](motor-control/2-link-arm-adaptive-controllers.html)-->

If you have any questions or comments, please email
[Travis DeWolf](http://compneuro.uwaterloo.ca/people/travis-dewolf.html).

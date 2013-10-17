title: 2 link arm models

Here are links to some of the different arm models that we've been working with, in both Python and Matlab.

####Python simulations

Here is Python code that simulates a simple 2 link arm model.
There is Python only code (arm_python.py), and a simulation generated from MapleSim and compiled down to some highly optimized C code (arm.py). To use the MapleSim simulator, download the folder and run 
"python setup.py build_ext -i". 

<img scr="http://compneuro.uwaterloo.ca/files/2linkarm.png">

[2 Link Arm Python code](https://github.com/studywolf/blog/tree/master/OSC/Arms/TwoLinkArm)


####Matlab simulations
Here is Matlab code that simulates a simple arm model.
To add forces to the arm, you can use the keys 'q' and 'w' for the shoulder and 'o' and 'p' for the elbow.
Should be able to just paste and run this in recent Matlab versions.

<img scr="http://compneuro.uwaterloo.ca/files/2linkarmmatlab.png">

[2 Link Arm Matlab code](http://compneuro.uwaterloo.ca/files/2linkarm-matlabcode.m)

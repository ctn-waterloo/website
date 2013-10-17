title: 3-link arm models

Here are links to some of the different arm models that we've been working with, in both Python and Matlab. 
This is a 3 link arm model simulation, developed in MapleSim5.  

####Python simulations

Here is Python code that simulates a simple 2 link arm model.
There is Python only code (arm_python.py), and a simulation generated from MapleSim and compiled down to some highly optimized C code (arm.py). 

To use the MapleSim simulator, download the folder and run "python setup.py build_ext -i". 

<img src="http://compneuro.uwaterloo.ca/files/ThreeLinkArm.png" style="width:400px;">

[3 Link Arm Python code](https://github.com/studywolf/blog/tree/master/OSC/Arms/ThreeLinkArm)


####Matlab simulations

All necessary files to run in Matlab are included. The files were compiled for a 64-bit system. To run on a 32-bit system, recompile the model using the modelGen.m file. The model currently only runs on PCs. To run, open the 'run' file and hit 'F5'. The number keys will activate/deactivate muscles, and the letters beneath will reset the activation level to 0. Please contact me (Travis) if you have any questions or would like the corresponding MapleSim files. The
files are open for sharing and modification, but shout outs are appreciated. 

<img src="http://compneuro.uwaterloo.ca/files/3LinkArmmatlab.png" style="width:400px;">

[3 Link Arm Matlab code](http://compneuro.uwaterloo.ca/files/3LinkArm.zip)

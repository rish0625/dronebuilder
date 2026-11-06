*ENAE380 DroneBuilder Project Log*

Goal: Developing a Python-based flight dynamics simulator for multirotor drones, starting with the mathematical and physics-based model rather than the graphical interface. The goal is to create a program where a user can define the physical characteristics of a drone, including its dimensions, mass, motor locations, propeller configuration, and other components. From these inputs, the program would calculate important properties such as the center of mass and moment of inertia tensor, and then use rigid-body dynamics to model the drone's six degrees of freedom.

*Day 1*
* Establishing project structure with a GitHub Repository
* Created a drone simulation folder to hold physics files that determine a potential drones physics characteristics and relative information
* Installed [numpy scipy matplotlib pytest] for this project, to run operations on arrays, vectors, tensors, differential equations, matlab plotting, and testing, all of which are essential to the basic physics and mapping for the drone
* Created some baseline functions for the motor in motor.py, and tested its baseline in the test_motor.py file.

*Day 2*
* Added torque calculations to motor.py
* Created more test criteria to test the motor.py function, criteria includes calculations 
in different scenarios of input
* Wrote a motor_demo display for user to input and test different RPMs and coefficients
* Created a thrust plot file to plot the drones information

*Day 3*
* Created classes in drone.py that holds each of the main components, the overall drone class accounts for some of the external components, and the following classes are particular to each main component (Frame, Motor, Battery, Flight Controller, Propellor, Antenna). I created a final class for the external components, jsut so they are accounted for.
* In mass_properties.py, I created functions to calculate total mass, center of mass, and the inertia tensor. These functions will be used in the drone dynamics that I will work on later.
* Created a test case for the mass_properties file and tested the total mass function.

*Day 4*
* Testing the other two mass_properties.py functions in the test_mass_prop.py file. Center of mass test and moment of inertia test failed because there is no default class, so that is a capability I will add
* Solved the first test case failure by adding extra component values so default case doesn't need to be called.
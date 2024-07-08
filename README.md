# 1D Collision-simulator
Recently I saw a cool video from 3Blue1Brown that assesed the physical phenomenon where in a friction-free and elastic environment, meaning that no energy is lost, the sum of collisions between the object of smaller mass, the object of greater mass and an wall will will have a starting number same as the ciphers of pi. It's quite a cool phenomenon that I still don't quite understand - this project was however an attempt at recreating it on my own with pygame. (Here's the video for anyone interested: https://www.youtube.com/watch?v=jsYwFizhncE)

The physics behind the game is pretty straight forward. It's based on the formulas from elastic collision theory that claim 1) that for a collision of two objects in an elastic environment, the collective amount kinetic energy of the two objects will remain the same before and after the collision (this is given the condition that no energy will be lost). The other law describes that (m_1*v*1)*(m_2*v_*2) = (m_1*v_1')+(m_2*v_2'), where m = mass, v = initial velocity and v' is final velocity (post-collision). When colving for the final velocities in the program, numpy is used to compute the linear algebra problem of two equations with two variables.

To play the difference collision animations just press 1-5, where the objects will have masses of:
1) 1 : 1 kg 
2) 1 : 100 kg
3) 1 : 10.000 kg
4) 1 : 100.000 kg
5) 1 : 1.000.000 kg

On the top left corner, I've included a collision counter to keep track of the pi phenomenon as mentioned earlier. 

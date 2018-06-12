import numpy as np
import math as mt
import matplotlib.pyplot as plt

x = []
y = []

PI = 3.141

angle = 0.0
theta = 0

ref = []
temp_x = 0.0
temp_y = 0.0
x_step = 0.0

for _ in range(0,3000):
	# temp_y = mt.sin(mt.radians(2*theta/15)) + mt.cos(mt.radians(2*theta/15))-1
	temp_y  = 10 + 2.0*mt.sin(theta*PI/6) + 2.0*mt.cos(theta*PI/6) -2 
	temp_x = theta
	theta += 1.0/100
	x_step = x_step + 0.01
	x.append(temp_x)
	y.append(temp_y)
	# print("x = ",'{:.3f}'.format(temp_x),   "y = ", '{:.3f}'.format(temp_y))




fig,ax = plt.subplots(nrows=1,ncols=1)

ax.plot(x,y,'b',label='predictions')
plt.show()


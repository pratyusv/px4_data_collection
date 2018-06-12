#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/scripts/data/states/"
state = np.load(data_dir + 's_x_cos_y.npy')
# print(state.shape)

vx = []
vy = []
vz = []

for row in range(state.shape[0]):
	vx.append(state[row,3])
	vy.append(state[row,4])
	vz.append(state[row,5])



fig, ax = plt.subplots(nrows=3, ncols=1)
# ax[0].set_title('Velocity')
ax[0].plot(vx, 'b')
ax[1].plot(vy, 'r')
ax[2].plot(vx, 'g')

plt.show()
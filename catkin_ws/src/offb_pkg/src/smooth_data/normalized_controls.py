#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np


s_data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/controls/"
control    = np.load(s_data_dir	+ "u_x_cos_y.npy")



min_val_X = []
max_val_X = []

for col in xrange(0,control.shape[1]):
	print('col : ',col, 'min = ','{:.5f}'.format(np.amin(control[:,col])), ' max =', '{:.5f}'.format(np.amax(control[:,col])))
	min_val_X.append(np.amin(control[:,col]))
	max_val_X.append(np.amax(control[:,col]))
	control[:, col] = (control[:,col] - np.amin(control[:,col]))/( np.amax(control[:,col]) -  np.amin(control[:,col]))



control = control*10

size = control.shape[0]


s_u0 = []
s_u1 = []
s_u2 = []
s_u3 = []

for row in range(0,size):

	s_u0.append(control[row,0])
	s_u1.append(control[row,1])
	s_u2.append(control[row,2])
	s_u3.append(control[row,3])





# Controls
fig1, ax1 = plt.subplots(nrows=4,ncols=1)
ax1[0].set_title('Velocity')
ax1[0].plot(s_u0,'r')
ax1[1].plot(s_u1,'r')
ax1[2].plot(s_u2,'r')
ax1[3].plot(s_u3,'r')






plt.show()

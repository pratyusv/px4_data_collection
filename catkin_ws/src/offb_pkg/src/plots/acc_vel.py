#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt


data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/scripts/data/"


vel = np.load(data_dir + 'states/s_rand_x_y.npy')
acc = np.load(data_dir + 'nn2/nn2_rand_x_y_grd_truth.npy')


s_vx = []
s_vy = []
s_vz = []


a_vx = []
a_vy = []
a_vz = []



for row in range(1,vel.shape[0]-1):

	s_vx.append(vel[row,12])
	s_vy.append(vel[row,13])
	s_vz.append(vel[row,14])

	a_vx.append((acc[row,0]* 0.02) + vel[row-1,12])
	a_vy.append((acc[row,1]* 0.02) + vel[row-1,13])
	a_vz.append((acc[row,2]* 0.02) + vel[row-1,14])

	# a_vx.append(vel[row-1,12])
	# a_vy.append(vel[row-1,13])
	# a_vz.append(vel[row-1,14])


sum_ = 0.0
for r in range(0,len(s_vx)):
	sum_ +=  np.abs(np.abs(s_vx[r]) - np.abs(a_vx[r]))


print(sum_)


fig,ax = plt.subplots(nrows=3,ncols=1)

ax[0].plot(s_vx,'b')
ax[0].plot(a_vx,'r')

ax[1].plot(s_vy,'b')
ax[1].plot(a_vy,'r')


ax[2].plot(s_vz,'b')
ax[2].plot(a_vz,'r')


plt.show()
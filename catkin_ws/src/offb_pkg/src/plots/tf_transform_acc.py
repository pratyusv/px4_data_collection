#!/usr/bin/python

import numpy as np
import math
import matplotlib.pyplot as plt

data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/scripts/data/"

acceleration = np.load(data_dir + 'acc/a_rand_x_neg_y.npy')
state     = np.load(data_dir + 'states/s_rand_x_neg_y.npy')

def tf_acceleration(euler_angles,acc):
	phi = euler_angles[0]
	theta = euler_angles[1]
	psi = euler_angles[2]

	R_hat = np.array([[1, math.sin(phi)* math.tan(theta), math.cos(phi)*math.tan(theta)],
			[0, math.cos(phi), -1*math.sin(phi)],
			[0, float(math.sin(phi)/math.cos(theta)), float(math.cos(phi)/ math.cos(theta)) ]])

	o = np.matmul(R_hat, acc)
	# print(o.shape)
	return o

# state = np.concatenate((state[:,0:6], state[:,12:18]),axis=1)

meas_ax = []
meas_ay = []
meas_az = []

calc_ax = []
calc_ay = []
calc_az = []


size = state.shape[0]
delta_t = 0.02
# size = 100
for row in xrange(0,size-1):
	calc_ax.append((state[row+1,3] - state[row,3])/delta_t)
	calc_ay.append((state[row+1,4] - state[row,4])/delta_t)
	calc_az.append((state[row+1,5] - state[row,5])/delta_t)


for row in xrange(0,size):
	temp = tf_acceleration(state[row,15:18], acceleration[row,0:3])
	meas_ax.append(temp[0])
	meas_ay.append(temp[1])
	meas_az.append(temp[2] - 9.8)

	# meas_ax.append(acceleration[row,0])
	# meas_ay.append(acceleration[row,1])
	# meas_az.append(acceleration[row,2])




fig,ax = plt.subplots(nrows=2,ncols=3)

ax[0][0].plot(meas_ax,'b',label='grnd_truth')
ax[0][0].plot(calc_ax,'r',label='predictions')


ax[0][1].plot(meas_ay,'b',label='grnd_truth')
ax[0][1].plot(calc_ay,'r',label='predictions')

ax[0][2].plot(calc_az,'r',label='predictions')
ax[0][2].plot(meas_az,'b',label='grnd_truth')

ax[1][0].plot(meas_ax,'b',label='grnd_truth')
ax[1][1].plot(meas_ay,'b',label='grnd_truth')
ax[1][2].plot(meas_az,'b',label='grnd_truth')




plt.show()
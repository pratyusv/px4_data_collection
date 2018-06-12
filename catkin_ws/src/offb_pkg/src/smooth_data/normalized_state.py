#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np


s_data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/states/"
s_state    = np.load(s_data_dir	+ "s_x_cos_y.npy")



min_val_X = []
max_val_X = []

for col in xrange(0,s_state.shape[1]):
	print('col : ',col, 'min = ','{:.5f}'.format(np.amin(s_state[:,col])), ' max =', '{:.5f}'.format(np.amax(s_state[:,col])))
	min_val_X.append(np.amin(s_state[:,col]))
	max_val_X.append(np.amax(s_state[:,col]))
	s_state[:, col] = (s_state[:,col] - np.amin(s_state[:,col]))/( np.amax(s_state[:,col]) -  np.amin(s_state[:,col]))



s_state = s_state*10

size = s_state.shape[0]

x = []
y = []
z = []

vx = []
vy = []
vz = []

phi = []
theta = []
psi = []

sin_phi = []
sin_theta = []
sin_psi = []

cos_phi = []
cos_theta = []
cos_psi = []

rs = []
ps = []
ys = []

s_x = []
s_y = []
s_z = []

s_vx = []
s_vy = []
s_vz = []

s_phi = []
s_theta = []
s_psi = []

s_sin_phi = []
s_sin_theta = []
s_sin_psi = []

s_cos_phi = []
s_cos_theta = []
s_cos_psi = []

s_rs = []
s_ps = []
s_ys = []

for row in range(0,size):

	s_x.append(s_state[row,0])
	s_y.append(s_state[row,1])
	s_z.append(s_state[row,2])


	s_vx.append(s_state[row,3] )
	s_vy.append(s_state[row,4])
	s_vz.append(s_state[row,5])

	s_sin_phi.append(s_state[row,6])
	s_sin_theta.append(s_state[row,7])
	s_sin_psi.append(s_state[row,8])

	s_cos_phi.append(s_state[row,9])
	s_cos_theta.append(s_state[row,10])
	s_cos_psi.append(s_state[row,11])

	s_rs.append(s_state[row,12] )
	s_ps.append(s_state[row,13] )
	s_ys.append(s_state[row,14] )

	s_phi.append(s_state[row,15] )
	s_theta.append(s_state[row,16])
	s_psi.append(s_state[row,17])



# ## Position
# fig1, ax1 = plt.subplots(nrows=3,ncols=1)
# ax1[0].set_title('Position')
# ax1[0].plot(s_x,'r')
# ax1[0].plot(x,'b')
# ax1[1].plot(s_y,'r')
# ax1[1].plot(y,'b')
# ax1[2].plot(s_z,'r')
# ax1[2].plot(z,'b')


# Velocity
fig1, ax1 = plt.subplots(nrows=3,ncols=1)
ax1[0].set_title('Velocity')
ax1[0].plot(vx,'b')
ax1[0].plot(s_vx,'r')
ax1[1].plot(vy,'b')
ax1[1].plot(s_vy,'r')
ax1[2].plot(vz,'b')
ax1[2].plot(s_vz,'r')


# ## SIN
# fig1, ax1 = plt.subplots(nrows=3,ncols=1)
# ax1[0].set_title('Sin')
# ax1[0].plot(s_sin_phi,'r')
# ax1[0].plot(sin_phi,'b')
# ax1[1].plot(s_sin_theta,'r')
# ax1[1].plot(sin_theta,'b')
# ax1[2].plot(s_sin_psi,'r')
# ax1[2].plot(sin_psi,'b')



# ## COS
# fig1, ax1 = plt.subplots(nrows=3,ncols=1)
# ax1[0].set_title('cos')
# ax1[0].plot(s_cos_phi,'r')
# ax1[0].plot(cos_phi,'b')
# ax1[1].plot(s_cos_theta,'r')
# ax1[1].plot(cos_theta,'b')
# ax1[2].plot(s_cos_psi,'r')
# ax1[2].plot(cos_psi,'b')


## Omega
# fig1, ax1 = plt.subplots(nrows=3,ncols=1)
# ax1[0].set_title('Angular Velocity')
# ax1[0].plot(rs,'b')
# ax1[0].plot(s_rs,'r')
# ax1[1].plot(ps,'b')
# ax1[1].plot(s_ps,'r')
# ax1[2].plot(ys,'b')
# ax1[2].plot(s_ys,'r')



## Theta
# fig1, ax1 = plt.subplots(nrows=3,ncols=1)
# ax1[0].set_title('Theta')
# ax1[0].plot(s_phi,'r')
# ax1[0].plot(phi,'b')
# ax1[1].plot(theta,'b')
# ax1[1].plot(s_theta,'r')
# ax1[2].plot(psi,'b')
# ax1[2].plot(s_psi,'r')


plt.show()
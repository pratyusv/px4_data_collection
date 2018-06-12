import os,fnmatch
import numpy as np
import matplotlib.pyplot as plt
import math

save_path = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data/states/"

states 	= os.listdir('/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/states/')
control = os.listdir('/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/controls/')
acc 	= os.listdir('/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/acc/')
nn2 	= os.listdir('/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/nn2/')


pattern = "*.npy"

filesName = []

for entry in states:
	if fnmatch.fnmatch(entry,pattern):
		print(entry)
		filesName.append(entry)



# exit()
count = 0
for file in filesName:
	# data_dir = "../next_state/data/states/"
	data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/states/"


	state 	= np.load(data_dir + file )

	size = state.shape[0]
	count += 1

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


	u1 = []
	u2 = []
	u3 = []
	u4 = []

	ac_x = []
	ac_y = []
	ac_z = []


	alpha_x = []
	alpha_y = []
	alpha_z = []


	s_vx = []
	s_vy = []
	s_vz = []

	s_rs = []
	s_ps = []
	s_ys = []

	s_ac_x = []
	s_ac_y = []
	s_ac_z = []


	s_alpha_x = []
	s_alpha_y = []
	s_alpha_z = []


	a = 0.05

	for row in range(0,size):
		x.append(state[row,0])
		y.append(state[row,1])
		z.append(state[row,2])

		vx.append(state[row,3] )
		vy.append(state[row,4])
		vz.append(state[row,5])

		sin_phi.append(state[row,6])
		sin_theta.append(state[row,7])
		sin_psi.append(state[row,8])


		cos_phi.append(state[row,9])
		cos_theta.append(state[row,10])
		cos_psi.append(state[row,11])


		rs.append(state[row,12] )
		ps.append(state[row,13] )
		ys.append(state[row,14] )

		phi.append(state[row,15] )
		theta.append(state[row,16])
		psi.append(state[row,17])

	## Linear velocity
	temp_x = state[0,3]
	temp_y = state[0,4]
	temp_z = state[0,5]
	for row in xrange(0,size):

		temp_x = temp_x + a*(state[row,3] - temp_x)
		temp_y = temp_y + a*(state[row,4] - temp_y)
		temp_z = temp_z + a*(state[row,5] - temp_z)

		s_vx.append( temp_x )
		s_vy.append( temp_y )
		s_vz.append( temp_z )


	## Angular Velocity

	temp_x = 0.0 
	temp_y = 0.0
	temp_z = 0.0

	temp_x = state[0,12]
	temp_y = state[0,13]
	temp_z = state[0,14]
	for row in xrange(0,size):

		temp_x = temp_x + a*(state[row,12] - temp_x)
		temp_y = temp_y + a*(state[row,13] - temp_y)
		temp_z = temp_z + a*(state[row,14] - temp_z)

		s_rs.append( temp_x )
		s_ps.append( temp_y )
		s_ys.append( temp_z )



	s_state = np.array([x,y,z, s_vx, s_vy, s_vz, sin_phi, sin_theta, sin_psi, cos_phi, cos_theta, cos_psi,s_rs, s_ps, s_ys, phi, theta, psi],ndmin=2).transpose()
	print('file name', file , ' shape :' , s_state.shape)
	np.save(save_path + file, s_state)


print(count)
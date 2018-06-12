import os,fnmatch
import numpy as np
import matplotlib.pyplot as plt
import math

save_path = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data/ang_acc/"

ang_acc 	= os.listdir('/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/states/')

pattern = "*.npy"

filesName = []

for entry in ang_acc:
	if fnmatch.fnmatch(entry,pattern):
		# print(entry)
		filesName.append(entry)

# exit()
count = 0
for file in filesName:
	data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/states/"

	state = np.load(data_dir + file )

	size = state.shape[0]
	count += 1

	alpha_x = []
	alpha_y = []
	alpha_z = []

	s_alpha_x = []
	s_alpha_y = []
	s_alpha_z = []

	a = 1
	## Angular Acceleration
	temp_x = state[0, 12]
	temp_y = state[0 ,13]
	temp_z = state[0, 14]

	delta_t = 0.02

	alpha_x.append(state[0, 12])
	alpha_y.append(state[0, 13])
	alpha_z.append(state[0, 14])

	for row in xrange(1,size):

		alpha_x.append((state[row,12] - temp_x )/delta_t)
		alpha_y.append((state[row,13] - temp_y )/delta_t)
		alpha_z.append((state[row,14] - temp_z )/delta_t)

		temp_x = state[row,12]
		temp_y = state[row,13]
		temp_z = state[row,14]


	s_temp_x = alpha_x[0]
	s_temp_y = alpha_y[0]
	s_temp_z = alpha_z[0]

	a = 0.01

	for row in xrange(0,size):
		s_temp_x = s_temp_x + a*(alpha_x[row] - s_temp_x)
		s_temp_y = s_temp_y + a*(alpha_y[row] - s_temp_y)
		s_temp_z = s_temp_z + a*(alpha_z[row] - s_temp_z)

		s_alpha_x.append( s_temp_x )
		s_alpha_y.append( s_temp_y )
		s_alpha_z.append( s_temp_z )		
	

	s_acc = np.array([s_alpha_x, s_alpha_y, s_alpha_z],ndmin=2).transpose()
	file = file.split('_',1)
	# print(file[1])
	file = 'alpha_'+ file[1]
	print('file name', file , ' shape :' , s_acc.shape)
	np.save(save_path + file, s_acc)


print(count)
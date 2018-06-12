import os,fnmatch
import numpy as np
import matplotlib.pyplot as plt
import math

save_path = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/lin_acc/"

acc 	= os.listdir('data/acc/')

pattern = "*.npy"

filesName = []

for entry in acc:
	if fnmatch.fnmatch(entry,pattern):
		print(entry)
		filesName.append(entry)

# exit()
count = 0
for file in filesName:
	data_dir = "../next_state/data/acc/"

	acc = np.load(data_dir + file )

	size = acc.shape[0]
	count += 1

	ac_x = []
	ac_y = []
	ac_z = []

	s_ac_x = []
	s_ac_y = []
	s_ac_z = []


	a = 0.05

	## Linear Acceleration
	temp_x = acc[0,0]
	temp_y = acc[0,1]
	temp_z = acc[0,2]
	for row in xrange(0,size):

		temp_x = temp_x + a*(acc[row,0] - temp_x)
		temp_y = temp_y + a*(acc[row,1] - temp_y)
		temp_z = temp_z + a*(acc[row,2] - temp_z)

		s_ac_x.append( temp_x )
		s_ac_y.append( temp_y )
		s_ac_z.append( temp_z )




	s_acc = np.array([s_ac_x, s_ac_y, s_ac_z],ndmin=2).transpose()
	print('file name', file , ' shape :' , s_acc.shape)
	np.save(save_path + file, s_acc)


print(count)
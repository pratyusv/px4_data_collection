import os,fnmatch
import numpy as np

listOfFiles = os.listdir('./states/')
# print(listOfFiles)

pattern = "*.npy"

filesName = []

# count = 0
for entry in listOfFiles:
	if fnmatch.fnmatch(entry,pattern):
		# print(entry)
		filesName.append(entry)
		# count += 1 





file_dir = './states/'
vel_dir = './vel/'
count = 0
delta_t = 0.05

for file in filesName:
	state = np.load(file_dir + file)
	count += 1
	print('file count :', count, ' State :', file)

	prev_x = 0
	prev_y = 0
	prev_z = 0

	vx = []
	vy = []
	vz = []

	size = state.shape[0]

	

	for row in xrange(1,size):
		vx.append((state[row,0] - prev_x)/delta_t)
		vy.append((state[row,1] - prev_y)/delta_t)
		vz.append((state[row,2] - prev_z)/delta_t)

		prev_x = state[row,0]
		prev_y = state[row,1]
		prev_z = state[row,2]


	vel = np.array([vx,vy,vz],ndmin=2).transpose()
	print(vel.shape)

	np.save(vel_dir+'v'+file[1:],vel)

import numpy as np
import matplotlib.pyplot as plt

new_dir="/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/data/controls/"
old_dir="/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/50k/controls/"

prev = np.load(old_dir+"u_cos_sin_x_y.npy")
new = np.load(new_dir+"u_cos_sin_x_y.npy")


r = new.shape[0]
r1 = prev.shape[0]
# print(r1)
# exit()

new_x = []
new_y = []
new_z = []


prev_x = []
prev_y = []
prev_z = []

for row in range(0,r-1):
	prev_x.append(prev[row,0])
	prev_y.append(prev[row,1])
	prev_z.append(prev[row,2])

	new_x.append(new[row,0])
	new_y.append(new[row,1])
	new_z.append(new[row,2])



fig, ax = plt.subplots(nrows=2,ncols=3)

ax[0][0].plot(prev_x,'b')
ax[0][0].plot(new_x,'r')


ax[0][1].plot(prev_y,'b')
ax[0][1].plot(new_y,'r')

ax[0][2].plot(prev_z,'b')
ax[0][2].plot(new_z,'r')


plt.show()
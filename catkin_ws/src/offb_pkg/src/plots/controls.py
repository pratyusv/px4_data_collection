import numpy as np
import matplotlib.pyplot as plt

data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/scripts/data3/"

state = np.load(data_dir+"controls/u_x.npy")

size = state.shape[0]

u0 = []
u1 = []
u2 = []
u3 = []

size = 200
for row in range(100,size):
	u0.append(state[row,0])
	u1.append(state[row,1])
	u2.append(state[row,2])
	u3.append(state[row,3])



fig, ax = plt.subplots(nrows=2,ncols=2)
ax[0][0].set_title('Roll')
ax[0][0].plot(u0,'b')
# ax[0][0].plot(u1,'r')

ax[0][1].set_title('Pitch')
ax[0][1].plot(u1,'r')


ax[1][0].set_title('Yaw')
ax[1][0].plot(u2,'b')

ax[1][1].set_title('Throttle')
ax[1][1].plot(u3,'b')




plt.show()
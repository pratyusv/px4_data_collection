import numpy as np
import matplotlib.pyplot as plt

data_dir = "../data/"

state = np.load(data_dir+"states/s_x_sin_y.npy")

size = state.shape[0]

x = []
y = []
z = []

vx = []
vy = []
vz = []



for row in range(0,size):
	x.append(state[row,0])
	y.append(state[row,1])
	z.append(state[row,2])

	vx.append(state[row,3])
	vy.append(state[row,4])
	vz.append(state[row,5])



fig, ax = plt.subplots(nrows=2,ncols=3)

ax[0][0].plot(x,'b')
ax[0][1].plot(y,'b')
ax[0][2].plot(z,'b')


ax[1][0].plot(vx,'b')
ax[1][1].plot(vy,'b')
ax[1][2].plot(vz,'b')



plt.show()
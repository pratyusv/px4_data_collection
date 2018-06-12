import numpy as np
import matplotlib.pyplot as plt

data_dir = "../data/"

state = np.load(data_dir+"controls/u_x_sin_y.npy")

size = state.shape[0]

u0 = []
u1 = []
u2 = []
u3 = []


for row in range(0,size):
	u0.append(state[row,0])
	u1.append(state[row,1])
	u2.append(state[row,2])
	u3.append(state[row,3])



fig, ax = plt.subplots(nrows=2,ncols=4)

ax[0][0].plot(u0,'b')
ax[0][1].plot(u1,'b')
ax[0][2].plot(u2,'b')
ax[0][3].plot(u3,'b')




plt.show()
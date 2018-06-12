import numpy as np
import matplotlib.pyplot as plt

delta_t =  0.02

state_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/data/states/"
nn1_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/next_state/data/nn1/"

state = np.load(state_dir + 's_circle.npy')
t_prev = state[:-1,3:6]
t_next = state[1:,3:6]

state_val = (t_next  - t_prev)/delta_t
acc = np.load(nn1_dir + 'nn1_circle_grd_truth.npy')

print(state_val.shape)
print(acc.shape)
# exit()

size = state_val.shape[0]

state_ax = []
state_ay = []
state_az = []

nn1_ax = []
nn1_ay = []
nn1_az = []

t = []

for i in xrange(0,size):
	t.append(i)

for row in xrange(0,size):
	state_ax.append(state_val[row,0])
	state_ay.append(state_val[row,1])
	state_az.append(state_val[row,2])

	nn1_ax.append(acc[row,0])
	nn1_ay.append(acc[row,1])
	nn1_az.append(acc[row,2])

fig,ax = plt.subplots(nrows=2,ncols=3)

ax[0][0].plot(t,nn1_ax,'r',label='predictions')
ax[0][0].plot(t,state_ax,'b',label='grnd_truth')


ax[0][1].plot(t,nn1_ay,'r',label='predictions')
ax[0][1].plot(t,state_ay,'b',label='grnd_truth')

# ax[1][0].axis([0,13000,0,5])
ax[0][2].plot(t,nn1_az,'r',label='predictions')
ax[0][2].plot(t,state_az,'b',label='grnd_truth')

# ax[1][1].plot(t,gt_3,'b',label='grnd_truth')
# ax[1][1].plot(t,pred_3,'r',label='predictions')

# ax[1].plot(t,gt_1,'b',label='grnd_truth')
# ax[0].plot(t,pred_1,'r',label='predictions')

# legend = ax[0].legend(loc='upper left', shadow=True, fontsize='x-small')

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import math

data_dir = "../data/"
control_dir = "../data/"
acc_dir = "../data/"
nn1_dir = "../data/"

dir_ = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/infinite_queue/"

state = np.load(dir_ +"s_x_sin_y.npy")
# control = np.load(control_dir + "controls/u_x_sin_y.npy")
acc  = np.load(dir_ + "a_x_sin_y.npy")
nn1_gt = np.load(dir_ + "nn1_x_sin_y_grd_truth.npy")

size = nn1_gt.shape[0]
# size = 10
meas_ax = []
meas_ay = []
meas_az = []


calc_ax = []
calc_ay = []
calc_az = []

vx = []
vy = []
vz = []

x = []
y = []
z = []

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm


for row in xrange(0,size):
	x.append(state[row,0])
	y.append(state[row,1])
	z.append(state[row,2])

	meas_ax.append(-1*acc[row,0])
	meas_ay.append(-1*acc[row,1])
	meas_az.append(acc[row,2])


	calc_ax.append(nn1_gt[row,0])
	calc_ay.append(nn1_gt[row,1])
	calc_az.append(nn1_gt[row,2]+9.8)


	vx.append(state[row,3])
	vy.append(state[row,4])
	vz.append(state[row,5])


# calc_ax = np.array([calc_ax],ndmin=2).transpose()
# calc_ay = np.array([calc_ay],ndmin=2).transpose()

# calc_ax = (calc_ax - calc_ax.mean())/(calc_ax.std())
# calc_ay = (calc_ay - calc_ay.mean())/(calc_ay.std())

calc_ay = normalize(calc_ay)

fig, ax = plt.subplots(nrows=4,ncols=3)


ax[0][0].plot(meas_ax,'r')
ax[0][1].plot(meas_ay,'r')
ax[0][2].plot(meas_az,'r')

ax[1][0].plot(calc_ax,'b')
ax[1][1].plot(calc_ay,'b')
ax[1][2].plot(calc_az,'b')

ax[2][0].plot(vx,'g')
ax[2][1].plot(vy,'g')
ax[2][2].plot(vz,'g')

ax[3][0].plot(x,'g')
ax[3][1].plot(y,'g')
ax[3][2].plot(z,'g')

plt.show()
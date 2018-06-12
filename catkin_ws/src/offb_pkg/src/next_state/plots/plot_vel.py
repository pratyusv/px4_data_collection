import numpy as np
import matplotlib.pyplot as plt
import math

# data_dir = "../tmp/data_30k/"
# acc_dir = "../tmp/data_30k/"

delta_t = 0.02

# calculated = np.load("nn2/nn2_x_grd_truth.npy")
# measured = np.load("acc/a_x.npy")
calculated = np.load("vel/v_x.npy")
measured = np.load("states/s_x.npy")

calc_vx = []
calc_vy = []
calc_vz = []

meas_vx = []
meas_vy = []
meas_vz = []




size = measured.shape[0]
print(measured.shape[0])
print(calculated.shape[0])
# size = 5000


for row in xrange(0,size-2):

	calc_vx.append(calculated[row+1,0])
	calc_vy.append(calculated[row+1,1])
	calc_vz.append(calculated[row+1,2])


	meas_vx.append(measured[row,3])
	meas_vy.append(measured[row,4])
	meas_vz.append(measured[row,5])


# sum = 0.0
# for row in xrange(0,size-1):
# 	sum = sum + (calc_rs[row] - aplha_x[row])

# print(sum)

fig, ax = plt.subplots(nrows=3,ncols=3)


ax[0][0].plot(calc_vx,'b')
ax[0][1].plot(calc_vy,'b')
ax[0][2].plot(calc_vz,'r')


ax[1][0].plot(meas_vx,'r')
ax[1][1].plot(meas_vy,'r')
ax[1][2].plot(meas_vz,'b')

# ax[2][0].plot(rs,'g')
# ax[2][1].plot(ps,'g')
# ax[2][2].plot(ys,'g')

plt.show()
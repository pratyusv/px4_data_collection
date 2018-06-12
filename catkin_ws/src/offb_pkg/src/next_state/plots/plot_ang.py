import numpy as np
import matplotlib.pyplot as plt
import math

data_dir = "../tmp/data_30k/"
acc_dir = "../tmp/data_30k/"

delta_t = 0.02

calculated = np.load(data_dir+"nn2/nn2_x_grd_truth.npy")
measured = np.load(acc_dir + "acc/a_x.npy")
angles = np.load(data_dir+"states/s_x.npy")

meas_rs = []
meas_ps = []
meas_ys = []

calc_rs = []
calc_ps = []
calc_ys = []


rs = []
ps = []
ys = []


aplha_x = []
aplha_y = []
aplha_z = []

# check_rs.append(0)
# check_ps.append(0)
# check_ys.append(0)


size = calculated.shape[0]
size = 5000

prev_omega_x = angles[0,12]
prev_omega_y = angles[0,13]
prev_omega_z = angles[0,14]

for row in xrange(1,size):
	aplha_x.append((angles[row,12] - prev_omega_x)/0.05)
	aplha_y.append((angles[row,13] - prev_omega_y)/0.05)
	aplha_z.append((angles[row,14] - prev_omega_z)/0.05) 

	prev_omega_x = angles[row,12] 
	prev_omega_y = angles[row,13]
	prev_omega_z = angles[row,14]


for row in xrange(0,size):


	rs.append(angles[row,12])
	ps.append(angles[row,13])
	ys.append(angles[row,14])

	calc_rs.append(calculated[row,0])
	calc_ps.append(calculated[row,1])
	calc_ys.append(calculated[row,2])


	meas_rs.append(measured[row,0])
	meas_ps.append(measured[row,1])
	meas_ys.append(measured[row,2])


sum = 0.0
for row in xrange(0,size-1):
	sum = sum + (calc_rs[row] - aplha_x[row])

print(sum)

fig, ax = plt.subplots(nrows=3,ncols=3)

ax[1][0].plot(meas_rs,'r')
ax[1][1].plot(meas_ps,'r')
ax[1][2].plot(meas_ys,'r')

ax[0][0].plot(calc_rs,'b')
ax[0][0].plot(aplha_x,'r')

ax[0][1].plot(calc_ps,'b')
ax[0][1].plot(aplha_y,'r')

ax[0][2].plot(calc_ys,'b')
ax[0][2].plot(aplha_z,'r')

# ax[2][0].plot(rs,'g')
# ax[2][1].plot(ps,'g')
# ax[2][2].plot(ys,'g')

plt.show()
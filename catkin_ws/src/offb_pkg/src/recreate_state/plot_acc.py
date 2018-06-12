import numpy as np
import matplotlib.pyplot  as plt

acc = np.load('a_xy.npy')
vel = np.load('s_xy.npy')

ax = []
ay = []
az = []

vx = []
vy = []
vz = []


pred_vx = []
pred_vy = []
pred_vz = []

size = acc.shape[0]
print(size)
size = 150 

start_point = 0

for row in range(start_point,size):

	vx.append(vel[row,3])
	vy.append(vel[row,4])
	vz.append(vel[row,5])

	ax.append(float(acc[row,1]))
	ay.append(float(acc[row,0]))
	az.append(-1*float(acc[row,2]))

prev_vx = vel[row,3]
prev_vy = vel[row,4]
prev_vz = vel[row,5]

for row  in range(start_point,size-1):

	temp_vx = (acc[row,1] * 0.02) + prev_vx
	temp_vy = (acc[row,0] * 0.02) + prev_vy
	temp_vz = ((acc[row,2]+9.8) * 0.02) + prev_vz

	pred_vx.append(temp_vx)
	pred_vy.append(temp_vy)
	pred_vz.append(temp_vz)

	prev_vx = temp_vx
	prev_vy = temp_vy
	prev_vz = temp_vz


# print(len(vx))

fig, axis = plt.subplots(nrows=3, ncols=3)

axis[0][0].plot(ax,'b')
axis[0][1].plot(ay,'b')
axis[0][2].plot(az,'b')

axis[1][0].plot(vx,'b')
axis[1][1].plot(vy,'b')
axis[1][2].plot(vz,'b')

axis[2][0].plot(pred_vx,'r')
axis[2][1].plot(pred_vy,'r')
axis[2][2].plot(pred_vz,'r')

plt.show()
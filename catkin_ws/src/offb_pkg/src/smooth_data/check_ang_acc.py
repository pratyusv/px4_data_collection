import numpy as np
import matplotlib.pyplot as plt
import math

data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data_original/nn2/"
acc    = np.load(data_dir		+ "nn2_circle_grd_truth.npy")

s_data_dir = "/home/pratyush/Desktop/quadrotor_lqr/catkin_ws/src/offb_pkg/src/smooth_data/data/ang_acc/"
s_acc    = np.load(s_data_dir	+ "alpha_circle.npy")



size = acc.shape[0]
# size = 50

ac_x = []
ac_y = []
ac_z = []

s_ac_x = []
s_ac_y = []
s_ac_z = []

for row in range(0,size):
	ac_x.append(acc[row,0])
	ac_y.append(acc[row,1])
	ac_z.append(acc[row,2])

	s_ac_x.append(s_acc[row,0])
	s_ac_y.append(s_acc[row,1])
	s_ac_z.append(s_acc[row,2])



## Angular Acceleration
fig1, ax1 = plt.subplots(nrows=3,ncols=1)
ax1[0].set_title('Angular Acceleration')
ax1[0].plot(ac_x,'b')
ax1[0].plot(s_ac_x,'r')
ax1[1].plot(ac_y,'b')
ax1[1].plot(s_ac_y,'r')
ax1[2].plot(ac_z,'b')
ax1[2].plot(s_ac_z,'r')


print("Grd_truth")
print('col :', 0 ,'min :', np.amin(acc[:,0]), ' max :', np.amax(acc[:,0]))
print('col :' ,1 ,'min :', np.amin(acc[:,1]), ' max :', np.amax(acc[:,1]))
print('col :' ,2 ,'min :', np.amin(acc[:,1]), ' max :', np.amax(acc[:,2]))

print("alpha")
print('col :', 0 ,'min :', np.amin(s_acc[:,0]), ' max :', np.amax(s_acc[:,0]))
print('col :' ,1 ,'min :', np.amin(s_acc[:,1]), ' max :', np.amax(s_acc[:,1]))
print('col :' ,2 ,'min :', np.amin(s_acc[:,1]), ' max :', np.amax(s_acc[:,2]))


plt.show()
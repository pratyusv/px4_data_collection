import numpy as np
import matplotlib.pyplot  as plt

data_dir = "./data/states/"
state = np.load(data_dir + 's_x_cos_z.npy')

size = state.shape[0]

# size = 10

x = []
y = []
z = []


vx = []
vy = []
vz = []


pred_x = []
pred_y = []
pred_z = []


for row in range(0,size):
	x.append(state[row,0])
	y.append(state[row,1])
	z.append(state[row,2])

	vx.append(state[row,3])
	vy.append(state[row,4])
	vz.append(state[row,5])


prev_x = state[0,0]
prev_y = state[0,1]
prev_z = state[0,2]


pred_x.append(state[0,0])
pred_y.append(state[0,1])
pred_z.append(state[0,2])

for row in range(1,size):

	temp_x = (state[row,3]*0.02) + prev_x
	temp_y = (state[row,4]*0.02) + prev_y
	temp_z = (state[row,5]*0.02) + prev_z

	pred_x.append(temp_x)
	pred_y.append(temp_y)
	pred_z.append(temp_z)

	prev_x = temp_x
	prev_y = temp_y
	prev_z = temp_z


# print("len x:",len(x), "len pred_x :", len(pred_x))

data_point = size

diff_x = []
abs_x = 0.0

diff_y = []
abs_y = 0.0


diff_z = []
abs_z = 0.0


for row in range(0,data_point):
	# print('z :','{:.5f}'.format(z[row]), 'pred_z :', '{:.5f}'.format(pred_z[row]))
	diff_x.append(pred_x[row] - x[row])  
	abs_x += abs(pred_x[row] - x[row])

	diff_y.append(pred_y[row] - y[row])  
	abs_y += abs(pred_y[row] - y[row])

	diff_z.append(pred_z[row] - z[row])  
	abs_z += abs(pred_z[row] - z[row])

diff_x = np.array([diff_x],ndmin=2).transpose()
diff_y = np.array([diff_y],ndmin=2).transpose()
diff_z = np.array([diff_z],ndmin=2).transpose()

print("Mean")
print('x = ','{:.5f}'.format(diff_x.mean()),'y = ','{:.5f}'.format(diff_y.mean()), ' z = ','{:.5f}'.format(diff_z.mean()))

print("absolute diff")
print('x = ','{:.5f}'.format(abs_x/size),'y = ','{:.5f}'.format(abs_y/size), ' z = ','{:.5f}'.format(abs_z/size))



fig, axis = plt.subplots(nrows=3,ncols=3)

axis[0][0].plot(x,'b')
axis[0][0].plot(pred_x,'r')

axis[0][1].plot(y,'b')
axis[0][1].plot(pred_y,'r')

axis[0][2].plot(z,'b')
axis[0][2].plot(pred_z,'r')
# axis[0][2].axis([0,10201, -1 ,10])


axis[1][0].plot(vx,'b')
axis[1][1].plot(vy,'b')
axis[1][2].plot(vz,'b')

axis[2][0].plot(diff_x,'b')
axis[2][1].plot(diff_y,'b')
axis[2][2].plot(diff_z,'b')

plt.show()
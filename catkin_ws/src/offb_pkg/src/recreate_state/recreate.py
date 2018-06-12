#!/usr/bin/python
import numpy as np
import math
import matplotlib.pyplot as plt

weight_dir_nn1 = "./w_nn1/"
weight_dir_nn2 = "./w_nn2/"

delta_t = 0.02

state = np.load('s_xy_sin.npy')
control = np.load('u_xy_sin.npy')

w_L1_nn1 = np.load(weight_dir_nn1 + 'WeightLayer0.npy')
b_L1_nn1 = np.load(weight_dir_nn1 + 'BiasLayer0.npy')
w_L2_nn1 = np.load(weight_dir_nn1 + 'WeightLayer1.npy')
b_L2_nn1 = np.load(weight_dir_nn1 + 'BiasLayer1.npy')

w_L1_nn2 = np.load(weight_dir_nn2 + 'WeightLayer0.npy')
b_L1_nn2 = np.load(weight_dir_nn2 + 'BiasLayer0.npy')
w_L2_nn2 = np.load(weight_dir_nn2 + 'WeightLayer1.npy')
b_L2_nn2 = np.load(weight_dir_nn2 + 'BiasLayer1.npy')
w_L3_nn2 = np.load(weight_dir_nn2 + 'WeightLayer2.npy')
b_L3_nn2 = np.load(weight_dir_nn2 + 'BiasLayer2.npy')

# w_L1_nn1 = np.array([w_L1_nn1],ndmin=2)
b_L1_nn1 = np.array([b_L1_nn1],ndmin=2)
# w_L2_nn1 = np.array([w_L2_nn1],ndmin=2)
b_L2_nn1 = np.array([b_L2_nn1],ndmin=2)

# print(w_L1_nn1.shape)
# print(b_L1_nn1.shape)
# print(w_L2_nn1.shape)
# print(b_L2_nn1.shape)
# exit()

position = []
velocity = []
sin = []
cos = []
omega = []
angles = []
# state = []
# state.append(state_rec[0,:])

def linear_acc(state,control):
	s = np.array([state[3:15]],ndmin=2)
	u = np.array([control[3]],ndmin=2)
	ipt = np.concatenate((s,u),axis=1)
	# print(ipt.shape)
	h1 = b_L1_nn1 + np.matmul(ipt,w_L1_nn1)
	h1[h1<0] = 0
	o  =  np.matmul(h1, w_L2_nn1)
	# print(o.shape)
	# exit()
	return o


def angular_acc(state,control):
	s = np.array([state[3:15]],ndmin=2)
	u = np.array([control[0:3]],ndmin=2)
	ipt = np.concatenate((s,u),axis=1)
	
	t1 = b_L1_nn2 + np.matmul(ipt,w_L1_nn2) 
	h1 = 1.0 / (1.0 + np.exp(-1*t1))

	h2 = b_L2_nn2 + np.matmul(h1, w_L2_nn2)
	h2[h2 < 0] = 0

	o = np.matmul(h2, w_L3_nn2)
	return o


def angular_velocity(euler_angles,omga):
	phi = euler_angles[0]
	theta = euler_angles[1]
	psi = euler_angles[2]
	R_hat = np.array([[1, math.sin(phi)* math.tan(theta), math.cos(phi)*math.tan(theta)],
			[0, math.cos(phi), -1*math.sin(phi)],
			[0, float(math.sin(phi)/math.cos(theta)), float(math.cos(phi)/ math.cos(theta)) ]])

	o = np.matmul(R_hat, omga)
	# print(o.shape)
	return o


data_points = 19999
for row in range(0,data_points):
	v = np.array([state[row,3:6]],ndmin=2)
	linear_a = linear_acc(state[row,:],control[row,:])
	linear_a = np.reshape(linear_a,(3,))
	

	# sin = np.array([state[row,6:9]],ndmin=2)
	# cos = np.array([state[row,9:12]],ndmin=2)
	ang_v = angular_velocity(state[row,12:15], state[row,15:18])
	angular_a = angular_acc(state[row,:],control[row,:])

	# s_dot = np.concatenate((v,linear_a,ang_v,angular_a),axis=1)

	temp_pos = state[row,3:6]*delta_t + state[row,0:3]
	temp_angles = ang_v*delta_t + state[row,12:15]
	temp_vel = linear_a*delta_t + state[row,3:6]
	temp_omega = angular_a*delta_t + state[row,15:18]
	temp_omega = np.reshape(temp_omega, (3,))


	position.append(temp_pos)
	angles.append(temp_angles)
	velocity.append(temp_vel)
	omega.append(temp_omega)



# print(position[0][0])
# t_pos = np.array([position[1.1]])
# print(t_pos.shape)
# exit()

# print(len(velocity[0]))
# print(velocity[0])
# exit()


truth_x = []
pred_x = []

truth_y = []
pred_y = []

truth_z = []
pred_z = []

sum = 0.0

#############
# POSITION  #
#############


# X pos
# sum = 0.0
# for row in range(0,data_points):
# 	truth_x.append(state[row+1,0])
# 	pred_x.append(position[row][0])
# 	diff =  state[row+1,0] - position[row][0]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,0]), "Prediction ", '{:.5f}'.format(position[row][0]))


# # Y pos
# sum = 0.0
# for row in range(0,data_points):
# 	truth_y.append(state[row+1,1])
# 	pred_y.append(position[row][1])
# 	diff =  state[row+1,1] - position[row][1]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,1]), "Prediction ", '{:.5f}'.format(position[row][1]))


# # Z position
# sum = 0.0
# for row in range(0,data_points):
# 	truth_z.append(state[row+1,2])
# 	pred_z.append(position[row][2])
# 	diff =  state[row+1,2] - position[row][2]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,2]), "Prediction ", '{:.5f}'.format(position[row][2]))




# #############
# # VELOCITY  #
# #############

# Vel X
sum = 0.0
for row in range(0,data_points):
	truth_x.append(state[row+1,3])
	pred_x.append(velocity[row][0])
	diff =  state[row+1,3] - velocity[row][0]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,3]), "Prediction ", '{:.5f}'.format(velocity[row][0]))



# Vel X
sum = 0.0
for row in range(0,data_points):
	truth_y.append(state[row+1,4])
	pred_y.append(velocity[row][1])
	diff =  state[row+1,4] - velocity[row][1]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,4]), "Prediction ", '{:.5f}'.format(velocity[row][1]))


# Vel Z
sum = 0.0
for row in range(0,data_points):
	truth_z.append(state[row+1,5])
	pred_z.append(velocity[row][2])
	diff =  state[row+1,5] - velocity[row][2]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,5]), "Prediction ", '{:.5f}'.format(velocity[row][2]))


#############
# ANGLES    #
#############

# # Angles X
# for row in range(0,data_points):
# 	truth_x.append(state[row+1,6])
# 	pred_x.append(angles[row][0])
# 	diff =  state[row+1,6] - angles[row][0]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,6]), "Prediction ", '{:.5f}'.format(angles[row][0]))


# # Angles Y
# for row in range(0,data_points):
# 	truth_y.append(state[row+1,7])
# 	pred_y.append(angles[row][1])
# 	diff =  state[row+1,7] - angles[row][1]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,7]), "Prediction ", '{:.5f}'.format(angles[row][1]))



# # Angles Z
# for row in range(0,data_points):
# 	truth_z.append(state[row+1,8])
# 	pred_z.append(angles[row][2])
# 	diff =  state[row+1,8] - angles[row][2]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,8]), "Prediction ", '{:.5f}'.format(angles[row][2]))




#############
# OMEGA     #
#############

# # omega X
# for row in range(0,data_points):
# 	truth_x.append(state[row+1,15])
# 	pred_x.append(omega[row][0])
# 	diff =  state[row+1,15] - omega[row][0]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,15]), "Prediction ", '{:.5f}'.format(omega[row][0]))



# # omega Y
# for row in range(0,data_points):
# 	truth_y.append(state[row+1,16])
# 	pred_y.append(omega[row][1])
# 	diff =  state[row+1,16] - omega[row][1]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,16]), "Prediction ", '{:.5f}'.format(omega[row][1]))


# # omega Z
# for row in range(0,data_points):
# 	truth_z.append(state[row+1,17])
# 	pred_z.append(omega[row][2])
# 	diff =  state[row+1,17] - omega[row][2]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,17]), "Prediction ", '{:.5f}'.format(omega[row][2]))


print(sum)

fig, ax = plt.subplots(nrows=2,ncols=3)

ax[0][0].plot(truth_x,'b')
ax[0][0].plot(pred_x,'r')

ax[0][1].plot(truth_y,'b')
ax[0][1].plot(pred_y,'r')

ax[0][2].plot(truth_z,'b')
ax[0][2].plot(pred_z,'r')


plt.show()
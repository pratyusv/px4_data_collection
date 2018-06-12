#!/usr/bin/python
import numpy as np
import math
import matplotlib.pyplot as plt

weight_dir_nn1 = "./w_nn1/"
weight_dir_nn2 = "./w_nn2/"

delta_t = 0.02

state = np.load('s_xy_sin.npy')
control = np.load('u_xy_sin.npy')
acceleration  = np.load('a_xy_sin.npy')

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

# calc_state = state[0,:]
# calc_state = np.zeros(18)
# calc_state =  np.reshape(calc_state,(18,))
# print(calc_state.shape)

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


calc_state = state[0,:]
calc_state =  np.reshape(calc_state,(18,))

data_points = 9999

for row in range(0,data_points):
	# v = np.array([calc_state[3:6]],ndmin=2)

	# linear_a = linear_acc(calc_state,control[row,:])
	# linear_a = np.reshape(linear_a,(3,))
	

	# sin = np.array([calc_state[6:9]])
	# sin = np.reshape(sin,(3,))
	# cos = np.array([calc_state[9:12]])
	# cos = np.reshape(cos,(3,))

	# ang_v = angular_velocity(calc_state[12:15], calc_state[15:18])
	# ang_v = np.reshape(ang_v,(3,))

	# angular_a = angular_acc(calc_state,control[row,:])
	# angular_a = np.reshape(angular_a, (3,))

	# temp_pos = [i for i in range(0,4)]

	a_x = acceleration[row,1]
	a_y = acceleration[row,0]
	a_z = -1*acceleration[row,2]

	ned_a = np.array([a_x,a_y,a_z],ndmin=2).transpose()
	ned_a = np.reshape(ned_a,(3,))
	temp_vel = (ned_a * delta_t) + calc_state[3:6]

	# temp_pos = (calc_state[3:6] * 0.02) +  calc_state[0:3] 
	# print("vel_t :"'{:.5}'.format(calc_state[5]), "*",'{:.5}'.format(delta_t),"+","pos_t :",'{:.5}'.format(calc_state[2]), "=","pos_t+1",'{:.5}'.format(temp_pos[2]) )
	# diff = temp_pos[2] - state[row+1,2]
	# print('row',row,'actual :' ,'{:.5f}'.format(state[row+1,2]),'calc :','{:.5f}'.format(temp_pos[2]) ,'difference = ','{:.5f}'.format(diff)) #,'Actual :' ,'{:.5f}'.format(state[row+1,0]))

	# temp_pos = (calc_state[3:6] * delta_t) + (0.5 *(state[row,3:6]-calc_state[3:6])*delta_t ) + calc_state[0:3]
	# temp_pos[2] = calc_state[5]*delta_t  - (0.5*10* delta_t*delta_t) + calc_state[2]
	# temp_pos[2] = 0.5*(calc_state[5] + state[row+1,5])*delta_t + calc_state[2]
	# temp_pos[2] = (calc_state[5]*delta_t + 0.5*( ((calc_state[5]-state[row+1,5])/delta_t))*delta_t*delta_t) + calc_state[2]
	# temp_pos[2] = calc_state[2] + (((state[row+1,5]**2) - (calc_state[5]**2)) / (-20))

	# print(calc_state[4]+ state[row+1,4])
	# temp_pos = state[row,3:6] *  delta_t + state[row,0:3]
	# temp_angles = ang_v*delta_t + state[row,12:15]
	# temp_vel = linear_a*delta_t + calc_state[3:6]
	# temp_omega = angular_a*delta_t + calc_state[15:18]
	
	# sin = np.array([math.sin(calc_state[6]),math.sin(calc_state[7]), math.sin(calc_state[8])])
	# cos = np.array([math.cos(calc_state[6]),math.cos(calc_state[7]), math.cos(calc_state[8])])

	temp_pos = state[row+1,0:3]
	# temp_vel = state[row+1,3:6]
	temp_angles = state[row+1,12:15]
	sin = state[row+1,6:9]
	cos = state[row+1,9:12]
	temp_omega = state[row+1,15:18]
	# temp_omega = np.reshape(temp_omega,(3,1))

	calc_state = np.concatenate((temp_pos,temp_vel,temp_angles,sin, cos, temp_omega))
	# print(calc_state)
	# print(state[row+1,2] - calc_state[2])
	# exit()



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
sum = 0.0
for row in range(0,data_points):
	truth_x.append(state[row+1,0])
	pred_x.append(position[row][0])
	diff =  state[row+1,0] - position[row][0]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,0]), "Prediction ", '{:.5f}'.format(position[row][0]))


# Y pos
sum = 0.0
for row in range(0,data_points):
	truth_y.append(state[row+1,1])
	pred_y.append(position[row][1])
	diff =  state[row+1,1] - position[row][1]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,1]), "Prediction ", '{:.5f}'.format(position[row][1]))


# Z pos
# sum = 0.0
for row in range(0,data_points):
	truth_z.append(state[row+1,2])
	pred_z.append(position[row][2])
	diff =  state[row+1,2] - position[row][2]
	# sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,2]), "Prediction ", '{:.5f}'.format(position[row][2]))




# #############
# # VELOCITY  #
# #############

# Vel X
truth_v_x = []
pred_v_x = []
sum = 0.0
for row in range(0,data_points):
	truth_v_x.append(state[row+1,3])
	pred_v_x.append(velocity[row][0])
	diff =  state[row+1,3] - velocity[row][0]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,3]), "Prediction ", '{:.5f}'.format(velocity[row][0]))



# Vel X
truth_v_y = []
pred_v_y = []
sum = 0.0
for row in range(0,data_points):
	truth_v_y.append(state[row+1,4])
	pred_v_y.append(velocity[row][1])
	diff =  state[row+1,4] - velocity[row][1]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,4]), "Prediction ", '{:.5f}'.format(velocity[row][1]))


# Vel Z
truth_v_z = []
pred_v_z = []
sum = 0.0
for row in range(0,data_points):
	truth_v_z.append(state[row+1,5])
	pred_v_z.append(velocity[row][2])
	diff =  state[row+1,5] - velocity[row][2]
	sum += diff 
	# print("Truth " ,'{:.5f}'.format(state[row+1,5]), "Prediction ", '{:.5f}'.format(velocity[row][2]))


#############
# ANGLES    #
#############

# # Angles X
# sum = 0.0
# truth_a_x = []
# pred_a_x = []
# for row in range(0,data_points):
# 	truth_a_x.append(state[row+1,6])
# 	pred_a_x.append(angles[row][0])
# 	diff =  state[row+1,6] - angles[row][0]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,6]), "Prediction ", '{:.5f}'.format(angles[row][0]))


# # Angles Y
# sum = 0.0
# truth_a_y = []
# pred_a_y = []
# for row in range(0,data_points):
# 	truth_a_y.append(state[row+1,7])
# 	pred_a_y.append(angles[row][1])
# 	diff =  state[row+1,7] - angles[row][1]
# 	sum += diff 
# 	# print("Truth " ,'{:.5f}'.format(state[row+1,7]), "Prediction ", '{:.5f}'.format(angles[row][1]))



# # Angles Z
# sum = 0.0
# truth_a_z = []
# pred_a_z = []
# for row in range(0,data_points):
# 	truth_a_z.append(state[row+1,8])
# 	pred_a_z.append(angles[row][2])
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

#####################
# VELOCITY DIFF     #
#####################

# vel_calc = []
# for row in range(0,data_points):
# 	diff = (state[row+1,3:6] - state[row,3:6])/ 0.02
# 	vel_calc.append(diff)


# truth_v_y = []
# pred_v_y = []
# for row in range(0,data_points):
# 	truth_v_y.append(state[row+1,5])
# 	pred_v_y.append(vel_calc[row][2])


fig, ax = plt.subplots(nrows=2,ncols=3)

ax[0][0].plot(truth_x,'b')
ax[0][0].plot(pred_x,'r')

ax[0][1].plot(truth_y,'b')
ax[0][1].plot(pred_y,'r')

ax[0][2].plot(pred_z,'r')
ax[0][2].plot(truth_z,'b')


ax[1][0].plot(pred_v_x,'r')
ax[1][0].plot(truth_v_x,'b')

ax[1][1].plot(pred_v_y,'r')
ax[1][1].plot(truth_v_y,'b')

ax[1][2].plot(truth_v_z,'b')
ax[1][2].plot(pred_v_z,'r')




plt.show()
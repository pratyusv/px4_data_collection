import numpy as np
import matplotlib.pyplot as plt
import math

data_dir 	= "../next_state/data/"
control_dir = "../next_state/data/"
acc_dir 	= "../next_state/data/"
nn2_dir 	= "../next_state/data/"

state 	= np.load(data_dir		+ "states/s_x_cos_sin_y.npy")
control = np.load(control_dir 	+ "controls/u_x_cos_sin_y.npy")
acc  	= np.load(acc_dir 		+ "acc/a_x_cos_sin_y.npy")
alpha 	= np.load(nn2_dir 		+ "nn2/nn2_x_cos_sin_y_grd_truth.npy")

size = state.shape[0]
# size = 50


x = []
y = []
z = []

vx = []
vy = []
vz = []

phi = []
theta = []
psi = []


sin_phi = []
sin_theta = []
sin_psi = []


cos_phi = []
cos_theta = []
cos_psi = []


rs = []
ps = []
ys = []


u1 = []
u2 = []
u3 = []
u4 = []

ac_x = []
ac_y = []
ac_z = []


alpha_x = []
alpha_y = []
alpha_z = []


s_vx = []
s_vy = []
s_vz = []

s_rs = []
s_ps = []
s_ys = []

s_ac_x = []
s_ac_y = []
s_ac_z = []


s_alpha_x = []
s_alpha_y = []
s_alpha_z = []


a = 0.05

for row in range(0,size):
	x.append(state[row,0])
	y.append(state[row,1])
	z.append(state[row,2])

	vx.append(state[row,3] )
	vy.append(state[row,4])
	vz.append(state[row,5])

	sin_phi.append(state[row,6])
	sin_theta.append(state[row,7])
	sin_psi.append(state[row,8])


	cos_phi.append(state[row,9])
	cos_theta.append(state[row,10])
	cos_psi.append(state[row,11])


	rs.append(state[row,12] )
	ps.append(state[row,13] )
	ys.append(state[row,14] )

	phi.append(state[row,15] )
	theta.append(state[row,16])
	psi.append(state[row,17])

	u1.append(control[row,0]*1)
	u2.append(control[row,1]*1)
	u3.append(control[row,2]*1)
	u4.append(control[row,3]*1)


	ac_x.append(acc[row,0])
	ac_y.append(acc[row,1])
	ac_z.append(acc[row,2])

	alpha_x.append(alpha[row,0])
	alpha_y.append(alpha[row,1])
	alpha_z.append(alpha[row,2])


## Linear velocity
temp_x = state[0,3]
temp_y = state[0,4]
temp_z = state[0,5]
for row in xrange(0,size):

	temp_x = temp_x + a*(state[row,3] - temp_x)
	temp_y = temp_y + a*(state[row,4] - temp_y)
	temp_z = temp_z + a*(state[row,5] - temp_z)

	s_vx.append( temp_x )
	s_vy.append( temp_y )
	s_vz.append( temp_z )



## Linear Acceleration
temp_x = acc[0,0]
temp_y = acc[0,1]
temp_z = acc[0,2]
for row in xrange(0,size):

	temp_x = temp_x + a*(acc[row,0] - temp_x)
	temp_y = temp_y + a*(acc[row,1] - temp_y)
	temp_z = temp_z + a*(acc[row,2] - temp_z)

	s_ac_x.append( temp_x )
	s_ac_y.append( temp_y )
	s_ac_z.append( temp_z )



## Angular Velocity
temp_x = state[0,12]
temp_y = state[0,13]
temp_z = state[0,14]

a = 0.03

for row in xrange(0,size):

	temp_x = temp_x + a*(state[row,12] - temp_x)
	temp_y = temp_y + a*(state[row,13] - temp_y)
	temp_z = temp_z + a*(state[row,14] - temp_z)

	s_rs.append( temp_x )
	s_ps.append( temp_y )
	s_ys.append( temp_z )



## Angular Acceleration
temp_x = s_rs[0]
temp_y = s_ps[0]
temp_z = s_ys[0]
delta_t = 0.02

for row in xrange(1,size):

	# temp_x = temp_x + a*(acc[row,0] - temp_x)
	# temp_y = temp_y + a*(acc[row,1] - temp_y)
	# temp_z = temp_z + a*(acc[row,2] - temp_z)

	s_alpha_x.append((s_rs[row] - temp_x )/delta_t)
	s_alpha_y.append((s_ps[row] - temp_y )/delta_t)
	s_alpha_z.append((s_ys[row] - temp_z )/delta_t)

	temp_x = s_rs[row]
	temp_y = s_ps[row]
	temp_z = s_ys[row]


# temp_x = alpha_x[0]
# temp_y = alpha_y[0]
# temp_z = alpha_z[0]
# for row in xrange(0,size):

# 	temp_x = temp_x + a*(alpha_x[row] - temp_x)
# 	temp_y = temp_y + a*(alpha_y[row] - temp_y)
# 	temp_z = temp_z + a*(alpha_z[row] - temp_z)

# 	s_alpha_x.append( temp_x )
# 	s_alpha_y.append( temp_y )
# 	s_alpha_z.append( temp_z )


# ## Linear Velocity
# fig1, ax1 = plt.subplots(nrows=3,ncols=1)
# ax1[0].set_title('Linear Velocity')
# # ax1[0].set_ylim(-0.2,0.2)
# ax1[0].plot(vx,'b',label='x')
# ax1[0].plot(s_vx,'r',label='x')
# # ax1[1].set_ylim(-0.2,0.2)
# ax1[1].plot(vy,'b',label='y')
# ax1[1].plot(s_vy,'r',label='y')
# # ax1[2].set_ylim(-0.2,0.2)
# ax1[2].plot(vz,'b',label='z')
# ax1[2].plot(s_vz,'r',label='z')



# ## Linear Acceleration
# fig1, ax1 = plt.subplots(nrows=3,ncols=1)
# ax1[0].set_title('Linear Acceleration')
# # ax1[0].set_ylim(-0.2,0.2)
# ax1[0].plot(ac_x,'b',label='x')
# ax1[0].plot(s_ac_x,'r',label='x')
# # ax1[1].set_ylim(-0.2,0.2)
# ax1[1].plot(ac_y,'b',label='y')
# ax1[1].plot(s_ac_y,'r',label='y')
# # ax1[2].set_ylim(-0.2,0.2)
# ax1[2].plot(ac_z,'b',label='z')
# ax1[2].plot(s_ac_z,'r',label='z')


## Angular Velocity
fig1, ax1 = plt.subplots(nrows=3,ncols=1)
ax1[0].set_title('Angular Velocity')
# ax1[0].set_ylim(-0.2,0.2)
ax1[0].plot(rs,'b',label='x')
ax1[0].plot(s_rs,'r',label='x')
# ax1[1].set_ylim(-0.2,0.2)
ax1[1].plot(ps,'b',label='y')
ax1[1].plot(s_ps,'r',label='y')
# ax1[2].set_ylim(-0.2,0.2)
ax1[2].plot(ys,'b',label='z')
ax1[2].plot(s_ys,'r',label='z')

## Angular Acceleration
fig1, ax1 = plt.subplots(nrows=3,ncols=1)
ax1[0].set_title('Angular Acceleration')
# ax1[0].set_ylim(-0.2,0.2)
ax1[0].plot(alpha_x,'b',label='x')
ax1[0].plot(s_alpha_x,'r',label='x')
# ax1[1].set_ylim(-0.2,0.2)
ax1[1].plot(alpha_y,'b',label='y')
ax1[1].plot(s_alpha_y,'r',label='y')
# ax1[2].set_ylim(-0.2,0.2)
ax1[2].plot(alpha_z,'b',label='z')
ax1[2].plot(s_alpha_z,'r',label='z')


plt.show()
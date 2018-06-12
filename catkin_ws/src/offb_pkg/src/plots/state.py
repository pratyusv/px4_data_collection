import numpy as np
import matplotlib.pyplot as plt
import math

data_dir = "../next_state/data/"
control_dir = "../next_state/data/"
acc_dir = "../next_state/data/"
nn2_dir = "../next_state/data/"

state = np.load(data_dir+"states/s_x_cos_sin_y.npy")
control = np.load(control_dir + "controls/u_x_cos_sin_y.npy")
acc  = np.load(acc_dir + "acc/a_x_cos_sin_y.npy")
alpha = np.load(nn2_dir + "nn2/nn2_x_cos_sin_y_grd_truth.npy")

size = state.shape[0]
# size = 50

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

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

check_phi = []
check_theta  = []
check_psi = []

mv_alpha_x = []
mv_alpha_y = []
mv_alpha_z = []

temp_alpha_x = 0.0
temp_alpha_y = 0.0
temp_alpha_z = 0.0

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

	check_phi.append(math.sin(state[row,15]))
	check_theta.append(math.sin(state[row,16]))
	check_psi.append(math.sin(state[row,17]))

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

	temp_alpha_x = temp_alpha_x + a*(state[row,12] - temp_alpha_x)
	temp_alpha_y = temp_alpha_y + a*(state[row,13] - temp_alpha_y)
	temp_alpha_z = temp_alpha_z + a*(state[row,14] - temp_alpha_z)


	mv_alpha_x.append( temp_alpha_x )
	mv_alpha_y.append( temp_alpha_y )
	mv_alpha_z.append( temp_alpha_z )



# print('vx :min',  '{:.5f}'.format(np.amin(vx)))
# print('vx :max',  '{:.5f}'.format(np.mean(vx)))


# vx = normalize(vx)
# vy = normalize(vy)

print('vx :mean', '{:.5f}'.format(np.mean(vx)))
print('vy :mean', '{:.5f}'.format(np.mean(vy)))
print('vz :mean', '{:.5f}'.format(np.mean(vz)))
print('---------------------------------------')


print('sin_phi   :mean', '{:.5f}'.format(np.mean(sin_phi)))
print('sin_theta :mean', '{:.5f}'.format(np.mean(sin_theta)))
print('sin_psi   :mean', '{:.5f}'.format(np.mean(sin_psi)))
print('---------------------------------------')

print('cos_phi   :mean', '{:.5f}'.format(np.mean(cos_phi)))
print('cos_theta :mean', '{:.5f}'.format(np.mean(cos_theta)))
print('cos_psi   :mean', '{:.5f}'.format(np.mean(cos_psi)))
print('---------------------------------------')


print('phi   :mean', '{:.5f}'.format(np.mean(phi)))
print('theta :mean', '{:.5f}'.format(np.mean(theta)))
print('psi   :mean', '{:.5f}'.format(np.mean(psi)))
print('---------------------------------------')

print('rs :mean', '{:.5f}'.format(np.mean(rs)))
print('ps :mean', '{:.5f}'.format(np.mean(ps)))
print('ys :mean', '{:.5f}'.format(np.mean(ys)))
print('---------------------------------------')

print('u1 :mean', '{:.5f}'.format(np.mean(u1)))
print('u2 :mean', '{:.5f}'.format(np.mean(u2)))
print('u3 :mean', '{:.5f}'.format(np.mean(u3)))
print('u4 :mean', '{:.5f}'.format(np.mean(u4)))

print('---------------------------------------')

print('ac_x :mean', '{:.5f}'.format(np.mean(ac_x)))
print('ac_y :mean', '{:.5f}'.format(np.mean(ac_y)))
print('ac_z :mean', '{:.5f}'.format(np.mean(ac_z)))

print('---------------------------------------')

print('alpha_x :mean', '{:.5f}'.format(np.mean(alpha_x)))
print('alpha_y :mean', '{:.5f}'.format(np.mean(alpha_y)))
print('alpha_z :mean', '{:.5f}'.format(np.mean(alpha_z)))

print('alpha_x :min :', '{:.5f}'.format(np.amin(alpha_x)), ' max :', '{:.5f}'.format(np.amax(alpha_x)) )
print('alpha_y :min :', '{:.5f}'.format(np.amin(alpha_y)), ' max :', '{:.5f}'.format(np.amax(alpha_y)) )
print('alpha_z :min :', '{:.5f}'.format(np.amin(alpha_z)), ' max :', '{:.5f}'.format(np.amax(alpha_z)) )


# exit()


x = np.array([x],ndmin=2).transpose()
y = np.array([y],ndmin=2).transpose()
z = np.array([z],ndmin=2).transpose()

vx = np.array([vx],ndmin=2).transpose()
vy = np.array([vy],ndmin=2).transpose()
vz = np.array([vz],ndmin=2).transpose()

phi = np.array([phi],ndmin=2).transpose()
theta = np.array([theta],ndmin=2).transpose()
psi = np.array([psi],ndmin=2).transpose()

rs = np.array([rs],ndmin=2).transpose()
ps = np.array([ps],ndmin=2).transpose()
ys = np.array([ys],ndmin=2).transpose()


u1 = np.array([u1],ndmin=2).transpose()
u2 = np.array([u2],ndmin=2).transpose()
u3 = np.array([u3],ndmin=2).transpose()
u4 = np.array([u4],ndmin=2).transpose()


# fig, ax = plt.subplots(nrows=4,ncols=3)

# ax[0][0].plot(x,'b')
# ax[0][1].plot(y,'b')
# ax[0][2].plot(z,'b')


# ax[1][0].plot(vx,'b')
# ax[1][1].plot(vy,'b')
# ax[1][2].plot(vz,'b')


# ax[2][0].plot(phi,'b')
# ax[2][1].plot(theta,'b')
# ax[2][2].plot(psi,'b')


# ax[3][0].plot(rs,'b')
# ax[3][1].plot(ps,'b')
# ax[3][2].plot(ys,'b')


# fig2, ax2 = plt.subplots(nrows=3,ncols=4)

# ax2[0][0].plot(u1,'r')
# ax2[0][1].plot(u2,'r')
# ax2[0][2].plot(u3,'r')
# ax2[0][3].plot(u4,'r')


# fig3, ax3 = plt.subplots(nrows=4,ncols=3)

# ax3[0][0].plot(phi,'b')
# ax3[0][1].plot(theta,'b')
# ax3[0][2].plot(psi,'b')

# ax3[1][0].plot(sin_phi,'b')
# ax3[1][1].plot(sin_theta,'b')
# ax3[1][2].plot(sin_psi,'b')

# ax3[2][0].plot(cos_phi,'b')
# ax3[2][1].plot(cos_theta,'b')
# ax3[2][2].plot(cos_psi,'b')

# ax3[3][0].plot(check_phi,'b')
# ax3[3][1].plot(check_theta,'b')
# ax3[3][2].plot(check_psi,'b')


# Accleration
# fig4, ax4 = plt.subplots(nrows=3,ncols=1)

# ax4[0].set_title('Linear Acceleration')

# ax4[0].plot(ac_x,'g',label='x')
# ax4[1].plot(ac_y,'g',label='y')
# ax4[2].plot(ac_z,'g',label='z')

#Velocity
# ax4[0].set_title('Linear Velocity')

# ax4[0].plot(vx,'r')
# ax4[1].plot(vy,'r')
# ax4[2].plot(vz,'r')



# Angular Accelearation
# fig5, ax5 = plt.subplots(nrows=3,ncols=1)
# ax5[0].set_title('Angular Acceleration')
# ax5[0].set_ylim(-2,2)
# ax5[0].plot(alpha_x,'g',label='x')
# ax5[1].set_ylim(-2,2)
# ax5[1].plot(alpha_y,'g',label='y')
# ax5[2].set_ylim(-2,2)
# ax5[2].plot(alpha_z,'g',label='z')


# Angular Velocity
# fig6, ax6 = plt.subplots(nrows=3,ncols=1)
# ax6[0].set_title('Angular Velocity')
# ax6[0].set_ylim(-0.2,0.2)
# ax6[0].plot(rs,'g',label='x')
# ax6[1].set_ylim(-0.2,0.2)
# ax6[1].plot(ps,'g',label='y')
# ax6[2].set_ylim(-0.2,0.2)
# ax6[2].plot(ys,'g',label='z')


# Angular Velocity
# fig7, ax7 = plt.subplots(nrows=3,ncols=1)
# ax7[0].set_title('Moving Angular Velocity')

# ax7[0].set_ylim(-0.2,0.2)
# ax7[0].plot(mv_alpha_x,'g',label='x')
# ax7[1].set_ylim(-0.2,0.2)
# ax7[1].plot(mv_alpha_y,'g',label='y')
# ax7[2].set_ylim(-0.2,0.2)
# ax7[2].plot(mv_alpha_z,'g',label='z')

plt.show()
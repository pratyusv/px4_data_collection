import numpy as np
import matplotlib.pyplot as plt
import math

data_dir = "../data/"
control_dir = "../data/"
acc_dir = "../data/"

state = np.load(data_dir+"states/s_y.npy")
control = np.load(control_dir + "controls/u_y.npy")
acc  = np.load(acc_dir + "acc/a_y.npy")

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

check_phi = []
check_theta  = []
check_psi = []

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


	rs.append(state[row,12] *10)
	ps.append(state[row,13] *10)
	ys.append(state[row,14] *10)

	phi.append(state[row,15] *10)
	theta.append(state[row,16]*10)
	psi.append(state[row,17]*10)

	check_phi.append(math.sin(state[row,15]))
	check_theta.append(math.sin(state[row,16]))
	check_psi.append(math.sin(state[row,17]))

	u1.append(control[row,0]*10)
	u2.append(control[row,1]*10)
	u3.append(control[row,2]*10)
	u4.append(control[row,3]*10)


	ac_x.append(acc[row,0])
	ac_y.append(acc[row,1])
	ac_z.append(acc[row,2])

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


fig, ax = plt.subplots(nrows=4,ncols=3)

ax[0][0].plot(x,'b')
ax[0][1].plot(y,'b')
ax[0][2].plot(z,'b')


ax[1][0].plot(vx,'b')
ax[1][1].plot(vy,'b')
ax[1][2].plot(vz,'b')


ax[2][0].plot(phi,'b')
ax[2][1].plot(theta,'b')
ax[2][2].plot(psi,'b')


ax[3][0].plot(rs,'b')
ax[3][1].plot(ps,'b')
ax[3][2].plot(ys,'b')


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


# fig4, ax4 = plt.subplots(nrows=2,ncols=3)

# ax4[0][0].plot(ac_x,'g')
# ax4[0][1].plot(ac_y,'g')
# ax4[0][2].plot(ac_z,'g')

# ax4[1][0].plot(vx,'r')
# ax4[1][1].plot(vy,'r')
# ax4[1][2].plot(vz,'r')

plt.show()
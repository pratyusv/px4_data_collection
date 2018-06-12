import numpy as np
import math
import matplotlib.pyplot as plt

x = []
y = []

PI = np.pi

angle = 0.0
theta = 0

ref = []
temp_x = 0.0
temp_y = 0.0
x_step = 0.0

# r = np.random.uniform(1500,1)*10
# theta = 0.0  

# for row in xrange(0,100):
# 	val = np.random.uniform(-1,1)
# 	for t in xrange(0,50):
# 		x.append(x_step)
# 		y.append(val*5*mt.sin(theta*PI/6) )
# 		x_step += 0.01 
# 		theta += 1.0/40

# for _ in range(0,3000):
	# temp_y = mt.sin(mt.radians(2*theta/15)) + mt.cos(mt.radians(2*theta/15))-1
	# temp_y  = 10 + 2.0*mt.sin(theta*PI/6) + 2.0*mt.cos(theta*PI/6) -2 
	# temp_x = theta
	# theta += 1.0/100
	# x_step = x_step + 0.01
	# x.append(temp_x)
	# y.append(temp_y)
	# print("x = ",'{:.3f}'.format(temp_x),   "y = ", '{:.3f}'.format(temp_y))

# for _ in range(0,10000):
# 	x.append(2.0*mt.cos(theta*PI/6) + 2.0*mt.cos(theta*PI/3))
# 	y.append(theta)
# 	theta += 1.0/100


r = np.random.rand(100,1) * 5
# r = np.sort(r,axis=0)

x_trgt = []
y_trgt = []

row = 0
theta = 0.0
x_step = 0.0
for t in xrange(0,50):
	# val = np.random.uniform(0,0.5)*5
	y_step = 0.0
	for p in xrange(0,50):
		x_trgt.append(x_step)
		y_trgt.append(r[t,0] + y_step)
		x_step += 0.01
		y_step += 0.01
		theta += 1.0/100


alpha = 0.5
temp = 0.0
y_new = []
for row in range(0,len(y_trgt)):
	temp = temp + alpha*(y_trgt[row] - temp)
	y_new.append(temp)

fig,ax = plt.subplots(nrows=2,ncols=1)

# ax[0].plot(x_trgt[0:20],y_new[0:20],'b',label='predictions')
ax[0].plot(x_trgt,y_new,'b',label='predictions')

# ax[1].plot(y_trgt,'b',label='predictions')


plt.show()
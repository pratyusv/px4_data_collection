import numpy as np

x = np.array([[1,2,3], [4,5,6],[7,8,9]],ndmin=2)

for col in xrange(0,x.shape[1]):
	x[:,col] = ( x[:,col] - x[:,col].mean() ) / x[:,col].std()

print(x)
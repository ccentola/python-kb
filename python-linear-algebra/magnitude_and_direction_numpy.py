import numpy as np
from scipy import linalg
from sklearn import preprocessing

# magnitude
## problem 1
v = np.array([-0.221,7.437])
print(np.linalg.norm(v))

# solution: 7.440282924728065

## problem 2
v = np.array([8.813,-1.331,-6.247])

print(np.linalg.norm(v))

# solution: 10.884187567292289

# L2 Normalization
## problem 1
v = np.array([5.581,-2.136])

print(v/np.linalg.norm(v))

# solution: [ 0.93393521 -0.35744233]

## problem 2
v = np.array([1.996,3.108,-4.554])

print(v/np.linalg.norm(v))

# solution: [ 0.3404013   0.5300437  -0.77664704]
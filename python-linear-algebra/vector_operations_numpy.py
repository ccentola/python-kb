import numpy as np
from scipy import linalg

# addition
v = [8.218,-9.341]
w = [-1.129,2.111]

print(np.add(v,w))

# answer: [ 7.089 -7.23 ]

# subtraction
v = [7.119,8.215]
w = [-8.223,0.878]

print(np.subtract(v,w))

# answer: [ 15.342   7.337]

# multiplication
v = [1.617,-1.012,-0.318]
c = 7.41

print(np.multiply(v,c))

# answer: [ 11.98197  -7.49892  -2.35638]
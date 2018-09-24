import numpy as np
from scipy import linalg
from math import pi

# dot product
## problem 1
v = np.array([7.887,4.138])
w = np.array([-8.802,6.776])

print(np.dot(v,w))

# solution: -41.3822859999999945439839166283

## problem 2
v = np.array([-5.955,-4.904,-1.874])
w = np.array([-4.496,-8.755,7.103])

print(np.dot(v,w))

# # solution: 56.3971780000000056997571107331

# angle

# helper functions
def unit_vector(v):
    '''Returns the unit vector of the vector.'''
    return v / np.linalg.norm(v)

def angle_between(v, w, in_degrees=False):
    '''Returns the angle in radians between vectors v and w.'''
    v_u = unit_vector(v)
    w_u = unit_vector(w)
    angle_in_radians = np.arccos(np.clip(np.dot(v_u, w_u), -1.0, 1.0))
    
    if in_degrees:
        degrees_per_radian = 180 / pi
        return angle_in_radians * degrees_per_radian
    else:
        return angle_in_radians

## problem 1
v = np.array([3.183,-7.627])
w = np.array([-2.668,5.319])

print(angle_between(v,w))

# solution: 3.0720263098372476

# ## problem 2
v = np.array([7.35,0.221,5.188])
w = np.array([2.751,8.259,3.985])

print(angle_between(v,w,in_degrees=True))

# solution: 60.27581120523091
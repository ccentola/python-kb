from vectors import Vector

# addition
v = Vector([8.218,-9.341])
w = Vector([-1.129,2.111])

print(v.plus(w))

# subtraction
v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])

print(v.minus(w))

# multiplication
v = Vector([1.617,-1.012,-0.318])
c = 7.41

print(v.times_scalar(c))

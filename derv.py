# from collections import namedtuple
# import sympy as sp
# n = sp.Symbol('n')
# a = sp.Symbol('a')
# b = sp.Symbol('b')

# position = [i for i in [2*n-n**2,-.5*7*n**2+2,0]]
# print(position)

# positionDerv = [sp.diff(i, n) for i in position]

# positionDervSquaredSum = sum([i**2 for i in positionDerv])

# unitVectorPositionDerv = [i / positionDervSquaredSum for i in positionDerv]

# arcLengthDerv = sp.sqrt(sum([i**2 for i in positionDerv]))

# g = 9.8

# v0 = 2

# energyConstant = g*position[1].subs(n, 0)+.5*v0**2

# velocity = sp.sqrt(2*(energyConstant-g*position[1]))

# vectorizedVelocity = [velocity*i for i in unitVectorPositionDerv]

# timeDerv = arcLengthDerv / velocity

# linearAcceleration = sp.diff(velocity, n) / timeDerv

# print(linearAcceleration)

# vectorizedAccelerationWithMotionAndGravityOffset = [vectorizedVelocity[i]/timeDerv - linearAcceleration*unitVectorPositionDerv[i] for i in range(len(position))]

# print(vectorizedAccelerationWithMotionAndGravityOffset)
a = {"hi","five","one","hi"}
print(a)
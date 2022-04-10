
import sympy as sp
n = sp.Symbol('n')

position = [i for i in [2*n-n**2,-.5*7*n**2+2,0]]

# position = [i for i in [2*n,.5*-9.8*n**2,0]]

print("Position:", position)

positionDerv = [sp.diff(i, n) for i in position]
1
positionDervMagnitude = sp.sqrt(sum([i**2 for i in positionDerv]))

unitVectorPositionDerv = [i / positionDervMagnitude for i in positionDerv]

arcLengthDerv = sp.sqrt(sum([i**2 for i in positionDerv]))

g = 9.8

v0 = 2

energyConstant = g*position[1].subs(n, 0)+.5*v0**2

velocity = sp.sqrt(2*(energyConstant-g*position[1]))

vectorizedVelocity = [velocity*i for i in unitVectorPositionDerv]

timeDerv = arcLengthDerv / velocity

print("Velocity:", velocity)

linearAcceleration = sp.diff(velocity, n) / timeDerv

print("Acceleration 1:", linearAcceleration)

vectorizedAccelerationWithMotionAndGravityOffset = [sp.diff(vectorizedVelocity[i],n)/timeDerv - linearAcceleration*unitVectorPositionDerv[i] for i in range(len(position))]

#to check that they are perp.
# print("Dot Product:", sum([vectorizedAccelerationWithMotionAndGravityOffset[i] * unitVectorPositionDerv[i] for i in range(len(position))]).subs(n, 0.5))

print(vectorizedAccelerationWithMotionAndGravityOffset[0].subs(n, 1), vectorizedAccelerationWithMotionAndGravityOffset[1].subs(n, 1))

vectorizedAccelerationWithMotionAndGravityOffset[1] += g

scalarProject = sum([vectorizedAccelerationWithMotionAndGravityOffset[i]*sp.sqrt(1-(unitVectorPositionDerv[i])**2) for i in range(len(position))])

# scalarProject += g*sp.sqrt(1-(unitVectorPositionDerv[1])**2)

# vectorizedAccelerationWithMotionAndGravityOffset[1] += g

print("Acceleration 2:", vectorizedAccelerationWithMotionAndGravityOffset)

print(vectorizedAccelerationWithMotionAndGravityOffset[0].subs(n, 0), vectorizedAccelerationWithMotionAndGravityOffset[1].subs(n, 0))


print(scalarProject)
print(scalarProject.subs(n, 0.01))
from math import cos, sin
from Matrix import Matrix
from Vector import Vector, Vector3


class Quaternion(Vector): 
    @staticmethod
    def fromEulerVector(v:Vector3):
        c0 = cos(v.x/2)
        c1 = cos(v.y/2)
        c2 = cos(v.z/2)
        s0 = sin(v.x/2)
        s1 = sin(v.y/2)
        s2 = sin(v.z/2)

        return Quaternion(
            s0 * c1 * c2 - c0 * s1 * s2,
            c0 * s1 * c2 + s0 * c1 * s2,
            c0 * c1 * s2 - s0 * s1 * c2,
            c0 * c1 * c2 + s0 * s1 * s2
        )
    @staticmethod
    def zeros():
        return Quaternion(0, 0, 0, 0)
    
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z, w)

    def toRotationMatrix(self):
        m = Matrix.fromSize(3, 3, 0)
        m[0][0] = 1 - 2*(self[1]*self[1] + self[2]*self[2])
        m[0][1] = 2 * (self[0]*self[1] - self[3]*self[2])
        m[0][2] = 2 * (self[3]*self[1] + self[0]*self[2])

        m[1][0] = 2 * (self[0]*self[1] + self[3]*self[2])
        m[1][1] = 1 - 2*(self[0]*self[0] + self[2]*self[2])
        m[1][2] = 2 * (-self[3]*self[0] + self[1]*self[2])

        m[2][0] = 2 * (-self[3]*self[1] + self[0]*self[2])
        m[2][1] = 2 * (self[3]*self[0] + self[1]*self[2])
        m[2][2] = 1 - 2*(self[0]*self[0] + self[1]*self[1])
        return m
    
    #conjugate
    def __neg__(self):
        return Quaternion(-self.x, -self.y, -self.z, self.w)

    def __invert__(self):
        c = (-self)
        m = abs(self)
        m = m*m
        return Quaternion(c.x / m, c.y / m, c.z / m, c.w / m)

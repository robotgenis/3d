from math import sqrt, cos, sin
from operator import itemgetter
from LengthList import LengthList

def isNumber(x):
    return isinstance(x, (int, float, complex, bool))

class Vector(LengthList):
    @staticmethod
    def zeros(size):
        return Vector(*(0 for _ in range(size)))
    @staticmethod
    def direction(size, axis):
        return Vector(*(int(axis==i) for i in range(size)))

    x = property(itemgetter(0))
    y = property(itemgetter(1))
    z = property(itemgetter(2))
    w = property(itemgetter(3))


    # Mathmetical
    def __add__(self, v):
        t = self.copy()
        t += v
        return t
    def __iadd__(self, v):
        for i in range(len(self)):
            self[i] += v[i]
        return self
    def __sub__(self, v):
        t = self.copy()
        t -= v
        return t
    def __isub__(self, v):
        for i in range(len(self)):
            self[i] -= v[i]
        return self
    def __mul__(self, v):
        t = self.copy()
        t *= v
        return t
    def __imul__(self, v):
        if isNumber(v):
            for i in range(len(self)):
                self[i] *= v
        else:
            for i in range(len(self)):
                self[i] *= v[i]
        return self
    def __truediv__(self, v):
        t = self.copy()
        t /= v
        return t
    def __itruediv__(self, v):
        if isNumber(v):
            for i in range(len(self)):
                self[i] /= v
        else:
            for i in range(len(self)):
                self[i] /= v[i]
        return self
    def __floordiv__(self, v):
        t = self.copy()
        t //= v
        return t
    def __floordiv__(self, v):
        if isNumber(v):
            for i in range(len(self)):
                self[i] //= v
        else:
            for i in range(len(self)):
                self[i] //= v[i]
        return self
    def __abs__(self):
        return sqrt(sum(i**2 for i in self))
    def __neg__(self):
        return self.copy() * -1
    
    # Dot product
    def dot(self, other):
        return sum(self[i] * other[i] for i in range(len(self)))

class Vector3(Vector):
    @staticmethod
    def zeros():
        return Vector3(0, 0, 0)
    @staticmethod
    def direction(axis):
        return Vector(*(int(axis==i) for i in range(3)))

    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    # Cross Product
    def cross(self, other):
        return Vector3(self[1]*other[2] - self[2]*other[1], self[2]*other[0] - self[0]*other[2], self[0]*other[1] - self[1]*other[0])


class Vector2(Vector):
    @staticmethod
    def zeros():
        return Vector2(0, 0)
    @staticmethod
    def direction(axis):
        return Vector(*(int(axis==i) for i in range(2)))

    def __init__(self, x, y):
        super().__init__(x, y)

    

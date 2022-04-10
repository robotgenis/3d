from math import sqrt
from operator import itemgetter
def isNumber(x):
    return isinstance(x, (int, float, complex, bool))

class Vector(list):
    __slots__ = []
            
    x = property(itemgetter(0))
    y = property(itemgetter(1))
    z = property(itemgetter(2))
    w = property(itemgetter(3))

    def __init__(self, *v):
        super().__init__(v)
    
    # Representations
    def __repr__(self):
        return f"<{', '.join(map(str, self))}>"

    # Resources
    def copy(self):
        return Vector(*self)

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
    def __matmul__(self, other):
        return sum(self[i] * other[i] for i in range(len(self)))


class Vector3(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
    
    # Cross Product
    def cross(self, other):
        return Vector3(self[1]*other[2] - self[2]*other[1], self[2]*other[0] - self[0]*other[2], self[0]*other[1] - self[1]*other[0])


class Vector2(Vector):
    def __init__(self, x, y):
        super().__init__(x, y)



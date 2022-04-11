from operator import attrgetter
from LengthList import FinalLengthList, LengthList
from Vector import Vector

class Matrix(FinalLengthList):
    @staticmethod
    def fromSize(h, w, val):
        return Matrix(*(LengthList(*(val for _ in range(w))) for _ in range(h)))
    @staticmethod
    def zeros(h, w):
        return Matrix(*(LengthList(*(0 for _ in range(w))) for _ in range(h)))
    @staticmethod
    def ones(n):
        return Matrix(*(LengthList(*(int(x==y) for x in range(n))) for y in range(n)))

    __slots__ = "__width", "__height"
    width = property(attrgetter("__width"))
    height = property(attrgetter("__height"))

    def __init__(self, *rows):
        super().__init__(*rows)
        self.__height = len(rows)
        self.__width = len(rows[0])
    
    def copy(self):
        return Matrix(*(LengthList(*(self[y][x] for x in range(self.__width))) for y in range(self.__height)))

    def __repr__(self):
        return "\n".join("|" + ", ".join(map(str, row)) + "|" for row in self)

    # Mathematics
    def __add__(self, other):
        m = self.copy()
        m += other
        return m
    def __iadd__(self, other):
        for x in range(self.__width):
            for y in range(self.__height):
                self[y][x] += other[y][x]
        return self
    def __sub__(self, other):
        m = self.copy()
        m -= other
        return m
    def __isub__(self, other):
        for x in range(self.__width):
            for y in range(self.__height):
                self[y][x] -= other[y][x]
        return self
    def __matmul__(self, other):
        n = self.__width
        return Matrix(*[[sum(self[y][i] * other[i][x] for i in range(n)) for x in range(other.__width)] for y in range(self.__height)])

    def mutliplyMatrixByVector(self, v):
        return Vector(*(v.dot(self[i]) for i in range(len(v))))
    def multiplyVectorByMatrix(self, v):
        return Vector(*(v.dot(self[i]) for i in range(len(v))))
        

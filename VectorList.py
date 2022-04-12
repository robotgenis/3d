

class VectorList(list):
    __slots__ = []
    
    def __init__(self, *v):
        super().__init__(v)
    
    def average(self):
        l =  len(self)
        s = self[0].copy()
        for i in range(1, l):
            s += self[i]
        s /= l
        return s

    def toTuple(self):
        return tuple(i for v in self for i in v)


class VectorList3(VectorList):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
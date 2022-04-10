
from operator import itemgetter
from Vector import *



class VectorList(list):
    __slots__ = []
            
    a = property(itemgetter(0))
    b = property(itemgetter(1))
    c = property(itemgetter(2))
    
    def __init__(self, *v):
        super().__init__(v)
    

    def average(self, ):
        l =  len(self)
        s = self[0].copy()
        for i in range(1, l):
            s += self[i]
        s /= l
        return s
    

class VectorList3(VectorList):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    


from Obj3D import Obj3D

from Triangle import Triangle
from Vector import Vec

from math import *

class ParametricGraph3D(Obj3D):
    def __init__(self) -> None:    
        super().__init__()
        self.equation = ("T", "T", "T");
        self.range = (0, 2);
        self.step = 0.5
    def unpackGraph(self):
        t = self.range[0]
        self.subset = []
        prev = [eval(i.replace("T", str(t))) for i in self.equation]
        while t < self.range[1]:
            t += self.step
            point = [eval(i.replace("T", str(t))) for i in self.equation]
            
            a = Vec(prev[0], prev[1], prev[2])
            b = Vec(point[0], point[1], point[2])
            c = a.copy()
            c.y -= 0.1
            d = b.copy()
            d.y -= 0.1
            
            
            self.subset.append(Triangle(a, b, c, self.material))
            self.subset.append(Triangle(b, c, d, self.material))
            
            prev = point
            
            
            
            
            
            
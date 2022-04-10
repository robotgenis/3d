

from Obj3D import Obj3D

from math import pi, sqrt
from Triangle import Triangle

from Vector import Vec

class Camera(Obj3D):
    def __init__(self) -> None:
        """Camera object for 3D engine
        """        
        super().__init__()
        self.fov = pi / 2
    def renderVecScreenPos(self, delta:Vec, focalScalar:float) -> Vec:
        return Vec(
            delta.z / delta.x / focalScalar,
            delta.y / delta.x / focalScalar,
            sqrt(delta.x*delta.x + delta.y*delta.y + delta.z*delta.z)
        )
    def renderTriangleScreenPos(self, triangle:Triangle, focalScalar:float) -> Triangle:
        return Triangle(
            self.renderVecScreenPos(triangle.a, focalScalar),
            self.renderVecScreenPos(triangle.b, focalScalar),
            self.renderVecScreenPos(triangle.c, focalScalar),
            triangle.material
        )
        
        
        

from Camera import Camera
from Obj3D import Obj3D
from Quaternion import RotationMatrix
from Triangle import Triangle

from math import sqrt, tan

from Vector import Vec

class Scene:
    def __init__(self):
        """Scene object for 3D Enginer class
        """        
        self.activeCamera = Camera()
        self.objects = []        
    def render(self) -> list[Triangle]:
        """Render function to render all objects in the scene

        Returns:
            [type]: [description]
        """        
        rot = RotationMatrix().fromQuaternion(self.activeCamera.rot)
        
        focalScalar = tan(self.activeCamera.fov / 2)
        
        triangles = []
        
        
        
        for i in self.objects:
            if isinstance(i, Triangle):
                triangles.append(i)
            if isinstance(i, Obj3D):
                triangles.extend(i.unpackSubset())
        
        deltas = []
        for i in triangles:
            deltas.extend(i.renderVectorPos(self.activeCamera.pos, rot))

        for i in range(len(deltas)):
            deltas[i] = self.activeCamera.renderTriangleScreenPos(deltas[i], focalScalar)
                
        
        deltas.sort(key=lambda x: x.average().z, reverse=True)

        return deltas
                
from abc import abstractmethod
from Object3D import Object3D
from VectorList import VectorList
from Vector import Vector2
import pyglet


class Material:
    @abstractmethod
    def draw(self, obj3D, batch):
        pass

class MaterialColor(Material):
    __slots__ = "color"
    def __init__(self, color):
        self.color = color
    def draw(self, obj3D, batch):
        for t in obj3D.subset:
            batch.add(3, pyglet.graphics.GL_TRIANGLES, None, 
                ('v2f', t.toTuple()),
                ('c3B', self.color * 3)
            )

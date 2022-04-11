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


window = pyglet.window.Window()

o = Object3D()
o.subset.append(VectorList(Vector2(0, 0), Vector2(500, 500), Vector2(0, 500)))

m = MaterialColor()

batch = pyglet.graphics.Batch()
# a = pyglet.shapes.Triangle(0, 0, 100, 100, 0, 100, batch=batch)
m.draw(o, batch)


@window.event
def on_draw():
    # window.clear()

    batch.draw()


pyglet.app.run()
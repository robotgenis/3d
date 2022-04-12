from Engine3D import *



a = Object3D()
a.subset.append(VectorList(Vector2(0, 0), Vector2(500, 500), Vector2(0, 500)))


b = Object3D()
b.subset.append(VectorList(Vector2(100, 100), Vector2(200, 200), Vector2(100, 200)))
b.subset.append(VectorList(Vector2(5, 5), Vector2(5, 7), Vector2(7, 7)))


s = Scene()
s.subset.append(a)
s.subset.append(b)

s.render(1)

# m = MaterialColor((0, 100, 0))

# batch = pyglet.graphics.Batch()
# m.draw(o, batch)


# @window.event
# def on_draw():
#     # window.clear()

#     batch.draw()


# pyglet.app.run()
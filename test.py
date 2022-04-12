from Engine3D import *
from random import randint


m = Vector3(0, 0, 0)

a = Object3DMaterial(MaterialColor((0, 100, 0)))
a.subset.append(VectorList(Vector3(1, 0, 0), Vector3(1, 0, 1), Vector3(1, 1, 0)))

s = Scene()


for x in range(5):
    for y in range(5):
        for z in range(5):
            a = Object3DMaterial(MaterialColor((randint(0, 255), randint(0, 255), randint(0, 255))))
            a.subset.append(VectorList(Vector3(z, y, x), Vector3(z, y, x+1), Vector3(z, y + 1, x)))
            s.subset.append(a)

window = Window3D(s)


@window.loop
def loop(keys, mouse):
    global m
    delta = Vector3.zeros()

    change = 0.02
    if keys[key.LSHIFT]:
        change = 0.05
    if keys[key.D]:
        delta[2] += change
    if keys[key.A]:
        delta[2] -= change
    if keys[key.W]:
        delta[0] += change
    if keys[key.S]:
        delta[0] -= change
    if keys[key.Q]:
        delta[1] += change
    if keys[key.E]:
        delta[1] -= change
    if keys[key.R]:
        m = Vector3(0, 0, 0)

    
    dir = m.copy()
    dir[2] = 0
    moveDir = Quaternion.fromEulerVector(dir)

    delta = (~moveDir).toRotationMatrix().mutliplyMatrixByVector(delta)
    window.scene.camera.transformation.position += delta
    
    m[1] += mouse["dx"] / 100
    m[2] += -mouse["dy"] / 100
    
    window.scene.camera.transformation.quaternion = Quaternion.fromEulerVector(m)

    
    window.width = 1000
    window.height = 1000

window.set_vsync(False)
window.run()

# a = Object3DMaterial(MaterialColor((0, 100, 0)))
# a.subset.append(VectorList(Vector3(1, 0, 0), Vector3(1, 0, 1), Vector3(1, 1, 0)))


# # b = Object3D()
# # b.subset.append(VectorList(Vector2(100, 100), Vector2(200, 200), Vector2(100, 200)))
# # b.subset.append(VectorList(Vector2(5, 5), Vector2(5, 7), Vector2(7, 7)))


# s = Scene()
# s.subset.append(a)
# # s.subset.append(b)

# # s.camera.transformation.quaternion = Quaternion.fromEulerVector(Vector3(0, 0.1, 0))



# # m = MaterialColor((0, 100, 0))
# window = pyglet.window.Window()

# r = 0

# def update(dt, dtb):
#     window.clear()
#     global r
#     s.camera.transformation.quaternion = Quaternion.fromEulerVector(Vector3(0, r, 0))
#     r += 0.01

#     st = time()
#     batch = pyglet.graphics.Batch()
#     s.render(batch)

#     batch.draw()
#     print(time() - st)

# @window.event
# def on_draw():
#     pass


# pyglet.clock.schedule(update, 1/20)
# pyglet.app.run()


# from Triangle import Triangle
# from Vector import Vec
# from Window3D import Window3D
from Color import ColorRGB1
from Engine3D import *

a = Window3D()

# a.scene.activeCamera.pos.z = 1
m = Vec(0, 0, 0)

a.scene.activeCamera.rot.fromVecEuler(m)

o = Obj3D()
o.subset.append(Triangle(Vec(1, 0, 0), Vec(1, 0, 1), Vec(1, 1, 0)))
o.material = MaterialColor(ColorRGB1(1,0,0))
o.unpackColor()
a.scene.objects.append(o)

a.scene.objects.append(Triangle(Vec(3, 0, 0), Vec(3, 0, 1), Vec(3, 1, 0), MaterialColor(ColorRGB1(0,1,0))))
a.scene.objects.append(Triangle(Vec(2, 0, 0), Vec(2, 0, 1), Vec(2, 1, 0), MaterialColor(ColorRGB1(0,0,1))))

def loop(keys, mouse):
    
    delta = Vec()
    change = 0.01
    if keys[key.D]:
        delta.z += change
    if keys[key.A]:
        delta.z -= change
    if keys[key.W]:
        delta.x += change
    if keys[key.S]:
        delta.x -= change
    if keys[key.Q]:
        delta.y += change
    if keys[key.E]:
        delta.y -= change
    dir = m.copy()
    dir.z = 0
    moveDir = Quaternion().fromVecEuler(dir) 
    delta = RotationMatrix().fromQuaternion(moveDir.inverse()).applyTo(delta)
    a.scene.activeCamera.pos += delta
    
    m.y += mouse["dx"] / 100
    m.z += -mouse["dy"] / 100
    
    a.scene.activeCamera.rot.fromVecEuler(m)
    
    a.width = 1000
    a.height = 1000
    

a.run(loop)



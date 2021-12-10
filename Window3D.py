from __future__ import annotations

import pyglet
from Material import MaterialColor, MaterialNone

from Scene import Scene

class Window3D(pyglet.window.Window):
    def __init__(self):
        super(Window3D, self).__init__()
        self.scene = Scene()
        self.keyHandler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyHandler)
        self.mouseDelta = {"dx":0, "dy":0, "delay":100}
    def render(self):
        triangles = self.scene.render()
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        pyglet.gl.glColor3f(1,0,0)
        scale = self.width / 2
        xStart = self.width / 2
        yStart = self.height / 2
        for i in triangles:
            if(isinstance(i, MaterialNone)):  
                pyglet.gl.glColor3f(1,0,0)
            if(isinstance(i.material, MaterialColor)):
                iColor = i.material.color
                pyglet.gl.glColor3f(iColor.r, iColor.g, iColor.b)
            a = pyglet.graphics.vertex_list(3, ('v2f', [
                i.a.x * scale + xStart, i.a.y * scale + yStart, 
                i.b.x * scale + xStart, i.b.y * scale + yStart, 
                i.c.x * scale + xStart, i.c.y * scale + yStart
            ]))
            a.draw(pyglet.gl.GL_TRIANGLES)
    def on_mouse_motion(self, x, y, dx, dy):
        if self.mouseDelta["delay"] == 0:
            self.mouseDelta["dx"] += dx
            self.mouseDelta["dy"] += dy
    def on_draw(self):
        self.render()
    def update(self, dt, dtb):
        self.userLoop(self.keyHandler, self.mouseDelta)
        self.mouseDelta["dx"] = 0
        self.mouseDelta["dy"] = 0
        if self.mouseDelta["delay"] > 0: self.mouseDelta["delay"] -= 1
        self.render()
    def run(self, loop):
        self.userLoop = loop
        pyglet.clock.schedule(self.update, 1/30)
        pyglet.app.run()
        
    
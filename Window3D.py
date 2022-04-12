from Scene import Scene
import pyglet
from time import time


class Window3D(pyglet.window.Window):
    __slots__ = "scene", "__keyHandler", "mouseDelta", "__userLoop"
    def __init__(self, scene = Scene()):
        super(Window3D, self).__init__()
        self.scene = scene
        self.__keyHandler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.__keyHandler)
        self.mouseDelta = {"dx":0, "dy":0}
    def render(self):
        # time1 = time()
        self.clear()
        batch = pyglet.graphics.Batch()
        # time2 = time()
        self.scene.render(batch, self.width, self.height)
        # time3 = time()
        batch.draw()
        # time4 = time()
        # print(time2 - time1, time3 - time2, time4 - time3)
    def on_mouse_motion(self, x, y, dx, dy):
        self.mouseDelta["dx"] += dx
        self.mouseDelta["dy"] += dy
    def on_draw(self):
        self.render()
    def update(self, dt, dtb):
        self.__userLoop(self.__keyHandler, self.mouseDelta)
        self.mouseDelta["dx"] = 0
        self.mouseDelta["dy"] = 0
        self.render()
    def loop(self, loop):
        self.__userLoop = loop
    def run(self):
        pyglet.clock.schedule(self.update, 1/120)
        pyglet.app.run()
        
    
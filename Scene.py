from Camera import Camera
from Object3D import Object3D

class Scene(Object3D):
	__slots__ = "camera"
	def __init__(self):
		super().__init__()
		self.camera = Camera()
	def render(self, batch):
		renderPacket = self.unpack()

		triangles = self.camera.render(renderPacket)

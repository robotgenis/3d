from Camera import Camera
from Object3D import Object3D
from Vector import Vector2
from time import time

class Scene(Object3D):
	__slots__ = "camera"
	def __init__(self):
		super().__init__()
		self.camera = Camera()
	def render(self, batch, width, height):
		time1 = time()
		renderPacket = self.unpack()

		time2 = time()

		triangles = self.camera.render(renderPacket)

		time3 = time()

		scale = max(width, height)

		time4 = time()

		for i in range(len(triangles)):
			for k in range(len(triangles[i][1])):
				triangles[i][1][k] = triangles[i][1][k] * scale + Vector2(width / 2, height / 2) 

		time5 = time()

		for tri in triangles:
			tri[0].draw(tri[1], batch)
		
		time6 = time()

		show1 = round(time2 - time1, 3)
		show2 = round(time3 - time2, 3)
		show3 = round(time4 - time3, 3)
		show4 = round(time5 - time4, 3)
		show5 = round(time6 - time5, 3)
		print(show1, show2, show3, show4, show5)


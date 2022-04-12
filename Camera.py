from Object3D import Object3D
from math import pi
from Vector import Vector3


class Camera(Object3D):
	__slots__ = "fieldOfView"
	def __init__(self, fov = pi / 2):
		super().__init__()
		self.fieldOfView = fov
	def render(self, renderPacket):
        #TODO
		pass
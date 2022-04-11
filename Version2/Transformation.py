from Vector import Vector3
from Quaternion import Quaternion


class Transformation3D():
	__slots__ = 'position', 'quaternion'
	def __init__(self, position=Vector3.zeros(), quaternion=Quaternion.zeros()):
		self.position = position
		self.quaternion = quaternion
from Transformation import Transformation3D


class Object3D():
	__slots__ = 'transformation', 'subset'
	def __init__(self, transformation3D=Transformation3D()):
		self.transformation = transformation3D
		self.subset = []


class Object3DMaterial(Object3D):
	__slots__ = 'material'
	def __init__(self, material, transformation3D=Transformation3D()):
		super().__init__(transformation3D)
		self.material = material
from Transformation import Transformation3D


class Object3D():
	__slots__ = 'transformation', 'subset'
	def __init__(self, transformation3D=Transformation3D()):
		self.transformation = transformation3D
		self.subset = []
	def unpack(self):
		arr = []
		for item in self.subset:
			if isinstance(item, Object3D):
				arr.extend(item.unpack())
			else:
				arr.append((None, item))
		return arr


class Object3DMaterial(Object3D):
	__slots__ = 'material'
	def __init__(self, material, transformation3D=Transformation3D()):
		super().__init__(transformation3D)
		self.material = material
	def unpack(self):
		arr = []
		for item in self.subset:
			if isinstance(item, Object3D):
				arr.extend(item.unpack())
			else:
				arr.append((self.material, item))
		return arr
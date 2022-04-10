
from Color import ColorRGB1

class Material:
    def __init__(self):
        pass

class MaterialColor(Material):
    def __init__(self, colorRGB1:ColorRGB1 = ColorRGB1()):
        super().__init__()
        self.color = colorRGB1

class MaterialNone(Material):
	def __init__(self):
		super().__init__()

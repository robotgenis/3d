class ColorRGB256():
    def __init__(self, r:float = 0, g:float = 0, b:float = 0):
        self.r = r
        self.g = g
        self.b = b
    def toColorRGB1(self):
        return ColorRGB1(self.r / 256.0, self.g / 256.0, self.b / 256.0)

class ColorRGB1():
    def __init__(self, r:float = 0, g:float = 0, b:float = 0):
        self.r = r
        self.g = g
        self.b = b
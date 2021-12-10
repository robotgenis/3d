from Material import MaterialNone
from Quaternion import Quaternion
from Triangle import Triangle
from Vector import Vec


class Obj3D:
    def __init__(self) -> None:
        """Object class for 3D objects in 3D Engine
        """
        self.pos = Vec()
        self.rot = Quaternion()
        self.subset = []
        self.material = MaterialNone()
    def unpackColor(self, applyToSubObjects: bool = False) -> None:
        for i in self.subset:
            if isinstance(i, Triangle):
                i.material = self.material
            if isinstance(i, Obj3D):
                if applyToSubObjects:
                    i.material = self.material
                    i.unpackColor(applyToSubObjects = True)
    def unpackSubset(self) -> list[Triangle]:
        unpacked = []
        for i in self.subset:
            if isinstance(i, Triangle):
                unpacked.append(i)
            if isinstance(i, Obj3D):
                unpacked.append(i.unpackSubset())
        return unpacked
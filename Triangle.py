from __future__ import annotations

from Material import Material, MaterialNone
from Quaternion import RotationMatrix

from Vector import Vec


class Triangle:
    def __init__(self, a:Vec=Vec(), b:Vec=Vec(), c:Vec=Vec(), material:Material=MaterialNone()) -> None:
        """Triangle Object to handle 3 Vec points

        Args:
            a (Vec, optional): First point of triangle. Defaults to Vec().
            b (Vec, optional): Second point of triangle. Defaults to Vec().
            c (Vec, optional): Third point of triangle. Defaults to Vec().
            material (Material, optional): Material for the triangle to be drawn with. Defaults to MaterialNone().
        """        
        self.a = a
        self.b = b
        self.c = c
        self.material = material
    def average(self) -> Vec:
        """Returns average of 3 points

        Returns:
            Vec: average of 3 points
        """        
        return Vec(
            (self.a.x + self.b.x + self.c.x) / 3,
            (self.a.y + self.b.y + self.c.y) / 3,
            (self.a.z + self.b.z + self.c.z) / 3
        ) 
    def __str__(self) -> str:
        """creates string of the traingle

        Returns:
            str: string of all three points in triangle
        """        
        return self.a.__str__() + " - " + self.b.__str__() + " - " + self.c.__str__()
    def renderVectorPos(self, cameraPos:Vec, rotationMatrix:RotationMatrix) -> list[Triangle]:
        aDelta = self.a - cameraPos
        bDelta = self.b - cameraPos
        cDelta = self.c - cameraPos
        
        aDelta = rotationMatrix.applyTo(aDelta)
        bDelta = rotationMatrix.applyTo(bDelta)
        cDelta = rotationMatrix.applyTo(cDelta)
        
        if bDelta.x < aDelta.x:
            aDelta, bDelta = bDelta, aDelta
        if cDelta.x < aDelta.x:
            aDelta, bDelta, cDelta = cDelta, aDelta, bDelta
        if cDelta.x < bDelta.x:
            bDelta, cDelta = cDelta, bDelta
            
        minX = 0.001
        
        aBehindCamera = aDelta.x < minX
        bBehindCamera = bDelta.x < minX
        cBehindCamera = cDelta.x < minX
        
        if aBehindCamera and bBehindCamera and cBehindCamera:
            return []
        
        if aBehindCamera:
            if bBehindCamera:
                aDelta = aDelta.renderMoveXToVal(cDelta, minX)
                bDelta = bDelta.renderMoveXToVal(cDelta, minX)
                # return [Triangle(aDelta, bDelta, cDelta, self.material)]
            else:
                #C must not be behind camera b/c of above
                aDelta = aDelta.renderMoveXToVal(bDelta, minX)
                dDelta = aDelta.renderMoveXToVal(cDelta, minX)
                return [
                    Triangle(aDelta, bDelta, cDelta, self.material),
                    Triangle(bDelta, cDelta, dDelta, self.material)
                ]
        return [Triangle(aDelta, bDelta, cDelta, self.material)]

        
from Object3D import Object3D
from math import pi, tan
from Vector import Vector2, Vector3
from VectorList import VectorList, VectorList3


def renderMoveXToVal(vec1, vec2, xVal:float):
    d = vec2 - vec1
    percent = abs((xVal - vec1.x) / d.x)
    return Vector3(xVal, percent * d.y + vec1.y, percent * d.z + vec1.z)


class Camera(Object3D):
    __slots__ = "fieldOfView"
    def __init__(self, fov = pi / 2):
        super().__init__()
        self.fieldOfView = fov
    def render(self, renderPacket):
        transformed = []

        rotationMatrix = self.transformation.quaternion.toRotationMatrix()
        cameraPos = self.transformation.position

        for tri in renderPacket:
            aDelta = tri[1][0] - cameraPos
            bDelta = tri[1][1] - cameraPos  
            cDelta = tri[1][2] - cameraPos

            aDelta = rotationMatrix.mutliplyMatrixByVector(aDelta)
            bDelta = rotationMatrix.mutliplyMatrixByVector(bDelta)
            cDelta = rotationMatrix.mutliplyMatrixByVector(cDelta)
            
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
                continue
            
            if aBehindCamera:
                if bBehindCamera:
                    aDelta = renderMoveXToVal(aDelta, cDelta, minX)
                    bDelta = renderMoveXToVal(bDelta, cDelta, minX)
                    # return [Triangle(aDelta, bDelta, cDelta, self.material)]
                else:
                    #C must not be behind camera b/c of above
                    aDelta = renderMoveXToVal(aDelta, bDelta, minX)
                    dDelta = renderMoveXToVal(aDelta, cDelta, minX)

                    transformed.append((tri[0], VectorList3(aDelta, bDelta, cDelta)))
                    transformed.append((tri[0], VectorList3(bDelta, cDelta, dDelta)))
                    
            transformed.append((tri[0], VectorList3(aDelta, bDelta, cDelta)))
        
        transformed.sort(key=lambda x: abs(x[1].average()), reverse=True)

        focalScalar = tan(self.fieldOfView / 2)

        output = []
        for tri in transformed:
            output.append((tri[0], VectorList(*(Vector2(v.z / v.x / focalScalar, v.y / v.x / focalScalar) for v in tri[1]))))

        return output
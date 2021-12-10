from __future__ import annotations

from math import cos, sin, sqrt

from Vector import Vec


class Quaternion:
    def __init__(self, x:float = 0, y:float = 0, z:float = 0, w:float = 0) -> None:
        """Quaternion class for 3D Engine

        Args:
            x (float, optional): x component. Defaults to 0.
            y (float, optional): y component. Defaults to 0.
            z (float, optional): z component. Defaults to 0.
            w (float, optional): w component. Defaults to 0.
        """             
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def fromVecEuler(self, v1: Vec) -> Quaternion:
        """sets quaternion from euler vector

        Args:
            v1 (Vec): Euler Vector

        Returns:
            Quaternion: current object
        """
        c0 = cos(v1.x/2)
        c1 = cos(v1.y/2)
        c2 = cos(v1.z/2)
        s0 = sin(v1.x/2)
        s1 = sin(v1.y/2)
        s2 = sin(v1.z/2)

        self.x = s0 * c1 * c2 - c0 * s1 * s2
        self.y = c0 * s1 * c2 + s0 * c1 * s2
        self.z = c0 * c1 * s2 - s0 * s1 * c2
        self.w = c0 * c1 * c2 + s0 * s1 * s2
        return self

    def __str__(self) -> str:
        """creates a string of the quaternion

        Returns:
            str: string of quaternion
        """
        return "<{0}, {1}, {2}> w = {3}".format(round(self.x, 4), round(self.y, 4), round(self.z, 4), round(self.w, 4))
    def conjugate(self) -> Quaternion:
        """creates a new conjugate of the quaternion

        Returns:
            Quaternion: conjugate quaternion
        """        
        return Quaternion(-self.x, -self.y, -self.z, self.w)
    def inverse(self) -> Quaternion:
        """creates a new inverse of the quaternion

        Returns:
            Quaternion: inverse quaternion
        """        
        c = self.conjugate()
        m = self.magnitude()
        m = m*m
        return Quaternion(c.x / m, c.y / m, c.z / m, c.w / m)
    def magnitude(self) -> float:
        """returns magnitude of quaternion

        Returns:
            float: magnitude
        """        
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z + self.w*self.w)

class RotationMatrix:
    def __init__(self) -> None:
        """Rotation Matrix Object for 3D Engine
        """
        self.m = [[0 for x in range(3)] for y in range(3)]

    def fromQuaternion(self, quat: Quaternion) -> RotationMatrix:
        """sets rtation matrix from quaternion values

        Args:
            quat (Quaternion): quaternion to create rotation matrix from

        Returns:
            RotationMatrix: current object
        """
        self.m[0][0] = 1 - 2*(quat.y*quat.y + quat.z*quat.z)
        self.m[0][1] = 2 * (quat.x*quat.y - quat.w*quat.z)
        self.m[0][2] = 2 * (quat.w*quat.y + quat.x*quat.z)

        self.m[1][0] = 2 * (quat.x*quat.y + quat.w*quat.z)
        self.m[1][1] = 1 - 2*(quat.x*quat.x + quat.z*quat.z)
        self.m[1][2] = 2 * (-quat.w*quat.x + quat.y*quat.z)

        self.m[2][0] = 2 * (-quat.w*quat.y + quat.x*quat.z)
        self.m[2][1] = 2 * (quat.w*quat.x + quat.y*quat.z)
        self.m[2][2] = 1 - 2*(quat.x*quat.x + quat.y*quat.y)
        return self

    def applyTo(self, v1: Vec) -> Vec:
        """Applies rotaiton matrix to a vector

        Args:
            v1 (Vec): 3D point as vector

        Returns:
            Vec: new vector rotated by matrix
        """
        ret = Vec()
        ret.x = self.m[0][0] * v1.x + self.m[0][1] * v1.y + self.m[0][2] * v1.z
        ret.y = self.m[1][0] * v1.x + self.m[1][1] * v1.y + self.m[1][2] * v1.z
        ret.z = self.m[2][0] * v1.x + self.m[2][1] * v1.y + self.m[2][2] * v1.z
        return ret
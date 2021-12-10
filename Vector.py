from __future__ import annotations

from math import sqrt


class Vec:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> Vec:
        """3 Axis vector for 3D Engine

        Args:
            x (float, optional): x axis value. Defaults to 0.
            y (float, optional): y axis value. Defaults to 0.
            z (float, optional): z axis value. Defaults to 0.
        """
        self.x = x
        self.y = y
        self.z = z
    # operators

    def __add__(self, v2: Vec) -> Vec:
        """Adds two vectors

        Args:
            v2 (Vec): second vector to add

        Returns:
            Vec: new vector created from sum of vectors
        """
        return Vec(self.x + v2.x, self.y + v2.y, self.z + v2.z)

    def __sub__(self, v2: Vec) -> Vec:
        """Subtracts two vectors

        Args:
            v2 (Vec): second vector to subtract

        Returns:
            Vec: new vector created from subtraction of vectors
        """
        return Vec(self.x - v2.x, self.y - v2.y, self.z - v2.z)

    def __mul__(self, s2: float) -> Vec:
        """Multiply a vector and a constant

        Args:
            s2 (float): number to scale vector by

        Returns:
            Vec: new vector created from scalar the orginial vector
        """
        ty = type(s2)
        if type(s2) == float or ty == int:
            return Vec(self.x * s2, self.y * s2, self.z * s2)
        print("Vec: Attempting incorrect multiplication")
        return self.copy()
    # string

    def __str__(self) -> str:
        """Create string of vector

        Returns:
            str: returns a string of the vector
        """
        return "<{0}, {1}, {2}>".format(round(self.x, 4), round(self.y, 4), round(self.z, 4))
    # comparisons

    def __eq__(self, v2: Vec) -> bool:
        """checks if two vectors are equal

        Args:
            v2 (Vec): vector to compare to

        Returns:
            bool: returns true if all values of the vector are equal
        """
        return self.x == v2.x and self.y == v2.y and self.z == v2.z
    # custom

    def asList(self) -> list[float]:
        """Creates a list of a vector

        Returns:
            List: a list of len 3 with the value of x, y, and z
        """
        return [self.x, self.y, self.z]

    def mag(self) -> float:
        """find magnitude of a vector

        Returns:
            float: magnitude of the vector
        """
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def copy(self) -> Vec:
        """creates a copy of a vector

        Returns:
            Vec: copy of original vector
        """
        return Vec(self.x, self.y, self.z)
    def renderMoveXToVal(self, other:Vec, xVal:float) -> Vec:
        d = other - self
        percent = abs((xVal - self.x) / d.x)
        return Vec(xVal, percent * d.y + self.y, percent * d.z + self.z)

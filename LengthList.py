class LengthList(list):
    __slots__ = '__size', '__default'

    def __init__(self, *v, default=0):
        super().__init__(v)
        self.__size = len(v)
    
    # Representations
    def __repr__(self):
        return f"<{', '.join(map(str, self))}>"
    
    # Replacing old array methods
    def append(self, val):
        raise Exception("Can't change the size of a LengthList")
    def clear(self):
        for i in range(len(self)):
            self[i] = self.__default
    def copy(self):
        return type(self)(*self)
    def extend(self, arr):
        raise Exception("Can't change the size of a LengthList")
    def insert(self, index, val):
        raise Exception("Can't change the size of a LengthList")
    def pop(self, index = 0):
        raise Exception("Can't change the size of a LengthList")
    def remove(self, val):
        raise Exception("Can't change the size of a LengthList")
    def __len__(self):
        return self.__size
    

class FinalLengthList(LengthList):
    def __setitem__():
        raise Exception("You can't set items a FinalLengthList")


class ListWrapperForValue(FinalLengthList):
    __slots__ = "__val"
    def __init__(self, val):
        super().__init__(val)
        self.__val = val
    
    def __getitem__(self, index):
        return self.__val

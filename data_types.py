"""

Low level arrays in python, array-based sequences

Implementing dynamic array in python although python's
list is already providing this capability.


"""
import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self._capicity = 1
        self._make_array(self._capicity)

    def _make_array(self, c):
        return (c * ctypes.py_object)()

class stack(object):

    def __init__(self):
        pass



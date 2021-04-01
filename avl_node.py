class AVLNode:
    def __init__(self, key, value=None, bf=0):
        self._key = key
        self._value = value
        self.right = None
        self.left = None
        self._bf = bf    # balance factor
        self._height = 1

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        self._height = new_height

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val

    @property
    def key(self):
        return self._key

    @property
    def bf(self):
        return self._bf

    @bf.setter
    def bf(self, new_bf):
        self._bf = new_bf

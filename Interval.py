class Interval:
    """
    Klasse fur representieren ein Interval.

    Attributes:
        left (float): Wo das Intervall beginnt
        right (float): Wo es endet
    """

    def __init__(self, left, right):
        self.__left = left
        self.__right = right

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new_left):
        self.__left = new_left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, new_right):
        self.__right = new_right

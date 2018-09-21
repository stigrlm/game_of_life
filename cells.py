class Cell:
    def __init__(self, alive_current):
        self.alive_current = alive_current
        self.alive_next = False

    def set_alive_current(self, value):
        self.alive_current = value

    def set_alive_next(self, value):
        self.alive_next = value

    # the dunder methods are impelmented so that sum operations could be
    # performed on numpy array, which will allow for efficient computing
    # of number of alive cells
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.alive_current + other.alive_current
        elif isinstance(other, int):
            return self.alive_current + other
        raise TypeError("Can only add cell instances or integers")

    def __radd__(self, other):
        return Cell.__add__(self, other)

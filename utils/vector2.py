import math


class Vector2(object):
    def __init__(self, *args):
        if len(args) == 0:
            values = 0, 0
        elif len(args) == 1:
            values = args[0], args[0]
        else:
            values = args[0], args[1]
        self.x, self.y = values

    @staticmethod
    def __raise(operator):
        TypeError(f"passed wrong argument to Vector2({operator})")

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)
        elif isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, list):
            return Vector2(self.x + other[0], self.y + other[1])
        else:
            self.__raise("+")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x - other, self.y - other)
        elif isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, list):
            return Vector2(self.x - other[0], self.y - other[1])
        else:
            self.__raise("-")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        elif isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, list):
            return Vector2(self.x * other[0], self.y * other[1])
        else:
            self.__raise("*")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        elif isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(other, list):
            return Vector2(self.x / other[0], self.y / other[1])
        else:
            self.__raise("/")

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x // other, self.y // other)
        elif isinstance(other, Vector2):
            return Vector2(self.x // other.x, self.y // other.y)
        elif isinstance(other, list):
            return Vector2(self.x // other[0], self.y // other[1])
        else:
            self.__raise("/")

    def __iter__(self):
        return [self.x, self.y]

    def __round__(self, n=None):
        return Vector2(round(self.x, n), round(self.y, n))

    @property
    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def normalize(self):
        return Vector2(self.x / self.length, self.y / self.length)

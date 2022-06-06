import math


class VectorInputCoordsValidationError(Exception):
    """Custom exception class for invalid input args given to the Vector instantiation"""


class Vector:
    # https://www.mathsisfun.com/algebra/vectors.html

    def __init__(self, *args):
        try:
            self.x, self.y, self.z = args if len(args) == 3 else args[0]
        except ValueError:
            raise VectorInputCoordsValidationError('Either give single iterable of 3 coords or pass them as *args')

    def __add__(self, other) -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other) -> "Vector":

        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __eq__(self, other) -> bool:
        # https://www.grc.nasa.gov/www/k-12/airplane/vectcomp.html
        # https://onlinemschool.com/math/library/vector/equality/
        return all((
            self.x == other.x,
            self.y == other.y,
            self.z == other.z
        ))

    def cross(self, other) -> "Vector":
        # https://www.mathsisfun.com/algebra/vectors-cross-product.html
        return Vector(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )

    def dot(self, other) -> int:
        # https://www.mathsisfun.com/algebra/vectors-dot-product.html
        return self.x*other.x + self.y*other.y + self.z*other.z

    def to_tuple(self) -> tuple:
        return self.x, self.y, self.z

    def __str__(self) -> str:
        return "<{x}, {y}, {z}>".format(**self.__dict__)

    @property
    def magnitude(self) -> float:
        return math.sqrt(
            sum (
                    (
                        self.x ** 2,
                        self.y ** 2,
                        self.z ** 2
                    )
            )
        )


"""from math import sqrt


class Vector:
    def __init__(self, *vector):
        self.vector = vector
        if len(vector) == 1:
            self.vector = tuple(vector[0])
        self.x, self.y, self.z = self.vector
        self.magnitude = sqrt(sum(v * v for v in self.vector))

    def to_tuple(self):
        return tuple(self.vector)

    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'

    def __add__(self, other):
        x, y, z = (a + other.vector[i] for i, a in enumerate(self.vector))
        return Vector(x, y, z)

    def __sub__(self, other):
        x, y, z = (a - other.vector[i] for i, a in enumerate(self.vector))
        return Vector(x, y, z)

    def __eq__(self, other):
        return all(v == other.vector[i] for i, v in enumerate(self.vector))

    def dot(self, other):
        return sum(v * other.vector[i] for i, v in enumerate(self.vector))

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = -(self.x * other.z - self.z * other.x)
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)"""
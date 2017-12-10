import math
from util import Util
from error import NoUniqueParallelComponent

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must not be empty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, vectorB):
        return self.coordinates == vectorB.coordinates

    def plus(self, vectorB):
        return Vector([x + y for x, y in zip(self.coordinates, vectorB.coordinates)])

    def minus(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, scalar):
        return Vector([scalar * x for x in self.coordinates])

    def magnitude(self):
        potencies = sum([x ** 2 for x in self.coordinates])
        return math.sqrt(potencies)

    def normalization(self):
        try:
            magnitude = self.magnitude()
            return Vector([x / magnitude for x in self.coordinates])
        except ZeroDivisionError:
            raise Exception('Thou shalt not divide by zero')

    def dot(self, vectorB):
        return sum([a * b for a, b in zip(self.coordinates, vectorB.coordinates)])

    def angle(self, vectorB):
        rad = math.acos(
            max(-1, min(self.normalization().dot(vectorB.normalization()), 1))
        )
        return [rad, rad * 180 / math.pi]

    def is_zero(self):
        return Util.is_nearly_zero(self.magnitude)

    def parallel(self, vectorB):
        return (self.is_zero()                              or
                vectorB.is_zero()                           or
                Util.is_nearly_zero(self.angle(vectorB)[0]) or
                round(self.angle(vectorB)[0], 3) == round(math.pi, 3))

    def orthogonal(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def component_parallel_to(self, basis):
        try:
            norm_basis = basis.normalization()
            weight = self.dot(norm_basis)
            return norm_basis.times_scalar(weight)

        except NoUniqueParallelComponent:
            print("A single parallel component could not be found")

    def component_orthogonal_to(self, basis):
        projection = self.component_parallel_to(basis)
        return self.minus(projection)

    def cross_product(self, vectorB):
        x_1, y_1, z_1 = self.coordinates
        x_2, y_2, z_2 = vectorB.coordinates

        return Vector([
            y_1 * z_2 - y_2 * z_1,
            - (x_1 * z_2 - x_2 * z_1),
            x_1 * y_2 - x_2 * y_1
        ])

    def area_of_triangle(self, vectorB):
        return self.area_of_parallelogram_with(vectorB) / 2.0

    def area_of_parallelogram_with(self, vectorB):
        return self.cross_product(vectorB).magnitude()


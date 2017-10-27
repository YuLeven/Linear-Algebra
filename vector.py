import math
from decimal import *

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.NO_UNIQUE_PARALLEL_COMPONENT_MSG = "NO_UNIQUE_PARALLEL_COMPONENT_MSG"
            self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "CANNOT_NORMALIZE_ZERO_VECTOR_MSG"

        except ValueError:
            raise ValueError('The coordinates must not be empty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        potencies = sum([x**2 for x in self.coordinates])
        return math.sqrt(float(potencies))

    def normalization(self):
        try:
            magnitude = float(self.magnitude())
            normalized = [x / magnitude for x in self.coordinates]
            return [x for x in normalized]
        except ZeroDivisionError:
            raise Exception('Thou shalt not divide by zero')

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle(self, v):
        u1 = Vector(self.normalization())
        u2 = Vector(v.normalization())
        rad = math.acos(u1.dot(u2))
        return ["%.3f" % x for x in [rad, rad * 180 / math.pi]]

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def parallel(self, v):
        return ( self.is_zero() or
                 v.is_zero() or
                 self.angle(v)[0] == 0 or
                 self.angle(v)[0] == math.pi )

    def orthogonal(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_parallel_to(self, basis):
        try:
            u = Vector(basis.normalization())
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            else:
                raise e

    def component(self, v):
        normalizedV = Vector(v.normalization())
        x = Vector(self.dot(normalizedV))
        return x.dot(normalizedV)

    def cross_product(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [
                y_1 * z_2 - y_2 * z_1,
                - (x_1 * z_2 - x_2 * z_1),
                x_1 * y_2 - x_2 * y_1
            ]
            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            raise e

    def area_of_triangle(self, v):
        return self.area_of_parallelogram_with(v) / 2.0

    def area_of_parallelogram_with(self, v):
        cross_product = self.cross_product(v)
        return cross_product.magnitude()

print('#1')
v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
print(v.cross_product(w))

v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])
print(v.area_of_parallelogram_with(w))

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
print(v.area_of_triangle(w))

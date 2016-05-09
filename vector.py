import math

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
            raise Exception('Thou shall not divide by zero')

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


print '#1'
myVector1 = Vector([3.039,1.879])
myVector2 = Vector([0.825,2.036])

print myVector1.component_parallel_to(myVector2)

print '#2'
v = Vector([-9.88, -3.264, -8.159])
w = Vector([-2.155, -9.353, -9.473])
print v.component_orthogonal_to(w)

print '#3'
v = Vector([3.009, -6.172, 3.692, -2.51])
w = Vector([6.404, -9.144, 2.759, 8.718])
vpar = v.component_parallel_to(w)
vort = v.component_orthogonal_to(w)
print "Parallel:", vpar
print "Parallel:", vort
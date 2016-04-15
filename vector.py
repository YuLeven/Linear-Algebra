import math

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


      



myVector1 = Vector([-7.579,-7.88])
myVector2 = Vector([22.737,23.64])

print myVector1.parallel(myVector2)
print myVector1.orthogonal(myVector2)

myVector1 = Vector([-2.029,9.97,4.172])
myVector2 = Vector([-9.231,-6.639, -7.245])

print myVector1.parallel(myVector2)
print myVector1.orthogonal(myVector2)

myVector1 = Vector([-2.328,-7.284, -1.214])
myVector2 = Vector([-1.821,1.072,-2.94])

print myVector1.parallel(myVector2)
print myVector1.orthogonal(myVector2)

myVector1 = Vector([2.118, 4.827])
myVector2 = Vector([0,0])
from math import sqrt

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
        potencies = sum([x*x for x in self.coordinates])
        return "%.3f" % sqrt(float(potencies))

    def normalization(self):
        magnitude = float(self.magnitude())
        normalized = [x / magnitude for x in self.coordinates]
        return ["%.3f" % x for x in normalized]
        

myVector1 = Vector([-0.221,7.437])
myVector2 = Vector([8.813,-1.331,-6.247])
myVector3 = Vector([5.581,-2.136])
myVector4 = Vector([1.996,3.108,-4.554])

print myVector1.magnitude()
print myVector2.magnitude()
print myVector3.normalization()
print myVector4.normalization()
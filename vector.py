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
        dot_product = sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
        return dot_product

    def angle(self, v):
        u1 = Vector(self.normalization())
        u2 = Vector(v.normalization())
        rad = math.acos(u1.dot(u2))
        return [rad, rad * 180 / math.pi]



myVector1 = Vector([7.887,4.138])
myVector2 = Vector([-8.802,6.776])
myVector3 = Vector([-5.955,-4.904,-1.874])
myVector4 = Vector([-4.496,-8.755,7.103])

myVector5 = Vector([3.183, -7.627])
myVector6 = Vector([-2.668, 5.319])

myVector7 = Vector([7.35,0.221,5.188])
myVector8 = Vector([2.751,8.259,3.985])


print "%.3f" % myVector1.dot(myVector2)
print "%.3f" % myVector3.dot(myVector4)
print myVector5.angle(myVector6)
print myVector7.angle(myVector8)
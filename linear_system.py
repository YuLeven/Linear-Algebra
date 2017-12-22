from decimal import getcontext
from copy import deepcopy

from error import NoNonzeroElementsFound, AllPlanesMustBeInSameDimension
from vector import Vector
from plane import Plane

getcontext().prec = 30

class LinearSystem(object):

    def __init__(self, planes):
        dimension = planes[0].dimension
        for plane in planes:
            if plane.dimension != dimension:
                raise AllPlanesMustBeInSameDimension

        self.planes = planes
        self.dimension = dimension


    def swap_rows(self, row1, row2):
        pass # add your code here

    def multiply_coefficient_and_row(self, coefficient, row):
        pass # add your code here

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        pass # add your code here

    def indices_of_first_nonzero_terms_in_each_row(self):
        indices = [-1] * len(self)

        for index, plane in enumerate(self.planes):
            try:
                indices[index] = plane.first_nonzero_index(plane.normal_vector.coordinates)
            except NoNonzeroElementsFound:
                pass

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        # Raises an excepion if the dimension doesn't match
        if x.dimension != self.dimension:
            raise AllPlanesMustBeInSameDimension
        self.planes[i] = x

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(index + 1, plane) for index, plane in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


p0 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
p1 = Plane(normal_vector=Vector([0,1,0]), constant_term=2)
p2 = Plane(normal_vector=Vector([1,1,-1]), constant_term=3)
p3 = Plane(normal_vector=Vector([1,0,-2]), constant_term=2)

s = LinearSystem([p0,p1,p2,p3])

print s.indices_of_first_nonzero_terms_in_each_row()
print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
print len(s)
print s

s[0] = p1
print s

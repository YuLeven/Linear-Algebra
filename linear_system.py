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
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1]

    def multiply_coefficient_and_row(self, coefficient, row):
        self.planes[row] = deepcopy(self.planes[row])
        self.planes[row].normal_vector = self.planes[row].normal_vector.times_scalar(coefficient)
        self.planes[row].constant_term *= coefficient
        self.planes[row].set_basepoint()

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        plane_to_be_added = self.planes[row_to_be_added_to]
        plane_to_add = deepcopy(self.planes[row_to_add])

        self.multiply_coefficient_and_row(coefficient, row_to_add)

        plane_to_be_added.normal_vector = plane_to_be_added.normal_vector.plus(self.planes[row_to_add].normal_vector)
        plane_to_be_added.constant_term += self.planes[row_to_add].constant_term
        plane_to_be_added.set_basepoint()

        self.planes[row_to_add] = deepcopy(plane_to_add)

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

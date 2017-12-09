from error import NoNonzeroElementsFound
from util import Util
from vector import Vector

class GeometricalRepresentation(object):
    
    @staticmethod
    def first_nonzero_index(iterable):
        for key, item in enumerate(iterable):
            if not Util.is_nearly_zero(item): 
                return key
        raise NoNonzeroElementsFound()

    def __init__(self, normal_vector = None, constant_term = None, dimension = 2):
        self.dimension = dimension

        if not normal_vector:
            normal_vector = GeometricalRepresentation.zero_vector(self.dimension)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = float(0)
        self.constant_term = float(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            # We create an array contaning N coordinates set to zero
            basepoint_coords = [0] * self.dimension

            # To set a basepoint we get the first non-zero coordinate
            # and set the other to zero after applying solving for it
            # using the expression Ax + By = K
            initial_index = GeometricalRepresentation.first_nonzero_index(self.normal_vector.coordinates)
            initial_coefficient = self.normal_vector.coordinates[initial_index]
            basepoint_coords[initial_index] = self.constant_term / initial_coefficient

            # We set our basepoint using the value we found using our normal vector
            self.basepoint = Vector(basepoint_coords)

        except NoNonzeroElementsFound:
            self.basepoint = None

    @staticmethod
    def zero_vector(dimension):
        all_zeros = [0] * dimension
        return Vector(all_zeros)

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = GeometricalRepresentation.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except NoNonzeroElementsFound:
            output = '0'

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output
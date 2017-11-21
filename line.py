from decimal import Decimal, getcontext
from vector import Vector

# Sets the precision in this mathematical context
getcontext().prec = 30


class Line(object):

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = [0] * self.dimension
            normal_vector = Vector(all_zeros)
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
            initial_index = Line.first_nonzero_index(self.normal_vector.coordinates)
            initial_coefficient = self.normal_vector.coordinates[initial_index]
            basepoint_coords[initial_index] = self.constant_term / initial_coefficient

            # We set our basepoint using the value we found using our normal vector
            self.basepoint = Vector(basepoint_coords)

        except NoNonzeroElementsFound:
            self.basepoint = None

    def is_parallel_to(self, lineB):
        return self.normal_vector.parallel(lineB.normal_vector)

    def __eq__(self, lineB):
        
        if not self.is_parallel_to(lineB):
            return False

        # We subtract both basepoints to find the line between them
        # If this vector is orthogonal to the normal vector of either lines,
        # then the lines are equal
        base_a = self.basepoint
        base_b = lineB.basepoint
        return base_a.minus(base_b).orthogonal(self.normal_vector)

    def intersection(self, lineB):
        is_parallel = self.is_parallel_to(lineB) 
        is_same = self == lineB

        if is_same:
            return "The lines have infinite intersection points"
        elif is_parallel and not is_same:
            return "The lines have no intersection points"

        # PyLint is quite angry at me here,
        # but this is a great way to represet the
        # somewhat messy mathematical formular
        # to calculate the intersection point between two lines.
        a = self.normal_vector.coordinates[0]
        b = self.normal_vector.coordinates[1]
        c = lineB.normal_vector.coordinates[0]
        d = lineB.normal_vector.coordinates[1]
        k1 = self.constant_term
        k2 = lineB.constant_term

        denominator = (a * d) - (b * c)
        x = (d * k1 - b * k2) / denominator
        y = (-c * k1 + a * k2) / denominator
        return Vector([x, y])

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
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i == initial_index)) + 'x_{}'.format(i + 1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except NoNonzeroElementsFound:
            output = '0'

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for key, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero(): 
                return key
        raise NoNonzeroElementsFound()


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

class NoNonzeroElementsFound(ValueError):
    """No nonzero elements found"""
    pass

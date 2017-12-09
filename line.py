from decimal import Decimal, getcontext
from vector import Vector
from util import Util
from error import NoNonzeroElementsFound
from geometrical_representation import GeometricalRepresentation

# Sets the precision in this mathematical context
getcontext().prec = 30

class Line(GeometricalRepresentation):

    def __init__(self, normal_vector=None, constant_term=None):
        super(Line, self).__init__(normal_vector, constant_term, 2)

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

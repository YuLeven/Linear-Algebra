from decimal import Decimal, getcontext
from vector import Vector
from error import NoNonzeroElementsFound
from geometrical_representation import GeometricalRepresentation

# Sets the precision in this mathematical context
getcontext().prec = 30

class Plane(GeometricalRepresentation):

    def __init__(self, normal_vector=None, constant_term=None):
        super(Plane, self).__init__(normal_vector, constant_term, 3)


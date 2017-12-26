from decimal import getcontext
from copy import deepcopy
from error import NoNonzeroElementsFound, AllPlanesMustBeInSameDimension, NoSolution, InfiniteSolutions
from vector import Vector
from plane import Plane
from util import Util

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

    def compute_triangular_form(self):
        system = deepcopy(self)
        for row, equ in enumerate(system):
            for col, term in enumerate(equ.normal_vector.coordinates):
                # If the current term is zero
                if Util.is_nearly_zero(term):
                    # Try to swap it from a equation with a nonzero term
                    if not system.swap_for_nonzero(row, col):
                        continue
                
                # Use the current equation to clear this term in equations bellow
                system.clear_coefficients_below(row, col)
                break

        return system

    def swap_for_nonzero(self, row, col):
        for equ_index in range(row + 1, len(self)):
            coefficient = self[equ_index].normal_vector.coordinates[col]
            # If the coefficient is not zero
            if not Util.is_nearly_zero(coefficient):
                # Swap it with the position of the caller
                self.swap_rows(row, equ_index)
                return True
        
        return False

    def clear_coefficients_below(self, row, col):
        # Get the term which will be used to clear equation terms bellow
        base_term = self[row].normal_vector.coordinates[col]

        for equ_index in range(row + 1, len(self)):
            # Gets the term which will be cleared
            term_to_clear = self[equ_index].normal_vector.coordinates[col]
            # Calculates the coefficient how many times the current term has to be 
            # multiplied in order to become equal to the term to clear. We multidiply it by -1
            # since we'll be adding this terms.
            clear_coefficient = (term_to_clear / base_term) * -1
            self.add_multiple_times_row_to_row(clear_coefficient, row, equ_index)

    def clear_coefficients_above(self, row, col):
        for index in range(row)[::-1]:
            clear_coefficient = self[index].normal_vector.coordinates[col] * -1
            self.add_multiple_times_row_to_row(clear_coefficient, row, index)

    def compute_rref(self):
        system = self.compute_triangular_form()
        pivot_indices = system.indices_of_first_nonzero_terms_in_each_row()

        for index in range(len(system))[::-1]:
            leading_term_index = pivot_indices[index]
            
            # Normalize and clear coefficients above if there's a matching pivotal index
            if leading_term_index < 0:
                continue

            system.normalize_to_coefficient_one(index, leading_term_index)
            system.clear_coefficients_above(index, leading_term_index)

        return system

    def compute_solution(self):
        system = self.compute_rref()
        
        try:
            system.assert_not_contradictory_equation()
            system.assert_too_few_leading_variables()
            return Vector([system.planes[i].constant_term for i in range(system.dimension)])
        except Exception as error:
            print error.message

    def assert_not_contradictory_equation(self):
        for plane in self.planes:
            try:
                plane.first_nonzero_index(plane.normal_vector.coordinates)
            
            except NoNonzeroElementsFound:
                if Util.is_nearly_zero(plane.constant_term):
                    raise NoSolution("The system has no solutions")

    def assert_too_few_leading_variables(self):
        leading_variables = self.indices_of_first_nonzero_terms_in_each_row()
        total_ld_variables = len(filter(lambda x: x >= 0, leading_variables))

        if total_ld_variables < self.dimension:
            raise InfiniteSolutions("The system has infinite solutions")

    def normalize_to_coefficient_one(self, row, col):
        coefficient = 1.0 / self[row].normal_vector.coordinates[col]
        self.multiply_coefficient_and_row(coefficient, row)

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

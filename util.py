import math


class Util(object):

    @staticmethod
    def is_nearly_zero(value, tolerance=1e-5):
        return value < tolerance

    @staticmethod
    def to_ordinal(number):
        return "%d%s" % (number, "tsnrhtdd"[(math.floor(number / 10) % 10 != 1) * (number % 10 < 4) * number % 10::4])

    @staticmethod
    def get_term_letter_for_iteration(iteration):
        if iteration == 0:
            return "x"
        else:
            return chr(ord("x") + iteration)
        

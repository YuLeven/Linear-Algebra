class Util(object):

    @staticmethod
    def is_nearly_zero(value, tolerance=1e-10):
        return value < tolerance

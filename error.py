class NoNonzeroElementsFound(ValueError):
    """No nonzero elements found"""
    pass

class NoUniqueParallelComponent(ValueError):
    """No unique parallel components where found"""
    pass

class CannotNormalizeZeroVector(ValueError):
    """Cannot normalize the zero vector"""
    pass

class AllPlanesMustBeInSameDimension(ValueError):
    """All planes must be in the same dimension"""
    pass

class NoSolution(ValueError):
    """The system has no solutions"""
    pass

class InfiniteSolutions(ValueError):
    """The system has infinite solutions"""
    pass
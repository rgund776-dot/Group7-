class OutOfSampleError(Exception):
    """
    Raised when a new input contains feature values
    outside the historical min/max range.
    """
    pass
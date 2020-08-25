# import Exception
class Error(Exception):
    """Base class for other exceptions"""
    pass


class IncorrectInputError(Error):
    """Raised when the input value is incorrect"""
    pass

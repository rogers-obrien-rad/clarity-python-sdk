class ClarityException(Exception):
    """
    The base exception class for Clarity.
    """

    def __init__(self, msg, response=None):
        """
        Parameters
        ----------
        msg : str
            short description of the error
        response : int, default None
            error response from the API call
        """
        super(ClarityException, self).__init__(msg)
        self.message = msg
        self.response = response

    def __str__(self):
        if self.response is None:
            return repr(self.message)
        else:
            return repr(f"{self.response} - {self.message}")


class DeviceNotFoundError(ClarityException):
    """Clarity device does not exist or cannot be found, 403 error"""
    pass
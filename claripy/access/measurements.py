from .base import Base

class Measurements(Base):

    def __init__(self, api_key) -> None:
        """
        Device measurements

        Creates
        -------
        endpoint : str
            resource-specific endpoint to be appended to the base URL
        """
        super().__init__(api_key)
        self.endpoint = "/v1/measurements"

    def get(self):
        """
        Wrapper for get_request
        """
        info = self.get_request(self.endpoint)

        return info
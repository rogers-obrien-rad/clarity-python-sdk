from .base import Base
from claripy.exceptions import ClarityException

class DataSources(Base):

    def __init__(self, api_key) -> None:
        """
        Metadata for all data sources belonging to the oganization of the caller

        Creates
        -------
        endpoint : str
            resource-specific endpoint to be appended to the base URL
        """
        super().__init__(api_key)
        self.endpoint = "/v1/datasources"

    def get(self):
        """
        Wrapper for get_request
        """
        response = self.get_request(self.endpoint)

        if response.ok:
            return response.json()
        else:
            raise ClarityException()
from .base import Base

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
        info = self.get_request(self.endpoint)

        return info
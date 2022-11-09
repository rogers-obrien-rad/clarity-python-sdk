from .base import Base

class Devices(Base):

    def __init__(self, api_key) -> None:
        """
        Devices that the developer has access to, together with metadata and the latest device status

        Creates
        -------
        endpoint : str
            resource-specific endpoint to be appended to the base URL
        """
        super().__init__(api_key)
        self.endpoint = "/v1/devices"
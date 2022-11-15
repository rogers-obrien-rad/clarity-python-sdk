from .base import Base
from claripy.exceptions import ClarityException

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

    def get(self):
        """Wrapper for get_request"""
        response = self.get_request(self.endpoint)

        if response.ok:
            return response.json()
        else:
            raise ClarityException()

    def codes(self):
        """Returns list of all device codes (str) registered to account"""
        info = self.get()
        codes = []
        for device_info in info:
            codes.append(device_info["code"])

        return codes
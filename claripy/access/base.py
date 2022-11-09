import urllib
import requests

class Base:

    def __init__(self, api_key) -> None:
        self.__api_key = api_key
        self.base_url = "https://clarity-data-api.clarity.io"

    def get_request(self, api_url):
        """
        Create a HTTP Get request

        Parameters
        ----------
        api_url : str
            endpoint for the specific API call

        Returns
        -------
        """
        pass
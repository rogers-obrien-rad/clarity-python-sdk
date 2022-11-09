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
        url = f"{self.base_url}{api_url}"
        headers = {"x-api-key": f"{self.__api_key}"}

        response = requests.get(
            url,
            headers=headers
        )

        if response.ok:
            return response.json()
        else:
            return response.status_code
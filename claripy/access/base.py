import urllib
import requests

class Base:

    def __init__(self, api_key) -> None:
        self.__api_key = api_key
        self.base_url = "https://clarity-data-api.clarity.io"

    def get_request(self, api_url, params=None):
        """
        Create a HTTP Get request

        Parameters
        ----------
        api_url : str
            endpoint for the specific API call
        params : dict, default None
            GET query parameters to parse

        Returns
        -------
        response : dict
            GET response in json
        """
        headers = {"x-api-key": f"{self.__api_key}"}
        
        if params is not None:
            url = f"{self.base_url}{api_url}?{urllib.parse.urlencode(params)}"
        else:
            url = f"{self.base_url}{api_url}"

        response = requests.get(
            url,
            headers=headers
        )

        return response
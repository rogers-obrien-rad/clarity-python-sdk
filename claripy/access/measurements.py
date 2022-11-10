from .base import Base
from claripy.exceptions import ClarityException, DeviceNotFoundError

from datetime import datetime
import warnings

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

    def get(self, code=None, frequency="minute", start_time=None, end_time=None, limit=5000):
        """
        Wrapper for get_request

        Parameters
        ----------
        code : str, default None
            node ID
        frequency : str in ["minute","hour","day"], default "minute"
            output frequency of the measurements
        start_time : str, default None
            timestamp of earliest measurement in ISO 8601 format
        end_time : str, default None
            timestamp of most recent measurement desired in ISO 8601 format
        limit : int, default None
            maximum number of measurements to be returned

        Returns
        -------
        measurements : dict
            available measurements
        """
        params = {} # query parameters dict to populate
        # device specific data
        if code is not None:
            params["code"] = code
        # measurement frequency
        if frequency in ["minute","hour","day"]:
            params["outputFrequency"] = frequency
        else:
            warnings.warn("Invalid frequency option - must be one of ['minute','hour','day']; defaulting to 'minute'", SyntaxWarning)
            params["outputFrequency"] = "minute" # default to minute which is the API's default anyway

        # start and end times
        def datetime_valid(dt_str):
            """Checks if the given string is ISO 8601 format"""
            try:
                datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
            except:
                return False

            return True

        if start_time is not None:
            if datetime_valid(start_time):
                params["startTime"] = start_time
            else:
                warnings.warn("Invalid datetime format - must be in ISO 1860; ignoring start_time", SyntaxWarning)

        if end_time is not None:
            if datetime_valid(end_time):
                params["endTime"] = end_time
            else:
                warnings.warn("Invalid datetime format - must be in ISO 1860; ignoring end_time", SyntaxWarning)

        # number of measurements
        if limit < 1 or limit > 5000: # range of possible values
            warnings.warn("Invalid limit - must be between 1 - 5000; defaulting to 5000", SyntaxWarning)
            params["limit"] = 5000
        else:
            params["limit"] = limit

        response = self.get_request(
            self.endpoint,
            params=params
        )

        if response.ok:
            return response.json()
        elif response.status_code == 403:
            raise DeviceNotFoundError(f"could not find the device {code}", 403)
        else:
            raise ClarityException()
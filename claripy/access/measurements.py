from .base import Base
from claripy.exceptions import ClarityException, DeviceNotFoundError

from datetime import datetime
import warnings
import pathlib
import pandas as pd

PATH_TO_ROOT = f"{pathlib.Path(__file__).resolve().parent.parent}"

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

    def export(self, codes, pollutants=None, frequency="minute", start_time=None, end_time=None, limit=5000, save_path=PATH_TO_ROOT):
        """
        Creates a csv of the gathered measurements
        
        Parameters
        ----------
        code : list of str
            node ID(s)
        pollutants : list of str, default None
            pollutants concentrations to export
            default is to export all available characteristics
        frequency : str in ["minute","hour","day"], default "minute"
            output frequency of the measurements
        start_time : str, default None
            timestamp of earliest measurement in ISO 8601 format
        end_time : str, default None
            timestamp of most recent measurement desired in ISO 8601 format
        limit : int, default None
            maximum number of measurements to be returned
        save_path : str, PATH_TO_ROOT
            absolute path to the directory to save
        
        Saves
        -----
        <measurements_by_device> : csv file
            data from each device specified
        """
        
        for device in codes:
            measurements = self.get(
                code=device,
                frequency=frequency,
                start_time=start_time,
                end_time=end_time,
                limit=limit
            )
            # defining pollutant list if not provided
            if pollutants is None:
                pollutants = []
                #for key, val in 
                pollutants = list(measurements[0]["characteristics"].keys())

            measurements_by_device = {pollutant: [] for pollutant in pollutants}
            measurements_by_device["timestamp"] = []

            for measurement in measurements:
                for pollutant in pollutants:
                    # adding pollutant concentrations to specific device
                    measurements_by_device[pollutant].append(
                        measurement["characteristics"][pollutant]["value"]
                    )

                # adding timestamp to specific device
                measurements_by_device["timestamp"].append(
                    measurement["time"]
                )

            # saving data
            dataset = pd.DataFrame(measurements_by_device)
            dataset.set_index("timestamp",inplace=True)
            latest_str = datetime.strftime(pd.to_datetime(dataset.index[0]), "%Y%m%d")
            earliest_str = datetime.strftime(pd.to_datetime(dataset.index[-1]), "%Y%m%d")
            dataset.to_csv(f"{save_path}/{device}-{earliest_str}-{latest_str}-{frequency}.csv")
#!/usr/bin/env python3
# ---
# Project Name: ClariPy
# Date Created: 11/09/2022
# Author: Hagen E. Fritz
# Description: SDK to access Clarity.io resources
# Last Edited: 11/09/2022
# ---

from .access import datasources, devices, measurements

class Clarity:

    def __init__(self, api_key) -> None:
        """
        Create connection to Clarity.io

        Parameters
        ----------
        api_key : str
            user-specific API key available from Clarity.io dashboard
        
        Creates
        -------
        __api_key : str
            private API key 
        """
        self.__api_key = api_key

        # create instances of endpoints
        self.__datasources__ = datasources.DataSources(api_key=self.__api_key)
        self.__devices__ = devices.Devices(api_key=self.__api_key)
        self.__measurements__ = measurements.Measurements(api_key=self.__api_key)
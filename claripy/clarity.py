#!/usr/bin/env python3
# ---
# Project Name: ClariPy
# Date Created: 11/09/2022
# Author: Hagen E. Fritz
# Description: SDK to access Clarity.io resources
# Last Edited: 11/09/2022
# ---

from .access import datasources, devices, measurements

__version__ = '1.0.2'

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

        self.name="base"
        self.pollutants = []

        # create instances of endpoints
        self.__datasources__ = datasources.DataSources(api_key=self.__api_key)
        self.__devices__ = devices.Devices(api_key=self.__api_key)
        self.__measurements__ = measurements.Measurements(api_key=self.__api_key)

class NodeS(Clarity):

    def __init__(self, api_key) -> None:
        super().__init__(api_key)

        self.name = "node_s"
        self.pollutants = [
            "relHumid", "temperature",
            "pm1ConcNum", "pm2_5ConcNum", "pm10ConcNum",
            "pm1ConcMass", "pm2_5ConcMass", "pm1ConcMass",
            "no2Conc"
        ]
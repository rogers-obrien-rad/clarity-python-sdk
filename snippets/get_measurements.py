import os
import sys
import pathlib
import json
from datetime import datetime, timedelta
sys.path.append(f"{pathlib.Path(__file__).resolve().parent.parent}")

from claripy.clarity import Clarity
from claripy.exceptions import DeviceNotFoundError

from dotenv import load_dotenv

if os.getenv("API_KEY") is None:
    load_dotenv()

if __name__ == "__main__":
    connection = Clarity(os.getenv("API_KEY"))

    # ----- #
    # Usage #
    # ----- #

    run_usage = False
    if run_usage:
        # Example 1: Get the latest 5000 measurements (if that many exist)
        # ---------
        ex1_measurements = connection.__measurements__.get()
        # entries within the list of measurements cycle through all available devices i.e. with two devices on your account:
        # index 0: device 1
        # index 1: device 2
        # index 2: device 1
        # index 3: device 3 ...
        print("Number of measurements:", len(ex1_measurements))
        print("Example output:\n", json.dumps(ex1_measurements[0], indent=4))

        # Example 2: Get data from one device
        # ---------
        ex2_measurements = connection.__measurements__.get(code="A637HNKG")
        print("Number of measurements:", len(ex2_measurements))
        print("Example output:\n", json.dumps(ex2_measurements[0], indent=4))

        # Example 3: Get data between dates
        # ---------
        ex3_measurements = connection.__measurements__.get(
            code="A637HNKG",
            start_time=(datetime.now() - timedelta(days=2)).isoformat(),
            end_time=datetime.now().isoformat()
        )
        print("Number of measurements:", len(ex3_measurements))
        print("Example output:\n", json.dumps(ex3_measurements[0], indent=4))

        # Example 4: Get hourly data
        # ---------
        ex4_measurements = connection.__measurements__.get(
            code="A637HNKG",
            frequency="hour",
            start_time=(datetime.now() - timedelta(days=2)).isoformat(),
            end_time=datetime.now().isoformat()
        )
        print("Number of measurements:", len(ex4_measurements))
        print("Example output:\n", json.dumps(ex4_measurements[0], indent=4))

        # Example 5: Get last 24 hours
        # ---------
        ex5_measurements = connection.__measurements__.get(
            code="A637HNKG",
            frequency="hour",
            end_time=datetime.now().isoformat(),
            limit=24
        )
        # Without specifying the device, you would need to multiply the the limit by the number of devices you have
        # For example: with 3 devices to your account, you would have to specify the limit as 3*24 = 72 to get the last 24 hours from each device
        print("Number of measurements:", len(ex5_measurements))
        print("Example output:\n", json.dumps(ex5_measurements[0], indent=4))
        # For best results, you would likely want to include an end date as well in the event that data were lost, you might actually get 24 measurements from the last 24+ hours

    # ------ #
    # Errors #
    # ------ #

    run_errors = True
    if run_errors:
        # Example 6: device does not exist
        # ---------
        try:
            ex6_measurements = connection.__measurements__.get(code="ABCD1234")
            print("Output:\n", json.dumps(ex6_measurements, indent=4))
        except DeviceNotFoundError as e:
            print(e)

        # Example 7: bad date
        # ---------
        ex7_measurements = connection.__measurements__.get(
            end_time=(datetime.now() - timedelta(days=2)).date(),
            limit=2
        )
        # will simply return the latest measurements
        print("Output:\n", json.dumps(ex7_measurements, indent=4))
import os
import sys
import pathlib
import json
from datetime import datetime, timedelta

PATH_TO_TOP = f"{pathlib.Path(__file__).resolve().parent.parent}"
sys.path.append(PATH_TO_TOP)

from claripy.clarity import NodeS
from claripy.exceptions import DeviceNotFoundError

from dotenv import load_dotenv

if os.getenv("API_KEY") is None:
    load_dotenv()

if __name__ == "__main__":
    deployment = NodeS(os.getenv("API_KEY"))

    # ----- #
    # Usage #
    # ----- #
    
    # Example 1: create datasets for all possible devices
    # ---------
    # get all devices
    device_codes = deployment.__devices__.codes()
    deployment.__measurements__.export(
        codes=device_codes,
        save_path=f"{PATH_TO_TOP}/data/processed"
    )
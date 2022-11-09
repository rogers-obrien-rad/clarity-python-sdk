import os
import sys
import pathlib
sys.path.append(f"{pathlib.Path(__file__).resolve().parent.parent}")

from claripy.clarity import Clarity

from dotenv import load_dotenv

if os.getenv("API_KEY") is None:
    load_dotenv()

if __name__ == "__main__":
    connection = Clarity(os.getenv("API_KEY"))

    print(connection.__devices__.get())
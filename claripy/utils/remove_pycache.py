import os
import shutil
import pathlib

PATH_TO_TOP = pathlib.Path(__file__).resolve().parent.parent.parent

if __name__ == "__main__":
    """
    Searches through all the folders in the parent directory and removes all instances
    of the __pycache__ directory.
    """
    subdirs = [x[0] for x in os.walk(PATH_TO_TOP)]
    for subdir in subdirs:
        if "__pycache__" in subdir:
            shutil.rmtree(subdir)

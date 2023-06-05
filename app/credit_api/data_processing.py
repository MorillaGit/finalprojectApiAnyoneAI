import os
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def load_data_checkpoint(path):
    """
    Load picklable object from destination path.

    Parameters
    ----------
    filename : str
        name of the picklable objetc to save.

    path : str
        full path of destination directory.

    Returns
    -------
        Confirmation message.
    """
    if os.path.exists(path):
        with open(path, "rb") as f:
            filename = pickle.load(f)
            print(f"Object loaded successfully from {path}.")
            return filename
    else:
        return print(f"Object or {path} does not exist.")
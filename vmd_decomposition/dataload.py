import os
import pandas as pd

def data_load(data_path):
    data = pd.read_csv(data_path, parse_dates=['date'])

    return data
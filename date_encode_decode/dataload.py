import pandas as pd
import os

def data_load(path):
    parent_folder = os.path.dirname(os.getcwd())
    data_path = os.path.join(parent_folder + path)
    
    data = pd.read_csv(data_path, parse_dates=['date'])
    
    return data

import os
import pandas as pd
import visualize


def data_load_daily(path):
    parent_folder = os.path.dirname(os.getcwd())
    data_path = os.path.join(parent_folder + path)
    
    data_all = pd.read_csv(data_path,index_col='date', parse_dates=True)
    data_all.index = pd.to_datetime(data_all.index, format="%m/%d/%Y")
    data_price = data_all['price']
    data_price.index = data_all.index
    
    return data_price

def data_load_monthly(path):
    parent_folder = os.path.dirname(os.getcwd())
    data_path = os.path.join(parent_folder + path)

    data_all = pd.read_csv(data_path,index_col='date', parse_dates=True)
    data_all.index = pd.to_datetime(data_all.index, format="%m/%d/%Y")
    
    return data_all
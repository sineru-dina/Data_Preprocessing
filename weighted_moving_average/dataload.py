import os
import pandas as pd

def data_load(data_path):
    data_all = pd.read_csv(data_path,index_col='date', parse_dates=True)
    data_all.index = pd.to_datetime(data_all.index, format="%m/%d/%Y")
    data_price = data_all['price']

    return data_price
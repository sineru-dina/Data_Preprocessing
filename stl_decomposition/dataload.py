import os
import pandas as pd
import visualize

curr_wd = os.getcwd()
data_path = os.path.join(curr_wd + '/data/price_data.csv')

def data_load_daily(data_path):
    data_all = pd.read_csv(data_path,index_col='date', parse_dates=True)
    data_all.index = pd.to_datetime(data_all.index, format="%m/%d/%Y")
    data_price = data_all['price']
    data_price.index = data_all.index
    
    return data_price

def data_load_monthly(data_path):
    data_all = pd.read_csv(data_path,index_col='date', parse_dates=True)
    data_all.index = pd.to_datetime(data_all.index, format="%m/%d/%Y")
    
    return data_all
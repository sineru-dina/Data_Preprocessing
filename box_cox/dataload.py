import os
import pandas as pd
import visualize

curr_wd = os.getcwd()
data_path = os.path.join(curr_wd + '/data/vol_data.csv')

def data_load(data_path):
    data_all = pd.read_csv(data_path,index_col='date', parse_dates=True)
    data_all.index = pd.to_datetime(data_all.index, format="%m/%d/%Y")
    data_vol = data_all['volume']

    visualize.data_plot(data_vol, lambdas=None, simple=True, sub=False, hist=False)

    return data_vol



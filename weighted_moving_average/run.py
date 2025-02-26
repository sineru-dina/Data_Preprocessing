import pandas as pd
import argparse

import dataload
import wma
import visualize

parser = argparse.ArgumentParser(description='Calculate the weighted moving average of a given dataset.')

parser.add_argument('--data_path', type=str, default='data/price_data.csv', help='Path to the price data file')
parser.add_argument('--weight', type=int, default=5, help='Number of past values to consider for the weighted moving average')

args = parser.parse_args()

# Load the data
data_price = dataload.data_load(args.data_path)
data_df = pd.DataFrame(data_price, columns=['price'])

# Calculate the weighted moving average
data_with_smoothen_data = wma.wma_cal(data_df, args.weight)

# Visualize original and smoothed data
visualize.plot_wma(data_with_smoothen_data)
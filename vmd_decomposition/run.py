import pandas as pd
import argparse

import dataload
import vmd
import visualize

parser = argparse.ArgumentParser(description='Calculate the weighted moving average of a given dataset.')

parser.add_argument('--data_path', type=str, default='data/price_data.csv', help='Path to the price data file')
parser.add_argument('--xseq', type=int, default=256, help='length of the past sequence used for analysis')
parser.add_argument('--yseq', type=int, default=8, help='length of the future sequence to predict')
parser.add_argument('--term', type=int, default=98, help='offset or forecasting horizon')
parser.add_argument('--k', type=int, default=5, help='Number of modes')
parser.add_argument('--be_idx', type=int, default=10, help='buffer index or exclusion index')
parser.add_argument('--sig_decomp', type=int, default=0, help='signal decomposition index: mode (IMF) to use from the decomposed signal.')

args = parser.parse_args()

# Load the data
data_price = dataload.data_load(args.data_path)

# Perform VMD decomposition
data = vmd.vmd_decomposition(data_price, args.xseq, args.yseq, args.term, args.k, args.be_idx, args.sig_decomp)

# Fill NaN values with 0 for plotting
data.fillna(0, inplace=True)

# Visualize original and smoothed data
visualize.plot_vmd(data, args.k)
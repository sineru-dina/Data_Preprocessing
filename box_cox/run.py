import numpy as np
import scipy.stats as boxcox
import argparse

import dataload
from boxcox import boxcox_transformation
import visualize

parser = argparse.ArgumentParser(description='Box-Cox transformation')

parser.add_argument('--data_path', type=str, default='data/vol_data.csv', help='Path to the volume data file')
parser.add_argument('--lambda_range', type=str, default='-3,3,15', help='Comma-separated string for lambda range (min,max,num)')

args = parser.parse_args()

## Load the data and visualize
data_vol = dataload.data_load(args.data_path)

lambda_min, lambda_max, num_lambdas = map(float, args.lambda_range.split(','))
lambdas = np.linspace(lambda_min, lambda_max, int(num_lambdas))

## Perform Box-Cox transformation
transformed_data = boxcox_transformation(data_vol, lambdas)

## Find the best lambda
data_transformed, best_lambda = boxcox(data_vol)
print(f"Best lambda found: {best_lambda:.4f}")

## Transform the data using the best lambda
best_transformed_data = (data_vol**best_lambda - 1) / best_lambda

## Visualize the best transformed data
visualize.data_plot(best_transformed_data, lambdas=None, simple=False, sub=False, hist=True)

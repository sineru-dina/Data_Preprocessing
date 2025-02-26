import argparse

import dataload
import stl_decomp
import forecast
import visualize

parser = argparse.ArgumentParser(description='STL Decompostion')

parser.add_argument('--data_path_daily', type=str, default='/data/price_data.csv', help='Path to the price data file')
parser.add_argument('--data_path_monthly', type=str, default='/data/price_monthly.csv', help='Path to the monthly price data file')
parser.add_argument('--test_date', type=str, default='2024.01.01', help='date until STL method should be used to decompoition the data')
parser.add_argument('--test_year', type=int, default=2024, help='year until STL method should be used to decompoition the data')

args = parser.parse_args()

## Load daily price data
daily_price = dataload.data_load_daily(args.data_path_daily)

## Selection of valid data for STL decomposition
daily_price = daily_price.loc[:args.test_date]

## STL Decomposition of daily data
seasonal, trend, residual, time_series_daily = stl_decomp.stl_decompose_daily(args.test_date, daily_price, freq=30, seasonal_period=121, trend_period=301)
## Visualizing the results of STL decomposition
visualize.data_plot(time_series_daily, seasonal, trend, residual)

## Forecasting next 3 months daily price with Sarima model
forecast_df, seasonal_, trend_, residual_ = forecast.sarima_forecast(trend, seasonal, residual, args.test_date, forecast_horizon=120, freq='D')
visualize.forecast_plot(time_series_daily, seasonal_, trend_, residual_, forecast_df)



## Load monthly price data
monthly_price = dataload.data_load_monthly(args.data_path_monthly)

## STL Decomposition of monthly data
seasonal, trend, residual, time_series_monthly = stl_decomp.stl_decompose_monthly(args.test_year, monthly_price, freq=12, seasonal_period=13, trend_period=13)

## Visualizing the results of STL decomposition
visualize.data_plot(time_series_monthly, seasonal, trend, residual)

## Forecasting next 5 months price with Sarima model
forecast_df, seasonal_, trend_, residual_ = forecast.sarima_forecast(trend, seasonal, residual, args.test_date, forecast_horizon=5, freq='M')

## Visualizing the results of forecast
visualize.forecast_plot(time_series_monthly, seasonal_, trend_, residual_, forecast_df)

## Printing the final forecast for next 5 months
print("Final forecast for next 5 months:")
print(forecast_df['final_forecast'])


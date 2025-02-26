import pandas as pd
from statsmodels.tsa.seasonal import STL

def stl_decompose_daily(test_date, time_series_data, freq, seasonal_period, trend_period):
    test_date = pd.to_datetime(test_date)    
    start_date = pd.to_datetime("2012-01-01")

    data_range = pd.date_range(start=start_date, end=test_date, freq='d')
    
    time_series = pd.Series(time_series_data, index=data_range)
    time_series = time_series.fillna(0)

    stl = STL(time_series, period = freq, seasonal = seasonal_period, trend = trend_period, robust=True)

    result = stl.fit()

    seasonal = result.seasonal
    trend = result.trend
    residual = result.resid

    return seasonal, trend, residual, time_series

def stl_decompose_monthly(test_year, data, freq, seasonal_period, trend_period):
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    time_series_data = []
    test_date = pd.to_datetime(f"{test_year+1}-01-31")


    test_date = pd.to_datetime(f"{test_year}-12-31")
    
    start_date = pd.to_datetime("2000-01-01")

    data_range = pd.date_range(start=start_date, end=test_date, freq='M')

    yr = int(data_range.strftime("%Y")[-1])+1
    
    for year in range(2000, yr):
        for month in months:
            col_name = f"{month}_price"
            if col_name in data.columns:
                price = data.loc[data.index.year == int(year), col_name]
                time_series_data.append(price)
    
    time_series = pd.Series(time_series_data, index=data_range)
    
    stl = STL(time_series, period = freq, seasonal = seasonal_period, trend = trend_period, robust=True)

    result = stl.fit()

    seasonal = result.seasonal
    trend = result.trend
    residual = result.resid

    return seasonal, trend, residual, time_series
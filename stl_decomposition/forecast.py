import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

def sarima_forecast(trend, seasonal, residual, test_date, forecast_horizon=5, freq='M'):
    trend_ = trend.loc[trend.index < test_date]
    seasonal_ = seasonal.loc[seasonal.index < test_date]
    residual_ = residual.loc[residual.index < test_date]

    stl_list = [trend_, seasonal_, residual_]
    stl_names = ["trend", "seasonal", "residual"]

    for stl, name in zip(stl_list, stl_names):
        sarima_ = SARIMAX(stl, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
        results_ = sarima_.fit(disp=False)
        forecast_ = results_.get_forecast(steps=forecast_horizon)
        forecast_mean = forecast_.predicted_mean

        if name == "trend":
            forecast_trend_mean = forecast_mean
        elif name == "seasonal":
            forecast_seasonal_mean = forecast_mean
        elif name == "residual":
            forecast_residual_mean = forecast_mean
        
    final_forecast = (
        forecast_trend_mean + 
        forecast_seasonal_mean + 
        forecast_residual_mean
    )

    future_dates = pd.date_range(start=trend_.index[-1] + pd.Timedelta(days=30), periods=forecast_horizon, freq=freq)
    forecast_df = pd.DataFrame({
        "date": future_dates,
        "season": forecast_seasonal_mean,
        "trend": forecast_trend_mean,
        "resid": forecast_residual_mean,
        "final_forecast": final_forecast
    }).set_index("date")

    return forecast_df, seasonal_, trend_, residual_
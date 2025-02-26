import matplotlib.pyplot as plt

def data_plot(time_series, seasonal, trend, residual):
    plt.figure(figsize=(15, 10))
    plt.subplot(4, 1, 1)
    plt.plot(time_series, label='Original', color='black')
    plt.legend(loc='upper left')

    plt.subplot(4, 1, 2)
    plt.plot(seasonal, label='Seasonal', color='blue')
    plt.legend(loc='upper left')

    plt.subplot(4, 1, 3)
    plt.plot(trend, label='Trend', color='orange')
    plt.legend(loc='upper left')

    plt.subplot(4, 1, 4)
    plt.plot(residual, label='Residual', color='green')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

def forecast_plot(time_series, seasonal_, trend_, residual_, forecast_df):
    plt.figure(figsize=(15, 10))
    plt.plot(time_series, label='Original', color='black')

    plt.plot(seasonal_, label="Seasonal (Observed)", color="blue")  # Observed seasonal component
    plt.plot(forecast_df["season"], label="Seasonal (Forecast)", linestyle="dashed", color="blue")
    
    plt.plot(trend_, label="Trend (Observed)", color="orange")  # Observed trend component
    plt.plot(forecast_df["trend"], label="Trend (Forecast)", linestyle="dashed", color="orange")

    plt.plot(residual_, label="Residual (Observed)", color="green")  # Observed trend component
    plt.plot(forecast_df["resid"], label="Residual (Forecast)", linestyle="dashed", color="green")

    plt.plot(forecast_df['final_forecast'], label="Final (Forecast)", linestyle="dashed", color="red")

    all_index = seasonal_.index.union(forecast_df.index)  # Merge both indices without duplicates
    yearly_ticks = all_index[all_index.month == 1]  # Select only January for yearly marking

    plt.xticks(ticks=yearly_ticks, labels=yearly_ticks.year, rotation=45)
    plt.legend()
    plt.show()
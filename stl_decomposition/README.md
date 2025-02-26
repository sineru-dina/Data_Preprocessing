# STL Decomposition: Seasonal-Trend Decomposition using LOESS
The repository includes theoretical explanations, Python implementations, and practical applications of STL decomposition for time series analysis.


## Introduction to STL  

STL (Seasonal-Trend decomposition using LOESS) is a robust and flexible method for decomposing a time series into three key components:  

1. **Seasonal Component**: Captures repeating patterns that occur at fixed intervals (e.g., daily, monthly, or yearly seasonality).  
2. **Trend Component**: Represents the long-term upward or downward movement in the data.  
3. **Residual (Remainder) Component**: Accounts for random noise or variations not explained by the trend or seasonal components.  

STL offers several advantages:  
✅ **Handles Non-Stationary Seasonality** – Adaptable to changes in seasonal patterns over time.  
✅ **Robust to Outliers** – Uses LOESS (Locally Estimated Scatterplot Smoothing) to smooth the trend and seasonal components.  
✅ **Flexible Seasonal Window Selection** – Allows control over how much variation is captured in the seasonal component.  

### **Mathematical Representation**  
Given a time series $Y_t$, STL decomposition expresses it as:  

$$
Y_t = T_t + S_t + R_t
$$

where:  
- $T_t$ is the trend component  
- $S_t$ is the seasonal component  
- $R_t$ is the residual component  

STL is widely used in **forecasting, anomaly detection, and time series analysis**, making it an essential tool in data science and econometrics.

## Experiments and Forecasting  

🔹 **Real-World Dataset:** This project applies STL decomposition on a real-world dataset to analyze and extract seasonal and trend components.  
🔹 **Forecasting with SARIMAX:** After decomposition, the **SARIMAX (Seasonal AutoRegressive Integrated Moving Average with Exogenous Regressors)** model is used to make future predictions based on the extracted trend and seasonal components.  

## Repository Contents  
- 📖 **Theoretical Notes** on STL decomposition  
- 🐍 **Python Implementations** using `statsmodels`  
- 📊 **Real-world Experiments** with actual time series data  
- 📈 **Forecasting using SARIMAX**

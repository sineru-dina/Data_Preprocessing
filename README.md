# Data Preprocessing

This repository contains various data preprocessing techniques commonly used in time series analysis and machine learning. It includes implementations and updates for several methods such as Box-Cox transformation, STL decomposition, Weighted Moving Average (WMA), and Variational Mode Decomposition (VMD).

## Techniques Implemented

### 1. **Box-Cox Transformation**
   - The Box-Cox transformation is used to stabilize variance and make data more closely resemble a normal distribution. It is particularly useful for handling non-normal data in time series.

### 2. **STL Decomposition (Seasonal and Trend decomposition using Loess)**
   - STL decomposition is used to separate a time series into three components: trend, seasonality, and residuals. This is especially useful for forecasting and anomaly detection.

### 3. **Weighted Moving Average (WMA)**
   - WMA is a smoothing technique that gives more weight to recent observations. It is often used in time series forecasting to reduce noise and capture trends.

### 4. **VMD Decomposition (Variational Mode Decomposition)**
   - VMD is an advanced signal decomposition technique that decomposes a signal into several intrinsic mode functions (IMFs), useful for noise reduction and extracting underlying trends from complex data.

### 5. **Data_encode_decode**
   - This module implements Cyclical Encoding, a technique used for encoding cyclical features such as hours of the day, days of the week, or months of the year. This approach is useful in machine learning models, as it ensures that cyclical patterns (e.g., the transition from December to January) are treated as continuous rather than discrete. The encoding uses sine and cosine transformations to map the cyclical features to two continuous values, allowing models to capture their periodic nature effectively.

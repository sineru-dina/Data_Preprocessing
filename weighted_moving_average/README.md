# Weighted Moving Average (WMA)

This repository contains implementations and experiments related to Weighted Moving Average (WMA), a statistical method used to smooth time series data by giving more weight to recent observations. WMA is widely used in time series analysis, forecasting, and signal processing due to its ability to provide a more responsive smoothing approach compared to simple moving averages.

Key concepts include:

* Weighted Averaging: Unlike the simple moving average (SMA), WMA assigns different weights to each data point in the window, with higher weights given to more recent data.
* Smoothing: The technique is often used to reduce noise and make underlying patterns (e.g., trends or seasonality) in the data more apparent.
* Applications: Commonly applied in areas like stock price forecasting, temperature trend analysis, and other time-dependent data.

This repository provides Python code, theoretical explanations, and practical examples for applying WMA on real-world price data of a product and smoothing noisy data.

## Concept of Moving Averages  
A moving average smooths out fluctuations in data, helping to identify trends by averaging past values over a specified time period (window size).

### Types of Moving Averages:
- **Simple Moving Average (SMA):** All values are weighted equally.
- **Weighted Moving Average (WMA):** Assigns different weights to values.
- **Exponential Moving Average (EMA):** Uses a decaying exponential function for weighting.

---

## How Weighted Moving Average (WMA) Works  
The **Weighted Moving Average (WMA)** places more emphasis on the most recent data points. The weights typically decrease linearly, so the newest value gets the highest weight, while the oldest value gets the lowest weight.

This makes WMA more responsive to recent changes in the data compared to a simple moving average.

---

## Formula for WMA  
The formula to calculate the Weighted Moving Average for a dataset $P_t$ (prices or values) over a period $n$ is:

$$ WMA = \frac{\sum_{i=1}^{n} (P_i \times W_i)}{\sum_{i=1}^{n} W_i} $$

Where:  
- $P_i$ is the value at position $i$.  
- $W_i$ is the weight assigned to $P_i$.  
- $\sum W_i$ is the sum of all weights.

---

## Example Calculation  
Consider a 3-day WMA with the following data:

| Day  | Price ($P$) | Weight ($W$) |
|------|-----------------|-----------------|
| 1    | 10              | 1               |
| 2    | 20              | 2               |
| 3    | 30              | 3               |

### Steps:
1. Multiply each price by its corresponding weight:
   - $(10 \times 1)$ + $(20 \times 2)$ + $(30 \times 3)$ = $10 + 40 + 90 = 140$
2. Sum of weights:  
   - $1 + 2 + 3 = 6$
3. Compute WMA:  
   - WMA $= \frac{140}{6} = 23.33$

So, the weighted moving average for this 3-day period is **$23.33$**.

# Distance-Based Pair Trading Strategy

This project implements a distance-based pair trading strategy using historical stock data. The strategy aims to identify pairs of stocks whose price movements are most similar by measuring the Euclidean distance between their normalized prices. Once these pairs are identified, the strategy opens positions based on the spread between the two stocks.

## Overview

The core idea behind this project is to select pairs of stocks based on the smallest Euclidean distance between their price movements. Once the pairs are identified, the spread between their prices is calculated, and trades are executed when the spread deviates significantly from its mean. This deviation is measured using volatility, and the strategy is designed to profit from mean reversion in the spread.

## Features

- **Distance Calculation**: Calculates the Euclidean distance between normalized stock prices to identify the most similar pairs of stocks.
- **Spread Calculation**: For each identified pair, calculates the spread as the difference between the two stock prices.
- **Mean Reversion Strategy**: Opens and closes positions based on the spread's deviation from its mean, using volatility to set entry and exit points.
- **Transaction Simulation**: Simulates trading by adjusting the portfolio based on the positions in the identified pairs of stocks.

## Requirements

To run this project, you need to install the following Python libraries:

- `numpy`
- `pandas`
- `yfinance`
- `statsmodels`
- `matplotlib`

## How It Works

The distance-based pair trading strategy involves the following key steps:

1. **Data Retrieval**:
   - The `distance_approach` function uses the `yfinance` library to download historical adjusted closing prices for the specified stock tickers.
   - Data is retrieved for the given date range (from `start_date` to `end_date`).
   - Missing values (NaNs) in the data are removed for each stock.

2. **Normalization**:
   - Each stock’s adjusted closing prices are normalized between 0 and 1.
   - This normalization is done by scaling the prices based on the minimum and maximum values of the stock’s price over the chosen period.
   - Normalization ensures that all stocks, regardless of their original price scale, are comparable.

3. **Distance Calculation**:
   - The Euclidean distance between the normalized prices of each pair of stocks is calculated.
   - The formula used for the distance between two stocks `s1` and `s2` is:
   
     \[
     \text{distance} = \sum \left( \text{normalized price of } s1 - \text{normalized price of } s2 \right)^2
     \]

   - The goal is to identify pairs of stocks whose price movements are most similar, as indicated by the smallest Euclidean distance.

4. **Spread Calculation**:
   - Once pairs are identified, the spread is calculated as the difference between the two stocks' prices.
   - For a given pair of stocks, the spread is computed as:
   
     \[
     \text{spread} = \text{price of } s2 - \text{price of } s1
     \]

   - The spread measures how far apart the two stocks are, which will be important for identifying when to enter and exit trades.

5. **Volatility and Mean Calculation**:
   - The mean and volatility of the spread are calculated:
     - **Mean**: The average value of the spread over the entire time period.
     - **Volatility**: The standard deviation of the spread, which measures how much the spread fluctuates around its mean.
   - These statistical measures help define the thresholds for when to enter or exit a position in the pair.

6. **Positioning**:
   - The strategy looks for points where the spread deviates significantly from its mean, beyond a volatility threshold:
     - **Entry Signal**: When the spread is greater than the mean plus one standard deviation (upper threshold), a short position is opened in `s1` and a long position in `s2`.
     - **Exit Signal**: When the spread is less than the mean minus one standard deviation (lower threshold), the position is reversed (long `s1` and short `s2`).
   - These entry and exit points are based on the assumption that the spread will revert to its mean over time.

7. **Portfolio Tracking**:
   - The strategy tracks the portfolio value by adjusting it as trades are executed.
   - The portfolio value is updated based on the positions held in the identified stock pairs.
   - At the end of the period, the final portfolio value is returned, reflecting the profits or losses from the strategy.

By following this approach, the strategy aims to profit from the mean-reverting behavior of the spread between two similar stocks. The goal is to open positions when the spread is too wide and close them when the spread narrows, assuming that the spread will revert to the mean over time.



The strategy generates a profit of 5662.47 USD (Initial amount=0) on first 30 stocks of S&P500 index (Selected in alphabatical order) from 2019-01-01 to 2024-01-01. Transcation fees are ignored.
![image](https://github.com/RonSheoran123/pairsTrading_distanceApproach/assets/106268100/7f5fa604-8b08-48d8-ab2c-2eef6202ac57)

# Good_results_stock_screener

# Stock Analysis Script

This repository contains a Python script that performs stock analysis using the `yfinance` library. The script reads a list of stock tickers from a CSV file and performs the following tasks:

1. Retrieves the latest and previous year's EPS (Earnings Per Share) values.
2. Compares the EPS values to identify stocks with significant improvement.
3. Calculates the percentage change in the stock price over the past year and writes the results to a text file.

## Features

- **EPS Analysis:** Compares EPS of the current year with the previous year's EPS to find significant improvements.
- **Price Calculation:** Calculates the percentage change in stock price from one year ago to the present.
- **Error Handling:** Logs any errors encountered during data retrieval to a text file.

## Prerequisites

Ensure you have the following Python packages installed:

- `pandas`
- `yfinance`

You can install these packages using pip:

```bash
pip install pandas yfinance

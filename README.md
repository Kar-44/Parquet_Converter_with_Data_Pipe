# Stock Market CSV to Parquet Converter

A Python utility that fetches historical sample stock market data directly from Kaggle, strips 'Adj Close' column for simplicity, and converts it into compressed Parquet format for optimized query and storage performance.

This project utilizes dataset files from the [Stock Market Dataset](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset) on Kaggle.

## Features

- **Direct Kaggle Integration:** Fetch specific stock CSV files directly into memory using `kagglehub`. This speeds up data preparation process.
- **Data Cleanup:** Automatically strips the `Adj Close` column to keep data concise and simple.
- **Fast Parquet Export:** Converts data into Apache Parquet format using `pyarrow`.
- **Automatic Directory Creation:** Creates the target output folder if it doesn't already exist.

## Requirements:

Before running the script, ensure you have Python 3 installed along with the required libraries.

```bash
pip install pandas pyarrow kagglehub
```

## How to run:
1. Open the script.
2. Open terminal and type in: `python3 parqconvert.py TICKER.csv /path/to/folder`
3. If the script runs correctly you will see a Success message and a TICKER.parquet file in the indicated folder.

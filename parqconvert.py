import sys
import os
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter


def download_and_convert(filename: str, dest_dir: str):
    # Construct the internal path used by the Kaggle dataset
    file_path = f"stocks/{filename}"

    # Construct the final destination path for the parquet file
    parquet_filename = os.path.splitext(filename)[0] + '.parquet'
    parquet_path = os.path.join(dest_dir, parquet_filename)

    try:
        print(f"  -> Fetching '{file_path}' from Kaggle...")
        # Load the dataset directly into a Pandas DataFrame
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "jacksoncrow/stock-market-dataset",
            file_path
        )
        print(f"  -> Successfully loaded {len(df)} rows.")

        # Delete the 'Adj Close' column if it exists
        if 'Adj Close' in df.columns:
            print("  -> Dropping 'Adj Close' column...")
            df = df.drop(columns=['Adj Close'])

        # Ensure the destination directory exists (creates it if it doesn't)
        os.makedirs(dest_dir, exist_ok=True)

        print(f"  -> Converting to '{parquet_path}'...")
        df.to_parquet(parquet_path, engine='pyarrow', index=False)
        print(f"  -> SUCCESS! Created: {parquet_path}")

    except Exception as e:
        print(f"  -> ERROR during fetch or conversion: {e}")


if __name__ == "__main__":
    print("Script started successfully...")

    # Check if exactly 2 arguments (script name + filename + dest path) were provided
    if len(sys.argv) < 3:
        print("ERROR: Missing arguments. Please run as:")
        print("python3 parqconvert.py AAPL.csv /path/to/folder")
        sys.exit(1)

    # Get the arguments
    input_filename = sys.argv[1]  # e.g., AAPL.csv
    dest_folder = sys.argv[2]  # e.g., /path/to/folder

    # Validate the file extension
    if not input_filename.lower().endswith('.csv'):
        print(f"ERROR: The requested file '{input_filename}' should end in .csv")
        sys.exit(1)

    print(f"Target file: '{input_filename}'")
    print(f"Destination folder: '{dest_folder}'")

    download_and_convert(input_filename, dest_folder)
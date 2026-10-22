import os
import pandas as pd

# Get filename from user
file_path = input("Enter the file path (CSV or JSON): ").strip()

if not os.path.exists(file_path):
    print("Error: File does not exist.")
else:
    # Identify file type and read data
    if file_path.lower().endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.lower().endswith('.json'):
        df = pd.read_json(file_path)
    else:
        print("Error: Unsupported file format. Please provide a CSV or JSON file.")
        df = None

    # Display analysis
    if df is not None:
        print("\n--- Dataset Summary ---")
        print(f"Number of records: {len(df)}")
        print(f"Number of fields: {len(df.columns)}")
        print(f"Field names: {list(df.columns)}")
        
        print("\nMissing values per field:")
        print(df.isnull().sum())

print("missing file ")
print("invalis input")
print("Empty CSV")
print("unsupported file format")
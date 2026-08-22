import pandas as pd
import os

# Path to raw data
raw_path = "data/raw/flipkart data"

# Output path
output_path = "data/cleaned/flipkart_master.csv"

# File and category mapping
files = {
    "flipkart_laptops.csv": "Laptop",
    "flipkart_mobiles.csv": "Mobile",
    "flipkart_refrigerator.csv": "Refrigerator",
    "flipkart_smart_watch.csv": "Smartwatch",
    "flipkart_tv.csv": "TV",
    "flipkart_washing_machine.csv": "Washing Machine"
}

dataframes = []

for file, category in files.items():

    file_path = os.path.join(raw_path, file)

    df = pd.read_csv(file_path, encoding="latin1")

    # Add category column
    df["Category"] = category

    dataframes.append(df)

    print(f"{category}: {df.shape[0]} products loaded")


# Combine all datasets
master_df = pd.concat(dataframes, ignore_index=True)

print("\n" + "=" * 60)
print("MASTER DATASET")
print("=" * 60)

print("Shape:", master_df.shape)

print("\nCategories:")
print(master_df["Category"].value_counts())

print("\nColumns:")
print(master_df.columns.tolist())

# Save master dataset
master_df.to_csv(output_path, index=False)

print("\nMaster dataset saved successfully!")
print("Location:", output_path)
import pandas as pd

# Load master dataset
df = pd.read_csv(
    "data/cleaned/flipkart_master.csv",
    encoding="latin1"
)

print("=" * 60)
print("DATA QUALITY CHECK")
print("=" * 60)

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Unique brands
print("\nNumber of Unique Brands:")
print(df["Brand"].nunique())

# Categories
print("\nCategories:")
print(df["Category"].value_counts())

# Numerical summary
print("\nNumerical Summary:")
print(df.describe())
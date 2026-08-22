import pandas as pd

# Load original master dataset
df = pd.read_csv(
    "data/cleaned/flipkart_master.csv",
    encoding="latin1"
)

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)


# --------------------------------------------------
# 1. Clean Discount
# --------------------------------------------------

df["Discount"] = (
    df["Discount"]
    .astype(str)
    .str.extract(r"(\d+)")
)

df["Discount"] = pd.to_numeric(
    df["Discount"],
    errors="coerce"
)


# --------------------------------------------------
# 2. Extract Ratings Count
# --------------------------------------------------

df["Ratings_Count"] = (
    df["No_of_ratings"]
    .astype(str)
    .str.extract(r"(\d+)")
)

df["Ratings_Count"] = pd.to_numeric(
    df["Ratings_Count"],
    errors="coerce"
)


# --------------------------------------------------
# 3. Extract Reviews Count
# --------------------------------------------------

df["Reviews_Count"] = (
    df["No_of_ratings"]
    .astype(str)
    .str.extract(r"(\d+)\s*Reviews")
)
df["Reviews_Count"] = pd.to_numeric(
    df["Reviews_Count"],
    errors="coerce"
)


# --------------------------------------------------
# 4. Convert numerical columns
# --------------------------------------------------

df["Selling Price"] = pd.to_numeric(
    df["Selling Price"],
    errors="coerce"
)

df["MRP"] = pd.to_numeric(
    df["MRP"],
    errors="coerce"
)

df["Ratings"] = pd.to_numeric(
    df["Ratings"],
    errors="coerce"
)


# --------------------------------------------------
# 5. Check missing values
# --------------------------------------------------

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# --------------------------------------------------
# 6. Remove duplicates
# --------------------------------------------------

before = len(df)

df = df.drop_duplicates()

after = len(df)

print("\nDuplicates removed:", before - after)


# --------------------------------------------------
# 7. Display cleaned columns
# --------------------------------------------------

print("\nCleaned Discount:")
print(df["Discount"].head())

print("\nRatings Count:")
print(df["Ratings_Count"].head())

print("\nReviews Count:")
print(df["Reviews_Count"].head())


# --------------------------------------------------
# 8. Save cleaned dataset
# --------------------------------------------------

output_path = "data/cleaned/flipkart_cleaned.csv"

df.to_csv(
    output_path,
    index=False
)

print("\n" + "=" * 60)
print("CLEANING COMPLETED SUCCESSFULLY!")
print("=" * 60)

print("Final Shape:", df.shape)
print("Saved at:", output_path)
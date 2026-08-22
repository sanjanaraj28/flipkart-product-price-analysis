import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================================
# FLIPKART PRODUCT PRICE ANALYSIS - VISUALIZATION
# ============================================================

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned/flipkart_cleaned.csv",
    encoding="latin1"
)

# Create output folder
output_folder = "visualization/charts"
os.makedirs(output_folder, exist_ok=True)

print("=" * 60)
print("FLIPKART DATA VISUALIZATION")
print("=" * 60)


# ============================================================
# 1. PRODUCT COUNT BY CATEGORY
# ============================================================

category_count = df["Category"].value_counts()

plt.figure(figsize=(10, 6))
category_count.plot(kind="bar")

plt.title("Product Count by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    f"{output_folder}/01_product_count_by_category.png",
    dpi=300
)
plt.close()

print("1. Product Count by Category - Saved")


# ============================================================
# 2. AVERAGE SELLING PRICE BY CATEGORY
# ============================================================

avg_price = (
    df.groupby("Category")["Selling Price"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
avg_price.plot(kind="bar")

plt.title("Average Selling Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Selling Price (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    f"{output_folder}/02_average_selling_price.png",
    dpi=300
)
plt.close()

print("2. Average Selling Price - Saved")


# ============================================================
# 3. AVERAGE DISCOUNT BY CATEGORY
# ============================================================

avg_discount = (
    df.groupby("Category")["Discount"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
avg_discount.plot(kind="bar")

plt.title("Average Discount by Category")
plt.xlabel("Category")
plt.ylabel("Average Discount (%)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    f"{output_folder}/03_average_discount.png",
    dpi=300
)
plt.close()

print("3. Average Discount - Saved")


# ============================================================
# 4. AVERAGE RATING BY CATEGORY
# ============================================================

avg_rating = (
    df.groupby("Category")["Ratings"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
avg_rating.plot(kind="bar")

plt.title("Average Rating by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.ylim(0, 5)
plt.tight_layout()

plt.savefig(
    f"{output_folder}/04_average_rating.png",
    dpi=300
)
plt.close()

print("4. Average Rating - Saved")


# ============================================================
# 5. SELLING PRICE DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Selling Price"],
    bins=30
)

plt.title("Selling Price Distribution")
plt.xlabel("Selling Price (₹)")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/05_price_distribution.png",
    dpi=300
)
plt.close()

print("5. Price Distribution - Saved")


# ============================================================
# 6. SELLING PRICE VS RATINGS
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Selling Price"],
    df["Ratings"],
    alpha=0.5
)

plt.title("Selling Price vs Rating")
plt.xlabel("Selling Price (₹)")
plt.ylabel("Rating")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/06_price_vs_rating.png",
    dpi=300
)
plt.close()

print("6. Price vs Rating - Saved")


# ============================================================
# 7. TOP 10 BRANDS BY PRODUCT COUNT
# ============================================================

top_brands = (
    df["Brand"]
    .value_counts()
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

top_brands.plot(kind="barh")

plt.title("Top 10 Brands by Product Count")
plt.xlabel("Number of Products")
plt.ylabel("Brand")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/07_top_brands.png",
    dpi=300
)
plt.close()

print("7. Top Brands - Saved")


# ============================================================
# 8. TOP 10 BRANDS BY TOTAL RATINGS
# ============================================================

popular_brands = (
    df.groupby("Brand")["Ratings_Count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))

popular_brands.plot(kind="barh")

plt.title("Top 10 Brands by Total Ratings")
plt.xlabel("Total Number of Ratings")
plt.ylabel("Brand")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/08_top_brands_by_ratings.png",
    dpi=300
)
plt.close()

print("8. Top Brands by Ratings - Saved")


# ============================================================
# 9. MRP VS SELLING PRICE
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["MRP"],
    df["Selling Price"],
    alpha=0.5
)

plt.title("MRP vs Selling Price")
plt.xlabel("MRP (₹)")
plt.ylabel("Selling Price (₹)")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/09_mrp_vs_selling_price.png",
    dpi=300
)
plt.close()

print("9. MRP vs Selling Price - Saved")


# ============================================================
# 10. DISCOUNT DISTRIBUTION
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Discount"],
    bins=20
)

plt.title("Discount Distribution")
plt.xlabel("Discount (%)")
plt.ylabel("Number of Products")
plt.tight_layout()

plt.savefig(
    f"{output_folder}/10_discount_distribution.png",
    dpi=300
)
plt.close()

print("10. Discount Distribution - Saved")


# ============================================================
# COMPLETED
# ============================================================

print("\n" + "=" * 60)
print("VISUALIZATION COMPLETED SUCCESSFULLY!")
print("=" * 60)

print(f"\nCharts saved inside:")
print(output_folder)
import pandas as pd

# ============================================================
# FLIPKART PRODUCT PRICE ANALYSIS - EDA
# ============================================================

# Load cleaned dataset
df = pd.read_csv(
    "data/cleaned/flipkart_cleaned.csv",
    encoding="latin1"
)

print("=" * 60)
print("FLIPKART PRODUCT PRICE ANALYSIS - EDA")
print("=" * 60)


# ============================================================
# 1. DATASET OVERVIEW
# ============================================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())


# ============================================================
# 2. PRODUCT COUNT BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("PRODUCT COUNT BY CATEGORY")
print("=" * 60)

category_count = (
    df["Category"]
    .value_counts()
)

print(category_count)


# ============================================================
# 3. AVERAGE SELLING PRICE BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE SELLING PRICE BY CATEGORY")
print("=" * 60)

avg_price = (
    df.groupby("Category")["Selling Price"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_price.round(2))


# ============================================================
# 4. AVERAGE MRP BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE MRP BY CATEGORY")
print("=" * 60)

avg_mrp = (
    df.groupby("Category")["MRP"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_mrp.round(2))


# ============================================================
# 5. AVERAGE DISCOUNT BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE DISCOUNT BY CATEGORY")
print("=" * 60)

avg_discount = (
    df.groupby("Category")["Discount"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_discount.round(2))


# ============================================================
# 6. AVERAGE RATING BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE RATING BY CATEGORY")
print("=" * 60)

avg_rating = (
    df.groupby("Category")["Ratings"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_rating.round(2))


# ============================================================
# 7. AVERAGE NUMBER OF RATINGS BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE NUMBER OF RATINGS BY CATEGORY")
print("=" * 60)

avg_ratings_count = (
    df.groupby("Category")["Ratings_Count"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_ratings_count.round(2))


# ============================================================
# 8. AVERAGE NUMBER OF REVIEWS BY CATEGORY
# ============================================================

print("\n" + "=" * 60)
print("AVERAGE NUMBER OF REVIEWS BY CATEGORY")
print("=" * 60)

avg_reviews = (
    df.groupby("Category")["Reviews_Count"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_reviews.round(2))


# ============================================================
# 9. TOP 10 BRANDS BY PRODUCT COUNT
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 BRANDS BY PRODUCT COUNT")
print("=" * 60)

top_brands = (
    df["Brand"]
    .value_counts()
    .head(10)
)

print(top_brands)


# ============================================================
# 10. TOP 10 MOST EXPENSIVE PRODUCTS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 MOST EXPENSIVE PRODUCTS")
print("=" * 60)

expensive_products = (
    df[
        [
            "Name",
            "Brand",
            "Category",
            "Selling Price"
        ]
    ]
    .sort_values(
        "Selling Price",
        ascending=False
    )
    .head(10)
)

print(
    expensive_products.to_string(
        index=False
    )
)


# ============================================================
# 11. TOP 10 HIGHEST DISCOUNT PRODUCTS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 HIGHEST DISCOUNT PRODUCTS")
print("=" * 60)

highest_discount = (
    df[
        [
            "Name",
            "Brand",
            "Category",
            "Selling Price",
            "Discount"
        ]
    ]
    .sort_values(
        "Discount",
        ascending=False
    )
    .head(10)
)

print(
    highest_discount.to_string(
        index=False
    )
)


# ============================================================
# 12. TOP 10 MOST RATED PRODUCTS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 MOST RATED PRODUCTS")
print("=" * 60)

most_rated = (
    df[
        [
            "Name",
            "Brand",
            "Category",
            "Ratings_Count",
            "Ratings"
        ]
    ]
    .sort_values(
        "Ratings_Count",
        ascending=False
    )
    .head(10)
)

print(
    most_rated.to_string(
        index=False
    )
)


# ============================================================
# 13. TOP 10 MOST REVIEWED PRODUCTS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 MOST REVIEWED PRODUCTS")
print("=" * 60)

most_reviewed = (
    df[
        [
            "Name",
            "Brand",
            "Category",
            "Reviews_Count"
        ]
    ]
    .sort_values(
        "Reviews_Count",
        ascending=False
    )
    .head(10)
)

print(
    most_reviewed.to_string(
        index=False
    )
)


# ============================================================
# 14. OVERALL PRICE STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("OVERALL PRICE STATISTICS")
print("=" * 60)

print(
    df[
        [
            "Selling Price",
            "MRP",
            "Discount"
        ]
    ].describe().round(2)
)


# ============================================================
# 15. OVERALL RATING STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("OVERALL RATING STATISTICS")
print("=" * 60)

print(
    df[
        [
            "Ratings",
            "Ratings_Count",
            "Reviews_Count"
        ]
    ].describe().round(2)
)


# ============================================================
# 16. HIGHEST RATED BRANDS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 BRANDS BY AVERAGE RATING")
print("=" * 60)

brand_rating = (
    df.groupby("Brand")
    .agg(
        Average_Rating=("Ratings", "mean"),
        Product_Count=("Name", "count")
    )
)

# Consider brands with at least 5 products
brand_rating = (
    brand_rating[
        brand_rating["Product_Count"] >= 5
    ]
    .sort_values(
        "Average_Rating",
        ascending=False
    )
    .head(10)
)

print(
    brand_rating.round(2)
)


# ============================================================
# 17. MOST POPULAR BRANDS
# ============================================================

print("\n" + "=" * 60)
print("TOP 10 BRANDS BY TOTAL RATINGS")
print("=" * 60)

popular_brands = (
    df.groupby("Brand")["Ratings_Count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(popular_brands)


# ============================================================
# 18. END OF EDA
# ============================================================

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY!")
print("=" * 60)
import pandas as pd

# ============================================================
# FLIPKART PRODUCT PRICE ANALYSIS - FINAL PROJECT SUMMARY
# ============================================================

print("=" * 70)
print("FLIPKART PRODUCT PRICE ANALYSIS - FINAL SUMMARY")
print("=" * 70)

# ------------------------------------------------------------
# 1. LOAD CLEANED DATA
# ------------------------------------------------------------

file_path = "data/cleaned/flipkart_cleaned.csv"

df = pd.read_csv(file_path)

print("\nDataset loaded successfully!")
print("Shape:", df.shape)


# ------------------------------------------------------------
# 2. BASIC INFORMATION
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("BASIC INFORMATION")
print("=" * 70)

print("Total Products:", len(df))
print("Total Columns:", len(df.columns))
print("Unique Brands:", df["Brand"].nunique())
print("Categories:", df["Category"].nunique())


# ------------------------------------------------------------
# 3. CATEGORY SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("CATEGORY SUMMARY")
print("=" * 70)

category_summary = df.groupby("Category").agg(
    Product_Count=("Name", "count"),
    Average_Selling_Price=("Selling Price", "mean"),
    Average_MRP=("MRP", "mean"),
    Average_Discount=("Discount", "mean"),
    Average_Rating=("Ratings", "mean"),
    Average_Ratings_Count=("Ratings_Count", "mean"),
    Average_Reviews_Count=("Reviews_Count", "mean")
).sort_values("Product_Count", ascending=False)

print(category_summary.round(2))


# ------------------------------------------------------------
# 4. MOST POPULAR CATEGORY
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("CATEGORY INSIGHTS")
print("=" * 70)

product_count = df["Category"].value_counts()

print("Most Products Category:")
print(product_count.idxmax(), "-", product_count.max(), "products")

print("\nHighest Average Selling Price:")
highest_price_category = df.groupby("Category")["Selling Price"].mean().idxmax()
highest_price = df.groupby("Category")["Selling Price"].mean().max()

print(highest_price_category, "-", round(highest_price, 2))

print("\nHighest Average Discount:")
highest_discount_category = df.groupby("Category")["Discount"].mean().idxmax()
highest_discount = df.groupby("Category")["Discount"].mean().max()

print(highest_discount_category, "-", round(highest_discount, 2), "%")

print("\nHighest Average Rating:")
highest_rating_category = df.groupby("Category")["Ratings"].mean().idxmax()
highest_rating = df.groupby("Category")["Ratings"].mean().max()

print(highest_rating_category, "-", round(highest_rating, 2))

print("\nHighest Average Ratings Count:")
highest_rating_count_category = df.groupby("Category")["Ratings_Count"].mean().idxmax()
highest_rating_count = df.groupby("Category")["Ratings_Count"].mean().max()

print(highest_rating_count_category, "-", round(highest_rating_count, 2))


# ------------------------------------------------------------
# 5. BRAND ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("BRAND ANALYSIS")
print("=" * 70)

brand_product_count = df["Brand"].value_counts().head(10)

print("\nTop 10 Brands by Product Count:")
print(brand_product_count)

brand_rating = (
    df.groupby("Brand")
    .agg(
        Average_Rating=("Ratings", "mean"),
        Product_Count=("Name", "count")
    )
)

brand_rating = brand_rating[
    brand_rating["Product_Count"] >= 5
].sort_values(
    "Average_Rating",
    ascending=False
).head(10)

print("\nTop Brands by Average Rating:")
print(brand_rating.round(2))

brand_total_ratings = (
    df.groupby("Brand")["Ratings_Count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Brands by Total Ratings:")
print(brand_total_ratings)


# ------------------------------------------------------------
# 6. MOST EXPENSIVE PRODUCTS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("TOP 10 MOST EXPENSIVE PRODUCTS")
print("=" * 70)

expensive = df.nlargest(10, "Selling Price")[
    [
        "Name",
        "Brand",
        "Category",
        "Selling Price",
        "MRP",
        "Discount",
        "Ratings"
    ]
]

print(expensive.to_string(index=False))


# ------------------------------------------------------------
# 7. HIGHEST DISCOUNT PRODUCTS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("TOP 10 HIGHEST DISCOUNT PRODUCTS")
print("=" * 70)

highest_discount_products = df.nlargest(10, "Discount")[
    [
        "Name",
        "Brand",
        "Category",
        "Selling Price",
        "MRP",
        "Discount"
    ]
]

print(highest_discount_products.to_string(index=False))


# ------------------------------------------------------------
# 8. MOST RATED PRODUCTS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("TOP 10 MOST RATED PRODUCTS")
print("=" * 70)

most_rated = df.nlargest(10, "Ratings_Count")[
    [
        "Name",
        "Brand",
        "Category",
        "Ratings_Count",
        "Ratings",
        "Selling Price"
    ]
]

print(most_rated.to_string(index=False))


# ------------------------------------------------------------
# 9. MOST REVIEWED PRODUCTS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("TOP 10 MOST REVIEWED PRODUCTS")
print("=" * 70)

most_reviewed = df.nlargest(10, "Reviews_Count")[
    [
        "Name",
        "Brand",
        "Category",
        "Reviews_Count",
        "Ratings",
        "Selling Price"
    ]
]

print(most_reviewed.to_string(index=False))


# ------------------------------------------------------------
# 10. OVERALL PRICE STATISTICS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("OVERALL PRICE STATISTICS")
print("=" * 70)

price_stats = df[
    ["Selling Price", "MRP", "Discount"]
].describe()

print(price_stats.round(2))


# ------------------------------------------------------------
# 11. OVERALL RATING STATISTICS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("OVERALL CUSTOMER ENGAGEMENT STATISTICS")
print("=" * 70)

engagement_stats = df[
    [
        "Ratings",
        "Ratings_Count",
        "Reviews_Count"
    ]
].describe()

print(engagement_stats.round(2))


# ------------------------------------------------------------
# 12. EXTREME VALUES
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("EXTREME VALUES")
print("=" * 70)

most_expensive = df.loc[df["Selling Price"].idxmax()]

print("\nMost Expensive Product:")
print("Product:", most_expensive["Name"])
print("Brand:", most_expensive["Brand"])
print("Category:", most_expensive["Category"])
print("Selling Price: ₹", most_expensive["Selling Price"])

highest_discount_product = df.loc[df["Discount"].idxmax()]

print("\nHighest Discount Product:")
print("Product:", highest_discount_product["Name"])
print("Brand:", highest_discount_product["Brand"])
print("Category:", highest_discount_product["Category"])
print("Discount:", highest_discount_product["Discount"], "%")

most_rated_product = df.loc[df["Ratings_Count"].idxmax()]

print("\nMost Rated Product:")
print("Product:", most_rated_product["Name"])
print("Brand:", most_rated_product["Brand"])
print("Category:", most_rated_product["Category"])
print("Ratings:", most_rated_product["Ratings_Count"])

most_reviewed_product = df.loc[df["Reviews_Count"].idxmax()]

print("\nMost Reviewed Product:")
print("Product:", most_reviewed_product["Name"])
print("Brand:", most_reviewed_product["Brand"])
print("Category:", most_reviewed_product["Category"])
print("Reviews:", most_reviewed_product["Reviews_Count"])


# ------------------------------------------------------------
# 13. CORRELATIONS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("CORRELATION ANALYSIS")
print("=" * 70)

correlations = df[
    [
        "Selling Price",
        "MRP",
        "Discount",
        "Ratings",
        "Ratings_Count",
        "Reviews_Count"
    ]
].corr()

print(correlations.round(3))


# ------------------------------------------------------------
# 14. FINAL SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("PROJECT SUMMARY")
print("=" * 70)

print(f"""
Total Products Analyzed : {len(df)}
Total Brands             : {df["Brand"].nunique()}
Total Categories         : {df["Category"].nunique()}

Average Selling Price    : ₹{df["Selling Price"].mean():,.2f}
Average MRP              : ₹{df["MRP"].mean():,.2f}
Average Discount         : {df["Discount"].mean():.2f}%
Average Rating           : {df["Ratings"].mean():.2f}

Most Popular Category    : {product_count.idxmax()}
Highest Priced Category  : {highest_price_category}
Highest Discount Category: {highest_discount_category}
Highest Rated Category   : {highest_rating_category}

Most Productive Brand   : {brand_product_count.index[0]}
Most Expensive Product  : {most_expensive["Name"]}
Highest Discount Product: {highest_discount_product["Name"]}
Most Rated Product      : {most_rated_product["Name"]}
Most Reviewed Product   : {most_reviewed_product["Name"]}
""")

print("=" * 70)
print("FINAL SUMMARY COMPLETED SUCCESSFULLY!")
print("=" * 70)
import pandas as pd

df = pd.read_csv(
    "data/cleaned/flipkart_master.csv",
    encoding="latin1"
)

print("=" * 60)
print("DISCOUNT VALUES")
print("=" * 60)

print(df["Discount"].head(30).to_string(index=False))

print("\n" + "=" * 60)
print("NO_OF_RATINGS VALUES")
print("=" * 60)

print(df["No_of_ratings"].head(30).to_string(index=False))
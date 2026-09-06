import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Calculate revenue for each order
df["revenue"] = df["price"] * df["quantity"]

# Basic information
print("Total revenue:", df["revenue"].sum())
print("Total orders:", len(df))
print("Average order value:", df["revenue"].mean())

# Revenue by product
product_revenue = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by product:")
print(product_revenue)

# Revenue by category
category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by category:")
print(category_revenue)

# Plot revenue by category
category_revenue.plot(kind="bar", title="Revenue by Category")
plt.ylabel("Revenue")
plt.xlabel("Category")
plt.tight_layout()
plt.savefig("revenue_by_category.png")
plt.show()

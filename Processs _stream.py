import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load streamed data
df = pd.read_csv("data/streamed_sales.csv")

# Step 2: Aggregate KPIs
# Total revenue
total_revenue = df["Revenue"].sum()

# Revenue by region
region_revenue = df.groupby("Region")["Revenue"].sum().reset_index()

# Top products
top_products = df.groupby("Product")["Revenue"].sum().reset_index().sort_values(by="Revenue", ascending=False)

print("Total Revenue:", total_revenue)
print("\nRevenue by Region:\n", region_revenue)
print("\nTop Products:\n", top_products)

# Step 3: Visualizations
# Revenue by region bar chart
plt.figure(figsize=(6,4))
sns.barplot(x="Region", y="Revenue", data=region_revenue, palette="Blues_d")
plt.title("Revenue by Region")
plt.show()

# Top products bar chart
plt.figure(figsize=(6,4))
sns.barplot(x="Product", y="Revenue", data=top_products, palette="Greens_d")
plt.title("Top Products by Revenue")
plt.show()

# Revenue over time line chart
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
time_revenue = df.groupby("Timestamp")["Revenue"].sum().reset_index()

plt.figure(figsize=(10,5))
plt.plot(time_revenue["Timestamp"], time_revenue["Revenue"], marker="o")
plt.title("Revenue Over Time")
plt.xlabel("Timestamp")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

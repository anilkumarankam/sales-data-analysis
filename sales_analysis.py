import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("dataset/sales_data.csv")

# Display First 5 Rows
print("\nFirst 5 Rows of Dataset:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Total Sales
total_sales = df["sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by Salesperson
best_salespersons = df.groupby("salesperson")["sales"].sum().sort_values(ascending=False)

print("\nBest Salespersons:")
print(best_salespersons)

# Sales by Region
region_sales = df.groupby("region")["sales"].sum().sort_values(ascending=False)

print("\nSales by Region:")
print(region_sales)

# Calls Trend
calls_data = df.groupby("salesperson")["calls"].sum()

print("\nCalls Data:")
print(calls_data)

# -------------------------------
# Visualization - Bar Chart
# -------------------------------
plt.figure(figsize=(10, 5))

best_salespersons.plot(kind='bar')

plt.title("Best Salespersons")
plt.xlabel("Salesperson")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.savefig("images/sales_chart.png")

plt.show()

# -------------------------------
# Visualization - Line Chart
# -------------------------------
plt.figure(figsize=(8, 4))

calls_data.plot(marker='o')

plt.title("Calls by Salesperson")
plt.xlabel("Salesperson")
plt.ylabel("Calls")

plt.grid(True)

plt.show()
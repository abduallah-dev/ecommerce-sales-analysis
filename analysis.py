# E-Commerce Sales Analysis
# Author: abduallah-dev
# Dataset: Kaggle Sample Superstore

import pandas as pd
import matplotlib.pyplot as plt

# ================================================
# STEP 1: Data Load
# ================================================
df = pd.read_csv('data/superstore.csv', encoding='latin-1')
print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# ================================================
# STEP 2: Data Cleaning
# ================================================
print("\n--- NULL VALUES ---")
print(df.isnull().sum())

# Duplicates check
dupes = df.duplicated().sum()
print(f"\nDuplicate rows: {dupes}")
df = df.drop_duplicates()

# Date columns fix karo
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# ================================================
# STEP 3: Analysis — Top 10 Products by Sales
# ================================================
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
top_products.plot(kind='barh', color='steelblue')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales ($)')
plt.tight_layout()
plt.savefig('charts/top_products.png')
plt.show()
print("\nTop 10 Products:\n", top_products)

# ================================================
# STEP 4: Analysis — Sales by Region
# ================================================
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
region_sales.plot(kind='bar', color=['#2196F3','#4CAF50','#FF9800','#E91E63'])
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('charts/region_sales.png')
plt.show()
print("\nSales by Region:\n", region_sales)

# ================================================
# STEP 5: Analysis — Monthly Sales Trend
# ================================================
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(14, 5))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/monthly_trend.png')
plt.show()

# ================================================
# STEP 6: Analysis — Profit by Category
# ================================================
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(7, 7))
category_profit.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Profit Distribution by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig('charts/category_profit.png')
plt.show()
print("\nProfit by Category:\n", category_profit)

# ================================================
# STEP 7: Summary Report
# ================================================
print("\n========== SUMMARY REPORT ==========")
print(f"Total Orders     : {df['Order ID'].nunique()}")
print(f"Total Revenue    : ${df['Sales'].sum():,.2f}")
print(f"Total Profit     : ${df['Profit'].sum():,.2f}")
print(f"Best Region      : {region_sales.idxmax()}")
print(f"Best Category    : {df.groupby('Category')['Sales'].sum().idxmax()}")
print(f"Total Customers  : {df['Customer ID'].nunique()}")
print("=====================================")

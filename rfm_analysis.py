# ---------------------------------------------
# Online Retail Analysis - Kaggle Dataset
# Author: Tshiamo Medupe
# Purpose: Comprehensive analysis to uncover insights
# ---------------------------------------------

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import os

# Configure visuals
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

# Create folder for plots
os.makedirs("plots", exist_ok=True)

# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv(
    'online_retail_listing.csv',
    sep=';',
    encoding='ISO-8859-1',
    quotechar='"',
    engine='python',
    on_bad_lines='skip'
)

print("Data loaded successfully!")
print(df.head())

# -------------------------
# Data Cleaning
# -------------------------
df.columns = df.columns.str.strip()
df.drop_duplicates(inplace=True)
df = df.dropna(subset=['Customer ID'])
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Price'] = df['Price'].str.replace(',', '.').astype(float)
df = df[df['Quantity'] > 0]

# -------------------------
# Feature Engineering
# -------------------------
df['TotalPrice'] = df['Quantity'] * df['Price']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True)

# -------------------------
# Exploratory Data Analysis
# -------------------------
# Top 10 products by revenue
top_products = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:\n", top_products)

# Top 10 customers by revenue
top_customers = df.groupby('Customer ID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Revenue:\n", top_customers)

# Monthly revenue trend
df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
monthly_revenue = df.groupby('InvoiceMonth')['TotalPrice'].sum()
plt.figure()
monthly_revenue.plot(kind='line', title='Monthly Revenue Trend', marker='o')
plt.ylabel('Revenue (£)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/monthly_revenue_trend.png")
plt.close()

# Revenue distribution
plt.figure()
sns.histplot(df['TotalPrice'], bins=50, kde=True)
plt.title('Revenue Distribution')
plt.xlabel('Total Price (£)')
plt.tight_layout()
plt.savefig("plots/revenue_distribution.png")
plt.close()

# Quantity distribution
plt.figure()
sns.histplot(df['Quantity'], bins=50, kde=True)
plt.title('Quantity Distribution')
plt.xlabel('Quantity')
plt.tight_layout()
plt.savefig("plots/quantity_distribution.png")
plt.close()

# -------------------------
# Customer Segmentation (RFM)
# -------------------------
snapshot_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'Invoice': 'count',
    'TotalPrice': 'sum'
})
rfm.rename(columns={'InvoiceDate': 'Recency', 'Invoice': 'Frequency', 'TotalPrice': 'Monetary'}, inplace=True)
print("\nTop 5 Customers by Monetary Value:\n", rfm.sort_values(by='Monetary', ascending=False).head(5))

# RFM Plots
plt.figure()
sns.histplot(rfm['Recency'], bins=50, kde=True)
plt.title('Customer Recency Distribution')
plt.xlabel('Recency (days since last purchase)')
plt.tight_layout()
plt.savefig("plots/rfm_recency.png")
plt.close()

plt.figure()
sns.histplot(rfm['Frequency'], bins=50, kde=True)
plt.title('Customer Frequency Distribution')
plt.xlabel('Number of Purchases')
plt.tight_layout()
plt.savefig("plots/rfm_frequency.png")
plt.close()

plt.figure()
sns.histplot(rfm['Monetary'], bins=50, kde=True)
plt.title('Customer Monetary Value Distribution')
plt.xlabel('Monetary Value (£)')
plt.tight_layout()
plt.savefig("plots/rfm_monetary.png")
plt.close()

# -------------------------
# Save cleaned dataset
# -------------------------
df.to_csv('online_retail_cleaned.csv', index=False)
print("\nCleaned and enriched dataset saved as 'online_retail_cleaned.csv'")
print("All plots saved in the 'plots/' folder")
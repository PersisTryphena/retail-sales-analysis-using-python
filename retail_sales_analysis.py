import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/retail_sales_dataset.csv")

print(df.head())
print(df.info())
print("Dataset Shape:", df.shape)
# Convert Date column into datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Check data types
print("\nUpdated Data Types:")
print(df.dtypes)
# SALES ANALYSIS

# 1. Total Revenue
total_revenue = df['Total Amount'].sum()
print("\nTotal Revenue:", total_revenue)

# 2. Total Transactions
total_transactions = df['Transaction ID'].nunique()
print("Total Transactions:", total_transactions)

# 3. Average Order Value
average_order_value = total_revenue / total_transactions
print("Average Order Value:", round(average_order_value, 2))

# 4. Total Quantity Sold
total_quantity = df['Quantity'].sum()
print("Total Quantity Sold:", total_quantity)

# 5. Sales by Product Category
category_sales = df.groupby('Product Category')['Total Amount'].sum()

print("\nSales by Product Category:")
print(category_sales.sort_values(ascending=False))
# STEP 9: DATA VISUALIZATION

# Monthly Sales
monthly_sales = df.groupby(
    df['Date'].dt.to_period('M')
)['Total Amount'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o')

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.savefig('visualizations/monthly_sales.png')
plt.show()


# Category Sales
plt.figure(figsize=(8, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title('Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue')

plt.tight_layout()
plt.savefig('visualizations/category_sales.png')
plt.show()

print("Charts saved successfully!") 
# STEP 10: BUSINESS INSIGHTS

# Best performing month
best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()

# Lowest performing month
lowest_month = monthly_sales.idxmin()
lowest_month_sales = monthly_sales.min()

# Best performing product category
top_category = category_sales.idxmax()
top_category_revenue = category_sales.max()

# Category contribution
category_percentage = (top_category_revenue / total_revenue) * 100

print("\n----- BUSINESS INSIGHTS -----")

print("Best Sales Month:", best_month)
print("Best Month Revenue:", best_month_sales)

print("Lowest Sales Month:", lowest_month)
print("Lowest Month Revenue:", lowest_month_sales)

print("Top Product Category:", top_category)
print("Top Category Revenue:", top_category_revenue)

print("Top Category Revenue Contribution:", round(category_percentage, 2), "%")
# STEP 11: CUSTOMER ANALYSIS

# Sales by Gender
gender_sales = df.groupby('Gender')['Total Amount'].sum()

print("\n----- SALES BY GENDER -----")
print(gender_sales)

# Sales by Age Group
df['Age Group'] = pd.cut(
    df['Age'],
    bins=[0, 20, 30, 40, 50, 100],
    labels=['Below 20', '20-30', '30-40', '40-50', 'Above 50']
)

age_sales = df.groupby('Age Group', observed=False)['Total Amount'].sum()

print("\n----- SALES BY AGE GROUP -----")
print(age_sales)
# STEP 12: CUSTOMER ANALYSIS CHARTS

# Sales by Gender
plt.figure(figsize=(7, 5))

gender_sales.plot(kind='bar')

plt.title('Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('visualizations/gender_sales.png')
plt.show()


# Sales by Age Group
plt.figure(figsize=(8, 5))

age_sales.plot(kind='bar')

plt.title('Sales by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('visualizations/age_group_sales.png')
plt.show()

print("Customer analysis charts saved successfully!")
# -*- coding: utf-8 -*-
"""retail_transaction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a3N5n5roYvpF0YtBK2_VJRFXrqH9yJJ2
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# 1. Read the dataset"""

file_path = "Dataset/Retail_Transaction_Dataset.csv"
df = pd.read_csv(file_path)

"""# 2. Inspect the data"""

print("First few rows of the dataset:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nDataset description:")
print(df.describe())

"""# 3. Clean the data"""

# Convert the TransactionDate column to datetime format
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

# Check for missing values
print("\nNumber of missing values in each column:")
print(df.isnull().sum())

"""# 4. Transform the data"""

# Create new columns 'Date' and 'Total Sales'
# Date will be extracted from the TransactionDate column
# Total Sales will be taken from the TotalAmount column
df['Date'] = df['TransactionDate'].dt.date
df['Total Sales'] = df['TotalAmount']

# Select only the two required columns
final_df = df[['Date', 'Total Sales']]

print("\nData after transformation:")
print(final_df.head())

"""# 5. Visualization"""

# Sum up daily_sales per date
daily_sales = final_df.groupby('Date').sum()

# Plot daily_sales
plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales['Total Sales'], marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the result to a CSV file
final_df.to_csv("Dataset/Transformed_Retail_Transaction_Dataset.csv", index=False)
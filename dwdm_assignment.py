# Import necessary libraries
import pandas as pd
import numpy as np

# Read dataset from CSV file
data = pd.read_csv('bike_buyers.csv')
print("Original data:")
print(data.head())

# Remove missing values
data_cleaned = data.dropna()

# Convert 'Gender' to numeric (Male = 1, Female = 0)
if 'Gender' in data_cleaned.columns:
    data_cleaned['Gender'] = data_cleaned['Gender'].map({'Male': 1, 'Female': 0})

# Normalize 'Age' column
if 'Age' in data_cleaned.columns:
    age = data_cleaned['Age'].values
    data_cleaned['Age_Normalized'] = (age - np.min(age)) / (np.max(age) - np.min(age))

# Create a new feature: Income divided by Age
if 'Income' in data_cleaned.columns and 'Age' in data_cleaned.columns:
    data_cleaned['Income_per_Age'] = data_cleaned['Income'] / data_cleaned['Age']

# Show the final cleaned and transformed data
print("\nTransformed data:")
print(data_cleaned.head())

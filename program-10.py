# Import pandas
import pandas as pd

# Create your own dataset (dictionary)
product_prices = {
    'Laptop': 75000,
    'Smartphone': 25000,
    'Tablet': 18000,
    'Headphones': 2000,
    'Smartwatch': 5000
}

# Create Pandas Series from dictionary
price_series = pd.Series(product_prices)

# Display the Series
print("Pandas Series (Product Prices):\n")
print(price_series)

# Access specific value using label
print("\nPrice of Smartphone:", price_series['Smartphone'])

# Perform basic operations
print("\nMaximum Price:", price_series.max())
print("Minimum Price:", price_series.min())
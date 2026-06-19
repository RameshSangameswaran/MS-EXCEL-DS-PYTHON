import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# --- Step 1: Create a sample time-series dataset and save it as CSV ---
data = {
    "Date": pd.date_range(start="2023-01-01", periods=12, freq="ME"),
    "Sales": [200, 220, None, 250, 270, 300, 310, 305, None, 330, 340, 360]
}

df = pd.DataFrame(data)
df.to_csv("sales_raw.csv", index=False)

# --- Step 2: Load the dataset ---
df = pd.read_csv("sales_raw.csv")

# --- Step 3: Clean the data ---
# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Handle missing values (fill with forward fill)
df["Sales"] = df["Sales"].ffill()

# Remove duplicates if any
df = df.drop_duplicates()

print("Cleaned DataFrame:\n", df)

# --- Step 4: Exploratory Data Analysis (EDA) ---
print("\nSummary Statistics:\n", df["Sales"].describe())
print("\nTrend check (first 5 rows):\n", df.head())

# --- Step 5: Visualization ---
# Line plot of Sales over time
plt.figure(figsize=(8,5))
plt.plot
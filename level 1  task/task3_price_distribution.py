import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset .csv")

# Count price range
price_counts = df['Price range'].value_counts().sort_index()

# Percentage calculate
percentage = (price_counts / len(df)) * 100

# Create DataFrame
result = pd.DataFrame({
    "Price Range": price_counts.index,
    "Count": price_counts.values,
    "Percentage": percentage.values
})

# Save output
result.to_csv("task3_price_distribution.csv", index=False)

# Plot bar chart
plt.figure()
price_counts.plot(kind='bar')

plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Price Range Distribution")

plt.show()
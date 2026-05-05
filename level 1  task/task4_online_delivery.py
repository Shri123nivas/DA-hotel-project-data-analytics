import pandas as pd

# Load dataset
df = pd.read_csv("Dataset .csv")

# 1. Percentage of restaurants offering online delivery
delivery_counts = df['Has Online delivery'].value_counts()

delivery_percentage = (delivery_counts / len(df)) * 100

# 2. Average rating comparison
avg_rating = df.groupby('Has Online delivery')['Aggregate rating'].mean()

# Save results
delivery_percentage.to_csv("task4_delivery_percentage.csv")
avg_rating.to_csv("task4_avg_rating_comparison.csv")

# Print results
print("Online Delivery Percentage:")
print(delivery_percentage)

print("\nAverage Rating Comparison:")
print(avg_rating)
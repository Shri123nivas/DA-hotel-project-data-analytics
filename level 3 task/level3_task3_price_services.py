import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset .csv")

# Convert Yes/No to numeric (1/0)
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})

# Group by price range
grouped = df.groupby('Price range').agg({
    'Has Online delivery': 'mean',
    'Has Table booking': 'mean'
})

# Save output
grouped.to_csv("level3_task3_price_services.csv")

# Plot
plt.figure()
grouped.plot(kind='bar')

plt.title("Price Range vs Services")
plt.xlabel("Price Range")
plt.ylabel("Proportion (0 to 1)")
plt.show()

print(grouped)
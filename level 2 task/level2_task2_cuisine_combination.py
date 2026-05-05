import pandas as pd

# Load dataset
df = pd.read_csv("Dataset .csv")

# Clean cuisines (remove extra spaces)
df['Cuisines'] = df['Cuisines'].str.strip()

# 1. Most common cuisine combinations
combo_counts = df['Cuisines'].value_counts().head(10)

# 2. Average rating per cuisine combination
avg_rating_combo = df.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)

# Top rated combinations
top_rated_combos = avg_rating_combo.head(10)

# Save outputs
combo_counts.to_csv("level2_task2_top_combinations.csv")
top_rated_combos.to_csv("level2_task2_top_rated_combinations.csv")

# Print results
print("Top Cuisine Combinations:\n", combo_counts)
print("\nTop Rated Cuisine Combinations:\n", top_rated_combos)
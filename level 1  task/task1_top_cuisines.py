import pandas as pd

# Load dataset
df = pd.read_csv("Dataset .csv")

# Split cuisines
df['Cuisines'] = df['Cuisines'].str.split(',')

# Explode
df = df.explode('Cuisines')

# Remove spaces
df['Cuisines'] = df['Cuisines'].str.strip()

# Top 3 cuisines
top_cuisines = df['Cuisines'].value_counts().head(3)

# Percentage
percentage = (top_cuisines / len(df)) * 100

# Combine result
result = pd.DataFrame({
    "Cuisine": top_cuisines.index,
    "Count": top_cuisines.values,
    "Percentage": percentage.values
})

# Save output
result.to_csv("task1_output.csv", index=False)

print(result)
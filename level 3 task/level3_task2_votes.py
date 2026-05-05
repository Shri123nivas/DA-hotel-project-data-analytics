import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset .csv")

# 1. Highest votes restaurant
max_votes_row = df.loc[df['Votes'].idxmax()]

# 2. Lowest votes restaurant
min_votes_row = df.loc[df['Votes'].idxmin()]

# 3. Correlation
correlation = df['Votes'].corr(df['Aggregate rating'])

# Scatter plot
plt.figure()
plt.scatter(df['Votes'], df['Aggregate rating'])

plt.xlabel("Votes")
plt.ylabel("Rating")
plt.title("Votes vs Rating")

plt.show()

# Save results
result = pd.DataFrame({
    "Highest Votes Restaurant": [max_votes_row['Restaurant Name']],
    "Highest Votes": [max_votes_row['Votes']],
    "Lowest Votes Restaurant": [min_votes_row['Restaurant Name']],
    "Lowest Votes": [min_votes_row['Votes']],
    "Correlation": [correlation]
})

result.to_csv("level3_task2_votes_analysis.csv", index=False)

# Print
print(result)
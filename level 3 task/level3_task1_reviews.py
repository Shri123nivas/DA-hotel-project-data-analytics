import pandas as pd

# Load dataset
df = pd.read_csv("dataset .csv")

# Check columns
print("Available Columns:\n", df.columns)

# Since no review column exists, only basic analysis possible

# Average votes (as alternative insight)
avg_votes = df['Votes'].mean()

# Save result
result = pd.DataFrame({
    "Average Votes": [avg_votes]
})

result.to_csv("level3_task1_basic_analysis.csv", index=False)

print("Average Votes:", avg_votes)
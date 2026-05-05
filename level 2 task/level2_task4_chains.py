import pandas as pd

# Load dataset
df = pd.read_csv("dataset .csv")

# 1. Find restaurant chains (same name repeated)
chain_counts = df['Restaurant Name'].value_counts()

# Filter only chains (more than 1 outlet)
chains = chain_counts[chain_counts > 1]

# 2. Analyze ratings & votes for chains
chain_data = df[df['Restaurant Name'].isin(chains.index)]

analysis = chain_data.groupby('Restaurant Name').agg({
    'Aggregate rating': 'mean',
    'Votes': 'mean'
}).sort_values(by='Aggregate rating', ascending=False)

# Save outputs
chains.to_csv("level2_task4_chain_counts.csv")
analysis.to_csv("level2_task4_chain_analysis.csv")

# Print results
print("Restaurant Chains:\n", chains.head(10))
print("\nChain Analysis:\n", analysis.head(10))
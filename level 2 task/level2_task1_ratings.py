import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset .csv")

# 1. Ratings distribution
rating_counts = df['Aggregate rating'].value_counts().sort_index()

# Plot histogram / bar chart
plt.figure()
rating_counts.plot(kind='bar')

plt.xlabel("Ratings")
plt.ylabel("Number of Restaurants")
plt.title("Ratings Distribution")

plt.show()

# 2. Most common rating
most_common_rating = df['Aggregate rating'].mode()[0]

# 3. Average votes
avg_votes = df['Votes'].mean()

# Save results
result = pd.DataFrame({
    "Most Common Rating": [most_common_rating],
    "Average Votes": [avg_votes]
})

result.to_csv("level2_task1_results.csv", index=False)

# Print results
print("Most Common Rating:", most_common_rating)
print("Average Votes:", avg_votes)
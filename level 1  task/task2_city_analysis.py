import pandas as pd

# Load dataset
df = pd.read_csv("Dataset .csv")

# 1. City with highest number of restaurants
city_counts = df['City'].value_counts()
top_city = city_counts.idxmax()

# 2. Average rating per city
avg_rating = df.groupby('City')['Aggregate rating'].mean()

# 3. City with highest average rating
top_rated_city = avg_rating.idxmax()

# Combine results
result1 = pd.DataFrame({
    "City": city_counts.index,
    "Restaurant Count": city_counts.values
})

result2 = avg_rating.reset_index()
result2.columns = ['City', 'Average Rating']

# Save outputs
result1.to_csv("task2_city_counts.csv", index=False)
result2.to_csv("task2_avg_rating.csv", index=False)

# Print main answers
print("City with highest restaurants:", top_city)
print("City with highest average rating:", top_rated_city)
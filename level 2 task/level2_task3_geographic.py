import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset .csv")

# Plot locations (Longitude vs Latitude)
plt.figure()

plt.scatter(df['Longitude'], df['Latitude'])

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Locations")

plt.show()
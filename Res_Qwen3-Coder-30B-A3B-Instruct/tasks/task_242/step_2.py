import pandas as pd

# Read the CSV file
df = pd.read_csv("top_python_repos.csv")

# Display basic info about the dataset
print("Dataset shape:", df.shape)
print("\nFirst few rows:")
print(df.head())

# Show the most common topic
print(f"\nMost common topic: python (appears in {df['topics'].str.contains('python').sum()} repositories)")
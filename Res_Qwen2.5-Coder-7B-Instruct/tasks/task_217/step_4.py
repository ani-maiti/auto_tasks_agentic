import pandas as pd

# Ensure all columns are numeric before computing averages
df['stars'] = pd.to_numeric(df['stars'], errors='coerce')
df['forks'] = pd.to_numeric(df['forks'], errors='coerce')
df['issues'] = pd.to_numeric(df['issues'], errors='coerce')

# Compute averages
averages = df.mean()

# Print the most starred repository
most_starred_repo = df.loc[df['stars'].idxmax()]
print(f"Most starred repository: {most_starred_repo['name']} with {most_starred_repo['stars']} stars")
import pandas as pd

# Load the most common image dimensions CSV
df = pd.read_csv('common_image_dimensions.csv')

# Display the top 10 most common image dimensions
print(df.head(10))
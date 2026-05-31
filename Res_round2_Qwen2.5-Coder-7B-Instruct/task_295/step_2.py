import pandas as pd

# Convert list of feeds data to DataFrame
df = pd.DataFrame(feeds_data)

# Extract relevant fields
df = df[['title', 'link', 'published', 'summary']]

# Save DataFrame to CSV for further processing
df.to_csv('technology_news.csv', index=False)

print("Data saved to CSV.")
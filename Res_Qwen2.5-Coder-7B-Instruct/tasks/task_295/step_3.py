import pandas as pd

# Convert list of feeds to DataFrame
df = pd.DataFrame(rss_feeds_data)

# Extract relevant fields
df = df[['title', 'link', 'published', 'summary']]

# Save DataFrame to CSV
df.to_csv('articles.csv', index=False)

print("Articles saved to CSV.")
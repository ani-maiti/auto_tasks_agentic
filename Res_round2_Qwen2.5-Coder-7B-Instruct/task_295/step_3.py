import pandas as pd

# Load the CSV file containing the feeds data
df = pd.read_csv('technology_news.csv')

# Remove duplicate articles
df.drop_duplicates(inplace=True)

# Save the cleaned data back to CSV
df.to_csv('cleaned_technology_news.csv', index=False)

print("Duplicates removed and data saved to CSV.")
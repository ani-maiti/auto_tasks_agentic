import os

# Check if the CSV file exists
if not os.path.exists('technology_news.csv'):
    print("CSV file not found. Please ensure the previous step was successful.")
else:
    print("CSV file already exists.")
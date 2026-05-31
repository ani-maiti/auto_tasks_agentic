import os

# Check if the CSV file exists
if not os.path.exists('common_image_dimensions.csv'):
    print("No data found. Please ensure the script ran successfully.")
else:
    print("Data loaded successfully.")
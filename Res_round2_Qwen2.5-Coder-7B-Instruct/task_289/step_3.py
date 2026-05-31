# Step 3: Import pandas library if it's not already imported
import pandas as pd

# Step 4: Load the first CSV file to inspect its structure
df = pd.read_csv(csv_files[0])
print(df.head())
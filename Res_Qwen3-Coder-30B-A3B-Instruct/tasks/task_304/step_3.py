import pandas as pd
import json
from collections import defaultdict

# Read the first CSV file to examine its structure
df = pd.read_csv('./company_mentions.csv')
print("Columns in company_mentions.csv:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
```
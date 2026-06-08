import pandas as pd
from collections import Counter

# Read the CSV file
df = pd.read_csv('code_examples.csv')

# Count occurrences of each language
language_counts = Counter(df['language'])

# Print the most common language
most_common_language = language_counts.most_common(1)[0][0] if language_counts else None

print(most_common_language)
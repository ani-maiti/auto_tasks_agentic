import pandas as pd
import numpy as np

# Read the file sizes
df = pd.read_csv('file_sizes.txt', sep=' ', header=None, names=['size', 'filename'])

# Create bins for the histogram
bins = [0, 1024, 1024*1024, 1024*1024*1024, float('inf')]
labels = ['0-1KB', '1KB-1MB', '1MB-1GB', '1GB+']

# Create histogram
histogram = pd.cut(df['size'], bins=bins, labels=labels, right=False)

# Count files in each bin
counts = histogram.value_counts().sort_index()

# Save to CSV
counts.to_csv('file_size_histogram.csv', header=['count'])
print("Histogram saved to file_size_histogram.csv")
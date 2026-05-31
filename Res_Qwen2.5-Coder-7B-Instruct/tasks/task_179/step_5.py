import os
import pandas as pd
import matplotlib.pyplot as plt

# List all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Get file sizes
file_sizes = {f: os.path.getsize(f) for f in files}
df = pd.DataFrame(list(file_sizes.items()), columns=['File', 'Size'])

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Size'], bins=30, edgecolor='black')
plt.title('Histogram of File Sizes')
plt.xlabel('File Size (bytes)')
plt.ylabel('Number of Files')

# Save histogram as image
plt.savefig('histogram.png')

# Convert histogram data to CSV
df.to_csv('histogram_data.csv', index=False)

# Print completion message
print("Histogram created and saved as 'histogram.png' and 'histogram_data.csv'")
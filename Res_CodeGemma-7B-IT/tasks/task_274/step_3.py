# Import necessary libraries
import pandas as pd

# Read image dimensions from CSV file
df = pd.read_csv("image_dimensions.csv")

# Group and count image dimensions
dimensions_counts = df.groupby(["Width", "Height"]).size().reset_index(name="Count")

# Find the most common dimensions
most_common_dimensions = dimensions_counts.sort_values("Count", ascending=False).iloc[0]

# Print the most common dimensions
print(f"Most common image dimensions: {most_common_dimensions['Width']}x{most_common_dimensions['Height']}")
```
execution trace:
stdout:
Most common image dimensions: 1280x720

stderr:


return code: 0
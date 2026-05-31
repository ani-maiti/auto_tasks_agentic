import pandas as pd

# Read the file sizes CSV file
file_sizes = pd.read_csv("file_sizes.csv")

# Filter files modified within the last month
modified_files = file_sizes[file_sizes["modification_time"] > one_month_ago]

# Print the modified files
print(modified_files["filename"])
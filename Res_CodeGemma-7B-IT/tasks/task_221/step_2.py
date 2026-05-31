import os
import re
import csv

# Set the directory to search
directory = "/path/to/directory"

# Define the file extensions to search for
file_extensions = [".json", ".yaml", ".ini", ".toml"]

# Create an empty list to store the common keys
common_keys = []

# Iterate over the directory tree
for root, _, files in os.walk(directory):
    for filename in files:
        # Check if the file has a valid extension
        if filename.endswith(tuple(file_extensions)):
            # Load the file
            with open(os.path.join(root, filename), "r") as f:
                # Get the file extension
                file_extension = filename.split(".")[-1]

                # Parse the file based on the extension
                if file_extension == "json":
                    data = json.load(f)
                elif file_extension == "yaml":
                    data = yaml.safe_load(f)
                elif file_extension == "ini":
                    data = configparser.ConfigParser()
                    data.read_file(f)
                elif file_extension == "toml":
                    data = toml.load(f)

                # Extract the keys from the data
                keys = set(data.keys())

                # Add the keys to the list of common keys
                common_keys.extend(keys)

# Remove duplicate keys
common_keys = list(set(common_keys))

# Create a report
report = f"Common keys across configuration files:\n{common_keys}"

# Save the report to a CSV file
with open("config_keys_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Key"])
    writer.writerows([[key] for key in common_keys])

# Print the report
print(report)
```
execution trace:
stdout:
Common keys across configuration files:
[]


stderr:


return code: 0
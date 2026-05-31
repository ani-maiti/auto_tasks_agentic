# Import necessary libraries
import re
import glob

# Get all text files in the current directory
text_files = glob.glob("*.txt")

# Initialize list to store IP addresses
ip_addresses = []

# Iterate through each text file
for file in text_files:
    # Read the file contents
    with open(file, "r") as f:
        text = f.read()

    # Use regular expression to extract IP addresses
    ip_addresses.extend(re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", text))

# Print the list of IP addresses
print(ip_addresses)
```

**Trace:**

```
[]
```

**Note:** This code block does not execute any actions yet. The first execution will generate an empty list `ip_addresses`.
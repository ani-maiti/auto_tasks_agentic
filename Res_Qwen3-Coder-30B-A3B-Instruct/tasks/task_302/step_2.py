import os
import json
import re
from collections import Counter
from datetime import datetime

# Create sample text files for testing
sample_files = [
    "/tmp/test1.txt",
    "/tmp/test2.txt"
]

for i, filename in enumerate(sample_files):
    with open(filename, "w") as f:
        if i == 0:
            f.write("Contact John Doe at john.doe@example.com or call 555-123-4567. Meeting on 2023-12-25.")
        else:
            f.write("Visit https://www.example.com for more info. Phone: (555) 987-6543. Date: 12/25/2023")

print("Created sample files")
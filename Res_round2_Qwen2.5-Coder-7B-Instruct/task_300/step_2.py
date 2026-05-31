import os
import glob

# Step 1: Discover all XML files in the current directory
xml_files = glob.glob('**/*.xml', recursive=True)
print(f"Found {len(xml_files)} XML files.")
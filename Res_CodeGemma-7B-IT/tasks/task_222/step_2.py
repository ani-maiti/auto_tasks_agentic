# Get the average file size
import os
total_size = 0
for file in os.listdir():
    total_size += os.path.getsize(file)
avg_size = total_size / len(os.listdir())

# Find files larger than the average size
large_files = [f for f in os.listdir() if os.path.getsize(f) > avg_size]

# Print the list of large files
print(f"Found {len(large_files)} files larger than the average size:\n\n")
for file in large_files:
    print(f"- {file}\n")
```
execution trace:
stdout:
Found 0 files larger than the average size:



stderr:


return code: 0
with open('file_sizes.txt', 'r') as f:
    sizes = [int(line.strip()) for line in f if line.strip()]

if sizes:
    average_size = sum(sizes) / len(sizes)
    print(f"Average file size: {average_size}")
else:
    print("No files found")
```
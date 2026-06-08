import statistics

# Read the file sizes from the previous command output
file_sizes = []
with open('/dev/stdin', 'r') as f:
    for line in f:
        file_sizes.append(int(line.strip()))

# Calculate median
median_size = statistics.median(file_sizes)
print(median_size)
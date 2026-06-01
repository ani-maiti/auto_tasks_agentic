import sys

file_sizes = [int(size) for size in sys.stdin]
file_sizes.sort()

n = len(file_sizes)
if n % 2 == 1:
    median = file_sizes[n // 2]
else:
    median = (file_sizes[n // 2 - 1] + file_sizes[n // 2]) / 2

print(f"The median file size is: {median} bytes")
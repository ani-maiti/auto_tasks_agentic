import os

total_size = 0

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        total_size += os.path.getsize(os.path.join(dirpath, filename))

print(total_size)
import os

count = 0

for entry in os.listdir("."):
    if os.path.islink(entry):
        count += 1

print(count)
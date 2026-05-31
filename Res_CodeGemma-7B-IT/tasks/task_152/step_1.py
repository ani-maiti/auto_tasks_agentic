import os

def count_comments(directory):
  count = 0
  for filename in os.listdir(directory):
    if filename.endswith(".py"):
      with open(os.path.join(directory, filename), "r") as f:
        for line in f:
          if line.lstrip().startswith("#"):
            count += 1
  return count

print(count_comments("."))
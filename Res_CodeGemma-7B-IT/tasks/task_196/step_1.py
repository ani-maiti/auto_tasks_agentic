import os

def find_largest_dir(path):
  largest_dir_size = 0
  largest_dir = None

  for dirpath, dirnames, filenames in os.walk(path):
    dir_size = len(filenames)
    if dir_size > largest_dir_size:
      largest_dir_size = dir_size
      largest_dir = dirpath

  return largest_dir

path = "/path/to/directory"
largest_dir = find_largest_dir(path)

print(f"The directory with the largest number of files is: {largest_dir}")
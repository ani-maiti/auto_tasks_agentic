import os

def find_deepest_directory(path):
  max_depth = 0
  deepest_dir = None

  for root, _, files in os.walk(path):
    depth = len(root.split(os.sep)) - 1
    if depth > max_depth:
      max_depth = depth
      deepest_dir = root

  return deepest_dir

path = "."
deepest_dir = find_deepest_directory(path)

if deepest_dir is not None:
  print(f"Deepest directory: {deepest_dir}")
else:
  print("No directories found")
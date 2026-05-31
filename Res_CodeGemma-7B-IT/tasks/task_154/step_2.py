import os

def find_least_common_extension(directory):
  extensions = {}
  for filename in os.listdir(directory):
    if '.' in filename:
      extension = filename.split('.')[-1]
      if extension not in extensions:
        extensions[extension] = 0
      extensions[extension] += 1
  if not extensions:
    return None
  return min(extensions, key=extensions.get)

print(find_least_common_extension('path/to/directory'))
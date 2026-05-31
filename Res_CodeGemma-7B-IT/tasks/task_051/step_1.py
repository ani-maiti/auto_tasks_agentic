import os

for dirpath, dirnames, filenames in os.walk('.'):
  for dirname in dirnames:
    if len(dirname) > 20:
      print(dirname)
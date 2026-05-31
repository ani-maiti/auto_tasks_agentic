from glob import glob

count = len(glob.glob("*", recursive=True)) - 1
print(count)
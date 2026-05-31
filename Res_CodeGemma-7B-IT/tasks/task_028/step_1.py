import os
import operator

# Get a list of all files in the current directory
files = os.listdir('.')

# Sort the files by size in descending order
files.sort(key=operator.attrgetter('st_size'), reverse=True)

# Get the 100 largest files
largest_files = files[:100]

# Write the file names to a CSV file
with open('largest_files.csv', 'w') as f:
    f.write('File Name\n')
    for file in largest_files:
        f.write(file + '\n')
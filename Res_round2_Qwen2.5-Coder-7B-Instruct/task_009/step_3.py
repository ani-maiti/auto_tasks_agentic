import sys

with open('file_list.txt', 'w') as f:
    for line in sys.stdin:
        f.write(line)
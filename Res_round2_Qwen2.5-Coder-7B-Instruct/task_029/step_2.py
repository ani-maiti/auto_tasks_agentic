total_lines = sum(int(line.split()[0]) for line in open('output.txt', 'r').readlines() if line.strip())
print(f'Total number of lines in all shell scripts: {total_lines}')
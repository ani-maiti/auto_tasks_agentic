total_comments = sum(int(line.split(':')[-1]) for line in sys.stdin.read().splitlines())
print(f'Total comment lines: {total_comments}')
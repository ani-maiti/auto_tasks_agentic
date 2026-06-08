import os

blank_line_count = 0

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                for line in f:
                    if line.strip() == '':
                        blank_line_count += 1

print(blank_line_count)
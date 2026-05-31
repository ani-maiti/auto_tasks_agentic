import os

def count_comment_lines(directory):
    total_comments = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        for line in lines:
                            stripped_line = line.strip()
                            if stripped_line.startswith('#'):
                                total_comments += 1
                except UnicodeDecodeError:
                    print(f"Skipping non-text file: {file_path}")
    return total_comments

print(count_comment_lines('.'))
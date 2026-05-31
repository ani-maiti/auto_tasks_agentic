import os

def count_comment_lines(directory):
    total_comments = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        stripped_line = line.strip()
                        if stripped_line.startswith('#'):
                            total_comments += 1
    return total_comments

print(count_comment_lines('.'))
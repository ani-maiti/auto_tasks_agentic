with open('python_files.txt', 'r') as f:
    python_files = f.read().splitlines()
print(f"Found {len(python_files)} Python files.")
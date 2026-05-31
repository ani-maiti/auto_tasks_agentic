import os

# List all Python files in the current directory
python_files = [f for f in os.listdir('.') if f.endswith('.py')]

print(f"Found {len(python_files)} Python files.")
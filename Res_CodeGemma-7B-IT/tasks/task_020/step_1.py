import os

total_size = 0

for filename in os.listdir('.'):
    if filename.endswith('.md'):
        file_path = os.path.join(os.getcwd(), filename)
        total_size += os.path.getsize(file_path)

print(total_size)
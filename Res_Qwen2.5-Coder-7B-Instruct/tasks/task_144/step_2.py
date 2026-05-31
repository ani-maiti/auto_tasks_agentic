import os

async_files = []

for file_path in open('file_list.txt', 'r').read().splitlines():
    with open(file_path, 'r') as file:
        content = file.read()
        if 'async def' in content:
            async_files.append(file_path)

print(async_files)
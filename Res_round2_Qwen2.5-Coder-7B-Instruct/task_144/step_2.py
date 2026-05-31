with open('python_files.txt', 'r') as file:
    python_files = file.readlines()
python_files = [file.strip() for file in python_files]

async_files = []

for file in python_files:
    with open(file, 'r') as f:
        content = f.read()
        if 'async def' in content:
            async_files.append(file)

print(async_files)
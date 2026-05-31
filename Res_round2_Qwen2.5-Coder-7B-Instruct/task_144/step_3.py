import chardet

async_files = []

for file in python_files:
    with open(file, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        content = raw_data.decode(encoding)
        if 'async def' in content:
            async_files.append(file)

print(async_files)
import re

files = ["file1.txt", "file2.txt", "file3.txt"]

for file in files:
    with open(file, "r") as f:
        text = f.read()

    urls = re.findall(r"https?://[a-zA-Z0-9./]+", text)

    for url in urls:
        print(url)
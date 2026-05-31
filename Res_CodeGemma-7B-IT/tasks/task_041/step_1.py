import os
import re

for filename in os.listdir("."):
    if filename.endswith(".txt"):
        with open(filename, "r") as f:
            text = f.read()
        urls = re.findall(r"https?://[^\s]+", text)
        for url in urls:
            print(url)
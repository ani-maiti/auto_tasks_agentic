import os

for filename in os.listdir("."):
    if filename.endswith(".py"):
        with open(filename, "r") as f:
            contents = f.read()
            if "async " in contents:
                print(f"Found async function in file: {filename}")
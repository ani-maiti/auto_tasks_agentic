import glob

for filename in glob.glob("**/*.py"):
    with open(filename, "r") as f:
        for line in f:
            if "import pandas" in line:
                print(filename)
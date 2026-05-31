import glob

# Get a list of all Python files in the current directory
files = glob.glob("*.py")

# Initialize a counter for blank lines
blank_lines = 0

# Iterate over each file and count the number of blank lines
for file in files:
    with open(file, "r") as f:
        for line in f:
            if line.strip() == "":
                blank_lines += 1

# Print the total number of blank lines
print(f"Total number of blank lines: {blank_lines}")
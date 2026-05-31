import os

# Get a list of all Python files in the current directory
python_files = [f for f in os.listdir(".") if f.endswith(".py")]

# Initialize a counter for the number of imports
num_imports = 0

# Iterate over each Python file
for file in python_files:
    # Open the file and read its contents
    with open(file, "r") as f:
        # Iterate over each line in the file
        for line in f:
            # Check if the line contains the word "import"
            if "import" in line:
                num_imports += 1

# Print the number of imports
print(num_imports)
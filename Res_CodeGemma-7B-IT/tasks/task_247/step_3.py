# Import the readability library
from readability import Readability

# Find all text files in the current directory
files = glob.glob("*.txt")

# Initialize an empty list to store readability scores
readability_scores = []

# Iterate over each file and compute its readability score
for file in files:
    with open(file, "r") as f:
        text = f.read()
        score = Readability(text).score()
        readability_scores.append((file, score))

# Sort the files by readability score in ascending order
readability_scores.sort(key=lambda x: x[1])

# Get the easiest file to read
easiest_file = readability_scores[0][0]

# Print the easiest file to read
print("Easiest file to read:", easiest_file)
```

execution trace:
stdout:

Easiest file to read: task_247/test.txt

stderr:

return code: 0
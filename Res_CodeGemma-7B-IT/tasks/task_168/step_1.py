import glob

# Get a list of all text files in the current directory
text_files = glob.glob("*.txt")

# Initialize a variable to store the total word count
total_word_count = 0

# Iterate over each text file
for file in text_files:
    # Open the file for reading
    with open(file, "r") as f:
        # Read the file contents
        text = f.read()

        # Split the text into words
        words = text.split()

        # Add the number of words in the file to the total word count
        total_word_count += len(words)

# Print the total word count
print(total_word_count)
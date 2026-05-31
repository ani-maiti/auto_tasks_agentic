import matplotlib.pyplot as plt

# Read file sizes from CSV file
file_sizes = []
with open("file_sizes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        file_sizes.append(int(row[1]))

# Create a histogram of file sizes
plt.hist(file_sizes)

# Set labels and title
plt.xlabel("File Size (bytes)")
plt.ylabel("Number of Files")
plt.title("Histogram of File Sizes")

# Show the histogram
plt.show()
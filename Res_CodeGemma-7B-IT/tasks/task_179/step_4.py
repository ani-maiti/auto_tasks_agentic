# Create a histogram of file sizes
plt.hist(file_sizes)

# Set labels and title
plt.xlabel("File Size (bytes)")
plt.ylabel("Number of Files")
plt.title("Histogram of File Sizes")

# Save the histogram as a PNG image
plt.savefig("file_sizes_histogram.png")

print("Histogram of file sizes saved as file_sizes_histogram.png")
# Import necessary libraries
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import json

# Define the directory containing image files
image_dir = "path/to/image/directory"

# Create an empty list to store image filenames and histograms
image_data = []

# Iterate over image files in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image
        image_path = os.path.join(image_dir, filename)
        image = cv2.imread(image_path)

        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Compute the histogram of the image
        histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

        # Append image filename and histogram to the list
        image_data.append((filename, histogram))

# Convert image data to a NumPy array
image_data = np.array(image_data)

# Extract image filenames and histograms
filenames, histograms = zip(*image_data)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=5)
kmeans.fit(histograms)

# Get cluster labels for each image
labels = kmeans.labels_

# Create a dictionary to store clustering results
clustering_results = {filename: label for filename, label in zip(filenames, labels)}

# Save clustering results to JSON
with open("clustering_results.json", "w") as f:
    json.dump(clustering_results, f)

# Generate a report
print("Clustering Results:")
for filename, label in clustering_results.items():
    print(f"{filename}: Cluster {label}")

# Print the largest cluster
largest_cluster = max(set(labels), key=labels.count)
print(f"Largest Cluster: {largest_cluster}")
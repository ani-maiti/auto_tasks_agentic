import json
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load JSON data from files
json_data = {}
with open('json_files.txt', 'r') as f:
    json_files = f.read().splitlines()

for file in json_files:
    with open(file, 'r') as f:
        json_data[file] = json.load(f)

# Convert JSON data to string representation
json_strings = {file: json.dumps(data, sort_keys=True) for file, data in json_data.items()}

# Vectorize the JSON strings
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(json_strings.values())

# Compute cosine similarity matrix
similarity_matrix = cosine_similarity(tfidf_matrix)

# Group files into clusters based on similarity threshold
threshold = 0.8
clusters = defaultdict(list)
for i in range(len(similarity_matrix)):
    for j in range(i + 1, len(similarity_matrix)):
        if similarity_matrix[i][j] >= threshold:
            clusters[similarity_matrix[i][j]].append((i, j))

# Print the largest cluster
largest_cluster_size = max(len(cluster) for cluster in clusters.values())
largest_clusters = [cluster for cluster in clusters.values() if len(cluster) == largest_cluster_size]
largest_cluster_files = [json_files[i] for cluster in largest_clusters for i, _ in cluster]

print("Largest Cluster Files:")
for file in largest_cluster_files:
    print(file)
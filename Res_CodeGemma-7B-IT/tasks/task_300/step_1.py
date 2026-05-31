import os
import xml.etree.ElementTree as ET
import json
from sklearn.cluster import KMeans

# Get all XML files in the current directory
xml_files = [f for f in os.listdir('.') if f.endswith('.xml')]

# Function to extract element hierarchies from an XML file
def get_element_hierarchy(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    element_hierarchy = []
    for element in root.iter():
        element_hierarchy.append(element.tag)
    return element_hierarchy

# Extract element hierarchies from all XML files
element_hierarchies = [get_element_hierarchy(f) for f in xml_files]

# Identify common element hierarchies
from collections import Counter
element_counts = Counter(element_hierarchies)
common_hierarchies = element_counts.most_common()

# Cluster files by similarity
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
features = vectorizer.fit_transform([h for h in element_hierarchies])
kmeans = KMeans(n_clusters=3)
kmeans.fit(features)
clusters = kmeans.labels_

# Save results to JSON
data = {'xml_files': xml_files, 'element_hierarchies': element_hierarchies, 'common_hierarchies': common_hierarchies, 'clusters': clusters}
with open('results.json', 'w') as f:
    json.dump(data, f)

# Generate report
print('XML files:')
for f in xml_files:
    print(f)

print('\nElement hierarchies:')
for h in element_hierarchies:
    print(h)

print('\nCommon element hierarchies:')
for h, c in common_hierarchies:
    print(f'{h}: {c}')

print('\nClusters:')
for cluster in set(clusters):
    print(f'Cluster {cluster}:')
    for i, f in enumerate(xml_files):
        if clusters[i] == cluster:
            print(f' - {f}')

# Print the largest cluster
largest_cluster = max(set(clusters), key=clusters.count)
print(f'\nLargest cluster: {largest_cluster}')
for i, f in enumerate(xml_files):
    if clusters[i] == largest_cluster:
        print(f' - {f}')
import os

text_files = [f for f in os.listdir('.') if f.endswith(('.txt', '.md', '.docx'))]
print("Found text files:", text_files)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json

documents = []
for file in text_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        documents.append(f.read())

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

clusters = {i: [] for i in range(true_k)}
for i, label in enumerate(model.labels_):
    clusters[label].append(text_files[i])

with open('document_clusters.json', 'w') as f:
    json.dump(clusters, f)

print("Clusters saved to document_clusters.json")
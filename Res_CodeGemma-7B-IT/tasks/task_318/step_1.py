# Import libraries
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import json

# Get all text files in the current directory
text_files = [f for f in os.listdir() if f.endswith('.txt')]

# Tokenize and stem each file
tokenized_texts = []
for file in text_files:
    with open(file, 'r') as f:
        text = f.read()
        tokens = word_tokenize(text)
        stemmed_tokens = [PorterStemmer().stem(token) for token in tokens if token not in stopwords.words('english')]
        tokenized_texts.append(' '.join(stemmed_tokens))

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_vectors = vectorizer.fit_transform(tokenized_texts)

# Perform K-Means clustering
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(tfidf_vectors)

# Get cluster assignments for each document
document_clusters = kmeans.labels_

# Create a dictionary of documents and their clusters
document_clusters_dict = {file: cluster for file, cluster in zip(text_files, document_clusters)}

# Save the cluster assignments to a JSON file
with open('document_clusters.json', 'w') as f:
    json.dump(document_clusters_dict, f)

# Print the largest cluster
largest_cluster = max(set(document_clusters), key=document_clusters.count)
print("Largest cluster:", largest_cluster)
import json

# Step 2: Build document similarity scores using term frequencies
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = []
with open('corpus.json', 'r') as file:
    data = json.load(file)
    for doc in data['documents']:
        documents.append(doc['content'])

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

similarity_scores = cosine_similarity(tfidf_matrix)
print("Similarity scores built successfully.")
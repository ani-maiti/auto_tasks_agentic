# Step 5: Re-run the document similarity calculation after installing the library
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the content of each text file
documents = []
for file_path in text_files:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        documents.append(file.read())

# Create TF-IDF matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Calculate cosine similarity scores
similarity_scores = cosine_similarity(tfidf_matrix)
print("Similarity scores calculated.")
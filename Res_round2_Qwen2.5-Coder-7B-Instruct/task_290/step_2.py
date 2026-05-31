# Step 2: Compute readability scores, sentiment scores, and lexical diversity metrics for each text file
import os
from readability import get_reading_time
from textblob import TextBlob
import nltk
nltk.download('punkt')

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Readability score
    reading_time = get_reading_time(content)
    
    # Sentiment analysis
    blob = TextBlob(content)
    sentiment = blob.sentiment
    
    # Lexical diversity
    words = nltk.word_tokenize(content)
    unique_words = set(words)
    lexical_diversity = len(unique_words) / len(words)
    
    return {
        'file_path': file_path,
        'readability_score': reading_time,
        'sentiment_polarity': sentiment.polarity,
        'sentiment_subjectivity': sentiment.subjectivity,
        'lexical_diversity': lexical_diversity
    }

files_to_analyze = [
    "test/test_email/data/msg_15.txt",
    "./cpython/Lib/test/test_email/data/msg_35.txt",
    # Add more file paths as needed
]

results = [analyze_file(file) for file in files_to_analyze]
import readability
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# Step 2: Compute readability scores, sentiment scores, and lexical diversity metrics
results = []

sia = SentimentIntensityAnalyzer()

for file_name in text_files:
    with open(file_name, 'r') as file:
        content = file.read()
        
        # Readability score
        readability_score = readability.get_grade(content)
        
        # Sentiment score
        sentiment_scores = sia.polarity_scores(content)
        
        # Lexical diversity metrics
        words = word_tokenize(content)
        unique_words = set(words)
        lexical_diversity = len(unique_words) / len(words)
        
        results.append({
            'file': file_name,
            'readability_score': readability_score,
            'sentiment_scores': sentiment_scores,
            'lexical_diversity': lexical_diversity
        })

print("Computed scores for all text files.")
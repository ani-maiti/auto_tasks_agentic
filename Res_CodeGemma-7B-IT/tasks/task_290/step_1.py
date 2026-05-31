# Import necessary libraries
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.metrics import lexical_diversity
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import defaultdict

# Define function to calculate readability score
def readability_score(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Calculate average word length
    avg_word_length = sum(len(token) for token in filtered_tokens) / len(filtered_tokens) if len(filtered_tokens) else 0
    # Calculate number of sentences
    sentences = text.split('.')
    num_sentences = len(sentences)
    # Calculate readability score
    readability_score = 0.398 * avg_word_length + 11.8 * (num_sentences / len(filtered_tokens)) - 15.59
    return readability_score

# Define function to calculate sentiment score
def sentiment_score(text):
    # Create sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    # Get sentiment polarity
    sentiment = analyzer.polarity_scores(text)
    # Return sentiment score
    return sentiment['compound']

# Define function to calculate lexical diversity
def lexical_diversity(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Calculate lexical diversity
    lexical_diversity = len(set(filtered_tokens)) / len(filtered_tokens)
    return lexical_diversity

# Get all text files in directory
text_files = [f for f in os.listdir('.') if f.endswith('.txt')]

# Create dictionary to store file metrics
file_metrics = defaultdict(list)

# Iterate over text files
for file_name in text_files:
    # Read file contents
    with open(file_name, 'r') as f:
        text = f.read()
    # Calculate readability score
    readability_score = readability_score(text)
    # Calculate sentiment score
    sentiment_score = sentiment_score(text)
    # Calculate lexical diversity
    lexical_diversity = lexical_diversity(text)
    # Store metrics for file
    file_metrics[file_name].extend([readability_score, sentiment_score, lexical_diversity])

# Rank files by each metric
ranked_files = {metric: sorted(file_metrics.items(), key=lambda x: x[1][metric], reverse=True) for metric in file_metrics[next(iter(file_metrics))]}

# Save results to CSV
with open('file_metrics.csv', 'w') as f:
    f.write('File Name,Readability Score,Sentiment Score,Lexical Diversity\n')
    for file_name, metrics in ranked_files.items():
        for metric, value in metrics:
            f.write(f"{file_name},{metrics[0]},{metrics[1]},{metrics[2]}\n")

# Generate report
print('File Metrics Report:')
for metric, files in ranked_files.items():
    print(f"\nTop 5 files by {metric}:")
    for file_name, value in files[:5]:
        print(f"\t{file_name}: {value[0]}")

# Print most complex file
most_complex_file = next(iter(ranked_files['Lexical Diversity']))
print(f"\nMost complex file: {most_complex_file[0]}")
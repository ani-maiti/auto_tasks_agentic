import os
from textstat import flesch_kincaid_grade, flesch_reading_ease
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from collections import Counter
import csv

# Ensure NLTK resources are available
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')

def compute_metrics(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Readability scores
    fk_grade = flesch_kincaid_grade(text)
    fk_ease = flesch_reading_ease(text)
    
    # Sentiment scores
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    
    # Lexical diversity
    words = word_tokenize(text.lower())
    unique_words = set(words)
    lexical_diversity = len(unique_words) / len(words) if words else 0
    
    return {
        'file': file_path,
        'fk_grade': fk_grade,
        'fk_ease': fk_ease,
        'sentiment_neg': sentiment['neg'],
        'sentiment_neu': sentiment['neu'],
        'sentiment_pos': sentiment['pos'],
        'sentiment_compound': sentiment['compound'],
        'lexical_diversity': lexical_diversity
    }

text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
results = []

for file in text_files:
    try:
        metrics = compute_metrics(file)
        results.append(metrics)
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Save results to CSV
with open('metrics_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['file', 'fk_grade', 'fk_ease', 'sentiment_neg', 'sentiment_neu', 'sentiment_pos', 'sentiment_compound', 'lexical_diversity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# Generate report
report = """
Readability Scores Report:
------------------------
File, Flesch-Kincaid Grade, Flesch Reading Ease

Sentiment Scores Report:
------------------------
File, Negative, Neutral, Positive, Compound

Lexical Diversity Report:
-------------------------
File, Lexical Diversity
"""

readability_sorted = sorted(results, key=lambda x: x['fk_grade'], reverse=True)
sentiment_sorted = sorted(results, key=lambda x: x['sentiment_compound'], reverse=True)
lexical_diversity_sorted = sorted(results, key=lambda x: x['lexical_diversity'], reverse=True)

report += "\nReadability Scores:\n"
for item in readability_sorted:
    report += f"{item['file']}, {item['fk_grade']:.2f}, {item['fk_ease']:.2f}\n"

report += "\nSentiment Scores:\n"
for item in sentiment_sorted:
    report += f"{item['file']}, {item['sentiment_neg']:.2f}, {item['sentiment_neu']:.2f}, {item['sentiment_pos']:.2f}, {item['sentiment_compound']:.2f}\n"

report += "\nLexical Diversity:\n"
for item in lexical_diversity_sorted:
    report += f"{item['file']}, {item['lexical_diversity']:.4f}\n"

with open('report.txt', 'w', encoding='utf-8') as report_file:
    report_file.write(report)

# Print the most complex file based on lexical diversity
most_complex_file = lexical_diversity_sorted[0]['file']
print(f"The most complex file is: {most_complex_file}")
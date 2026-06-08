import os
import pandas as pd
from textstat import textstat
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

# Create a list to store results
results = []

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Get all text files
text_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            text_files.append(os.path.join(root, file))

print(f"Found {len(text_files)} text files")

# Process each text file
for file_path in text_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Compute readability scores
        flesch_reading_ease = textstat.flesch_reading_ease(content)
        smog_index = textstat.smog_index(content)
        flesch_kincaid_grade = textstat.flesch_kincaid_grade(content)
        coleman_liau_index = textstat.coleman_liau_index(content)
        automated_readability_index = textstat.automated_readability_index(content)
        dale_chall_readability_score = textstat.dale_chall_readability_score(content)
        difficult_words = textstat.difficult_words(content)
        linsear_write_formula = textstat.linsear_write_formula(content)
        gunning_fog = textstat.gunning_fog(content)
        
        # Compute sentiment scores
        sentiment_scores = analyzer.polarity_scores(content)
        compound_sentiment = sentiment_scores['compound']
        positive_sentiment = sentiment_scores['pos']
        negative_sentiment = sentiment_scores['neg']
        neutral_sentiment = sentiment_scores['neu']
        
        # Compute lexical diversity metrics
        words = re.findall(r'\b\w+\b', content.lower())
        unique_words = set(words)
        lexical_diversity = len(unique_words) / len(words) if words else 0
        hapax_legomena = len([w for w, count in pd.Series(words).value_counts().items() if count == 1])
        hapax_legomena_ratio = hapax_legomena / len(words) if words else 0
        
        # Store results
        results.append({
            'file': file_path,
            'flesch_reading_ease': flesch_reading_ease,
            'smog_index': smog_index,
            'flesch_kincaid_grade': flesch_kincaid_grade,
            'coleman_liau_index': coleman_liau_index,
            'automated_readability_index': automated_readability_index,
            'dale_chall_readability_score': dale_chall_readability_score,
            'difficult_words': difficult_words,
            'linsear_write_formula': linsear_write_formula,
            'gunning_fog': gunning_fog,
            'compound_sentiment': compound_sentiment,
            'positive_sentiment': positive_sentiment,
            'negative_sentiment': negative_sentiment,
            'neutral_sentiment': neutral_sentiment,
            'lexical_diversity': lexical_diversity,
            'hapax_legomena_ratio': hapax_legomena_ratio
        })
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Save results to CSV
df = pd.DataFrame(results)
df.to_csv('text_analysis_results.csv', index=False)

print("Analysis complete. Results saved to text_analysis_results.csv")
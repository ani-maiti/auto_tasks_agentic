import re
from collections import Counter

# Read the titles from file
with open('doc_crawl/titles.txt', 'r') as f:
    titles = [line.strip() for line in f if line.strip()]

# Extract keywords from titles
keywords = []
for title in titles:
    # Remove common words and punctuation, then split into words
    words = re.findall(r'\b[a-zA-Z]+\b', title.lower())
    # Filter out very short words and common stop words
    filtered_words = [word for word in words if len(word) > 2 and word not in 
                     ['the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'its', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use', 'doc', 'python', 'manual', 'reference', 'guide', 'tutorial', 'library', 'standard', 'built', 'in', 'functions', 'module', 'class', 'object', 'method', 'function', 'exception', 'error', 'type', 'value', 'string', 'number', 'list', 'dict', 'set', 'tuple', 'file', 'io', 'input', 'output', 'process', 'thread', 'async', 'await', 'coroutine', 'generator', 'iterator', 'context', 'manager', 'decorator', 'property', 'attribute', 'variable', 'constant', 'parameter', 'argument', 'return', 'yield', 'import', 'from', 'as', 'with', 'try', 'except', 'finally', 'raise', 'assert', 'break', 'continue', 'pass', 'del', 'global', 'nonlocal', 'lambda', 'if', 'elif', 'else', 'while', 'for', 'match', 'case', 'def', 'class', 'import', 'from', 'as', 'with', 'try', 'except', 'finally', 'raise', 'assert', 'break', 'continue', 'pass', 'del', 'global', 'nonlocal', 'lambda', 'if', 'elif', 'else', 'while', 'for', 'match', 'case', 'def', 'class']]
    keywords.extend(filtered_words)

# Count keyword frequencies
keyword_counts = Counter(keywords)

# Get top 20 keywords
top_keywords = keyword_counts.most_common(20)

# Print results
print("Top 20 Keywords:")
for keyword, count in top_keywords:
    print(f"{keyword}: {count}")

# Save analysis to file
with open('keyword_analysis.txt', 'w') as f:
    f.write("Top 20 Keywords:\n")
    for keyword, count in top_keywords:
        f.write(f"{keyword}: {count}\n")
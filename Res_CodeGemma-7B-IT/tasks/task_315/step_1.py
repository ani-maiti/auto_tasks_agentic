import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import networkx as nx
import json

# Retrieve Hacker News stories
response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.content, 'html.parser')

# Extract keywords and domains
keywords = []
domains = []
for story in soup.find_all('a', class_='storylink'):
    text = story.text.lower()
    tokens = word_tokenize(text)
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    keywords.extend(lemmatized_tokens)
    domains.append(story['href'].split('/')[2])

# Build keyword co-occurrence network
graph = nx.Graph()
for keyword in keywords:
    graph.add_node(keyword)

for i in range(len(keywords)):
    for j in range(i + 1, len(keywords)):
        if keywords[i] != keywords[j]:
            graph.add_edge(keywords[i], keywords[j])

# Save graph to JSON
nx.write_graphml(graph, 'hacker_news_graph.graphml')

# Generate report
print('Top 10 keywords:')
for keyword, degree in graph.degree():
    print(f'{keyword}: {degree}')

print('\nTop 10 most connected keywords:')
for keyword, neighbors in graph.adjacency():
    if len(neighbors) > 9:
        print(f'{keyword}: {neighbors[:10]}')

print('\nTop 10 most common domains:')
domain_counts = {}
for domain in domains:
    domain_counts[domain] = domain_counts.get(domain, 0) + 1
sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)
print(sorted_domains[:10])
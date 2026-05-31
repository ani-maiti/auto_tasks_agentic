# Step 3: Print the most common topic
with open('classified_repositories.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    all_topics = [topic.split(', ') for repo in reader for topic in repo['Topics'].split(',')]
    flattened_topics = [topic for sublist in all_topics for topic in sublist]
    most_common_topic = Counter(flattened_topics).most_common(1)[0][0]

print(f"The most common topic among the top 50 Python repositories is: {most_common_topic}")
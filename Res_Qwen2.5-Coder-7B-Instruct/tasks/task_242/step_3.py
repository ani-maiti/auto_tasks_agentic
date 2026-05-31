import csv

# Step 2: Classify repositories by topic keywords
topics = {
    'web development': ['django', 'flask', 'react'],
    'data science': ['pandas', 'numpy', 'scikit-learn'],
    'machine learning': ['tensorflow', 'keras', 'pytorch'],
    'devops': ['docker', 'kubernetes', 'ansible']
}

classified_repositories = []

with open('top_50_python_repos.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        repo_name = row[0]
        topics_found = set()
        for topic, keywords in topics.items():
            if any(keyword.lower() in repo_name.lower() for keyword in keywords):
                topics_found.add(topic)
        classified_repositories.append((repo_name, topics_found))

# Save classified repositories to a new CSV file
with open('classified_repositories.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Repository Name', 'Topics'])
    for repo in classified_repositories:
        writer.writerow([repo[0], ', '.join(repo[1])])

print("Repositories classified by topics and saved to classified_repositories.csv")
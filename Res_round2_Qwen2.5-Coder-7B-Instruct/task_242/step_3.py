# Step 2: Classify repositories by topic keywords
topics = {
    'machine learning': ['ml', 'tensorflow', 'keras', 'pytorch'],
    'data science': ['pandas', 'numpy', 'scikit-learn', 'statsmodels'],
    'web development': ['django', 'flask', 'react', 'vue'],
    'devops': ['docker', 'kubernetes', 'ansible', 'terraform'],
    'security': ['cryptography', 'ssl', 'hacking', 'penetration testing']
}

repository_topics = []

for repo in repositories:
    repo_topics = []
    for topic, keywords in topics.items():
        if any(keyword in repo['name'].lower() or keyword in repo['description'].lower() for keyword in keywords):
            repo_topics.append(topic)
    repository_topics.append(repo_topics)

# Save results to CSV
with open('github_repositories.csv', 'w', newline='') as csvfile:
    fieldnames = ['repo_name', 'repo_url', 'topics']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i, repo in enumerate(repositories):
        writer.writerow({
            'repo_name': repo['name'],
            'repo_url': repo['html_url'],
            'topics': ', '.join(repository_topics[i])
        })

print("Results saved to github_repositories.csv")
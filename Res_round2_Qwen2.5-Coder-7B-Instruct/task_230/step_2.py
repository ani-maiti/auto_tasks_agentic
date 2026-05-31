# Step 2: Compute average stars and forks
total_stars = sum(repo['stargazers_count'] for repo in repositories)
total_forks = sum(repo['forks_count'] for repo in repositories)
average_stars = total_stars / len(repositories)
average_forks = total_forks / len(repositories)

print(f"Average Stars: {average_stars}")
print(f"Average Forks: {average_forks}")
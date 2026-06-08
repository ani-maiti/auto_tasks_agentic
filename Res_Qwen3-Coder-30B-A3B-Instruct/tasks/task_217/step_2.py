import csv
import statistics

# Read the CSV file and calculate averages
with open('repo_metadata.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Collect all values
    stars = []
    forks = []
    open_issues = []
    
    for row in reader:
        stars.append(int(row['stars']))
        forks.append(int(row['forks']))
        open_issues.append(int(row['open_issues']))
    
    # Calculate averages
    avg_stars = statistics.mean(stars)
    avg_forks = statistics.mean(forks)
    avg_open_issues = statistics.mean(open_issues)
    
    # Find the most starred repository
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    max_stars = 0
    most_starred_repo = ""
    
    for row in reader:
        star_count = int(row['stars'])
        if star_count > max_stars:
            max_stars = star_count
            most_starred_repo = row['name']
    
    print(f"Average stars: {avg_stars:.2f}")
    print(f"Average forks: {avg_forks:.2f}")
    print(f"Average open issues: {avg_open_issues:.2f}")
    print(f"Most starred repository: {most_starred_repo} with {max_stars} stars")
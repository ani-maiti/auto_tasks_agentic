import requests
import csv
from datetime import datetime
import time

# List of popular GitHub repositories (50 repos)
repos = [
    "facebook/react", "vuejs/vue", "angular/angular", "tensorflow/tensorflow",
    "microsoft/vscode", "nodejs/node", "jquery/jquery", "expressjs/express",
    "webpack/webpack", "axios/axios", "babel/babel", "gatsbyjs/gatsby",
    "nextjs/next.js", "vercel/next.js", "sveltejs/svelte", "nuxt/nuxt",
    "ionic-team/ionic", "expo/expo", "storybookjs/storybook", "jestjs/jest",
    "cypress-io/cypress", "puppeteer/puppeteer", "electron/electron", "nwjs/nw.js",
    "atom/atom", "brave/browser-laptop", "mongodb/mongo", "redis/redis",
    "docker/docker", "kubernetes/kubernetes", "prometheus/prometheus",
    "grafana/grafana", "influxdata/influxdb", "elastic/elasticsearch",
    "apache/spark", "apache/hadoop", "apache/kafka", "apache/cassandra",
    "apache/zookeeper", "apache/flink", "apache/airflow", "apache/nifi",
    "apache/beam", "apache/druid", "apache/kylin", "apache/solr",
    "apache/tika", "apache/accumulo", "apache/ignite", "apache/calcite",
    "apache/phoenix", "apache/zeppelin", "apache/arrow", "apache/parquet"
]

# Function to get latest release info
def get_latest_release(repo):
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                'repo': repo,
                'tag_name': data.get('tag_name', ''),
                'published_at': data.get('published_at', ''),
                'name': data.get('name', ''),
                'body': data.get('body', '')
            }
        elif response.status_code == 404:
            # No releases found
            return {
                'repo': repo,
                'tag_name': '',
                'published_at': '',
                'name': '',
                'body': ''
            }
        else:
            print(f"Error fetching {repo}: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception fetching {repo}: {e}")
        return None

# Fetch release information for all repositories
print("Fetching release information...")
releases = []
for i, repo in enumerate(repos):
    release_info = get_latest_release(repo)
    if release_info:
        releases.append(release_info)
    # Rate limiting
    if (i + 1) % 10 == 0:
        print(f"Fetched {i + 1} repositories...")
    time.sleep(1)

print(f"Successfully fetched {len(releases)} repositories")

# Calculate release age
def calculate_age(published_at_str):
    if not published_at_str:
        return "No release"
    
    try:
        published_date = datetime.strptime(published_at_str, "%Y-%m-%dT%H:%M:%SZ")
        now = datetime.utcnow()
        delta = now - published_date
        days = delta.days
        if days < 30:
            return f"{days} days"
        elif days < 365:
            months = days // 30
            return f"{months} months"
        else:
            years = days // 365
            return f"{years} years"
    except Exception as e:
        return f"Error: {e}"

# Add age to release information
print("Calculating release ages...")
for release in releases:
    release['age'] = calculate_age(release['published_at'])

# Save to CSV
csv_filename = "github_releases.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['repo', 'tag_name', 'name', 'published_at', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for release in releases:
        writer.writerow({
            'repo': release['repo'],
            'tag_name': release['tag_name'],
            'name': release['name'],
            'published_at': release['published_at'],
            'age': release['age']
        })

print(f"Release information saved to {csv_filename}")
# Fetch releases for each repository
all_releases = []

for repo_name in repo_names:
    try:
        releases_url = f"https://api.github.com/repos/{org_name}/{repo_name}/releases?per_page=100"
        response = requests.get(releases_url)
        releases = response.json()
        
        for release in releases:
            all_releases.append({
                'repository': repo_name,
                'tag_name': release['tag_name'],
                'published_at': release['published_at'],
                'name': release['name']
            })
            
        print(f"Fetched {len(releases)} releases from {repo_name}")
    except Exception as e:
        print(f"Error fetching releases from {repo_name}: {e}")

print(f"Total releases collected: {len(all_releases)}")
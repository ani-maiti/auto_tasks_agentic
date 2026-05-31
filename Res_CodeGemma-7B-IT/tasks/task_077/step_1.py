from github import Github

# Set up GitHub client
g = Github("your_username", "your_password")

# Get the repository
repo = g.get_repo("cli/cli")

# Get the latest release
latest_release = repo.get_latest_release()

# Print the tag name
print(latest_release.tag_name)
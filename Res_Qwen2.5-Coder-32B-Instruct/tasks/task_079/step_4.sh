echo "Fetching the requests GitHub repository data again..."
curl -s https://api.github.com/repos/psf/requests | grep stargazers_count
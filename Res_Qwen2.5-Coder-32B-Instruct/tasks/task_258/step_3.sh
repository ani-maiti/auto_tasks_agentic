echo "Attempting to retrieve metadata for top 100 GitHub repositories tagged with data-science..."
curl -s "https://api.github.com/search/repositories?q=topic:data-science&sort=stars&order=desc&per_page=100" > repos.json
echo "Data retrieved and saved to repos.json"
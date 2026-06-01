echo "Fetching numpy GitHub repository data..."
curl -s https://api.github.com/repos/numpy/numpy | grep '"stargazers_count"'
echo "Fetching the number of open issues in the pandas GitHub repository..."
curl -s https://api.github.com/repos/pandas-dev/pandas | grep open_issues_count
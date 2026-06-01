echo "Fetching the number of open issues in the requests GitHub repository..."
curl -s https://api.github.com/repos/psf/requests | grep '"open_issues":' | awk -F': ' '{print $2}' | tr -d ','
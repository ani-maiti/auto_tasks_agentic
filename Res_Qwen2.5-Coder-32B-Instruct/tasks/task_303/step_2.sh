echo "Fetching the first page of datasets from data.gov..."
curl -s https://catalog.data.gov/dataset?q=environment | grep -oP '(?<=href=")/dataset/[^\"]+'
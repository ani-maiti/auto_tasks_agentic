echo "Please manually enter the URL of the documentation site to crawl:"
url="https://example.com/docs"  # Replace with the actual URL
echo "Starting crawl of $url"
wget --spider -r -l 1 -np -nd -o wget_output.txt "$url"
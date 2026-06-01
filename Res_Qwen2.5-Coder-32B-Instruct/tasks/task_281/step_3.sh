echo "Please provide the URL of the public documentation website."
read url
echo "Starting crawl of $url"
timeout 60s curl -I "$url" 2>/dev/null | grep HTTP
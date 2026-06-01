echo "Please provide the URL of the documentation site to crawl:"
read url
echo "Starting crawl of $url"
wget --spider -r -l 1 -np -nd -o wget_output.txt "$url"
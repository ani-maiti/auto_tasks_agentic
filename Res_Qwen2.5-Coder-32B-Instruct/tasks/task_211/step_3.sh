echo "Enter the URL of the website to crawl:"
read website_url
echo "Starting to crawl $website_url"
timeout 60s wget --spider -r -l1 -np -nd -o wget_output.txt "$website_url"
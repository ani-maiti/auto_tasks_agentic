echo "Finding a public RSS feed related to technology..."
curl -s https://www.cnet.com/rss | grep -oP '(?<=<link>).*?(?=</link>)' | head -n 1
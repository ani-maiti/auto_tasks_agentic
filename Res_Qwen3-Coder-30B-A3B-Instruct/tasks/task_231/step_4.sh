#!/bin/bash

# Create a directory for our work
mkdir -p doc_crawl
cd doc_crawl

# Download the main page
curl -s https://docs.python.org/3/ > main.html

# Extract all HTML links
grep -o 'href="[^"]*\.html"' main.html | cut -d'"' -f2 | head -100 > links.txt

# Create a script to fetch titles
cat > fetch_titles.sh << 'EOF'
#!/bin/bash
while read -r link; do
    if [[ $link == /* ]]; then
        full_url="https://docs.python.org/3$link"
    else
        full_url="https://docs.python.org/3/$link"
    fi
    curl -s "$full_url" | grep -o '<title>[^<]*</title>' | sed 's/<title>\(.*\)<\/title>/\1/'
done < links.txt
EOF

chmod +x fetch_titles.sh
./fetch_titles.sh > titles.txt
rm titles.txt
curl -s "https://rss.cnn.com/rss/edition.rss" | grep -o '<title>[^<]*</title>' | head -n 100 | sed 's/<title>\(.*\)<\/title>/\1/' > titles.txt
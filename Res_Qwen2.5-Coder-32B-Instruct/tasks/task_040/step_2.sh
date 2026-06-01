echo "Counting unique words in all text files..."
grep -oE '\w+' *.txt | sort | uniq | wc -l
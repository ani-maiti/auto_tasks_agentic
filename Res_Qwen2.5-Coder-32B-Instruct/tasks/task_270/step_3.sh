echo "Counting occurrences of each programming language..."
sort code_fences.txt | uniq -c | sort -nr > language_counts.txt
cat language_counts.txt
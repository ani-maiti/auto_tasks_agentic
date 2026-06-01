echo "Converting the largest_files.txt to CSV format."
awk '{print $2 "," $1}' largest_files.txt > largest_files.csv
echo "Conversion complete. CSV saved as largest_files.csv"
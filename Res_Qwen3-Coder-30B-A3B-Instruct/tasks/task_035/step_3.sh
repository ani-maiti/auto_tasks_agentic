# Create a temporary file to store file sizes
find . -type f -exec stat -c "%s %n" {} \; > /tmp/file_sizes.txt

# Calculate average file size
awk '{sum += $1; count++} END {print "Average:", sum/count}' /tmp/file_sizes.txt

# Find files larger than average
awk '{sum += $1; count++} END {avg = sum/count; print "Average:", avg; getline; while (NR <= FNR) {if ($1 > avg) print $0; getline}}' /tmp/file_sizes.txt /tmp/file_sizes.txt
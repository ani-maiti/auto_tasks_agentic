echo "Getting file sizes in bytes..."
find . -type f -exec ls -l {} + | awk '{print $5}' > file_sizes_bytes.txt
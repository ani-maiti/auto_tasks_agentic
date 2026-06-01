echo "The ten oldest files in the current directory tree are:"
find . -type f -printf "%T+ %p\n" | sort | head -n 10 | awk '{print $2}'
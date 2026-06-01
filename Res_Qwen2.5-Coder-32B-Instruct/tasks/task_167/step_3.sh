echo "The ten newest files in the current directory tree are:"
find . -type f -printf "%T+ %p\n" | sort -r | head -n 10 | cut -d' ' -f2-
echo "Checking if there are any directories larger than 10 MB..."
du -sh */ | grep '[0-9]\+G\|[1-9][0-9]\+M'
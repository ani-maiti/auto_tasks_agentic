echo "Finding files accessed within the last day in home directory..."
find ~ -type f -atime -1 2>/dev/null
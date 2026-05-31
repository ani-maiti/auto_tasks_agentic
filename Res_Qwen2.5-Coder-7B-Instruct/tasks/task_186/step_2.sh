echo "Total number of lines across all shell scripts:"
grep -oP '^\d+' <<< "$stdout" | awk '{sum+=$1} END {print sum}'
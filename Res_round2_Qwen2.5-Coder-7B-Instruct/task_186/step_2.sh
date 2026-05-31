echo "Total number of lines in shell scripts:"
grep -oP '^\d+\s+.*\.sh' <<< "$output" | awk '{sum += $1} END {print sum}'
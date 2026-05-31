echo "Shell scripts and their line counts:"
grep -oP '^\d+\s+.*\.sh' <<< "$output"
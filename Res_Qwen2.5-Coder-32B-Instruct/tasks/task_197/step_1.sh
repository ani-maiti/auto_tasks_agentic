echo "Starting directory size check"
du -sh */ 2>/dev/null | sort -rh | head -n 1
echo "Checking /home for largest subdirectory"
du -sh /home/* 2>/dev/null | sort -rh | head -n 1
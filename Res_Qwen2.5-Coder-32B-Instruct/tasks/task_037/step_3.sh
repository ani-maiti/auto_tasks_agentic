echo "Checking /home/ai_admin for largest subdirectory"
du -sh /home/ai_admin/* 2>/dev/null | sort -rh | head -n 1
echo "Checking if there are subdirectories in cpython"
du -sh cpython/*/ 2>/dev/null | sort -rh | head -n 1
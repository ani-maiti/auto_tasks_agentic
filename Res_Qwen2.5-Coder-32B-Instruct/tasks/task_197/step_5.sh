echo "Largest subdirectory in cpython/Lib is test with size 39M"
du -sh cpython/Lib/test/*/ 2>/dev/null | sort -rh | head -n 1
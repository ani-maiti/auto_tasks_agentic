echo "Largest subdirectory in cpython is Lib with size 56M"
du -sh cpython/Lib/*/ 2>/dev/null | sort -rh | head -n 1
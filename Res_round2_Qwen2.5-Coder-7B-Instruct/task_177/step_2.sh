cat <<EOF > largest_files_report.txt
$(du -ah --max-depth=1 | sort -hr | head -n 100)
EOF
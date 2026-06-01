echo "Starting directory listing..."
ls -l | grep "^d" | awk '{print $9}'
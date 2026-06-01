echo "Please provide a path to search for log files:"
read log_path
find "$log_path" -type f -name "*.log" -print
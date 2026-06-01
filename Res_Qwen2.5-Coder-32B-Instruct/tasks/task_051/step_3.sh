echo "Checking current directory name length..."
current_dir_name=$(basename "$PWD")
current_dir_length=${#current_dir_name}
echo "Current directory name: $current_dir_name"
echo "Current directory name length: $current_dir_length"
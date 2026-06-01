echo "Starting image discovery..."
find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.bmp" \) > image_files.txt
echo "Image discovery complete. Listing files..."
cat image_files.txt
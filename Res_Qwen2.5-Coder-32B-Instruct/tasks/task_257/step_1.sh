echo "Finding all image files..."
find . \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.bmp" -o -iname "*.gif" \) > image_files.txt
echo "Image files found and listed in image_files.txt"
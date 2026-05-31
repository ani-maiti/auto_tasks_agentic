# Step 2: Inspect contained file extensions
# We'll use tar to extract and list file extensions
for archive in $(find . -type f \( -name "*.zip" -o -name "*.tar.gz" -o -name "*.rar" -o -name "*.7z" \)); do
    echo "Inspecting $archive"
    case "$archive" in
        *.zip) unzip -l "$archive" | grep -oP '\.\K[^ ]+' ;;
        *.tar.gz) tar -tzf "$archive" | grep -oP '\.\K[^ ]+' ;;
        *.rar) unrar l "$archive" | grep -oP '\.\K[^ ]+' ;;
        *.7z) 7z l "$archive" | grep -oP '\.\K[^ ]+' ;;
    esac
done > file_extensions.txt
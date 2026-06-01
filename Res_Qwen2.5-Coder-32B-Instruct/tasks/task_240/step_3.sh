for archive in $(find . -type f \( -iname "*.zip" -o -iname "*.tar" -o -iname "*.gz" -o -iname "*.bz2" -o -iname "*.rar" \)); do
    echo "Processing $archive"
    if [[ $archive == *.tar.gz || $archive == *.tgz ]]; then
        tar -tzf "$archive" | sed 's/.*\(\.[^.]*\)$/\1/'
    elif [[ $archive == *.tar.bz2 ]]; then
        tar -tjf "$archive" | sed 's/.*\(\.[^.]*\)$/\1/'
    elif [[ $archive == *.tar ]]; then
        tar -tf "$archive" | sed 's/.*\(\.[^.]*\)$/\1/'
    elif [[ $archive == *.rar ]]; then
        rar l -n "$archive" | awk '/^Path/{getline; print $NF}' | sed 's/.*\(\.[^.]*\)$/\1/'
    fi
done > extensions.txt
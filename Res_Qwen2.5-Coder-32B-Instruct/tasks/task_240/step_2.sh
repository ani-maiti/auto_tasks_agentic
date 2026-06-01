for archive in $(find . -type f \( -iname "*.zip" -o -iname "*.tar" -o -iname "*.gz" -o -iname "*.bz2" -o -iname "*.rar" \)); do
    echo "Processing $archive"
    if [[ $archive == *.zip ]]; then
        unzip -l "$archive" | awk 'NR>2 {print $NF}' | sed 's/.*\(\.[^.]*\)$/\1/'
    elif [[ $archive == *.tar ]]; then
        tar -tf "$archive" | sed 's/.*\(\.[^.]*\)$/\1/'
    elif [[ $archive == *.gz ]]; then
        gzip -dc "$archive" | tar -tf - | sed 's/.*\(\.[^.]*\)$/\1/'
    elif [[ $archive == *.bz2 ]]; then
        bzip2 -dc "$archive" | tar -tf - | sed 's/.*\(\.[^.]*\)$/\1/'
    elif [[ $archive == *.rar ]]; then
        rar l -n "$archive" | awk '/^Path/{getline; print $NF}' | sed 's/.*\(\.[^.]*\)$/\1/'
    fi
done > extensions.txt
echo "Sorting and finding median using awk..."
find . -type f -exec ls -l {} + | awk '{print $5}' | sort -n | awk '{
    count[NR] = $1
}
END {
    if (NR % 2 == 1) {
        print "The median file size is: " count[(NR+1)/2] " bytes"
    } else {
        mid1 = count[NR/2]
        mid2 = count[NR/2+1]
        print "The median file size is: " (mid1 + mid2) / 2 " bytes"
    }
}'
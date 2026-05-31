awk '{print $2}' function_definitions.txt | while read func; do
    file=$(grep -rl "$func" $(cat py_files.txt))
    line=$(grep -n "$func" $file | cut -d: -f1)
    length=$(wc -l < $file)
    echo "$file:$line:$length"
done > function_lengths.txt
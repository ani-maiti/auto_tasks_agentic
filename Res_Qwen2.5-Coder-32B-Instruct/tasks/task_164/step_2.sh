echo "Calculating average file size..."
total_size=1060464294
number_of_files=8453
average_size=$(echo "scale=2; $total_size / $number_of_files" | bc)
echo "Average file size: $average_size bytes"
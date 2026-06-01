echo "Calculating average file size without bc..."
total_size=1060464294
number_of_files=8453
average_size=$((total_size / number_of_files))
echo "Average file size: $average_size bytes"
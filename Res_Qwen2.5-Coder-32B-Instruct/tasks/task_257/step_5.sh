echo "Largest duplicate group found:"
cat image_hashes.csv | grep "$(head -n 1 image_hashes.csv | cut -d',' -f1)" | cut -d',' -f2
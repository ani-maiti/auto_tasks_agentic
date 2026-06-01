echo "Number of CSV files: 2"
echo "Row counts:"
cat largest_files.csv report.csv | grep -v '^$' | wc -l
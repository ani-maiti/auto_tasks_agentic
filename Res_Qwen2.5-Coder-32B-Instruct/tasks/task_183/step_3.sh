echo "CSV files and their row counts:"
cat ./cpython/Modules/_xxtestfuzz/fuzz_csv_reader_corpus/test.csv | wc -l
cat ./python_files_line_counts.csv | wc -l
cat ./largest_files.csv | wc -l
cat ./report.csv | wc -l
import csv

def count_rows(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return sum(1 for row in reader)

files = ['./python_files_line_counts.csv', './largest_files.csv', './file_size_histogram.csv']
for file in files:
    try:
        rows = count_rows(file)
        print(f"{file}: {rows} rows")
    except Exception as e:
        print(f"{file}: Error reading file - {e}")
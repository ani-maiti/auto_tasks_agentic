import os
import csv
import datetime
import json
from collections import defaultdict

# Find all CSV files in the current directory
csv_files = [f for f in os.listdir() if f.endswith('.csv')]

# Initialize variables for analysis
date_columns = []
date_ranges = defaultdict(list)
overlapping_datasets = set()

# Iterate over each CSV file
for csv_file in csv_files:
    # Open the CSV file
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)

        # Identify columns containing dates
        for row in reader:
            for i, cell in enumerate(row):
                try:
                    datetime.datetime.strptime(cell, '%Y-%m-%d')
                    date_columns.append(i)
                except ValueError:
                    pass

    # Normalize date formats and compute date ranges
    for i in date_columns:
        for row in reader:
            cell = row[i]
            try:
                date = datetime.datetime.strptime(cell, '%Y-%m-%d')
                date_ranges[i].append(date)
            except ValueError:
                pass

# Detect overlapping datasets
for i in date_ranges:
    if len(date_ranges[i]) > 1:
        overlapping_datasets.add(i)

# Save the analysis to JSON
analysis = {
    'date_columns': date_columns,
    'date_ranges': date_ranges,
    'overlapping_datasets': list(overlapping_datasets)
}
with open('analysis.json', 'w') as f:
    json.dump(analysis, f)

# Generate a report
report = f"""
## Dataset Analysis Report

**Date Columns:** {date_columns}

**Date Ranges:** {date_ranges}

**Overlapping Datasets:** {overlapping_datasets}

**Dataset with Widest Range:**

* **Column:** {max(date_ranges, key=lambda k: max(date_ranges[k]))}
* **Start Date:** {min(date_ranges[max(date_ranges, key=lambda k: max(date_ranges[k]))])}
* **End Date:** {max(date_ranges[max(date_ranges, key=lambda k: max(date_ranges[k]))])}
"""
print(report)
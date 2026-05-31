import os

# Create a new directory to store the report
os.mkdir("directory_report")

# Create a file to write the report to
report_file = open("directory_report/report.txt", "w")

# Write the report to the file
report_file.write("Directory Report:\n")
for directory, size in sorted_directories:
    report_file.write(f"{directory:<20s} {size:>10d}\n")

# Close the report file
report_file.close()

# Print a message to the console
print("Report written to directory_report/report.txt")
```
execution trace:
stdout:


stderr:


return code: 0
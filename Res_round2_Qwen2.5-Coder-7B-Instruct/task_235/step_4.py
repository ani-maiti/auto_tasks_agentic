import markdown

# Generate a Markdown report
report = "# CSV Primary Key Detection Report\n\n"

for csv_file, keys in results.items():
    report += f"## {csv_file}\n"
    report += "Potential primary key columns:\n"
    for key in keys:
        report += f"- {key}\n"

# Save the report to a Markdown file
with open("primary_key_report.md", "w") as f:
    f.write(report)

print("Report saved to primary_key_report.md")
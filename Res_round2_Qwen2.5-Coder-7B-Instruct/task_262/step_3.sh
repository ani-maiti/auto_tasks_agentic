echo "# Command Frequency Report" > command_report.md
echo "" >> command_report.md
cat command_frequency.txt | while read line; do echo "- $line" >> command_report.md; done
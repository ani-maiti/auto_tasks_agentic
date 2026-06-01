echo "Generating Markdown report..."
awk '{print "| " $2 " | " $1 " |"}' command_frequency.txt > command_frequency_report.md
echo "| Command | Frequency |" >> command_frequency_report.md
echo "|---------|-----------|" >> command_frequency_report.md
cat command_frequency.txt | awk '{print "| " $2 " | " $1 " |"}' >> command_frequency_report.md
echo "Cleaning up paths in report..."
awk '{if ($2 !~ /^\//) print $0}' file_extension_report.txt > cleaned_file_extension_report.txt
echo "Cleaned report saved to cleaned_file_extension_report.txt"
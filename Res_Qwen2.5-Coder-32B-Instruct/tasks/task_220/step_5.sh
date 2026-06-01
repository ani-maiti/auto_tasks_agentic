echo "Generating frequency table of third-party modules"
awk '{print $NF}' filtered_imports.txt | sort | uniq -c | sort -nr > module_frequency.txt
echo "Frequency table saved to module_frequency.txt"
cat module_frequency.txt
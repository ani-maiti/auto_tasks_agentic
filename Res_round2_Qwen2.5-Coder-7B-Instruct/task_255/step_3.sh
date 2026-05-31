echo "File,Heading" > report.csv
cat duplicated_headings.txt | while read heading; do
    grep -r "$heading" $(grep -l "$heading" markdown_files.txt) >> report.csv
done
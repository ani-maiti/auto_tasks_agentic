cat xml_files.txt | xargs xmllint --noout
```

This command uses `xmllint` to validate the structure of each XML file listed in `xml_files.txt`. It will output any validation errors to the terminal.
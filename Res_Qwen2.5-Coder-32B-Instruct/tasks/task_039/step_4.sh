echo "Searching specific files for email addresses..."
grep -E -o "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" _3.txt test.py task_descriptions.txt task_descriptions_all.txt
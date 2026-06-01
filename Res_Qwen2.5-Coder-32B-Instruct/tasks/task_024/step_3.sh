echo "Verification: Checking if ./task_descriptions.txt is indeed the oldest file."
find . -type f -newer ./task_descriptions.txt | wc -l
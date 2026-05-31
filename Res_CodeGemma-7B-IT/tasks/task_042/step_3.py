import os
import re

def get_files_with_date(directory):
    """
    Returns a list of files whose names contain a date in the format YYYY-MM-DD.

    Args:
        directory: The directory to search.

    Returns:
        A list of filenames.
    """

    files = []
    for filename in os.listdir(directory):
        if re.search(r"\d{4}-\d{2}-\d{2}", filename):
            files.append(filename)

    return files

files = get_files_with_date(".")
for filename in files:
    print(filename)
```
execution trace:
stdout:
task_descriptions_all.txt
task_descriptions.txt


stderr:


return code: 0
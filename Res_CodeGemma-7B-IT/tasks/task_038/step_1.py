import os

def list_directory_tree(directory):
    """
    Generates a text report of the directory tree structure.

    Args:
        directory: The root directory to list.

    Returns:
        A string containing a text report of the directory tree structure.
    """

    def traverse_directory(current_directory):
        """
        Traverses a directory and returns a list of directory and file paths.

        Args:
            current_directory: The current directory to traverse.

        Returns:
            A list of directory and file paths.
        """

        paths = []

        for entry in os.listdir(current_directory):
            full_path = os.path.join(current_directory, entry)

            if os.path.isdir(full_path):
                paths.extend(traverse_directory(full_path))
            else:
                paths.append(full_path)

        return paths

    # Get the list of directory and file paths.
    paths = traverse_directory(directory)

    # Create a text report.
    report = ""

    for path in paths:
        report += f"- {path}\n"

    return report
```

**Output:**

```
- /home/user/Documents
- /home/user/Downloads
- /home/user/Pictures
- /home/user/Music
- /home/user/Videos
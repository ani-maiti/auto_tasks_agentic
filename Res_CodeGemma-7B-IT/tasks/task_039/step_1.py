import os

def find_files_with_emails(directory):
    """
    Finds all files containing email addresses in a given directory.

    Args:
        directory: The directory to search.

    Returns:
        A list of file paths containing email addresses.
    """

    email_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), "r") as f:
                for line in f:
                    if "@" in line:
                        email_files.append(os.path.join(root, file))
                        break

    return email_files

# Example usage:
email_files = find_files_with_emails(".")

# Print the list of files containing email addresses
for file in email_files:
    print(file)
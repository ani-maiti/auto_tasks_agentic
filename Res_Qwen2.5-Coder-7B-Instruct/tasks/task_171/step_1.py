import os
import re

# Define the regular expression pattern for matching email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Function to find emails in a file
def find_emails_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            emails = re.findall(email_pattern, content)
            return emails
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

# Function to process all text files in a directory
def process_directory(directory):
    emails = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                emails.extend(find_emails_in_file(file_path))
    return emails

# Main function to start the process
def main():
    directory_to_search = input("Enter the directory path to search for text files: ")
    all_emails = process_directory(directory_to_search)
    if all_emails:
        print("Found email addresses:")
        for email in all_emails:
            print(email)
    else:
        print("No email addresses found.")

if __name__ == "__main__":
    main()
```

This script will prompt the user to enter a directory path, then it will recursively search for `.txt` files within that directory and extract all email addresses found in those files. The extracted email addresses will be printed out.
import os
from datetime import datetime

def get_file_age(file_path):
    """Returns the age of a file in days."""
    file_creation_time = datetime.fromtimestamp(os.path.getmtime(file_path))
    current_time = datetime.now()
    return (current_time - file_creation_time).days

def get_oldest_files(num_files):
    """Returns a list of the oldest files in the current directory tree."""
    current_dir = os.getcwd()
    files = [(file_path, get_file_age(file_path)) for file_path in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, file_path))]
    files.sort(key=lambda f: f[1], reverse=True)
    return [file_path for file_path, _ in files[:num_files]]

oldest_files = get_oldest_files(10)
print(oldest_files)
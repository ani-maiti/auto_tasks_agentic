import os
from datetime import datetime

def get_oldest_file(root_dir):
    oldest_file = None
    oldest_time = datetime.max

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                file_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                if file_time < oldest_time:
                    oldest_time = file_time
                    oldest_file = filepath
            except Exception as e:
                print(f"Error accessing {filepath}: {e}")

    return oldest_file

print(get_oldest_file('.'))
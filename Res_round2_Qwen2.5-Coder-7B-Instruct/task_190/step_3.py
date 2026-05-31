import os
from datetime import datetime, timedelta

one_hour_ago = datetime.now() - timedelta(hours=1)
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getmtime(file_path) > one_hour_ago.timestamp():
            print(file_path)
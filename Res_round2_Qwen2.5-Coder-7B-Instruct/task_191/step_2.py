import os
from datetime import datetime, timedelta

one_day_ago = datetime.now() - timedelta(days=1)
one_day_ago_timestamp = int(one_day_ago.timestamp())

files_modified_last_day = [file for file in os.listdir('.') if os.path.isfile(file) and os.path.getmtime(file) > one_day_ago_timestamp]

for file in files_modified_last_day:
    print(file)
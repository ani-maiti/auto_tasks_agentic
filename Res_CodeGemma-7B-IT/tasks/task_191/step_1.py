import datetime
import os

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

for filename in os.listdir("."):
    file_path = os.path.join(".", filename)
    file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))

    if file_mtime.date() == yesterday:
        print(filename)
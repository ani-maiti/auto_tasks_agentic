import datetime
import os

today = datetime.date.today()
one_year_ago = today - datetime.timedelta(days=365)

for filename in os.listdir("."):
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date()
        if file_mtime < one_year_ago:
            print(filename)
```
execution trace:
stdout:


stderr:


return code: 0
import os
import re

for filename in os.listdir("."):
    if re.search(r"\d{4}-\d{2}-\d{2}", filename):
        print(filename)
```
execution trace:
stdout:
task_descriptions_all.txt
task_descriptions.txt


stderr:


return code: 0
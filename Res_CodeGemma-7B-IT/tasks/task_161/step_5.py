import os

for dirpath, dirnames, filenames in os.walk("."):
    if len(filenames) > 100:
        print(dirpath)
```
execution trace:
stdout:


stderr:
Traceback (most recent call last):
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_161/step_5.py", line 4, in <module>
    for dirpath, dirnames, filenames in os.walk("."):
NameError: name 'os' is not defined


return code: 1
# Print the size of each file
for filename in large_files:
    print(filename, os.path.getsize(filename))
```
execution trace:
stdout:


stderr:
Traceback (most recent call last):
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_035/step_3.py", line 2, in <module>
    for filename in large_files:
NameError: name 'large_files' is not defined


return code: 1
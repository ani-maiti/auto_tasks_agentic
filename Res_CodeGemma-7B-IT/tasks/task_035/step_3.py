# Define large_files in the first code block
large_files = []
for filename in os.listdir():
    if os.path.isfile(filename) and os.path.getsize(filename) > average_size:
        large_files.append(filename)

# Print the size of each file
for filename in large_files:
    print(filename, os.path.getsize(filename))
```
execution trace:
stdout:
task_descriptions_all.txt 364
generate_code_model_run.py 100384
generate_code_model_run (copy).py 100384


stderr:


return code: 0
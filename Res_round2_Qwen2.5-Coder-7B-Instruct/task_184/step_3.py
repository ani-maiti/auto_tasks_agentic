import json

files = [
    "tep_1_log.json",
    "./tasks/task_037/step_3_log.json",
    # ... add all other file paths here ...
]

for file_path in files:
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        print(f"{file_path} is valid JSON")
    except json.JSONDecodeError:
        print(f"{file_path} is NOT valid JSON")
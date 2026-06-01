import os

def count_functions_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    function_count = sum(1 for line in lines if line.strip().startswith('def '))
    return function_count

files = [
    './generate_code_model_run.py',
    './tasks/task_023/step_2.py',
    './tasks/task_032/step_2.py',
    './tasks/task_046/step_2.py',
    './tasks/task_041/step_2.py',
    './tasks/task_009/step_2.py',
    './tasks/task_025/step_3.py',
    './tasks/task_025/step_2.py',
    './test.py',
    './generate_code_model_run1.py'
]

total_functions = sum(count_functions_in_file(file) for file in files)
print(f"Total number of functions: {total_functions}")
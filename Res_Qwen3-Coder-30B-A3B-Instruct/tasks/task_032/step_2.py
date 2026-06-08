import hashlib
import os

def compute_md5(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return str(e)

# Get list of Python files
python_files = [
    "./generate_code_model_run.py",
    "./tasks/task_023/step_5.py",
    "./tasks/task_023/step_2.py",
    "./tasks/task_013/step_3.py",
    "./tasks/task_017/step_3.py",
    "./tasks/task_003/step_3.py",
    "./tasks/task_009/step_2.py",
    "./tasks/task_010/step_3.py",
    "./tasks/task_031/step_2.py",
    "./tasks/task_016/step_2.py",
    "./tasks/task_025/step_3.py",
    "./tasks/task_025/step_1.py",
    "./tasks/task_025/step_2.py",
    "./tasks/task_025/step_4.py",
    "./tasks/task_011/step_3.py",
    "./tasks/task_011/step_2.py"
]

# Compute and print MD5 hashes
for file_path in python_files:
    md5_hash = compute_md5(file_path)
    print(f"{md5_hash}  {file_path}")
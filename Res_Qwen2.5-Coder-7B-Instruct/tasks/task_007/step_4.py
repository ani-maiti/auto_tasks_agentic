import os

def find_deepest_directory(path):
    max_depth = 0
    deepest_dir = None
    
    for root, dirs, files in os.walk(path):
        current_depth = root[len(path):].count(os.sep)
        if current_depth > max_depth:
            max_depth = current_depth
            deepest_dir = root
            
    return deepest_dir

deepest_path = find_deepest_directory('./tasks/task_007/subdir')
print(deepest_path)
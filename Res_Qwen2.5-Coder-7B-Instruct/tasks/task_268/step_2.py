import json
from collections import defaultdict
import numpy as np

# Dictionary to store numeric fields and their values
numeric_fields = defaultdict(list)

# Function to extract numeric fields from a JSON file
def extract_numeric_fields(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for key, value in data.items():
            if isinstance(value, (int, float)):
                numeric_fields[key].append(value)
            elif isinstance(value, dict):
                extract_numeric_fields(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, (int, float)):
                        numeric_fields[key].append(item)
                    elif isinstance(item, dict):
                        extract_numeric_fields(item)

# Iterate over all found JSON files and extract numeric fields
for file_path in ['26/step_2_log.json', './tasks/task_126/step_3_log.json', './tasks/task_089/step_1_log.json', './tasks/task_089/step_2_log.json', './tasks/task_089/step_3_log.json', './tasks/task_191/step_5_log.json', './tasks/task_191/step_1_log.json', './tasks/task_191/step_4_log.json', './tasks/task_191/step_2_log.json', './tasks/task_191/step_3_log.json', './tasks/task_005/step_1_log.json', './tasks/task_005/step_4_log.json', './tasks/task_005/step_2_log.json', './tasks/task_005/step_3_log.json', './tasks/task_026/step_5_log.json', './tasks/task_026/step_1_log.json', './tasks/task_026/step_4_log.json', './tasks/task_026/step_2_log.json', './tasks/task_026/step_3_log.json', './tasks/task_131/step_1_log.json', './tasks/task_131/step_2_log.json', './tasks/task_131/step_3_log.json', './tasks/task_028/step_1_log.json', './tasks/task_028/step_4_log.json', './tasks/task_028/step_2_log.json', './tasks/task_028/step_3_log.json', './tasks/task_021/step_1_log.json', './tasks/task_021/step_2_log.json', './tasks/task_021/step_3_log.json', './tasks/task_242/step_1_log.json', './tasks/task_242/step_4_log.json', './tasks/task_242/step_2_log.json', './tasks/task_242/step_3_log.json', './tasks/task_240/step_1_log.json', './tasks/task_240/step_2_log.json', './tasks/task_256/step_1_log.json', './tasks/task_256/step_4_log.json', './tasks/task_256/step_2_log.json', './tasks/task_256/step_3_log.json', './tasks/task_189/step_1_log.json', './tasks/task_189/step_2_log.json', './tasks/task_189/step_3_log.json', './tasks/task_150/step_1_log.json', './tasks/task_150/step_4_log.json', './tasks/task_150/step_2_log.json', './tasks/task_150/step_3_log.json', './tasks/task_022/step_1_log.json', './tasks/task_022/step_2_log.json', './tasks/task_022/step_3_log.json', './tasks/task_251/step_1_log.json', './tasks/task_251/step_4_log.json', './tasks/task_251/step_2_log.json', './tasks/task_251/step_3_log.json', './tasks/task_267/step_5_log.json', './tasks/task_267/step_1_log.json', './tasks/task_267/step_4_log.json', './tasks/task_267/step_2_log.json', './tasks/task_267/step_3_log.json', './tasks/task_243/step_1_log.json', './tasks/task_128/step_1_log.json', './tasks/task_128/step_4_log.json', './tasks/task_1
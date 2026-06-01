import os
import json
import yaml
import configparser
import toml

config_files = [
    f for f in os.popen("find . \( -name '*.json' -o -name '*.yaml' -o -name '*.ini' -o -name '*.toml' \)").read().strip().split('\n')
]

keys_dict = {}

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        extract_keys(data, file_path)

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        extract_keys(data, file_path)

def read_ini(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    for section in config.sections():
        for key in config[section]:
            add_key(f"{section}.{key}", file_path)

def read_toml(file_path):
    with open(file_path, 'r') as file:
        data = toml.load(file)
        extract_keys(data, file_path)

def extract_keys(data, file_path, parent_key=''):
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            add_key(new_key, file_path)
            extract_keys(v, file_path, new_key)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            extract_keys(item, file_path, new_key)

def add_key(key, file_path):
    if key not in keys_dict:
        keys_dict[key] = set()
    keys_dict[key].add(file_path)

for file in config_files:
    try:
        if file.endswith('.json'):
            read_json(file)
        elif file.endswith('.yaml') or file.endswith('.yml'):
            read_yaml(file)
        elif file.endswith('.ini'):
            read_ini(file)
        elif file.endswith('.toml'):
            read_toml(file)
    except Exception as e:
        print(f"Error reading {file}: {e}")

common_keys = {k: v for k, v in keys_dict.items() if len(v) > 1}

with open('common_keys_report.csv', 'w') as f:
    f.write("Key,Files\n")
    for key, files in common_keys.items():
        f.write(f"{key},{','.join(files)}\n")

print("Report generated: common_keys_report.csv")
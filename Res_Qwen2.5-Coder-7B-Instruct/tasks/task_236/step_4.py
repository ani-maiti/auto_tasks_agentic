import json
from difflib import Differ

def compare_json_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    differ = Differ()
    diff = list(differ.compare(json.dumps(data1, indent=4).splitlines(), json.dumps(data2, indent=4).splitlines()))
    return '\n'.join(diff)

# Example usage:
# result = compare_json_files('./path/to/file1.json', './path/to/file2.json')
# print(result)
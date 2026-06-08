import json

with open('cross_reference_report.json', 'r') as f:
    report = json.load(f)

print(f"Total shared values: {report['total_shared_values']}")
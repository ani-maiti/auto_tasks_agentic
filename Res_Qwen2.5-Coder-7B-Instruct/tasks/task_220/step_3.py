import json

module_counts = {module: imported_modules.count(module) for module in imported_modules}
sorted_module_counts = sorted(module_counts.items(), key=lambda x: x[1], reverse=True)

with open('module_frequency.json', 'w') as f:
    json.dump(sorted_module_counts, f, indent=4)

top_10_modules = sorted_module_counts[:10]

print(top_10_modules)
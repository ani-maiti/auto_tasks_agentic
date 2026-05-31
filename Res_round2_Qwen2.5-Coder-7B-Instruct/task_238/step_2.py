import json
from collections import defaultdict

call_graph = defaultdict(list)
function_counts = defaultdict(int)

with open('python_files.txt', 'r') as f:
    for file_path in f.readlines():
        file_path = file_path.strip()
        with open(file_path, 'r') as file:
            lines = file.readlines()

        current_function = None
        for line in lines:
            if line.startswith('def '):
                current_function = line.split()[1].split('(')[0]
                function_counts[current_function] += 1
            elif current_function and line.strip().startswith('    '):
                call_graph[current_function].append(line.strip())

# Save the call graph to JSON
with open('call_graph.json', 'w') as f:
    json.dump(call_graph, f, indent=4)

# Print the most frequently called function
most_frequently_called = max(function_counts.items(), key=lambda x: x[1])
print(f"The most frequently called function is '{most_frequently_called[0]}' with {most_frequently_called[1]} calls.")
import os
import re

count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
                # Count occurrences of "import" as a whole word
                matches = re.findall(r'\bimport\b', content)
                count += len(matches)

print(count)
import os
import re
from collections import defaultdict
import csv

# Create a sample directory structure for testing
os.makedirs('/tmp/test_logs', exist_ok=True)
with open('/tmp/test_logs/app1.log', 'w') as f:
    f.write('2023-01-01 12:30:45 INFO message1\n2023-01-01 13:45:22 ERROR message2\n')
with open('/tmp/test_logs/app2.log', 'w') as f:
    f.write('Jan 01 12:30:45 host1 app2: INFO message3\nJan 01 13:45:22 host1 app2: ERROR message4\n')
with open('/tmp/test_logs/app3.log', 'w') as f:
    f.write('[01/01/2023 12:30:45] INFO message5\n[01/01/2023 13:45:22] ERROR message6\n')

# Find all log files
log_files = []
for root, dirs, files in os.walk('/tmp/test_logs'):
    for file in files:
        if file.endswith('.log'):
            log_files.append(os.path.join(root, file))

print(f"Found {len(log_files)} log files")
for f in log_files:
    print(f)
```
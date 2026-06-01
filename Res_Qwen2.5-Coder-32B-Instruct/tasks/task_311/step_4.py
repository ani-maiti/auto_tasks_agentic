import re
from datetime import datetime

log_files = ['/var/log/Xorg.0.log', '/var/log/pacman.log', '/var/log/pacman.PackageKit.log']
events = []

for file in log_files:
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r'\[(\d+\.\d+)\]', line)
            if match:
                timestamp = float(match.group(1))
                event_time = datetime.fromtimestamp(timestamp)
                events.append((event_time, file, line.strip()))

events.sort()

with open('timeline.csv', 'w') as f:
    f.write('Timestamp,File,Event\n')
    for event in events:
        f.write(f'{event[0]},{event[1]},{event[2]}\n')

print("Timeline saved to timeline.csv")
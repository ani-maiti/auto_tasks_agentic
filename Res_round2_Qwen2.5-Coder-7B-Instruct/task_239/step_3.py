import pandas as pd

timestamps = []
with open('timestamps.txt', 'r') as file:
    for line in file:
        count, timestamp = line.strip().split()
        timestamps.append({'count': int(count), 'timestamp': timestamp})

df = pd.DataFrame(timestamps)
df.to_csv('timestamp_stats.csv', index=False)
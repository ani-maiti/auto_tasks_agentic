import os
import datetime

# Get the current directory
cwd = os.getcwd()

# Find all log files in the current directory tree
log_files = [f for f in os.listdir(cwd) if f.endswith('.log')]

# Initialize variables for timestamp formats, error patterns, and activity statistics
timestamp_formats = []
error_patterns = {}
hourly_activity = {}

# Iterate over log files
for log_file in log_files:
    # Read the log file
    with open(log_file, 'r') as f:
        for line in f:
            # Extract timestamp and error message
            timestamp, message = line.split(':', 1)

            # Identify timestamp formats
            try:
                datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
                timestamp_formats.append('%Y-%m-%d %H:%M:%S.%f')
            except ValueError:
                try:
                    datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                    timestamp_formats.append('%Y-%m-%d %H:%M:%S')
                except ValueError:
                    # Unknown timestamp format
                    pass

            # Detect recurring error patterns
            if 'error' in message.lower():
                error_patterns.setdefault(message, 0)
                error_patterns[message] += 1

            # Build hourly activity statistics
            hour = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').hour
            hourly_activity.setdefault(hour, 0)
            hourly_activity[hour] += 1

# Save results to CSV
with open('log_analysis.csv', 'w') as f:
    f.write('Timestamp Format,Error Message,Count\n')
    for format in timestamp_formats:
        f.write(f'{format},{format},{timestamp_formats.count(format)}\n')
    for message, count in error_patterns.items():
        f.write(f'N/A,{message},{count}\n')
    for hour, count in hourly_activity.items():
        f.write(f'N/A,Hour {hour},{count}\n')

# Generate report
print('Log Analysis Report:')
print('Timestamp Formats:')
for format in timestamp_formats:
    print(f'- {format}')
print('\nError Patterns:')
for message, count in error_patterns.items():
    print(f'- {message}: {count}')
print('\nHourly Activity:')
for hour, count in hourly_activity.items():
    print(f'- Hour {hour}: {count}')

# Print most common error pattern
most_common_error = max(error_patterns, key=error_patterns.get)
print(f'\nMost Common Error Pattern: {most_common_error}')
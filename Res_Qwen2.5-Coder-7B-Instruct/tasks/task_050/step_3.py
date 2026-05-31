import json
trace = json.loads(open('trace.json').read())
print(f"Total disk usage of the current directory: {trace['stdout'].strip()}")
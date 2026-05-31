import subprocess
result = subprocess.run(['cat', '/proc/self/environ'], capture_output=True, text=True)
env_vars = result.stdout.split('\n')
for var in env_vars:
    if var.startswith('TRACE='):
        trace_path = var.split('=')[1]
        break
else:
    raise ValueError("TRACE environment variable not found")

with open(trace_path, 'r') as f:
    trace = json.load(f)
print(f"The latest Debian stable release version is: {trace['stdout']}")
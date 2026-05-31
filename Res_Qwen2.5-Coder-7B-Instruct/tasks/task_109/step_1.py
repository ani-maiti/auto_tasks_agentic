import subprocess

# Use dig command to query MX records for outlook.com
result = subprocess.run(['dig', '+short', 'MX', 'outlook.com'], capture_output=True, text=True)

# Print the result
print(result.stdout)
```

This code uses the `subprocess` module to run the `dig` command with the appropriate arguments to fetch the MX records for `outlook.com`. The results are captured and printed.
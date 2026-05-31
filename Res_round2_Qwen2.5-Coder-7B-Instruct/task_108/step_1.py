import subprocess

# Use dig command to query MX records for gmail.com
dig_command = "dig +short mx gmail.com"
result = subprocess.run(dig_command, shell=True, capture_output=True, text=True)

# Print the result
print(result.stdout)
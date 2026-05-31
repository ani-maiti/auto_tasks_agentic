import subprocess

result = subprocess.run(['git', 'ls-remote', '--tags', 'https://github.com/cli/cli.git'], capture_output=True, text=True)
stdout = result.stdout.strip()
print("Latest release tag:", stdout.split()[1])
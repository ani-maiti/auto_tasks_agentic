import subprocess

result = subprocess.run(['git', 'ls-remote', '--tags', 'https://github.com/cli/cli.git'], capture_output=True, text=True)
latest_tag = result.stdout.strip().split('\n')[-1].split()[1]
print(f"Latest release tag: {latest_tag}")
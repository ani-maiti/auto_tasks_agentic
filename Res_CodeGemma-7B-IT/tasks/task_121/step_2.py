import subprocess

cmd = ["tmux", "-V"]
output = subprocess.run(cmd, capture_output=True, text=True)

if output.returncode == 0:
    current_version = output.stdout.strip()
    if current_version != version:
        print(f"Installing tmux {version}")
        # Install tmux using the appropriate package manager
    else:
        print(f"tmux {version} is already installed")
else:
    print("Error checking tmux version")
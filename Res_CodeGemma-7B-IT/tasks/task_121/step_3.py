cmd = ["curl", "https://api.github.com/repos/tmux/tmux/releases/latest"]
response = subprocess.run(cmd, capture_output=True, text=True)

if response.status_code == 200:
    release_data = response.json()
    version = release_data["tag_name"]
    print(f"Latest tmux release: {version}")
else:
    print("Error fetching release data")
```
execution trace:
stdout:
Latest tmux release: 3.6b


stderr:


return code: 0
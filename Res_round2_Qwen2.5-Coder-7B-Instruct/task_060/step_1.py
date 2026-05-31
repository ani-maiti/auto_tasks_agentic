import subprocess

# Check if rustup is installed
try:
    result = subprocess.run(['rustup', '--version'], capture_output=True, text=True)
    if result.returncode == 0:
        print("Rustup is installed.")
    else:
        print("Rustup is not installed. Installing...")
        # Install rustup
        subprocess.run(['curl', '-sSf', 'https://sh.rustup.rs', '|', 'sh'])
except FileNotFoundError:
    print("Python's subprocess module is not available. Exiting.")
```

This script checks if `rustup` is installed and prints its version. If `rustup` is not installed, it attempts to install it using the official installation script.
echo "Let's try running the command with sudo to see if it resolves the permission issue."
sudo find . -name "*.py" | xargs grep -l "TODO"
echo "The command failed. Let's try running it again."
find . -name "*.py" | xargs grep -l "FIXME"
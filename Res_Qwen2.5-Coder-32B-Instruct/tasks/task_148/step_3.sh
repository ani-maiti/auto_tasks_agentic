echo "List of Python files containing FIXME comments:"
cat $(grep -rl "FIXME" . --include=*.py)
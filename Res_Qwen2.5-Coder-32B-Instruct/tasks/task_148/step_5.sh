echo "Task completed. List of Python files containing FIXME comments and their respective FIXME lines:"
grep -rl "FIXME" . --include=*.py | xargs grep -H "FIXME"
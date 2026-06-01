echo "List of Python files containing FIXME comments:"
grep -rl "FIXME" . --include=*.py | xargs grep -H "FIXME"
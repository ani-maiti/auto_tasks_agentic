echo "Found Python files importing requests:"
grep -l "import requests" $(find . -name "*.py")
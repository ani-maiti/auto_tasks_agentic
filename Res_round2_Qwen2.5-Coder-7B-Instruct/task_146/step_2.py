print("All Python files that import requests:")
for file in open('imports_requests.txt', 'r').read().splitlines():
    print(file)
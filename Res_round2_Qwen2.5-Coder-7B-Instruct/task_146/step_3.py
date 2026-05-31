with open('imports_requests.txt', 'w') as f:
    for file in open('imports_requests.txt', 'r').read().splitlines():
        if 'import requests' in open(file, 'r').read():
            f.write(file + '\n')